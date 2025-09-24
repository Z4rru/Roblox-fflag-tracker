#!/usr/bin/env python3
import os
import subprocess
import datetime
import json
import html
import shutil
import sys
import argparse
from pathlib import Path
from zoneinfo import ZoneInfo
import asyncio
import logging
import time
import random
import re
from collections import defaultdict
from filelock import FileLock

try:
    from jsonschema import validate as json_validate, ValidationError
except ImportError:
    print("Warning: jsonschema not installed. Install via `pip install jsonschema`.")
    json_validate = None
    ValidationError = Exception

try:
    from openai import AsyncOpenAI, RateLimitError
except ImportError:
    AsyncOpenAI = None
try:
    import google.generativeai as genai
except ImportError:
    genai = None

# ============================
# Settings and Paths
# ============================
SCRIPT_DIR = Path(__file__).resolve().parent
WORKSPACE = Path(os.getenv("GITHUB_WORKSPACE", str(SCRIPT_DIR))).resolve()
OUTPUT_DIR = WORKSPACE / "output"
OUTPUT_MD = OUTPUT_DIR / "FFlag_Report.md"
OUTPUT_HTML = OUTPUT_DIR / "FFlag_Report.html"
OUTPUT_JSON = OUTPUT_DIR / "FFlag_Report.json"
CACHE_FILE = OUTPUT_DIR / "fflag_cache.json"
DIFF_CACHE_FILE = OUTPUT_DIR / "diff_cache.json"
HISTORY_FILE = OUTPUT_DIR / "history.json"
KEY_INDEX_FILE = OUTPUT_DIR / ".key_index.json"
REPO_URL = "https://github.com/MaximumADHD/Roblox-FFlag-Tracker.git"
TARGET_FILE = "PCDesktopClient.json"
DAYS = 30
HISTORY_DAYS = 90
AI_BATCH_SIZE = 5
AI_BATCH_DELAY = 2.0
MAX_RETRIES = 3
MAX_REPORT_COMMITS = 50
COMMIT_BATCH_SIZE = 10
DEBUG = True
SUBPROCESS_TIMEOUT = 120
MAX_CONCURRENT_AI_REQUESTS = 3  # Limit concurrent AI requests

# ============================
# Command-Line Arguments
# ============================
parser = argparse.ArgumentParser(description="Roblox FFlag Tracker")
parser.add_argument("--dry-run", action="store_true", help="Run without AI enrichment")
args = parser.parse_args()

# ============================
# Logging Utility
# ============================
logging.basicConfig(level=logging.INFO if not DEBUG else logging.DEBUG, format="[%(levelname)s] %(message)s (%(asctime)s)")
log = logging.getLogger(__name__)

# ============================
# API Key Management
# ============================
def load_api_keys(env_var: str) -> list[str]:
    keys_raw = os.getenv(env_var, "")
    keys = [k.strip() for k in keys_raw.split(",") if k.strip()]
    if not keys:
        log.warning(f"⚠ No {env_var} found.")
    return keys

OPENAI_KEYS = load_api_keys("OPENAI_API_KEYS")
GEMINI_KEYS = load_api_keys("GEMINI_API_KEYS")
if not OPENAI_KEYS and not GEMINI_KEYS and not args.dry_run:
    log.warning("⚠ No API keys found. AI enrichment will be skipped.")

