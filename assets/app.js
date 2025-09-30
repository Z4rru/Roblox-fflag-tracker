// assets/app.js
(async function initChart() {
  async function loadScript(src) {
    return new Promise((resolve, reject) => {
      const s = document.createElement('script');
      s.src = src;
      s.async = true;
      s.onload = resolve;
      s.onerror = reject;
      document.head.appendChild(s);
    });
  }

  try {
    if (!window.Chart) {
      await loadScript('https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.0/chart.umd.min.js');
    }
    if (!window.ChartZoom) {
      await loadScript('https://cdnjs.cloudflare.com/ajax/libs/chartjs-plugin-zoom/2.0.1/chartjs-plugin-zoom.umd.min.js');
    }
  } catch (err) {
    console.warn('[App] CDN load failed, falling back to local assets:', err);
    try {
      if (!window.Chart) {
        await loadScript('assets/chart.js');
      }
      if (!window.ChartZoom) {
        await loadScript('assets/chartjs-plugin-zoom.js');
      }
    } catch (e) {
      console.error('[App] Failed to load local chart libraries:', e);
      return;
    }
  }

  // Initialize chart
  const ctx = document.getElementById('chart').getContext('2d');
  const chart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: ['Jan', 'Feb', 'Mar', 'Apr'],
      datasets: [{
        label: 'Example',
        data: [10, 20, 30, 25],
        borderWidth: 2
      }]
    },
    options: {
      responsive: true,
      plugins: {
        zoom: {
          zoom: {
            wheel: { enabled: true },
            pinch: { enabled: true },
            mode: 'x'
          }
        }
      }
    }
  });

  console.log('[App] Chart initialized successfully.');
})();
