import os
import re
import sys
import subprocess
from datetime import datetime, timedelta
from pathlib import Path

# --- Settings ---
TRACKER_DIR = Path.home() / "Roblox-FFlag-Tracker"
REPO_URL = "https://github.com/MaximumADHD/Roblox-FFlag-Tracker"
TARGET_FILE = "PCDesktopClient.json"
DAYS = 2

# --- Paths ---
SCRIPT_DIR = Path(__file__).resolve().parent
WORKSPACE = Path(os.getenv("GITHUB_WORKSPACE", SCRIPT_DIR)).resolve()
OUTPUT_DIR = WORKSPACE / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_MD = OUTPUT_DIR / "FFlag_Report.md"
OUTPUT_HTML = OUTPUT_DIR / "FFlag_Report.html"

print(f"[DEBUG] Script directory: {SCRIPT_DIR}")
print(f"[DEBUG] Workspace: {WORKSPACE}")
print(f"[DEBUG] Output directory: {OUTPUT_DIR}")


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


def check_git():
    try:
        subprocess.check_output(["git", "--version"], stderr=subprocess.STDOUT)
    except Exception:
        print("[ERROR] Git is not installed or not in PATH.")
        print("Download Git: https://git-scm.com/downloads")
        sys.exit(1)


def ensure_repo():
    if not TRACKER_DIR.exists():
        print("[INFO] Cloning fresh repo...")
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


def update_landing_page(date_str, added, removed):
    """Updates index.html placeholders with the latest run stats."""
    index_file = OUTPUT_DIR / "index.html"
    if not index_file.exists():
        print("[WARN] Landing page not found, skipping update.")
        return
    html = index_file.read_text(encoding="utf-8")
    html = re.sub(r'document\.getElementById\("last-run"\).*?;',
                  f'document.getElementById("last-run").textContent = "{date_str}";', html)
    html = re.sub(r'document\.getElementById\("flags-added"\).*?;',
                  f'document.getElementById("flags-added").textContent = "{added}";', html)
    html = re.sub(r'document\.getElementById\("flags-removed"\).*?;',
                  f'document.getElementById("flags-removed").textContent = "{removed}";', html)
    index_file.write_text(html, encoding="utf-8")
    print(f"[DEBUG] Landing page updated with {added} added / {removed} removed.")


def export_reports(report, summary_counts):
    # --- Update landing page ---
    date_str = datetime.now().strftime("%Y-%m-%d")
    added = sum(v for (c, a), v in summary_counts.items() if a == "Added")
    removed = sum(v for (c, a), v in summary_counts.items() if a == "Removed")
    update_landing_page(date_str, added, removed)

    md = [f"# Roblox Client FFlag Intel Report ({DAYS} Days)\n"]
    html = [
        "<html><head><title>Roblox FFlag Intel Report</title>",
        "<style>body{font-family:Arial;} .added{color:green;} .removed{color:red;} code{background:#eee;}</style>",
        "</head><body>",
        f"<h1>Roblox Client FFlag Intel Report ({DAYS} Days)</h1>",
        f"<p>Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>"
    ]

    # --- Summary Table ---
    md.append("## Summary of Changes\n")
    md.append("| Category | Added | Removed | Total |")
    md.append("|----------|-------|---------|-------|")
    html.append("<h2>Summary of Changes</h2>")
    html.append("<table border='1' cellpadding='5'><tr><th>Category</th><th>Added</th><th>Removed</th><th>Total</th></tr>")

    for cat in CATEGORIES.keys():
        added = summary_counts.get((cat, "Added"), 0)
        removed = summary_counts.get((cat, "Removed"), 0)
        total = added + removed
        md.append(f"| {cat} | {added} | {removed} | {total} |")
        html.append(f"<tr><td>{cat}</td><td style='color:green;'>{added}</td><td style='color:red;'>{removed}</td><td>{total}</td></tr>")

    md.append("")
    html.append("</table>")

    # --- Detailed Changes ---
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

    print(f"[DEBUG] Writing Markdown report: {OUTPUT_MD}")
    OUTPUT_MD.write_text("\n".join(md), encoding="utf-8")

    print(f"[DEBUG] Writing HTML report: {OUTPUT_HTML}")
    OUTPUT_HTML.write_text("\n".join(html), encoding="utf-8")


def main():
    print("=" * 60)
    print(" Roblox Client FFlag Intel Tracker ")
    print("=" * 60)
    check_git()
    ensure_repo()
    commits = get_commits()
    if not commits:
        print(f"[INFO] No changes in the past {DAYS} days.")
        OUTPUT_MD.write_text("# No FFlag changes detected.\n", encoding="utf-8")
        OUTPUT_HTML.write_text("<html><body><h1>No FFlag changes detected.</h1></body></html>", encoding="utf-8")
        return
    report, summary_counts = build_report(commits)
    export_reports(report, summary_counts)
    print("[SUCCESS] Reports generated!")
    print(f"- Markdown: {OUTPUT_MD}")
    print(f"- HTML:     {OUTPUT_HTML}")
    print("Open the HTML report in your browser for a clean view.")


if __name__ == "__main__":
    main()
