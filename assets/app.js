const canvas = document.getElementById('particleCanvas');
const ctx = canvas.getContext('2d');
let resizeTimeout, animationId, particles = [];

function resizeCanvas() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
}

function generateParticles() {
    particles = Array.from({length: 30}, () => ({
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
    animationId = requestAnimationFrame(animateParticles);
}

function stopAnimation() {
    cancelAnimationFrame(animationId);
}

resizeCanvas();
generateParticles();
if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    animateParticles();
}

window.addEventListener('resize', () => {
    clearTimeout(resizeTimeout);
    resizeTimeout = setTimeout(resizeCanvas, 200);
});

document.addEventListener('visibilitychange', () => {
    if (document.hidden) stopAnimation();
    else if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) animateParticles();
});

document.getElementById('themeToggle').addEventListener('click', () => {
    document.body.classList.toggle('light');
    if (document.body.classList.contains('high-contrast')) {
        document.body.classList.remove('high-contrast');
    }
});

document.getElementById('contrastToggle').addEventListener('click', () => {
    document.body.classList.toggle('high-contrast');
    if (document.body.classList.contains('light')) {
        document.body.classList.remove('light');
    }
    if (document.body.classList.contains('high-contrast')) {
        stopAnimation();
        canvas.style.display = 'none';
    } else {
        canvas.style.display = 'block';
        if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) animateParticles();
    }
});

fetch("history.json").then(r => r.json()).then(data => {
    if (data.length === 0) {
        document.getElementById("trendChart").parentNode.innerHTML = '<p>No history data yet.</p>';
        return;
    }
    const ctx = document.getElementById("trendChart").getContext("2d");
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: data.map(d => d.date),
            datasets: [
                {label: 'Added', data: data.map(d => d.added), borderColor: '#34d399', backgroundColor: 'rgba(52,211,153,0.2)', fill: true, tension: 0.4},
                {label: 'Changed', data: data.map(d => d.changed || 0), borderColor: '#60a5fa', backgroundColor: 'rgba(96,165,250,0.2)', fill: true, tension: 0.4},
                {label: 'Removed', data: data.map(d => d.removed), borderColor: '#f87171', backgroundColor: 'rgba(248,113,113,0.2)', fill: true, tension: 0.4}
            ]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {position: 'top'},
                zoom: {zoom: {wheel: {enabled: true}, pinch: {enabled: true}, mode: 'x'}, pan: {enabled: true, mode: 'x'}},
                tooltip: {callbacks: {label: (ctx) => `${ctx.dataset.label}: ${ctx.raw}`}}
            },
            interaction: {mode: 'nearest', axis: 'x', intersect: false}
        }
    });
}).catch(error => {
    console.error('Error loading history:', error);
    document.getElementById("trendChart").parentNode.innerHTML = '<p class="error-message">Error loading history data.</p>';
});

const reportContent = document.getElementById('reportContent');
const loadingSpinner = document.getElementById('loadingSpinner');
let globalData = null;
let currentData = [];
let virtualItems = [];
const itemsPerPage = 10;

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
        h3.style.cursor = 'pointer';
        h3.setAttribute('aria-expanded', 'true');
        h3.setAttribute('aria-label', `${typ} flags in ${cat}`);
        h3.tabIndex = 0;
        h3.role = 'button';
        card.appendChild(h3);
        const ul = document.createElement('ul');
        flags.forEach(f => {
            const li = document.createElement('li');
            li.dataset.freq = f.freq;
            let desc = '';
            if (f.old_value === null && f.new_value !== null) {
                desc = `= ${f.new_value}`;
            } else if (f.old_value !== null && f.new_value !== null) {
                desc = `changed from ${f.old_value} to ${f.new_value}`;
            } else if (f.old_value !== null && f.new_value === null) {
                desc = `(was ${f.old_value})`;
            }
            li.textContent = `${f.name} ${desc}`;
            if (f.mechanism && f.purpose && !f.mechanism.startsWith('N/A')) {
                li.textContent += " - Mechanism: " + (f.mechanism || "N/A").replace(/\n/g," ").replace(/"/g,"'") +
                                  " - Purpose: " + (f.purpose || "N/A").replace(/\n/g," ").replace(/"/g,"'");
                const copyBtn = document.createElement('button');
                copyBtn.classList.add('copy-btn');
                copyBtn.dataset.copy = (f.mechanism + " - " + f.purpose).replace(/\n/g," ").replace(/"/g,"'");
                copyBtn.setAttribute('aria-label', `Copy mechanism and purpose for ${f.name}`);
                copyBtn.textContent = 'Copy';
                li.appendChild(copyBtn);
            } else {
                li.textContent += ` - Mechanism: N/A - Purpose: N/A`;
            }
            ul.appendChild(li);
        });
        ul.style.maxHeight = ul.scrollHeight + 'px';
        card.appendChild(ul);
    });
    return card;
}

function loadVirtualItems(startIndex, endIndex) {
    const fragment = document.createDocumentFragment();
    const itemsToRender = virtualItems.slice(startIndex, endIndex);
    itemsToRender.forEach(item => {
        if (!item.element) {
            item.element = createCommitCard(item.commit);
        }
        fragment.appendChild(item.element);
    });
    reportContent.appendChild(fragment);
}

