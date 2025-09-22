#!/usr/bin/env python3
import os
import itertools
import subprocess
import shutil
import datetime
import json
import html
from pathlib import Path
from zoneinfo import ZoneInfo
import asyncio
import openai

# ===============================
# Settings and Paths
# ===============================
SCRIPT_DIR = Path(__file__).resolve().parent
WORKSPACE = Path(os.getenv("GITHUB_WORKSPACE", SCRIPT_DIR)).resolve()
OUTPUT_DIR = WORKSPACE / "output"
OUTPUT_MD = OUTPUT_DIR / "FFlag_Report.md"
OUTPUT_HTML = OUTPUT_DIR / "FFlag_Report.html"

REPO_URL = "https://github.com/MaximumADHD/Roblox-FFlag-Tracker"
LOCAL_CLONE = WORKSPACE / "Roblox-FFlag-Tracker"
TARGET_FILE = "PCDesktopClient.json"
DAYS = 8  # How many days to look back for commits
HISTORY_DAYS = 90  # Keep history for trend analysis
AI_BATCH_SIZE = 10  # Number of flags per AI batch

CACHE_FILE = OUTPUT_DIR / "fflag_cache.json"

# ===============================
# OpenAI API Key Rotation Setup
# ===============================
keys = os.getenv("OPENAI_API_KEYS", "").split(",")
if not keys or keys == [""]:
    raise ValueError("No OpenAI API keys found in OPENAI_API_KEYS environment variable.")

key_cycle = itertools.cycle(keys)

def get_next_api_key():
    """Return the next API key from the round-robin rotation."""
    return next(key_cycle)

# ===============================
# Categories for classification
# ===============================
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

# ===============================
# Logging and Utility Functions
# ===============================
def log(msg, level="INFO"):
    ts = datetime.datetime.now(ZoneInfo("Asia/Manila")).strftime("%Y-%m-%d %I:%M:%S %p %Z")
    print(f"[{level}] {msg} ({ts})")

def run_cmd(cmd, cwd=None):
    """Run shell command and return output, log errors if any."""
    result = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True)
    if result.returncode != 0:
        log(f"Command failed: {cmd}", level="ERROR")
        log(result.stderr, level="ERROR")
    return result.stdout.strip()

def categorize_flag(flag_name):
    """Return category based on keywords."""
    lower_flag = flag_name.lower()
    for cat, keywords in CATEGORIES.items():
        for word in keywords:
            if word.lower() in lower_flag:
                return cat
    return "Other"

def escape_flag(flag_name):
    """Escape flag names for HTML output."""
    return html.escape(flag_name)

# ===============================
# Repository Management
# ===============================
def ensure_repo():
    """Clone or update the FFlag repository."""
    if LOCAL_CLONE.exists():
        log("Updating existing repo...")
        run_cmd("git fetch --all", cwd=LOCAL_CLONE)
        run_cmd("git reset --hard origin/main", cwd=LOCAL_CLONE)
    else:
        log("Cloning fresh repo...")
        run_cmd(f"git clone --depth=1 {REPO_URL} {LOCAL_CLONE}")

def get_commits():
    """Get commits for target file in last DAYS."""
    since_date = (datetime.datetime.now() - datetime.timedelta(days=DAYS)).strftime("%Y-%m-%d")
    commits = run_cmd(
        f"git log --since='{since_date}' --pretty=format:'%H' -- {TARGET_FILE}",
        cwd=LOCAL_CLONE
    ).splitlines()
    return commits

def build_diff_for_commit(commit_hash):
    """Return header, added, and removed flags for a commit."""
    header = run_cmd(f"git show --no-patch --pretty=format:'%h - %ci - %s' {commit_hash}", cwd=LOCAL_CLONE)
    diff = run_cmd(f"git show {commit_hash} -- {TARGET_FILE}", cwd=LOCAL_CLONE)
    added, removed = [], []
    for line in diff.splitlines():
        if line.startswith("+") and not line.startswith("+++"):
            added.append(line[1:].strip())
        elif line.startswith("-") and not line.startswith("---"):
            removed.append(line[1:].strip())
    return header, added, removed

def build_report(commits):
    """Build report and summary from commits."""
    report = []
    summary_counts = {}
    for c in commits:
        header, added_flags, removed_flags = build_diff_for_commit(c)
        changes = []

        for flag in added_flags:
            cat = categorize_flag(flag)
            changes.append(("Added", cat, flag))
            summary_counts.setdefault((cat, "Added"), 0)
            summary_counts[(cat, "Added")] += 1

        for flag in removed_flags:
            cat = categorize_flag(flag)
            changes.append(("Removed", cat, flag))
            summary_counts.setdefault((cat, "Removed"), 0)
            summary_counts[(cat, "Removed")] += 1

        if changes:
            report.append((header, changes))
    return report, summary_counts

