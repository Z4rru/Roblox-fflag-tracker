#!/usr/bin/env python3
import os
import subprocess
import datetime
import json
import html
from pathlib import Path
from zoneinfo import ZoneInfo
import asyncio
import logging
import time
try:
    import openai
except ImportError:
    openai = None  # Graceful degrade if not available

# ===============================
# Settings and Paths
# ===============================
SCRIPT_DIR = Path(__file__).resolve().parent
WORKSPACE = Path(os.getenv("GITHUB_WORKSPACE", str(SCRIPT_DIR))).resolve()
OUTPUT_DIR = WORKSPACE / "output"
OUTPUT_MD = OUTPUT_DIR / "FFlag_Report.md"
OUTPUT_HTML = OUTPUT_DIR / "FFlag_Report.html"
OUTPUT_JSON = OUTPUT_DIR / "FFlag_Report.json"
CACHE_FILE = OUTPUT_DIR / "fflag_cache.json"
DIFF_CACHE_FILE = OUTPUT_DIR / "diff_cache.json"
HISTORY_FILE = OUTPUT_DIR / "history.json"

REPO_URL = "https://github.com/MaximumADHD/Roblox-FFlag-Tracker"
LOCAL_CLONE = WORKSPACE / "Roblox-FFlag-Tracker"
TARGET_FILE = "PCDesktopClient.json"

DAYS = 365
HISTORY_DAYS = 90
AI_BATCH_SIZE = 20  # Increased for better scalability
MAX_RETRIES = 3
DEBUG = True

# ===============================
# Logging Utility
# ===============================
logging.basicConfig(level=logging.INFO if not DEBUG else logging.DEBUG, format="[%(levelname)s] %(message)s (%(asctime)s)")
log = logging.getLogger(__name__)

# ===============================
# OpenAI API Key Management
# ===============================
keys_raw = os.getenv("OPENAI_API_KEYS", "")
keys = [k.strip() for k in keys_raw.split(",") if k.strip()]
if not keys:
    log.warning("⚠ No OpenAI API keys found. AI enrichment will be skipped.")

key_index = -1
def get_next_api_key():
    global key_index
    if not keys:
        return None
    key_index = (key_index + 1) % len(keys)
    key = keys[key_index]
    display_key = f"{key[:4]}...{key[-4:]}" if len(key) > 8 else "****"
    log.debug(f"Using OpenAI API key #{key_index+1} ({display_key})")
    return key

# ===============================
# FFlags Categories
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
    "Body": ["Body", "Ragdoll", "Torso", "Limb", "Character"],
    "Other": []
}

# ===============================
# Utility Functions
# ===============================
def run_cmd(cmd: str, cwd: Path | None = None, timeout: int = 120) -> str:
    try:
        result = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True, timeout=timeout)
        if result.returncode != 0:
            log.error(f"Command failed (return code {result.returncode}): {cmd}")
            log.error(result.stderr.strip())
            raise subprocess.CalledProcessError(result.returncode, cmd, output=result.stdout, stderr=result.stderr)
        return result.stdout.strip()
    except subprocess.TimeoutExpired:
        log.error(f"Command timed out after {timeout} seconds: {cmd}")
        raise
    except Exception as e:
        log.error(f"Cmd error: {e}")
        raise

def categorize_flag(flag_name: str) -> str:
    lower = flag_name.lower()
    for cat, keywords in CATEGORIES.items():
        if any(k.lower() in lower for k in keywords):
            return cat
    return "Other"

def escape_flag(flag_name: str) -> str:
    return html.escape(flag_name)

# ===============================
# Repository Management
# ===============================
def ensure_repo() -> None:
    try:
        if LOCAL_CLONE.exists():
            log.info("Updating existing repository...")
            run_cmd("git fetch --all", cwd=LOCAL_CLONE, timeout=300)
            run_cmd("git fetch --unshallow", cwd=LOCAL_CLONE, timeout=300)  # Increased timeout for unshallow
            run_cmd("git reset --hard origin/main", cwd=LOCAL_CLONE)
        else:
            LOCAL_CLONE.parent.mkdir(parents=True, exist_ok=True)  # Ensure nested paths
            success = False
            for attempt in range(1, MAX_RETRIES + 1):
                log.info(f"Cloning repository (attempt {attempt}/{MAX_RETRIES})...")
                try:
                    run_cmd(f"git clone {REPO_URL} {LOCAL_CLONE.name}", cwd=LOCAL_CLONE.parent, timeout=600)  # High timeout for clone
                    success = True
                    break
                except Exception as e:
                    log.warning(f"Clone attempt {attempt} failed: {e}")
                    time.sleep(5)  # Brief backoff
            if not success:
                raise RuntimeError("Failed to clone repository after maximum retries.")
            log.info("Clone successful.")
    except Exception as e:
        log.error(f"Repo ensure failed: {e}")
        raise