def get_next_api_key(service: str) -> str | None:
    keys = OPENAI_KEYS if service == "openai" else GEMINI_KEYS
    if not keys:
        return None
    lock = FileLock(str(KEY_INDEX_FILE) + ".lock", timeout=10)
    with lock:
        index_data = {"openai_idx": 0, "gemini_idx": 0}
        if KEY_INDEX_FILE.exists():
            try:
                index_data = json.loads(KEY_INDEX_FILE.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                log.warning(f"Corrupted {KEY_INDEX_FILE}. Resetting indices.")
        idx = index_data.get(f"{service}_idx", 0)
        key = keys[idx % len(keys)]
        index_data[f"{service}_idx"] = idx + 1
        KEY_INDEX_FILE.write_text(json.dumps(index_data, indent=2), encoding="utf-8")
    display_key = f"{key[:4]}...{key[-4:]}" if len(key) > 8 else "****"
    log.debug(f"Using {service} API key #{idx % len(keys) + 1} ({display_key})")
    return key

# ============================
# FFlags Categories
# ============================
CATEGORIES = {
    "Graphics": ["Graphics", "Lighting", "Render", "GPU", "VSync", "Shadow", "Texture"],
    "Physics": ["Physics", "Solver", "Collision", "Humanoid", "Constraint", "Ragdoll"],
    "Network": ["Network", "Replication", "Packet", "Ping", "Server", "Client"],
    "Camera/UI": ["Camera", "Mouse", "Input", "FOV", "ShiftLock", "UI", "Menu", "Cursor"],
    "Security": ["Exploit", "AntiCheat", "Safe", "Encryption", "Bypass"],
    "World": ["Terrain", "World", "Map", "Environment", "Ocean", "Sky"],
    "Input": ["Input", "Keyboard", "Mouse", "Controller", "Touch", "Gamepad"],
    "Hit": ["Hit", "Damage", "Projectile", "Bullet", "CollisionDetection"],
    "Interpolation": ["Interp", "Interpolation", "Tween", "Smooth", "Extrapolate"],
    "Body": ["Body", "Ragdoll", "Torso", "Limb", "Character"],
    "Other": []
}

# ============================
# Utility Functions
# ============================
def run_cmd(cmd: str, cwd: Path | None = None) -> str:
    try:
        result = subprocess.run(
            cmd, shell=True, cwd=cwd, capture_output=True, text=True, timeout=SUBPROCESS_TIMEOUT
        )
        if result.returncode != 0:
            log.error(f"Command failed (return code {result.returncode}): {cmd}")
            log.error(result.stderr.strip())
            raise subprocess.CalledProcessError(result.returncode, cmd, output=result.stdout, stderr=result.stderr)
        return result.stdout.strip()
    except subprocess.TimeoutExpired:
        log.error(f"Command timed out after {SUBPROCESS_TIMEOUT} seconds: {cmd}")
        raise
    except Exception as e:
        log.error(f"Cmd error: {e}")
        raise

def categorize_flag(flag_name: str) -> str:
    if not isinstance(flag_name, str):
        return "Other"
    lower = flag_name.lower()
    for cat, keywords in CATEGORIES.items():
        if any(k.lower() in lower for k in keywords):
            return cat
    return "Other"

def format_value(v: any) -> str:
    if isinstance(v, bool):
        return str(v).capitalize()
    return str(v)

cache_path = Path(os.environ.get("FFLAG_REPO_CACHE", ".fflag-repo-cache"))

def ensure_manifest_repo(repo_url: str = REPO_URL) -> Path:
    if not re.match(r"^https://github\.com/[A-Za-z0-9_-]+/[A-Za-z0-9_-]+\.git$", repo_url):
        raise ValueError(f"Invalid repository URL: {repo_url}")
    if cache_path.exists() and (cache_path / ".git").exists():
        log.info(f"Using cached manifest repo at {cache_path}")
        try:
            if not (cache_path / TARGET_FILE).exists():
                raise FileNotFoundError(f"{TARGET_FILE} not found in repo")
            subprocess.run(["git", "-C", str(cache_path), "stash", "save", "--include-untracked"], check=True)
            subprocess.run(["git", "-C", str(cache_path), "pull", "--ff-only"], check=True)
            subprocess.run(["git", "-C", str(cache_path), "stash", "pop"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            return cache_path
        except (subprocess.CalledProcessError, FileNotFoundError):
            log.warning("Cached repo pull or file check failed, recloning...")
            shutil.rmtree(cache_path, ignore_errors=True)
    log.info("Cloning fresh manifest repo...")
    subprocess.run(["git", "clone", repo_url, str(cache_path)], check=True)
    if not (cache_path / TARGET_FILE).exists():
        raise FileNotFoundError(f"{TARGET_FILE} not found in cloned repo")
    return cache_path

def get_commits(days: int = DAYS, manifest_repo: Path | None = None) -> list[str]:
    since = (datetime.datetime.now() - datetime.timedelta(days=days)).strftime("%Y-%m-%d")
    commits = run_cmd(f"git log --since='{since}' --pretty=format:%H -- {TARGET_FILE}", cwd=manifest_repo)
    return commits.splitlines()[:MAX_REPORT_COMMITS] if commits else []

# ============================
# Diff Utilities
# ============================
def build_diff_for_commit_old(commit_hash: str, manifest_repo: Path | None = None) -> tuple[str, list[tuple[str, any]], list[tuple[str, any, any]], list[tuple[str, any]]]:
    header = run_cmd(f"git show --no-patch --pretty=format:'%h - %ci - %s' {commit_hash}", cwd=manifest_repo)
    diff = run_cmd(f"git show {commit_hash} -- {TARGET_FILE}", cwd=manifest_repo)
    try:
        prev_content = run_cmd(f"git show {commit_hash}~1:{TARGET_FILE}", cwd=manifest_repo)
        curr_content = run_cmd(f"git show {commit_hash}:{TARGET_FILE}", cwd=manifest_repo)
        prev_json = json.loads(prev_content) if prev_content else {}
        curr_json = json.loads(curr_content)
        added = [(k, v) for k, v in curr_json.items() if k not in prev_json]
        changed = [(k, prev_json[k], curr_json[k]) for k in curr_json if k in prev_json and curr_json[k] != prev_json[k]]
        removed = [(k, v) for k, v in prev_json.items() if k not in curr_json]
        return header, added, changed, removed
    except (json.JSONDecodeError, subprocess.CalledProcessError):
        log.debug("Falling back to line-by-line diff parsing")
        added_dict = {}
        removed_dict = {}
        for line in diff.splitlines():
            if line.startswith("+") and not line.startswith("+++"):
                l = line[1:].strip()
                if l.startswith('"') and ":" in l:
                    try:
                        if l.endswith(","):
                            l = l[:-1]
                        d = json.loads("{" + l + "}")
                        for k, v in d.items():
                            added_dict[k] = v
                    except Exception as e:
                        log.debug(f"Failed to parse added line: {l} {e}")
            elif line.startswith("-") and not line.startswith("---"):
                l = line[1:].strip()
                if l.startswith('"') and ":" in l:
                    try:
                        if l.endswith(","):
                            l = l[:-1]
                        d = json.loads("{" + l + "}")
                        for k, v in d.items():
                            removed_dict[k] = v
                    except Exception as e:
                        log.debug(f"Failed to parse removed line: {l} {e}")
        added = [(k, v) for k, v in added_dict.items() if k not in removed_dict]
        changed = [(k, removed_dict[k], added_dict[k]) for k in added_dict if k in removed_dict]
        removed = [(k, v) for k, v in removed_dict.items() if k not in added_dict]
        return header, added, changed, removed

async def async_build_diff_for_commit(commit_hash: str, diff_cache: dict, manifest_repo: Path | None = None) -> tuple[str, list[tuple[str, any]], list[tuple[str, any, any]], list[tuple[str, any]]]:
    if commit_hash in diff_cache:
        cached = diff_cache[commit_hash]
        added = [(f, v) for f, v in cached.get('added', [])]
        changed = [(f, o, n) for f, o, n in cached.get('changed', [])]
        removed = [(f, v) for f, v in cached.get('removed', [])]
        return cached['header'], added, changed, removed
    header, added, changed, removed = await asyncio.get_running_loop().run_in_executor(None, lambda: build_diff_for_commit_old(commit_hash, manifest_repo))
    diff_cache[commit_hash] = {
        'header': header,
        'added': [[f, v] for f, v in added],
        'changed': [[f, o, n] for f, o, n in changed],
        'removed': [[f, v] for f, v in removed]
    }
    return header, added, changed, removed

async def build_report(commits: list[str], diff_cache: dict, manifest_repo: Path | None = None) -> tuple[list, dict, dict]:
    report = []
    summary = {}
    flag_changes = defaultdict(int)
    for i in range(0, len(commits), COMMIT_BATCH_SIZE):
        batch = commits[i:i + COMMIT_BATCH_SIZE]
        tasks = [async_build_diff_for_commit(c, diff_cache, manifest_repo) for c in batch]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        for result in results:
            if isinstance(result, Exception):
                log.error(f"Diff failed: {result}")
                continue
            header, added, changed, removed = result
            changes = []
            for flag, value in added:
                cat = categorize_flag(flag)
                changes.append(("Added", cat, flag, value))
                summary[(cat, "Added")] = summary.get((cat, "Added"), 0) + 1
                flag_changes[flag] += 1
            for flag, old, new in changed:
                cat = categorize_flag(flag)
                changes.append(("Changed", cat, flag, old, new))
                summary[(cat, "Changed")] = summary.get((cat, "Changed"), 0) + 1
                flag_changes[flag] += 1
            for flag, value in removed:
                cat = categorize_flag(flag)
                changes.append(("Removed", cat, flag, value))
                summary[(cat, "Removed")] = summary.get((cat, "Removed"), 0) + 1
                flag_changes[flag] += 1
            if changes:
                report.append((header, changes))
    return report, summary, flag_changes

# ============================
# History Management
# ============================
def update_history(added: int, changed: int, removed: int, last_run: str) -> None:
    history = []
    if HISTORY_FILE.exists():
        try:
            history = json.loads(HISTORY_FILE.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            log.warning("Corrupted history file. Starting new history.")
    current_date = last_run.split(' ')[0]
    if history and history[-1]['date'].split(' ')[0] == current_date:
        last_entry = history[-1]
        last_entry['added'] = (last_entry['added'] + added) / 2
        last_entry['changed'] = (last_entry['changed'] + changed) / 2
        last_entry['removed'] = (last_entry['removed'] + removed) / 2
        last_entry['date'] = last_run
    else:
        history.append({"date": last_run, "added": added, "changed": changed, "removed": removed})
    history = history[-HISTORY_DAYS:]
    HISTORY_FILE.write_text(json.dumps(history, indent=2), encoding="utf-8")

# ============================
# AI Enrichment
# ============================
try:
    FLAG_INFO = json.loads(CACHE_FILE.read_text(encoding="utf-8")) if CACHE_FILE.exists() else {}
except json.JSONDecodeError:
    log.warning("Corrupted fflag_cache.json. Using empty cache.")
    FLAG_INFO = {}

FLAG_SCHEMA = {
    "type": "object",
    "patternProperties": {
        "^(FFlag|DFFlag|DFInt|DFLog|SFFlag|FString|FInt|DFString)[A-Za-z0-9_]+$": {
            "type": "object",
            "properties": {
                "mechanism": {"type": "string"},
                "purpose": {"type": "string"}
            },
            "required": ["mechanism", "purpose"]
        }
    },
    "additionalProperties": False
}

def extract_and_validate_json(text: str) -> dict:
    match = re.search(r"(\{(?:.|\n)*?\})", text, re.DOTALL)
    if not match:
        raise json.JSONDecodeError("No valid JSON object found", text, 0)
    try:
        data = json.loads(match.group(0))
    except json.JSONDecodeError as e:
        log.error(f"Failed to parse JSON: {e}")
        raise
    if json_validate:
        try:
            json_validate(instance=data, schema=FLAG_SCHEMA)
        except ValidationError as ve:
            log.warning(f"Schema issue: {ve}. Filtering invalid keys.")
            data = {k: v for k, v in data.items() if re.match(r"^(FFlag|DFFlag|DFInt|DFLog|SFFlag|FString|FInt|DFString)[A-Za-z0-9_]+$", k)}
    return data

async def ai_enrich_flags_batch(batch: list[str], use_gemini: bool = False, semaphore: asyncio.Semaphore = None) -> dict:
    async with semaphore:
        if args.dry_run:
            log.info("Dry run: Skipping AI enrichment")
            return {f: {"mechanism": "N/A (dry run)", "purpose": "N/A (dry run)"} for f in batch}
        system_prompt = "You are a JSON generator. Always output valid JSON only."
        user_prompt = (
            "Explain these Roblox FFlags in simple layman's terms. "
            "For each flag, return a JSON object with:\n"
            "- mechanism: how it technically works (short)\n"
            "- purpose: what benefit or change it brings for Roblox players.\n\n"
            f"Flags: {json.dumps(batch)}"
        )
        loop = asyncio.get_running_loop()
        if not use_gemini:
            if not OPENAI_KEYS or not AsyncOpenAI:
                if GEMINI_KEYS and genai:
                    log.info("No OpenAI available. Falling back to Gemini.")
                    return await ai_enrich_flags_batch(batch, use_gemini=True, semaphore=semaphore)
                log.error("No OpenAI API keys or client available.")
                return {f: {"mechanism": "N/A (no OpenAI)", "purpose": "N/A (no OpenAI)"} for f in batch}
            temp_system_prompt = system_prompt
            for attempt in range(MAX_RETRIES):
                try:
                    client = AsyncOpenAI(api_key=get_next_api_key("openai"))
                    response = await client.chat.completions.create(
                        model="gpt-4o-mini",
                        messages=[
                            {"role": "system", "content": temp_system_prompt},
                            {"role": "user", "content": user_prompt}
                        ],
                        temperature=0.3
                    )
                    text = response.choices[0].message.content.strip()
                    return extract_and_validate_json(text)
                except RateLimitError as e:
                    if e.response and e.response.headers.get('x-ratelimit-remaining-requests') == '0':
                        if GEMINI_KEYS and genai:
                            log.info("OpenAI request limit reached. Falling back to Gemini.")
                            return await ai_enrich_flags_batch(batch, use_gemini=True, semaphore=semaphore)
                        log.error("OpenAI request limit reached, no Gemini fallback.")
                        return {f: {"mechanism": "N/A (rate limit)", "purpose": "N/A (rate limit)"} for f in batch}
                    sleep_time = 2 ** attempt
                    if hasattr(e, 'response') and e.response:
                        retry_after = e.response.headers.get('Retry-After')
                        if retry_after and retry_after.isdigit():
                            sleep_time = int(retry_after) + 1
                    log.warning(f"OpenAI rate limit hit on attempt {attempt+1}. Sleeping for {sleep_time}s.")
                    await asyncio.sleep(sleep_time)
                    continue
                except json.JSONDecodeError as je:
                    log.error(f"Failed to parse OpenAI response: {je}")
                    temp_system_prompt += " Respond strictly in JSON only, no extra text."
                    await asyncio.sleep(1)
                    continue
                except Exception as e:
                    log.error(f"OpenAI batch failed (attempt {attempt+1}): {e}")
                    await asyncio.sleep(2 ** attempt)
                    continue
            if GEMINI_KEYS and genai:
                log.info("Falling back to Gemini after OpenAI retries.")
                return await ai_enrich_flags_batch(batch, use_gemini=True, semaphore=semaphore)
            log.error("Failed to enrich batch after max retries with OpenAI.")
            return {f: {"mechanism": "N/A (retry failed)", "purpose": "N/A (retry failed)"} for f in batch}
        else:
            if not GEMINI_KEYS or not genai:
                log.error("No Gemini available.")
                return {f: {"mechanism": "N/A (no Gemini)", "purpose": "N/A (no Gemini)"} for f in batch}
            genai.configure(api_key=get_next_api_key("gemini"))
            model = genai.GenerativeModel("gemini-1.5-flash")
            prompt = system_prompt + "\n" + user_prompt + "\nRespond with only the valid JSON object, nothing else."
            try:
                async def sync_generate_with_timeout():
                    return await asyncio.wait_for(loop.run_in_executor(None, lambda: model.generate_content(prompt).text.strip()), timeout=30)
                text = await sync_generate_with_timeout()
                return extract_and_validate_json(text)
            except Exception as e:
                log.warning(f"Gemini enrichment failed, skipping batch: {e}")
                return {f: {"mechanism": "N/A (Gemini skipped)", "purpose": "N/A (Gemini skipped)"} for f in batch}

def should_enrich_flag(flag: str) -> bool:
    if args.dry_run:
        return False
    if flag not in FLAG_INFO:
        return True
    mechanism = FLAG_INFO[flag].get("mechanism", "")
    return mechanism.startswith("N/A")

async def generate_flag_info_batch(flags: list[str]) -> None:
    new_flags = [f for f in flags if should_enrich_flag(f)]
    if not new_flags:
        return
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    batches = [new_flags[i:i + AI_BATCH_SIZE] for i in range(0, len(new_flags), AI_BATCH_SIZE)]
    semaphore = asyncio.Semaphore(MAX_CONCURRENT_AI_REQUESTS)
    tasks = [ai_enrich_flags_batch(batch, semaphore=semaphore) for batch in batches]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    for batch, result in zip(batches, results):
        if isinstance(result, Exception):
            log.error(f"Batch enrichment failed: {result}")
            for flag in batch:
                FLAG_INFO[flag] = {"mechanism": "N/A (error)", "purpose": "N/A (error)"}
        else:
            for f in batch:
                info = result.get(f, {})
                FLAG_INFO[f] = {"mechanism": info.get("mechanism", "Unknown"), "purpose": info.get("purpose", "Unknown")}
        await asyncio.sleep(AI_BATCH_DELAY)

def generate_flag_info(flag: str) -> dict:
    return FLAG_INFO.get(flag, {"mechanism": "Unknown", "purpose": "Unknown"})

# ============================
# Report Export
# ============================
def export_reports(report: list, summary: dict, flag_changes: dict) -> None:
    last_run = datetime.datetime.now(ZoneInfo("Asia/Manila")).strftime("%Y-%m-%d %I:%M:%S %p %Z")
    added_total = sum(summary.get((cat, "Added"), 0) for cat in CATEGORIES)
    changed_total = sum(summary.get((cat, "Changed"), 0) for cat in CATEGORIES)
    removed_total = sum(summary.get((cat, "Removed"), 0) for cat in CATEGORIES)
    net_changes = added_total - removed_total
    history = []
    if HISTORY_FILE.exists():
        try:
            history = json.loads(HISTORY_FILE.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            log.warning("Corrupted history file. Using empty history.")
    total_historical_added = sum(entry.get('added', 0) for entry in history)
    total_historical_changed = sum(entry.get('changed', 0) for entry in history)
    total_historical_removed = sum(entry.get('removed', 0) for entry in history)
    percent_change = 0.0
    historical_avg_added = total_historical_added / len(history) if history else 0.0
    historical_avg_changed = total_historical_changed / len(history) if history else 0.0
    historical_avg_removed = total_historical_removed / len(history) if history else 0.0
    if len(history) > 1:
        prev = history[-2]
        prev_total = prev['added'] + prev['changed'] + prev['removed']
        curr_total = added_total + changed_total + removed_total
        percent_change = round(((curr_total - prev_total) / prev_total * 100), 2) if prev_total > 0 else 0.0
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    md = [f"# Roblox Client FFlag Intel Report ({DAYS} Days)\n"]
    md.append(f"- Last Run: {last_run}")
    md.append(f"- Flags Added: {added_total}")
    md.append(f"- Flags Changed: {changed_total}")
    md.append(f"- Flags Removed: {removed_total}\n")
    md.append("## Summary\n| Category | Added | Changed | Removed | Total |\n|---|---|---|---|---|")
    for cat in CATEGORIES:
        a = summary.get((cat, "Added"), 0)
        c = summary.get((cat, "Changed"), 0)
        r = summary.get((cat, "Removed"), 0)
        md.append(f"| {cat} | {a} | {c} | {r} | {a+c+r} |")
    md.append("\n## History Summary\n")
    md.append(f"- Total Historical Added: {total_historical_added}")
    md.append(f"- Total Historical Changed: {total_historical_changed}")
    md.append(f"- Total Historical Removed: {total_historical_removed}")
    if len(history) <= 1:
        md.append("- Note: Limited history available.")
    if not report:
        md.append(f"\n## No Recent Changes\nNo flag changes in the last {DAYS} days.")
    else:
        for header, changes in report:
            md.append(f"\n## {header}")
            grouped = {}
            for typ, cat, flag, *values in changes:
                grouped.setdefault((typ, cat), []).append((flag, *values))
            for (typ, cat), items in grouped.items():
                md.append(f"{typ} in {cat}:")
                for item in items:
                    flag = item[0]
                    values = item[1:]
                    info = generate_flag_info(flag)
                    desc = ""
                    if typ == "Added":
                        desc = f"= {format_value(values[0])}"
                    elif typ == "Changed":
                        desc = f"changed from {format_value(values[0])} to {format_value(values[1])}"
                    elif typ == "Removed":
                        desc = f"removed (was {format_value(values[0])})"
                    md.append(f"- {flag} {desc} | Mechanism: {info['mechanism']} | Purpose: {info['purpose']}")
    OUTPUT_MD.write_text("\n".join(md), encoding="utf-8")
    html_lines = ['<!DOCTYPE html>', '<html lang="en">', '<head><title>Roblox FFlag Report</title></head>', '<body>', '<h1>Roblox FFlag Report</h1>']
    if not report:
        html_lines.append(f"<p>No Recent Changes</p><p>No flag changes in the last {DAYS} days.</p>")
    else:
        for header, changes in report:
            html_lines.append(f"<h2>{html.escape(header)}</h2>")
            grouped = {}
            for typ, cat, flag, *values in changes:
                grouped.setdefault((typ, cat), []).append((flag, *values))
            for (typ, cat), items in grouped.items():
                html_lines.append(f"<details><summary>{html.escape(typ)} in {html.escape(cat)}</summary><ul>")
                for item in items:
                    flag = item[0]
                    values = item[1:]
                    info = generate_flag_info(flag)
                    desc = ""
                    if typ == "Added":
                        desc = f"= {html.escape(format_value(values[0]))}"
                    elif typ == "Changed":
                        desc = f"changed from {html.escape(format_value(values[0]))} to {html.escape(format_value(values[1]))}"
                    elif typ == "Removed":
                        desc = f"removed (was {html.escape(format_value(values[0]))})"
                    html_lines.append(f"<li>{html.escape(flag)} {desc} - Mechanism: {html.escape(info['mechanism'])} - Purpose: {html.escape(info['purpose'])}</li>")
                html_lines.append("</ul></details>")
    html_lines.append('</body></html>')
    OUTPUT_HTML.write_text("\n".join(html_lines), encoding="utf-8")
    json_data = {
        "last_run": last_run,
        "added_total": added_total,
        "changed_total": changed_total,
        "removed_total": removed_total,
        "net_changes": net_changes,
        "percent_change": percent_change,
        "historical_avg_added": historical_avg_added,
        "historical_avg_changed": historical_avg_changed,
        "historical_avg_removed": historical_avg_removed,
        "total_historical_added": total_historical_added,
        "total_historical_changed": total_historical_changed,
        "total_historical_removed": total_historical_removed,
        "summary": {cat: {"added": summary.get((cat, "Added"), 0), "changed": summary.get((cat, "Changed"), 0), "removed": summary.get((cat, "Removed"), 0)} for cat in CATEGORIES},
        "report": [],
        "days": DAYS
    }
    for header, changes in report:
        grouped = {}
        for typ, cat, flag, *values in changes:
            info = generate_flag_info(flag)
            entry = {"name": flag, "mechanism": info['mechanism'], "purpose": info['purpose'], "freq": flag_changes.get(flag, 0)}
            if typ == "Added":
                entry["old_value"] = None
                entry["new_value"] = format_value(values[0])
            elif typ == "Changed":
                entry["old_value"] = format_value(values[0])
                entry["new_value"] = format_value(values[1])
            elif typ == "Removed":
                entry["old_value"] = format_value(values[0])
                entry["new_value"] = None
            grouped.setdefault(f"{typ}_{cat}", []).append(entry)
        json_data["report"].append({"header": header, "grouped": grouped})
    json_data["report"] = json_data["report"][-MAX_REPORT_COMMITS:]
    OUTPUT_JSON.write_text(json.dumps(json_data, indent=2), encoding="utf-8")
    summary_data = json_data.copy()
    commits_data = summary_data.pop("report")
    SUMMARY_JSON = OUTPUT_DIR / "summary.json"
    COMMITS_JSON = OUTPUT_DIR / "commits.json"
    SUMMARY_JSON.write_text(json.dumps(summary_data, indent=2), encoding="utf-8")
    COMMITS_JSON.write_text(json.dumps(commits_data, indent=2), encoding="utf-8")
    log.info(f"Reports generated: {OUTPUT_MD}, {OUTPUT_HTML}, {OUTPUT_JSON}, {SUMMARY_JSON}, {COMMITS_JSON}")

# ============================
# Landing Page
# ============================
def ensure_landing_page(added: int, changed: int, removed: int, last_run: str) -> None:
    index_html = OUTPUT_DIR / "index.html"
    sw_js = OUTPUT_DIR / "sw.js"
    if not HISTORY_FILE.exists():
        HISTORY_FILE.write_text("[]", encoding="utf-8")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    net_changes = added - removed
    history = []
    if HISTORY_FILE.exists():
        try:
            history = json.loads(HISTORY_FILE.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            log.warning("Corrupted history file. Using empty history.")
    total_historical_added = sum(entry.get('added', 0) for entry in history)
    total_historical_changed = sum(entry.get('changed', 0) for entry in history)
    total_historical_removed = sum(entry.get('removed', 0) for entry in history)
    percent_change = 0.0
    if len(history) > 1:
        prev = history[-2]
        prev_total = prev['added'] + prev['changed'] + prev['removed']
        curr_total = added + changed + removed
        percent_change = round(((curr_total - prev_total) / prev_total * 100), 2) if prev_total > 0 else 0.0
    category_options = "\n".join([f'    <option value="{cat}">{cat}</option>' for cat in CATEGORIES])
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Roblox FFlag Tracker</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
<style>
:root {{ 
  --primary-green: #2f855a; /* WCAG-compliant green */
  --primary-blue: #2b6cb0; /* WCAG-compliant blue */
  --primary-red: #c53030; /* WCAG-compliant red */
  --primary-yellow: #d69e2e; /* WCAG-compliant yellow */
  --historical-green: #276749;
  --historical-blue: #2c5282;
  --historical-red: #9b2c2c;
  --bg-opacity: 0.15;
  --text-color: #ffffff;
  --bg-color: linear-gradient(135deg,#2d3748,#4a5568,#718096,#a0aec0);
  --high-contrast-bg: #1a202c;
  --high-contrast-text: #ffffff;
}}
body {{ 
  font-family: 'Inter', sans-serif;
  margin: 0;
  background: var(--bg-color);
  background-size: 400% 400%;
  animation: gradientBG 15s ease infinite;
  color: var(--text-color);
  overflow-x: hidden;
}}
body.light {{
  --text-color: #1a202c;
  --bg-opacity: 0.05;
  --bg-color: linear-gradient(135deg,#edf2f7,#e2e8f0,#cbd5e0,#a0aec0);
}}
body.high-contrast {{
  background: var(--high-contrast-bg);
  color: var(--high-contrast-text);
  --bg-opacity: 0;
}}
@keyframes gradientBG {{ 
  0% {{background-position:0% 50%;}}
  50% {{background-position:100% 50%;}}
  100% {{background-position:0% 50%;}}
}}
header {{ 
  text-align: center; 
  padding: 60px 20px; 
  text-shadow: 0 0 8px rgba(0,0,0,0.4); 
}}
header h1 {{ 
  font-size: 2.5rem; 
  font-weight: 700; 
}}
.stats {{ 
  display: flex;
  justify-content: center;
  gap: 20px;
  flex-wrap: wrap;
  max-width: 1200px;
  margin: -40px auto 40px;
  position: relative; 
  z-index: 2;
}}
.badge {{ 
  flex: 1; 
  min-width: 200px;
  text-align: center;
  padding: 20px;
  border-radius: 12px;
  font-weight: 600;
  backdrop-filter: blur(10px);
  background: rgba(255,255,255,var(--bg-opacity));
  box-shadow: 0 8px 24px rgba(0,0,0,0.3);
  transition: transform 0.3s ease, box-shadow 0.3s ease, border 0.3s ease;
}}
.badge:hover {{ 
  transform: translateY(-5px);
  box-shadow: 0 12px 32px rgba(0,0,0,0.4);
  border: 2px solid var(--primary-green);
}}
.added {{ border-left: 6px solid var(--primary-green); }}
.changed {{ border-left: 6px solid var(--primary-blue); }}
.removed {{ border-left: 6px solid var(--primary-red); }}
.net {{ border-left: 6px solid var(--primary-yellow); }}
.percent {{ border-left: 6px solid var(--primary-blue); }}
.percent.positive {{ border-left-color: var(--primary-green); }}
.percent.negative {{ border-left-color: var(--primary-red); }}
.historical-added {{ border-left: 6px solid var(--historical-green); }}
.historical-changed {{ border-left: 6px solid var(--historical-blue); }}
.historical-removed {{ border-left: 6px solid var(--historical-red); }}
.status-icon {{ 
  font-size: 1.2rem; 
  margin-right: 8px; 
  vertical-align: middle;
}}
.last-run {{ 
  text-align: center; 
  margin: 20px 0; 
  font-style: italic; 
  color: #e2e8f0; 
}}
section {{ 
  max-width: 1200px; 
  margin: 0 auto; 
  padding: 20px; 
}}
.report-container {{ 
  background: rgba(255,255,255,var(--bg-opacity));
  backdrop-filter: blur(10px);
  border-radius: 12px;
  box-shadow: 0 8px 24px rgba(0,0,0,0.25);
  padding: 15px;
  position: relative;
  min-height: 75vh;
}}
#loadingSpinner {{ 
  position: absolute;
  top: 50%; 
  left: 50%;
  transform: translate(-50%, -50%);
  border: 4px solid rgba(255,255,255,0.3);
  border-top: 4px solid var(--primary-green);
  border-radius: 50%;
  width: 40px; 
  height: 40px;
  animation: spin 1s linear infinite;
}}
@keyframes spin {{ 
  0% {{ transform: rotate(0deg); }}
  100% {{ transform: rotate(360deg); }}
}}
#reportContent {{ 
  width: 100%; 
}}
canvas#trendChart {{ 
  display: block; 
  max-width: 850px; 
  margin: 40px auto; 
  border-radius: 12px; 
}}
input#searchInput {{ 
  width: 90%; 
  padding: 12px; 
  margin: 20px auto; 
  display: block;
  border-radius: 12px; 
  border: 1px solid rgba(255,255,255,0.3);
  background: rgba(0,0,0,0.2); 
  color: var(--text-color); 
  font-size: 1rem;
  backdrop-filter: blur(5px);
}}
select {{ 
  padding: 12px; 
  margin: 10px; 
  border-radius: 12px; 
  background: rgba(0,0,0,0.2); 
  color: var(--text-color);
}}
button {{ 
  padding: 10px 20px; 
  border-radius: 8px; 
  background: var(--primary-blue); 
  color: white; 
  border: none; 
  cursor: pointer;
}}
button:hover {{ 
  background: var(--primary-green); 
}}
.copy-btn {{ 
  margin-left: 10px; 
  padding: 5px 10px; 
  font-size: 0.8rem; 
  background: var(--primary-yellow);
}}
.commit-card {{ 
  background: rgba(255,255,255,0.2);
  border-radius: 8px;
  padding: 15px;
  margin-bottom: 20px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.2);
  opacity: 0;
  transform: translateY(20px);
  transition: opacity 0.3s ease, transform 0.3s ease;
}}
.commit-card.visible {{ 
  opacity: 1;
  transform: translateY(0);
}}
h3 {{ 
  cursor: pointer; 
}}
ul {{ 
  overflow: hidden;
  transition: max-height 0.3s ease;
  list-style-type: none;
}}
footer {{ 
  text-align: center; 
  margin-top: 60px; 
  padding: 25px; 
  font-size: 0.9rem; 
  color: #e2e8f0; 
}}
canvas#particleCanvas {{ 
  position: fixed;
  top: 0; 
  left: 0; 
  width: 100%; 
  height: 100%;
  pointer-events: none;
  z-index: 0;
}}
table {{ 
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 40px;
}}
th, td {{ 
  border: 1px solid rgba(255,255,255,0.3);
  padding: 12px;
  text-align: left;
}}
th {{ 
  background: rgba(0,0,0,0.2);
}}
.high-contrast th, .high-contrast td {{ 
  border: 1px solid #ffffff;
}}
.high-contrast .report-container, .high-contrast .badge, .high-contrast .commit-card {{ 
  background: var(--high-contrast-bg);
  color: var(--high-contrast-text);
}}
</style>
</head>
<body>
<canvas id="particleCanvas" aria-hidden="true"></canvas>
<header>
  <h1>Roblox FFlag Tracker</h1>
  <button id="themeToggle">Toggle Theme</button>
  <button id="highContrastToggle">High Contrast</button>
