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

    # Fetch commit hashes for PCDesktopClient.json from the last 2 days
    since_date = (datetime.datetime.now() - datetime.timedelta(days=2)).strftime('%Y-%m-%d')
    
    # Log the date being used for filtering
    log(f"Fetching commits since: {since_date}")

    # Fetch all commits from the last 2 days (considering the exact time)
    commits = run_cmd(
        f"git log --since='{since_date} 00:00:00' --pretty=format:'%H|%an|%ar|%s|%cd' -- ClientSettings/PCDesktopClient.json",
        cwd=LOCAL_CLONE
    ).splitlines()

    # Debug log to confirm which commits are being fetched
    log(f"Fetched commits: {commits}")

    if len(commits) < 1:
        log("No commits in the past 2 days for PCDesktopClient.json", level="WARN")
        return 0, 0, []

    commit_details = []
    for commit in commits:
        commit_hash, author, relative_time, message, commit_date = commit.split("|")
        
        # Log full commit details for debugging
        log(f"Commit Details: {commit_hash} | {author} | {relative_time} | {message} | {commit_date}")

        # Fetch diff for each commit
        diff = run_cmd(f"git diff {commit_hash}^ {commit_hash} -- ClientSettings/PCDesktopClient.json", cwd=LOCAL_CLONE).splitlines()

        added, removed = 0, 0
        for line in diff:
            if line.startswith("+") and not line.startswith("+++"):
                added += 1
            elif line.startswith("-") and not line.startswith("---"):
                removed += 1

        commit_info = {
            "hash": commit_hash,
            "author": author,
            "when": relative_time,
            "message": message,
            "commit_date": commit_date,
            "added": added,
            "removed": removed
        }

        commit_details.append(commit_info)

    total_added = sum(c["added"] for c in commit_details)
    total_removed = sum(c["removed"] for c in commit_details)

    log(f"Detected {total_added} added flags, {total_removed} removed flags in the past 2 days.")
    return total_added, total_removed, commit_details

# ===============================
# Report generation
# ===============================
def generate_reports():
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    md_report = OUTPUT_DIR / "FFlag_Report.md"
    html_report = OUTPUT_DIR / "FFlag_Report.html"

    added, removed, commit_details = analyze_flags()
    last_run = datetime.datetime.now(ZoneInfo("Asia/Manila")).strftime("%Y-%m-%d %I:%M:%S %p %Z")

    # Markdown Report
    md_content = f"# Roblox Client FFlag Report (Last 2 Days)\n\n"
    md_content += f"- **Last Run:** {last_run}\n"
    md_content += f"- **Flags Added:** {added}\n"
    md_content += f"- **Flags Removed:** {removed}\n"
    if commit_details:
        md_content += "\n## Commit History\n"
        for commit in commit_details:
            md_content += f"- `{commit['hash']}` by {commit['author']} ({commit['when']}) - {commit['message']}\n"
            md_content += f"  - **Added:** {commit['added']} | **Removed:** {commit['removed']}\n"
            md_content += f"  - **Commit Date:** {commit['commit_date']}\n"

    md_report.write_text(md_content, encoding="utf-8")

    # HTML Report
    commit_html = ""
    if commit_details:
        for commit in commit_details:
            commit_html += f"""
            <div class="commit">
              <p><strong>Commit:</strong> <code>{commit['hash']}</code></p>
              <p><strong>Author:</strong> {commit['author']}</p>
              <p><strong>When:</strong> {commit['when']}</p>
              <p><strong>Message:</strong> {commit['message']}</p>
              <p><strong>Flags Added:</strong> {commit['added']} | <strong>Flags Removed:</strong> {commit['removed']}</p>
              <p><strong>Commit Date:</strong> {commit['commit_date']}</p>
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
  <h1>Roblox Client FFlag Report (Last 2 Days)</h1>
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
    return added, removed, last_run, commit_details

# ===============================
# Landing page
# ===============================
def ensure_landing_page(output_dir: Path, added, removed, last_run, commit_details):
    commit_html = ""
    if commit_details:
        for commit in commit_details:
            commit_html += f"""
            <section class="commit">
              <h3>🔗 Commit</h3>
              <p><strong>Hash:</strong> <code>{commit['hash']}</code></p>
              <p><strong>Author:</strong> {commit['author']}</p>
              <p><strong>When:</strong> {commit['when']}</p>
              <p><strong>Message:</strong> {commit['message']}</p>
              <p><strong>Flags Added:</strong> {commit['added']} | <strong>Flags Removed:</strong> {commit['removed']}</p>
              <p><strong>Commit Date:</strong> {commit['commit_date']}</p>
            </section>
            """

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Roblox FFlag Tracker</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <style>
    body {{
      font-family: Arial, sans-serif;
      background: #f4f6fb;
      color: #333;
      line-height: 1.6;
    }}
    header {{
      background: linear-gradient(135deg, #1e3c72, #2a5298);
      color: #fff;
      padding: 40px 20px;
      text-align: center;
    }}
    header h1 {{ font-size: 2.5rem; font-weight: 700; }}
    header p {{ margin-top: 10px; font-size: 1.1rem; }}
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
      border-radius: 12px;
      font-size: 1.3em;
      text-align: center;
      background: white;
    }}
    .added {{ background: #4caf50; color: white; }}
    .removed {{ background: #f44336; color: white; }}
    .last-run {{
      text-align: center;
      margin-top: 10px;
      font-style: italic;
      color: #555;
    }}
    section.commit {{
      margin: 20px auto;
      max-width: 800px;
      background: #fff;
      padding: 20px;
      border-radius: 10px;
      box-shadow: 0 2px 6px rgba(0,0,0,0.08);
    }}
    footer {{
      text-align: center;
      padding: 25px;
      margin-top: 40px;
      background: #1e3c72;
      color: white;
    }}
  </style>
</head>
<body>
  <header>
    <h1>Roblox Client FFlag Tracker</h1>
    <p>Automatic updates — tracking changes in the last 2 days</p>
  </header>

  <section class="stats">
    <div class="badge added">Added: <span>{added}</span></div>
    <div class="badge removed">Removed: <span>{removed}</span></div>
  </section>

  <p class="last-run">Last Run: <span>{last_run}</span></p>

  {commit_html}

  <footer>
    <p>Generated automatically by Roblox FFlag Tracker.</p>
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
    log(" Roblox Client FFlag Intel Tracker (Past 2 Days) ")
    log("============================================================")

    clone_or_update_repo()
    added, removed, last_run, commit_details = generate_reports()
    ensure_landing_page(OUTPUT_DIR, added, removed, last_run, commit_details)

    log("All done!", level="SUCCESS")

if __name__ == "__main__":
    main()