def get_commits() -> list[str]:
    since = (datetime.datetime.now() - datetime.timedelta(days=DAYS)).strftime("%Y-%m-%d")
    commits = run_cmd(f"git log --since='{since}' --pretty=format:%H -- {TARGET_FILE}", cwd=LOCAL_CLONE)
    return commits.splitlines() if commits else []

# ===============================
# Diff Utilities
# ===============================
def build_diff_for_commit_old(commit_hash: str) -> tuple[str, list[str], list[str]]:
    header = run_cmd(f"git show --no-patch --pretty=format:'%h - %ci - %s' {commit_hash}", cwd=LOCAL_CLONE)
    diff = run_cmd(f"git show {commit_hash} -- {TARGET_FILE}", cwd=LOCAL_CLONE)
    added, removed = [], []
    for line in diff.splitlines():
        if line.startswith("+") and not line.startswith("+++"):
            added.append(line[1:].strip())
        elif line.startswith("-") and not line.startswith("---"):
            removed.append(line[1:].strip())
    return header, added, removed

def build_diff_for_commit(commit_hash: str, diff_cache: dict) -> tuple[str, list[str], list[str]]:
    if commit_hash in diff_cache:
        cached = diff_cache[commit_hash]
        return cached['header'], cached['added'], cached['removed']
    header = run_cmd(f"git show --no-patch --pretty=format:'%h - %ci - %s' {commit_hash}", cwd=LOCAL_CLONE)
    curr_content = run_cmd(f"git show {commit_hash}:{TARGET_FILE}", cwd=LOCAL_CLONE)
    try:
        prev_content = run_cmd(f"git show {commit_hash}~1:{TARGET_FILE}", cwd=LOCAL_CLONE)
        prev_json = json.loads(prev_content)
    except Exception:
        prev_json = {}
    try:
        curr_json = json.loads(curr_content)
    except json.JSONDecodeError:
        header, added, removed = build_diff_for_commit_old(commit_hash)
        diff_cache[commit_hash] = {'header': header, 'added': added, 'removed': removed}
        return header, added, removed
    added = [k for k in curr_json if k not in prev_json or curr_json[k] != prev_json.get(k)]
    removed = [k for k in prev_json if k not in curr_json]
    diff_cache[commit_hash] = {'header': header, 'added': added, 'removed': removed}
    return header, added, removed

def build_report(commits: list[str], diff_cache: dict) -> tuple[list, dict]:
    report, summary = [], {}
    for c in commits:
        header, added_flags, removed_flags = build_diff_for_commit(c, diff_cache)
        changes = []
        for flag in added_flags:
            cat = categorize_flag(flag)
            changes.append(("Added", cat, flag))
            summary[(cat, "Added")] = summary.get((cat, "Added"), 0) + 1
        for flag in removed_flags:
            cat = categorize_flag(flag)
            changes.append(("Removed", cat, flag))
            summary[(cat, "Removed")] = summary.get((cat, "Removed"), 0) + 1
        if changes:
            report.append((header, changes))
    return report, summary