</header>
<div class="stats">
  <div class="badge added">
    <span class="status-icon" aria-hidden="true">✅</span> Added: <span id="flags-added">{added}</span>
  </div>
  <div class="badge changed">
    <span class="status-icon" aria-hidden="true">🔄</span> Changed: <span id="flags-changed">{changed}</span>
  </div>
  <div class="badge removed">
    <span class="status-icon" aria-hidden="true">❌</span> Removed: <span id="flags-removed">{removed}</span>
  </div>
  <div class="badge net">
    <span class="status-icon" aria-hidden="true">📊</span> Net Changes: <span id="net-changes">{net_changes}</span>
  </div>
  <div class="badge percent">
    <span class="status-icon" aria-hidden="true">%</span> % Change: <span id="percent-change">{percent_change:.2f}</span>%
  </div>
  <div class="badge historical-added">
    <span class="status-icon" aria-hidden="true">📈</span> Historical Added: <span id="historical-added">{total_historical_added}</span>
  </div>
  <div class="badge historical-changed">
    <span class="status-icon" aria-hidden="true">📈</span> Historical Changed: <span id="historical-changed">{total_historical_changed}</span>
  </div>
  <div class="badge historical-removed">
    <span class="status-icon" aria-hidden="true">📉</span> Historical Removed: <span id="historical-removed">{total_historical_removed}</span>
  </div>
