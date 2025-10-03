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

  async function fetchData() {
    const res = await fetch("output/fflag.json");
    if (!res.ok) throw new Error("Failed to fetch fflag.json");
    return await res.json();
  }

  try {
    // Load dependencies (via jsDelivr to satisfy CSP)
    await loadScript("https://cdn.jsdelivr.net/npm/hammerjs@2.0.8/hammer.min.js");
    await loadScript("https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.js");
    await loadScript("https://cdn.jsdelivr.net/npm/chartjs-plugin-zoom@2.2.0/dist/chartjs-plugin-zoom.umd.min.js");

    console.log("[App] Libraries loaded successfully");

    // Register zoom plugin
    if (window.Chart && window.ChartZoom) {
      window.Chart.register(window.ChartZoom);
    } else {
      throw new Error("Chart or ChartZoom missing after load");
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
      canvas.outerHTML = '<p>Chart load failed — check console. [Static fallback here]</p>';
    }
  }
});
