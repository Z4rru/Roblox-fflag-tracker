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

FFLAG_REPO = "https://github.com/MaximumADHD/Roblox-FFlag-Tracker.git"
LOCAL_CLONE = WORKSPACE / "Roblox-FFlag-Tracker"

TRACK_FILE = "PCDesktopClient.json"  # file to track

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
        log("Updating existing repo...")
        run_cmd("git fetch --all", cwd=LOCAL_CLONE)
        run_cmd("git reset --hard origin/main", cwd=LOCAL_CLONE)
    else:
        log("Cloning fresh repo...")
        run_cmd(f"git clone {FFLAG_REPO} {LOCAL_CLONE}")

# ===============================
# Diffing logic
# ===============================
def analyze_flags(days=5):
    log(f"Analyzing {TRACK_FILE} for flag changes...")

    since_date = (datetime.datetime.now(ZoneInfo("UTC")) - datetime.timedelta(days=days)).strftime('%Y-%m-%d')
    log(f"Fetching commits since: {since_date} (last {days} days)")

    # Correct path: just TRACK_FILE in repo root
    commits_raw = run_cmd(
        f"git log --since='{since_date} 00:00:00' --pretty=format:'%H|%an|%ar|%s|%cd' -- {TRACK_FILE}",
        cwd=LOCAL_CLONE
    )
    commits = commits_raw.splitlines()
    log(f"Fetched commits: {commits}")

    if not commits:
        log(f"No commits in the past {days} days for {TRACK_FILE}", level="WARN")
        return 0, 0, []

    commit_details = []
    for entry in commits:
        parts = entry.split("|", maxsplit=4)
        if len(parts) != 5:
            continue
        commit_hash, author, relative_time, message, commit_date = parts

        # diff counting
        diff_raw = run_cmd(f"git diff {commit_hash}^ {commit_hash} -- {TRACK_FILE}", cwd=LOCAL_CLONE)
        diff_lines = diff_raw.splitlines()
        added = sum(1 for l in diff_lines if l.startswith("+") and not l.startswith("+++"))
        removed = sum(1 for l in diff_lines if l.startswith("-") and not l.startswith("---"))

        commit_info = {
            "hash": commit_hash,
            "author": author,
            "when": relative_time,
            "message": message,
            "commit_date": commit_date,
            "added": added,
            "removed": removed
        }
        log(f"Commit Details: {commit_info}")
        commit_details.append(commit_info)

    total_added = sum(c["added"] for c in commit_details)
    total_removed = sum(c["removed"] for c in commit_details)
    log(f"Detected {total_added} added flags, {total_removed} removed flags in the past {days} days.")

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

    added, removed, commit_details = analyze_flags(days=5)
    last_run = datetime.datetime.now(ZoneInfo("Asia/Manila")).strftime("%Y-%m-%d %I:%M:%S %p %Z")

    # Markdown
    md = []
    md.append(f"# Roblox Client FFlag Report — `{TRACK_FILE}` (Last 5 Days)\n")
    md.append(f"- **Last Run:** {last_run}")
    md.append(f"- **Flags Added:** {added}")
    md.append(f"- **Flags Removed:** {removed}\n")

    if commit_details:
        md.append("## Commit History\n")
        for c in commit_details:
            md.append(f"- `{c['hash']}` by {c['author']} ({c['when']}) — {c['message']}")
            md.append(f"  - Added: {c['added']} | Removed: {c['removed']}")
            md.append(f"  - Commit Date: {c['commit_date']}\n")

    md_report.write_text("\n".join(md), encoding="utf-8")

    # HTML Report — styled dark dashboard style
    commit_html = ""
    for c in commit_details:
        commit_html += f"""
        <section class="commit">
          <h3>Commit <code>{c['hash']}</code></h3>
          <p><strong>Author:</strong> {c['author']}</p>
          <p><strong>When:</strong> {c['when']}</p>
          <p><strong>Message:</strong> {c['message']}</p>
          <p><strong>Added:</strong> {c['added']} &nbsp;|&nbsp; <strong>Removed:</strong> {c['removed']}</p>
          <p><strong>Commit Date:</strong> {c['commit_date']}</p>
        </section>
        """

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Roblox Client FFlag Report — {TRACK_FILE}</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    body {{
      font-family: "Segoe UI", Roboto, Arial, sans-serif;
      background: #0d1117;
      color: #c9d1d9;
      margin: 0;
      padding: 0;
    }}
    header {{
      background: linear-gradient(135deg, #1f4068, #1b1b2f);
      color: #fff;
      padding: 40px 20px;
      text-align: center;
      box-shadow: 0 4px 20px rgba(0,0,0,0.4);
    }}
    header h1 {{
      font-size: 2.5rem;
      margin: 0;
    }}
    header p {{
      color: #8b949e;
      margin-top: 8px;
    }}
    .stats {{
      display: flex;
      justify-content: center;
      gap: 20px;
      margin: 30px auto;
      flex-wrap: wrap;
      max-width: 900px;
    }}
    .card {{
      flex: 1;
      min-width: 150px;
      padding: 25px;
      border-radius: 12px;
      font-size: 1.3em;
      text-align: center;
      font-weight: bold;
      background: #161b22;
      box-shadow: 0 4px 15px rgba(0,0,0,0.4);
    }}
    .added {{ color: #4caf50; }}
    .removed {{ color: #f44336; }}
    .last-run {{
      text-align: center;
      margin-top: 10px;
      font-style: italic;
      color: #8b949e;
    }}
    section.commit {{
      margin: 20px auto 40px auto;
      max-width: 900px;
      background: #161b22;
      padding: 20px;
      border-radius: 12px;
      box-shadow: 0 4px 10px rgba(0,0,0,0.3);
    }}
    section.commit h3 {{
      margin-top: 0;
      color: #58a6ff;
    }}
    code {{
      background: #21262d;
      color: #f0f6fc;
      padding: 2px 5px;
      border-radius: 4px;
    }}
    footer {{
      text-align: center;
      padding: 20px;
      background: #1b1b2f;
      color: #8b949e;
      margin-top: 40px;
    }}
  </style>
</head>
<body>
  <header>
    <h1>Roblox Client FFlag Tracker</h1>
    <p>Tracking `{TRACK_FILE}` changes (Last 5 Days)</p>
  </header>

  <div class="stats">
    <div class="card added">Added: <span class="added">{added}</span></div>
    <div class="card removed">Removed: <span class="removed">{removed}</span></div>
  </div>

  <p class="last-run">Last Run: <span>{last_run}</span></p>

  {commit_html}

  <footer>
    <p>⚡ Generated via Roblox-FFlag-Tracker • Live updates on GitHub Pages</p>
  </footer>
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
    # Make landing page same design style
    commit_html = ""
    if commit_details:
        for c in commit_details:
            commit_html += f"""
            <section class="commit">
              <h3>Commit <code>{c['hash']}</code></h3>
              <p><strong>Author:</strong> {c['author']}</p>
              <p><strong>Message:</strong> {c['message']}</p>
              <p><strong>Added:</strong> {c['added']} &nbsp;|&nbsp; <strong>Removed:</strong> {c['removed']}</p>
            </section>
            """

    index_html = output_dir / "index.html"
    content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Roblox FFlag Dashboard</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    body {{
      font-family: "Segoe UI", Roboto, Arial, sans-serif;
      background: #0d1117;
      color: #c9d1d9;
      margin: 0;
      padding: 0;
    }}
    header {{
      background: linear-gradient(135deg, #1f4068, #1b1b2f);
      color: #fff;
      padding: 40px 20px;
      text-align: center;
      box-shadow: 0 4px 20px rgba(0,0,0,0.4);
    }}
    header h1 {{
      font-size: 2.5rem;
      margin: 0;
    }}
    header p {{
      color: #8b949e;
      margin-top: 8px;
    }}
    .stats {{
      display: flex;
      justify-content: center;
      gap: 20px;
      margin: 30px auto;
      flex-wrap: wrap;
      max-width: 900px;
    }}
    .card {{
      flex: 1;
      min-width: 150px;
      padding: 25px;
      border-radius: 12px;
      font-size: 1.3em;
      text-align: center;
      font-weight: bold;
      background: #161b22;
      box-shadow: 0 4px 15px rgba(0,0,0,0.4);
    }}
    .added {{ color: #4caf50; }}
    .removed {{ color: #f44336; }}
    .last-run {{
      text-align: center;
      margin-top: 10px;
      font-style: italic;
      color: #8b949e;
    }}
    section.commit {{
      margin: 20px auto;
      max-width: 900px;
      background: #161b22;
      padding: 20px;
      border-radius: 12px;
      box-shadow: 0 4px 10px rgba(0,0,0,0.3);
    }}
    section.commit h3 {{
      margin-top: 0;
      color: #58a6ff;
    }}
    code {{
      background: #21262d;
      color: #f0f6fc;
      padding: 2px 5px;
      border-radius: 4px;
    }}
    footer {{
      text-align: center;
      padding: 20px;
      background: #1b1b2f;
      color: #8b949e;
      margin-top: 40px;
    }}
    a {{
      color: #58a6ff;
      text-decoration: none;
    }}
    a:hover {{
      text-decoration: underline;
    }}
  </style>
</head>
<body>
  <header>
    <h1>Roblox FFlag Dashboard</h1>
    <p>Live: {TRACK_FILE} changes</p>
  </header>

  <div class="stats">
    <div class="card added">Added: <span class="added">{added}</span></div>
    <div class="card removed">Removed: <span class="removed">{removed}</span></div>
  </div>

  <p class="last-run">Last Run: <span>{last_run}</span></p>

  {commit_html}

  <footer>
    <p>View full report: <a href="FFlag_Report.html">Report Page</a> | Markdown version available</p>
  </footer>
</body>
</html>
"""
    index_html.write_text(content, encoding="utf-8")
    log(f"Landing page updated: {index_html}")

# ===============================
# Main
# ===============================
def main():
    log("============================================================")
    log(" Roblox Client FFlag Tracker Dashboard ")
    log("============================================================")

    clone_or_update_repo()
    added, removed, last_run, commit_details = generate_reports()
    ensure_landing_page(OUTPUT_DIR, added, removed, last_run, commit_details)

    log("All done!", level="SUCCESS")

if __name__ == "__main__":
    main()
