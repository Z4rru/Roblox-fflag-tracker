#!/usr/bin/env python3
import os
import subprocess
import shutil
import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

# ===============================
# Configuration
# ===============================
SCRIPT_DIR = Path(__file__).resolve().parent
WORKSPACE = SCRIPT_DIR
OUTPUT_DIR = WORKSPACE / "output"

FFLAG_REPO = "https://github.com/MaximumADHD/Roblox-Client-Tracker.git"
LOCAL_CLONE = WORKSPACE / "Roblox-Client-Tracker"

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

# ===============================
# Repo sync
# ===============================
def clone_or_update_repo():
    if LOCAL_CLONE.exists():
        log("Updating existing Roblox-Client-Tracker repo...")
        run_cmd("git fetch --all", cwd=LOCAL_CLONE)
        run_cmd("git reset --hard origin/master", cwd=LOCAL_CLONE)
    else:
        log("Cloning fresh Roblox-Client-Tracker repo...")
        run_cmd(f"git clone {FFLAG_REPO} {LOCAL_CLONE}")

# ===============================
# Diffing logic
# ===============================
def analyze_flags():
    log("Analyzing PCDesktopClient.json for flag changes...")
    commits = run_cmd("git log --pretty=format:%H -- PCDesktopClient.json", cwd=LOCAL_CLONE).splitlines()

    if len(commits) < 2:
        log("Not enough commits for PCDesktopClient.json", level="WARN")
        return 0, 0, None

    latest, previous = commits[0], commits[1]
    diff = run_cmd(f"git diff {previous} {latest} -- PCDesktopClient.json", cwd=LOCAL_CLONE).splitlines()

    added, removed = 0, 0
    for line in diff:
        if line.startswith("+") and not line.startswith("+++"):
            added += 1
        elif line.startswith("-") and not line.startswith("---"):
            removed += 1

    # Fetch commit metadata for latest
    metadata = run_cmd(
        f'git log -1 --pretty=format:"%H|%an|%ad" --date=iso {latest}',
        cwd=LOCAL_CLONE
    )
    commit_hash, author, date = metadata.split("|")
    commit_info = {
        "hash": commit_hash,
        "author": author,
        "date": date
    }

    log(f"Detected {added} added flags, {removed} removed flags.")
    log(f"Latest commit: {commit_hash} by {author} on {date}")
    return added, removed, commit_info

