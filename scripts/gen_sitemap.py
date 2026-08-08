#!/usr/bin/env python3
"""sitemap.xml üreteci — lastmod'u GERÇEK git commit tarihinden alır.

Sorun: sitemap'teki <lastmod> elle yazılıyordu ve bayatlıyordu (sayfa değişse
bile tarih eskide kalıyor → Google'a yanlış tazelik sinyali). Bu script her
URL'nin eşlendiği dosyanın son commit tarihini (git log %cs) okuyup sitemap'i
yeniden yazar. Sayfa içeriği değişince tek komutla güncellenir:

    python3 scripts/gen_sitemap.py

Bağımlılık yok (git + Python 3 stdlib). priority/changefreq burada tutulur.
"""
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://kriterin.com"

# (URL yolu, eşlenen dosya, changefreq, priority) — sıra sitemap'teki sırayı korur.
PAGES = [
    ("/",                                 "index.html",                        "daily",   "1.0"),
    ("/hesaplayici.html",                 "hesaplayici.html",                  "daily",   "0.9"),
    ("/gunun-sorusu",                     "gunun-sorusu.html",                 "daily",   "0.9"),
    ("/anket.html",                       "anket.html",                        "weekly",  "0.9"),
    ("/yazilar.html",                     "yazilar.html",                      "weekly",  "0.8"),
    ("/kriterler-neden-imkansiz.html",    "kriterler-neden-imkansiz.html",     "monthly", "0.8"),
    ("/turkiyede-boy-dagilimi.html",      "turkiyede-boy-dagilimi.html",       "monthly", "0.8"),
    ("/yasa-gore-evlilik-oranlari.html",  "yasa-gore-evlilik-oranlari.html",   "monthly", "0.8"),
    ("/egitim-ve-gelir.html",             "egitim-ve-gelir.html",              "monthly", "0.8"),
    ("/goz-ve-sac-rengi.html",            "goz-ve-sac-rengi.html",             "monthly", "0.8"),
    ("/sigara-alkol-ve-aliskanliklar.html","sigara-alkol-ve-aliskanliklar.html","monthly","0.8"),
    ("/sehirlere-gore-farklar.html",      "sehirlere-gore-farklar.html",       "monthly", "0.8"),
    ("/iq-dagilimi-nasil-okunur.html",    "iq-dagilimi-nasil-okunur.html",     "monthly", "0.8"),
    ("/taraftarlik-cografyasi.html",      "taraftarlik-cografyasi.html",       "monthly", "0.8"),
    ("/hakkimizda.html",                  "hakkimizda.html",                   "yearly",  "0.5"),
    ("/gizlilik-politikasi.html",         "gizlilik-politikasi.html",          "yearly",  "0.3"),
    ("/cerez-politikasi.html",            "cerez-politikasi.html",             "yearly",  "0.3"),
    ("/kullanim-kosullari.html",          "kullanim-kosullari.html",           "yearly",  "0.3"),
]


def git_date(path):
    """Dosyanın son commit tarihi (YYYY-MM-DD). Commit yoksa bugünkü değil, dosya
    yoksa None döner — çağıran karar verir."""
    try:
        out = subprocess.run(["git", "-C", ROOT, "log", "-1", "--format=%cs", "--", path],
                             capture_output=True, text=True, check=True).stdout.strip()
        return out or None
    except subprocess.CalledProcessError:
        return None


def main():
    missing = []
    rows = []
    for url, fname, freq, prio in PAGES:
        fpath = os.path.join(ROOT, fname)
        if not os.path.exists(fpath):
            missing.append(fname)
            continue
        d = git_date(fname)
        if not d:
            # Henüz commit edilmemiş yeni dosya: lastmod'u atla (yanlış tarih yazma).
            missing.append(fname + " (commit yok)")
            rows.append(f'  <url><loc>{BASE}{url}</loc><changefreq>{freq}</changefreq>'
                        f'<priority>{prio}</priority></url>')
            continue
        rows.append(f'  <url><loc>{BASE}{url}</loc><lastmod>{d}</lastmod>'
                    f'<changefreq>{freq}</changefreq><priority>{prio}</priority></url>')

    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
           + "\n".join(rows) + "\n</urlset>\n")
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(xml)

    print(f"✓ sitemap.xml yazıldı ({len(rows)} URL).")
    if missing:
        print("UYARI, atlanan/eksik:", ", ".join(missing))
        return 1 if any("(commit yok)" not in m for m in missing) else 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
