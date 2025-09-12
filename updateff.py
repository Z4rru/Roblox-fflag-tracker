#!/usr/bin/env python3
import os
import subprocess
import shutil
import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

# ===============================
# Settings
# ===============================
SCRIPT_DIR = Path(__file__).resolve().parent
WORKSPACE = Path(os.getenv("GITHUB_WORKSPACE", SCRIPT_DIR)).resolve()
OUTPUT_DIR = WORKSPACE / "output"
OUTPUT_MD = OUTPUT_DIR / "FFlag_Report.md"
OUTPUT_HTML = OUTPUT_DIR / "FFlag_Report.html"

REPO_URL = "https://github.com/MaximumADHD/Roblox-FFlag-Tracker"
LOCAL_CLONE = WORKSPACE / "Roblox-FFlag-Tracker"
TARGET_FILE = "PCDesktopClient.json"
DAYS = 2

# ===============================
# Categories
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
    "Other": []
}

# ===============================
# Helpers
# ===============================
def log(msg, level="INFO"):
    ts = datetime.datetime.now(ZoneInfo("Asia/Manila")).strftime("%Y-%m-%d %I:%M:%S %p %Z")
    print(f"[{level}] {msg} ({ts})")

def run_cmd(cmd, cwd=None):
    result = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True)
    if result.returncode != 0:
        log(f"Command failed: {cmd}", level="ERROR")
        log(result.stderr, level="ERROR")
    return result.stdout.strip()

def categorize_flag(flag_name):
    for cat, keywords in CATEGORIES.items():
        for word in keywords:
            if word.lower() in flag_name.lower():
                return cat
    return "Other"

# ===============================
# Repo sync
# ===============================
def ensure_repo():
    if LOCAL_CLONE.exists():
        log("Updating existing repo...")
        run_cmd("git fetch --all", cwd=LOCAL_CLONE)
        run_cmd("git reset --hard origin/main", cwd=LOCAL_CLONE)
    else:
        log("Cloning fresh repo...")
        run_cmd(f"git clone {REPO_URL} {LOCAL_CLONE}")

# ===============================
# Diffing logic
# ===============================
def get_commits():
    since_date = (datetime.datetime.now() - datetime.timedelta(days=DAYS)).strftime("%Y-%m-%d")
    commits = run_cmd(
        f"git log --since='{since_date}' --pretty=format:'%H' -- {TARGET_FILE}",
        cwd=LOCAL_CLONE
    ).splitlines()
    return commits

