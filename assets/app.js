// app.js - Local-only chart setup (no CDN)
(async function() {
  async function loadScript(src) {
    return new Promise((resolve, reject) => {
      const script = document.createElement('script');
      script.src = src;
      script.async = true;
      script.onload = () => resolve();
      script.onerror = (e) => reject(e);
      document.head.appendChild(script);
    });
  }

  try {
    // ✅ Load from local assets only
    await loadScript('assets/chart.js');
    await loadScript('assets/chartjs-plugin-zoom.js');

    console.log('[App] Local chart libraries loaded');

    // ✅ Initialize chart
    const ctx = document.getElementById('myChart').getContext('2d');
    new Chart(ctx, {
      type: 'line',
      data: {
        labels: ['A', 'B', 'C', 'D'],
        datasets: [{
          label: 'Demo',
          data: [10, 20, 15, 30],
          borderColor: 'rgb(75, 192, 192)',
          fill: false
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

  } catch (err) {
    console.error('[App] Failed to load local chart libraries:', err);
  }
})();
