#!/usr/bin/env python3
import os
import subprocess
import datetime
import json
import html
import shutil
import sys
import argparse
import asyncio
import logging
import re
import tempfile
from pathlib import Path
from zoneinfo import ZoneInfo
from collections import defaultdict
from filelock import FileLock

try:
    from jsonschema import validate as json_validate, ValidationError
except ImportError:
    json_validate = None
    ValidationError = Exception

try:
    from openai import AsyncOpenAI, RateLimitError
except ImportError:
    AsyncOpenAI = None

SCRIPT_DIR = Path(__file__).resolve().parent
WORKSPACE = Path(os.getenv("GITHUB_WORKSPACE", str(SCRIPT_DIR))).resolve()
OUTPUT_DIR = WORKSPACE / "output"
ASSETS_SRC = SCRIPT_DIR / "assets"
CUSTOM_SW_SRC = SCRIPT_DIR / "custom-sw" / "sw.js"
OUTPUT_MD = OUTPUT_DIR / "FFlag_Report.md"
OUTPUT_HTML = OUTPUT_DIR / "FFlag_Report.html"
OUTPUT_JSON = OUTPUT_DIR / "FFlag_Report.json"
CACHE_FILE = OUTPUT_DIR / "fflag_cache.json"
DIFF_CACHE_FILE = OUTPUT_DIR / "diff_cache.json"
HISTORY_FILE = OUTPUT_DIR / "history.json"
FAILED_FLAGS_FILE = OUTPUT_DIR / "failed_flags.json"
KEY_INDEX_FILE = OUTPUT_DIR / ".key_index.json"
SUMMARY_FILE = OUTPUT_DIR / "summary.json"
COMMITS_INDEX_FILE = OUTPUT_DIR / "commits_index.json"
MANIFEST_FILE = OUTPUT_DIR / "manifest.json"
REPO_URL = "https://github.com/MaximumADHD/Roblox-FFlag-Tracker.git"
TARGET_FILE = "PCDesktopClient.json"
DAYS = 350
HISTORY_DAYS = 350
AI_BATCH_SIZE = 5
AI_CONCURRENT_LIMIT = 5
AI_BATCH_DELAY = 1.0
MAX_RETRIES = 3
MAX_REPORT_COMMITS = 200
COMMIT_BATCH_SIZE = 30
COMMIT_CHUNK_SIZE = 20
SUBPROCESS_TIMEOUT = 120
DEBUG = os.getenv("DEBUG", "true").lower() == "true"
TIMEZONE = ZoneInfo("Asia/Manila")

parser = argparse.ArgumentParser(description="Roblox FFlag Tracker")
parser.add_argument("--dry-run", action="store_true", help="Skip AI enrichment")
parser.add_argument("--force-refresh", action="store_true", help="Force reclone and re-enrich")
args = parser.parse_args()

logging.basicConfig(
    level=logging.DEBUG if DEBUG else logging.INFO,
    format="[%(levelname)s] %(message)s (%(asctime)s)"
)
log = logging.getLogger(__name__)

CATEGORIES = {
    "Graphics": ["Graphics", "Lighting", "Render", "GPU", "VSync", "Shadow", "Texture"],
    "Physics": ["Physics", "Solver", "Collision", "Humanoid", "Constraint", "Ragdoll", "Mass", "Gravity", "Force"],
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

FLAG_INFO = {}
FAILED_FLAGS = []


def atomic_write(path, content, encoding="utf-8"):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=p.parent, suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding=encoding) as f:
            f.write(content)
        shutil.move(tmp, str(p))
    except Exception:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise


def safe_read_json(path, default=None):
    if default is None:
        default = {}
    if not Path(path).exists():
        return default if not isinstance(default, list) else list(default)
    try:
        data = json.loads(Path(path).read_text(encoding="utf-8"))
        if isinstance(default, list) and not isinstance(data, list):
            return list(default)
        if isinstance(default, dict) and not isinstance(data, dict):
            return dict(default)
        return data
    except (json.JSONDecodeError, OSError) as e:
        log.warning(f"Corrupted {Path(path).name}: {e}")
        return default if not isinstance(default, list) else list(default)


def load_caches():
    global FLAG_INFO, FAILED_FLAGS
    FLAG_INFO = safe_read_json(CACHE_FILE, {})
    FAILED_FLAGS = safe_read_json(FAILED_FLAGS_FILE, [])
    if args.force_refresh:
        FLAG_INFO.clear()
        FAILED_FLAGS.clear()
        log.info("Force refresh: cleared all caches")


def validate_sha(h):
    return bool(h and re.match(r"^[0-9a-f]{7,40}$", h.strip()))


def run_cmd(cmd, cwd=None):
    try:
        result = subprocess.run(
            cmd, shell=True, cwd=cwd, capture_output=True, text=True, timeout=SUBPROCESS_TIMEOUT
        )
        if result.returncode != 0:
            log.error(f"Command failed ({result.returncode}): {cmd}")
            log.error(result.stderr.strip())
            raise subprocess.CalledProcessError(
                result.returncode, cmd, output=result.stdout, stderr=result.stderr
            )
        return result.stdout.strip()
    except subprocess.TimeoutExpired:
        log.error(f"Timed out ({SUBPROCESS_TIMEOUT}s): {cmd}")
        raise


def categorize_flag(flag_name):
    if not isinstance(flag_name, str):
        return "Other"
    lower = flag_name.lower()
    for cat, keywords in CATEGORIES.items():
        if any(k.lower() in lower for k in keywords):
            return cat
    return "Other"


def format_value(v):
    if isinstance(v, bool):
        return str(v).capitalize()
    return str(v)


def load_api_keys(env_var):
    keys = [k.strip() for k in os.getenv(env_var, "").split(",") if k.strip()]
    if not keys:
        log.warning(f"⚠ No {env_var} found.")
    return keys


