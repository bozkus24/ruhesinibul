# -*- coding: utf-8 -*-
# AdSense içerik hacmi için 4 yeni makale (niteliksel; uydurma istatistik yok).
# Kullanılan az sayıda oran, sitedeki mevcut makalelerde zaten geçen değerlerdir.
from gen import page

DATE = '2026-08-17'
MDATE = '17 Ağustos 2026'

# ============================================================
# 1) Kriter listesi nasıl kurulur?
# ============================================================
page('kriter-listesi-nasil-kurulur.html',
 "Kriter listesi nasıl kurulur? Havuzu koruyan akıllı bir yaklaşım",
 "Partner kriterlerini sıralamanın matematiği: hangi kriter havuzu çok daraltır, hangisi neredeyse hiç? Listeyi kısaltmadan akıllıca kurmanın yolu.",
 f'''<h1>Kriter listesi nasıl kurulur? Havuzu koruyan akıllı bir yaklaşım</h1>
<p class="lede">Kriterlerinden vazgeçmene gerek yok. Ama onları hangi sırayla ve hangi katılıkta koyduğun, geriye kalan kişi sayısını tamamen değiştirir.</p>
<p class="meta">Okuma süresi ~5 dakika · Güncelleme: {MDATE}</p>

<p>Çoğu insan kriter listesini bir alışveriş listesi gibi kurar: aklına gelen her maddeyi alt alta yazar. Sorun şu ki bu liste, birbirinden çok farklı "maliyetlere" sahip maddeleri aynı ağırlıkta gösterir. Bir kriter havuzu neredeyse hiç daraltmazken, bir diğeri tek başına onda dokuzunu silebilir. Listenin uzunluğu değil, <b>bileşimi</b> belirleyicidir.</p>

<h2>Önce "pahalı" ve "ucuz" kriterleri ayır</h2>
<p>Her kriterin bir bedeli vardır: havuzun ne kadarını elediği. Bu bedeli görmeden liste kurmak, fiyat etiketlerine bakmadan sepet doldurmaya benzer. Kabaca üç grup vardır:</p>
<ul>
<li><b>Ucuz kriterler:</b> Nüfusun büyük bir bölümünün karşıladığı maddeler. Saç şekli bunun tipik örneğidir; düz saç istemek havuzu yalnızca yarıya indirir. Bu tür kriterleri listede tutmanın maliyeti düşüktür.</li>
<li><b>Orta kriterler:</b> Havuzu belirgin ama yıkıcı olmayan biçimde daraltanlar. Belirli bir eğitim seviyesi ya da makul bir boy aralığı çoğu zaman bu gruba girer.</li>
<li><b>Pahalı kriterler:</b> Tek başına havuzun büyük kısmını silen maddeler. Ayrık ve nadir kategoriler; örneğin mavi göz, nüfusun küçük bir dilimidir ve diğer kriterlerle çarpıldığında sonucu birkaç yüze indirebilir.</li>
</ul>
<p>Amaç pahalı kriterlerden vazgeçmek değil; onların pahalı olduğunun <b>farkında olmak</b>. İki pahalı kriteri aynı listeye koyduğunda, geriye kalanın neden bir avuç insan olduğunu artık şaşırtıcı bulmazsın.</p>

<h2>Katılık, madde sayısından daha önemli</h2>
<p>Aynı kriter, seçtiğin eşiğe göre bambaşka bir maliyete sahip olabilir. "Uzun olsun" demek ile "çok uzun olsun" demek arasında dağlar vardır: alt eşiği birkaç santim gevşetmek, çoğu zaman listeden başka bir maddeyi tamamen çıkarmaktan daha fazla kişi kazandırır. Bu yüzden listeni kısaltmadan önce, mevcut maddelerin eşiklerini gevşetmeyi dene. Genellikle tek bir maddedeki küçük bir esneme, listenin tamamını korumanı sağlar.</p>

<h2>Bağlı kriterleri birlikte düşün</h2>
<p>Bazı kriterler birbirine bağlıdır ve bunu bilmek listeyi hem daha gerçekçi hem daha verimli yapar. Yüksek eğitim isteyen biri, farkında olmadan yüksek geliri de büyük ölçüde istemiş olur; ikincisini ayrıca eklemek havuzu pek daraltmaz. Tersine, genç bir yaş aralığı ile çok ileri bir eğitim seviyesini birlikte istemek iki maddeyi neredeyse çelişkiye sokar, çünkü diploma zaman ister. Bağlı kriterleri tek tek değil, çift olarak değerlendirmek gereksiz daraltmayı önler.</p>

<h2>Pratik bir yöntem</h2>
<p>İşe yarayan basit bir sıra şudur:</p>
<ul>
<li>Önce senin için gerçekten <b>vazgeçilmez</b> olan bir ya da iki maddeyi belirle. Liste bunların etrafında kurulur.</li>
<li>Sonra "olsa iyi olur" dediklerini ekle, ama her birini ekledikten sonra havuzun ne kadar değiştiğine bak.</li>
<li>Sonuç beklediğinden küçükse, en pahalı maddeyi bul ve onu bir kademe gevşet — çıkarmadan.</li>
<li>Birbirine bağlı iki madde varsa, birini seçmenin diğerini zaten büyük ölçüde belirlediğini unutma.</li>
</ul>
<p>Bu yaklaşımın amacı seni "daha az seçici" yapmak değil. Amaç, hangi kriterin sana gerçekten neye mal olduğunu görmen ve listeni bilinçli kurman. Etkiyi kendi seçimlerinle canlı görmek için kriterleri tek tek açıp kapatabilir, her birinin havuzu nasıl değiştirdiğini izleyebilirsin.</p>

<a class="cta" href="/hesaplayici.html">Kendi listeni hesaplayıcıda dene →</a>''',
 related=[
   ('kriterler-neden-imkansiz.html', "Kriterleriniz neden imkânsıza yakın?", "Beş makul kriter, koca bir ülkeyi bir sınıf mevcuduna nasıl indiriyor?"),
   ('turkiyede-boy-dagilimi.html', "Türkiye'de boy dağılımı", "Bir kriteri gevşetmenin gücü: boy eşiğinin havuza etkisi."),
 ], published=DATE, modified=DATE)

