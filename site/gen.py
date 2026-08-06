# -*- coding: utf-8 -*-
import os

NAV = '''<div class="nav"><div class="nav-in">
  <a class="nav-logo" href="/"><img src="/favicon-96.png" alt=""><span class="wm">Kriterin</span></a>
  <span class="sp"></span>
  <a class="lnk home" href="/">Hesaplayıcı</a>
  <a class="lnk" href="/yazilar.html">Yazılar</a>
  <a class="lnk" href="/hakkimizda.html">Hakkımızda</a>
  <button class="theme-btn" id="themeBtn" type="button" title="Temayı değiştir" aria-label="Temayı değiştir">◐</button>
</div></div>'''

FOOT = '''<footer>
  <div style="margin-bottom:10px">
    <a href="/">Hesaplayıcı</a><a href="/yazilar.html">Yazılar</a><a href="/hakkimizda.html">Hakkımızda</a>
    <a href="/gizlilik-politikasi.html">Gizlilik</a><a href="/cerez-politikasi.html">Çerezler</a>
    <a href="/kullanim-kosullari.html">Kullanım Koşulları</a><a href="/#cerez">Çerez tercihleri</a>
  </div>
  <div>İletişim ve iş birliği: <a href="mailto:kriterincom@gmail.com" style="color:var(--accent)">kriterincom@gmail.com</a></div>
  <div style="margin-top:8px">© 2026 Kriterin · Sonuçlar tahminidir, eğlence ve fikir verme amaçlıdır.</div>
</footer>'''

ADS = '''<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-7993571496408496" crossorigin="anonymous"></script>'''

def jsonld(slug, title, desc, ptype):
    import json
    d = {"@context": "https://schema.org", "@type": ptype,
         "headline": title, "name": title, "description": desc,
         "inLanguage": "tr-TR", "image": "https://kriterin.com/og.png",
         "mainEntityOfPage": {"@type": "WebPage", "@id": f"https://kriterin.com/{slug}"},
         "publisher": {"@type": "Organization", "name": "Kriterin",
                       "url": "https://kriterin.com/",
                       "logo": {"@type": "ImageObject",
                                "url": "https://kriterin.com/favicon-192.png"}}}
    if ptype == "Article":
        d["author"] = {"@type": "Organization", "name": "Kriterin", "url": "https://kriterin.com/"}
        d["datePublished"] = "2026-07-31"
        d["dateModified"] = "2026-07-31"
    return ('<script type="application/ld+json">'
            + json.dumps(d, ensure_ascii=False) + '</script>')


def page(slug, title, desc, body, updated='31 Temmuz 2026', ptype='Article'):
    html = f'''<!doctype html>
<html lang="tr" data-theme="light">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{title} · Kriterin</title>
<meta name="description" content="{desc}" />
<link rel="canonical" href="https://kriterin.com/{slug}" />
<meta property="og:type" content="article" />
<meta property="og:site_name" content="Kriterin" />
<meta property="og:locale" content="tr_TR" />
<meta property="og:url" content="https://kriterin.com/{slug}" />
<meta property="og:title" content="{title}" />
<meta property="og:description" content="{desc}" />
<meta property="og:image" content="https://kriterin.com/og.png" />
<meta name="twitter:card" content="summary_large_image" />
<link rel="icon" href="/favicon.ico" sizes="any" />
<link rel="icon" type="image/png" sizes="96x96" href="/favicon-96.png" />
<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png" />
<style>{open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sayfa.css'), encoding='utf-8').read()}</style>
<script>try{{var t=localStorage.getItem('kriterin_tema');if(t)document.documentElement.setAttribute('data-theme',t);}}catch(e){{}}</script>
{jsonld(slug, title, desc, ptype)}
{ADS}
</head>
<body>
{NAV}
<div class="wrap">
{body}
{FOOT}
</div>
<script>
(function(){{
  var r=document.documentElement, b=document.getElementById('themeBtn');
  b.addEventListener('click',function(){{
    var next = r.getAttribute('data-theme')==='dark' ? 'light' : 'dark';
    r.setAttribute('data-theme',next);
    try{{localStorage.setItem('kriterin_tema',next);}}catch(e){{}}
  }});
}})();
</script>
</body>
</html>'''
    open(slug, 'w', encoding='utf-8').write(html)
    return slug
