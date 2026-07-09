const CACHE_NAME = "solarvision-v2";

const FILES = [
    "/",
    "/settings",
    "/static/css/style.css",
    "/static/js/dashboard.js",
    "/static/js/settings.js",
    "/static/manifest.json",
    "/static/icons/icon-192.png",
    "/static/icons/icon-512.png"
];

self.addEventListener("install", event => {

    event.waitUntil(

        caches.open(CACHE_NAME)
            .then(cache => cache.addAll(FILES))

    );

});

self.addEventListener("fetch", event => {

    event.respondWith(

        caches.match(event.request)
            .then(response => response || fetch(event.request))

    );

});