# ===============================
# History Tracking
# ===============================
def update_history(added, removed, last_run):
    hist_file = OUTPUT_DIR / "history.json"
    history = []
    if hist_file.exists():
        history = json.loads(hist_file.read_text(encoding="utf-8"))
    history.append({"date": last_run, "added": added, "removed": removed})
    history = history[-HISTORY_DAYS:]
    hist_file.write_text(json.dumps(history, indent=2), encoding="utf-8")

# ===============================
# AI Enrichment with Multi-Key Rotation, Async, and Caching
# ===============================
if CACHE_FILE.exists():
    with open(CACHE_FILE, "r", encoding="utf-8") as f:
        FLAG_INFO = json.load(f)
else:
    FLAG_INFO = {}

async def fetch_ai_batch(batch):
    """Fetch AI explanation for a batch of flags with retries and key rotation."""
    prompt = "Explain the Roblox FFlags in detail:\n" + "".join([f"- {f}\n" for f in batch])
    prompt += "\nProvide Mechanism and Purpose for each, 1-2 sentences each."

    try:
        openai.api_key = get_next_api_key()
        response = await openai.chat.completions.create(
            model="gpt-5-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )
        text = response.choices[0].message["content"].strip().split("\n")
        for line in text:
            if ":" in line:
                f, rest = line.split(":", 1)
                f = f.strip()
                if f in batch:
                    FLAG_INFO[f] = {"mechanism": rest.strip(), "purpose": "N/A"}
    except openai.error.RateLimitError:
        log("Rate limit reached. Retrying batch with next key.", level="WARN")
        await fetch_ai_batch(batch)
    except Exception as e:
        log(f"AI batch generation failed: {e}", level="ERROR")
        for f in batch:
            FLAG_INFO[f] = {"mechanism": "Unknown", "purpose": "Unknown"}

async def generate_flag_info_batch(flags):
    """Generate AI explanations in batches asynchronously."""
    new_flags = [f for f in flags if f not in FLAG_INFO]
    if not new_flags:
        return

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    tasks = [fetch_ai_batch(new_flags[i:i+AI_BATCH_SIZE]) for i in range(0, len(new_flags), AI_BATCH_SIZE)]
    await asyncio.gather(*tasks)

    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(FLAG_INFO, f, indent=2)

def generate_flag_info(flag_name):
    return FLAG_INFO.get(flag_name, {"mechanism": "Unknown", "purpose": "Unknown"})

# ===============================
# Report Generation
# ===============================
def export_reports(report, summary_counts):
    """Generate Markdown and HTML reports with enriched AI info."""
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    date_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    added_count = sum(v for (c, a), v in summary_counts.items() if a == "Added")
    removed_count = sum(v for (c, a), v in summary_counts.items() if a == "Removed")

    # Markdown
    md = [f"# Roblox Client FFlag Intel Report ({DAYS} Days)\n"]
    md.append(f"- **Last Run:** {date_str}")
    md.append(f"- **Flags Added:** {added_count}")
    md.append(f"- **Flags Removed:** {removed_count}\n")

    md.append("## Summary of Changes\n")
    md.append("| Category | Added | Removed | Total |")
    md.append("|----------|-------|---------|-------|")
    for cat in CATEGORIES.keys():
        a = summary_counts.get((cat, "Added"), 0)
        r = summary_counts.get((cat, "Removed"), 0)
        md.append(f"| {cat} | {a} | {r} | {a+r} |")
    md.append("")

    for header, changes in report:
        md.append(f"## {header}\n")
        grouped = {}
        for action, cat, flag in changes:
            grouped.setdefault((action, cat), []).append(flag)
        for (action, cat), flags in grouped.items():
            md.append(f"**{action} in {cat}:**")
            for f in flags:
                info = generate_flag_info(f)
                md.append(f"- {escape_flag(f)}")
                md.append(f"  - Mechanism: {info['mechanism']}")
                md.append(f"  - Purpose: {info['purpose']}")
        md.append("")
    OUTPUT_MD.write_text("\n".join(md), encoding="utf-8")

    # HTML
    html_lines = [f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Roblox FFlag Intel Report</title>
<style>
body {{ font-family: Arial, sans-serif; background: #0d1117; color: #c9d1d9; }}
h1,h2,h3 {{ color: #58a6ff; }}
table {{ border-collapse: collapse; margin: 20px 0; }}
th,td {{ border: 1px solid #333; padding: 8px 12px; }}
.added {{ color: #4caf50; }}
.removed {{ color: #f44336; }}
code {{ background: #161b22; padding: 2px 5px; border-radius: 4px; }}
.commit {{ background: #161b22; padding: 15px; margin: 15px 0; border-radius: 8px; }}
</style>
</head>
<body>
<h1>Roblox Client FFlag Intel Report ({DAYS} Days)</h1>
<p><strong>Last Run:</strong> {date_str}</p>
<p><strong>Flags Added:</strong> <span class="added">{added_count}</span> |
<strong>Removed:</strong> <span class="removed">{removed_count}</span></p>
<h2>Summary of Changes</h2>
<table>
<tr><th>Category</th><th>Added</th><th>Removed</th><th>Total</th></tr>"""]

    for cat in CATEGORIES.keys():
        a = summary_counts.get((cat, "Added"), 0)
        r = summary_counts.get((cat, "Removed"), 0)
        html_lines.append(f"<tr><td>{cat}</td><td class='added'>{a}</td><td class='removed'>{r}</td><td>{a+r}</td></tr>")
    html_lines.append("</table>")

    for header, changes in report:
        html_lines.append(f"<div class='commit'><h2>{header}</h2>")
        grouped = {}
        for action, cat, flag in changes:
            grouped.setdefault((action, cat), []).append(flag)
        for (action, cat), flags in grouped.items():
            html_lines.append(f"<h3>{action} in {cat}</h3><ul>")
            for f in flags:
                info = generate_flag_info(f)
                html_lines.append(f"<li class='{action.lower()}'><code>{escape_flag(f)}</code>")
                html_lines.append(f"<p><strong>Mechanism:</strong> {info['mechanism']}</p>")
                html_lines.append(f"<p><strong>Purpose:</strong> {info['purpose']}</p></li>")
            html_lines.append("</ul>")
        html_lines.append("</div>")
    html_lines.append("</body></html>")
    OUTPUT_HTML.write_text("\n".join(html_lines), encoding="utf-8")

    log(f"Reports generated:\n- {OUTPUT_MD}\n- {OUTPUT_HTML}")
    return added_count, removed_count, date_str, report

# ===============================
# Landing Page Dashboard
# ===============================
def ensure_landing_page(added, removed, last_run):
    index_html = OUTPUT_DIR / "index.html"
    if not (OUTPUT_DIR / "history.json").exists():
        (OUTPUT_DIR / "history.json").write_text("[]")

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><title>Roblox FFlag Tracker Dashboard</title></head>
<body>
<h1>Roblox Client FFlag Tracker</h1>
<p>Flags Added: {added} | Flags Removed: {removed}</p>
<p>Last Run: {last_run}</p>
<iframe src="FFlag_Report.html" style="width:95%; height:70vh;"></iframe>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<canvas id="trendChart" style="max-width:900px; margin:20px auto; display:block;"></canvas>
<script>
fetch("history.json")
  .then(r=>r.json())
  .then(data=>{{
    new Chart(document.getElementById("trendChart").getContext("2d"), {{
      type:'line',
      data:{{
        labels:data.map(d=>d.date),
        datasets:[{{label:"Flags Added", data:data.map(d=>d.added), borderColor:"#4caf50", fill:false}},
                  {{label:"Flags Removed", data:data.map(d=>d.removed), borderColor:"#f44336", fill:false}}]
      }},
      options:{{responsive:true}}
    }});
  }});
</script>
</body></html>"""
    index_html.write_text(html_content, encoding="utf-8")
    log(f"Landing page written: {index_html}")

# ===============================
# Main Entry Point
# ===============================
def main():
    log("="*60)
    log("Roblox Client FFlag Tracker (Daily Automation Ready)")
    log("="*60)

    ensure_repo()
    commits = get_commits()
    if not commits:
        log(f"No commits in the last {DAYS} days.", level="WARN")
        return

    report, summary_counts = build_report(commits)

    # AI enrichment with async and multi-key rotation
    all_flags = [f for _, changes in report for _, _, f in changes]
    if all_flags:
        asyncio.run(generate_flag_info_batch(all_flags))

    added, removed, last_run, _ = export_reports(report, summary_counts)
    ensure_landing_page(added, removed, last_run)
    update_history(added, removed, last_run)

    log("All done!", level="SUCCESS")

if __name__ == "__main__":
    main()