OPENAI_KEYS = load_api_keys("OPENAI_API_KEYS")
if not OPENAI_KEYS and not args.dry_run:
    log.warning("⚠ No OpenAI API keys. AI enrichment skipped.")


def get_next_api_key():
    if not OPENAI_KEYS:
        return None
    lock = FileLock(str(KEY_INDEX_FILE) + ".lock", timeout=10)
    with lock:
        index_data = safe_read_json(KEY_INDEX_FILE, {"openai_idx": 0})
        idx = index_data.get("openai_idx", 0)
        key = OPENAI_KEYS[idx % len(OPENAI_KEYS)]
        index_data["openai_idx"] = idx + 1
        atomic_write(KEY_INDEX_FILE, json.dumps(index_data, indent=2))
    return key


cache_path = Path(os.environ.get("FFLAG_REPO_CACHE", ".fflag-repo-cache"))


def ensure_manifest_repo(repo_url=REPO_URL):
    if not re.match(r"^https://github\.com/[A-Za-z0-9_./-]+\.git$", repo_url):
        raise ValueError(f"Invalid repository URL: {repo_url}")
    if not args.force_refresh and cache_path.exists() and (cache_path / ".git").exists():
        log.info(f"Using cached repo at {cache_path}")
        try:
            if not (cache_path / TARGET_FILE).exists():
                raise FileNotFoundError(f"{TARGET_FILE} not found")
            subprocess.run(
                ["git", "-C", str(cache_path), "stash", "push", "--include-untracked", "-q"],
                check=False, timeout=30
            )
            subprocess.run(["git", "-C", str(cache_path), "pull", "--ff-only"], check=True, timeout=60)
            subprocess.run(
                ["git", "-C", str(cache_path), "stash", "pop"],
                check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=30
            )
            return cache_path
        except (subprocess.CalledProcessError, FileNotFoundError, subprocess.TimeoutExpired):
            log.warning("Cached repo update failed, recloning...")
            shutil.rmtree(cache_path, ignore_errors=True)
    log.info("Cloning manifest repo...")
    since_date = (datetime.datetime.now() - datetime.timedelta(days=DAYS + 30)).strftime("%Y-%m-%d")
    subprocess.run(
        ["git", "clone", f"--shallow-since={since_date}", repo_url, str(cache_path)],
        check=True, timeout=300
    )
    if not (cache_path / TARGET_FILE).exists():
        raise FileNotFoundError(f"{TARGET_FILE} not found in cloned repo")
    return cache_path


def get_commits(days=DAYS, manifest_repo=None):
    since = (datetime.datetime.now() - datetime.timedelta(days=days)).strftime("%Y-%m-%d")
    raw = run_cmd(f"git log --since='{since}' --pretty=format:%H -- {TARGET_FILE}", cwd=manifest_repo)
    if not raw:
        return []
    commits = [c.strip() for c in raw.splitlines() if validate_sha(c)]
    return commits[:MAX_REPORT_COMMITS]


def build_diff_for_commit(commit_hash, manifest_repo=None):
    header = run_cmd(
        f"git show --no-patch --pretty=format:'%h - %ci - %s' {commit_hash}", cwd=manifest_repo
    )
    diff = run_cmd(f"git show {commit_hash} -- {TARGET_FILE}", cwd=manifest_repo)
    try:
        prev_content = run_cmd(f"git show {commit_hash}~1:{TARGET_FILE}", cwd=manifest_repo)
        curr_content = run_cmd(f"git show {commit_hash}:{TARGET_FILE}", cwd=manifest_repo)
        prev_json = json.loads(prev_content) if prev_content else {}
        curr_json = json.loads(curr_content)
        added = []
        changed = []
        removed = []
        for key in curr_json:
            if key not in prev_json:
                added.append((key, curr_json[key]))
            elif prev_json[key] != curr_json[key]:
                changed.append((key, prev_json[key], curr_json[key]))
        for key in prev_json:
            if key not in curr_json:
                removed.append((key, prev_json[key]))
        return header, added, changed, removed
    except (json.JSONDecodeError, subprocess.CalledProcessError):
        log.debug(f"Falling back to line-by-line diff for {commit_hash[:8]}")
        added_dict = {}
        removed_dict = {}
        for line in diff.splitlines():
            if line.startswith("+++") or line.startswith("---"):
                continue
            is_add = line.startswith("+") and not line.startswith("+++")
            is_rem = line.startswith("-") and not line.startswith("---")
            if not is_add and not is_rem:
                continue
            snippet = line[1:].strip()
            if not (snippet.startswith('"') and ":" in snippet):
                continue
            if snippet.endswith(","):
                snippet = snippet[:-1]
            try:
                parsed = json.loads("{" + snippet + "}")
                target = added_dict if is_add else removed_dict
                for k, v in parsed.items():
                    target[k] = v
            except Exception:
                pass
        final_added = []
        final_changed = []
        final_removed = []
        for k, new_v in added_dict.items():
            if k in removed_dict:
                old_v = removed_dict.pop(k)
                if old_v != new_v:
                    final_changed.append((k, old_v, new_v))
            else:
                final_added.append((k, new_v))
        for k, old_v in removed_dict.items():
            final_removed.append((k, old_v))
        return header, final_added, final_changed, final_removed


async def async_build_diff(commit_hash, diff_cache, manifest_repo=None):
    if commit_hash in diff_cache:
        c = diff_cache[commit_hash]
        return (
            c["header"],
            [tuple(e) for e in c.get("added", []) if len(e) == 2],
            [tuple(e) for e in c.get("changed", []) if len(e) == 3],
            [tuple(e) for e in c.get("removed", []) if len(e) == 2],
        )
    header, added, changed, removed = await asyncio.get_running_loop().run_in_executor(
        None, lambda: build_diff_for_commit(commit_hash, manifest_repo)
    )
    diff_cache[commit_hash] = {
        "header": header,
        "added": [list(a) for a in added],
        "changed": [list(c) for c in changed],
        "removed": [list(r) for r in removed],
    }
    return header, added, changed, removed


