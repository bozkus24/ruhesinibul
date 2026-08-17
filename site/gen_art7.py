# -*- coding: utf-8 -*-
# İkinci içerik turu: 4 yeni makale (niteliksel; uydurma istatistik yok, uzun çizgi yok).
from gen import page

DATE = '2026-08-17'
MDATE = '17 Ağustos 2026'

# ============================================================
# 1) Din ve değerler kriteri
# ============================================================
page('din-ve-degerler-kriteri.html',
 "Din ve değerler: en sessiz ama en belirleyici kriter",
 "Din ve değer uyumu, çoğu kriter listesinde açıkça yazılmaz ama arka planda pek çok başka oranı birlikte belirler. Neden bu kadar güçlü bir filtredir?",
 f'''<h1>Din ve değerler: en sessiz ama en belirleyici kriter</h1>
<p class="lede">Çoğu kişi kriter listesine boyu, yaşı, eğitimi yazar; din ve değerleri ise çoğu zaman yazmaz ama zaten varsayar. Oysa bu sessiz kriter, listedeki en güçlü filtrelerden biridir.</p>
<p class="meta">Okuma süresi ~5 dakika · Güncelleme: {MDATE}</p>

<p>Partner kriterleri konuşulurken din ve değerler garip bir yerde durur. İnsanlar bunları çoğu zaman yüksek sesle söylemez, çünkü fazla "seçici" görünmek istemezler. Ama pratikte bu kriter, çoğu somut özellikten daha belirleyicidir. Sebebi basit: din yalnızca tek bir soruyu yanıtlamaz, arkasında bir yaşam tarzı, alışkanlık ve değer kümesi taşır.</p>

<h2>Neden tek bir kriter değil, bir demet?</h2>
<p>Bir kişinin dinî aidiyetini bildiğinizde, aslında onunla ilgili başka pek çok olasılığı da güncellemiş olursunuz. Bunların en net örneği alkoldür. Türkiye genelinde alkol kullanımı belirli bir orandayken, dinî aidiyete göre bu oran çok farklı seviyelere kayar; inançlı bir grupta çok düşük, seküler bir grupta çok yüksek olabilir. Yani "alkol kullanmasın" ve "dindar olsun" kriterlerini birlikte istediğinizde, ikincisi zaten büyük ölçüde birincisini de sağlamıştır. İki ayrı çarpan gibi düşünürseniz havuzu olduğundan küçük hesaplarsınız.</p>
<p>Aynı bağ beslenme, gelenek, tatil alışkanlıkları ve aile yapısı için de geçerlidir. Din kriterini seçmek, bunların hepsinde sessizce bir tarafı seçmek demektir. Bu yüzden din, listedeki tek satır gibi görünse de arka planda birçok satırı birden doldurur.</p>

<h2>Coğrafyayla iç içe</h2>
<p>Değerler kriteri coğrafyadan bağımsız da değildir. Ülkenin batısındaki büyük şehirlerde seküler yaşam tarzının oranı ülke ortalamasının üzerindeyken, başka bölgelerde tersi geçerlidir. Bu yüzden "şu değerlere sahip olsun" demek, farkında olmadan bir bölge tercihine de yaklaşmaktır. Şehir ile değer kriterini birlikte seçtiğinizde ikisi birbirini ya güçlendirir ya da neredeyse imkânsız kılar.</p>

<h2>Görünür kriter, görünmez varsayım</h2>
<p>İşin ilginç yanı, çoğu kişinin din ve değer uyumunu listeye hiç yazmadan varsaymasıdır. "Nasılsa benim gibi biriyle tanışırım" diye düşünülür. Oysa bu varsayım, havuzu daha ilk adımda ciddi biçimde daraltır ve çoğu zaman kişi bunun farkında bile değildir. Değer uyumunu açıkça düşünmek, en azından hangi kriterin sizin için gerçekten vazgeçilmez olduğunu netleştirir.</p>

<h2>Pratik sonuç</h2>
<ul>
<li>Din ve değerler tek bir kriter değil, arkasında alışkanlık ve yaşam tarzı taşıyan bir demettir.</li>
<li>Bu yüzden başka kriterlerle güçlü biçimde bağlıdır; ayrı çarpanlar gibi hesaplamak yanıltır.</li>
<li>Değer uyumunu çoğu kişi yazmadan varsayar; bu sessiz varsayım havuzu erkenden daraltır.</li>
<li>Coğrafyayla iç içedir; şehir ve değer kriteri birbirini belirler.</li>
</ul>
<p>Kriterlerinin gerçek etkisini görmek istiyorsan, din ve değerlerle ilgili seçimleri de dahil edip sonucun nasıl değiştiğine bakabilirsin.</p>

<a class="cta" href="/hesaplayici.html">Değer kriterlerini hesaplayıcıda dene →</a>''',
 related=[
   ('sigara-alkol-ve-aliskanliklar.html', "Sigara ve alkol: alışkanlıklar birbirini nasıl tetikliyor?", "Din ve alkol arasındaki güçlü bağın rakamları."),
   ('sehirlere-gore-farklar.html', "Aynı ülke, farklı ihtimaller", "Değerlerin şehre göre nasıl değiştiği."),
 ], published=DATE, modified=DATE)

