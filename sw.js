const CACHE_NAME = "fflag-cache-v3"; // Bumped for changes
const URLS_TO_CACHE = [
    "./",
    "index.html",
    "summary.json",
    "commits_index.json",
    "assets/app.js",
    "assets/chart.js",
    "assets/chartjs-plugin-zoom.js"
];

// Install: cache local files safely
self.addEventListener("install", (event) => {
  event.waitUntil((async () => {
    try {
      const cache = await caches.open(CACHE_NAME);
      await cache.addAll(URLS_TO_CACHE);
      self.skipWaiting(); // Activate immediately
    } catch (e) {
      console.error('Service worker install error:', e);
    }
  })());
});

// Activate: clean up old caches
self.addEventListener("activate", (event) => {
  event.waitUntil((async () => {
    try {
      const cacheNames = await caches.keys();
      await Promise.all(
        cacheNames
          .filter(name => name !== CACHE_NAME)
          .map(name => caches.delete(name))
      );
      self.clients.claim(); // Take control of pages
    } catch (e) {
      console.error('Service worker activate error:', e);
    }
  })());
});

// Fetch: cache-first with network fallback and offline handling
self.addEventListener("fetch", (event) => {
  const url = new URL(event.request.url);
  // Bypass external Google Fonts (fetch directly with cache fallback)
  if (
    url.origin === "https://fonts.googleapis.com" ||
    url.origin === "https://fonts.gstatic.com"
  ) {
    event.respondWith(
      fetch(event.request, { redirect: 'follow' }).catch(() => caches.match(event.request))
    );
    return;
  }
  // For local assets, cache-first
  event.respondWith((async () => {
    try {
      const cachedResponse = await caches.match(event.request);
      if (cachedResponse) return cachedResponse;
      const fetchResponse = await fetch(event.request, { redirect: 'follow' });
      const cache = await caches.open(CACHE_NAME);
      cache.put(event.request, fetchResponse.clone());
      return fetchResponse;
    } catch (e) {
      console.error('Fetch error:', e);
      return new Response('Offline - Unable to fetch', { status: 503 });
    }
  })());
});