async def build_report(commits, diff_cache, manifest_repo=None):
    report = []
    summary = {}
    flag_changes = defaultdict(int)
    total = len(commits)
    for i in range(0, total, COMMIT_BATCH_SIZE):
        batch = commits[i : i + COMMIT_BATCH_SIZE]
        log.info(f"Processing commits {i + 1}–{min(i + len(batch), total)} of {total}")
        tasks = [async_build_diff(c, diff_cache, manifest_repo) for c in batch]
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


def update_history(added, changed, removed, last_run):
    history = safe_read_json(HISTORY_FILE, [])
    current_date = last_run.split(" ")[0]
    entry = {"date": last_run, "added": added, "changed": changed, "removed": removed}
    if history and history[-1].get("date", "").split(" ")[0] == current_date:
        history[-1] = entry
    else:
        history.append(entry)
    history = history[-HISTORY_DAYS:]
    atomic_write(HISTORY_FILE, json.dumps(history, indent=2))


FLAG_SCHEMA = {
    "type": "object",
    "patternProperties": {
        "^(FFlag|DFFlag|DFInt|DFLog|SFFlag|FString|FInt|DFString)[A-Za-z0-9_]+$": {
            "type": "object",
            "properties": {"mechanism": {"type": "string"}, "purpose": {"type": "string"}},
            "required": ["mechanism", "purpose"],
        }
    },
    "additionalProperties": False,
}


def safe_json_parse(raw):
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        cleaned = re.sub(r"^```(?:json)?|```$", "", raw.strip(), flags=re.MULTILINE).strip()
        cleaned = re.sub(r",\s*([}\]])", r"\1", cleaned)
        try:
            return json.loads(cleaned)
        except json.JSONDecodeError:
            return None


def normalize_ai_response(raw, flags):
    data = safe_json_parse(raw)
    if isinstance(data, list):
        return {f: obj for f, obj in zip(flags, data) if isinstance(obj, dict)}
    return data


def extract_and_validate_json(text):
    data = safe_json_parse(text)
    if data is None:
        raise json.JSONDecodeError("Invalid JSON after repair", text, 0)
    if json_validate:
        try:
            json_validate(instance=data, schema=FLAG_SCHEMA)
        except ValidationError:
            data = {
                k: v
                for k, v in data.items()
                if re.match(r"^(FFlag|DFFlag|DFInt|DFLog|SFFlag|FString|FInt|DFString)[A-Za-z0-9_]+$", k)
            }
    return data


async def ai_enrich_flags_batch(batch):
    if args.dry_run:
        return {f: {"mechanism": "N/A (dry run)", "purpose": "N/A (dry run)"} for f in batch}
    if not OPENAI_KEYS or not AsyncOpenAI:
        return {}
    system_prompt = (
        "Respond ONLY with valid JSON.\n"
        "Each flag must be the key of an object.\n"
        "The value must be another object with exactly two fields:\n"
        "- mechanism (short, technical)\n"
        "- purpose (player-facing benefit)\n"
        "Example:\n"
        '{\n  "FFlagExample": {"mechanism": "...", "purpose": "..."},\n'
        '  "DFFlagOther": {"mechanism": "...", "purpose": "..."}\n}'
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
                    {"role": "user", "content": user_prompt},
                ],
                temperature=0.3,
            )
            text = response.choices[0].message.content.strip()
            parsed = normalize_ai_response(text, batch)
            parsed = extract_and_validate_json(json.dumps(parsed))
            if parsed:
                return parsed
            return {f: {"mechanism": "N/A (invalid)", "purpose": "N/A (invalid)"} for f in batch}
        except RateLimitError as e:
            retry_after = 60
            if hasattr(e, "response") and e.response and e.response.headers.get("Retry-After"):
                try:
                    retry_after = min(int(e.response.headers["Retry-After"]), 60)
                except ValueError:
                    pass
            log.warning(f"Rate limit (attempt {attempt + 1}). Waiting {retry_after}s.")
            await asyncio.sleep(retry_after)
        except json.JSONDecodeError:
            system_prompt = "Respond strictly in valid JSON with 'mechanism' and 'purpose' for each Roblox FFlag."
            await asyncio.sleep(1)
        except Exception as e:
            log.error(f"AI batch failed (attempt {attempt + 1}): {e}")
            await asyncio.sleep(2**attempt)
    return {f: {"mechanism": "N/A (failed)", "purpose": "N/A (failed)"} for f in batch}


async def process_batches(batches):
    semaphore = asyncio.Semaphore(AI_CONCURRENT_LIMIT)
    failed_flags = []

    async def limited_task(b):
        async with semaphore:
            result = await ai_enrich_flags_batch(b)
            await asyncio.sleep(AI_BATCH_DELAY)
            return result, b

    tasks = [limited_task(b) for b in batches]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    for res in results:
        if isinstance(res, Exception):
            log.error(f"Batch enrichment error: {res}")
            continue
        info_batch, batch_flags = res
        for f in batch_flags:
            info = info_batch.get(f, {})
            if info and info.get("mechanism") and info.get("purpose") and not info["mechanism"].startswith("N/A"):
                FLAG_INFO[f] = {"mechanism": info["mechanism"], "purpose": info["purpose"]}
                if f in FAILED_FLAGS:
                    FAILED_FLAGS.remove(f)
            else:
                FLAG_INFO[f] = {"mechanism": info.get("mechanism", "N/A"), "purpose": info.get("purpose", "N/A")}
                if f not in failed_flags:
                    failed_flags.append(f)
    return failed_flags


