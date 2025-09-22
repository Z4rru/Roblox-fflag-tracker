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
CACHE_FILE = OUTPUT_DIR / "fflag_cache.json"

REPO_URL = "https://github.com/MaximumADHD/Roblox-FFlag-Tracker"
LOCAL_CLONE = WORKSPACE / "Roblox-FFlag-Tracker"
TARGET_FILE = "PCDesktopClient.json"

DAYS = 8
HISTORY_DAYS = 90
AI_BATCH_SIZE = 10
DEBUG = True

# ===============================
# Logging Utility
# ===============================
def log(msg, level="INFO"):
    ts = datetime.datetime.now(ZoneInfo("Asia/Manila")).strftime("%Y-%m-%d %I:%M:%S %p %Z")
    prefix = f"[{level}]"
    print(f"{prefix} {msg} ({ts})")

# ===============================
# OpenAI API Key Management
# ===============================
keys_raw = os.getenv("OPENAI_API_KEYS", "")
keys = [k.strip() for k in keys_raw.split(",") if k.strip()]
if not keys:
    log("⚠ No OpenAI API keys found. AI enrichment will be skipped.", level="WARN")
    keys = []

if keys:
    key_index = -1
    key_cycle = itertools.cycle(keys)
    def get_next_api_key():
        global key_index
        key_index = (key_index + 1) % len(keys)
        key = keys[key_index]
        display_key = f"{key[:4]}...{key[-4:]}" if len(key) > 8 else "****"
        log(f"Using OpenAI API key #{key_index+1} ({display_key})", level="DEBUG")
        return key
else:
    def get_next_api_key():
        return None

# ===============================
# FFlags Categories
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
# Utility Functions
# ===============================
def run_cmd(cmd, cwd=None):
    result = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True)
    if result.returncode != 0:
        log(f"Command failed: {cmd}", level="ERROR")
        log(result.stderr.strip(), level="ERROR")
    return result.stdout.strip()

def categorize_flag(flag_name):
    lower = flag_name.lower()
    for cat, keywords in CATEGORIES.items():
        if any(k.lower() in lower for k in keywords):
            return cat
    return "Other"

def escape_flag(flag_name):
    return html.escape(flag_name)

# ===============================
# Repository Management
# ===============================
def ensure_repo():
    if LOCAL_CLONE.exists():
        log("Updating existing repository...")
        run_cmd("git fetch --all", cwd=LOCAL_CLONE)
        run_cmd("git reset --hard origin/main", cwd=LOCAL_CLONE)
    else:
        log("Cloning repository for the first time...")
        run_cmd(f"git clone --depth=1 {REPO_URL} {LOCAL_CLONE}")

def get_commits():
    since = (datetime.datetime.now() - datetime.timedelta(days=DAYS)).strftime("%Y-%m-%d")
    commits = run_cmd(f"git log --since='{since}' --pretty=format:'%H' -- {TARGET_FILE}", cwd=LOCAL_CLONE)
    return commits.splitlines() if commits else []

def build_diff_for_commit(commit_hash):
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
    report, summary = [], {}
    for c in commits:
        header, added_flags, removed_flags = build_diff_for_commit(c)
        changes = []
        for flag in added_flags:
            cat = categorize_flag(flag)
            changes.append(("Added", cat, flag))
            summary[(cat,"Added")] = summary.get((cat,"Added"),0)+1
        for flag in removed_flags:
            cat = categorize_flag(flag)
            changes.append(("Removed", cat, flag))
            summary[(cat,"Removed")] = summary.get((cat,"Removed"),0)+1
        if changes:
            report.append((header, changes))
    return report, summary

# ===============================
# History Management
# ===============================
def update_history(added, removed, last_run):
    hist_file = OUTPUT_DIR / "history.json"
    history = json.loads(hist_file.read_text(encoding="utf-8")) if hist_file.exists() else []
    history.append({"date": last_run, "added": added, "removed": removed})
    history = history[-HISTORY_DAYS:]
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    hist_file.write_text(json.dumps(history, indent=2), encoding="utf-8")

# ===============================
# AI Enrichment
# ===============================
FLAG_INFO = json.load(CACHE_FILE.open("r", encoding="utf-8")) if CACHE_FILE.exists() else {}