# ============================================================
# 2) Vücut tipi beklentileri
# ============================================================
page('vucut-tipi-beklentileri.html',
 "Vücut tipi beklentileri: algı ile istatistik arasındaki fark",
 "Atletik, zayıf, normal; vücut tipi kriteri kulağa basit gelir ama beklentiyle gerçek dağılım çoğu zaman örtüşmez. Yaş ve cinsiyet bu tabloyu nasıl değiştirir?",
 f'''<h1>Vücut tipi beklentileri: algı ile istatistik arasındaki fark</h1>
<p class="lede">"Atletik olsun" demek kolaydır. Ama bu tercihin havuzda karşılığı, çoğu kişinin sandığından hem daha küçük hem de yaşa göre çok değişkendir.</p>
<p class="meta">Okuma süresi ~5 dakika · Güncelleme: {MDATE}</p>

<p>Vücut tipi, partner kriterleri arasında en görsel ve en çok konuşulanlardan biridir. Ama tam da görsel olduğu için, beklentiler gerçek dağılımdan kolayca kopar. İnsanların kafasındaki "normal" ya da "atletik" tanımı, çoğu zaman sosyal medyanın ve reklamların şekillendirdiği bir idealdir; nüfusun gerçek dağılımı ise bambaşkadır.</p>

<h2>Algı neden çarpık?</h2>
<p>Gün boyu gördüğünüz bedenler rastgele bir örneklem değildir. Sosyal medyada öne çıkan, reklamlarda kullanılan ve dikkat çeken bedenler belirli bir tipe yığılır. Bu tekrarlı maruz kalma, o tipin yaygın olduğu yanılgısını yaratır. Oysa gerçek nüfusta o tip nadir olabilir. Bu, boy ya da göz rengi için de geçerli olan aynı kümelenme yanılgısının vücut tipindeki karşılığıdır.</p>

<h2>Yaş her şeyi değiştirir</h2>
<p>Vücut tipini diğer fiziksel kriterlerden ayıran en önemli özellik, zamanla değişmesidir. Boy yetişkinlikte sabittir; vücut tipi ise değildir. Atletik ya da zayıf olma oranı genç yaş gruplarında belirgin biçimde yüksekken, ileri yaşlarda kilo dağılımı yukarı kayar. Bu yüzden "atletik olsun" kriteri, seçtiğiniz yaş aralığına tamamen bağlıdır. Genç bir aralıkta bu kriter havuzu az daraltırken, ileri bir yaş aralığında çok daha sert bir filtre hâline gelir.</p>

<h2>Cinsiyet farkı</h2>
<p>Vücut tipi dağılımı cinsiyete göre de ayrışır. Kaslılık ve atletiklik oranı erkeklerde farklı, kadınlarda farklı seyreder ve bu iki dağılım aynı değildir. Bu yüzden aynı vücut tipi kriteri, karşı cinsin hangisi olduğuna göre farklı bir maliyet taşır. Tek bir "atletik" kelimesi, kimi ararsanız ona göre farklı bir havuz bırakır.</p>

<h2>Beklentiyi gerçeğe yaklaştırmak</h2>
<p>Vücut tipi kriteri kötü ya da yanlış değildir; ama en çok yanılgıya açık olanıdır. Çünkü referans noktanız gerçek nüfus değil, gün boyu gördüğünüz seçilmiş görüntülerdir. Bu kriteri koyarken sormakta fayda var: aradığım tip, gerçekten yaygın mı, yoksa yalnızca sık mı gördüğüm bir tip? Yaş aralığını da hesaba katmak, beklentiyle gerçeği birbirine yaklaştırır.</p>
<ul>
<li>Vücut tipi algısı, gerçek dağılımdan çok gördüğünüz seçilmiş görüntülerle şekillenir.</li>
<li>Boyun aksine vücut tipi yaşla değişir; kriterin maliyeti yaş aralığına sıkı biçimde bağlıdır.</li>
<li>Dağılım cinsiyete göre ayrışır; aynı kelime farklı bir havuz bırakır.</li>
<li>En sık yanılgıya açık kriter budur; referansı gerçek oranlara dayamak gerekir.</li>
</ul>

<a class="cta" href="/hesaplayici.html">Vücut tipi kriterini yaşa göre dene →</a>''',
 related=[
   ('turkiyede-boy-dagilimi.html', "Türkiye'de boy dağılımı", "Fiziksel bir kriterin yüzdelik dilimlerle gerçek maliyeti."),
   ('online-tanisma-filtreleri.html', "Online tanışmada filtreler algıyı nasıl çarpıtır?", "Neden gördüğün dağılım gerçek dağılım değildir."),
 ], published=DATE, modified=DATE)

