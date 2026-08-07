# -*- coding: utf-8 -*-
# Kriterin makale (yazi) sayfasi ureteci — CANLI site sablonuyla esitli.
# Icerir: Consent Mode v2 + AdSense + giris bari (authNav/authnav.js) + cerez.js
#         + og-v2 gorseli + breadcrumb (crumb) + sosyal medya footer.
#
# KULLANIM: cd site && python3 gen_artX.py   (dosya repo kokune yazilir)
# NOT: Bu uretec YALNIZCA yazi/makale sayfalari icindir. index.html, hesaplayici.html,
# gunun-sorusu.html, anket.html ELLE bakimdadir; gen_index/gen_legal/gen_404 canliyla
# birebir ayni degildir, korlemesine calistirma.
import os, json

BASE = os.path.dirname(os.path.abspath(__file__))
# Sosyal medya footer blogu ayri dosyada tutulur (buyuk inline SVG); yayinda servis edilmez.
SOCIAL = open(os.path.join(BASE, '_social.html'), encoding='utf-8').read()

NAV = """<div class="nav"><div class="nav-in">
  <a class="nav-logo" href="/"><img src="/favicon-96.png" alt=""><span class="wm">Kriterin</span></a>
  <span class="sp"></span>
  <a class="lnk home" href="/hesaplayici.html">Hesaplayıcı</a>
  <a class="lnk" href="/yazilar.html">Yazılar</a>
  <span id="authNav"></span>
</div></div>"""

THEME_BTN = ('<button class="theme-btn" id="themeBtn" type="button" title="Temayı değiştir" '
             'aria-label="Temayı değiştir" style="float:right;margin:2px 0 10px 12px">◐</button>')

FOOT = ("""<footer>
  <div style="margin-bottom:10px">
    <a href="/hesaplayici.html">Hesaplayıcı</a><a href="/yazilar.html">Yazılar</a><a href="/hakkimizda.html">Hakkımızda</a>
    <a href="/gizlilik-politikasi.html">Gizlilik</a><a href="/cerez-politikasi.html">Çerezler</a>
    <a href="/kullanim-kosullari.html">Kullanım Koşulları</a><a href="#cerez">Çerez tercihleri</a>
  </div>
  <div>İletişim ve iş birliği: <a href="mailto:kriterincom@gmail.com" style="color:var(--accent)">kriterincom@gmail.com</a></div>
  <div style="margin-top:8px">© 2026 Kriterin · Sonuçlar tahminidir, eğlence ve fikir verme amaçlıdır.</div>
""" + SOCIAL + "</footer>")

ADS = ('<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js'
       '?client=ca-pub-7993571496408496" crossorigin="anonymous"></script>')

CONSENT = """<script>/* Consent Mode v2: onay gelene kadar reklam ve olcum depolamasi kapali. gtag yuklenmeden once calismali. */
window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments)}
(function(){var c="denied";try{if(localStorage.getItem("kriterin_cerez")==="kabul")c="granted"}catch(e){}
gtag("consent","default",{ad_storage:c,ad_user_data:c,ad_personalization:c,analytics_storage:c,wait_for_update:500});})();</script>"""

END = """<script>
(function(){
  var r=document.documentElement, b=document.getElementById('themeBtn');
  b.addEventListener('click',function(){
    var next = r.getAttribute('data-theme')==='dark' ? 'light' : 'dark';
    r.setAttribute('data-theme',next);
    try{localStorage.setItem('kriterin_tema',next);}catch(e){}
  });
})();
</script>
<script>if('serviceWorker' in navigator){window.addEventListener('load',function(){navigator.serviceWorker.register('/sw.js').catch(function(){});});}</script>
<script src="/authnav.js?v=7" defer></script>
<script src="/cerez.js" data-ads defer></script>"""


def _esc(s):
    return s.replace("&", "&amp;").replace('"', "&quot;").replace("<", "&lt;").replace(">", "&gt;")


