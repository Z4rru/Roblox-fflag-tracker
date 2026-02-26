(function () {
  const $ = (id) => document.getElementById(id);
  const state = {
    summary: null, index: null, commits: [], history: [],
    page: 0, loading: false, done: false,
    search: "", category: "", sort: ""
  };

  function debounce(fn, ms) {
    let t; return (...a) => { clearTimeout(t); t = setTimeout(() => fn(...a), ms); };
  }

  function initTheme() {
    const saved = localStorage.getItem("fflag-theme");
    if (saved) document.body.className = saved;
    $("themeToggle")?.addEventListener("click", () => {
      document.body.classList.remove("high-contrast");
      document.body.classList.toggle("light");
      localStorage.setItem("fflag-theme", document.body.className.trim());
      rebuildChart();
    });
    $("contrastToggle")?.addEventListener("click", () => {
      document.body.classList.remove("light");
      document.body.classList.toggle("high-contrast");
      localStorage.setItem("fflag-theme", document.body.className.trim());
      rebuildChart();
    });
  }

  function initParticles() {
    const c = $("particleCanvas");
    if (!c || matchMedia("(prefers-reduced-motion:reduce)").matches) return;
    const ctx = c.getContext("2d");
    const resize = () => { c.width = innerWidth; c.height = innerHeight; };
    resize();
    addEventListener("resize", debounce(resize, 250));
    const n = Math.min(~~(innerWidth * innerHeight / 20000), 55);
    const ps = Array.from({ length: n }, () => ({
      x: Math.random() * c.width, y: Math.random() * c.height,
      r: Math.random() * 1.4 + 0.4,
      dx: (Math.random() - 0.5) * 0.22, dy: (Math.random() - 0.5) * 0.22,
      o: Math.random() * 0.25 + 0.05
    }));
    (function draw() {
      ctx.clearRect(0, 0, c.width, c.height);
      if (!document.body.classList.contains("high-contrast")) {
        const rgb = document.body.classList.contains("light") ? "0,0,0" : "255,255,255";
        for (const p of ps) {
          p.x = (p.x + p.dx + c.width) % c.width;
          p.y = (p.y + p.dy + c.height) % c.height;
          ctx.beginPath();
          ctx.arc(p.x, p.y, p.r, 0, 6.2832);
          ctx.fillStyle = `rgba(${rgb},${p.o})`;
          ctx.fill();
        }
      }
      requestAnimationFrame(draw);
    })();
  }

  function animateNum(el, to) {
    if (!el) return;
    const t0 = performance.now(), dur = 1000;
    const isF = String(to).includes(".");
    (function tick(now) {
      const p = Math.min((now - t0) / dur, 1);
      const v = to * (1 - Math.pow(1 - p, 3));
      el.textContent = isF ? v.toFixed(2) : Math.round(v);
      if (p < 1) requestAnimationFrame(tick);
    })(t0);
  }

  async function get(url) {
    const r = await fetch(url);
    if (!r.ok) throw new Error(`${r.status} ${url}`);
    return r.json();
  }

  async function loadSummary() {
    try {
      const s = state.summary = await get("summary.json");
      animateNum($("flags-added"), s.added_total || 0);
      animateNum($("flags-changed"), s.changed_total || 0);
      animateNum($("flags-removed"), s.removed_total || 0);
      animateNum($("net-changes"), s.net_changes || 0);
      animateNum($("percent-change"), s.percent_change || 0);
      animateNum($("historical-added"), s.total_historical_added || 0);
      animateNum($("historical-changed"), s.total_historical_changed || 0);
      animateNum($("historical-removed"), s.total_historical_removed || 0);
      const lr = $("last-run");
      if (lr && s.last_run) lr.textContent = s.last_run;
      const pctBadge = document.querySelector(".badge.pct");
      if (pctBadge) {
        pctBadge.classList.remove("positive", "negative");
        pctBadge.classList.add((s.percent_change || 0) >= 0 ? "positive" : "negative");
      }
    } catch (e) { console.error("summary:", e); }
  }

  async function loadHistory() {
    try { state.history = await get("history.json"); }
    catch (e) { console.error("history:", e); state.history = []; }
  }

  async function loadIndex() {
    try {
      const d = await get("commits_index.json");
      if (Array.isArray(d)) {
        state.index = { chunks: d.map((p) => p.replace(/^output\//, "")), total: d.length * 20 };
      } else {
        state.index = d;
      }
    } catch (e) {
      console.error("index:", e);
      state.index = { chunks: [], total: 0 };
    }
  }

  async function loadNextChunk() {
    if (state.loading || state.done || !state.index) return;
    const chunks = state.index.chunks || [];
    if (state.page >= chunks.length) { state.done = true; return; }
    state.loading = true;
    spin(true);
    try {
      const data = await get(chunks[state.page]);
      if (Array.isArray(data)) state.commits.push(...data);
      state.page++;
      render();
    } catch (e) { console.error("chunk:", e); }
    finally { state.loading = false; spin(false); }
  }

  function spin(on) {
    const s = $("loadingSpinner");
    if (s) s.style.display = on ? "block" : "none";
  }

  function filtered() {
    const q = state.search.toLowerCase();
    const cat = state.category;
    return state.commits.map((c) => {
      const g = {};
      let any = false;
      for (const [k, flags] of Object.entries(c.grouped || {})) {
        const gc = k.split("_").slice(1).join("_");
        if (cat && gc !== cat) continue;
        const ff = q
          ? flags.filter((f) =>
              f.name.toLowerCase().includes(q) ||
              (f.mechanism || "").toLowerCase().includes(q) ||
              (f.purpose || "").toLowerCase().includes(q))
          : flags;
        if (ff.length) {
          g[k] = state.sort === "freq"
            ? [...ff].sort((a, b) => (b.freq || 0) - (a.freq || 0))
            : ff;
          any = true;
        }
      }
      return any ? { ...c, grouped: g } : null;
    }).filter(Boolean);
  }

  function render() {
    const el = $("reportContent");
    if (!el) return;
    const list = filtered();
    if (!list.length) {
      el.innerHTML = state.commits.length
        ? '<p style="text-align:center;padding:40px;opacity:.6">No matching flags.</p>'
        : "";
      return;
    }
    const frag = document.createDocumentFragment();
    for (const commit of list) {
      const card = document.createElement("div");
      card.className = "commit-card";
      const h3 = document.createElement("h3");
      h3.textContent = commit.header || "—";
      h3.tabIndex = 0;
      h3.setAttribute("role", "button");
      h3.setAttribute("aria-expanded", "true");
      const body = document.createElement("div");
      for (const [k, flags] of Object.entries(commit.grouped || {})) {
        const type = k.split("_")[0];
        const gc = k.split("_").slice(1).join("_");
        const ico = type === "Added" ? "✅" : type === "Changed" ? "🔄" : "❌";
        const cls = type === "Added" ? "a" : type === "Changed" ? "c" : "r";
        const det = document.createElement("details");
        det.open = true;
        const sum = document.createElement("summary");
        sum.className = cls;
        sum.textContent = `${ico} ${type} — ${gc} (${flags.length})`;
        det.appendChild(sum);
        const ul = document.createElement("ul");
        for (const fl of flags) {
          const li = document.createElement("li");
          const nm = document.createElement("strong");
          nm.textContent = fl.name;
          const cp = document.createElement("button");
          cp.className = "copy-btn";
          cp.textContent = "📋";
          cp.title = "Copy flag name";
          cp.setAttribute("aria-label", "Copy " + fl.name);
          cp.addEventListener("click", (ev) => {
            ev.stopPropagation();
            navigator.clipboard.writeText(fl.name).then(() => {
              cp.textContent = "✓";
              setTimeout(() => (cp.textContent = "📋"), 1200);
            }).catch(() => {});
          });
          let desc = "";
          if (type === "Added") desc = " = " + (fl.new_value ?? "?");
          else if (type === "Changed") desc = " " + (fl.old_value ?? "?") + " → " + (fl.new_value ?? "?");
          else desc = " was " + (fl.old_value ?? "?");
          li.appendChild(nm);
          li.appendChild(cp);
          li.appendChild(document.createTextNode(desc));
          if (fl.mechanism && !fl.mechanism.startsWith("N/A")) {
            const sm = document.createElement("small");
            sm.style.cssText = "display:block;opacity:.6;margin-top:2px";
            sm.textContent = fl.mechanism + " — " + fl.purpose;
            li.appendChild(sm);
          }
          if (fl.freq > 1) {
            const sp = document.createElement("span");
            sp.style.cssText = "margin-left:6px;font-size:.7rem;opacity:.4";
            sp.textContent = "×" + fl.freq;
            li.appendChild(sp);
          }
          ul.appendChild(li);
        }
        det.appendChild(ul);
        body.appendChild(det);
      }
      let open = true;
      const toggle = () => {
        open = !open;
        body.style.display = open ? "" : "none";
        h3.setAttribute("aria-expanded", String(open));
      };
      h3.addEventListener("click", toggle);
      h3.addEventListener("keydown", (e) => {
        if (e.key === "Enter" || e.key === " ") { e.preventDefault(); toggle(); }
      });
      card.appendChild(h3);
      card.appendChild(body);
      frag.appendChild(card);
    }
    el.innerHTML = "";
    el.appendChild(frag);
  }

  function rebuildChart() {
    if (window._fc) { window._fc.destroy(); window._fc = null; }
    const reset = document.querySelector(".reset-zoom");
    if (reset) reset.remove();
    initChart();
  }

  function initChart() {
    const canvas = $("myChart");
    if (!canvas || !state.history.length || !window.Chart) return;
    const ct = $("chart-container");
    if (ct) ct.style.cssText = "position:relative;max-width:920px;margin:40px auto";
    const labels = state.history.map((h) => (h.date || "").split(" ")[0]);
    const dk = !document.body.classList.contains("light");
    const gc = dk ? "rgba(255,255,255,.06)" : "rgba(0,0,0,.06)";
    const tc = dk ? "#94a3b8" : "#64748b";
    const tb = dk ? "rgba(15,23,42,.95)" : "rgba(255,255,255,.95)";
    const tt = dk ? "#e2e8f0" : "#1e293b";
    const opts = {
      responsive: true,
      aspectRatio: 2.2,
      interaction: { intersect: false, mode: "index" },
      plugins: {
        legend: { labels: { color: tc, usePointStyle: true, padding: 16, font: { size: 12 } } },
        tooltip: {
          backgroundColor: tb, titleColor: tt, bodyColor: tc,
          borderColor: dk ? "rgba(255,255,255,.1)" : "rgba(0,0,0,.1)",
          borderWidth: 1, cornerRadius: 8, padding: 12
        }
      },
      scales: {
        x: { grid: { color: gc }, ticks: { color: tc, maxRotation: 45, autoSkip: true, maxTicksLimit: 14 } },
        y: { beginAtZero: true, grid: { color: gc }, ticks: { color: tc } }
      }
    };
    if (window.Chart.registry?.plugins?.get("zoom")) {
      opts.plugins.zoom = {
        zoom: { wheel: { enabled: true }, pinch: { enabled: true }, mode: "x" },
        pan: { enabled: true, mode: "x" }
      };
    }
    window._fc = new Chart(canvas, {
      type: "line",
      data: {
        labels,
        datasets: [
          { label: "Added", data: state.history.map((h) => h.added || 0), borderColor: "#34d399", backgroundColor: "rgba(52,211,153,.08)", fill: true, tension: .35, pointRadius: 2, pointHoverRadius: 6, borderWidth: 2 },
          { label: "Changed", data: state.history.map((h) => h.changed || 0), borderColor: "#60a5fa", backgroundColor: "rgba(96,165,250,.08)", fill: true, tension: .35, pointRadius: 2, pointHoverRadius: 6, borderWidth: 2 },
          { label: "Removed", data: state.history.map((h) => h.removed || 0), borderColor: "#f87171", backgroundColor: "rgba(248,113,113,.08)", fill: true, tension: .35, pointRadius: 2, pointHoverRadius: 6, borderWidth: 2 }
        ]
      },
      options: opts
    });
    if (ct && !ct.querySelector(".reset-zoom") && opts.plugins.zoom) {
      const b = document.createElement("button");
      b.textContent = "Reset Zoom";
      b.className = "reset-zoom";
      b.style.cssText = "margin:10px auto;display:block;padding:6px 18px;border-radius:6px;background:var(--b,#60a5fa);color:#fff;border:none;cursor:pointer;font-size:.8rem";
      b.addEventListener("click", () => window._fc?.resetZoom());
      ct.appendChild(b);
    }
  }

  function csvExport() {
    const rows = [["Commit", "Type", "Category", "Flag", "Old", "New", "Mechanism", "Purpose", "Freq"]];
    for (const c of filtered()) {
      for (const [k, flags] of Object.entries(c.grouped || {})) {
        const t = k.split("_")[0], cat = k.split("_").slice(1).join("_");
        for (const f of flags)
          rows.push([c.header, t, cat, f.name, f.old_value || "", f.new_value || "", f.mechanism || "", f.purpose || "", f.freq || 0]);
      }
    }
    dl("fflag_export.csv", rows.map((r) => r.map((c) => '"' + String(c).replace(/"/g, '""') + '"').join(",")).join("\n"), "text/csv");
  }

  function jsonExport() {
    dl("fflag_export.json", JSON.stringify({ exported: new Date().toISOString(), summary: state.summary, commits: filtered() }, null, 2), "application/json");
  }

  function dl(name, content, type) {
    const a = document.createElement("a");
    a.href = URL.createObjectURL(new Blob([content], { type }));
    a.download = name;
    a.click();
    URL.revokeObjectURL(a.href);
  }

  function initControls() {
    const si = $("searchInput"), cf = $("categoryFilter"), ss = $("sortSelect");
    si?.addEventListener("input", debounce(() => { state.search = si.value.trim(); render(); }, 220));
    cf?.addEventListener("change", () => { state.category = cf.value; render(); });
    ss?.addEventListener("change", () => { state.sort = ss.value; render(); });
    $("exportCSV")?.addEventListener("click", csvExport);
    $("exportJSON")?.addEventListener("click", jsonExport);
  }

  function initScroll() {
    const sen = document.createElement("div");
    sen.style.height = "1px";
    $("reportContent")?.after(sen);
    new IntersectionObserver((entries) => {
      if (entries[0].isIntersecting) loadNextChunk();
    }, { rootMargin: "400px" }).observe(sen);
  }

  function initBackToTop() {
    const btn = document.createElement("button");
    btn.setAttribute("aria-label", "Back to top");
    btn.textContent = "↑";
    btn.style.cssText = "position:fixed;bottom:24px;right:24px;width:44px;height:44px;border-radius:50%;background:var(--b,#60a5fa);color:#fff;border:none;cursor:pointer;font-size:1.3rem;display:none;z-index:10;box-shadow:0 4px 16px rgba(0,0,0,.3);transition:opacity .3s";
    document.body.appendChild(btn);
    btn.addEventListener("click", () => scrollTo({ top: 0, behavior: "smooth" }));
    addEventListener("scroll", debounce(() => { btn.style.display = scrollY > 500 ? "block" : "none"; }, 80), { passive: true });
  }

  function initKeys() {
    document.addEventListener("keydown", (e) => {
      if (e.target.tagName === "INPUT" || e.target.tagName === "SELECT" || e.target.tagName === "TEXTAREA") {
        if (e.key === "Escape") { e.target.blur(); e.target.value = ""; state.search = ""; render(); }
        return;
      }
      if (e.key === "/") { e.preventDefault(); $("searchInput")?.focus(); }
      if (e.key === "t") $("themeToggle")?.click();
    });
  }

  function regSW() {
    if ("serviceWorker" in navigator) {
      navigator.serviceWorker.register("sw.js").catch(() => {});
    }
  }

  async function init() {
    initTheme();
    initParticles();
    initControls();
    initKeys();
    initBackToTop();
    regSW();
    spin(true);
    await Promise.all([loadSummary(), loadHistory(), loadIndex()]);
    initChart();
    await loadNextChunk();
    spin(false);
    initScroll();
    if (!state.commits.length && state.done) {
      const el = $("reportContent");
      if (el) el.innerHTML = '<p style="text-align:center;padding:40px;opacity:.5">No data yet — check back after the next tracker run.</p>';
    }
  }

  init();
})();
