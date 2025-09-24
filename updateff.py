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
import requests

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
DEBUG_DIR = OUTPUT_DIR / "debug"
REPO_URL = "https://github.com/MaximumADHD/Roblox-FFlag-Tracker.git"
TARGET_FILE = "PCDesktopClient.json"
DAYS = 30
HISTORY_DAYS = 90
AI_BATCH_SIZE = 5
AI_CONCURRENT_LIMIT = 5
AI_BATCH_DELAY = 1.0
MAX_RETRIES = 3
MAX_REPORT_COMMITS = 50
COMMIT_BATCH_SIZE = 30
DEBUG = True
SUBPROCESS_TIMEOUT = 120

# ============================
# Command-Line Arguments
# ============================
parser = argparse.ArgumentParser(description="Roblox FFlag Tracker")
parser.add_argument("--dry-run", action="store_true", help="Run without AI enrichment")
args = parser.parse_args()

# ============================
# Logging Utility
# ============================
logging.basicConfig(
    level=logging.INFO if not DEBUG else logging.DEBUG,
    format="[%(levelname)s] %(message)s (%(asctime)s)"
)
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
if not OPENAI_KEYS and not args.dry_run:
    log.warning("⚠ No OpenAI API keys found. AI enrichment will be skipped.")

def get_next_api_key() -> str | None:
    if not OPENAI_KEYS:
        return None
    lock = FileLock(str(KEY_INDEX_FILE) + ".lock", timeout=10)
    with lock:
        index_data = {"openai_idx": 0}
        if KEY_INDEX_FILE.exists():
            try:
                index_data = json.loads(KEY_INDEX_FILE.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                log.warning(f"Corrupted {KEY_INDEX_FILE}. Resetting index.")
        idx = index_data.get("openai_idx", 0)
        key = OPENAI_KEYS[idx % len(OPENAI_KEYS)]
        index_data["openai_idx"] = idx + 1
        KEY_INDEX_FILE.write_text(json.dumps(index_data, indent=2), encoding="utf-8")
    display_key = f"{key[:4]}...{key[-4:]}" if len(key) > 8 else "****"
    log.debug(f"Using OpenAI API key #{idx % len(OPENAI_KEYS) + 1} ({display_key})")
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
            raise subprocess.CalledProcessError(
                result.returncode, cmd, output=result.stdout, stderr=result.stderr
            )
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
            subprocess.run(
                ["git", "-C", str(cache_path), "stash", "push", "--include-untracked", "--quiet"],
                check=False
            )
            subprocess.run(["git", "-C", str(cache_path), "pull", "--ff-only"], check=True)
            subprocess.run(
                ["git", "-C", str(cache_path), "stash", "pop"],
                check=False,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
            return cache_path
        except (subprocess.CalledProcessError, FileNotFoundError):
            log.warning("Cached repo pull or file check failed, recloning...")
            shutil.rmtree(cache_path, ignore_errors=True)
    log.info("Cloning fresh manifest repo...")
    subprocess.run(["git", "clone", "--depth=200", repo_url, str(cache_path)], check=True)
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
def build_diff_for_commit_old(
    commit_hash: str, manifest_repo: Path | None = None
) -> tuple[str, list[tuple[str, any]], list[tuple[str, any, any]], list[tuple[str, any]]]:
    header = run_cmd(
        f"git show --no-patch --pretty=format:'%h - %ci - %s' {commit_hash}", cwd=manifest_repo
    )
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

async def async_build_diff_for_commit(
    commit_hash: str, diff_cache: dict, manifest_repo: Path | None = None
) -> tuple[str, list[tuple[str, any]], list[tuple[str, any, any]], list[tuple[str, any]]]:
    if commit_hash in diff_cache:
        cached = diff_cache[commit_hash]
        added = [(f, v) for f, v in cached.get('added', [])]
        changed = [(f, o, n) for f, o, n in cached.get('changed', [])]
        removed = [(f, v) for f, v in cached.get('removed', [])]
        return cached['header'], added, changed, removed
    header, added, changed, removed = await asyncio.get_running_loop().run_in_executor(
        None, lambda: build_diff_for_commit_old(commit_hash, manifest_repo)
    )
    diff_cache[commit_hash] = {
        'header': header,
        'added': [[f, v] for f, v in added],
        'changed': [[f, o, n] for f, o, n in changed],
        'removed': [[f, v] for f, v in removed]
    }
    return header, added, changed, removed

async def build_report(
    commits: list[str], diff_cache: dict, manifest_repo: Path | None = None
) -> tuple[list, dict, dict]:
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

def safe_json_parse(raw: str):
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        cleaned = re.sub(r"^```(?:json)?|```$", "", raw.strip(), flags=re.MULTILINE).strip()
        cleaned = re.sub(r",\s*([}\]])", r"\1", cleaned)
        try:
            return json.loads(cleaned)
        except json.JSONDecodeError as e:
            log.warning(f"JSON still invalid after cleanup: {e}")
            return None

def normalize_ai_response(raw: str, flags: list[str]):
    data = safe_json_parse(raw)
    if isinstance(data, list):
        return {flag: obj for flag, obj in zip(flags, data) if isinstance(obj, dict)}
    return data

def extract_and_validate_json(text: str) -> dict:
    data = safe_json_parse(text)
    if data is None:
        raise json.JSONDecodeError("Invalid JSON after repair", text, 0)
    if json_validate:
        try:
            json_validate(instance=data, schema=FLAG_SCHEMA)
        except ValidationError as ve:
            log.warning(f"Schema issue: {ve}. Filtering invalid keys.")
            data = {k: v for k, v in data.items() if re.match(
                r"^(FFlag|DFFlag|DFInt|DFLog|SFFlag|FString|FInt|DFString)[A-Za-z0-9_]+$",
                k
            )}
    return data

async def ai_enrich_flags_batch(batch: list[str]) -> dict:
    if args.dry_run:
        log.info("Dry run: Skipping AI enrichment")
        return {f: {"mechanism": "N/A (dry run)", "purpose": "N/A (dry run)"} for f in batch}
    if not OPENAI_KEYS or not AsyncOpenAI:
        log.warning("No OpenAI API keys or client available. Skipping enrichment.")
        return {}
    system_prompt = (
        "Respond ONLY with valid JSON.\n"
        "Each flag must be the key of an object.\n"
        "The value must be another object with exactly two fields:\n"
        "- mechanism (short, technical)\n"
        "- purpose (player-facing benefit)\n"
        "Example:\n"
        "{\n"
        "  \"FFlagExample\": {\"mechanism\": \"...\", \"purpose\": \"...\"},\n"
        "  \"DFFlagOther\": {\"mechanism\": \"...\", \"purpose\": \"...\"}\n"
        "}"
    )
    user_prompt = (
        "Explain these Roblox FFlags in simple layman's terms. "
        "For each flag, return a JSON object with:\n"
        "- mechanism: how it technically works (short)\n"
        "- purpose: what benefit or change it brings for Roblox players.\n\n"
        f"Flags: {json.dumps(batch)}"
    )
    for attempt in range(MAX_RETRIES):
        try:
            client = AsyncOpenAI(api_key=get_next_api_key())
            response = await client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.3
            )
            text = response.choices[0].message.content.strip()
            parsed = normalize_ai_response(text, batch)
            parsed = extract_and_validate_json(json.dumps(parsed))
            if not parsed:
                log.warning("OpenAI returned invalid JSON. Skipping enrichment.")
                return {f: {"mechanism": "N/A (invalid)", "purpose": "N/A (invalid)"} for f in batch}
            return parsed
        except RateLimitError as e:
            retry_after = 60
            if hasattr(e, 'response') and e.response and e.response.headers.get('Retry-After'):
                try:
                    retry_after = min(int(e.response.headers.get('Retry-After')), 60)
                except ValueError:
                    pass
            log.warning(f"OpenAI rate limit hit on attempt {attempt+1}. Waiting {retry_after}s.")
            await asyncio.sleep(retry_after)
            continue
        except json.JSONDecodeError as je:
            log.warning(f"Failed to parse OpenAI response: {je}. Retrying with stricter prompt.")
            system_prompt = "Respond strictly in valid JSON with 'mechanism' and 'purpose' for each Roblox FFlag."
            await asyncio.sleep(1)
            continue
        except Exception as e:
            log.error(f"OpenAI batch failed (attempt {attempt+1}): {e}")
            await asyncio.sleep(2 ** attempt)
            continue
    log.warning("OpenAI failed after max retries. Skipping enrichment.")
    return {f: {"mechanism": "N/A (invalid)", "purpose": "N/A (invalid)"} for f in batch}

async def generate_flag_info_batch(flags: list[str]) -> None:
    new_flags = [f for f in flags if should_enrich_flag(f)]
    if not new_flags:
        return
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    batches = [new_flags[i:i + AI_BATCH_SIZE] for i in range(0, len(new_flags), AI_BATCH_SIZE)]
    semaphore = asyncio.Semaphore(AI_CONCURRENT_LIMIT)
    async def limited_task(batch):
        async with semaphore:
            result = await ai_enrich_flags_batch(batch)
            await asyncio.sleep(AI_BATCH_DELAY)
            return result, batch
    tasks = [limited_task(batch) for batch in batches]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    for result in [r for r in results if not isinstance(r, Exception)]:
        info_batch, batch = result
        for f in batch:
            info = info_batch.get(f, {})
            if info and "mechanism" in info and "purpose" in info:
                FLAG_INFO[f] = {"mechanism": info.get("mechanism", "Unknown"),
                              "purpose": info.get("purpose", "Unknown")}
            else:
                log.warning(f"Skipping invalid or missing info for flag {f}")
                FLAG_INFO[f] = {"mechanism": "N/A (invalid)", "purpose": "N/A (invalid)"}
    for exception in [r for r in results if isinstance(r, Exception)]:
        log.error(f"Batch enrichment failed: {exception}")
        for flag in batch:
            FLAG_INFO[flag] = {"mechanism": "N/A (error)", "purpose": "N/A (error)"}
    CACHE_FILE.write_text(json.dumps(FLAG_INFO, indent=2), encoding="utf-8")

def should_enrich_flag(flag: str) -> bool:
    if args.dry_run:
        return False
    if flag not in FLAG_INFO:
        return True
    info = FLAG_INFO[flag]
    return not (info.get("mechanism") and info.get("purpose") and not info["mechanism"].startswith("N/A"))

def generate_flag_info(flag: str) -> dict:
    return FLAG_INFO.get(flag, {"mechanism": "N/A", "purpose": "N/A"})

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
    html_lines = ['<!DOCTYPE html>', '<html>', '<head><title>Roblox FFlag Report</title></head>', '<body>', '<h1>Roblox FFlag Report</h1>']
    if not report:
        html_lines.append(f"<p>No Recent Changes</p><p>No flag changes in the last {html.escape(str(DAYS))} days.</p>")
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
                    html_lines.append(
                        f"<li>{html.escape(flag)} {desc} - Mechanism: {html.escape(info['mechanism'])} - Purpose: {html.escape(info['purpose'])}</li>"
                    )
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
        "summary": {
            cat: {
                "added": summary.get((cat, "Added"), 0),
                "changed": summary.get((cat, "Changed"), 0),
                "removed": summary.get((cat, "Removed"), 0)
            } for cat in CATEGORIES
        },
        "report": [],
        "days": DAYS
    }
    for header, changes in report:
        grouped = {}
        for typ, cat, flag, *values in changes:
            info = generate_flag_info(flag)
            entry = {
                "name": flag,
                "mechanism": info['mechanism'],
                "purpose": info['purpose'],
                "freq": flag_changes.get(flag, 0)
            }
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
    app_js = OUTPUT_DIR / "assets" / "app.js"
    if not HISTORY_FILE.exists():
        HISTORY_FILE.write_text("[]", encoding="utf-8")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUTPUT_DIR / "assets").mkdir(parents=True, exist_ok=True)
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
    category_options = "\n".join([f'    <option value="{html.escape(cat)}">{html.escape(cat)}</option>' for cat in CATEGORIES])
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self' https://cdn.jsdelivr.net; connect-src 'self' https://cdn.jsdelivr.net; img-src 'self' data:; style-src 'self' https://fonts.googleapis.com 'unsafe-inline'; font-src https://fonts.gstatic.com; object-src 'none'; base-uri 'self';">
    <title>Roblox FFlag Tracker</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
    <style>
        :root {{
            --primary-green: #34d399;
            --primary-blue: #60a5fa;
            --primary-red: #f87171;
            --primary-yellow: #fbbf24;
            --historical-green: #10b981;
            --historical-blue: #3b82f6;
            --historical-red: #ef4444;
            --bg-opacity: 0.15;
            --text-color: #fff;
            --bg-color: linear-gradient(135deg,#4f46e5,#3b82f6,#06b6d4,#14b8a6);
            --high-contrast-bg: #000;
            --high-contrast-text: #fff;
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
            --text-color: #333;
            --bg-opacity: 0.05;
            --bg-color: linear-gradient(135deg,#e0f2fe,#bfdbfe,#a5f3fc,#99f6e4);
        }}
        body.high-contrast {{
            --bg-color: var(--high-contrast-bg);
            --text-color: var(--high-contrast-text);
            --bg-opacity: 1;
            background: var(--high-contrast-bg);
        }}
        @keyframes gradientBG {{
            0% {{background-position:0% 50%;}}
            50% {{background-position:100% 50%;}}
            100% {{background-position:0% 50%;}}
        }}
        @media (prefers-reduced-motion: reduce) {{
            * {{
                animation-duration: 0s !important;
                transition-duration: 0s !important;
            }}
            #particleCanvas {{ display: none; }}
        }}
        header {{
            text-align: center;
            padding: 60px 20px;
            text-shadow: 0 0 12px rgba(0,0,0,0.3);
        }}
        header h1 {{
            font-size: 3rem;
            font-weight: 700;
        }}
        .stats {{
            display: flex;
            justify-content: center;
            gap: 30px;
            flex-wrap: wrap;
            max-width: 1200px;
            margin: -40px auto 40px;
            position: relative;
            z-index: 2;
        }}
        .badge {{
            flex: 1;
            min-width: 220px;
            text-align: center;
            padding: 25px;
            border-radius: 16px;
            font-weight: 700;
            backdrop-filter: blur(10px);
            background: #ffffff;
            color: #0b1220;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            transition: transform 0.3s ease, box-shadow 0.3s ease, border 0.3s ease;
        }}
        body.high-contrast .badge {{
            background: var(--high-contrast-bg);
            border: 2px solid var(--high-contrast-text);
        }}
        .badge:hover {{
            transform: translateY(-8px);
            box-shadow: 0 14px 40px rgba(0,0,0,0.4);
            border: 2px solid var(--primary-green);
        }}
        .added {{
            border-left: 6px solid var(--primary-green);
        }}
        .added::before {{
            content: "✅ Added: ";
            font-size: 0.9rem;
        }}
        .changed {{
            border-left: 6px solid var(--primary-blue);
        }}
        .changed::before {{
            content: "🔄 Changed: ";
            font-size: 0.9rem;
        }}
        .removed {{
            border-left: 6px solid var(--primary-red);
        }}
        .removed::before {{
            content: "❌ Removed: ";
            font-size: 0.9rem;
        }}
        .net {{
            border-left: 6px solid var(--primary-yellow);
        }}
        .net::before {{
            content: "Net Changes: ";
            font-size: 0.9rem;
        }}
        .percent {{
            border-left: 6px solid var(--primary-blue);
        }}
        .percent::before {{
            content: "% Change: ";
            font-size: 0.9rem;
        }}
        .percent.positive {{
            border-left-color: var(--primary-green);
        }}
        .percent.negative {{
            border-left-color: var(--primary-red);
        }}
        .historical-added {{
            border-left: 6px solid var(--historical-green);
        }}
        .historical-added::before {{
            content: "📈 Historical Added: ";
            font-size: 0.9rem;
        }}
        .historical-changed {{
            border-left: 6px solid var(--historical-blue);
        }}
        .historical-changed::before {{
            content: "📈 Historical Changed: ";
            font-size: 0.9rem;
        }}
        .historical-removed {{
            border-left: 6px solid var(--historical-red);
        }}
        .historical-removed::before {{
            content: "📉 Historical Removed: ";
            font-size: 0.9rem;
        }}
        .last-run {{
            text-align: center;
            margin: 20px 0;
            font-style: italic;
            color: #eee;
        }}
        body.high-contrast .last-run {{
            color: var(--high-contrast-text);
        }}
        section {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }}
        .report-container {{
            background: rgba(255,255,255,var(--bg-opacity));
            backdrop-filter: blur(10px);
            border-radius: 16px;
            box-shadow: 0 12px 36px rgba(0,0,0,0.25);
            padding: 15px;
            position: relative;
            min-height: 75vh;
        }}
        body.high-contrast .report-container {{
            background: var(--high-contrast-bg);
            border: 2px solid var(--high-contrast-text);
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
            min-height: 75vh;
            border-radius: 12px;
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
        body.high-contrast input#searchInput {{
            background: var(--high-contrast-bg);
            border: 1px solid var(--high-contrast-text);
            color: var(--high-contrast-text);
        }}
        select {{
            padding: 12px;
            margin: 10px;
            border-radius: 12px;
            background: rgba(0,0,0,0.2);
            color: var(--text-color);
        }}
        body.high-contrast select {{
            background: var(--high-contrast-bg);
            border: 1px solid var(--high-contrast-text);
            color: var(--high-contrast-text);
        }}
        body.light input#searchInput,
        body.light select,
        body.light button {{
            background: #fff !important;
            color: #111 !important;
            border: 1px solid #ccc !important;
        }}
        body.light .copy-btn {{
            background: #fbbf24 !important;
            color: #111 !important;
        }}
        button {{
            padding: 10px 20px;
            border-radius: 8px;
            background: var(--primary-blue);
            color: white;
            border: none;
            cursor: pointer;
        }}
        body.high-contrast button {{
            background: var(--high-contrast-text);
            color: var(--high-contrast-bg);
            border: 1px solid var(--high-contrast-text);
        }}
        button:hover {{
            background: var(--primary-green);
        }}
        body.high-contrast button:hover {{
            background: var(--primary-green);
            color: var(--high-contrast-text);
        }}
        .copy-btn {{
            margin-left: 10px;
            padding: 5px 10px;
            font-size: 0.8rem;
            background: var(--primary-yellow);
        }}
        body.high-contrast .copy-btn {{
            background: var(--high-contrast-text);
            color: var(--high-contrast-bg);
        }}
        .commit-card {{
            background: rgba(255,255,255,0.2);
            border-radius: 8px;
            padding: 15px;
            margin-bottom: 20px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.2);
        }}
        body.high-contrast .commit-card {{
            background: var(--high-contrast-bg);
            border: 2px solid var(--high-contrast-text);
        }}
        h3 {{
            cursor: pointer;
        }}
        ul {{
            overflow: hidden;
            transition: max-height 0.3s ease;
            list-style-type: none;
            padding-left: 0;
        }}
        footer {{
            text-align: center;
            margin-top: 60px;
            padding: 25px;
            font-size: 0.9rem;
            color: #eee;
        }}
        body.high-contrast footer {{
            color: var(--high-contrast-text);
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
        body.high-contrast canvas#particleCanvas {{
            display: none;
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
        body.high-contrast th, body.high-contrast td {{
            border: 1px solid var(--high-contrast-text);
        }}
        th {{
            background: rgba(0,0,0,0.2);
        }}
        body.high-contrast th {{
            background: var(--high-contrast-bg);
            color: var(--high-contrast-text);
        }}
        :focus {{
            outline: 3px solid #ffbf47;
            outline-offset: 3px;
        }}
        button:focus, a:focus {{
            box-shadow: 0 0 0 3px rgba(96,165,250,0.3);
        }}
        .skip-link {{
            position: absolute;
            left: -999px;
            top: auto;
            width: 1px;
            height: 1px;
            overflow: hidden;
        }}
        .skip-link:focus {{
            left: 10px;
            top: 10px;
            width: auto;
            height: auto;
            z-index: 9999;
        }}
        .error-message {{
            color: var(--primary-red);
            text-align: center;
            padding: 20px;
        }}
    </style>
</head>
<body>
    <a class="skip-link" href="#reportContent">Skip to report</a>
    <canvas id="particleCanvas"></canvas>
    <header>
        <h1>Roblox Client FFlag Tracker</h1>
        <button id="themeToggle">Toggle Theme</button>
        <button id="contrastToggle">High Contrast</button>
    </header>
    <div class="stats">
        <div class="badge added" aria-label="Added flags">
            <span id="flags-added">{html.escape(str(added))}</span>
        </div>
        <div class="badge changed" aria-label="Changed flags">
            <span id="flags-changed">{html.escape(str(changed))}</span>
        </div>
        <div class="badge removed" aria-label="Removed flags">
            <span id="flags-removed">{html.escape(str(removed))}</span>
        </div>
        <div class="badge net" aria-label="Net changes">
            <span id="net-changes">{html.escape(str(net_changes))}</span>
        </div>
        <div class="badge percent" aria-label="Percent change">
            <span id="percent-change">{html.escape(str(percent_change)):.2f}</span>%
        </div>
        <div class="badge historical-added" aria-label="Historical added">
            <span id="historical-added">{html.escape(str(total_historical_added))}</span>
        </div>
        <div class="badge historical-changed" aria-label="Historical changed">
            <span id="historical-changed">{html.escape(str(total_historical_changed))}</span>
        </div>
        <div class="badge historical-removed" aria-label="Historical removed">
            <span id="historical-removed">{html.escape(str(total_historical_removed))}</span>
        </div>
    </div>
    <p class="last-run">Last Run: <span id="last-run">{html.escape(last_run)}</span></p>
    <section>
        <label for="searchInput" class="sr-only">Search flags</label>
        <input type="text" id="searchInput" placeholder="Search flags..." aria-label="Search flags">
        <label for="categoryFilter" class="sr-only">Filter by category</label>
        <select id="categoryFilter" aria-label="Filter by category">
            <option value="">All Categories</option>
            {category_options}
        </select>
        <label for="sortSelect" class="sr-only">Sort options</label>
        <select id="sortSelect" aria-label="Sort options">
            <option value="">Sort by Name</option>
            <option value="freq">Sort by Frequency</option>
        </select>
        <h2>Summary</h2>
        <table id="summaryTable" aria-label="Summary of flag changes by category"></table>
        <h2>📄 Full Markdown Report</h2>
        <a href="FFlag_Report.md" target="_blank">View Markdown Report</a>
        <h2>📊 Latest Full Report</h2>
        <div class="report-container">
            <div id="loadingSpinner" aria-label="Loading report"></div>
            <div id="reportContent" role="region" aria-live="polite"></div>
        </div>
        <button id="exportCSV" aria-label="Export report as CSV">Export CSV</button>
        <button id="exportJSON" aria-label="Export report as JSON">Export JSON</button>
        <canvas id="trendChart" aria-label="Trend chart of flag changes"></canvas>
    </section>
    <footer>Built with ❤️ by FFlag Tracker • Updated automatically</footer>
    <script src="assets/app.js" defer></script>
</body>
</html>"""
    index_html.write_text(html_content, encoding="utf-8")
    sw_content = """
const CACHE_NAME = "fflag-cache-v1";
const URLS_TO_CACHE = [
    "./",
    "index.html",
    "summary.json",
    "commits.json",
    "history.json",
    "assets/app.js"
];

self.addEventListener("install", event => {
    event.waitUntil(
        caches.open(CACHE_NAME).then(cache => cache.addAll(URLS_TO_CACHE))
    );
});

self.addEventListener("fetch", event => {
    event.respondWith(
        caches.match(event.request).then(response => response || fetch(event.request))
    );
});
"""
    sw_js.write_text(sw_content, encoding="utf-8")
    app_js_content = open(app_js, 'r', encoding="utf-8").read()
    app_js.write_text(app_js_content, encoding="utf-8")
    log.info(f"Landing page written: {index_html}")
    log.info(f"Service worker written: {sw_js}")
    log.info(f"App script written: {app_js}")

# ============================
# Publish Helper
# ============================
def publish_output_to_github():
    token = os.getenv('GITHUB_TOKEN')
    repo = os.getenv('GITHUB_REPO')
    branch = os.getenv('GITHUB_PAGES_BRANCH', 'gh-pages')
    if not token or not repo:
        log.warning("GITHUB_TOKEN or GITHUB_REPO not set. Skipping publish.")
        return
    remote = f"https://x-access-token:{token}@github.com/{repo}.git"
    try:
        try:
            run_cmd(f"git checkout {branch}")
        except subprocess.CalledProcessError:
            run_cmd(f"git checkout --orphan {branch}")
        for item in os.listdir(WORKSPACE):
            if item != '.git':
                path = WORKSPACE / item
                if path.is_dir():
                    shutil.rmtree(path)
                else:
                    os.remove(path)
        for item in OUTPUT_DIR.iterdir():
            dest = WORKSPACE / item.name
            if item.is_dir():
                shutil.copytree(item, dest)
            else:
                shutil.copy(item, dest)
        run_cmd("git add .")
        try:
            run_cmd('git commit -m "Publish FFlag Tracker output"')
            run_cmd(f"git push {remote} {branch}")
            log.info(f"Successfully published to {branch} branch.")
        except subprocess.CalledProcessError as e:
            if "nothing to commit" in e.stderr:
                log.info("No changes to publish.")
            else:
                raise
    except Exception as e:
        log.error(f"Publish failed: {e}")

# ============================
# Main Execution
# ============================
async def main() -> None:
    try:
        startup_delay = int(os.getenv('STARTUP_DELAY_SECONDS', '0'))
        await asyncio.sleep(startup_delay)
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
            if os.getenv('PRUNE_CACHE', 'true').lower() == 'true':
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
        if os.getenv('PUBLISH_GH', 'false').lower() == 'true':
            publish_output_to_github()
        log.info("All done! Reports and dashboard ready.")
    except Exception as e:
        log.error(f"Main execution failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())
