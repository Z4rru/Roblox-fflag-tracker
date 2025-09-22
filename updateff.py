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
CACHE_FILE = OUTPUT_DIR / "fflag_cache.json"

REPO_URL = "https://github.com/MaximumADHD/Roblox-FFlag-Tracker"
LOCAL_CLONE = WORKSPACE / "Roblox-FFlag-Tracker"
TARGET_FILE = "PCDesktopClient.json"

DAYS: int = 8
HISTORY_DAYS: int = 90
AI_BATCH_SIZE: int = 10
MAX_RETRIES: int = 3
DEBUG: bool = True

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
    keys = []

if keys:
    key_index = -1
    def get_next_api_key() -> str:
        global key_index
        key_index = (key_index + 1) % len(keys)
        key = keys[key_index]
        display_key = f"{key[:4]}...{key[-4:]}" if len(key) > 8 else "****"
        log.debug(f"Using OpenAI API key #{key_index+1} ({display_key})")
        return key
else:
    def get_next_api_key() -> None:
        return None

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
def run_cmd(cmd: str, cwd: Path | None = None) -> str:
    try:
        result = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True, timeout=30)
        if result.returncode != 0:
            log.error(f"Command failed: {cmd}")
            log.error(result.stderr.strip())
        return result.stdout.strip()
    except Exception as e:
        log.error(f"Cmd error: {e}")
        return ""

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
            run_cmd("git fetch --all", cwd=LOCAL_CLONE)
            run_cmd("git reset --hard origin/main", cwd=LOCAL_CLONE)
        else:
            log.info("Cloning repository for the first time...")
            run_cmd(f"git clone --depth=1 {REPO_URL} {LOCAL_CLONE}")
    except Exception as e:
        log.error(f"Repo ensure failed: {e}")

def get_commits() -> list[str]:
    since = (datetime.datetime.now() - datetime.timedelta(days=DAYS)).strftime("%Y-%m-%d")
    commits = run_cmd(f"git log --since='{since}' --pretty=format:'%H' -- {TARGET_FILE}", cwd=LOCAL_CLONE)
    return commits.splitlines() if commits else []

def build_diff_for_commit(commit_hash: str) -> tuple[str, list[str], list[str]]:
    header = run_cmd(f"git show --no-patch --pretty=format:'%h - %ci - %s' {commit_hash}", cwd=LOCAL_CLONE)
    diff = run_cmd(f"git show {commit_hash} -- {TARGET_FILE}", cwd=LOCAL_CLONE)
    added, removed = [], []
    for line in diff.splitlines():
        if line.startswith("+") and not line.startswith("+++"):
            added.append(line[1:].strip())
        elif line.startswith("-") and not line.startswith("---"):
            removed.append(line[1:].strip())
    return header, added, removed

def build_report(commits: list[str]) -> tuple[list, dict]:
    report, summary = [], {}
    for c in commits:
        header, added_flags, removed_flags = build_diff_for_commit(c)
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
    hist_file = OUTPUT_DIR / "history.json"
    history = json.loads(hist_file.read_text(encoding="utf-8")) if hist_file.exists() else []
    history.append({"date": last_run, "added": added, "removed": removed})
    history = history[-HISTORY_DAYS:]
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    hist_file.write_text(json.dumps(history, indent=2), encoding="utf-8")

# ===============================
# AI Enrichment
# ===============================
FLAG_INFO: dict = json.loads(CACHE_FILE.read_text(encoding="utf-8")) if CACHE_FILE.exists() else {}

