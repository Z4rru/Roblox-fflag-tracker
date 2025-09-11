import os
import subprocess
import datetime

# -------------------------------
# Logging helper
# -------------------------------
def log(message, level="INFO"):
    now = datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S %p %Z")
    print(f"[{level}] {message} ({now})")

# -------------------------------
# Repo paths
# -------------------------------
BASE_DIR = os.getcwd()
REPO_DIR = os.path.join(BASE_DIR, "Roblox-Client-Tracker")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")

os.makedirs(OUTPUT_DIR, exist_ok=True)

# -------------------------------
# Clone fresh repo
# -------------------------------
if os.path.exists(REPO_DIR):
    subprocess.run(["rm", "-rf", REPO_DIR])
log("Cloning fresh Roblox-Client-Tracker repo...")
subprocess.run(
    ["git", "clone", "--depth", "50", "https://github.com/MaximumADHD/Roblox-Client-Tracker.git", REPO_DIR],
    check=True
)

# -------------------------------
# Extract changes in PCDesktopClient.json
# -------------------------------
os.chdir(REPO_DIR)

result = subprocess.run(
    ["git", "log", "--pretty=format:%H", "--", "PCDesktopClient.json"],
    capture_output=True,
    text=True,
    check=True
)

commits = result.stdout.strip().splitlines()
added_flags, removed_flags = [], []

if len(commits) < 2:
    log("Not enough history for PCDesktopClient.json, no diff available.", "WARN")
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
# Write Reports
# -------------------------------
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S %p %Z")

def write_reports():
    md_path = os.path.join(OUTPUT_DIR, "FFlag_Report.md")
    html_path = os.path.join(OUTPUT_DIR, "FFlag_Report.html")
    index_path = os.path.join(OUTPUT_DIR, "index.html")

    # Build report content
    if not added_flags and not removed_flags:
        md_content = f"# Roblox FFlag Report\n\n*Last Updated: {timestamp}*\n\nNo changes since last update."
        html_content = f"""
        <html>
        <head>
            <title>Roblox FFlag Report</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 20px; }}
                .card {{ border: 1px solid #ddd; padding: 20px; border-radius: 10px; max-width: 600px; }}
                h1 {{ color: #333; }}
            </style>
        </head>
        <body>
            <div class="card">
                <h1>Roblox FFlag Report</h1>
                <p><b>Last Updated:</b> {timestamp}</p>
                <p><i>No changes since last update.</i></p>
            </div>
        </body>
        </html>
        """
    else:
        md_content = f"# Roblox FFlag Report\n\n*Last Updated: {timestamp}*\n\n"
        html_content = f"""
        <html>
        <head>
            <title>Roblox FFlag Report</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 20px; }}
                .card {{ border: 1px solid #ddd; padding: 20px; border-radius: 10px; max-width: 800px; }}
                h1 {{ color: #333; }}
                h2 {{ color: #444; margin-top: 20px; }}
                ul {{ margin: 10px 0 20px 20px; }}
            </style>
        </head>
        <body>
            <div class="card">
                <h1>Roblox FFlag Report</h1>
                <p><b>Last Updated:</b> {timestamp}</p>
        """

        if added_flags:
            md_content += "## Added Flags\n" + "\n".join(f"- {flag}" for flag in added_flags) + "\n\n"
            html_content += "<h2>Added Flags</h2><ul>" + "".join(f"<li>{flag}</li>" for flag in added_flags) + "</ul>"

        if removed_flags:
            md_content += "## Removed Flags\n" + "\n".join(f"- {flag}" for flag in removed_flags) + "\n\n"
            html_content += "<h2>Removed Flags</h2><ul>" + "".join(f"<li>{flag}</li>" for flag in removed_flags) + "</ul>"

        html_content += "</div></body></html>"

    # Write files
    with open(md_path, "w") as f:
        f.write(md_content)
    with open(html_path, "w") as f:
        f.write(html_content)
    with open(index_path, "w") as f:
        f.write(html_content)

    log("Reports written:")
    log(f"- {md_path}")
    log(f"- {html_path}")
    log(f"- {index_path}")

write_reports()

log("All done!", "SUCCESS")