def should_enrich_flag(flag):
    if args.dry_run:
        return False
    if flag not in FLAG_INFO:
        return True
    info = FLAG_INFO[flag]
    return not (info.get("mechanism") and info.get("purpose") and not info["mechanism"].startswith("N/A"))


async def generate_flag_info_batch(flags):
    global FAILED_FLAGS
    retryable = list(set(FAILED_FLAGS))
    if retryable:
        log.info(f"Retrying {len(retryable)} previously failed flags")
        batches = [retryable[i : i + AI_BATCH_SIZE] for i in range(0, len(retryable), AI_BATCH_SIZE)]
        still_failed = await process_batches(batches)
    else:
        still_failed = []
    new_flags = [f for f in flags if should_enrich_flag(f)]
    if new_flags:
        log.info(f"Enriching {len(new_flags)} new flags via AI")
        batches = [new_flags[i : i + AI_BATCH_SIZE] for i in range(0, len(new_flags), AI_BATCH_SIZE)]
        still_failed += await process_batches(batches)
    FAILED_FLAGS = list(set(still_failed))
    atomic_write(FAILED_FLAGS_FILE, json.dumps(FAILED_FLAGS, indent=2))
    atomic_write(CACHE_FILE, json.dumps(FLAG_INFO, indent=2))
    return FAILED_FLAGS


def get_flag_info(flag):
    return FLAG_INFO.get(flag, {"mechanism": "N/A", "purpose": "N/A"})


def compute_stats(summary):
    added = sum(summary.get((cat, "Added"), 0) for cat in CATEGORIES)
    changed = sum(summary.get((cat, "Changed"), 0) for cat in CATEGORIES)
    removed = sum(summary.get((cat, "Removed"), 0) for cat in CATEGORIES)
    return added, changed, removed


def compute_history_stats(history):
    ha = sum(e.get("added", 0) for e in history)
    hc = sum(e.get("changed", 0) for e in history)
    hr = sum(e.get("removed", 0) for e in history)
    pct = 0.0
    if len(history) > 1:
        prev = history[-2]
        pt = prev.get("added", 0) + prev.get("changed", 0) + prev.get("removed", 0)
        ct = history[-1].get("added", 0) + history[-1].get("changed", 0) + history[-1].get("removed", 0)
        pct = round(((ct - pt) / pt * 100), 2) if pt > 0 else 0.0
    return ha, hc, hr, pct


