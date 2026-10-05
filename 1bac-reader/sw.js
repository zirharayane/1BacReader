const CACHE_NAME = '1bac-reader-v1';

const STATIC_ASSETS = [
  './',
  './index.html',
  './reader.html',
  './manifest.json',
  './css/main.css',
  './css/reader.css',
  './js/vendor/page-flip.browser.js',
  './js/app.js',
  './js/parser.js',
  './js/inspector.js',
  './js/reader.js',
  './js/sw-register.js',
  './data/boite/chapters.json',
  './data/boite/dictionary.json',
  './data/boite/figures.json',
  './data/boite/detected_figures.json',
  './data/condamne/chapters.json',
  './data/condamne/dictionary.json',
  './data/condamne/figures.json',
  './data/condamne/detected_figures.json',
  './data/antigone/scenes.json',
  './data/antigone/dictionary.json',
  './data/antigone/figures.json',
  './data/antigone/detected_figures.json'
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => {
      console.log('[Service Worker] Caching static assets');
      return cache.addAll(STATIC_ASSETS);
    })
  );
  self.skipWaiting();
});

self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(cacheNames => {
      return Promise.all(
        cacheNames.map(cache => {
          if (cache !== CACHE_NAME) {
            console.log('[Service Worker] Deleting old cache:', cache);
            return caches.delete(cache);
          }
        })
      );
    })
  );
  self.clients.claim();
});

self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request).then(response => {
      if (response) {
        return response; // Serve from cache
      }
      return fetch(event.request).then(networkResponse => {
        if (!networkResponse || networkResponse.status !== 200 || networkResponse.type !== 'basic') {
          return networkResponse;
        }
        const responseToCache = networkResponse.clone();
        caches.open(CACHE_NAME).then(cache => {
          cache.put(event.request, responseToCache);
        });
        return networkResponse;
      });
    })
  );
});