async def fetch_ai_batch(batch: list[str]) -> None:
    if not keys or not openai:
        for f in batch:
            FLAG_INFO[f] = {"mechanism": "Unknown", "purpose": "Unknown"}
        return
    prompt = "Explain the Roblox FFlags in detail:\n" + "".join([f"- {f}\n" for f in batch])
    prompt += "\nProvide Mechanism and Purpose, 1-2 sentences each."
    backoff = 1
    while True:
        try:
            openai.api_key = get_next_api_key()
            response = await openai.chat.completions.create(
                model="gpt-5-mini",  # Updated for 2025
                messages=[{"role": "user", "content": prompt}],
                temperature=0.3
            )
            text = response.choices[0].message.content.strip().split("\n")
            for line in text:
                if ":" in line:
                    f, rest = line.split(":", 1)
                    f = f.strip()
                    if f in batch:
                        FLAG_INFO[f] = {"mechanism": rest.strip(), "purpose": "N/A"}
            break
        except openai.RateLimitError:
            log.warning(f"Rate limit reached. Retrying in {backoff}s.")
            await asyncio.sleep(backoff)
            backoff *= 2
        except Exception as e:
            log.error(f"AI batch failed: {e}")
            for f in batch:
                FLAG_INFO[f] = {"mechanism": "Unknown", "purpose": "Unknown"}
            break

async def generate_flag_info_batch(flags: list[str]) -> None:
    new_flags = [f for f in flags if f not in FLAG_INFO]
    if not new_flags:
        return
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    tasks = [fetch_ai_batch(new_flags[i:i + AI_BATCH_SIZE]) for i in range(0, len(new_flags), AI_BATCH_SIZE)]
    await asyncio.gather(*tasks)
    CACHE_FILE.write_text(json.dumps(FLAG_INFO, indent=2), encoding="utf-8")

def generate_flag_info(flag: str) -> dict:
    return FLAG_INFO.get(flag, {"mechanism": "Unknown", "purpose": "Unknown"})

# ===============================
# Report Generation (Markdown + HTML)
# ===============================
def export_reports(report: list, summary: dict) -> tuple[int, int, str, str]:
    last_run = datetime.datetime.now(ZoneInfo("Asia/Manila")).strftime("%Y-%m-%d %I:%M:%S %p %Z")
    added_total = sum(v for (cat, typ), v in summary.items() if typ == "Added")
    removed_total = sum(v for (cat, typ), v in summary.items() if typ == "Removed")
    
    # Basic MD report
    md_content = "# Roblox FFlag Report\n"
    for header, changes in report:
        md_content += f"## {header}\n"
        for typ, cat, flag in changes:
            info = generate_flag_info(flag)
            md_content += f"- {typ} ({cat}): {flag} - Mechanism: {info['mechanism']}\n"
    OUTPUT_MD.write_text(md_content, encoding="utf-8")
    
    # Basic HTML report (mirroring MD for completeness)
    html_content = "<html><body><h1>Roblox FFlag Report</h1>"
    for header, changes in report:
        html_content += f"<h2>{header}</h2><ul>"
        for typ, cat, flag in changes:
            info = generate_flag_info(flag)
            html_content += f"<li>{typ} ({cat}): {escape_flag(flag)} - Mechanism: {info['mechanism']}</li>"
    html_content += "</ul></body></html>"
    OUTPUT_HTML.write_text(html_content, encoding="utf-8")
    
    log.info(f"Reports exported: {OUTPUT_MD} and {OUTPUT_HTML}")
    return added_total, removed_total, last_run, "reports_generated"  # Dummy fourth return for unpack

# ===============================
# Landing Page with Full Features
# ===============================
def ensure_landing_page(added: int, removed: int, last_run: str) -> None:
    index_html: Path = OUTPUT_DIR / "index.html"
    hist_file: Path = OUTPUT_DIR / "history.json"
    if not hist_file.exists():
        hist_file.write_text("[]", encoding="utf-8")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Roblox FFlag Tracker</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