def export_reports(report, summary, flag_changes):
    last_run = datetime.datetime.now(TIMEZONE).strftime("%Y-%m-%d %I:%M:%S %p %Z")
    added, changed, removed = compute_stats(summary)
    net = added - removed
    history = safe_read_json(HISTORY_FILE, [])
    hist_a, hist_c, hist_r, pct = compute_history_stats(history)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    md = [f"# Roblox Client FFlag Intel Report ({DAYS} Days)\n"]
    md.append(f"**Last Run:** {last_run}\n")
    md.append(f"| Metric | Count |\n|---|---|\n| Added | {added} |\n| Changed | {changed} |"
              f"\n| Removed | {removed} |\n| Net | {net} |\n| % Change | {pct}% |\n")
    md.append("## Summary\n\n| Category | Added | Changed | Removed | Total |\n|---|---|---|---|---|")
    for cat in CATEGORIES:
        a = summary.get((cat, "Added"), 0)
        c = summary.get((cat, "Changed"), 0)
        r = summary.get((cat, "Removed"), 0)
        md.append(f"| {cat} | {a} | {c} | {r} | {a + c + r} |")
    if not report:
        md.append(f"\n*No flag changes in the last {DAYS} days.*")
    else:
        for header, changes in report:
            md.append(f"\n---\n## {header}\n")
            grouped = {}
            for typ, cat, flag, *vals in changes:
                grouped.setdefault((typ, cat), []).append((flag, *vals))
            for (typ, cat), items in grouped.items():
                icon = {"Added": "✅", "Changed": "🔄", "Removed": "❌"}.get(typ, "")
                md.append(f"\n### {icon} {typ} — {cat}\n")
                if typ == "Changed":
                    md.append("| Flag | Old | New | Mechanism | Purpose |\n|---|---|---|---|---|")
                    for item in items:
                        info = get_flag_info(item[0])
                        md.append(f"| `{item[0]}` | {format_value(item[1])} | {format_value(item[2])} | {info['mechanism']} | {info['purpose']} |")
                elif typ == "Added":
                    md.append("| Flag | Value | Mechanism | Purpose |\n|---|---|---|---|")
                    for item in items:
                        info = get_flag_info(item[0])
                        md.append(f"| `{item[0]}` | {format_value(item[1])} | {info['mechanism']} | {info['purpose']} |")
                else:
                    md.append("| Flag | Was | Mechanism | Purpose |\n|---|---|---|---|")
                    for item in items:
                        info = get_flag_info(item[0])
                        md.append(f"| `{item[0]}` | {format_value(item[1])} | {info['mechanism']} | {info['purpose']} |")
    atomic_write(OUTPUT_MD, "\n".join(md))

    hl = ["<!DOCTYPE html><html lang='en'><head><meta charset='UTF-8'>"]
    hl.append("<meta name='viewport' content='width=device-width,initial-scale=1.0'>")
    hl.append("<title>FFlag Report</title><style>")
    hl.append("*{box-sizing:border-box}body{font-family:system-ui,-apple-system,sans-serif;margin:0;padding:20px;background:#0f172a;color:#e2e8f0}")
    hl.append("h1{color:#60a5fa}h2{color:#34d399;border-bottom:1px solid #334155;padding-bottom:8px}h3{color:#fbbf24}")
    hl.append("details{background:#1e293b;border-radius:8px;padding:12px;margin:8px 0}")
    hl.append("summary{cursor:pointer;font-weight:600}ul{list-style:none;padding:0}")
    hl.append("li{padding:6px 0;border-bottom:1px solid #1e293b;font-size:.9rem}")
    hl.append(".a{color:#34d399}.c{color:#60a5fa}.r{color:#f87171}")
    hl.append("</style></head><body>")
    hl.append("<h1>Roblox FFlag Report</h1>")
    if not report:
        hl.append(f"<p>No changes in {DAYS} days.</p>")
    else:
        for header, changes in report:
            hl.append(f"<h2>{html.escape(header)}</h2>")
            grouped = {}
            for typ, cat, flag, *vals in changes:
                grouped.setdefault((typ, cat), []).append((flag, *vals))
            for (typ, cat), items in grouped.items():
                cls = {"Added": "a", "Changed": "c", "Removed": "r"}.get(typ, "")
                hl.append(f"<details><summary class='{cls}'>{html.escape(typ)} in {html.escape(cat)} ({len(items)})</summary><ul>")
                for item in items:
                    flag = item[0]
                    info = get_flag_info(flag)
                    if typ == "Added":
                        desc = f"= {html.escape(format_value(item[1]))}"
                    elif typ == "Changed":
                        desc = f"{html.escape(format_value(item[1]))} → {html.escape(format_value(item[2]))}"
                    else:
                        desc = f"was {html.escape(format_value(item[1]))}"
                    hl.append(f"<li><strong>{html.escape(flag)}</strong> {desc}<br><small>{html.escape(info['mechanism'])} — {html.escape(info['purpose'])}</small></li>")
                hl.append("</ul></details>")
    hl.append("</body></html>")
    atomic_write(OUTPUT_HTML, "\n".join(hl))

    json_data = {
        "last_run": last_run,
        "days": DAYS,
        "added_total": added,
        "changed_total": changed,
        "removed_total": removed,
        "net_changes": net,
        "percent_change": pct,
        "total_historical_added": hist_a,
        "total_historical_changed": hist_c,
        "total_historical_removed": hist_r,
        "historical_avg_added": round(hist_a / max(len(history), 1), 2),
        "historical_avg_changed": round(hist_c / max(len(history), 1), 2),
        "historical_avg_removed": round(hist_r / max(len(history), 1), 2),
        "summary": {
            cat: {
                "added": summary.get((cat, "Added"), 0),
                "changed": summary.get((cat, "Changed"), 0),
                "removed": summary.get((cat, "Removed"), 0),
            }
            for cat in CATEGORIES
        },
        "report": [],
    }
    for header, changes in report:
        grouped = {}
        for typ, cat, flag, *vals in changes:
            info = get_flag_info(flag)
            entry = {
                "name": flag,
                "mechanism": info["mechanism"],
                "purpose": info["purpose"],
                "freq": flag_changes.get(flag, 0),
            }
            if typ == "Added":
                entry["old_value"] = None
                entry["new_value"] = format_value(vals[0])
            elif typ == "Changed":
                entry["old_value"] = format_value(vals[0])
                entry["new_value"] = format_value(vals[1])
            else:
                entry["old_value"] = format_value(vals[0])
                entry["new_value"] = None
            grouped.setdefault(f"{typ}_{cat}", []).append(entry)
        json_data["report"].append({"header": header, "grouped": grouped})
    json_data["report"] = json_data["report"][-MAX_REPORT_COMMITS:]
    atomic_write(OUTPUT_JSON, json.dumps(json_data, indent=2))

    summary_data = {k: v for k, v in json_data.items() if k != "report"}
    commits_data = json_data["report"]
    chunks = []
    for i in range(0, max(len(commits_data), 1), COMMIT_CHUNK_SIZE):
        chunk = commits_data[i : i + COMMIT_CHUNK_SIZE]
        fname = f"commits_{i // COMMIT_CHUNK_SIZE}.json"
        atomic_write(OUTPUT_DIR / fname, json.dumps(chunk, indent=2))
        chunks.append(fname)
    summary_data["num_chunks"] = len(chunks)
    atomic_write(SUMMARY_FILE, json.dumps(summary_data, indent=2))

    index_data = {"total": len(commits_data), "chunk_size": COMMIT_CHUNK_SIZE, "chunks": chunks}
    atomic_write(COMMITS_INDEX_FILE, json.dumps(index_data, indent=2))

    log.info(f"Reports: {OUTPUT_MD.name}, {OUTPUT_HTML.name}, {OUTPUT_JSON.name}, {SUMMARY_FILE.name}, {len(chunks)} chunks")


def ensure_assets():
    dst = OUTPUT_DIR / "assets"
    if dst.exists():
        shutil.rmtree(dst)
    if ASSETS_SRC.exists():
        shutil.copytree(ASSETS_SRC, dst)
        log.info(f"Copied assets → {dst}")
    else:
        dst.mkdir(parents=True, exist_ok=True)
        log.warning("assets/ source not found, created empty dir")


def ensure_service_worker():
    dst = OUTPUT_DIR / "sw.js"
    if CUSTOM_SW_SRC.exists():
        shutil.copy2(CUSTOM_SW_SRC, dst)
        log.info(f"Copied custom SW → {dst}")
    else:
        sw = (
            'const C="fflag-v2",U=["./","index.html","summary.json","commits_index.json",'
            '"history.json","assets/app.js","assets/chart.umd.js","assets/hammer.min.js",'
            '"assets/chartjs-plugin-zoom.js"];'
            "self.addEventListener('install',e=>{e.waitUntil(caches.open(C).then(c=>c.addAll(U)))});"
            "self.addEventListener('fetch',e=>{e.respondWith(caches.match(e.request)"
            ".then(r=>r||fetch(e.request).then(res=>{if(res.ok){const cl=res.clone();"
            "caches.open(C).then(c=>c.put(e.request,cl))}return res})"
            ".catch(()=>caches.match('index.html'))))});"
            "self.addEventListener('activate',e=>{e.waitUntil(caches.keys()"
            ".then(ks=>Promise.all(ks.filter(k=>k!==C).map(k=>caches.delete(k)))))});"
        )
        atomic_write(dst, sw)
        log.info(f"Generated fallback SW → {dst}")


