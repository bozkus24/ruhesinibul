# -*- coding: utf-8 -*-
from gen import page

page('404.html', 'Sayfa bulunamadı',
 'Aradığınız sayfa bulunamadı. Kriterin hesaplayıcısına veya yazılara dönebilirsiniz.',
 '''<h1>Bu sayfa yok</h1>
<p class="lede">Aradığın adres taşınmış ya da hiç var olmamış olabilir.</p>
<p class="meta">Hata 404</p>

<p>Bağlantıyı elle yazdıysan bir harf hatası olabilir. Aşağıdakilerden biriyle devam edebilirsin:</p>

<div class="cards">
  <a class="card" href="/">
    <b>Hesaplayıcı</b>
    <span>Aradığın kriterlere Türkiye'de kaç kişinin uyduğunu hesapla.</span>
  </a>
  <a class="card" href="/yazilar.html">
    <b>Yazılar</b>
    <span>Boy, evlilik, eğitim, gelir ve alışkanlık verileri üzerine yazılar.</span>
  </a>
</div>

<a class="cta" href="/">Hesaplayıcıya git →</a>''', ptype='WebPage')
print("ok")
