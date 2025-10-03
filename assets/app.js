document.addEventListener('DOMContentLoaded', async function () {
  async function fetchData() {
    const res = await fetch("output/fflag.json");
    if (!res.ok) throw new Error("Failed to fetch fflag.json");
    return await res.json();
  }

  try {
    // Register zoom plugin, assuming Chart.js and the plugin are loaded from the HTML
    if (window.Chart && window.ChartZoom) {
      window.Chart.register(window.ChartZoom);
      console.log("[App] Chart libraries found and zoom plugin registered.");
    } else {
      throw new Error("Chart.js or chartjs-plugin-zoom is missing. Ensure they are loaded in the HTML.");
    }

    // Get FFlag data
    const { labels, data } = await fetchData();

    // Initialize chart
    const canvas = document.getElementById("myChart");
    if (!canvas) throw new Error("Canvas not found");

    if (window.myChart) {
      window.myChart.destroy();
    }

    window.myChart = new Chart(canvas.getContext("2d"), {
      type: "line",
      data: {
        labels,
        datasets: [{
          label: "FFlag Changes",
          data,
          borderColor: "rgb(75, 192, 192)",
          backgroundColor: "rgba(75, 192, 192, 0.2)",
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
              mode: "xy"
            },
            pan: {
              enabled: true,
              mode: "xy"
            }
          }
        },
        scales: {
          y: { beginAtZero: true }
        }
      }
    });

    console.log("[App] Chart initialized with real FFlag data!");

  } catch (err) {
    console.error("[App] Full fail on chart setup:", err);
    const canvas = document.getElementById("myChart");
    if (canvas) {
      canvas.outerHTML = '<p>Chart load failed — check console for details.</p>';
    }
  }
});
