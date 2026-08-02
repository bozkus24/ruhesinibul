/* Kriterin service worker — installability + çevrimdışı yedek.
   Strateji: yalnızca aynı-köken HTML gezinmeleri için AĞ-ÖNCELİKLİ.
   Çevrimiçiyken her zaman taze içerik gelir (bayat sayfa riski yok).
   Reklam/analitik gibi üçüncü-taraf ve varlık istekleri dokunulmadan geçer. */
const CACHE = 'kriterin-v1';

self.addEventListener('install', function () {
  self.skipWaiting();
});

self.addEventListener('activate', function (event) {
  event.waitUntil((async function () {
    const keys = await caches.keys();
    await Promise.all(keys.filter(function (k) { return k !== CACHE; }).map(function (k) { return caches.delete(k); }));
    await self.clients.claim();
  })());
});

self.addEventListener('fetch', function (event) {
  const req = event.request;
  if (req.method !== 'GET') return;
  let url;
  try { url = new URL(req.url); } catch (e) { return; }
  if (url.origin !== self.location.origin) return;   // üçüncü taraf: karışma
  if (req.mode !== 'navigate') return;               // yalnızca sayfa gezinmeleri
  event.respondWith((async function () {
    try {
      const net = await fetch(req);
      try { (await caches.open(CACHE)).put(req, net.clone()); } catch (e) {}
      return net;
    } catch (err) {
      const cached = await caches.match(req);
      if (cached) return cached;
      const home = await caches.match('/');
      if (home) return home;
      throw err;
    }
  })());
});
