#!/usr/bin/env python3
import os
import subprocess
import datetime
from zoneinfo import ZoneInfo
import shutil

# -------------------------------
# Helpers
# -------------------------------
def log(msg, level="INFO"):
    ts = datetime.datetime.now(ZoneInfo("Asia/Manila")).strftime("%Y-%m-%d %I:%M:%S %p %Z")
    print(f"[{level}] {msg} ({ts})")

# -------------------------------
# Setup paths
# -------------------------------
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
WORKSPACE = os.path.join(SCRIPT_DIR)
OUTPUT_DIR = os.path.join(WORKSPACE, "output")

if os.path.exists(OUTPUT_DIR):
    shutil.rmtree(OUTPUT_DIR)
os.makedirs(OUTPUT_DIR, exist_ok=True)

# -------------------------------
# Clone Roblox Client Tracker
# -------------------------------
log("============================================================")
log(" Roblox Client FFlag Intel Tracker ")
log("============================================================")

REPO_DIR = os.path.join(WORKSPACE, "Roblox-Client-Tracker")
if os.path.exists(REPO_DIR):
    shutil.rmtree(REPO_DIR)

log("Cloning fresh Roblox-Client-Tracker repo...")
# clone full history to avoid missing commits
subprocess.run(
    ["git", "clone", "https://github.com/MaximumADHD/Roblox-Client-Tracker.git", REPO_DIR],
    check=True
)

# -------------------------------
# Extract changes in PCDesktopClient.json
# -------------------------------
os.chdir(REPO_DIR)

# Get latest 2 commits for PCDesktopClient.json
result = subprocess.run(
    ["git", "log", "-n", "2", "--pretty=format:%H", "--", "PCDesktopClient.json"],
    capture_output=True,
    text=True,
    check=True
)

commits = result.stdout.strip().splitlines()

added, removed = 0, 0
if len(commits) < 2:
    log("Only one commit found for PCDesktopClient.json, no diff available.", "WARN")
else:
    latest, previous = commits[0], commits[1]

    # Diff between latest and previous commit
    diff = subprocess.run(
        ["git", "diff", previous, latest, "--", "PCDesktopClient.json"],
        capture_output=True,
        text=True,
        check=True
    ).stdout.splitlines()

    added = sum(1 for line in diff if line.startswith("+") and not line.startswith("+++"))
    removed = sum(1 for line in diff if line.startswith("-") and not line.startswith("---"))

log(f"Detected {added} added flags, {removed} removed flags.")

# -------------------------------
# Time (Philippines)
# -------------------------------
ph_time = datetime.datetime.now(ZoneInfo("Asia/Manila"))
last_run = ph_time.strftime("%Y-%m-%d %I:%M:%S %p %Z")

# -------------------------------
# Generate Reports
# -------------------------------
md_report = f"""# Roblox Client FFlag Tracker

**Last Updated:** {last_run}  

- **Added:** {added}  
- **Removed:** {removed}  

_Source: [Roblox-Client-Tracker](https://github.com/MaximumADHD/Roblox-Client-Tracker)_
"""

html_report = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Roblox FFlag Tracker</title>
  <style>
    body {{
      font-family: Arial, sans-serif;
      background: linear-gradient(135deg, #1e1e2f, #2c3e50);
      color: #f5f5f5;
      margin: 0;
      padding: 0;
      text-align: center;
    }}
    header {{
      background: #111827;
      padding: 20px;
      box-shadow: 0 2px 10px rgba(0,0,0,0.5);
    }}
    h1 {{
      margin: 0;
      font-size: 2.5rem;
    }}
    .content {{
      margin: 40px auto;
      max-width: 600px;
      background: #1f2937;
      padding: 30px;
      border-radius: 12px;
      box-shadow: 0 5px 20px rgba(0,0,0,0.3);
    }}
    .stat {{
      font-size: 1.3rem;
      margin: 15px 0;
      padding: 10px;
      border-radius: 8px;
    }}
    .added {{
      background: #065f46;
      color: #d1fae5;
    }}
    .removed {{
      background: #7f1d1d;
      color: #fee2e2;
    }}
    footer {{
      margin: 40px 0 20px;
      font-size: 0.9rem;
      color: #9ca3af;
    }}
  </style>
</head>
<body>
  <header>
    <h1>Roblox Client FFlag Tracker</h1>
    <p>Last Updated: {last_run}</p>
  </header>
  <div class="content">
    <div class="stat added">Added Flags: {added}</div>
    <div class="stat removed">Removed Flags: {removed}</div>
  </div>
  <footer>
    Source: <a href="https://github.com/MaximumADHD/Roblox-Client-Tracker" style="color:#60a5fa;">Roblox-Client-Tracker</a>
  </footer>
</body>
</html>
"""

with open(os.path.join(OUTPUT_DIR, "FFlag_Report.md"), "w", encoding="utf-8") as f:
    f.write(md_report)

with open(os.path.join(OUTPUT_DIR, "FFlag_Report.html"), "w", encoding="utf-8") as f:
    f.write(html_report)

# Copy HTML to index.html
shutil.copy(os.path.join(OUTPUT_DIR, "FFlag_Report.html"), os.path.join(OUTPUT_DIR, "index.html"))

log("Reports written:")
log(f"- {os.path.join(OUTPUT_DIR, 'FFlag_Report.md')}")
log(f"- {os.path.join(OUTPUT_DIR, 'FFlag_Report.html')}")
log(f"Landing page written: {os.path.join(OUTPUT_DIR, 'index.html')}")
log("All done!", "SUCCESS")
