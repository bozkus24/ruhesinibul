# scripts/

## smoke.py — hafif smoke test

Netlify'a deploy edilmeden önce, geçmişte tekrar eden üç hata sınıfını yakalar:

1. **`authnav.js?v=N` sürüm tutarsızlığı** — sayfalar farklı sürüme işaret ediyorsa
   (elle cache-bust bump'ı unutulunca oluşan footgun).
2. **JS/JSON syntax hataları** — bağımsız `.js` dosyaları + tüm inline `<script>`
   blokları (`node --check`) ve `application/ld+json` şemaları (JSON doğrulama).
3. **Kırık yerel referanslar** — `href`/`src="/x"` işaret ettiği dosya yoksa.

### Çalıştırma

```bash
python3 scripts/smoke.py
```

Sıfır bağımlılık: yalnızca Python 3 + `node`. Bir kontrol düşerse çıkış kodu `1`.

CI'da `.github/workflows/smoke.yml` üzerinden `main`'e push ve tüm PR'larda otomatik
çalışır.