</div>
<p class="last-run">Last Run: <span id="last-run">{last_run}</span></p>
<section>
  <input type="text" id="searchInput" placeholder="Search flags..." aria-label="Search flags">
  <select id="categoryFilter" aria-label="Filter by category">
    <option value="">All Categories</option>
{category_options}
  </select>
  <select id="sortSelect" aria-label="Sort options">
    <option value="">Sort by Name</option>
    <option value="freq">Sort by Frequency</option>
  </select>
  <h2>Summary</h2>
  <table id="summaryTable" aria-label="Summary of flag changes by category">
    <tr><th>Category</th><th>Added</th><th>Changed</th><th>Removed</th></tr>
  </table>
  <h2>📊 Latest Full Report</h2>
  <div class="report-container">
    <div id="loadingSpinner" aria-hidden="true"></div>
    <div id="reportContent" role="region" aria-live="polite"></div>
  </div>
  <button id="exportCSV" aria-label="Export report as CSV">Export CSV</button>
  <button id="exportJSON" aria-label="Export report as JSON">Export JSON</button>
  <canvas id="trendChart" aria-label="Trend chart of flag changes"></canvas>
</section>
<footer>Built with ❤️ by FFlag Tracker • Updated automatically</footer>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.4"></script>
<script src="https://cdn.jsdelivr.net/npm/chartjs-plugin-zoom@2.0.1/dist/chartjs-plugin-zoom.min.js"></script>
<script>
// Particle animation
const canvas = document.getElementById('particleCanvas');
const ctx = canvas.getContext('2d');
let resizeTimeout, animationId, particles = [];
function resizeCanvas() {
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;
}
function generateParticles() {
  particles = Array.from({length: 30}, () => ({
    x: Math.random() * canvas.width,
    y: Math.random() * canvas.height,
    r: Math.random() * 2 + 1,
    dx: (Math.random() - 0.5) / 2,
    dy: (Math.random() - 0.5) / 2,
    color: `rgba(${Math.floor(Math.random() * 50 + 200)}, 255, 255, 0.15)`,
  }));
}
function animateParticles() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  particles.forEach(p => {
    p.x += p.dx;
    p.y += p.dy;
    if (p.x < 0 || p.x > canvas.width) p.dx *= -1;
    if (p.y < 0 || p.y > canvas.height) p.dy *= -1;
    ctx.beginPath();
    ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
    ctx.fillStyle = p.color;
    ctx.fill();
  });
  animationId = requestAnimationFrame(animateParticles);
}
function stopAnimation() {
  cancelAnimationFrame(animationId);
}
resizeCanvas();
generateParticles();
animateParticles();
window.addEventListener('resize', () => {
  clearTimeout(resizeTimeout);
  resizeTimeout = setTimeout(resizeCanvas, 200);
});
document.addEventListener('visibilitychange', () => {
  if (document.hidden) stopAnimation();
  else animateParticles();
});

