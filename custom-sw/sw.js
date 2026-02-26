const CACHE = "fflag-v5";
const SHELL = [
  "./",
  "index.html",
  "manifest.json",
  "assets/app.js",
  "assets/chart.umd.js",
  "assets/hammer.min.js",
  "assets/chartjs-plugin-zoom.js",
  "assets/favicon.ico"
];

self.addEventListener("install", (e) => {
  e.waitUntil(
    caches.open(CACHE)
      .then((c) => c.addAll(SHELL))
      .then(() => self.skipWaiting())
  );
});

self.addEventListener("activate", (e) => {
  e.waitUntil(
    caches.keys()
      .then((ks) => Promise.all(ks.filter((k) => k !== CACHE).map((k) => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener("fetch", (e) => {
  const url = new URL(e.request.url);
  if (url.origin !== location.origin) return;

  if (url.pathname.endsWith(".json")) {
    e.respondWith(
      caches.open(CACHE).then(async (cache) => {
        const cached = await cache.match(e.request);
        const net = fetch(e.request).then((r) => {
          if (r.ok) cache.put(e.request, r.clone());
          return r;
        }).catch(() => null);
        return cached || await net || new Response('{"error":"offline"}', {
          status: 503,
          headers: { "Content-Type": "application/json" }
        });
      })
    );
    return;
  }

  e.respondWith(
    caches.match(e.request).then((cached) => {
      if (cached) return cached;
      return fetch(e.request).then((r) => {
        if (r.ok) {
          const cl = r.clone();
          caches.open(CACHE).then((c) => c.put(e.request, cl));
        }
        return r;
      }).catch(() => {
        if (e.request.mode === "navigate") return caches.match("index.html");
        return new Response("Offline", { status: 503 });
      });
    })
  );
});