def ensure_manifest():
    m = {
        "name": "Roblox FFlag Tracker",
        "short_name": "FFlags",
        "start_url": ".",
        "display": "standalone",
        "background_color": "#0f172a",
        "theme_color": "#3b82f6",
        "description": "Track Roblox client feature flag changes",
        "icons": [{"src": "assets/favicon.ico", "sizes": "64x64", "type": "image/x-icon"}],
    }
    atomic_write(MANIFEST_FILE, json.dumps(m, indent=2))


def ensure_landing_page(added, changed, removed, last_run, summary=None):
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    net = added - removed
    history = safe_read_json(HISTORY_FILE, [])
    hist_a, hist_c, hist_r, pct = compute_history_stats(history)
    pct_cls = "positive" if pct >= 0 else "negative"
    cat_opts = "\n".join(f'<option value="{html.escape(c)}">{html.escape(c)}</option>' for c in CATEGORIES)
    s_rows = ""
    if summary:
        for cat in CATEGORIES:
            a = summary.get((cat, "Added"), 0)
            c = summary.get((cat, "Changed"), 0)
            r = summary.get((cat, "Removed"), 0)
            t = a + c + r
            s_rows += f"<tr><td>{html.escape(cat)}</td><td>{a}</td><td>{c}</td><td>{r}</td><td>{t}</td></tr>\n"
    else:
        s_rows = "<tr><td colspan='5'>No data</td></tr>"
    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="Live Roblox client feature flag tracker with AI analysis">