<style>
:root {{ 
  --primary-green: #34d399;
  --primary-red: #f87171;
  --bg-opacity: 0.15;
  --text-color: #fff;
}}
body {{ 
  font-family:'Inter',sans-serif;
  margin:0;
  background: linear-gradient(135deg,#4f46e5,#3b82f6,#06b6d4,#14b8a6);
  background-size: 400% 400%;
  animation: gradientBG 15s ease infinite;
  color: var(--text-color);
  overflow-x: hidden;
}}
@keyframes gradientBG {{ 
  0% {{background-position:0% 50%;}}
  50% {{background-position:100% 50%;}}
  100% {{background-position:0% 50%;}}
}}
header {{ text-align:center; padding:60px 20px; text-shadow:0 0 12px rgba(0,0,0,0.3); }}
header h1 {{ font-size:3rem; font-weight:700; }}
.stats {{ 
  display:flex;
  justify-content:center;
  gap:30px;
  flex-wrap:wrap;
  max-width:900px;
  margin:-40px auto 40px;
  position:relative; z-index:2;
}}
.badge {{ 
  flex:1; min-width:220px;
  text-align:center;
  padding:25px;
  border-radius:16px;
  font-weight:700;
  backdrop-filter:blur(10px);
  background:rgba(255,255,255,var(--bg-opacity));
  box-shadow:0 10px 30px rgba(0,0,0,0.3);
  transition: transform 0.3s ease, box-shadow 0.3s ease, border 0.3s ease;
}}
.badge:hover {{ 
  transform:translateY(-8px);
  box-shadow:0 14px 40px rgba(0,0,0,0.4);
  border:2px solid var(--primary-green);
}}
.added {{ border-left:6px solid var(--primary-green); }}
.removed {{ border-left:6px solid var(--primary-red); }}
.last-run {{ text-align:center; margin:20px 0; font-style:italic; color:#eee; }}
section {{ max-width:1200px; margin:0 auto; padding:20px; }}
.report-container {{ 
  background: rgba(255,255,255,var(--bg-opacity));
  backdrop-filter: blur(10px);
  border-radius:16px;
  box-shadow:0 12px 36px rgba(0,0,0,0.25);
  padding:15px;
  position: relative;
}}
#loadingSpinner {{ 
  position: absolute;
  top: 50%; left: 50%;
  transform: translate(-50%, -50%);
  border: 4px solid rgba(255,255,255,0.3);
  border-top: 4px solid var(--primary-green);
  border-radius: 50%;
  width: 40px; height: 40px;
  animation: spin 1s linear infinite;
}}
@keyframes spin {{ 
  0% {{ transform: rotate(0deg); }}
  100% {{ transform: rotate(360deg); }}
}}
iframe {{ width:100%; height:75vh; border:none; border-radius:12px; }}
canvas#trendChart {{ display:block; max-width:850px; margin:40px auto; border-radius:12px; }}
input#searchInput {{ 
  width:90%; padding:12px; margin:20px auto; display:block;
  border-radius:12px; border:1px solid rgba(255,255,255,0.3);
  background:rgba(0,0,0,0.2); color: var(--text-color); font-size:1rem;
  backdrop-filter:blur(5px);
}}
footer {{ text-align:center; margin-top:60px; padding:25px; font-size:0.9rem; color:#eee; }}
canvas#particleCanvas {{ 
  position: fixed;
  top:0; left:0; width:100%; height:100%;
  pointer-events:none;
  z-index:0;
}}
</style>
</head>
<body>
<canvas id="particleCanvas"></canvas>
<header>
  <h1>Roblox Client FFlag Tracker</h1>
</header>

<section>
  <div class="stats">
    <div class="badge added">✅ Added: <span id="flags-added">{added}</span></div>
    <div class="badge removed">❌ Removed: <span id="flags-removed">{removed}</span></div>
  </div>

  <p class="last-run">Last Run: <span id="last-run">{last_run}</span></p>

  <input type="text" id="searchInput" placeholder="Search flags..." aria-label="Search flags">

  <h2>📊 Latest Full Report</h2>
  <div class="report-container">
    <div id="loadingSpinner"></div>
    <iframe src="FFlag_Report.html" id="reportFrame" aria-label="Latest report"></iframe>
  </div>

  <canvas id="trendChart" aria-label="Trend chart"></canvas>
