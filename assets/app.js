const canvas = document.getElementById('particleCanvas');
const ctx = canvas.getContext('2d');
let resizeTimeout, animationId, particles = [];

// =============================
// Particle Background
// =============================
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
    animationId = requestAnimationFrame(() => setTimeout(animateParticles, 16));  // Throttled to ~60fps
}

function stopAnimation() {
    cancelAnimationFrame(animationId);
}

window.addEventListener('resize', () => {
    clearTimeout(resizeTimeout);
    resizeTimeout = setTimeout(resizeCanvas, 200);
});

document.addEventListener('visibilitychange', () => {
    if (document.hidden) stopAnimation();
    else if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) animateParticles();
});

document.addEventListener('DOMContentLoaded', () => {
    resizeCanvas();
    generateParticles();
    if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
        animateParticles();
    }
});

// =============================
 // Theme & Contrast Toggle (with persistence)
// =============================
function applyTheme() {
    const theme = localStorage.getItem('theme');
    document.body.classList.remove('light', 'high-contrast');
    if (theme === 'light') {
        document.body.classList.add('light');
    } else if (theme === 'high-contrast') {
        document.body.classList.add('high-contrast');
        stopAnimation();
        canvas.style.display = 'none';
    } else {
        canvas.style.display = 'block';
        if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) animateParticles();
    }
}

document.addEventListener('DOMContentLoaded', () => {
    applyTheme();

    document.getElementById('themeToggle').addEventListener('click', () => {
        if (document.body.classList.contains('light')) {
            localStorage.removeItem('theme');
        } else {
            localStorage.setItem('theme', 'light');
        }
        applyTheme();
    });

    document.getElementById('contrastToggle').addEventListener('click', () => {
        if (document.body.classList.contains('high-contrast')) {
            localStorage.removeItem('theme');
        } else {
            localStorage.setItem('theme', 'high-contrast');
        }
        applyTheme();
    });
});
    import Chart from './assets/chart.js';
    import zoomPlugin from './assets/chartjs-plugin-zoom.min.js'; // <- put the downloaded file here

    // Register the plugin before creating any chart
    Chart.register(zoomPlugin);
// =============================
 // Chart.js Trend Chart
// =============================
document.addEventListener('DOMContentLoaded', async () => {
    const trendChart = document.getElementById("trendChart");
    if (!trendChart) return;

    trendChart.style.display = 'none';
    const loadingP = document.createElement('p');
    loadingP.textContent = 'Loading...';
    trendChart.parentNode.insertBefore(loadingP, trendChart);

    const loadChartData = async () => {
        try {
            const response = await fetch("output/history.json");
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
            loadingP.textContent = 'Error loading chart. Retrying in 5 seconds...';
            setTimeout(loadChartData, 5000);  // Retry optimization
        }
    };

    loadChartData();
});

// =============================
 // Report Rendering
// =============================
const reportContent = document.getElementById('reportContent');
const loadingSpinner = document.getElementById('loadingSpinner');
let globalData = null;
let currentData = [];
let offset = 0;
const limit = 20;

function createCommitCard(commit) {
    const card = document.createElement('div');
    card.classList.add('commit-card');
    card.setAttribute('aria-label', `Commit: ${commit.header}`);
    const h2 = document.createElement('h2');
    h2.textContent = commit.header;
    card.appendChild(h2);

    Object.entries(commit.grouped).forEach(([groupKey, flags]) => {
        const [typ, cat] = groupKey.split('_');
        const h3 = document.createElement('h3');
        h3.textContent = `${typ} in ${cat}`;
        h3.setAttribute('aria-expanded', 'true');
        h3.setAttribute('aria-label', `${typ} flags in ${cat}`);
        h3.tabIndex = 0;
        h3.setAttribute('role', 'button');
        card.appendChild(h3);

        const ul = document.createElement('ul');
        flags.forEach(f => {
            const li = document.createElement('li');
            li.dataset.freq = f.freq;
            let desc = '';
            if (f.old_value === null && f.new_value !== null) desc = `= ${f.new_value}`;
            else if (f.old_value !== null && f.new_value !== null) desc = `changed from ${f.old_value} to ${f.new_value}`;
            else if (f.old_value !== null && f.new_value === null) desc = `(was ${f.old_value})`;
            li.textContent = `${f.name} ${desc} - Mechanism: ${f.mechanism || "N/A"} - Purpose: ${f.purpose || "N/A"}`;

            if (f.mechanism && f.purpose && !f.mechanism.startsWith('N/A')) {
                const copyBtn = document.createElement('button');
                copyBtn.classList.add('copy-btn');
                copyBtn.dataset.copy = `${f.mechanism || "N/A"} - ${f.purpose || "N/A"}`;
                copyBtn.setAttribute('aria-label', `Copy mechanism and purpose for ${f.name}`);
                copyBtn.textContent = 'Copy';
                li.appendChild(copyBtn);
            }
            ul.appendChild(li);
        });
        ul.style.maxHeight = ul.scrollHeight + 'px';
        card.appendChild(ul);
    });
    return card;
}

