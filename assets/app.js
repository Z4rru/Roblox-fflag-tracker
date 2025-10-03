document.addEventListener('DOMContentLoaded', async function () {
  async function fetchData() {
    // 'fflag.json' is in the root of gh-pages
    const res = await fetch("fflag.json");
    if (!res.ok) throw new Error("Failed to fetch fflag.json");
    return await res.json();
  }

  // Helper: wait until canvas exists
  function waitForCanvas(id, timeout = 2000) {
    return new Promise((resolve, reject) => {
      const start = Date.now();
      (function check() {
        const el = document.getElementById(id);
        if (el) return resolve(el);
        if (Date.now() - start > timeout) return reject(new Error("Canvas not found"));
        requestAnimationFrame(check);
      })();
    });
  }

  try {
    // Register zoom plugin
    if (window.Chart && window.ChartZoom) {
      window.Chart.register(window.ChartZoom);
      console.log("[App] Chart libraries found and zoom plugin registered.");
    } else {
      throw new Error("Chart.js or chartjs-plugin-zoom is missing. Ensure they are loaded in the HTML.");
    }

    // Get FFlag data
    const { labels, data } = await fetchData();

    // Wait for canvas (fixes race condition with injection/DOM rebuild)
    const canvas = await waitForCanvas("myChart");

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
