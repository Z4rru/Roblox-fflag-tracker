// Fixes for CSP, MIME, and canvas oversize errors
// Place in assets/app.js after Chart.bundle.js is loaded

(async function() {
  const DEBUG = true;

  function log(...args) {
    if (DEBUG) console.log('[App]', ...args);
  }

  if (!window.Chart) {
    log('Chart.js not found. Ensure chart.bundle.js is included.');
    return;
  }

  // Ensure a container with proper dimensions
  let container = document.getElementById('chart-container');
  if (!container) {
    container = document.createElement('div');
    container.id = 'chart-container';
    container.style.width = '800px';
    container.style.height = '400px';
    container.style.maxWidth = '100%';
    container.style.maxHeight = '600px';
    document.body.appendChild(container);
  }

  let canvas = document.getElementById('fflagChart');
  if (!canvas) {
    canvas = document.createElement('canvas');
    canvas.id = 'fflagChart';
    container.appendChild(canvas);
  }

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
          zoom: { wheel: { enabled: true }, pinch: { enabled: true }, mode: 'xy' },
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

  try {
    new Chart(canvas, config);
    log('Chart initialized successfully.');
  } catch (err) {
    console.error('Chart initialization failed:', err);
  }
})();