async function loadCommits(offset=0, limit=20) {
    const dataToUse = currentData.length > 0 ? currentData : globalData.report;
    const slice = dataToUse.slice(offset, offset + limit);
    if (slice.length === 0) return false;
    const fragment = document.createDocumentFragment();
    slice.forEach(commit => {
        fragment.appendChild(createCommitCard(commit));
    });
    reportContent.appendChild(fragment);
    return true;
}

// =============================
// Filters & Data Loader
// =============================
function applyFilters() {
    if (!globalData) {
        reportContent.innerHTML = '<p class="error-message">Error: Data not loaded.</p>';
        return;
    }
    const cat = document.getElementById('categoryFilter').value;
    const query = document.getElementById('searchInput').value.toLowerCase();
    const sortBy = document.getElementById('sortSelect').value;

    let filtered = globalData.report;
    if (cat || query) {
        filtered = globalData.report.map(commit => {
            const grouped = {};
            Object.entries(commit.grouped).forEach(([groupKey, flags] ) => {
                const [typ, category] = groupKey.split('_');
                if (cat && category !== cat) return;
                let matches = flags;
                if (query) {
                    matches = flags.filter(f =>
                        f.name.toLowerCase().includes(query) ||
                        (f.mechanism && f.mechanism.toLowerCase().includes(query)) ||
                        (f.purpose && f.purpose.toLowerCase().includes(query))
                    );
                }
                if (matches.length > 0) grouped[groupKey] = matches;
            });
            return Object.keys(grouped).length ? { ...commit, grouped } : null;
        }).filter(Boolean);
    } else {
        // merge all items for "All Categories"
        const allItems = [];
        globalData.report.forEach(commit => {
            Object.values(commit.grouped).forEach(arr => allItems.push(...arr));
        });
        filtered = [{ header: 'All Changes', grouped: {'All_All': allItems} }];
    }

    filtered.forEach(commit => {
        Object.values(commit.grouped).forEach(flags => {
            flags.sort((a, b) => {
                if (sortBy === 'freq') return b.freq - a.freq;
                return a.name.localeCompare(b.name);
            });
        });
    });

    currentData = filtered;
    reportContent.innerHTML = '';
    offset = 0;
    if (currentData.length === 0) {
        reportContent.innerHTML = `<p>No recent flag changes in the last ${globalData.days} days.</p>`;
    } else {
        loadCommits(offset, limit);
        offset += limit;
    }
}

