const CACHE_NAME = "fflag-cache-v1";
const URLS_TO_CACHE = [
    "./",
    "index.html",
    "summary.json",
    "commits_index.json",
    "history.json",
    "assets/app.js",
    "assets/chart.js",
    "assets/chartjs-plugin-zoom.js"
];

// Install: cache local files
self.addEventListener("install", event => {
    event.waitUntil(
        caches.open(CACHE_NAME).then(cache => cache.addAll(URLS_TO_CACHE))
    );
});

// Activate: clean up old caches
self.addEventListener("activate", event => {
    event.waitUntil(
        caches.keys().then(cacheNames => 
            Promise.all(
                cacheNames
                    .filter(name => name !== CACHE_NAME)
                    .map(name => caches.delete(name))
            )
        )
    );
});

// Fetch: respond from cache or network
self.addEventListener("fetch", event => {
    const url = event.request.url;

    // Bypass external Google Fonts
    if (
        url.startsWith("https://fonts.googleapis.com") ||
        url.startsWith("https://fonts.gstatic.com")
    ) {
        event.respondWith(fetch(event.request, { redirect: 'follow' }));
        return;
    }

    // For local assets, use cache first
    event.respondWith(
        caches.match(event.request).then(response => response || fetch(event.request, { redirect: 'follow' }))
    );
});
