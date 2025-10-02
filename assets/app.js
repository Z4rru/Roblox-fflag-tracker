document.addEventListener('DOMContentLoaded', async function () {
  async function loadScript(src) {
    return new Promise((resolve, reject) => {
      const script = document.createElement('script');
      script.src = src;
      script.async = true;
      script.onload = () => {
        console.log(`[App] Loaded ${src}`);
        resolve();
      };
      script.onerror = (err) => {
        console.error(`[App] Failed to load ${src}`, err);
        reject(err);
      };
      document.head.appendChild(script);
    });
  }

  try {
    // Load Chart.js then plugin sequentially
    await loadScript('assets/chart.js');
    await loadScript('assets/chartjs-plugin-zoom.js');
    console.log('[App] Local chart libraries loaded successfully');

    // Register zoom plugin (UMD export is window.ChartZoom)
    if (window.Chart && window.ChartZoom) {
      window.Chart.register(window.ChartZoom);
    }

    // Initialize chart
    const canvas = document.getElementById('myChart');
    if (!canvas) throw new Error('Canvas not found');

    new Chart(canvas.getContext('2d'), {
      type: 'line',
      data: {
        labels: ['Jan', 'Feb', 'Mar', 'Apr'],
        datasets: [{
          label: 'FFlag Changes',
          data: [12, 19, 3, 5],
          borderColor: 'rgb(75, 192, 192)',
          backgroundColor: 'rgba(75, 192, 192, 0.2)',
          fill: false,
          tension: 0.1
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          zoom: {
            zoom: {
              wheel: { enabled: true },
              pinch: { enabled: true },
              mode: 'xy'
            },
            pan: {
              enabled: true,
              mode: 'xy'
            }
          }
        },
        scales: {
          y: { beginAtZero: true }
        }
      }
    });

    console.log('[App] Chart initialized — zoom away!');

  } catch (err) {
    console.error('[App] Full fail on local chart setup:', err);
    const canvas = document.getElementById('myChart');
    if (canvas) {
      canvas.outerHTML = '<p>Chart load failed — check console. [Static fallback here]</p>';
    }
  }
});