# ============================================================
# 2) Karşılıklı uyum
# ============================================================
page('karsilikli-uyum.html',
 "Karşılıklı uyum: sen de birinin kriterisin",
 "Eşleşme çift yönlüdür: yalnızca senin kriterlerin değil, karşı tarafın kriterleri de eler. Uyumun neden sandığından daha nadir olduğunun matematiği.",
 f'''<h1>Karşılıklı uyum: sen de birinin kriterisin</h1>
<p class="lede">Kriter hesabı çoğu zaman tek taraflı yapılır: "benim aradığıma kaç kişi uyuyor?" Ama eşleşmenin ikinci yarısı çoğu kişinin atladığı yerde saklı.</p>
<p class="meta">Okuma süresi ~5 dakika · Güncelleme: {MDATE}</p>

<p>Bir partner ararken doğal olarak kendi listenden bakarsın: senin kriterlerine kaç kişi uyuyor? Bu hesap havuzun bir yarısını verir. Diğer yarısı ise şu sorudur: <b>o kişilerin kaçının kriterlerine sen uyuyorsun?</b> Gerçek bir eşleşme, iki listenin aynı anda tutmasını gerektirir; ve iki bağımsız koşulun birlikte sağlanması, her birinin tek başına sağlanmasından her zaman daha nadirdir.</p>

<h2>İki filtre, tek kapı</h2>
<p>Şöyle düşün: senin kriterlerin bir eleme turu, karşı tarafın kriterleri ayrı bir eleme turu. Bir ilişkinin başlaması için bir kişinin <b>her iki turdan da</b> geçmesi gerekir. Senin listene uyan biri, senin onun listesine uymadığın için elenebilir; ya da tam tersi. Bu yüzden "bana uygun kaç kişi var?" sorusunun cevabı, "benimle eşleşebilecek kaç kişi var?" sorusunun cevabından her zaman büyüktür.</p>
<p>Kriterin'in hesaplayıcısı bilinçli olarak <b>tek yönü</b> ölçer: senin kriterlerine uyan kişi sayısını. Bu, üst sınırı verir. Karşılıklılık devreye girdiğinde gerçek havuz her zaman bundan küçüktür — ama ne kadar küçük olduğu, senin ve aradığın kişinin kriterlerinin ne kadar örtüştüğüne bağlıdır.</p>

<h2>Örtüşme bazen lehine çalışır</h2>
<p>İyi haber şu: iki listenin tutması her zaman şansa kalmış değildir. İnsanlar rastgele eşleşmez; benzer eğitim, benzer yaşam tarzı ve benzer çevredeki kişiler hem birbirini arar hem birbirinin ortamlarında bulunur. Senin değer verdiğin özelliklere sahip biri, çoğu zaman senin de sahip olduğun özelliklere değer veriyordur. Bu örtüşme, ham matematiğin gösterdiği kadar karamsar bir tabloyu yumuşatır.</p>

<h2>"Ben seçiciyim" ile "ben seçilirim" aynı madalyonun yüzleri</h2>
<p>Kriter listesi kurarken kolayca unutulan gerçek: her eklediğin madde, karşı taraf için de bir "sen" tanımı oluşturur. Çok yüksek bir eşik koyduğunda yalnızca aday havuzunu daraltmazsın; o havuzdaki kişilerin de yüksek eşikleri olma olasılığını artırırsın, çünkü benzer kişiler benzer beklentilere sahip olur. Bu yüzden karşılıklılığı hesaba katmak, listeni yalnızca daha gerçekçi değil, aynı zamanda daha adil yapar: kendinden istediğin standardı, karşındakinden istediğin standartla aynı terazide tartmanı sağlar.</p>

<h2>Pratik sonuç</h2>
<ul>
<li>Hesaplayıcının verdiği sayı bir <b>üst sınırdır</b>; karşılıklılık gerçek havuzu her zaman biraz daha küçültür.</li>
<li>Ama insanlar rastgele dağılmadığı için, senin değer verdiklerine sahip biri genellikle senin sahip olduklarına da değer verir — bu, matematiği yumuşatır.</li>
<li>Kriter koyarken "bu madde beni birinin gözünde nasıl konumlandırır?" sorusunu da sor. Eşleşme iki yönlü bir sözleşmedir.</li>
</ul>
<p>Kendi kriterlerinden bir anket oluşturup çevrendekilere çözdürürsen, karşılıklılığın somut bir örneğini görürsün: aynı kişi hem senin kriterlerini karşılar hem de kendi cevaplarıyla sana ne kadar uyduğunu gösterir.</p>

<a class="cta" href="/anket.html">Kendi uyum anketini oluştur →</a>''',
 related=[
   ('kriterler-neden-imkansiz.html', "Kriterleriniz neden imkânsıza yakın?", "Olasılıkların çarpılması ve kriter enflasyonu."),
   ('kriter-listesi-nasil-kurulur.html', "Kriter listesi nasıl kurulur?", "Havuzu koruyan akıllı bir yaklaşım."),
 ], published=DATE, modified=DATE)

