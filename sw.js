
self.addEventListener('install', e => {
e.waitUntil(
caches.open('fflag-cache').then(cache => {
return cache.addAll([
'/',
'/index.html',
'/summary.json',
'/commits.json',
'/history.json'
]);
})
);
});
self.addEventListener('fetch', e => {
e.respondWith(
caches.match(e.request).then(response => {
return response || fetch(e.request);
})
);
});