// Theme and high-contrast toggle
document.getElementById('themeToggle').addEventListener('click', () => {
  document.body.classList.toggle('light');
  document.body.classList.remove('high-contrast');
});
document.getElementById('highContrastToggle').addEventListener('click', () => {
  document.body.classList.toggle('high-contrast');
  document.body.classList.remove('light');
});

// Trend chart
fetch("history.json").then(r => r.json()).then(data => {
  if (data.length === 0) {
    document.getElementById("trendChart").parentNode.innerHTML = '<p>No history data yet.</p>';
    return;
  }
  const ctx = document.getElementById("trendChart").getContext("2d");
  new Chart(ctx, {
    type: 'line',
    data: {
      labels: data.map(d => d.date),
      datasets: [
        {label: 'Added', data: data.map(d => d.added), borderColor: '#2f855a', backgroundColor: 'rgba(47,133,90,0.2)', fill: true, tension: 0.4},
        {label: 'Changed', data: data.map(d => d.changed || 0), borderColor: '#2b6cb0', backgroundColor: 'rgba(43,108,176,0.2)', fill: true, tension: 0.4},
        {label: 'Removed', data: data.map(d => d.removed), borderColor: '#c53030', backgroundColor: 'rgba(197,48,48,0.2)', fill: true, tension: 0.4}
      ]
    },
    options: {
      responsive: true,
      plugins: {
        legend: {position: 'top'},
        zoom: {zoom: {wheel: {enabled: true}, pinch: {enabled: true}, mode: 'x'}, pan: {enabled: true, mode: 'x'}},
        tooltip: {callbacks: {label: (ctx) => `${ctx.dataset.label}: ${ctx.raw}`}}
      },
      interaction: {mode: 'nearest', axis: 'x', intersect: false},
      scales: {
        y: {beginAtZero: true}
      }
    }
  });
}).catch(error => {
  console.error('Error loading history:', error);
  document.getElementById("trendChart").parentNode.innerHTML = '<p>Error loading history data.</p>';
});