function updateVirtualScroll() {
    const scrollTop = reportContent.scrollTop;
    const containerHeight = reportContent.clientHeight;
    const totalHeight = virtualItems.length * 100; // Estimate item height
    reportContent.style.height = `${totalHeight}px`;
    const startIndex = Math.floor(scrollTop / 100);
    const endIndex = Math.min(startIndex + Math.ceil(containerHeight / 100) + 1, virtualItems.length);
    reportContent.innerHTML = '';
    loadVirtualItems(startIndex, endIndex);
    const paddingTop = startIndex * 100;
    reportContent.style.paddingTop = `${paddingTop}px`;
}

function setupVirtualScroll(data) {
    virtualItems = data.map(commit => ({ commit, element: null }));
    reportContent.innerHTML = '';
    reportContent.style.overflowY = 'auto';
    reportContent.style.position = 'relative';
    updateVirtualScroll();
    reportContent.addEventListener('scroll', updateVirtualScroll);
}

function debounce(func, delay) {
    let timeout;
    return (...args) => {
        clearTimeout(timeout);
        timeout = setTimeout(() => func(...args), delay);
    };
}

function applyFilters() {
    if (!globalData) {
        reportContent.innerHTML = '<p class="error-message">Error: Data not loaded.</p>';
        return;
    }
    let filtered = globalData.report;
    const cat = document.getElementById('categoryFilter').value;
    const query = document.getElementById('searchInput').value.toLowerCase();
    const sortBy = document.getElementById('sortSelect').value;
    if (cat || query) {
        filtered = globalData.report.map(commit => {
            const grouped = {};
            Object.entries(commit.grouped).forEach(([groupKey, flags]) => {
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
            return Object.keys(grouped).length ? {...commit, grouped} : null;
        }).filter(Boolean);
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
    if (currentData.length === 0) {
        reportContent.innerHTML = `<p>No recent flag changes in the last ${globalData.days} days.</p>`;
        reportContent.style.height = 'auto';
        reportContent.style.paddingTop = '0';
        reportContent.removeEventListener('scroll', updateVirtualScroll);
    } else {
        setupVirtualScroll(currentData);
    }
}

async function loadReportData() {
    try {
        const summaryResponse = await fetch('summary.json');
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
        if (percent > 0) percentBadge.classList.add('positive');
        else if (percent < 0) percentBadge.classList.add('negative');
        document.getElementById('historical-added').textContent = data.total_historical_added;
        document.getElementById('historical-changed').textContent = data.total_historical_changed;
        document.getElementById('historical-removed').textContent = data.total_historical_removed;
        document.getElementById('last-run').textContent = data.last_run;
        const summaryTable = document.getElementById('summaryTable');
        let tableHtml = '<tr><th>Category</th><th>Added</th><th>Changed</th><th>Removed</th></tr>';
        for (let cat in data.summary) {
            const s = data.summary[cat];
            tableHtml += `<tr><td>${cat}</td><td>${s.added}</td><td>${s.changed}</td><td>${s.removed}</td></tr>`;
        }
        summaryTable.innerHTML = tableHtml;
        const commitsResponse = await fetch('commits.json');
        if (!commitsResponse.ok) throw new Error('Failed to load commits.json');
        globalData.report = await commitsResponse.json();
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
        reportContent.innerHTML = '<p class="error-message">Error loading report data. Please try again later.</p>';
    }
}

loadReportData();
document.getElementById('searchInput').addEventListener('input', debounce(applyFilters, 300));
document.getElementById('categoryFilter').addEventListener('change', applyFilters);
document.getElementById('sortSelect').addEventListener('change', applyFilters);
document.getElementById('exportCSV').addEventListener('click', () => {
    if (!globalData) return;
    let csv = 'Commit,Type,Category,Flag,Old Value,New Value,Mechanism,Purpose,Frequency
';
    globalData.report.forEach(commit => {
        Object.entries(commit.grouped).forEach(([groupKey, flags]) => {
            const [typ, cat] = groupKey.split('_');
            flags.forEach(f => {
                csv += `"${commit.header}","${typ}","${cat}","${f.name}","${f.old_value || ''}","${f.new_value || ''}","${f.mechanism || 'N/A'}","${f.purpose || 'N/A'}","${f.freq}"
`;
            });
        });
    });
    download('fflag_report.csv', csv);
});
document.getElementById('exportJSON').addEventListener('click', () => {
    if (!globalData) return;
    const fullData = {...globalData, report: globalData.report};
    download('fflag_report.json', JSON.stringify(fullData, null, 2));
});
function download(filename, text) {
    const a = document.createElement('a');
    a.href = URL.createObjectURL(new Blob([text], {type: 'text/plain'}));
    a.download = filename;
    a.click();
}
setInterval(() => {
    fetch('summary.json?ts=' + Date.now()).then(r => r.json()).then(newData => {
        if (globalData && newData.last_run !== globalData.last_run) {
            location.reload();
        }
    }).catch(() => {});
}, 60000);
if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register('sw.js').catch(error => {
        console.error('Service Worker registration failed:', error);
    });
}