# ============================================================
# 3) Online tanışmada filtreler
# ============================================================
page('online-tanisma-filtreleri.html',
 "Online tanışmada filtreler algıyı nasıl çarpıtır?",
 "Tanışma uygulamalarındaki filtreler ve profiller, gerçek nüfus dağılımını olduğundan farklı gösterir. Neden gördüğün dağılım gerçek dağılım değildir?",
 f'''<h1>Online tanışmada filtreler algıyı nasıl çarpıtır?</h1>
<p class="lede">Tanışma uygulamalarında gördüğün "havuz", Türkiye'nin gerçek dağılımı değildir. Filtreler, beyanlar ve algoritmalar araya girer — ve algını sessizce kaydırır.</p>
<p class="meta">Okuma süresi ~5 dakika · Güncelleme: {MDATE}</p>

<p>Bir tanışma uygulamasını birkaç hafta kullanan çoğu insan, farkında olmadan nüfus hakkında bir "sezgi" geliştirir: sanki uzun boylular çok yaygın, sanki herkes belirli bir yaşam tarzına sahip. Bu sezgi neredeyse her zaman yanlıştır, çünkü uygulamada gördüğün şey gerçek nüfusun bir örneği değil, birçok filtreden geçmiş, çarpıtılmış bir kesittir.</p>

<h2>Birinci çarpıtma: kim orada?</h2>
<p>Uygulamayı kullananlar rastgele bir grup değildir. Belirli yaş aralıkları, belirli şehirler ve belirli yaşam tarzları çevrimiçi tanışmada aşırı temsil edilir. Yani daha ilk adımda, ülke geneliyle örtüşmeyen bir havuza bakarsın. "Herkes şöyle" dediğin şey, aslında "bu uygulamayı kullanan kesim şöyle"dir.</p>

<h2>İkinci çarpıtma: beyan, ölçüm değildir</h2>
<p>Profillerdeki bilgiler ölçülmez, beyan edilir. İnsanların kendi boylarını birkaç santim yukarı yuvarlama eğilimi iyi bilinen bir olgudur ve profillerde bu daha da belirginleşir. Aynı şey eğitim, meslek ve yaşam tarzı için de geçerlidir: profil, kişinin gerçek hâlini değil, sunmak istediği hâlini gösterir. Bu yüzden uygulamadaki dağılım, gerçek dağılımdan sistematik olarak "şişkin" tarafa kayar.</p>

<h2>Üçüncü çarpıtma: filtrenin kendisi</h2>
<p>En sinsi çarpıtma, senin koyduğun filtrelerden gelir. Bir alt sınır belirlediğin anda, o sınırın altındaki herkes görünmez olur — ve zamanla, görmediğin şeyin var olmadığını düşünmeye başlarsın. Filtre yalnızca havuzu daraltmaz; algını da yeniden şekillendirir. Birkaç hafta boyunca yalnızca belirli bir profili gördüğünde, o profilin "normal" olduğuna dair sahte bir inanç oluşur.</p>

<h2>Algoritma da tarafsız değil</h2>
<p>Uygulamalar sana kimleri göstereceğini rastgele seçmez. Etkileşim aldıkları profilleri öne çıkarma eğilimindedirler; bu da zaten popüler olan belirli bir profil türünü daha da görünür kılar. Sonuçta gördüğün akış, nüfusun değil, sistemin "ilgi çekici" bulduğu şeyin bir yansımasıdır.</p>

<h2>Bu neden önemli?</h2>
<p>Çünkü bu çarpıtmalar birikince, gerçekçi olmayan bir kriter listesine yol açar. Uygulamada belirli bir profili sık gördüğün için onu yaygın sanır, kriterlerini ona göre yükseltirsin. Oysa gerçek nüfusta o profil çok daha nadir olabilir. Kriterlerinin gerçek maliyetini görmenin en iyi yolu, uygulamanın çarpıtılmış aynasına değil, nüfusun gerçek oranlarına bakmaktır.</p>
<ul>
<li>Uygulamadaki havuz, ülke geneli değil; kendini seçmiş bir kesittir.</li>
<li>Profiller ölçülmüş değil beyan edilmiştir; dağılımı olduğundan iyi gösterir.</li>
<li>Kendi filtren, görmediğin şeyi "yok" sanmana yol açar.</li>
<li>Gerçekçi bir kriter listesi, uygulamanın algısına değil gerçek oranlara dayanmalı.</li>
</ul>

<a class="cta" href="/hesaplayici.html">Gerçek oranlarla hesapla →</a>''',
 related=[
   ('turkiyede-boy-dagilimi.html', "Türkiye'de boy dağılımı", "Beyan edilen boylar ile ölçülen boylar neden farklı?"),
   ('kriter-listesi-nasil-kurulur.html', "Kriter listesi nasıl kurulur?", "Algıya değil, gerçek oranlara dayalı bir liste."),
 ], published=DATE, modified=DATE)