async def fetch_ai_batch(batch):
    if not keys:
        for f in batch:
            FLAG_INFO[f] = {"mechanism": "Unknown", "purpose": "Unknown"}
        return
    prompt = "Explain the Roblox FFlags in detail:\n" + "".join([f"- {f}\n" for f in batch])
    prompt += "\nProvide Mechanism and Purpose, 1-2 sentences each."
    try:
        openai.api_key = get_next_api_key()
        response = await openai.chat.completions.create(
            model="gpt-5-mini",
            messages=[{"role":"user","content":prompt}],
            temperature=0.3
        )
        text = response.choices[0].message["content"].strip().split("\n")
        for line in text:
            if ":" in line:
                f, rest = line.split(":",1)
                f = f.strip()
                if f in batch:
                    FLAG_INFO[f] = {"mechanism": rest.strip(), "purpose": "N/A"}
    except openai.error.RateLimitError:
        log("Rate limit reached. Retrying batch.", level="WARN")
        await fetch_ai_batch(batch)
    except Exception as e:
        log(f"AI batch failed: {e}", level="ERROR")
        for f in batch:
            FLAG_INFO[f] = {"mechanism":"Unknown","purpose":"Unknown"}

async def generate_flag_info_batch(flags):
    new_flags = [f for f in flags if f not in FLAG_INFO]
    if not new_flags: return
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    tasks = [fetch_ai_batch(new_flags[i:i+AI_BATCH_SIZE]) for i in range(0,len(new_flags),AI_BATCH_SIZE)]
    await asyncio.gather(*tasks)
    CACHE_FILE.write_text(json.dumps(FLAG_INFO, indent=2), encoding="utf-8")

def generate_flag_info(flag):
    return FLAG_INFO.get(flag, {"mechanism":"Unknown","purpose":"Unknown"})

