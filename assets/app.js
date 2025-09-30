// assets/app.js - Consolidated UMD fallback, charts, particles, themes, error handling, and SW registration

(function() {
  // Global Error Handling
  window.onerror = function (message, source, lineno, colno, error) {
    console.error(`Grok Debug: ${message} at ${source}:${lineno}:${colno}`);
    if (/ERR_BLOCKED_BY_CLIENT|MIME|CORS/.test(error?.message || message)) {
      alert('Adblocker or extension blocking CDN—disable for cdnjs.cloudflare.com or use local assets!');
      localStorage.setItem('errorLog', JSON.stringify({ message, source, lineno, colno, timestamp: new Date().toISOString() }));
    }
    return true; // Prevent default error popup in some browsers
  };

  // Load Script Utility (used for fallbacks)
  function loadScript(src) {
    return new Promise((resolve, reject) => {
      const s = document.createElement('script');
      s.src = src;
      s.onload = resolve;
      s.onerror = () => reject(new Error(`Failed to load ${src}`));
      document.head.appendChild(s);
    });
  }

  // Font Preload Handler (CSP-safe, externalized)
  function handleFontPreload() {
    const pl = document.getElementById('font-preload');
    if (pl) {
      pl.addEventListener('load', () => { pl.rel = 'stylesheet'; });
    } else {
      const preloadLink = document.querySelector('link[rel="preload"][as="style"]');
      if (preloadLink) preloadLink.rel = 'stylesheet';
    }
  }

  // Particle Background (Optimized for performance)
  const canvas = document.getElementById('particleCanvas');
  let ctx, animationId, particles = [];
  if (canvas) {
    ctx = canvas.getContext('2d');
    function resizeCanvas() {
      canvas.width = window.innerWidth;
      canvas.height = window.innerHeight;
    }
    function generateParticles() {
      particles = Array.from({ length: 20 }, () => ({
        x: Math.random() * canvas.width,
        y: Math.random() * canvas.height,
        r: Math.random() * 2 + 1,
        dx: (Math.random() - 0.5) / 2,
        dy: (Math.random() - 0.5) / 2,
        color: `rgba(${Math.floor(Math.random() * 50 + 200)}, 255, 255, 0.15)`
      }));
    }
    function animateParticles() {
      if (!ctx) return;
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
    window.addEventListener('resize', resizeCanvas);
    document.addEventListener('visibilitychange', () => {
      if (document.hidden) stopAnimation();
      else if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) animateParticles();
    });
  }

  // Theme & Contrast Toggle (with localStorage and cookie fallback)
  function applyTheme() {
    let theme = localStorage.getItem('theme') || (document.cookie.match(/theme=([^;]*)/)?.[1] || '');
    document.body.classList.remove('light', 'high-contrast');
    if (canvas) canvas.style.display = 'block';
    if (theme === 'light') {
      document.body.classList.add('light');
    } else if (theme === 'high-contrast') {
      document.body.classList.add('high-contrast');
      if (canvas) {
        stopAnimation();
        canvas.style.display = 'none';
      }
    } else if (canvas && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
      animateParticles();
    }
  }
  function setTheme(theme) {
    localStorage.setItem('theme', theme);
    document.cookie = `theme=${theme}; path=/; max-age=31536000`;
    applyTheme();
  }

  // Basic Chart Initialization (for fflagChart if present)
  async function initBasicChart() {
    if (!document.getElementById('fflagChart')) return;
    let ChartRef = window.Chart;
    let ZoomPlugin = window.ChartZoom || window.zoomPlugin || window.hammerZoom; // Handle possible UMD names
    if (!ChartRef || !ZoomPlugin) {
      try {
        await loadScript('https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.min.js');
        await loadScript('https://cdnjs.cloudflare.com/ajax/libs/chartjs-plugin-zoom/2.0.1/chartjs-plugin-zoom.min.js');
        ChartRef = window.Chart;
        ZoomPlugin = window.ChartZoom || window.zoomPlugin;
      } catch (e) {
        console.warn('CDN failed, loading local');
        try {
          await loadScript('assets/chart.js');
          await loadScript('assets/chartjs-plugin-zoom.js');
          ChartRef = window.Chart;
          ZoomPlugin = window.ChartZoom || window.zoomPlugin;
        } catch (localErr) {
          console.error('Local fallback failed:', localErr);
          return;
        }
      }
    }
    try {
      ChartRef.register(ZoomPlugin);
    } catch (e) {
      console.warn('Zoom plugin registration failed:', e);
    }
    const ctx = document.getElementById('fflagChart').getContext('2d');
    new ChartRef(ctx, {
      type: 'line',
      data: {
        labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May'], // Dynamic replacement needed
        datasets: [{
          label: 'FFlag Changes',
          data: [10, 20, 15, 25, 30], // Fetch from JSON
          borderColor: 'rgb(75, 192, 192)',
          tension: 0.1
        }]
      },
      options: {
        responsive: true,
        plugins: {
          zoom: {
            zoom: { wheel: { enabled: true }, pinch: { enabled: true }, mode: 'xy' },
            pan: { enabled: true, mode: 'xy' }
          }
        },
        scales: {
          x: { type: 'time', time: { unit: 'month' } },
          y: { beginAtZero: true }
        }
      }
    });
  }

  // Trend Chart Loader (with retries and fallback)
  async function initTrendChart() {
    const trendChart = document.getElementById('trendChart');
    if (!trendChart) return;
    trendChart.style.display = 'none';
    const loadingP = document.createElement('p');
    loadingP.textContent = 'Loading...';
    trendChart.parentNode.insertBefore(loadingP, trendChart);
    let retries = 0;
    const maxRetries = 5;
    async function loadChartData() {
      try {
        let ChartRef = window.Chart;
        let zoomPlugin = window.ChartZoom || window.zoomPlugin;
        if (!ChartRef || !zoomPlugin) {
          try {
            // Prefer cdnjs for reliable MIME/CORS
            await loadScript('https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.min.js');
            await loadScript('https://cdnjs.cloudflare.com/ajax/libs/chartjs-plugin-zoom/2.0.1/chartjs-plugin-zoom.min.js');
            ChartRef = window.Chart;
            zoomPlugin = window.ChartZoom || window.zoomPlugin;
          } catch (cdnError) {
            console.warn('CDN failed, falling back to local:', cdnError);
            await loadScript('assets/chart.js');
            await loadScript('assets/chartjs-plugin-zoom.js');
            ChartRef = window.Chart;
            zoomPlugin = window.ChartZoom || window.zoomPlugin;
          }
        }
        ChartRef.register(zoomPlugin);
        const response = await fetch('history.json');
        if (!response.ok) throw new Error(`Failed to load history.json: ${response.status}`);
        const data = await response.json();
        if (!data || data.length === 0) {
          loadingP.textContent = 'No history data yet.';
          trendChart.remove();
          return;
        }
        const ctx = trendChart.getContext('2d');
        new ChartRef(ctx, {
          type: 'line',
          data: {
            labels: data.map(d => d.date),
            datasets: [
              { label: 'Added', data: data.map(d => d.added || 0), borderColor: '#34d399', backgroundColor: 'rgba(52,211,153,0.2)', fill: true, tension: 0.4 },
              { label: 'Changed', data: data.map(d => d.changed || 0), borderColor: '#60a5fa', backgroundColor: 'rgba(96,165,250,0.2)', fill: true, tension: 0.4 },
              { label: 'Removed', data: data.map(d => d.removed || 0), borderColor: '#f87171', backgroundColor: 'rgba(248,113,113,0.2)', fill: true, tension: 0.4 }
            ]
          },
          options: {
            responsive: true,
            plugins: {
              legend: { position: 'top' },
              zoom: { zoom: { wheel: { enabled: true }, pinch: { enabled: true }, mode: 'x' }, pan: { enabled: true, mode: 'x' } },
              tooltip: { callbacks: { label: ctx => `${ctx.dataset.label}: ${ctx.raw}` } }
            },
            interaction: { mode: 'nearest', axis: 'x', intersect: false }
          }
        });
        loadingP.remove();
        trendChart.style.display = '';
      } catch (error) {
        console.error('Error loading trend chart:', error);
        if (retries < maxRetries) {
          retries++;
          loadingP.textContent = `Error loading chart. Retrying (${retries}/${maxRetries}) in ${retries * 2} seconds... (Check adblockers or network!)`;
          setTimeout(loadChartData, retries * 2000);
        } else {
          loadingP.textContent = 'Failed after max retries. Use local JS files or check console.';
        }
      }
    }
    await loadChartData();
  }

  // Debug Mode Toggle
  function initDebug() {
    document.addEventListener('keydown', e => {
      if (e.ctrlKey && e.shiftKey && e.key === 'D') {
        console.log('Grok Raw Debug: Dumping globalData', window.globalData || 'No globalData defined');
        alert('Debug mode activated—check console for raw logs!');
      }
    });
  }

  // Service Worker Registration
  if ('serviceWorker' in navigator) {
    window.addEventListener('load', async () => {
      try {
        const reg = await navigator.serviceWorker.register('/sw.js');
        console.log('Service Worker registered:', reg);
      } catch (err) {
        console.error('Service Worker registration failed:', err);
      }
    });
  }

  // DOMContentLoaded Initialization
  document.addEventListener('DOMContentLoaded', async () => {
    handleFontPreload();
    if (canvas) {
      resizeCanvas();
      generateParticles();
      if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) animateParticles();
    }
    applyTheme();
    const themeToggle = document.getElementById('themeToggle');
    if (themeToggle) themeToggle.addEventListener('click', () => setTheme(document.body.classList.contains('light') ? '' : 'light'));
    const contrastToggle = document.getElementById('contrastToggle');
    if (contrastToggle) contrastToggle.addEventListener('click', () => setTheme(document.body.classList.contains('high-contrast') ? '' : 'high-contrast'));
    await initBasicChart();
    await initTrendChart();
    initDebug();
  });
})();