def build_report(commits):
    report = []
    summary_counts = {}
    for c in commits:
        header = run_cmd(
            f"git show --no-patch --pretty=format:'%h - %ci - %s' {c}",
            cwd=LOCAL_CLONE
        )
        diff = run_cmd(
            f"git show {c} -- {TARGET_FILE}",
            cwd=LOCAL_CLONE
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

# ===============================
# Export reports
# ===============================
def export_reports(report, summary_counts):
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    date_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    added = sum(v for (c, a), v in summary_counts.items() if a == "Added")
    removed = sum(v for (c, a), v in summary_counts.items() if a == "Removed")

    # Markdown
    md = [f"# Roblox Client FFlag Intel Report ({DAYS} Days)\n"]
    md.append(f"- **Last Run:** {date_str}")
    md.append(f"- **Flags Added:** {added}")
    md.append(f"- **Flags Removed:** {removed}\n")

    md.append("## Summary of Changes\n")
    md.append("| Category | Added | Removed | Total |")
    md.append("|----------|-------|---------|-------|")
    for cat in CATEGORIES.keys():
        a = summary_counts.get((cat, "Added"), 0)
        r = summary_counts.get((cat, "Removed"), 0)
        total = a + r
        md.append(f"| {cat} | {a} | {r} | {total} |")
    md.append("")

    for header, changes in report:
        md.append(f"## {header}\n")
        grouped = {}
        for action, cat, flag in changes:
            grouped.setdefault((action, cat), []).append(flag)
        for (action, cat), flags in grouped.items():
            md.append(f"**{action} in {cat}:**")
            for f in flags:
                md.append(f"- {f}")
        md.append("")

    OUTPUT_MD.write_text("\n".join(md), encoding="utf-8")

    # HTML
    html = [f"""<!DOCTYPE html>
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
  <p><strong>Flags Added:</strong> <span class="added">{added}</span> |
     <strong>Removed:</strong> <span class="removed">{removed}</span></p>
  <h2>Summary of Changes</h2>
  <table>
    <tr><th>Category</th><th>Added</th><th>Removed</th><th>Total</th></tr>"""]

    for cat in CATEGORIES.keys():
        a = summary_counts.get((cat, "Added"), 0)
        r = summary_counts.get((cat, "Removed"), 0)
        total = a + r
        html.append(f"<tr><td>{cat}</td><td class='added'>{a}</td><td class='removed'>{r}</td><td>{total}</td></tr>")

    html.append("</table>")

    for header, changes in report:
        html.append(f"<div class='commit'><h2>{header}</h2>")
        grouped = {}
        for action, cat, flag in changes:
            grouped.setdefault((action, cat), []).append(flag)
        for (action, cat), flags in grouped.items():
            html.append(f"<h3>{action} in {cat}</h3><ul>")
            for f in flags:
                html.append(f"<li class='{action.lower()}'><code>{f}</code></li>")
            html.append("</ul>")
        html.append("</div>")

    html.append("</body></html>")
    OUTPUT_HTML.write_text("\n".join(html), encoding="utf-8")

    log(f"Reports generated:\n- {OUTPUT_MD}\n- {OUTPUT_HTML}")
    return added, removed, date_str, report

# ===============================
# Landing Page
# ===============================
def ensure_landing_page(added, removed, last_run):
    index_html = OUTPUT_DIR / "index.html"
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta property="og:title" content="Roblox FFlag Tracker">
  <meta property="og:description" content="Live tracking of Roblox Client FFlag changes (last {DAYS} days)">
  <meta property="og:type" content="website">
  <title>Roblox FFlag Tracker Dashboard</title>
  <style>
    body {{
      margin: 0; font-family: 'Segoe UI', Arial, sans-serif;
      background: #0d1117; color: #c9d1d9;
    }}
    header {{
      background: linear-gradient(135deg, #1f2937, #111827);
      padding: 40px 20px; text-align: center;
      border-bottom: 1px solid #30363d;
    }}
    header h1 {{
      margin: 0; font-size: 2.2rem; color: #58a6ff;
    }}
    header p {{
      margin-top: 8px; color: #8b949e;
    }}
    nav {{
      margin-top: 20px;
    }}
    nav a {{
      color: #58a6ff; margin: 0 10px; text-decoration: none;
      font-weight: 500;
    }}
    nav a:hover {{ text-decoration: underline; }}
    .stats {{
      display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 20px; margin: 40px auto; max-width: 900px;
    }}
    .card {{
      padding: 20px; border-radius: 12px; background: #161b22;
      text-align: center; font-size: 1.5rem; font-weight: bold;
      box-shadow: 0 2px 6px rgba(0,0,0,0.4);
      transition: transform 0.2s;
    }}
    .card:hover {{ transform: translateY(-4px); }}
    .added {{ color: #4caf50; }}
    .removed {{ color: #f44336; }}
    .last-run {{
      text-align: center; font-style: italic; margin: 20px 0;
      color: #8b949e;
    }}
    iframe {{
      display: block; margin: 30px auto; width: 95%; height: 70vh;
      border: 1px solid #30363d; border-radius: 8px;
      background: #0d1117;
    }}
    footer {{
      margin-top: 40px; padding: 20px;
      text-align: center; background: #161b22; color: #8b949e;
      font-size: 0.9rem;
    }}
  </style>
</head>
<body>
  <header>
    <h1>Roblox Client FFlag Tracker</h1>
    <p>Tracking changes in <code>{TARGET_FILE}</code></p>
    <nav>
      <a href="index.html">Dashboard</a> |
      <a href="FFlag_Report.html">Full Report</a> |
      <a href="https://github.com/MaximumADHD/Roblox-FFlag-Tracker" target="_blank">GitHub Repo</a>
    </nav>
  </header>

  <section class="stats">
    <div class="card added">+ {added} <br><small>Flags Added</small></div>
    <div class="card removed">- {removed} <br><small>Flags Removed</small></div>
  </section>

  <p class="last-run">Last Run: {last_run}</p>

  <h2 style="text-align:center; color:#58a6ff;">Latest Report</h2>
  <iframe src="FFlag_Report.html"></iframe>

  <footer>
    <p>Generated automatically by <code>updateff.py</code> | Last Updated: {last_run}</p>
  </footer>
</body>
</html>"""
    index_html.write_text(html, encoding="utf-8")
    log(f"Landing page written: {index_html}")

# ===============================
# Main
# ===============================
def main():
    log("============================================================")
    log(" Roblox Client FFlag Intel Tracker with Categories ")
    log("============================================================")

    ensure_repo()
    commits = get_commits()
    if not commits:
        log("No commits in the last {DAYS} days.", level="WARN")
        return

    report, summary_counts = build_report(commits)
    added, removed, last_run, _ = export_reports(report, summary_counts)
    ensure_landing_page(added, removed, last_run)
    log("All done!", level="SUCCESS")

if __name__ == "__main__":
    main()
