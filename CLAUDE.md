# CLAUDE.md — kriterin.com

Türkçe demografik / flört-kriteri sitesi. **Statik HTML**, build adımı yok. Netlify `main`'den deploy eder. Backend: Firebase Firestore + Google/Anonymous Auth + App Check (reCAPTCHA v3, kullanıcı tarafından enforce edildi).

## Mutlak kurallar (asla ihlal etme)
- **"commit et" denmeden HİÇBİR ŞEYİ commit etme.** Dosya düzenlemek serbest; commit/push/merge/deploy her seferinde ayrı açık onay ister.
- **Sormadan merge/deploy YOK.** Netlify ücretsiz plan = 250 kredi/ay, her production deploy ~15 kredi. Kullanıcı kredi maliyetine çok duyarlı. Toplu işi tek commit + tek deploy'da birleştir.
- **Site içeriğinde uzun çizgi (— / –) kullanma.** Normal tire veya yeniden yaz.
- **Uydurma istatistik YOK.** Sadece nitel içerik ya da mevcut makale külliyatında zaten geçen sayılar.

## Yapı (tekrar taramaya gerek yok)
- Kök dizin: ~28 `*.html` sayfa (canlıda servis edilenler) + `authnav.js`, `cerez.js`, `sw.js`, `firestore.rules`, `sitemap.xml`, `robots.txt`, `ads.txt`, `manifest.webmanifest`.
- `site/` = **makale üreteç kaynakları (arşiv, canlıda servis edilmez)**. `gen.py` ortak şablon (NAV/FOOT/CONSENT/ADS/JSON-LD); `gen_artN.py` makale batch'leri; `sayfa.css` makale CSS; `_social.html` footer sosyal blok. Yeni makale = `cd site && python3 gen_artN.py` (dosyayı repo köküne yazar).
- `site/gen_index.py`, `gen_legal.py`, `gen_404.py` canlıyla birebir DEĞİL — körlemesine çalıştırma. `index.html`, `hesaplayici.html`, `anket.html`, `gunun-sorusu.html` ELLE bakımdadır.
- `scripts/smoke.py` = bağımlılıksız CI (authnav.js?v=N sürüm tutarlılığı, `node --check` JS sözdizimi, JSON-LD geçerliliği, ölü yerel linkler). `scripts/gen_sitemap.py` = git commit tarihlerinden `sitemap.xml` üretir.
- `netlify/functions/leaderboard.js` (Günün Sorusu liderlik), `netlify/edge-functions/anket-og.js` (anket paylaşım OG başlığı). Kurallar `netlify.toml`'da.
- `.github/workflows/smoke.yml` = PR'da smoke test.

## İş akışı
1. Geliştirmeyi `claude/blissful-rubin-apcac3` dalında yap (yoksa oluştur).
2. Commit onayından sonra: `git push -u origin claude/blissful-rubin-apcac3` (ağ hatasında 2/4/8/16s backoff, 4 deneme).
3. PR sadece kullanıcı isterse. Merge sonrası dalı tazele: `git fetch origin main && git checkout -B claude/blissful-rubin-apcac3 origin/main` (+ force-with-lease).
4. **Merged PR'a yeni commit ekleme** — takip işi main'den taze dalla başlar.
5. Değişiklik sonrası `python3 scripts/smoke.py` çalıştır; makale/sayfa eklediysen `python3 scripts/gen_sitemap.py`.

## Dikkat noktaları
- **Cache-bust:** `authnav.js?v=N` sürümü tüm sayfalarda tutarlı olmalı (smoke bunu kontrol eder). JS'te `netlify.toml` zaten 1 saatlik tazelik verir.
- **FOUC/karanlık mod:** tema `<head>` içinde SENKRON script ile kurulur (deferred module'dan ÖNCE), `prefers-color-scheme` fallback'li.
- **Consent Mode v2** + AdSense head kodu her sayfada. AdSense onayı gelene kadar reklam kodu HTML'de kalmalı.
- **AdSense** onay bekliyor (geçmişte "düşük değerli içerik" reddi alındı; içerik derinleştirildi).
- GitHub işlemleri `gh` yok → `mcp__github__*` araçları. Repo scope: `bozkus24/ruhesinibul`.