async function loadReportData() {
    try {
        const summaryResponse = await fetch('output/summary.json');
        if (!summaryResponse.ok) throw new Error('Failed to load summary.json');
        const data = await summaryResponse.json();
        globalData = data;

        document.getElementById('flags-added').textContent = data.added_total;
        document.getElementById('flags-changed').textContent = data.changed_total;
        document.getElementById('flags-removed').textContent = data.removed_total;
        document.getElementById('net-changes').textContent = data.net_changes;
        const percent = data.percent_change.toFixed(2);
        document.getElementById('percent-change').textContent = percent;
        const percentBadge = document.querySelector('.percent');
        percentBadge.classList.remove('positive', 'negative');
        if (percent > 0) percentBadge.classList.add('positive');
        else if (percent < 0) percentBadge.classList.add('negative');

        document.getElementById('historical-added').textContent = data.total_historical_added;
        document.getElementById('historical-changed').textContent = data.total_historical_changed;
        document.getElementById('historical-removed').textContent = data.total_historical_removed;
        document.getElementById('last-run').textContent = data.last_run;

        const summaryTableBody = document.querySelector('#summaryTable tbody');
        summaryTableBody.innerHTML = '';
        for (let cat in data.summary) {
            const s = data.summary[cat];
            summaryTableBody.innerHTML += `<tr><td>${cat}</td><td>${s.added}</td><td>${s.changed}</td><td>${s.removed}</td><td>${s.added + s.changed + s.removed}</td></tr>`;
        }

        globalData.report = [];
        const indexRes = await fetch("output/commits_index.json");
        if (!indexRes.ok) throw new Error('Failed to load commits_index.json');
        const commitFiles = await indexRes.json();
        for (const file of commitFiles) {
            const res = await fetch(file);
            if (!res.ok) {
                console.error(`Failed to load ${file}`);
                reportContent.innerHTML += '<p class="error-message">Failed to load some report data. Check console for details.</p>';
                break;
            }
            const chunk = await res.json();
            globalData.report = globalData.report.concat(chunk);
        }

        loadingSpinner.style.display = 'none';
        applyFilters();

        reportContent.addEventListener('click', e => {
            if (e.target.tagName === 'H3') {
                const ul = e.target.nextElementSibling;
                if (ul && ul.tagName === 'UL') {
                    const expanded = e.target.getAttribute('aria-expanded') === 'true';
                    ul.style.maxHeight = expanded ? '0px' : ul.scrollHeight + 'px';
                    e.target.setAttribute('aria-expanded', !expanded);
                }
            } else if (e.target.classList.contains('copy-btn')) {
                navigator.clipboard.writeText(e.target.dataset.copy).then(() => {
                    e.target.textContent = 'Copied!';
                    setTimeout(() => e.target.textContent = 'Copy', 2000);
                });
            }
        });

        reportContent.addEventListener('keydown', e => {
            if (e.key === 'Enter' || e.key === ' ') {
                const h = e.target;
                if (h.tagName === 'H3') h.click();
            }
        });

    } catch (error) {
        console.error('Error loading report:', error);
        loadingSpinner.style.display = 'none';
        reportContent.innerHTML = '<p class="error-message">Error loading report data. Please try again later or run updateff.py to generate files.</p>';
    }
}

function debounce(func, delay) {
    let timeout;
    return (...args) => {
        clearTimeout(timeout);
        timeout = setTimeout(() => func(...args), delay);
    };
}

loadReportData();
document.getElementById('searchInput').addEventListener('input', debounce(applyFilters, 300));
document.getElementById('categoryFilter').addEventListener('change', applyFilters);
document.getElementById('sortSelect').addEventListener('change', applyFilters);

reportContent.addEventListener("scroll", debounce(() => {
    if (reportContent.scrollHeight - reportContent.scrollTop - reportContent.clientHeight < 200) {
        loadCommits(offset, limit);
        offset += limit;
    }
}, 100));

// =============================
// Export + Auto-refresh + SW
// =============================
document.getElementById('exportCSV').addEventListener('click', () => {
    if (!globalData) return;
    let csv = 'Commit,Type,Category,Flag,Old Value,New Value,Mechanism,Purpose,Frequency\n';
    globalData.report.forEach(commit => {
        Object.entries(commit.grouped).forEach(([groupKey, flags]) => {
            const [typ, cat] = groupKey.split('_');
            flags.forEach(f => {
                const escapeCsvField = (str) => `"${(str || '').toString().replace(/"/g, '""')}"`;
                csv += `${escapeCsvField(commit.header)},${escapeCsvField(typ)},${escapeCsvField(cat)},${escapeCsvField(f.name)},${escapeCsvField(f.old_value)},${escapeCsvField(f.new_value)},${escapeCsvField(f.mechanism || 'N/A')},${escapeCsvField(f.purpose || 'N/A')},${escapeCsvField(f.freq)}\n`;
            });
        });
    });
    download('fflag_report.csv', csv);
});

document.getElementById('exportJSON').addEventListener('click', () => {
    if (!globalData) return;
    const fullData = { ...globalData, report: globalData.report };
    download('fflag_report.json', JSON.stringify(fullData, null, 2));
});

function download(filename, text) {
    const a = document.createElement('a');
    a.href = URL.createObjectURL(new Blob([text], { type: 'text/plain' }));
    a.download = filename;
    a.click();
}

setInterval(() => {
    fetch('output/summary.json?ts=' + Date.now()).then(r => r.json()).then(newData => {
        if (globalData && newData.last_run !== globalData.last_run) {
            location.reload();
        }
    }).catch(() => { });
}, 60000);

if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register('sw.js').catch(error => {
        console.error('Service Worker registration failed:', error);
    });
}

window.onerror = function (message, source, lineno, colno, error) {
    if (/ERR_BLOCKED_BY_CLIENT/.test(error?.message)) {
        localStorage.setItem('errorLog', JSON.stringify({
            message, source, lineno, colno, timestamp: new Date().toISOString()
        }));
    }
};