// Virtual scrolling for report
const reportContent = document.getElementById('reportContent');
const loadingSpinner = document.getElementById('loadingSpinner');
let globalData = null;
let currentData = [];
let observer;
let isLoading = false;
let hasMore = true;
const itemsPerPage = 10;

function createCommitCard(commit) {
  const card = document.createElement('div');
  card.classList.add('commit-card');
  const h2 = document.createElement('h2');
  h2.textContent = commit.header;
  card.appendChild(h2);
  Object.entries(commit.grouped).forEach(([groupKey, flags]) => {
    const [typ, cat] = groupKey.split('_');
    const h3 = document.createElement('h3');
    h3.textContent = `${typ} in ${cat}`;
    h3.style.cursor = 'pointer';
    h3.setAttribute('aria-expanded', 'true');
    h3.setAttribute('tabindex', '0');
    card.appendChild(h3);
    const ul = document.createElement('ul');
    flags.forEach(f => {
      const li = document.createElement('li');
      li.dataset.freq = f.freq;
      let desc = '';
      if (f.old_value === null && f.new_value !== null) {
        desc = `= ${f.new_value}`;
      } else if (f.old_value !== null && f.new_value !== null) {
        desc = `changed from ${f.old_value} to ${f.new_value}`;
      } else if (f.old_value !== null && f.new_value === null) {
        desc = `(was ${f.old_value})`;
      }
      const icon = typ === 'Added' ? '✅' : typ === 'Changed' ? '🔄' : '❌';
      li.innerHTML = `<span class="status-icon" aria-hidden="true">${icon}</span> ${f.name} ${desc} - Mechanism: ${f.mechanism} - Purpose: ${f.purpose} <button class="copy-btn" data-copy="${f.mechanism} - ${f.purpose}" aria-label="Copy mechanism and purpose for ${f.name}">Copy</button>`;
      ul.appendChild(li);
    });
    ul.style.maxHeight = ul.scrollHeight + 'px';
    card.appendChild(ul);
  });
  setTimeout(() => card.classList.add('visible'), 100);
  return card;
}

