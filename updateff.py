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
TARGET_FILE = "PCDesktopClient.json"   # ✅ fixed path

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
        run_cmd("git reset --hard origin/main", cwd=LOCAL_CLONE)
    else:
        log("Cloning fresh Roblox-Client-Tracker repo...")
        run_cmd(f"git clone {FFLAG_REPO} {LOCAL_CLONE}")

# ===============================
# Diffing logic
# ===============================
def analyze_flags():
    log(f"Analyzing {TARGET_FILE} for flag changes...")

    since_date = (datetime.datetime.now(ZoneInfo("UTC")) - datetime.timedelta(days=5)).strftime('%Y-%m-%d')
    log(f"Fetching commits since: {since_date}")

    commits = run_cmd(
        f"git log --since='{since_date} 00:00:00' --pretty=format:'%H|%an|%ar|%s|%cd' -- {TARGET_FILE}",
        cwd=LOCAL_CLONE
    ).splitlines()

    log(f"Fetched commits: {commits}")

    if not commits or commits == ['']:
        log(f"No commits in the past 5 days for {TARGET_FILE}", level="WARN")
        return 0, 0, []

    commit_details = []
    for commit in commits:
        commit_hash, author, relative_time, message, commit_date = commit.split("|", 4)
        log(f"Commit Details: {commit_hash} | {author} | {relative_time} | {message} | {commit_date}")

        diff = run_cmd(f"git diff {commit_hash}^ {commit_hash} -- {TARGET_FILE}", cwd=LOCAL_CLONE).splitlines()
        added, removed = 0, 0
        for line in diff:
            if line.startswith("+") and not line.startswith("+++"):
                added += 1
            elif line.startswith("-") and not line.startswith("---"):
                removed += 1

        commit_details.append({
            "hash": commit_hash,
            "author": author,
            "when": relative_time,
            "message": message,
            "commit_date": commit_date,
            "added": added,
            "removed": removed
        })

    total_added = sum(c["added"] for c in commit_details)
    total_removed = sum(c["removed"] for c in commit_details)

    log(f"Detected {total_added} added flags, {total_removed} removed flags in the past 5 days.")
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

    # Markdown
    md_content = f"# Roblox Client FFlag Report (Last 5 Days)\n\n"
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

    # HTML (Dark DMZ Style)
    commit_html = "".join([
        f"""
        <section class="commit">
          <h3>🔗 {c['hash'][:7]} - {c['message']}</h3>
          <p><strong>Author:</strong> {c['author']} | <strong>When:</strong> {c['when']}</p>
          <p><strong>Flags Added:</strong> <span class="added">{c['added']}</span> | 
             <strong>Flags Removed:</strong> <span class="removed">{c['removed']}</span></p>
          <p><em>{c['commit_date']}</em></p>
        </section>
        """ for c in commit_details
    ])

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Roblox FFlag Report</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    body {{ margin:0; font-family: 'Segoe UI', sans-serif; background:#0f172a; color:#e2e8f0; }}
    header {{ background:#1e293b; padding:30px; text-align:center; }}
    header h1 {{ margin:0; font-size:2.2em; color:#38bdf8; }}
    header p {{ margin:8px 0 0; color:#94a3b8; }}
    .stats {{ display:flex; justify-content:center; gap:20px; margin:30px; flex-wrap:wrap; }}
    .card {{ flex:1; min-width:150px; background:#1e293b; padding:20px; border-radius:12px; text-align:center; }}
    .card span {{ font-size:1.6em; font-weight:bold; }}
    .added {{ color:#22c55e; }}
    .removed {{ color:#ef4444; }}
    .last-run {{ text-align:center; margin-bottom:20px; color:#94a3b8; }}
    section.commit {{ background:#1e293b; margin:15px auto; max-width:800px; padding:15px 20px; border-radius:10px; }}
    footer {{ text-align:center; padding:20px; margin-top:40px; background:#1e293b; color:#64748b; }}
    code {{ background:#334155; padding:2px 4px; border-radius:4px; }}
  </style>
</head>
<body>
  <header>
    <h1>Roblox Client FFlag Tracker</h1>
    <p>Automated Intel — Last 5 Days</p>
  </header>

  <section class="stats">
    <div class="card added">Added<br><span>{added}</span></div>
    <div class="card removed">Removed<br><span>{removed}</span></div>
  </section>

  <p class="last-run">Last Run: {last_run}</p>
  {commit_html}

  <footer>
    <p>⚡ Generated by Roblox FFlag Tracker</p>
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
    shutil.copy(output_dir / "FFlag_Report.html", output_dir / "index.html")
    log(f"Landing page written: {output_dir/'index.html'}")

# ===============================
# Main
# ===============================
def main():
    log("============================================================")
    log(" Roblox Client FFlag Intel Tracker (Past 5 Days) ")
    log("============================================================")

    clone_or_update_repo()
    added, removed, last_run, commit_details = generate_reports()
    ensure_landing_page(OUTPUT_DIR, added, removed, last_run, commit_details)

    log("All done!", level="SUCCESS")

if __name__ == "__main__":
    main()