def article_jsonld(slug, title, desc, ptype, published, modified):
    d = {"@context": "https://schema.org", "@type": ptype,
         "headline": title, "name": title, "description": desc,
         "inLanguage": "tr-TR", "image": "https://kriterin.com/og-v2.png",
         "mainEntityOfPage": {"@type": "WebPage", "@id": f"https://kriterin.com/{slug}"},
         "publisher": {"@type": "Organization", "name": "Kriterin", "url": "https://kriterin.com/",
                       "logo": {"@type": "ImageObject", "url": "https://kriterin.com/favicon-192.png"}}}
    if ptype == "Article":
        d["author"] = {"@type": "Organization", "name": "Kriterin", "url": "https://kriterin.com/"}
        d["datePublished"] = published
        d["dateModified"] = modified
    return '<script type="application/ld+json">' + json.dumps(d, ensure_ascii=False) + '</script>'


def breadcrumb_jsonld(slug, crumb):
    d = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Ana Sayfa", "item": "https://kriterin.com/"},
        {"@type": "ListItem", "position": 2, "name": "Yazılar", "item": "https://kriterin.com/yazilar.html"},
        {"@type": "ListItem", "position": 3, "name": crumb, "item": f"https://kriterin.com/{slug}"}]}
    return '<script type="application/ld+json">' + json.dumps(d, ensure_ascii=False) + '</script>'


def crumb_nav(crumb):
    return ('<nav class="crumb" aria-label="İçerik yolu" style="font-size:13px;color:var(--muted);margin:2px 0 14px">'
            '<a href="/" style="color:var(--muted);text-decoration:none">Ana sayfa</a> › '
            '<a href="/yazilar.html" style="color:var(--muted);text-decoration:none">Yazılar</a> › '
            f'<span>{_esc(crumb)}</span></nav>')


def related_section(related):
    # related: [(slug, baslik, aciklama), ...] ya da None
    if not related:
        return ''
    cards = ''.join(
        f'<a class="card" href="/{s}"><b>{_esc(t)}</b><span>{_esc(d)}</span></a>' for (s, t, d) in related)
    return ('<section aria-label="İlgili yazılar" style="margin-top:36px"><h2>İlgili yazılar</h2>'
            f'<div class="cards">{cards}</div></section>')


def page(slug, title, desc, body, crumb=None, related=None,
         published='2026-07-31', modified='2026-07-31', ptype='Article'):
    """Bir yazi (makale) HTML'i uretip repo kokune yazar."""
    if crumb is None:
        crumb = title
    css = open(os.path.join(BASE, 'sayfa.css'), encoding='utf-8').read()
    html = f'''<!doctype html>
<html lang="tr" data-theme="light">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{_esc(title)} · Kriterin</title>
<meta name="description" content="{_esc(desc)}" />
<link rel="canonical" href="https://kriterin.com/{slug}" />
<meta property="og:type" content="article" />
<meta property="og:site_name" content="Kriterin" />
<meta property="og:locale" content="tr_TR" />
<meta property="og:url" content="https://kriterin.com/{slug}" />
<meta property="og:title" content="{_esc(title)}" />
<meta property="og:description" content="{_esc(desc)}" />
<meta property="og:image" content="https://kriterin.com/og-v2.png" />
<meta name="twitter:card" content="summary_large_image" />
<link rel="icon" href="/favicon.ico" sizes="any" />
<link rel="icon" type="image/png" sizes="96x96" href="/favicon-96.png" />
<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png" />
<link rel="manifest" href="/manifest.webmanifest" />
<meta name="theme-color" content="#e0405f" />
<meta name="mobile-web-app-capable" content="yes" />
<meta name="apple-mobile-web-app-capable" content="yes" />
<meta name="apple-mobile-web-app-status-bar-style" content="default" />
<meta name="apple-mobile-web-app-title" content="Kriterin" />
<style>{css}</style>
<script>try{{var t=localStorage.getItem('kriterin_tema');if(t)document.documentElement.setAttribute('data-theme',t);}}catch(e){{}}</script>
{article_jsonld(slug, title, desc, ptype, published, modified)}
{breadcrumb_jsonld(slug, crumb)}
{CONSENT}
{ADS}
</head>
<body>
{NAV}
<div class="wrap">{THEME_BTN}
{crumb_nav(crumb)}
{body}
{related_section(related)}
{FOOT}
</div>
{END}
</body>
</html>'''
    out = os.path.join(BASE, '..', slug)
    open(out, 'w', encoding='utf-8').write(html)
    return slug