# ============================================================
# 3) Kriterlerin psikolojisi
# ============================================================
page('kriterlerin-psikolojisi.html',
 "'Tipim değil' derken ne diyoruz? Kriterlerin psikolojisi",
 "Kriterler yalnızca bir istek listesi değildir; alışkanlıkların, çevrenin ve geçmiş deneyimlerin bir yansımasıdır. 'Tipim' dediğimiz şey gerçekte nedir?",
 f'''<h1>'Tipim değil' derken ne diyoruz? Kriterlerin psikolojisi</h1>
<p class="lede">Bir kriter listesi, mantıklı bir tercih tablosu gibi görünür. Oysa çoğu madde bilinçli bir karardan çok, farkında olmadığımız bir alışkanlığın yansımasıdır.</p>
<p class="meta">Okuma süresi ~5 dakika · Güncelleme: {MDATE}</p>

<p>"Tipim değil" cümlesi çok kesin duyulur; sanki net bir ölçüt varmış gibi. Ama biraz kurcalayınca, bu ölçütün nereden geldiği çoğu zaman belirsizdir. Kriterler mantıklı bir hesabın sonucu gibi sunulur, gerçekteyse büyük bölümü çevrenin, geçmiş deneyimlerin ve sosyal beklentilerin sessiz bir toplamıdır. Kriterlerin psikolojisini anlamak, listeyi hem daha dürüst hem daha işe yarar yapar.</p>

<h2>Kriterler nereden gelir?</h2>
<p>Çoğu kriterin üç kaynağı vardır. Birincisi çevredir: büyüdüğünüz ortamda "normal" sayılan özellikler, farkında olmadan sizin ölçünüz olur. İkincisi geçmiş deneyimlerdir; iyi ya da kötü biten bir ilişki, sonraki listeye sessizce bir madde ekler ya da çıkarır. Üçüncüsü sosyal onaydır: başkalarının gözünde "iyi bir tercih" sayılacak özellikler, kişinin kendi isteği sanılarak listeye girer. Bu üç kaynak birbirine karışır ve sonunda "benim tipim" dediğimiz şey ortaya çıkar.</p>

<h2>İstek mi, alışkanlık mı?</h2>
<p>Kriterlerin bir kısmı gerçek bir isteği yansıtır; bir kısmı ise yalnızca alışkanlıktır. Aradaki farkı ayırmak zordur çünkü ikisi de aynı kesinlikle hissedilir. İyi bir test şudur: bir kriteri neden istediğinizi açıklamaya çalışın. Gerçek bir isteğin arkasında genellikle somut bir sebep vardır; alışkanlığın arkasında ise çoğu zaman "bilmiyorum, öyle işte" cevabı çıkar. "Öyle işte" ile biten kriterler, listeyi gizlice şişiren ama size gerçekte bir şey katmayan maddelerdir.</p>

<h2>Kesinlik yanılgısı</h2>
<p>Kriterler bir de kesinlik yanılgısı yaratır. Liste ne kadar uzun ve nettse, kişi o kadar "ne istediğini bilen" biri gibi hisseder. Oysa uzun ve katı bir liste, çoğu zaman ne istediğini bilmekten değil, riskten kaçınmaktan doğar. Her yeni madde, hayal kırıklığına karşı bir sigorta gibi eklenir. Sorun şu ki bu sigortaların toplamı, matematiksel olarak havuzu neredeyse sıfıra indirir ve kişi sonunda kimseyi "yeterince uygun" bulamaz hâle gelir.</p>

<h2>Listeyi dürüstleştirmek</h2>
<p>Amaç kriterlerden utanmak ya da onları silmek değil. Amaç, hangi maddenin gerçekten size ait olduğunu ayırmak. Kendinize sorun: bu kriter benim gerçek bir ihtiyacım mı, yoksa çevremin ya da geçmişimin bir kalıntısı mı? Bu ayrımı yapmak, listeyi kısaltmadan bile daha net ve daha adil hâle getirir. Çünkü en tatmin edici eşleşmeler, en uzun listelerden değil, en dürüst listelerden çıkar.</p>
<ul>
<li>Kriterler mantıklı bir hesap gibi görünür; büyük bölümü çevre, geçmiş ve sosyal onayın yansımasıdır.</li>
<li>Gerçek istek ile alışkanlığı ayırmanın testi: "neden?" sorusuna somut cevap verebiliyor musun?</li>
<li>Uzun ve katı liste, çoğu zaman netlikten değil riskten kaçınmaktan doğar.</li>
<li>Listeyi kısaltmadan da dürüstleştirebilirsin; en iyi eşleşmeler en dürüst listelerden çıkar.</li>
</ul>

<a class="cta" href="/anket.html">Kendi kriterlerini bir ankete dök →</a>''',
 related=[
   ('mukemmel-partner-tuzagi.html', "'Mükemmeli' aramanın matematiksel tuzağı", "Kriter katlamanın psikolojisi ve matematiği."),
   ('kriter-listesi-nasil-kurulur.html', "Kriter listesi nasıl kurulur?", "Hangi madde gerçekten sana ait?"),
 ], published=DATE, modified=DATE)

