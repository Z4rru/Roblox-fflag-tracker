const CACHE_NAME = "fflag-cache-v2"; // Bumped version for fresh cache
const URLS_TO_CACHE = [
    "./",
    "index.html",
    "summary.json",
    "commits_index.json",
    "history.json",
    "assets/app.js",
    "assets/chart.js", // Local fallback
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

// Fetch: respond from cache or network with offline fallback
self.addEventListener("fetch", event => {
    const url = event.request.url;
    // Bypass external Google Fonts (both APIs and static)
    if (
        url.startsWith("https://fonts.googleapis.com") ||
        url.startsWith("https://fonts.gstatic.com")
    ) {
        event.respondWith(fetch(event.request, { redirect: 'follow' }).catch(() => caches.match(event.request)));
        return;
    }
    // For local assets, use cache first with network fallback and offline handling
    event.respondWith(
        caches.match(event.request).then(response => {
            return response || fetch(event.request, { redirect: 'follow' }).then(fetchRes => {
                return caches.open(CACHE_NAME).then(cache => {
                    cache.put(event.request, fetchRes.clone());
                    return fetchRes;
                });
            }).catch(() => {
                console.warn(`Grok Debug: Offline fallback for ${url}`);
                return new Response('Offline - Cached content unavailable', { status: 503 });
            });
        })
    );
});