# ===============================
# Report Generation (Markdown + HTML)
# ===============================
def export_reports(report, summary):
    if OUTPUT_DIR.exists(): shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    date_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    added_count = sum(v for (c,a),v in summary.items() if a=="Added")
    removed_count = sum(v for (c,a),v in summary.items() if a=="Removed")

    # Markdown
    md = [f"# Roblox FFlag Report ({DAYS} Days)\n","",f"- Last Run: {date_str}","- Added: {added_count}","- Removed: {removed_count}\n","## Summary\n"]
    md.append("| Category | Added | Removed | Total |")
    md.append("|----------|-------|---------|-------|")
    for cat in CATEGORIES.keys():
        a=summary.get((cat,"Added"),0)
        r=summary.get((cat,"Removed"),0)
        md.append(f"| {cat} | {a} | {r} | {a+r} |")
    md.append("")
    for header, changes in report:
        md.append(f"## {header}")
        grouped={}; 
        for action, cat, flag in changes:
            grouped.setdefault((action, cat),[]).append(flag)
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
    html_lines = [f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>FFlag Report</title></head><body>
<h1>Roblox FFlag Report ({DAYS} Days)</h1><p>Last Run: {date_str}</p><p>Added: {added_count} | Removed: {removed_count}</p>"""]
    for header, changes in report:
        html_lines.append(f"<h2>{header}</h2>")
        grouped={}
        for action, cat, flag in changes: grouped.setdefault((action,cat),[]).append(flag)
        for (action,cat),flags in grouped.items():
            html_lines.append(f"<h3>{action} in {cat}</h3><ul>")
            for f in flags:
                info = generate_flag_info(f)
                html_lines.append(f"<li>{escape_flag(f)}<br>Mechanism: {info['mechanism']}<br>Purpose: {info['purpose']}</li>")
            html_lines.append("</ul>")
    html_lines.append("</body></html>")
    OUTPUT_HTML.write_text("\n".join(html_lines), encoding="utf-8")
    log(f"Reports generated: {OUTPUT_MD}, {OUTPUT_HTML}")
    return added_count, removed_count, date_str, report

# ===============================
# Dashboard Landing Page
# ===============================
def ensure_landing_page(added, removed, last_run):
    index_html = OUTPUT_DIR / "index.html"
    hist_file = OUTPUT_DIR / "history.json"
    if not hist_file.exists():
        hist_file.write_text("[]", encoding="utf-8")

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Roblox FFlag Tracker</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
<style>
  body {{ font-family:'Inter',sans-serif; margin:0; background:#f4f6fb; color:#333; }}
  header {{ background:linear-gradient(135deg,#4f46e5,#3b82f6); color:#fff; padding:40px 20px; text-align:center; box-shadow:0 4px 10px rgba(0,0,0,0.2); }}
  header h1 {{ margin:0; font-size:2.5rem; font-weight:700; }}
  .stats {{ display:flex; justify-content:center; gap:30px; margin:30px auto; flex-wrap:wrap; max-width:800px; }}
  .badge {{ flex:1; min-width:200px; text-align:center; padding:20px; border-radius:16px; font-size:1.3rem; font-weight:600; box-shadow:0 4px 12px rgba(0,0,0,0.08); transition:transform 0.2s,box-shadow 0.2s; }}
  .badge:hover {{ transform:translateY(-4px); box-shadow:0 6px 16px rgba(0,0,0,0.12); }}
  .added {{ background:#ecfdf5; color:#047857; border:2px solid #34d399; }}
  .removed {{ background:#fef2f2; color:#b91c1c; border:2px solid #f87171; }}
  .last-run {{ text-align:center; margin:20px 0; font-style:italic; color:#555; }}
  input#searchInput {{ width:90%; padding:10px; margin:20px auto; display:block; border-radius:8px; border:1px solid #ccc; font-size:1rem; }}
  section {{ max-width:1200px; margin:0 auto; padding:20px; }}
  .report-container {{ background:#fff; border-radius:12px; box-shadow:0 4px 16px rgba(0,0,0,0.1); padding:10px; }}
  iframe {{ width:100%; height:75vh; border:none; border-radius:8px; }}
  footer {{ margin-top:40px; padding:20px; text-align:center; font-size:0.9rem; color:#777; }}
</style>
</head>
<body>
<header>
  <h1>Roblox Client FFlag Tracker</h1>
</header>

<section>
  <div class="stats">
    <div class="badge added">✅ Added: <span id="flags-added">{added}</span></div>
    <div class="badge removed">❌ Removed: <span id="flags-removed">{removed}</span></div>
  </div>

  <p class="last-run">Last Run: <span id="last-run">{last_run}</span></p>

  <input type="text" id="searchInput" placeholder="Search flags...">

  <h2>📊 Latest Full Report</h2>
  <div class="report-container">
    <iframe src="FFlag_Report.html" id="reportFrame"></iframe>
  </div>

  <canvas id="trendChart" style="max-width:800px; margin:30px auto; display:block;"></canvas>
</section>

<footer>
  Built with ❤️ by FFlag Tracker • Updated automatically
</footer>

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
// Trend chart
fetch("history.json").then(r=>r.json()).then(data=>{
  const ctx = document.getElementById("trendChart").getContext("2d");
  new Chart(ctx, {{
    type:'line',
    data:{{
      labels: data.map(d=>d.date),
      datasets:[
        {{ label:'Added', data:data.map(d=>d.added), borderColor:'#34d399', fill:false }},
        {{ label:'Removed', data:data.map(d=>d.removed), borderColor:'#f87171', fill:false }}
      ]
    }},
    options: {{ responsive:true }}
  }});
});

// Search/filter functionality
document.getElementById('searchInput').addEventListener('input', function() {{
  const query = this.value.toLowerCase();
  const iframe = document.getElementById('reportFrame');
  const doc = iframe.contentDocument || iframe.contentWindow.document;
  const items = doc.querySelectorAll('li');
  items.forEach(li => {{
    li.style.display = li.textContent.toLowerCase().includes(query) ? '' : 'none';
  }});
}});
</script>
</body>
</html>
"""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    index_html.write_text(html_content, encoding="utf-8")
    log(f"Landing page written: {index_html}")


# ===============================
# Main Execution
# ===============================
def main():
    log("="*80)
    log("Roblox Client FFlag Tracker (Safe & Resilient Version)")
    log("="*80)
    ensure_repo()
    commits = get_commits()
    if not commits:
        log(f"No commits in the last {DAYS} days.", level="WARN")
        return
    report, summary = build_report(commits)
    all_flags = [f for _, changes in report for _, _, f in changes]
    if all_flags:
        asyncio.run(generate_flag_info_batch(all_flags))
    added, removed, last_run, _ = export_reports(report, summary)
    ensure_landing_page(added, removed, last_run)
    update_history(added, removed, last_run)
    log("All done! Reports generated successfully.", level="SUCCESS")

if __name__=="__main__":
    main()
