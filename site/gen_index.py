# -*- coding: utf-8 -*-
from gen import page

page('yazilar.html', "Yazılar",
 "Türkiye'nin demografik verileri, olasılık hesapları ve partner kriterleri üzerine yazılar.",
 '''<h1>Yazılar</h1>
<p class="lede">Kriterin'in arkasındaki sayılar, veriler ve hesaplar. Türkiye'nin demografisine olasılık gözüyle bakan yazılar.</p>
<p class="meta">Güncelleme: 31 Temmuz 2026</p>

<div class="cards">
  <a class="card" href="/kriterler-neden-imkansiz.html">
    <b>Kriterleriniz neden matematiksel olarak imkânsıza yakın?</b>
    <span>Beş makul kriter, koca bir ülkeyi bir sınıf mevcuduna indirebilir. Olasılıkların çarpılması ve kriter enflasyonu.</span>
  </a>
  <a class="card" href="/turkiyede-boy-dagilimi.html">
    <b>Türkiye'de boy dağılımı: 180 cm gerçekten uzun mu?</b>
    <span>Kadın ve erkeklerde ortalama boy, yüzdelik dilimler ve boy kriterinin havuzu ne kadar daralttığı.</span>
  </a>
  <a class="card" href="/yasa-gore-evlilik-oranlari.html">
    <b>Yaşa göre evlilik oranları</b>
    <span>Bekâr kalma ihtimali kaç yaşında düşüyor? Kadın ve erkek arasındaki makas ve ileri yaşta açılan fark.</span>
  </a>
  <a class="card" href="/egitim-ve-gelir.html">
    <b>Eğitim geliri ne kadar artırıyor?</b>
    <span>Türkiye'de eğitim seviyelerinin dağılımı, lisans–yüksek lisans–doktora kazanç farkı ve yaş bağlantısı.</span>
  </a>
  <a class="card" href="/goz-ve-sac-rengi.html">
    <b>Göz ve saç rengi dağılımı: Mavi göz gerçekten nadir mi?</b>
    <span>Göz rengi, saç rengi ve saç şekli oranları; bu özelliklerin birbiriyle olan istatistiksel bağlantısı.</span>
  </a>
  <a class="card" href="/sigara-alkol-ve-aliskanliklar.html">
    <b>Sigara ve alkol birbirini nasıl tetikliyor?</b>
    <span>Kullanım oranları, cinsiyet farkı ve iki alışkanlık arasındaki güçlü bağ. Din ve yaşın etkisi.</span>
  </a>
  <a class="card" href="/sehirlere-gore-farklar.html">
    <b>İl seçmek sonucu nasıl değiştiriyor?</b>
    <span>İstanbul, Ankara, İzmir, Bursa ve Antalya'da eğitim, gelir, alkol ve etnik köken oranları.</span>
  </a>
  <a class="card" href="/iq-dagilimi-nasil-okunur.html">
    <b>IQ dağılımı nasıl okunur?</b>
    <span>Ortalamanın altı puan kayması neden 14 milyon kişiyi taraf değiştirtiyor?</span>
  </a>
  <a class="card" href="/taraftarlik-cografyasi.html">
    <b>Taraftarlığın coğrafyası ve kimliği</b>
    <span>Trabzonspor Karadeniz'de neden üç kat? Cinsiyet ve etnik kökenin taraftarlığa etkisi.</span>
  </a>
</div>

<h2>Bu yazılar niçin var?</h2>
<p>Kriterin bir hesaplayıcı; girdiğiniz kriterlere kaç kişinin uyduğunu tahmin ediyor. Ama tek bir sayı, arkasındaki mantığı anlatmıyor. Bu yazılar o boşluğu dolduruyor: hangi verinin nereden geldiğini, kriterlerin birbirini nasıl etkilediğini ve bir sayının neden beklediğinizden farklı çıktığını açıklıyor.</p>
<p>Hepsi aynı ilkeye dayanıyor: <b>kriterler bağımsız değildir.</b> Yaş eğitimi, eğitim geliri, din alkolü, sigara da alkolü etkiler. Bu bağlantıları görmezden gelen bir hesap, çoğu zaman gerçekten uzak bir sonuç verir.</p>

<a class="cta" href="/">Hesaplayıcıya git →</a>''', ptype='CollectionPage')
print("ok")
