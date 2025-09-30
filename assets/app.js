(function() {
  // Global Error Handling with Adblock/CDN detection
  window.onerror = function (message, source, lineno, colno, error) {
    console.error(`Grok Debug: ${message} at ${source}:${lineno}:${colno}`);
    if (/ERR_BLOCKED_BY_CLIENT|MIME|CORS/.test(error?.message || message)) {
      console.warn('Adblocker or extension blocking CDN—falling back to local assets.');
      localStorage.setItem('errorLog', JSON.stringify({
        message, source, lineno, colno,
        timestamp: new Date().toISOString()
      }));
    }
    return true;
  };

  // Utility: Dynamic script loader (CSP-safe)
  function loadScript(src) {
    return new Promise((resolve, reject) => {
      const s = document.createElement('script');
      s.src = src;
      s.async = true;
      s.onload = resolve;
      s.onerror = () => reject(new Error(`Failed to load ${src}`));
      document.head.appendChild(s);
    });
  }

  // Chart Initialization (with CDN + Local fallback)
  async function initChartSafe(elId) {
    const el = document.getElementById(elId);
    if (!el) return;

    let ChartRef = window.Chart;
    let ZoomPlugin = window.ChartZoom || window.zoomPlugin;

    if (!ChartRef || !ZoomPlugin) {
      try {
        await loadScript('https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.min.js');
        await loadScript('https://cdnjs.cloudflare.com/ajax/libs/chartjs-plugin-zoom/2.0.1/chartjs-plugin-zoom.min.js');
        ChartRef = window.Chart;
        ZoomPlugin = window.ChartZoom || window.zoomPlugin;
      } catch (e) {
        console.warn('CDN failed, using local assets.', e);
        try {
          await loadScript('assets/chart.js');
          await loadScript('assets/chartjs-plugin-zoom.js');
          ChartRef = window.Chart;
          ZoomPlugin = window.ChartZoom || window.zoomPlugin;
        } catch (localErr) {
          console.error('Both CDN and local assets failed.', localErr);
          return;
        }
      }
    }

    try { ChartRef.register(ZoomPlugin); } catch (e) {
      console.warn('Zoom plugin registration issue:', e);
    }

    new ChartRef(el.getContext('2d'), {
      type: 'line',
      data: {
        labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
        datasets: [{
          label: 'FFlag Changes',
          data: [10, 20, 15, 25, 30],
          borderColor: 'rgb(75,192,192)',
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
        scales: { x: { type: 'category' }, y: { beginAtZero: true } }
      }
    });
  }

  // Service Worker Safe Registration
  if ('serviceWorker' in navigator) {
    window.addEventListener('load', async () => {
      try {
        await navigator.serviceWorker.register('/sw.js');
        console.log('Service Worker registered.');
      } catch (err) {
        console.warn('Service Worker registration failed:', err);
      }
    });
  }

  // DOMContentLoaded Init
  document.addEventListener('DOMContentLoaded', async () => {
    await initChartSafe('fflagChart');
    await initChartSafe('trendChart');
  });
})();
