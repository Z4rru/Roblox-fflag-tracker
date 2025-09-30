// Error Handling Global
window.onerror = function (message, source, lineno, colno, error) {
    console.error(`Grok Debug: ${message} at ${source}:${lineno}:${colno}`);
    if (/ERR_BLOCKED_BY_CLIENT|MIME|CORS/.test(error?.message)) {
        alert('Adblocker or extension blocking CDN—disable for jsDelivr or use local assets!');
        localStorage.setItem('errorLog', JSON.stringify({ message, source, lineno, colno, timestamp: new Date().toISOString() }));
    }
};

// Particle Background (Optimized)
const canvas = document.getElementById('particleCanvas');
const ctx = canvas.getContext('2d');
let animationId, particles = [];
function resizeCanvas() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
}
function generateParticles() {
    particles = Array.from({ length: 20 }, () => ({
        x: Math.random() * canvas.width,
        y: Math.random() * canvas.height,
        r: Math.random() * 2 + 1,
        dx: (Math.random() - 0.5) / 2,
        dy: (Math.random() - 0.5) / 2,
        color: `rgba(${Math.floor(Math.random() * 50 + 200)}, 255, 255, 0.15)`
    }));
}
function animateParticles() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    particles.forEach(p => {
        p.x += p.dx;
        p.y += p.dy;
        if (p.x < 0 || p.x > canvas.width) p.dx *= -1;
        if (p.y < 0 || p.y > canvas.height) p.dy *= -1;
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
        ctx.fillStyle = p.color;
        ctx.fill();
    });
    animationId = requestAnimationFrame(animateParticles); // Native 60fps
}
function stopAnimation() {
    cancelAnimationFrame(animationId);
}
window.addEventListener('resize', () => resizeCanvas());
document.addEventListener('visibilitychange', () => {
    if (document.hidden) stopAnimation();
    else if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) animateParticles();
});
document.addEventListener('DOMContentLoaded', () => {
    const preloadLink = document.querySelector('link[rel="preload"][as="style"]');
    if (preloadLink) preloadLink.rel = 'stylesheet';
    resizeCanvas();
    generateParticles();
    if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) animateParticles();
});

// Theme & Contrast Toggle (with Cookie Fallback)
function applyTheme() {
    let theme = localStorage.getItem('theme') || (document.cookie.match(/theme=([^;]*)/)?.[1] || '');
    document.body.classList.remove('light', 'high-contrast');
    if (theme === 'light') document.body.classList.add('light');
    else if (theme === 'high-contrast') {
        document.body.classList.add('high-contrast');
        stopAnimation();
        canvas.style.display = 'none';
    } else {
        canvas.style.display = 'block';
        if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) animateParticles();
    }
}
function setTheme(theme) {
    localStorage.setItem('theme', theme);
    document.cookie = `theme=${theme}; path=/; max-age=31536000`;
    applyTheme();
}
document.addEventListener('DOMContentLoaded', () => {
    applyTheme();
    document.getElementById('themeToggle').addEventListener('click', () => {
        setTheme(document.body.classList.contains('light') ? '' : 'light');
    });
    document.getElementById('contrastToggle').addEventListener('click', () => {
        setTheme(document.body.classList.contains('high-contrast') ? '' : 'high-contrast');
    });
});

// Chart.js Trend Chart (with Local Fallback)
document.addEventListener('DOMContentLoaded', async () => {
    const trendChart = document.getElementById("trendChart");
    if (!trendChart) return;
    trendChart.style.display = 'none';
    const loadingP = document.createElement('p');
    loadingP.textContent = 'Loading...';
    trendChart.parentNode.insertBefore(loadingP, trendChart);
    let retries = 0;
    const maxRetries = 5;
    const loadChartData = async () => {
        try {
            let Chart, zoomPlugin;
            try {
                // Try CDN ESM
                ({ Chart, registerables: registerables } = await import('https://cdn.jsdelivr.net/npm/chart.js@4.5.0/dist/chart.esm.js'));
                Chart.register(...registerables);
                ({ default: zoomPlugin } = await import('https://cdn.jsdelivr.net/npm/chartjs-plugin-zoom@2.0.1/dist/chartjs-plugin-zoom.esm.min.js'));
            } catch (cdnError) {
                console.warn('CDN failed, falling back to local assets');
                const chartScript = document.createElement('script');
                chartScript.src = 'assets/chart.js'; // Assume local min.js
                document.head.appendChild(chartScript);
                await new Promise(resolve => chartScript.onload = resolve);
                const zoomScript = document.createElement('script');
                zoomScript.src = 'assets/chartjs-plugin-zoom.js';
                document.head.appendChild(zoomScript);
                await new Promise(resolve => zoomScript.onload = resolve);
                Chart = window.Chart;
                zoomPlugin = window.zoomPlugin;
            }
            Chart.register(zoomPlugin);
            const response = await fetch("history.json");
            if (!response.ok) throw new Error('Failed to load history.json');
            const data = await response.json();
            if (!data || data.length === 0) {
                loadingP.textContent = 'No history data yet.';
                trendChart.remove();
                return;
            }
            const ctx = trendChart.getContext("2d");
            new Chart(ctx, {
                type: 'line',
                data: {
                    labels: data.map(d => d.date),
                    datasets: [
                        { label: 'Added', data: data.map(d => d.added || 0), borderColor: '#34d399', backgroundColor: 'rgba(52,211,153,0.2)', fill: true, tension: 0.4 },
                        { label: 'Changed', data: data.map(d => d.changed || 0), borderColor: '#60a5fa', backgroundColor: 'rgba(96,165,250,0.2)', fill: true, tension: 0.4 },
                        { label: 'Removed', data: data.map(d => d.removed || 0), borderColor: '#f87171', backgroundColor: 'rgba(248,113,113,0.2)', fill: true, tension: 0.4 }
                    ]
                },
                options: {
                    responsive: true,
                    plugins: {
                        legend: { position: 'top' },
                        zoom: {
                            zoom: { wheel: { enabled: true }, pinch: { enabled: true }, mode: 'x' },
                            pan: { enabled: true, mode: 'x' }
                        },
                        tooltip: { callbacks: { label: ctx => `${ctx.dataset.label}: ${ctx.raw}` } }
                    },
                    interaction: { mode: 'nearest', axis: 'x', intersect: false }
                }
            });
            loadingP.remove();
            trendChart.style.display = '';
        } catch (error) {
            console.error('Error loading chart:', error);
            if (retries < maxRetries) {
                retries++;
                loadingP.textContent = `Error loading chart. Retrying (${retries}/${maxRetries}) in ${retries * 2} seconds... (Disable adblockers!)`;
                setTimeout(loadChartData, retries * 2000); // Exponential backoff
            } else {
                loadingP.textContent = 'Failed after retries. Disable adblocker or use local JS files.';
            }
        }
    };
    loadChartData();
});

// Debug Mode Toggle
document.addEventListener('keydown', e => {
    if (e.ctrlKey && e.shiftKey && e.key === 'D') {
        console.log('Grok Raw Debug: Dumping globalData', globalData); // Raw, no filters
        alert('Debug mode activated—check console for raw logs!');
    }
});

// Service Worker Registration (Add this to app.js if SW is not separate)
if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
        navigator.serviceWorker.register('/sw.js')
            .then(reg => console.log('Service Worker registered:', reg))
            .catch(err => console.error('Service Worker registration failed:', err));
    });
}
