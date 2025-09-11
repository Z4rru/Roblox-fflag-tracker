#!/usr/bin/env python3
import os
import sys
import subprocess
import re
import shutil
from datetime import datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

# --- Settings ---
TRACKER_DIR = Path.home() / "Roblox-FFlag-Tracker"
REPO_URL = "https://github.com/MaximumADHD/Roblox-Client-Tracker"
TARGET_FILE = "PCDesktopClient.json"
DAYS = 2

# --- Paths ---
SCRIPT_DIR = Path(__file__).resolve().parent
WORKSPACE = Path(os.getenv("GITHUB_WORKSPACE", SCRIPT_DIR)).resolve()
OUTPUT_DIR = WORKSPACE / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_MD = OUTPUT_DIR / "FFlag_Report.md"
OUTPUT_HTML = OUTPUT_DIR / "FFlag_Report.html"
INDEX_HTML = OUTPUT_DIR / "index.html"

# --- Categories ---
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
    "Other": []
}

# --- Logging ---
def log(msg, level="INFO"):
    ts = datetime.now(ZoneInfo("Asia/Manila")).strftime("%Y-%m-%d %I:%M:%S %p %Z")
    print(f"[{level}] {msg} ({ts})")

# --- Utilities ---
def check_git():
    try:
        subprocess.check_output(["git", "--version"], stderr=subprocess.STDOUT)
    except Exception:
        log("Git is not installed or not in PATH.", "ERROR")
        sys.exit(1)

def ensure_repo():
    if not TRACKER_DIR.exists():
        log("Cloning fresh repo...")
        subprocess.run(["git", "clone", REPO_URL, str(TRACKER_DIR)], check=True)
    os.chdir(TRACKER_DIR)
    subprocess.run(["git", "fetch", "--all"], check=True)
    subprocess.run(["git", "reset", "--hard", "origin/main"], check=True)

def categorize_flag(flag_name):
    for cat, keywords in CATEGORIES.items():
        for word in keywords:
            if word.lower() in flag_name.lower():
                return cat
    return "Other"

def get_commits():
    since_date = (datetime.now() - timedelta(days=DAYS)).strftime("%Y-%m-%d")
    log_cmd = ["git", "log", f"--since={since_date}", "--pretty=format:%H", "--", TARGET_FILE]
    return subprocess.check_output(log_cmd, text=True).splitlines()

def build_report(commits):
    report = []
    summary_counts = {}

    for c in commits:
        header = subprocess.check_output(
            ["git", "show", "--no-patch", "--pretty=format:%h - %ci - %s", c],
            text=True
        )
        diff = subprocess.check_output(
            ["git", "show", c, "--", TARGET_FILE], text=True, errors="ignore"
        )
        added, removed = [], []
        for line in diff.splitlines():
            if line.startswith("+") and not line.startswith("+++"):
                added.append(line[1:].strip())
            elif line.startswith("-") and not line.startswith("---"):
                removed.append(line[1:].strip())

        changes = []
        for flag in added:
            cat = categorize_flag(flag)
            changes.append(("Added", cat, flag))
            summary_counts.setdefault((cat, "Added"), 0)
            summary_counts[(cat, "Added")] += 1

        for flag in removed:
            cat = categorize_flag(flag)
            changes.append(("Removed", cat, flag))
            summary_counts.setdefault((cat, "Removed"), 0)
            summary_counts[(cat, "Removed")] += 1

        if changes:
            report.append((header, changes))

    return report, summary_counts

# --- Landing page helpers ---
def ensure_landing_page():
    if not INDEX_HTML.exists():
        log("Creating landing page template...")
        INDEX_HTML.write_text("""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Roblox FFlag Tracker</title>
  <style>
    body {
      font-family: 'Segoe UI', Tahoma, sans-serif;
      margin: 0;
      padding: 0;
      background: linear-gradient(135deg, #1e1e2f, #2c3e50);
      color: #f5f5f5;
    }
    header {
      background: #111827;
      padding: 20px 40px;
      text-align: center;
      box-shadow: 0 4px 10px rgba(0,0,0,0.5);
    }
    h1 { margin: 0; font-size: 2rem; }
    .stats {
      display: flex;
      justify-content: center;
      gap: 30px;
      margin: 30px 0;
    }
    .badge {
      padding: 15px 30px;
      border-radius: 16px;
      font-size: 1.2em;
      font-weight: bold;
      box-shadow: 0 3px 8px rgba(0,0,0,0.3);
    }
    .added { background: #065f46; color: #d1fae5; }
    .removed { background: #7f1d1d; color: #fee2e2; }
    .last-run { text-align: center; font-style: italic; margin-top: 10px; color: #bbb; }
    h2 { text-align: center; margin-top: 40px; color: #f5f5f5; }
    iframe {
      width: 90%;
      height: 75vh;
      border: none;
      border-radius: 12px;
      margin: 20px auto;
      display: block;
      box-shadow: 0 4px 20px rgba(0,0,0,0.2);
      background: white;
    }
    footer {
      text-align: center;
      padding: 20px;
      background: #111827;
      margin-top: 40px;
      font-size: 0.9em;
      color: #bbb;
    }
  </style>
</head>
<body>
  <header>
    <h1>Roblox Client FFlag Tracker</h1>
  </header>

  <div class="stats">
    <div class="badge added">
      Added: <span id="flags-added">0</span>
    </div>
    <div class="badge removed">
      Removed: <span id="flags-removed">0</span>
    </div>
  </div>

  <p class="last-run">
    Last Run: <span id="last-run">Never</span>
  </p>

  <h2>Latest Full Report</h2>
  <iframe src="FFlag_Report.html"></iframe>

  <footer>
    Generated by Roblox FFlag Tracker • Updated automatically
  </footer>
</body>
</html>""", encoding="utf-8")