# ===============================
# History Management
# ===============================
def update_history(added: int, removed: int, last_run: str) -> None:
    if HISTORY_FILE.exists():
        try:
            history = json.loads(HISTORY_FILE.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            log.warning("Corrupted history file. Starting new history.")
            history = []
    else:
        history = []
    history.append({"date": last_run, "added": added, "removed": removed})
    history = history[-HISTORY_DAYS:]
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    HISTORY_FILE.write_text(json.dumps(history, indent=2), encoding="utf-8")

# ===============================
# AI Enrichment
# ===============================
FLAG_INFO = json.loads(CACHE_FILE.read_text(encoding="utf-8")) if CACHE_FILE.exists() else {}

async def fetch_ai_batch(batch: list[str]) -> None:
    if not keys or not openai:
        for f in batch:
            FLAG_INFO[f] = {"mechanism": "Unknown", "purpose": "Unknown"}
        return
    prompt = "Explain the Roblox FFlags below. For each, provide Mechanism and Purpose in JSON format.\n" + json.dumps(batch)
    for attempt in range(MAX_RETRIES):
        try:
            openai.api_key = get_next_api_key()
            response = await openai.chat.completions.create(
                model="gpt-5-mini",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.3
            )
            content = response.choices[0].message.content.strip()
            try:
                data = json.loads(content)
                for f in batch:
                    info = data.get(f, {})
                    FLAG_INFO[f] = {"mechanism": info.get("mechanism", "Unknown"), "purpose": info.get("purpose", "Unknown")}
            except json.JSONDecodeError:
                for line in content.splitlines():
                    if ":" in line:
                        f, rest = line.split(":", 1)
                        f = f.strip()
                        if f in batch:
                            FLAG_INFO[f] = {"mechanism": rest.strip(), "purpose": "N/A"}
            break
        except openai.RateLimitError:
            await asyncio.sleep(2 ** attempt)
        except Exception as e:
            log.error(f"AI batch failed (attempt {attempt+1}): {e}")
    else:
        for f in batch:
            FLAG_INFO[f] = {"mechanism": "Unknown", "purpose": "Unknown"}
    CACHE_FILE.write_text(json.dumps(FLAG_INFO, indent=2), encoding="utf-8")

async def generate_flag_info_batch(flags: list[str]) -> None:
    new_flags = [f for f in flags if f not in FLAG_INFO]
    if not new_flags:
        return
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    tasks = [fetch_ai_batch(new_flags[i:i + AI_BATCH_SIZE]) for i in range(0, len(new_flags), AI_BATCH_SIZE)]
    if tasks:
        await asyncio.gather(*tasks)

def generate_flag_info(flag: str) -> dict:
    return FLAG_INFO.get(flag, {"mechanism": "Unknown", "purpose": "Unknown"})

# ===============================
# Report Export (Enhanced with Grouping for Collapsibles and History Summary)
# ===============================
def export_reports(report: list, summary: dict) -> tuple[int, int, str, str]:
    last_run = datetime.datetime.now(ZoneInfo("Asia/Manila")).strftime("%Y-%m-%d %I:%M:%S %p %Z")
    added_total = sum(v for (cat, typ), v in summary.items() if typ == "Added")
    removed_total = sum(v for (cat, typ), v in summary.items() if typ == "Removed")
    
    # Load history.json to compute historical aggregates
    if HISTORY_FILE.exists():
        try:
            history = json.loads(HISTORY_FILE.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            log.warning("Corrupted history file. Using empty history for report.")
            history = []
    else:
        history = []
    total_historical_added = sum(entry['added'] for entry in history)
    total_historical_removed = sum(entry['removed'] for entry in history)
    
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    # Markdown with Summary and History Chart Counts
    md = [f"# Roblox Client FFlag Intel Report ({DAYS} Days)\n"]
    md.append(f"- **Last Run:** {last_run}")
    md.append(f"- **Flags Added:** {added_total}")
    md.append(f"- **Flags Removed:** {removed_total}\n")
    md.append("## Summary\n| Category | Added | Removed | Total |\n|---|---|---|---|")
    for cat in CATEGORIES:
        a = summary.get((cat, "Added"), 0)
        r = summary.get((cat, "Removed"), 0)
        md.append(f"| {cat} | {a} | {r} | {a+r} |")
    md.append("\n## History Summary Chart Counts\n")  # New history section in markdown
    md.append(f"- **Total Historical Added:** {total_historical_added}")
    md.append(f"- **Total Historical Removed:** {total_historical_removed}")
    if len(history) == 1:
        md.append("- **Note:** No prior history available yet")
    if not report:
        md.append(f"\n## No Recent Changes\nNo flag changes in the last {DAYS} days.")
    else:
        for header, changes in report:
            md.append(f"\n## {header}")
            grouped = {}
            for typ, cat, flag in changes:
                grouped.setdefault((typ, cat), []).append(flag)
            for (typ, cat), flags in grouped.items():
                md.append(f"**{typ} in {cat}:**")
                for f in flags:
                    info = generate_flag_info(f)
                    md.append(f"- {f} | Mechanism: {info['mechanism']} | Purpose: {info['purpose']}")
    OUTPUT_MD.write_text("\n".join(md), encoding="utf-8")
    
    # HTML with <h3><ul> for Collapsibles
    html_lines = ["<html><body><h1>Roblox FFlag Report</h1>"]
    if not report:
        html_lines.append(f"<h2>No Recent Changes</h2><p>No flag changes in the last {DAYS} days.</p>")
    else:
        for header, changes in report:
            html_lines.append(f"<h2>{header}</h2>")
            grouped = {}
            for typ, cat, flag in changes:
                grouped.setdefault((typ, cat), []).append(flag)
            for (typ, cat), flags in grouped.items():
                html_lines.append(f"<h3>{typ} in {cat}</h3><ul>")
                for f in flags:
                    info = generate_flag_info(f)
                    html_lines.append(f"<li>{escape_flag(f)} - Mechanism: {info['mechanism']} - Purpose: {info['purpose']}</li>")
                html_lines.append("</ul>")
    html_lines.append("</body></html>")
    OUTPUT_HTML.write_text("\n".join(html_lines), encoding="utf-8")
    
    # JSON for responsive landing page, now with historical counts
    json_data = {
        "last_run": last_run,
        "added_total": added_total,
        "removed_total": removed_total,
        "total_historical_added": total_historical_added,  # New fields
        "total_historical_removed": total_historical_removed,
        "summary": {cat: {"added": summary.get((cat, "Added"), 0), "removed": summary.get((cat, "Removed"), 0)} for cat in CATEGORIES},
        "report": [],
        "days": DAYS
    }
    for header, changes in report:
        grouped = {}
        for typ, cat, flag in changes:
            grouped.setdefault(f"{typ}_{cat}", []).append({
                "name": flag,
                "mechanism": generate_flag_info(flag)['mechanism'],
                "purpose": generate_flag_info(flag)['purpose']
            })
        json_data["report"].append({
            "header": header,
            "grouped": grouped
        })
    OUTPUT_JSON.write_text(json.dumps(json_data, indent=2), encoding="utf-8")
    
    log.info(f"Reports generated: {OUTPUT_MD}, {OUTPUT_HTML}, {OUTPUT_JSON}")
    return added_total, removed_total, last_run, "report_done"

# ===============================
# Landing Page (Particles + Collapsibles JS)
# ===============================
def ensure_landing_page(added: int, removed: int, last_run: str) -> None:
    index_html = OUTPUT_DIR / "index.html"
    if not HISTORY_FILE.exists():
        HISTORY_FILE.write_text("[]", encoding="utf-8")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Roblox FFlag Tracker</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
<style>
:root { 
  --primary-green: #34d399;
  --primary-red: #f87171;
  --historical-green: #10b981;
  --historical-red: #ef4444;
  --bg-opacity: 0.15;
  --text-color: #fff;
}
body { 
  font-family:'Inter',sans-serif;
  margin:0;
  background: linear-gradient(135deg,#4f46e5,#3b82f6,#06b6d4,#14b8a6);
  background-size: 400% 400%;
  animation: gradientBG 15s ease infinite;
  color: var(--text-color);
  overflow-x: hidden;
}
@keyframes gradientBG { 
  0% {background-position:0% 50%;}
  50% {background-position:100% 50%;}
  100% {background-position:0% 50%;}
}
header { text-align:center; padding:60px 20px; text-shadow:0 0 12px rgba(0,0,0,0.3); }
header h1 { font-size:3rem; font-weight:700; }
.stats { 
  display:flex;
  justify-content:center;
  gap:30px;
  flex-wrap:wrap;
  max-width:1200px;
  margin:-40px auto 40px;
  position:relative; z-index:2;
}
.badge { 
  flex:1; min-width:220px;
  text-align:center;
  padding:25px;
  border-radius:16px;
  font-weight:700;
  backdrop-filter:blur(10px);
  background:rgba(255,255,255,var(--bg-opacity));
  box-shadow:0 10px 30px rgba(0,0,0,0.3);
  transition: transform 0.3s ease, box-shadow 0.3s ease, border 0.3s ease;
}
.badge:hover { 
  transform:translateY(-8px);
  box-shadow:0 14px 40px rgba(0,0,0,0.4);
  border:2px solid var(--primary-green);
}
.added { border-left:6px solid var(--primary-green); }
.removed { border-left:6px solid var(--primary-red); }
.historical-added { border-left:6px solid var(--historical-green); }
.historical-removed { border-left:6px solid var(--historical-red); }
.last-run { text-align:center; margin:20px 0; font-style:italic; color:#eee; }
section { max-width:1200px; margin:0 auto; padding:20px; }
.report-container { 
  background: rgba(255,255,255,var(--bg-opacity));
  backdrop-filter: blur(10px);
  border-radius:16px;
  box-shadow:0 12px 36px rgba(0,0,0,0.25);
  padding:15px;
  position: relative;
}
#loadingSpinner { 
  position: absolute;
  top: 50%; left: 50%;
  transform: translate(-50%, -50%);
  border: 4px solid rgba(255,255,255,0.3);
  border-top: 4px solid var(--primary-green);
  border-radius: 50%;
  width: 40px; height: 40px;
  animation: spin 1s linear infinite;
}
@keyframes spin { 
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
#reportContent { width:100%; min-height:75vh; border-radius:12px; }
canvas#trendChart { display:block; max-width:850px; margin:40px auto; border-radius:12px; }
input#searchInput { 
  width:90%; padding:12px; margin:20px auto; display:block;
  border-radius:12px; border:1px solid rgba(255,255,255,0.3);
  background:rgba(0,0,0,0.2); color: var(--text-color); font-size:1rem;
  backdrop-filter:blur(5px);
}
footer { text-align:center; margin-top:60px; padding:25px; font-size:0.9rem; color:#eee; }
canvas#particleCanvas { 
  position: fixed;
  top:0; left:0; width:100%; height:100%;
  pointer-events:none;
  z-index:0;
}
table { 
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 40px;
}
th, td { 
  border: 1px solid rgba(255,255,255,0.3);
  padding: 12px;
  text-align: left;
}
th { 
  background: rgba(0,0,0,0.2);
}
</style>
</head>
<body>
<canvas id="particleCanvas"></canvas>
<header>
  <h1>Roblox Client FFlag Tracker</h1>
</header>

<section>
  <div class="stats">
    <div class="badge added">✅ Added: <span id="flags-added">0</span></div>
    <div class="badge removed">❌ Removed: <span id="flags-removed">0</span></div>
    <div class="badge historical-added">📈 Historical Added: <span id="historical-added">0</span></div>
    <div class="badge historical-removed">📉 Historical Removed: <span id="historical-removed">0</span></div>
  </div>

  <p class="last-run">Last Run: <span id="last-run"></span></p>

  <input type="text" id="searchInput" placeholder="Search flags..." aria-label="Search flags">

  <h2>Summary</h2>
  <table id="summaryTable"></table>

  <h2>📊 Latest Full Report</h2>
  <div class="report-container">
    <div id="loadingSpinner"></div>
    <div id="reportContent" aria-label="Latest report"></div>
  </div>

  <canvas id="trendChart" aria-label="Trend chart"></canvas>
</section>

<footer>Built with ❤️ by FFlag Tracker • Updated automatically</footer>

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
// Particle animation - reduced particle count and added visibility check
const canvas = document.getElementById('particleCanvas');
const ctx = canvas.getContext('2d');
let resizeTimeout;
let animationId;
let particles = [];
function resizeCanvas() {
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;
}

function generateParticles() {
  particles = Array.from({ length: 30 }, () => ({
    x: Math.random() * canvas.width,
    y: Math.random() * canvas.height,
    r: Math.random() * 2 + 1,
    dx: (Math.random() - 0.5) / 2,
    dy: (Math.random() - 0.5) / 2,
    color: `rgba(${Math.floor(Math.random() * 50 + 200)}, 255, 255, 0.15)`,
  }));
}

function animateParticles() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  particles.forEach(p => {
    p.x += p.dx;
    p.y += p.dy;
    if (p.x < 0 || p.x > canvas.width) p.dx *= -1;
    if (p.y < 0 || p.y > canvas.height) p.dy *= -1;
    ctx.beginPath();
    ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
    ctx.fillStyle = p.color;
    ctx.fill();
  });
  animationId = requestAnimationFrame(animateParticles);
}

function stopAnimation() {
  cancelAnimationFrame(animationId);
}

resizeCanvas();
generateParticles();
animateParticles();

window.addEventListener('resize', () => {
  clearTimeout(resizeTimeout);
  resizeTimeout = setTimeout(resizeCanvas, 200);
});

document.addEventListener('visibilitychange', () => {
  if (document.hidden) stopAnimation();
  else animateParticles();
});

// Trend chart using Chart.js with limited data points
fetch("history.json").then(r => r.json()).then(data => {
  if (data.length === 0) {
    document.getElementById("trendChart").parentNode.innerHTML = '<p>No history data yet.</p>';
    return;
  }
  const ctx = document.getElementById("trendChart").getContext("2d");
  new Chart(ctx, {
    type: 'line',
    data: {
      labels: data.map(d => d.date),
      datasets: [
        {
          label: 'Added',
          data: data.map(d => d.added),
          borderColor: '#34d399',
          backgroundColor: 'rgba(52,211,153,0.2)',
          fill: true,
          tension: 0.4
        },
        {
          label: 'Removed',
          data: data.map(d => d.removed),
          borderColor: '#f87171',
          backgroundColor: 'rgba(248,113,113,0.2)',
          fill: true,
          tension: 0.4
        }
      ]
    },
    options: {
      responsive: true,
      plugins: {
        legend: {
          position: 'top'
        }
      },
      interaction: {
        mode: 'nearest',
        axis: 'x',
        intersect: false
      }
    }
  });
}).catch(error => {
  console.error('Error loading history:', error);
  document.getElementById("trendChart").parentNode.innerHTML = '<p>Error loading history data.</p>';
});

// Lazy Loading of report data
const reportContent = document.getElementById('reportContent');
const loadingSpinner = document.getElementById('loadingSpinner');
let currentPage = 0;
const itemsPerPage = 10;

function loadReportPage(data, page = 0) {
  const startIndex = page * itemsPerPage;
  const endIndex = startIndex + itemsPerPage;
  const reportPage = data.slice(startIndex, endIndex);
  
  reportPage.forEach(commit => {
    const h2 = document.createElement('h2');
    h2.textContent = commit.header;
    reportContent.appendChild(h2);

    Object.entries(commit.grouped).forEach(([groupKey, flags]) => {
      const [typ, cat] = groupKey.split('_');
      const h3 = document.createElement('h3');
      h3.textContent = `${typ} in ${cat}`;
      h3.style.cursor = 'pointer';
      h3.setAttribute('aria-expanded', 'true');
      reportContent.appendChild(h3);

      const ul = document.createElement('ul');
      ul.style.display = 'block';
      flags.forEach(f => {
        const li = document.createElement('li');
        li.textContent = `${f.name} - Mechanism: ${f.mechanism} - Purpose: ${f.purpose}`;
        ul.appendChild(li);
      });
      reportContent.appendChild(ul);
    });
  });
}

fetch('FFlag_Report.json')
  .then(response => response.json())
  .then(data => {
    document.getElementById('flags-added').textContent = data.added_total;
    document.getElementById('flags-removed').textContent = data.removed_total;
    document.getElementById('historical-added').textContent = data.total_historical_added;
    document.getElementById('historical-removed').textContent = data.total_historical_removed;
    document.getElementById('last-run').textContent = data.last_run;

    // Populate summary table
    const summaryTable = document.getElementById('summaryTable');
    let tableHtml = '<thead><tr><th>Category</th><th>Added</th><th>Removed</th></tr></thead><tbody>';
    for (let cat in data.summary) {
      const s = data.summary[cat];
      tableHtml += `<tr><td>${cat}</td><td>${s.added}</td><td>${s.removed}</td></tr>`;
    }
    tableHtml += '</tbody>';
    summaryTable.innerHTML = tableHtml;

    if (data.report.length === 0) {
      reportContent.innerHTML = `<p>No recent flag changes in the last ${data.days} days.</p>`;
    } else {
      loadReportPage(data.report, currentPage);
      const maxPages = Math.ceil(data.report.length / itemsPerPage);
      if (1 < maxPages) {
        const sentinel = document.createElement('div');
        sentinel.id = 'sentinel';
        reportContent.appendChild(sentinel);
        const observer = new IntersectionObserver(entries => {
          if (entries[0].isIntersecting) {
            const nextPage = currentPage + 1;
            if (nextPage < maxPages) {
              currentPage = nextPage;
              loadReportPage(data.report, currentPage);
              const stillMore = currentPage + 1 < maxPages;
              if (stillMore) {
                reportContent.appendChild(sentinel);
              } else {
                observer.unobserve(sentinel);
                sentinel.remove();
              }
            }
          }
        }, { threshold: 0 });
        observer.observe(sentinel);
      }
    }
    loadingSpinner.style.display = 'none';

    // Event delegation for collapsibles
    reportContent.addEventListener('click', e => {
      if (e.target.tagName === 'H3') {
        const ul = e.target.nextElementSibling;
        if (ul && ul.tagName === 'UL') {
          const expanded = ul.style.display !== 'none';
          ul.style.display = expanded ? 'none' : 'block';
          e.target.setAttribute('aria-expanded', !expanded);
        }
      }
    });
  })
  .catch(error => {
    console.error('Error loading report:', error);
    loadingSpinner.style.display = 'none';
    reportContent.innerHTML = '<p>Error loading report.</p>';
  });

// Search with Debounced Input for Filtering
document.getElementById('searchInput').addEventListener('input', function() { 
  clearTimeout(window.searchTimeout);
  window.searchTimeout = setTimeout(() => filterFlags(this.value), 300);
});
function filterFlags(query) {
  const searchQuery = query.toLowerCase();
  if (!searchQuery) {
    // Show all
    reportContent.querySelectorAll('h2, h3, ul, li').forEach(el => {
      el.style.display = '';
      if (el.tagName === 'H3') {
        el.setAttribute('aria-expanded', 'true');
      }
      if (el.tagName === 'UL') {
        el.style.display = 'block';
      }
    });
    return;
  }

  // Loop through commits (h2)
  const commits = reportContent.querySelectorAll('h2');
  commits.forEach(h2 => {
    let commitVisible = false;
    let sibling = h2.nextElementSibling;
    while (sibling && sibling.tagName !== 'H2') {
      if (sibling.tagName === 'H3') {
        const catText = sibling.textContent.toLowerCase();
        const ul = sibling.nextElementSibling;
        if (ul && ul.tagName === 'UL') {
          let groupVisible = false;
          if (catText.includes(searchQuery)) {
            // Match category, show all in group
            sibling.style.display = '';
            ul.style.display = 'block';
            sibling.setAttribute('aria-expanded', 'true');
            ul.querySelectorAll('li').forEach(li => li.style.display = '');
            groupVisible = true;
          } else {
            // Check each li
            ul.querySelectorAll('li').forEach(li => {
              if (li.textContent.toLowerCase().includes(searchQuery)) {
                li.style.display = '';
                groupVisible = true;
              } else {
                li.style.display = 'none';
              }
            });
            if (groupVisible) {
              sibling.style.display = '';
              ul.style.display = 'block';
              sibling.setAttribute('aria-expanded', 'true');
            } else {
              sibling.style.display = 'none';
              ul.style.display = 'none';
            }
          }
          if (groupVisible) commitVisible = true;
        }
      }
      sibling = sibling.nextElementSibling;
    }
    h2.style.display = commitVisible ? '' : 'none';
  });
}
</script>
</body>
</html>
"""
    index_html.write_text(html_content, encoding="utf-8")
    log.info(f"Landing page written: {index_html}")

# ===============================
# Main Execution
# ===============================
def main() -> None:
    try:
        log.info("=" * 80)
        log.info("Roblox Client FFlag Tracker (Integrated Categories + Interpolation)")
        log.info("=" * 80)
        ensure_repo()
        commits = get_commits()
        diff_cache = json.loads(DIFF_CACHE_FILE.read_text(encoding="utf-8")) if DIFF_CACHE_FILE.exists() else {}
        if not commits:
            log.warning(f"No commits in the last {DAYS} days.")
            report = []
            summary = {}
        else:
            report, summary = build_report(commits, diff_cache)
        DIFF_CACHE_FILE.write_text(json.dumps(diff_cache, indent=2), encoding="utf-8")
        all_flags = [f for _, changes in report for _, _, f in changes]
        if all_flags:
            asyncio.run(generate_flag_info_batch(all_flags))
        last_run = datetime.datetime.now(ZoneInfo("Asia/Manila")).strftime("%Y-%m-%d %I:%M:%S %p %Z")
        added = sum(v for (cat, typ), v in summary.items() if typ == "Added")
        removed = sum(v for (cat, typ), v in summary.items() if typ == "Removed")
        update_history(added, removed, last_run)
        export_reports(report, summary)
        ensure_landing_page(added, removed, last_run)
        log.info("All done! Reports and dashboard ready.")
    except Exception as e:
        log.error(f"Main execution failed: {e}")

if __name__ == "__main__":
    main()
