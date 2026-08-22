# HANDOFF.md — kriterin.com

Sonraki oturum için devir notu. Sabit proje kuralları için `CLAUDE.md`'ye bak; bu dosya **anlık durumu** taşır.

## Standing kurallar (ihlal etme)
- "commit et" denmeden commit/push/merge/deploy YOK. Her deploy ~15 Netlify kredisi (ücretsiz plan 250/ay).
- Site içeriğinde uzun çizgi (— / –) yok. Uydurma istatistik yok (sadece mevcut külliyattaki sayılar).
- Dal: `claude/blissful-rubin-apcac3`. Netlify `main`'den deploy eder.

## Bekleyen COMMIT'siz değişiklikler (hesaplayıcı anonim demografi — kullanıcı "commit et" deyince)
- `hesaplayici.html` — YENİ akış: (1) kriterlerden ÖNCE "Önce seni tanıyalım" kartı (yaş 18-99 sayı input + cinsiyet Kadın/Erkek/Belirtmek istemiyorum chip'leri), (2) sonuç `body.res-locked` ile "Sonucu öğren" butonuna kadar GİZLİ (minibar dahil), (3) butona basınca doğrulama + sonuç açılır (sonrası canlı güncellenmeye devam eder) + `hesap_stats`'a tek anonim satır: `{age, gender, criteria(map: 16 grup + boy/yasAraligi/iq aralıkları), createdAt}` (uid YOK, addDoc oto id, sayfa başına tek yazım, fire-and-forget). SSS "Girdiğim bilgiler kaydediliyor mu?" metni güncellendi.
- `firestore.rules` — `hesap_stats/{id}`: read:false, create hasOnly(['age','gender','criteria','createdAt']) + tip/aralık, update/delete:false. **Firebase'e AYRICA deploy gerekir!**
- `gizlilik-politikasi.html` — özet kutusu + madde 1 yeniden yazıldı ("hiçbir zaman gönderilmez" vaadi kaldırıldı, anonim istatistik aydınlatması), saklama süresi, tarih 22 Ağustos 2026.
- Smoke GEÇİYOR; Playwright doğrulaması: kilit/doğrulama/açılma/serileştirme OK (19 anahtar).

## Canlıda (main'e merge edildi, kullanıcı onayıyla)
- Anket anonim demografi (yaş+cinsiyet → `stats`), İletişim sayfası + FOUC düzeltmesi, AdSense içerik işi. **Kullanıcı `firestore.rules`'u Firebase'e henüz deploy ETMEDİ** (edene kadar stats yazımları reddedilir; kullanıcı "halledince yazacağım" dedi).
- Önizleme artifact'i: https://claude.ai/code/artifact/3d5143c2-b5b2-4135-a7f8-e4ea1d64b37b

## Standing kural (kullanıcı, 22 Ağu): ben söylemeden HİÇBİR ŞEY Netlify'a deploy edilmeyecek (main'e merge/push dahil).

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