# ============================================================
# 4) Yaş farkı tercihleri
# ============================================================
page('yas-farki-tercihleri.html',
 "Yaş farkı tercihleri: kaç yaş fark havuzu nasıl değiştirir?",
 "Yaş aralığı seçmek yalnızca bir sayı seçmek değildir; evlilik durumu, eğitim ve gelir oranlarını da birlikte belirler. Yaş farkı tercihinin gizli maliyeti.",
 f'''<h1>Yaş farkı tercihleri: kaç yaş fark havuzu nasıl değiştirir?</h1>
<p class="lede">Yaş aralığı, çoğu kişinin "kendime yakın olsun" diye hızlıca geçtiği bir kriterdir. Oysa seçtiğin aralık, farkında olmadan başka birçok oranı da birlikte belirler.</p>
<p class="meta">Okuma süresi ~5 dakika · Güncelleme: {MDATE}</p>

<p>Yaş, kriter listelerinin en erken doldurulan ve en az sorgulanan maddesidir. İnsanlar genellikle "kendime birkaç yaş yakın olsun" der ve bunun tarafsız bir seçim olduğunu düşünür. Gerçekte ise yaş aralığı, havuzu belirleyen en güçlü kaldıraçlardan biridir; çünkü yalnızca o yaştaki kişi sayısını değil, o yaştakilerin bütün başka özelliklerini de birlikte seçer.</p>

<h2>Yaş, tek başına bir sayı değildir</h2>
<p>Bir yaş aralığı seçtiğinizde, o aralıkta evlilik oranının, eğitim seviyesinin, gelir dağılımının ve alışkanlıkların ne olduğunu da seçmiş olursunuz. Genç bir aralık bekâr oranını yükseltir ama aynı zamanda yüksek eğitim ve yüksek gelir olasılığını düşürür, çünkü bu ikisi zaman ister. İleri bir aralık ise eğitim ve geliri yukarı taşırken bekâr havuzunu ciddi biçimde daraltır. Yani "yaş farkı" dediğiniz şey, aslında bir dizi başka kriteri aynı anda ayarlayan bir düğmedir.</p>

<h2>Farkın yönü de önemli</h2>
<p>Yaş farkı tercihinde yalnızca büyüklük değil, yön de belirleyicidir. Kendinden büyük mü yoksa küçük mü tercih ettiğiniz, karşınıza çıkan havuzun bütün profilini değiştirir. Kendinden büyük bir aralık, evlilik oranının daha yüksek olduğu bir bölgeye kayar; kendinden küçük bir aralık ise bekâr oranı yüksek ama eğitim ve gelirin henüz oturmadığı bir bölgeye. Aynı "beş yıl fark" ifadesi, yukarı ya da aşağı olmasına göre bambaşka iki havuz demektir.</p>

<h2>Dar aralık, çift taraflı daralma</h2>
<p>Çok dar bir yaş aralığı seçmek, sezginin aksine iki kez daraltır. Birincisi doğrudan: yalnızca o yaştaki kişileri bırakır. İkincisi dolaylı: o dar aralık, belirli bir evlilik ve eğitim profilini de sabitler. Aralığı birkaç yıl genişletmek, çoğu zaman listeden başka bir maddeyi tamamen çıkarmaktan daha fazla kişi kazandırır. Yaş, üzerinde en kolay esneklik sağlanabilecek kriterlerden biridir ama en az esnetilenidir.</p>

<h2>Pratik sonuç</h2>
<ul>
<li>Yaş aralığı seçmek, evlilik, eğitim, gelir ve alışkanlık oranlarını aynı anda seçmektir.</li>
<li>Genç aralık bekâr oranını yükseltir ama eğitim ve geliri düşürür; ileri aralık tersi.</li>
<li>Farkın yönü havuzun profilini kökten değiştirir; yukarı ve aşağı fark aynı şey değildir.</li>
<li>Dar aralık iki kez daraltır; birkaç yıl genişletmek çoğu zaman en verimli hamledir.</li>
</ul>
<p>Yaş aralığını değiştirdiğinde diğer oranların birlikte nasıl kaydığını görmek için hesaplayıcıda aralığı oynatıp sonucu izleyebilirsin.</p>

<a class="cta" href="/hesaplayici.html">Yaş aralığını hesaplayıcıda dene →</a>''',
 related=[
   ('yasa-gore-evlilik-oranlari.html', "Yaşa göre evlilik oranları", "Bekâr kalma ihtimali kaç yaşında düşüyor?"),
   ('egitim-ve-gelir.html', "Eğitim geliri ne kadar artırıyor?", "Eğitim ve gelirin yaşla bağlantısı."),
 ], published=DATE, modified=DATE)

print("4 makale daha üretildi.")
