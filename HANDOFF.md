# HANDOFF.md — kriterin.com

Sonraki oturum için devir notu. Sabit proje kuralları için `CLAUDE.md`'ye bak; bu dosya **anlık durumu** taşır.

## Standing kurallar (ihlal etme)
- "commit et" denmeden commit/push/merge/deploy YOK. Her deploy ~15 Netlify kredisi (ücretsiz plan 250/ay).
- Site içeriğinde uzun çizgi (— / –) yok. Uydurma istatistik yok (sadece mevcut külliyattaki sayılar).
- Dal: `claude/blissful-rubin-apcac3`. Netlify `main`'den deploy eder.

## Bekleyen COMMIT'siz değişiklikler (28 dosya — tek commit + tek deploy'a hazır)
Kullanıcı "commit et" deyince tek seferde canlıya alınacak:
- `anket.html` — karanlık mod beyaz flaş (FOUC) düzeltmesi: `<head>`'e senkron tema script'i (prefers-color-scheme fallback'li) + footer İletişim linki.
- `iletisim.html` — **YENİ** İletişim sayfası (hakkimizda.html şablonundan). ContactPage JSON-LD, e-posta kriterincom@gmail.com, sosyal linkler. "daha hızlı dönüş yaparız" baloncuğu KALDIRILDI. "Genellikle birkaç iş günü içinde yanıt veriyoruz." satırı DURUYOR (kullanıcı çıkarma demedi).
- 26 HTML — footer'a `/iletisim.html` linki (2 desen: mailto→link değişimi + Çerez tercihleri öncesine ekleme).
- `site/gen.py` — FOOT sabitine İletişim linki.
- `scripts/gen_sitemap.py` + `sitemap.xml` — iletisim.html eklendi (27 URL).
- `CLAUDE.md`, `HANDOFF.md` — bu oturumda eklendi.
- Smoke test GEÇİYOR.

## Tamamlanan işler (canlıda, merged)
- **AdSense "düşük değerli içerik" reddi giderme** (PR #57, main): 9→17 makale (8 yeni, qualitative, em-dash'siz), 14 sayfaya içerik, index.html trust paragrafı, IQ uyarı kutusu, hakkimizda + iletisim + yasal sayfalar. İçerik ~5.500→~14.000 kelime.
- CI smoke test (PR #50): `scripts/smoke.py` + `.github/workflows/smoke.yml`.
- Güvenlik sertleştirme: Firestore kuralları (affectedKeys scoping), App Check reCAPTCHA v3 enforce (kullanıcı %98'de enforce etti, akışlar doğrulandı OK), netlify.toml güvenlik başlıkları (HSTS/CSP).
- JS helper konsolidasyonu (window.KUtil).
- Denetim bulguları #2,3,4,6,7,8,9,10,11 düzeltildi. #1 (head ad kodunu kaldırma) AdSense onayına kadar ERTELENDİ — kod HTML'de KALMALI. #5 kullanıcı isteğiyle bırakıldı.

## Önemli kararlar
- **AdSense reklam kodu `<head>`'de kalacak** onay gelene kadar (doğrulama için gerekli). Consent Mode v2 uyumu zaten sağlıyor.
- Deploy previews Netlify'de kapalı — PR'da Netlify status çıkmaz, sadece CI smoke.
- Parallel Workflow subagent'ları bu ortamda canUseTool hatası veriyor ("permission handler...required parameter missing") — içerik işini kendim yapıyorum.

## Devam eden / karar bekleyen: Anonim demografi toplama (yeni özellik, HENÜZ KODLANMADI)
Kullanıcı anket akışına anonim yaş+cinsiyet toplama eklemek istiyor. Üzerinde anlaşılanlar:
- **Anonim** olacak (uid/IP/isim'e bağlanmayacak), gizlilik politikasına AYDINLATMA cümlesi (açık rıza kutusu gerekmez).
- Girişte **kesin yaş elle girilir** (sayı input, 18-99, min 18 zorunlu) + cinsiyet (Kadın/Erkek/Belirtmek istemiyorum). Kullanıcı istediği değeri girebilir.
- AdSense bu özellik için şimdilik göz ardı edilecek.
- **Bekleyen tek karar (kullanıcıdan):** ham anonim satır modeli (çapraz analiz mümkün, satır başına veri) mi, yoksa aggregate counter (en anonim, çapraz analiz yok) mu. Claude ham anonim satır (uid'siz, kesin yaş) öneriyor. Onay gelince: anket.html giriş adımı + Firestore uid'siz `stats` yazımı + kural + gizlilik aydınlatması kurgulanacak (commit etmeden).

## Bilinen konular / açık işler
- iletisim.html "Genellikle birkaç iş günü..." meta satırı: kullanıcı karar vermedi (çıkarılabilir).
- AdSense manuel adımlar (kullanıcıda): içerik deploy sonrası 3-7 gün bekle, biraz trafik getir, SONRA review iste — hemen isteme.
- Firestore emulator testi için jar scratchpad'de + @firebase/rules-unit-testing (kural değişikliği yaparsan).

## Faydalı yollar
- Makale üret: `cd site && python3 gen_artN.py`
- Smoke: `python3 scripts/smoke.py` · Sitemap: `python3 scripts/gen_sitemap.py`
- Playwright: chrome `/opt/pw-browsers/chromium-1194/chrome-linux/chrome`, node `/opt/node22/bin/node`, lib `/opt/node22/lib/node_modules/playwright/index.mjs`, yerel sunucu `python3 -m http.server 8099`.
- App Check site key: `6LdNungtAAAAAJ3h5_uGSEiUnyMGpk0Vns_DlOQn`