async function loadReportPage(page, category = '', query = '', sortBy = '') {
  if (isLoading || !hasMore) return;
  isLoading = true;
  try {
    const response = await fetch(`commits.json?page=${page}&itemsPerPage=${itemsPerPage}&category=${encodeURIComponent(category)}&query=${encodeURIComponent(query)}&sortBy=${sortBy}`);
    if (!response.ok) throw new Error('Failed to load page');
    const data = await response.json();
    if (data.length === 0) {
      hasMore = false;
      if (page === 0) reportContent.innerHTML = `<p>No recent flag changes in the last ${globalData.days} days.</p>`;
      return;
    }
    currentData = currentData.concat(data);
    data.forEach(commit => {
      reportContent.appendChild(createCommitCard(commit));
    });
    setupObserver();
  } catch (error) {
    console.error('Error loading page:', error);
    reportContent.innerHTML = '<p>Error loading report data. Please try again later.</p>';
  } finally {
    isLoading = false;
    loadingSpinner.style.display = 'none';
  }
}

function setupObserver() {
  if (observer) observer.disconnect();
  if (!hasMore) return;
  const sentinel = document.createElement('div');
  sentinel.id = 'sentinel';
  reportContent.appendChild(sentinel);
  observer = new IntersectionObserver(entries => {
    if (entries[0].isIntersecting && !isLoading) {
      const category = document.getElementById('categoryFilter').value;
      const query = document.getElementById('searchInput').value.toLowerCase();
      const sortBy = document.getElementById('sortSelect').value;
      loadReportPage(currentData.length / itemsPerPage, category, query, sortBy);
    }
  }, {threshold: 0, rootMargin: '100px'});
  observer.observe(sentinel);
}

function debounce(func, delay) {
  let timeout;
  return (...args) => {
    clearTimeout(timeout);
    timeout = setTimeout(() => func(...args), delay);
  };
}

async function applyFilters() {
  const category = document.getElementById('categoryFilter').value;
  const query = document.getElementById('searchInput').value.toLowerCase();
  const sortBy = document.getElementById('sortSelect').value;
  reportContent.innerHTML = '';
  currentData = [];
  hasMore = true;
  isLoading = false;
  await loadReportPage(0, category, query, sortBy);
}

