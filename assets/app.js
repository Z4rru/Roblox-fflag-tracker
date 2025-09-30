// assets/app.js
// Main application logic for Fflag Tracker
// Handles chart initialization, data loading, and resilience against CSP/CDN issues

(async function() {
  // Debug toggle
  const DEBUG = true;

  function log(...args) {
    if (DEBUG) console.log('[App]', ...args);
  }

  // Ensure Chart.js is available (from bundle)
  if (!window.Chart) {
    log('Chart.js not found. Make sure assets/chart.bundle.js is loaded.');
    return;
  }

  // Create or get canvas
  let canvas = document.getElementById('fflagChart');
  if (!canvas) {
    canvas = document.createElement('canvas');
    canvas.id = 'fflagChart';
    document.body.appendChild(canvas);
  }

  // Example dataset: Replace with real FFlag tracking data
  const data = {
    labels: ['Flag A', 'Flag B', 'Flag C', 'Flag D'],
    datasets: [{
      label: 'FFlag Toggles',
      data: [12, 19, 3, 5],
      borderColor: 'rgba(75,192,192,1)',
      backgroundColor: 'rgba(75,192,192,0.2)',
      tension: 0.2
    }]
  };

  // Chart config with zoom & pan
  const config = {
    type: 'line',
    data: data,
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: { position: 'top' },
        title: { display: true, text: 'Fflag Tracker Debug' },
        zoom: {
          zoom: {
            wheel: { enabled: true },
            pinch: { enabled: true },
            mode: 'xy'
          },
          pan: { enabled: true, mode: 'xy' }
        }
      },
      interaction: { mode: 'nearest', axis: 'x', intersect: false },
      scales: {
        x: { title: { display: true, text: 'Flags' } },
        y: { title: { display: true, text: 'Values' } }
      }
    }
  };

  // Initialize chart
  try {
    new Chart(canvas, config);
    log('Chart initialized successfully.');
  } catch (err) {
    console.error('Chart initialization failed:', err);
  }
})();
