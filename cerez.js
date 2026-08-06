/* Çerez onayı — tüm sayfalarda ortak.
 *
 * Reklam betiği (adsbygoogle) sayfa HTML'inde YOKTUR; yalnızca kullanıcı
 * "Kabul et" dediğinde buradan enjekte edilir. Reddedildiğinde ya da henüz
 * seçim yapılmadığında hiç yüklenmez.
 *
 * Analytics tarafında Google Consent Mode v2 kullanılır: varsayılan "denied"
 * (çerezsiz, kimliksiz ölçüm), onay verilince "granted"a yükseltilir.
 * Varsayılanlar sayfa <head>'inde, gtag yüklenmeden önce set edilir —
 * bu dosya defer ile geldiği için orayı burası yapamaz.
 *
 * Bandı da bu dosya çizer; sayfalarda ayrı işaretleme gerekmez.
 * "#cerez" adresi (footer'daki "Çerez tercihleri") her sayfada tercihleri
 * yeniden açar.
 */
(function () {
  var KEY = 'kriterin_cerez';
  var PUB = 'ca-pub-7993571496408496';

  function oku() { try { return localStorage.getItem(KEY); } catch (e) { return null; } }
  function yaz(v) { try { localStorage.setItem(KEY, v); } catch (e) {} }
  function sil() { try { localStorage.removeItem(KEY); } catch (e) {} }
  function gt() { if (typeof window.gtag === 'function') window.gtag.apply(null, arguments); }

  // Reklam yalnızca bunu isteyen sayfalarda: <script src="/cerez.js" data-ads defer>
  // Anket ve açılış sayfasında reklam yok, onay verilse bile yüklenmemeli.
  var etiket = document.querySelector('script[src="/cerez.js"]');
  var reklamIster = !!(etiket && etiket.hasAttribute('data-ads'));

  // ---- reklam betiği: yalnızca onaydan sonra ----
  var reklamVar = false;
  function reklamYukle() {
    if (reklamVar || !reklamIster) return;
    reklamVar = true;
    var s = document.createElement('script');
    s.async = true;
    s.crossOrigin = 'anonymous';
    s.src = 'https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=' + PUB;
    (document.head || document.documentElement).appendChild(s);
  }

  function onayla() {
    gt('consent', 'update', {
      ad_storage: 'granted', ad_user_data: 'granted',
      ad_personalization: 'granted', analytics_storage: 'granted'
    });
    reklamYukle();
  }

  // Sayfa açılışında zaten onay varsa reklamı hemen getir
  if (oku() === 'kabul') onayla();

  // ---- band ----
  if (!document.getElementById('kr-cerez-css')) {
    var st = document.createElement('style');
    st.id = 'kr-cerez-css';
    st.textContent =
      '.kr-cerez{position:fixed;left:12px;right:12px;bottom:12px;z-index:9999;max-width:760px;margin:0 auto;' +
      'background:var(--surface,#fff);color:var(--ink,#231a20);border:1px solid var(--line,#e8e0e1);' +
      'border-radius:14px;padding:14px 16px;box-shadow:0 10px 34px rgba(0,0,0,.18);' +
      'display:flex;flex-wrap:wrap;gap:10px 16px;align-items:center;font-size:13.5px;line-height:1.5}' +
      '.kr-cerez[hidden]{display:none}' +
      '.kr-cerez p{margin:0;flex:1 1 320px}' +
      '.kr-cerez a{color:var(--accent,#e0405f)}' +
      '.kr-cerez .kr-btns{display:flex;gap:8px;flex:0 0 auto;margin-left:auto}' +
      '.kr-cerez button{cursor:pointer;font:inherit;font-weight:700;padding:9px 16px;border-radius:10px;' +
      'border:1px solid var(--line,#e8e0e1);background:var(--surface-2,#faf7f6);color:var(--ink,#231a20)}' +
      '.kr-cerez button.kr-ok{background:var(--accent,#e0405f);border-color:var(--accent,#e0405f);color:#fff}' +
      '.kr-cerez button:focus-visible{outline:2px solid var(--accent,#e0405f);outline-offset:2px}' +
      '@media(max-width:520px){.kr-cerez .kr-btns{width:100%;margin-left:0}.kr-cerez button{flex:1}}';
    document.head.appendChild(st);
  }

  var bar = document.createElement('div');
  bar.className = 'kr-cerez';
  bar.id = 'krCerez';
  bar.setAttribute('role', 'dialog');
  bar.setAttribute('aria-label', 'Çerez tercihleri');
  bar.hidden = true;
  bar.innerHTML =
    '<p>Bu sitede deneyimi iyileştirmek, trafiği ölçmek ve reklamları kişiselleştirmek için çerezler ' +
    'kullanılıyor. Reddedersen reklam ve ölçüm çerezleri yüklenmez. Ayrıntılar için ' +
    '<a href="/cerez-politikasi.html">Çerez Politikası</a> ve ' +
    '<a href="/gizlilik-politikasi.html">Gizlilik Politikası</a> sayfalarına bakabilirsin.</p>' +
    '<div class="kr-btns"><button type="button" data-ck="ret">Reddet</button>' +
    '<button type="button" class="kr-ok" data-ck="kabul">Kabul et</button></div>';
  document.body.appendChild(bar);

  function sec(v) {
    yaz(v);
    bar.hidden = true;
    if (v === 'kabul') onayla();
    gt('event', 'cerez_secim', { secim: v });
  }
  bar.addEventListener('click', function (e) {
    var b = e.target.closest('[data-ck]');
    if (b) sec(b.getAttribute('data-ck'));
  });

  function tercihleriAc() { sil(); bar.hidden = false; }

  // Footer'daki "Çerez tercihleri" bağlantısı her sayfada çalışsın
  document.addEventListener('click', function (e) {
    var a = e.target.closest('a[href="#cerez"], a[href="/#cerez"], #ckReset');
    if (!a) return;
    e.preventDefault();
    tercihleriAc();
  });
  window.addEventListener('hashchange', function () {
    if (location.hash === '#cerez') tercihleriAc();
  });

  if (location.hash === '#cerez') tercihleriAc();
  else if (!oku()) setTimeout(function () { bar.hidden = false; }, 1000);
})();