<meta name="theme-color" content="#3b82f6">
<meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; font-src 'self'; connect-src 'self'; object-src 'none'; base-uri 'self';">
<title>Roblox FFlag Tracker</title>
<link rel="icon" href="assets/favicon.ico">
<link rel="manifest" href="manifest.json">
<style>
:root{{--g:#34d399;--b:#60a5fa;--r:#f87171;--y:#fbbf24;--bg:#0f172a;--bg2:#1e293b;--tx:#e2e8f0;--card:rgba(30,41,59,.85);--radius:14px;--shadow:0 8px 32px rgba(0,0,0,.4)}}
*{{box-sizing:border-box;margin:0;padding:0}}
html{{scroll-behavior:smooth}}
body{{font-family:system-ui,-apple-system,'Segoe UI',Roboto,sans-serif;background:var(--bg);color:var(--tx);overflow-x:hidden;line-height:1.6}}
body.light{{--bg:#f1f5f9;--bg2:#fff;--tx:#1e293b;--card:rgba(255,255,255,.9)}}
body.high-contrast{{--bg:#000;--bg2:#000;--tx:#fff;--card:#000}}
.skip{{position:absolute;left:-999px;top:auto;width:1px;height:1px;overflow:hidden;z-index:999}}
.skip:focus{{left:10px;top:10px;width:auto;height:auto;padding:12px 20px;background:var(--y);color:#000;border-radius:var(--radius);font-weight:700}}
:focus-visible{{outline:3px solid var(--y);outline-offset:3px}}
@media(prefers-reduced-motion:reduce){{*{{animation:none!important;transition:none!important}}#particleCanvas{{display:none}}}}
@media(prefers-color-scheme:light){{body:not(.dark):not(.high-contrast){{--bg:#f1f5f9;--bg2:#fff;--tx:#1e293b;--card:rgba(255,255,255,.9)}}}}
canvas#particleCanvas{{position:fixed;inset:0;pointer-events:none;z-index:0}}
body.high-contrast #particleCanvas{{display:none}}
header{{text-align:center;padding:clamp(30px,8vw,70px) 20px 40px;position:relative;z-index:1}}
header h1{{font-size:clamp(1.8rem,5vw,3.2rem);font-weight:800;background:linear-gradient(135deg,var(--b),var(--g));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}}
header p.sub{{margin-top:6px;opacity:.7;font-size:.95rem}}
.toolbar{{display:flex;gap:8px;justify-content:center;margin-top:16px;flex-wrap:wrap}}
.toolbar button{{padding:8px 18px;border-radius:8px;border:1px solid rgba(255,255,255,.15);background:var(--bg2);color:var(--tx);cursor:pointer;font-size:.85rem;font-weight:600;transition:background .2s,transform .15s}}
.toolbar button:hover{{background:var(--b);color:#fff;transform:translateY(-1px)}}
body.high-contrast .toolbar button{{border:2px solid var(--tx)}}
.stats{{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:16px;max-width:1200px;margin:-10px auto 30px;padding:0 20px;position:relative;z-index:1}}
.badge{{text-align:center;padding:22px 16px;border-radius:var(--radius);background:var(--card);backdrop-filter:blur(12px);box-shadow:var(--shadow);font-weight:700;font-size:1.5rem;transition:transform .25s,box-shadow .25s;border-left:5px solid var(--b)}}
.badge:hover{{transform:translateY(-4px);box-shadow:0 12px 40px rgba(0,0,0,.5)}}
.badge small{{display:block;font-size:.7rem;font-weight:400;opacity:.7;margin-bottom:4px;text-transform:uppercase;letter-spacing:.5px}}
.badge.added{{border-color:var(--g)}}.badge.changed{{border-color:var(--b)}}.badge.removed{{border-color:var(--r)}}.badge.net{{border-color:var(--y)}}
.badge.pct{{border-color:var(--b)}}.badge.positive{{border-color:var(--g)}}.badge.negative{{border-color:var(--r)}}
.badge.ha{{border-color:#10b981}}.badge.hc{{border-color:#3b82f6}}.badge.hr{{border-color:#ef4444}}
.last-run{{text-align:center;margin:0 0 24px;font-size:.85rem;opacity:.6}}
section{{max-width:1200px;margin:0 auto;padding:0 20px 60px;position:relative;z-index:1}}
.controls{{display:flex;gap:10px;flex-wrap:wrap;margin-bottom:20px}}
.controls input,.controls select{{flex:1;min-width:200px;padding:11px 16px;border-radius:10px;border:1px solid rgba(255,255,255,.12);background:var(--bg2);color:var(--tx);font-size:.9rem}}
body.high-contrast .controls input,body.high-contrast .controls select{{border:2px solid var(--tx)}}
.controls input::placeholder{{color:rgba(255,255,255,.3)}}
body.light .controls input::placeholder{{color:rgba(0,0,0,.3)}}
table{{width:100%;border-collapse:collapse;margin-bottom:32px;font-size:.9rem}}
th,td{{border:1px solid rgba(255,255,255,.08);padding:10px 14px;text-align:left}}
th{{background:rgba(0,0,0,.25);font-weight:600;font-size:.8rem;text-transform:uppercase;letter-spacing:.3px}}
tr:nth-child(even){{background:rgba(255,255,255,.03)}}
body.high-contrast th,body.high-contrast td{{border:1px solid var(--tx)}}
.report-container{{background:var(--card);backdrop-filter:blur(12px);border-radius:var(--radius);box-shadow:var(--shadow);padding:20px;min-height:60vh;position:relative}}
body.high-contrast .report-container{{border:2px solid var(--tx)}}
#loadingSpinner{{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:36px;height:36px;border:3px solid rgba(255,255,255,.15);border-top-color:var(--g);border-radius:50%;animation:spin .8s linear infinite}}
@keyframes spin{{to{{transform:translate(-50%,-50%) rotate(360deg)}}}}
#reportContent{{min-height:60vh}}
.commit-card{{background:rgba(255,255,255,.05);border-radius:10px;padding:16px;margin-bottom:14px}}
body.high-contrast .commit-card{{border:1px solid var(--tx)}}
.commit-card h3{{cursor:pointer;font-size:1rem;margin-bottom:8px}}
.commit-card ul{{list-style:none;overflow:hidden;transition:max-height .3s ease}}
.commit-card li{{padding:5px 0;font-size:.88rem;border-bottom:1px solid rgba(255,255,255,.05)}}
.copy-btn{{margin-left:6px;padding:3px 8px;font-size:.75rem;background:var(--y);color:#000;border:none;border-radius:4px;cursor:pointer}}
.export-bar{{display:flex;gap:10px;margin:20px 0;flex-wrap:wrap}}
.export-bar button{{padding:10px 22px;border-radius:8px;background:var(--b);color:#fff;border:none;cursor:pointer;font-weight:600;transition:background .2s}}
.export-bar button:hover{{background:var(--g)}}
body.high-contrast .export-bar button{{border:2px solid var(--tx)}}
canvas#myChart{{display:block;max-width:900px;margin:40px auto;border-radius:var(--radius)}}
footer{{text-align:center;padding:30px 20px;font-size:.8rem;opacity:.5;position:relative;z-index:1}}
.sr-only{{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);border:0}}
.error-message{{color:var(--r);text-align:center;padding:20px;font-size:1.1rem}}
::-webkit-scrollbar{{width:8px}}::-webkit-scrollbar-track{{background:transparent}}::-webkit-scrollbar-thumb{{background:rgba(255,255,255,.15);border-radius:4px}}
@media print{{body{{background:#fff;color:#000}}canvas#particleCanvas,.toolbar,.controls,.export-bar,footer{{display:none}}.badge{{box-shadow:none;border:1px solid #ccc}}}}
@media(max-width:600px){{.stats{{grid-template-columns:repeat(2,1fr);gap:10px}}.badge{{padding:14px 10px;font-size:1.2rem}}.controls{{flex-direction:column}}.controls input,.controls select{{min-width:100%}}}}
</style>
</head>
<body>
<a class="skip" href="#reportContent">Skip to report</a>
<canvas id="particleCanvas" aria-hidden="true"></canvas>
<header>
<h1>Roblox FFlag Tracker</h1>
<p class="sub">Client feature flag intelligence — updated automatically</p>
<div class="toolbar">
<button id="themeToggle" aria-label="Toggle dark/light theme">🌓 Theme</button>
<button id="contrastToggle" aria-label="Toggle high contrast">⬛ Contrast</button>
</div>
</header>
<div class="stats" role="region" aria-label="Summary statistics">
<div class="badge added" aria-label="{added} flags added"><small>✅ Added</small><span id="flags-added">{added}</span></div>
<div class="badge changed" aria-label="{changed} flags changed"><small>🔄 Changed</small><span id="flags-changed">{changed}</span></div>
<div class="badge removed" aria-label="{removed} flags removed"><small>❌ Removed</small><span id="flags-removed">{removed}</span></div>
<div class="badge net" aria-label="Net changes: {net}"><small>📊 Net</small><span id="net-changes">{net}</span></div>
<div class="badge pct {pct_cls}" aria-label="Percent change: {pct}%"><small>📈 % Change</small><span id="percent-change">{pct:.2f}</span>%</div>
<div class="badge ha" aria-label="Historical added: {hist_a}"><small>∑ Added</small><span id="historical-added">{hist_a}</span></div>
<div class="badge hc" aria-label="Historical changed: {hist_c}"><small>∑ Changed</small><span id="historical-changed">{hist_c}</span></div>
<div class="badge hr" aria-label="Historical removed: {hist_r}"><small>∑ Removed</small><span id="historical-removed">{hist_r}</span></div>
</div>
<p class="last-run">Last updated: <time id="last-run">{html.escape(last_run)}</time></p>
<section>
<div class="controls">
<label for="searchInput" class="sr-only">Search flags</label>
<input type="search" id="searchInput" placeholder="Search flags…" aria-label="Search flags" autocomplete="off">
<label for="categoryFilter" class="sr-only">Category</label>
<select id="categoryFilter" aria-label="Filter by category">
<option value="">All Categories</option>
{cat_opts}
</select>
<label for="sortSelect" class="sr-only">Sort</label>
<select id="sortSelect" aria-label="Sort options">
<option value="">Sort by Name</option>
<option value="freq">Sort by Frequency</option>
</select>
</div>
<h2>Summary</h2>
<table id="summaryTable" aria-label="Category breakdown">
<thead><tr><th>Category</th><th>Added</th><th>Changed</th><th>Removed</th><th>Total</th></tr></thead>
<tbody>{s_rows}</tbody>
</table>
<h2>📄 Reports</h2>
<p><a href="FFlag_Report.md" style="color:var(--b)">Markdown</a> · <a href="FFlag_Report.html" style="color:var(--b)">Standalone HTML</a> · <a href="FFlag_Report.json" style="color:var(--b)">Full JSON</a></p>
<h2>📊 Commit History</h2>
<div class="report-container">
<div id="loadingSpinner" aria-label="Loading"></div>
<div id="reportContent" role="region" aria-live="polite"></div>
</div>
<div class="export-bar">
<button id="exportCSV" aria-label="Export CSV">Export CSV</button>
<button id="exportJSON" aria-label="Export JSON">Export JSON</button>
</div>
<div id="chart-container">
<canvas id="myChart" aria-label="Trend chart"></canvas>
</div>
</section>
<footer>Built with ❤️ by FFlag Tracker · auto-updated</footer>
<script src="assets/hammer.min.js" defer></script>
<script src="assets/chart.umd.js" defer></script>
<script src="assets/chartjs-plugin-zoom.js" defer></script>
<script src="assets/app.js" defer></script>
</body>
</html>"""
    atomic_write(OUTPUT_DIR / "index.html", page)
    log.info(f"Landing page → {OUTPUT_DIR / 'index.html'}")


def publish_output_to_github():
    token = os.getenv("GITHUB_TOKEN")
    repo = os.getenv("GITHUB_REPO")
    branch = os.getenv("GITHUB_PAGES_BRANCH", "gh-pages")
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
            if item == ".git":
                continue
            p = WORKSPACE / item
            if p.is_dir():
                shutil.rmtree(p)
            else:
                os.remove(p)
        for item in OUTPUT_DIR.iterdir():
            dest = WORKSPACE / item.name
            if item.is_dir():
                shutil.copytree(item, dest)
            else:
                shutil.copy2(item, dest)
        run_cmd("git add .")
        try:
            run_cmd('git commit -m "Publish FFlag Tracker output"')
            run_cmd(f"git push {remote} {branch}")
            log.info(f"Published to {branch}")
        except subprocess.CalledProcessError as e:
            if "nothing to commit" in (e.stderr or ""):
                log.info("No changes to publish.")
            else:
                raise
    except Exception as e:
        log.error(f"Publish failed: {e}")


async def main():
    try:
        startup_delay = int(os.getenv("STARTUP_DELAY_SECONDS", "0"))
        if startup_delay:
            await asyncio.sleep(startup_delay)
        log.info("=" * 72)
        log.info("Roblox Client FFlag Tracker")
        log.info("=" * 72)

        load_caches()
        manifest_repo = ensure_manifest_repo()
        commits = get_commits(DAYS, manifest_repo)
        log.info(f"Found {len(commits)} commits in last {DAYS} days")

        lock = FileLock(str(OUTPUT_DIR / "cache.lock"), timeout=10)
        with lock:
            diff_cache = safe_read_json(DIFF_CACHE_FILE, {})
            if args.force_refresh:
                diff_cache.clear()

            report, summary, flag_changes = [], {}, {}
            if commits:
                report, summary, flag_changes = await build_report(commits, diff_cache, manifest_repo)

            atomic_write(DIFF_CACHE_FILE, json.dumps(diff_cache, indent=2))

            all_flags = set()
            for _, changes in report:
                for _, _, flag, *_ in changes:
                    all_flags.add(flag)
            if all_flags:
                await generate_flag_info_batch(list(all_flags))

            if os.getenv("PRUNE_CACHE", "true").lower() == "true" and flag_changes:
                recent_flags = set(flag_changes.keys())
                pruned = [f for f in list(FLAG_INFO.keys()) if f not in recent_flags]
                for f in pruned:
                    del FLAG_INFO[f]
                if pruned:
                    log.info(f"Pruned {len(pruned)} stale flags from cache")

            atomic_write(CACHE_FILE, json.dumps(FLAG_INFO, indent=2))

        last_run = datetime.datetime.now(TIMEZONE).strftime("%Y-%m-%d %I:%M:%S %p %Z")
        added, changed, removed = compute_stats(summary)
        update_history(added, changed, removed, last_run)

        export_reports(report, summary, flag_changes)
        ensure_landing_page(added, changed, removed, last_run, summary)

        if os.getenv("SKIP_ASSETS", "false").lower() != "true":
            loop = asyncio.get_running_loop()
            await loop.run_in_executor(None, ensure_assets)
            await loop.run_in_executor(None, ensure_service_worker)
            await loop.run_in_executor(None, ensure_manifest)

        if os.getenv("PUBLISH_GH", "false").lower() == "true":
            publish_output_to_github()

        log.info(f"✅ Done — {added} added, {changed} changed, {removed} removed")
    except Exception as e:
        log.error(f"Fatal: {e}", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
