
const CACHE_NAME = "fflag-cache-v1";
const URLS_TO_CACHE = [
    "./",
    "index.html",
    "summary.json",
    "commits.json",
    "history.json",
    "assets/app.js"
];

self.addEventListener("install", event => {
    event.waitUntil(
        caches.open(CACHE_NAME).then(cache => cache.addAll(URLS_TO_CACHE))
    );
});

self.addEventListener("fetch", event => {
    event.respondWith(
        caches.match(event.request).then(response => response || fetch(event.request))
    );
});