# ============================================================
# 4) Mükemmeli aramanın tuzağı
# ============================================================
page('mukemmel-partner-tuzagi.html',
 "'Mükemmeli' aramanın matematiksel tuzağı",
 "Her yeni kriter listeye bir madde eklemek gibi hissettirir; aslında havuzu bir kesirle çarpmaktır. 'Mükemmel' partner arayışının neden matematiksel bir tuzak olduğu.",
 f'''<h1>'Mükemmeli' aramanın matematiksel tuzağı</h1>
<p class="lede">Kriterlerini artırmak, listeye zararsız maddeler eklemek gibi görünür. Oysa her madde, geriye kalanı bir kesirle çarpar — ve çarpım acımasızdır.</p>
<p class="meta">Okuma süresi ~5 dakika · Güncelleme: {MDATE}</p>

<p>"Mükemmel" partner fikri masumdur: herkesin aklında, sahip olmasını istediği özelliklerin bir toplamı vardır. Sorun bu özelliklerin her birinde değil, bir araya geldiklerinde ortaya çıkan matematiktedir. Sezgimiz kriter eklemeyi bir <b>toplama</b> işlemi sanır; gerçekte olan bir <b>çarpma</b> işlemidir. Ve bu iki işlem, birkaç adımdan sonra tamamen farklı sonuçlara götürür.</p>

<h2>Toplama sezgisi, çarpma gerçeği</h2>
<p>Bir kriter eklediğinde sezgin "havuz biraz azalır" der. Gerçekte olan şey, kalan havuzun bir <b>yüzdesine</b> inmektir. Tek başına insanların büyük bölümünün karşıladığı üç kriteri yan yana koyduğunda bile, geriye bu üç oranın toplamı değil, çarpımı kalır — ve çarpım her adımda küçülür. Onuncu kriter, birincisi kadar "masum" değildir; çünkü kendinden önceki dokuzun zaten daralttığı küçük havuza uygulanır.</p>

<h2>Neden bu kadar hızlı çöküyor?</h2>
<p>Çünkü her kriter bağımsız bir çarpan gibi davranır ve birden küçük sayıları çarpmak, sonucu hızla sıfıra doğru iter. Yarının yarısı çeyrektir; çeyreğin yarısı sekizde birdir. Birkaç "makul" tercih, koca bir ülkeyi bir mahalleye indirebilir. Bu, senin fazla seçici olmandan değil, çarpmanın doğasından kaynaklanır. "Mükemmel" dediğin şey, aslında matematiksel olarak neredeyse imkânsız bir kesişim noktasıdır.</p>

<h2>Tuzağın psikolojisi</h2>
<p>Bu matematik bir de psikolojik tuzak yaratır. Her yeni kriter, kişiye "daha iyisini hak ediyorum" hissi verir ve tek tek bakıldığında hiçbiri haksız görünmez. Ama liste büyüdükçe, geriye kalan kişi sayısı görünmez biçimde erir. İnsan çoğu zaman havuzun neden bu kadar küçük olduğunu fark etmeden, "neden kimseyi bulamıyorum?" sorusuna takılır. Cevap genellikle karşı tarafta değil, listenin çarpımındadır.</p>

<h2>Tuzaktan çıkış: hangi kriter gerçekten önemli?</h2>
<p>Çözüm listeyi çöpe atmak değil. Çözüm, hangi kriterin senin için gerçekten belirleyici olduğunu ayırmak. Çoğu insan listesindeki en katı maddenin en önemlisi olduğunu sanır; oysa hesap çoğu zaman aksini söyler. Bazı kriterler havuzu neredeyse hiç daraltmaz, bir tanesi ise tek başına her şeyi değiştirir. "Mükemmeli" aramak yerine, senin için en çok neyin önemli olduğunu bilerek seçmek; hem daha mutlu edici hem matematiksel olarak çok daha mümkündür.</p>
<ul>
<li>Kriter eklemek toplama değil, çarpmadır; sonuç her adımda hızla küçülür.</li>
<li>Onuncu kriter, birincinin daralttığı havuza uygulandığı için çok daha "pahalıdır".</li>
<li>"Mükemmel" partner, matematiksel olarak neredeyse imkânsız bir kesişimdir.</li>
<li>Tuzaktan çıkış, listeyi kısaltmak değil; gerçekten önemli olanı ayırmaktır.</li>
</ul>

<a class="cta" href="/hesaplayici.html">Kriterlerinin gerçek maliyetini gör →</a>''',
 related=[
   ('kriterler-neden-imkansiz.html', "Kriterleriniz neden imkânsıza yakın?", "Çarpmanın acımasız matematiği, adım adım."),
   ('karsilikli-uyum.html', "Karşılıklı uyum: sen de birinin kriterisin", "Eşleşmenin çift yönlü matematiği."),
 ], published=DATE, modified=DATE)

print("4 makale üretildi.")