async function loadReportData() {
  try {
    const summaryResponse = await fetch('summary.json');
    if (!summaryResponse.ok) throw new Error('Failed to load summary.json');
    const data = await summaryResponse.json();
    globalData = data;
    document.getElementById('flags-added').textContent = data.added_total;
    document.getElementById('flags-changed').textContent = data.changed_total;
    document.getElementById('flags-removed').textContent = data.removed_total;
    document.getElementById('net-changes').textContent = data.net_changes;
    const percent = data.percent_change.toFixed(2);
    document.getElementById('percent-change').textContent = percent;
    const percentBadge = document.querySelector('.percent');
    if (percent > 0) percentBadge.classList.add('positive');
    else if (percent < 0) percentBadge.classList.add('negative');
    document.getElementById('historical-added').textContent = data.total_historical_added;
    document.getElementById('historical-changed').textContent = data.total_historical_changed;
    document.getElementById('historical-removed').textContent = data.total_historical_removed;
    document.getElementById('last-run').textContent = data.last_run;
    const summaryTable = document.getElementById('summaryTable');
    let tableHtml = '<tr><th>Category</th><th>Added</th><th>Changed</th><th>Removed</th></tr>';
    for (let cat in data.summary) {
      const s = data.summary[cat];
      tableHtml += `<tr><td>${cat}</td><td>${s.added}</td><td>${s.changed}</td><td>${s.removed}</td></tr>`;
    }
    summaryTable.innerHTML = tableHtml;
    await applyFilters();
    reportContent.addEventListener('click', e => {
      if (e.target.tagName === 'H3') {
        const ul = e.target.nextElementSibling;
        if (ul && ul.tagName === 'UL') {
          const expanded = e.target.getAttribute('aria-expanded') === 'true';
          ul.style.maxHeight = expanded ? '0px' : ul.scrollHeight + 'px';
          e.target.setAttribute('aria-expanded', !expanded);
        }
      } else if (e.target.classList.contains('copy-btn')) {
        navigator.clipboard.writeText(e.target.dataset.copy).then(() => {
          e.target.textContent = 'Copied!';
          setTimeout(() => e.target.textContent = 'Copy', 2000);
        });
      }
    });
    reportContent.addEventListener('keydown', e => {
      if (e.target.tagName === 'H3' && (e.key === 'Enter' || e.key === ' ')) {
        e.preventDefault();
        const ul = e.target.nextElementSibling;
        if (ul && ul.tagName === 'UL') {
          const expanded = e.target.getAttribute('aria-expanded') === 'true';
          ul.style.maxHeight = expanded ? '0px' : ul.scrollHeight + 'px';
          e.target.setAttribute('aria-expanded', !expanded);
        }
      }
    });
  } catch (error) {
    console.error('Error loading report:', error);
    loadingSpinner.style.display = 'none';
    reportContent.innerHTML = '<p>Error loading report data. Please try again later.</p>';
  }
}

loadReportData();
document.getElementById('searchInput').addEventListener('input', debounce(applyFilters, 300));
document.getElementById('categoryFilter').addEventListener('change', applyFilters);
document.getElementById('sortSelect').addEventListener('change', applyFilters);
document.getElementById('exportCSV').addEventListener('click', async () => {
  if (!globalData) return;
  const response = await fetch('commits.json');
  if (!response.ok) return;
  const reportData = await response.json();
  let csv = 'Commit,Type,Category,Flag,Old Value,New Value,Mechanism,Purpose,Frequency\n';
  reportData.forEach(commit => {
    Object.entries(commit.grouped).forEach(([groupKey, flags]) => {
      const [typ, cat] = groupKey.split('_');
      flags.forEach(f => {
        csv += `"${commit.header}","${typ}","${cat}","${f.name}","${f.old_value || ''}","${f.new_value || ''}","${f.mechanism}","${f.purpose}","${f.freq}"\n`;
      });
    });
  });
  download('fflag_report.csv', csv);
});
document.getElementById('exportJSON').addEventListener('click', async () => {
  if (!globalData) return;
  const response = await fetch('commits.json');
  if (!response.ok) return;
  const reportData = await response.json();
  const fullData = {...globalData, report: reportData};
  download('fflag_report.json', JSON.stringify(fullData, null, 2));
});
function download(filename, text) {
  const a = document.createElement('a');
  a.href = URL.createObjectURL(new Blob([text], {type: 'text/plain'}));
  a.download = filename;
  a.click();
}
setInterval(() => {
  fetch('summary.json?ts=' + Date.now()).then(r => r.json()).then(newData => {
    if (globalData && newData.last_run !== globalData.last_run) {
      location.reload();
    }
  }).catch(() => {});
}, 60000);
if ('serviceWorker' in navigator) {
  navigator.serviceWorker.register('/sw.js').catch(error => {
    console.error('Service Worker registration failed:', error);
  });
}
</script>
</body>
</html>"""
    index_html.write_text(html_content, encoding="utf-8")
    sw_content = """self.addEventListener('install', e => {
  e.waitUntil(
    caches.open('fflag-cache').then(cache => {
      return cache.addAll([
        '/',
        '/index.html',
        '/summary.json',
        '/commits.json',
        '/history.json'
      ]);
    })
  );
});
self.addEventListener('fetch', e => {
  e.respondWith(
    caches.match(e.request).then(response => {
      return response || fetch(e.request).then(async res => {
        if (e.request.url.includes('commits.json') && e.request.url.includes('page=')) {
          const clone = res.clone();
          const data = await clone.json();
          return new Response(JSON.stringify(data), {
            headers: {'Content-Type': 'application/json'}
          });
        }
        return res;
      });
    })
  );
});
"""
    sw_js.write_text(sw_content, encoding="utf-8")
    log.info(f"Landing page written: {index_html}")
    log.info(f"Service worker written: {sw_js}")

# ============================
# Main Execution
# ============================
async def main() -> None:
    try:
        await asyncio.sleep(random.uniform(0, 300))
        log.info("=" * 80)
        log.info("Roblox Client FFlag Tracker (Integrated Categories + Interpolation)")
        log.info("=" * 80)
        manifest_repo = ensure_manifest_repo()
        commits = get_commits(DAYS, manifest_repo)
        lock = FileLock(str(OUTPUT_DIR / "cache.lock"), timeout=10)
        with lock:
            diff_cache = {}
            if DIFF_CACHE_FILE.exists():
                try:
                    diff_cache = json.loads(DIFF_CACHE_FILE.read_text(encoding="utf-8"))
                except json.JSONDecodeError:
                    log.warning("Corrupted diff_cache.json. Using empty cache.")
            report = []
            summary = {}
            flag_changes = {}
            if commits:
                report, summary, flag_changes = await build_report(commits, diff_cache, manifest_repo)
            DIFF_CACHE_FILE.write_text(json.dumps(diff_cache, indent=2), encoding="utf-8")
            all_flags = set(flag for _, changes in report for _, _, flag, *_ in changes)
            if all_flags:
                await generate_flag_info_batch(list(all_flags))
            history_commits = get_commits(HISTORY_DAYS, manifest_repo)
            _, _, flag_changes_history = await build_report(history_commits, diff_cache, manifest_repo)
            recent_flags = set(flag_changes_history.keys())
            prune_list = [f for f in list(FLAG_INFO.keys()) if f not in recent_flags]
            for f in prune_list:
                del FLAG_INFO[f]
            if prune_list:
                log.info(f"Pruned {len(prune_list)} old flags from cache.")
            CACHE_FILE.write_text(json.dumps(FLAG_INFO, indent=2), encoding="utf-8")
        last_run = datetime.datetime.now(ZoneInfo("Asia/Manila")).strftime("%Y-%m-%d %I:%M:%S %p %Z")
        added = sum(summary.get((cat, "Added"), 0) for cat in CATEGORIES)
        changed = sum(summary.get((cat, "Changed"), 0) for cat in CATEGORIES)
        removed = sum(summary.get((cat, "Removed"), 0) for cat in CATEGORIES)
        update_history(added, changed, removed, last_run)
        export_reports(report, summary, flag_changes)
        ensure_landing_page(added, changed, removed, last_run)
        log.info("All done! Reports and dashboard ready.")
    except Exception as e:
        log.error(f"Main execution failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())