# ===============================
# Report generation
# ===============================
def generate_reports():
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    md_report = OUTPUT_DIR / "FFlag_Report.md"
    html_report = OUTPUT_DIR / "FFlag_Report.html"

    added, removed, commit_info = analyze_flags()
    last_run = datetime.datetime.now(ZoneInfo("Asia/Manila")).strftime("%Y-%m-%d %I:%M:%S %p %Z")

    # Markdown
    md_content = f"# Roblox Client FFlag Report\n\n"
    md_content += f"- **Last Run:** {last_run}\n"
    md_content += f"- **Flags Added:** {added}\n"
    md_content += f"- **Flags Removed:** {removed}\n"
    if commit_info:
        md_content += f"- **Latest Commit:** `{commit_info['hash']}` by {commit_info['author']} on {commit_info['date']}\n"

    md_report.write_text(md_content, encoding="utf-8")

    # HTML
    commit_html = ""
    if commit_info:
        commit_html = f"""
        <div class="commit">
          <p><strong>Latest Commit:</strong></p>
          <p>Hash: <code>{commit_info['hash']}</code></p>
          <p>Author: {commit_info['author']}</p>
          <p>Date: {commit_info['date']}</p>
        </div>
        """

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>FFlag Report</title>
  <style>
    body {{ font-family: Arial, sans-serif; margin: 20px; background: #f4f6fb; }}
    h1 {{ color: #1e3c72; }}
    .stats {{ display: flex; gap: 20px; margin: 20px 0; }}
    .card {{
      flex: 1;
      padding: 20px;
      border-radius: 12px;
      box-shadow: 0 4px 12px rgba(0,0,0,0.1);
      background: white;
      text-align: center;
      font-size: 1.2em;
      font-weight: bold;
    }}
    .added {{ color: #4caf50; }}
    .removed {{ color: #f44336; }}
    .last-run {{ margin-top: 10px; font-style: italic; color: #555; }}
    .commit {{ margin-top: 20px; padding: 15px; background: #fff; border-radius: 10px; box-shadow: 0 2px 6px rgba(0,0,0,0.08); }}
    code {{ background: #eee; padding: 2px 4px; border-radius: 4px; }}
  </style>
</head>
<body>
  <h1>Roblox Client FFlag Report</h1>
  <div class="stats">
    <div class="card added">Added: {added}</div>
    <div class="card removed">Removed: {removed}</div>
  </div>
  <p class="last-run">Last Run: {last_run}</p>
  {commit_html}
</body>
</html>
"""
    html_report.write_text(html_content, encoding="utf-8")

    log(f"Reports written:\n- {md_report}\n- {html_report}")
    return added, removed, last_run, commit_info

# ===============================
# Landing page
# ===============================
def ensure_landing_page(output_dir: Path, added, removed, last_run, commit_info):
    commit_html = ""
    if commit_info:
        commit_html = f"""
        <section class="commit">
          <h3>🔗 Latest Commit</h3>
          <p><strong>Hash:</strong> <code>{commit_info['hash']}</code></p>
          <p><strong>Author:</strong> {commit_info['author']}</p>
          <p><strong>Date:</strong> {commit_info['date']}</p>
        </section>
        """

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Roblox FFlag Tracker</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <!-- Google Font -->
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">

  <style>
    :root {{
      --primary: #1e3c72;
      --secondary: #2a5298;
      --bg: #f4f6fb;
      --card-bg: #fff;
      --added: #4caf50;
      --removed: #f44336;
      --shadow: 0 4px 12px rgba(0,0,0,0.12);
      --radius: 12px;
    }}

    body {{
      font-family: "Inter", sans-serif;
      background: var(--bg);
      color: #333;
      line-height: 1.6;
    }}

    header {{
      background: linear-gradient(135deg, var(--primary), var(--secondary));
      color: #fff;
      padding: 40px 20px;
      text-align: center;
      box-shadow: var(--shadow);
    }}
    header h1 {{ font-size: 2.5rem; font-weight: 700; }}
    header p {{ margin-top: 10px; font-size: 1.1rem; opacity: 0.9; }}

    nav {{
      background: #fff;
      padding: 12px 20px;
      text-align: center;
      box-shadow: var(--shadow);
    }}
    nav a {{
      margin: 0 15px;
      text-decoration: none;
      font-weight: 600;
      color: var(--primary);
    }}
    nav a:hover {{ text-decoration: underline; }}

    .stats {{
      display: flex;
      justify-content: center;
      gap: 20px;
      margin: 30px auto;
      flex-wrap: wrap;
      max-width: 900px;
    }}
    .badge {{
      flex: 1;
      min-width: 150px;
      padding: 20px;
      border-radius: var(--radius);
      font-size: 1.3em;
      font-weight: 600;
      text-align: center;
      box-shadow: var(--shadow);
      color: #fff;
    }}
    .added {{ background: var(--added); }}
    .removed {{ background: var(--removed); }}

    .last-run {{
      text-align: center;
      margin-top: 10px;
      font-style: italic;
      color: #555;
    }}

    main {{
      max-width: 1100px;
      margin: 40px auto;
      padding: 0 20px;
    }}
    main h2 {{ text-align: center; margin-bottom: 20px; color: var(--primary); }}
    iframe {{
      width: 100%;
      height: 70vh;
      border: none;
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      background: var(--card-bg);
    }}

    .commit {{
      max-width: 800px;
      margin: 20px auto;
      padding: 20px;
      background: #fff;
      border-radius: var(--radius);
      box-shadow: var(--shadow);
    }}
    .commit code {{
      background: #eee;
      padding: 2px 6px;
      border-radius: 4px;
    }}

    footer {{
      text-align: center;
      padding: 25px;
      margin-top: 40px;
      background: var(--primary);
      color: white;
      font-size: 0.95em;
    }}
    footer a {{ color: #ffd54f; text-decoration: none; }}
    footer a:hover {{ text-decoration: underline; }}
  </style>
</head>
<body>
  <header>
    <h1>Roblox Client FFlag Tracker</h1>
    <p>Automatic updates every 6 hours — track feature flag changes in real time</p>
  </header>

  <nav>
    <a href="index.html">Home</a>
    <a href="FFlag_Report.html">HTML Report</a>
    <a href="FFlag_Report.md">Markdown Report</a>
    <a href="https://github.com/z4rru/Roblox-fflag-tracker" target="_blank">GitHub</a>
  </nav>

  <section class="stats">
    <div class="badge added">Added: <span>{added}</span></div>
    <div class="badge removed">Removed: <span>{removed}</span></div>
  </section>

  <p class="last-run">Last Run: <span>{last_run}</span></p>

  {commit_html}

  <main>
    <h2>📊 Latest Report</h2>
    <iframe src="FFlag_Report.html"></iframe>
  </main>

  <footer>
    <p>Generated automatically by <strong>Roblox FFlag Tracker</strong>. 
    Access reports: <a href="FFlag_Report.html">HTML</a> | <a href="FFlag_Report.md">Markdown</a></p>
  </footer>
</body>
</html>
"""
    (output_dir / "index.html").write_text(html, encoding="utf-8")
    log(f"Landing page written: {output_dir/'index.html'}")

# ===============================
# Main
# ===============================
def main():
    log("============================================================")
    log(" Roblox Client FFlag Intel Tracker ")
    log("============================================================")

    clone_or_update_repo()
    added, removed, last_run, commit_info = generate_reports()
    ensure_landing_page(OUTPUT_DIR, added, removed, last_run, commit_info)

    log("All done!", level="SUCCESS")

if __name__ == "__main__":
    main()