def update_landing_page(date_str, added, removed):
    html = INDEX_HTML.read_text(encoding="utf-8")
    html = re.sub(r'<span id="last-run">.*?</span>',
                  f'<span id="last-run">{date_str}</span>', html)
    html = re.sub(r'<span id="flags-added">.*?</span>',
                  f'<span id="flags-added">{added}</span>', html)
    html = re.sub(r'<span id="flags-removed">.*?</span>',
                  f'<span id="flags-removed">{removed}</span>', html)
    INDEX_HTML.write_text(html, encoding="utf-8")
    log(f"Landing page updated with {added} added / {removed} removed.")

# --- Export reports ---
def export_reports(report, summary_counts):
    ph_time = datetime.now(ZoneInfo("Asia/Manila"))
    date_str = ph_time.strftime("%Y-%m-%d %I:%M:%S %p %Z")
    added = sum(v for (c, a), v in summary_counts.items() if a == "Added")
    removed = sum(v for (c, a), v in summary_counts.items() if a == "Removed")
    update_landing_page(date_str, added, removed)

    md = [f"# Roblox Client FFlag Intel Report ({DAYS} Days)\n"]
    html = [
        "<html><head><title>Roblox FFlag Intel Report</title>",
        "<style>body{font-family:Arial;background:#f5f5f5;color:#111;} .added{color:green;} .removed{color:red;} code{background:#eee;}</style>",
        "</head><body>",
        f"<h1>Roblox Client FFlag Intel Report ({DAYS} Days)</h1>",
        f"<p>Generated: {date_str}</p>"
    ]

    md.append("## Summary of Changes\n")
    md.append("| Category | Added | Removed | Total |")
    md.append("|----------|-------|---------|-------|")
    html.append("<h2>Summary of Changes</h2>")
    html.append("<table border='1' cellpadding='5'><tr><th>Category</th><th>Added</th><th>Removed</th><th>Total</th></tr>")

    for cat in CATEGORIES.keys():
        a = summary_counts.get((cat, "Added"), 0)
        r = summary_counts.get((cat, "Removed"), 0)
        total = a + r
        md.append(f"| {cat} | {a} | {r} | {total} |")
        html.append(f"<tr><td>{cat}</td><td style='color:green;'>{a}</td><td style='color:red;'>{r}</td><td>{total}</td></tr>")

    md.append("")
    html.append("</table>")

    for header, changes in report:
        md.append(f"## {header}\n")
        html.append(f"<h2>{header}</h2>")
        grouped = {}
        for action, cat, flag in changes:
            grouped.setdefault((action, cat), []).append(flag)
        for (action, cat), flags in grouped.items():
            md.append(f"**{action} in {cat}:**")
            html.append(f"<h3>{action} in {cat}</h3><ul>")
            for f in flags:
                md.append(f"- `{f}`")
                html.append(f"<li class='{action.lower()}'><code>{f}</code></li>")
            html.append("</ul>")
        md.append("")
    html.append("</body></html>")

    OUTPUT_MD.write_text("\n".join(md), encoding="utf-8")
    OUTPUT_HTML.write_text("\n".join(html), encoding="utf-8")
    log("Reports exported.")

# --- Main ---
def main():
    log("=" * 60)
    log("Roblox Client FFlag Intel Tracker")
    log("=" * 60)

    ensure_landing_page()
    check_git()
    ensure_repo()

    commits = get_commits()
    if not commits:
        log(f"No changes in the past {DAYS} days.", "INFO")
        OUTPUT_MD.write_text("# No FFlag changes detected.\n", encoding="utf-8")
        OUTPUT_HTML.write_text("<html><body><h1>No FFlag changes detected.</h1></body></html>", encoding="utf-8")
        return

    report, summary_counts = build_report(commits)
    export_reports(report, summary_counts)
    log("All done!", "SUCCESS")
    log(f"- Markdown: {OUTPUT_MD}")
    log(f"- HTML:     {OUTPUT_HTML}")
    log(f"- Landing:  {INDEX_HTML}")

if __name__ == "__main__":
    main()
