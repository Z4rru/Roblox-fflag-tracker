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
subprocess.run(
    ["git", "clone", "https://github.com/MaximumADHD/Roblox-Client-Tracker.git", REPO_DIR],
    check=True
)

# -------------------------------
# Extract changes in PCDesktopClient.json
# -------------------------------
os.chdir(REPO_DIR)

result = subprocess.run(
    ["git", "log", "-n", "2", "--pretty=format:%H", "--", "PCDesktopClient.json"],
    capture_output=True,
    text=True,
    check=True
)

commits = result.stdout.strip().splitlines()
added_flags, removed_flags = [], []

if len(commits) < 2:
    log("Only one commit found for PCDesktopClient.json, no diff available.", "WARN")
else:
    latest, previous = commits[0], commits[1]

    diff = subprocess.run(
        ["git", "diff", previous, latest, "--", "PCDesktopClient.json"],
        capture_output=True,
        text=True,
        check=True
    ).stdout.splitlines()

    for line in diff:
        if line.startswith("+") and not line.startswith("+++"):
            added_flags.append(line[1:].strip())
        elif line.startswith("-") and not line.startswith("---"):
            removed_flags.append(line[1:].strip())

log(f"Detected {len(added_flags)} added flags, {len(removed_flags)} removed flags.")

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

- **Added:** {len(added_flags)}  
- **Removed:** {len(removed_flags)}  

## Added Flags
{"\n".join(f"- `{flag}`" for flag in added_flags) if added_flags else "_None_"}

## Removed Flags
{"\n".join(f"- `{flag}`" for flag in removed_flags) if removed_flags else "_None_"}

_Source: [Roblox-Client-Tracker](https://github.com/MaximumADHD/Roblox-Client-Tracker)_
"""

html_report = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Roblox FFlag Tracker</title>
  <style>
    body {{
      font-family: 'Inter', Arial, sans-serif;
      background: #f4f6fb;
      margin: 0;
      padding: 0;
      color: #333;
    }}
    header {{
      background: linear-gradient(135deg, #1e3c72, #2a5298);
      color: #fff;
      padding: 40px 20px;
      text-align: center;
      box-shadow: 0 4px 12px rgba(0,0,0,0.3);
    }}
    header h1 {{
      margin: 0;
      font-size: 2.5rem;
    }}
    .stats {{
      display: flex;
      justify-content: center;
      gap: 20px;
      margin: 30px auto;
      max-width: 600px;
      flex-wrap: wrap;
    }}
    .card {{
      flex: 1;
      min-width: 200px;
      padding: 20px;
      border-radius: 12px;
      font-size: 1.2em;
      font-weight: bold;
      text-align: center;
      color: #fff;
      box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }}
    .added {{ background: #4caf50; }}
    .removed {{ background: #f44336; }}
    .last-run {{
      text-align: center;
      margin-top: 10px;
      font-style: italic;
      color: #555;
    }}
    main {{
      max-width: 900px;
      margin: 40px auto;
      padding: 0 20px;
    }}
    h2 {{
      margin-top: 30px;
      color: #1e3c72;
    }}
    ul {{
      background: white;
      padding: 20px;
      border-radius: 10px;
      box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    }}
    li {{
      font-family: monospace;
      margin: 5px 0;
    }}
    footer {{
      text-align: center;
      padding: 20px;
      margin-top: 40px;
      background: #1e3c72;
      color: white;
    }}
    footer a {{ color: #ffd54f; text-decoration: none; }}
  </style>
</head>
<body>
  <header>
    <h1>Roblox Client FFlag Tracker</h1>
    <p>Last Updated: {last_run}</p>
  </header>
  <section class="stats">
    <div class="card added">Added Flags: {len(added_flags)}</div>
    <div class="card removed">Removed Flags: {len(removed_flags)}</div>
  </section>
  <p class="last-run">Last Run: {last_run}</p>
  <main>
    <h2>✅ Added Flags</h2>
    {"<ul>" + "".join(f"<li>{flag}</li>" for flag in added_flags) + "</ul>" if added_flags else "<p>None</p>"}
    <h2>❌ Removed Flags</h2>
    {"<ul>" + "".join(f"<li>{flag}</li>" for flag in removed_flags) + "</ul>" if removed_flags else "<p>None</p>"}
  </main>
  <footer>
    Source: <a href="https://github.com/MaximumADHD/Roblox-Client-Tracker" target="_blank">Roblox-Client-Tracker</a>
  </footer>
</body>
</html>
"""

with open(os.path.join(OUTPUT_DIR, "FFlag_Report.md"), "w", encoding="utf-8") as f:
    f.write(md_report)

with open(os.path.join(OUTPUT_DIR, "FFlag_Report.html"), "w", encoding="utf-8") as f:
    f.write(html_report)

shutil.copy(os.path.join(OUTPUT_DIR, "FFlag_Report.html"), os.path.join(OUTPUT_DIR, "index.html"))

log("Reports written:")
log(f"- {os.path.join(OUTPUT_DIR, 'FFlag_Report.md')}")
log(f"- {os.path.join(OUTPUT_DIR, 'FFlag_Report.html')}")
log(f"Landing page written: {os.path.join(OUTPUT_DIR, 'index.html')}")
log("All done!", "SUCCESS")