</section>

<footer>Built with ❤️ by FFlag Tracker • Updated automatically</footer>

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
// Particle animation
const canvas = document.getElementById('particleCanvas');
const ctx = canvas.getContext('2d');
let resizeTimeout;
function resizeCanvas(){{ canvas.width=window.innerWidth; canvas.height=window.innerHeight; }}
resizeCanvas();
const particles=Array.from({{length:100}},()=>({{x:Math.random()*canvas.width,y:Math.random()*canvas.height,r:Math.random()*2+1,dx:(Math.random()-0.5)/2,dy:(Math.random()-0.5)/2,color:`rgba(${{Math.floor(Math.random()*50+200)}},255,255,0.15)`}}));
function animateParticles(){{ctx.clearRect(0,0,canvas.width,canvas.height);particles.forEach(p=>{{p.x+=p.dx;p.y+=p.dy;if(p.x<0||p.x>canvas.width)p.dx*=-1;if(p.y<0||p.y>canvas.height)p.dy*=-1;ctx.beginPath();ctx.arc(p.x,p.y,p.r,0,Math.PI*2);ctx.fillStyle=p.color;ctx.fill();}});requestAnimationFrame(animateParticles);}}
animateParticles();
window.addEventListener('resize',()=>{{clearTimeout(resizeTimeout);resizeTimeout=setTimeout(resizeCanvas,200);}});

// Trend chart
fetch("history.json").then(r=>r.json()).then(data=>{{
  const ctx=document.getElementById("trendChart").getContext("2d");
  new Chart(ctx,{{type:'line',data:{{labels:data.map(d=>d.date),datasets:[
    {{label:'Added',data:data.map(d=>d.added),borderColor:'#34d399',backgroundColor:'rgba(52,211,153,0.2)',fill:true,tension:0.4}},
    {{label:'Removed',data:data.map(d=>d.removed),borderColor:'#f87171',backgroundColor:'rgba(248,113,113,0.2)',fill:true,tension:0.4}}
  ]}},options:{{responsive:true,plugins:{{legend:{{position:'top'}}}},interaction:{{mode:'nearest',axis:'x',intersect:false}}}}}});
}});

// Search/filter
document.getElementById('searchInput').addEventListener('input',function(){{
  const q=this.value.toLowerCase();
  const iframe=document.getElementById('reportFrame');
  const doc=iframe.contentDocument||iframe.contentWindow.document;
  doc.querySelectorAll('li').forEach(li=>{{li.style.display=li.textContent.toLowerCase().includes(q)?'':'none';}});
}});

// Collapsible sections
const iframe=document.getElementById('reportFrame');
iframe.onload=()=>{{const doc=iframe.contentDocument||iframe.contentWindow.document; doc.querySelectorAll('h3').forEach(h3=>{{const ul=h3.nextElementSibling; h3.style.cursor='pointer'; h3.setAttribute('aria-expanded','true'); ul.style.display='block'; h3.addEventListener('click',()=>{{const expanded=ul.style.display!=='none';ul.style.display=expanded?'none':'block';h3.setAttribute('aria-expanded',!expanded);}});}});}};
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
        log.info("Roblox Client FFlag Tracker (Safe & Resilient Version)")
        log.info("=" * 80)
        ensure_repo()
        commits = get_commits()
        if not commits:
            log.warning(f"No commits in the last {DAYS} days.")
            return
        report, summary = build_report(commits)
        all_flags = [f for _, changes in report for _, _, f in changes]
        if all_flags:
            asyncio.run(generate_flag_info_batch(all_flags))
        added, removed, last_run, _ = export_reports(report, summary)
        ensure_landing_page(added, removed, last_run)
        update_history(added, removed, last_run)
        log.info("All done! Reports generated successfully.")
    except Exception as e:
        log.error(f"Main execution failed: {e}")

if __name__ == "__main__":
    main()
