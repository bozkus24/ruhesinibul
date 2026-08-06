# Makale üreteçleri — ARŞİV, ÇALIŞTIRMAYIN

Bu klasördeki Python betikleri, sitedeki yazı ve hukuki sayfaların **ilk
sürümünü** üretti. Kök dizindeki yayında olan HTML dosyaları o günden beri
elle düzenlendi, dolayısıyla **bu betikler artık yayındaki içeriği
üretmiyor.**

Yeniden çalıştırırsanız kök dizindeki dosyaların üzerine yazar ve aşağıdaki
düzenlemelerin hepsi geri gider.

## Üreteç çıktısı ile yayındaki HTML arasındaki farklar

Şablon (`gen.py`):

- Üst bar artık `<span id="authNav"></span>` içeriyor; üreteçteki
  Hesaplayıcı / Yazılar / Hakkımızda bağlantıları kaldırılmış.
- Tema düğmesi üst bardan çıkıp `.wrap` içine taşındı (`float:right`).
- `<head>`e manifest, `theme-color` ve mobile-web-app etiketleri eklendi.
- Yazı sayfalarına `BreadcrumbList` JSON-LD ve görünür breadcrumb eklendi.
- Sayfa sonuna sosyal medya takip bloğu eklendi.
- Service worker kaydı ve `<script src="/authnav.js" defer>` eklendi.

Bağlantılar:

- Ana sayfa artık açılış sayfası; hesaplayıcı `/hesaplayici.html` adresinde.
  CTA ve footer bağlantıları buna göre güncellendi (üreteçlerde hâlâ `/`).

Metin:

- Uzun tireler temizlendi: `kritik — 5 cm` → `kritik, 5 cm`,
  `(12–14 cm)` → `(12 ile 14 cm)`.
- Her yazının sonuna "İlgili yazılar" bölümü eklendi (iç bağlantılar).

## Yeniden kullanmak isterseniz

İki seçenek var:

1. **Kaynak olarak canlandırmak:** `gen.py` şablonunu ve `gen_art*.py`
   gövdelerini yukarıdaki farkları kapsayacak şekilde güncelleyin, sonra
   çıktıyı kök dizindeki HTML ile karşılaştırıp fark kalmadığını doğrulayın.
2. **Bırakmak:** Yazıları doğrudan HTML üzerinde düzenlemeye devam edin ve
   bu klasörü yalnızca geçmiş kayıt olarak tutun.

Şu an ikinci durumdayız.

## Not

Bu klasör Netlify'a dağıtılıyor (`publish = "."`), bu yüzden `netlify.toml`
içinde `/site/*` yolunu 404'e düşüren bir kural var. Klasörü taşırsanız o
kuralı da güncelleyin.
