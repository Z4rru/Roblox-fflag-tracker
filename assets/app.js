document.addEventListener('DOMContentLoaded', function () {
  if (window.Chart && (window['chartjs-plugin-zoom'] || window.ChartZoom)) {
    const zoomPlugin = window['chartjs-plugin-zoom'] || window.ChartZoom;
    window.Chart.register(zoomPlugin);
  }

  const ctx = document.getElementById('myChart');
  if (!ctx) return console.error('Canvas not found');

  new Chart(ctx.getContext('2d'), {
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
      }
    }
  });
});
