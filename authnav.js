// Üst bar giriş widget'ı (tüm sayfalarda ortak).
// Firebase'i SAYFA AÇILIŞINDA yüklemez; yalnızca "Giriş"/"Çıkış" tıklanınca yükler.
// Giriş durumu localStorage'dan (kriterin_user) anında gösterilir; anket + günün
// sorusu sayfaları gerçek Firebase durumundan bu anahtarı günceller, senkron kalır.
(function(){
  var KEY='kriterin_user';
  var slot=document.getElementById('authNav');
  if(!slot) return;

  function getU(){ try{ return JSON.parse(localStorage.getItem(KEY)||'null'); }catch(e){ return null; } }
  function setU(u){ try{ u?localStorage.setItem(KEY,JSON.stringify(u)):localStorage.removeItem(KEY); }catch(e){} }
  function esc(s){ return (s+'').replace(/[<>&"]/g,function(c){return {'<':'&lt;','>':'&gt;','&':'&amp;','"':'&quot;'}[c]; }); }

  // Ad + soyad gostermeye calisir. Ikisi birlikte 19 karakteri asarsa yalnizca
  // ad gosterilir. Ucnokta ile kisaltma yapilmaz.
  var AD_SINIR = 19;
  function kisaAd(s){
    var p = (s||'').trim().split(/\s+/).filter(Boolean);
    if(!p.length) return 'Hesabım';
    var ad = p[0];
    if(p.length === 1) return ad;
    var ikili = ad + ' ' + p[p.length-1];
    return ikili.length <= AD_SINIR ? ikili : ad;
  }

  // Ad temizligi: gunun-sorusu.html'deki filtreyle ayni. Bos donerse ad gecersiz.
  var BAD=['orospu','piç','pic','yarrak','yarak','amk','pezevenk','kahpe','anani','anan','yavsak','oç','sik','got','siktir','amcik'];
  function cleanName(s){ s=(s||'').trim().replace(/\s+/g,' ').slice(0,19); if(!s)return ''; var l=s.toLowerCase().replace(/[0-9@_.*ıİ]/g,''); for(var i=0;i<BAD.length;i++){ if(l.indexOf(BAD[i])>=0) return ''; } return s; }
  // Liderlik tablosunda kullanilan ad (gunun-sorusu ile ortak anahtar).
  function getNick(){ try{ return (localStorage.getItem('kriterin_nick')||'').trim(); }catch(e){ return ''; } }

  // Küçük stil (bir kez enjekte)
  if(!document.getElementById('authnav-css')){
    var st=document.createElement('style'); st.id='authnav-css';
    st.textContent='#authNav{position:relative;display:inline-flex;align-items:center}'
      +'#authNav a.an-login{cursor:pointer;color:var(--muted);font-weight:600;font-size:14px;text-decoration:none;white-space:nowrap;'
        +'display:inline-flex;align-items:center;min-height:44px;padding:0 6px;touch-action:manipulation}#authNav a.an-login:hover{color:var(--accent)}'
      /* Dokunma hedefi en az 44px: Android'de kucuk hedefe isabet ettirmek zor,
         iOS'un dokunma toleransi daha comert oldugu icin sorun orada gorunmuyordu. */
      +'#authNav .an-btn{display:inline-flex;align-items:center;gap:7px;cursor:pointer;background:none;border:0;'
        +'padding:0 4px;min-height:44px;font:inherit;touch-action:manipulation;-webkit-tap-highlight-color:transparent}'
      +'#authNav .an-name{white-space:nowrap;font-weight:700;font-size:14px;color:var(--accent)}'
      +'#authNav .an-caret{width:20px;height:20px;flex:none;display:inline-flex;align-items:center;justify-content:center;'
        +'border-radius:50%;background:var(--accent-soft,rgba(0,0,0,.06));transition:transform .18s}'
      +'#authNav .an-caret svg{width:12px;height:12px;stroke:var(--accent,#e0405f);fill:none;stroke-width:2.6;stroke-linecap:round;stroke-linejoin:round}'
      +'#authNav .an-btn[aria-expanded="true"] .an-caret{transform:rotate(180deg)}'
      +'#authNav .an-drop{position:absolute;top:100%;right:0;margin-top:6px;min-width:172px;background:var(--surface,#fff);border:1px solid var(--line,#eee);border-radius:12px;box-shadow:0 10px 30px rgba(0,0,0,.18);padding:6px;z-index:9999;display:none}'
      +'#authNav .an-drop.open{display:block}'
      +'#authNav .an-item{display:flex;align-items:center;min-height:44px;padding:0 14px;border-radius:9px;color:var(--ink,#222);text-decoration:none;font-weight:600;font-size:14px;cursor:pointer;white-space:nowrap;touch-action:manipulation}'
      +'#authNav .an-item:hover{background:var(--accent-soft,rgba(0,0,0,.05));color:var(--accent)}'
      /* Isim duzenleme paneli: "Ismi duzenle"ye basilinca acilir, menu ogeleri gizlenir. */
      +'#authNav .an-edit{display:none;flex-direction:column;gap:7px;padding:6px 8px 4px}'
      +'#authNav .an-drop.editing .an-edit{display:flex}'
      +'#authNav .an-drop.editing .an-item{display:none}'
      +'#authNav .an-input{width:100%;box-sizing:border-box;min-height:40px;padding:0 11px;border:1px solid var(--line,#ddd);border-radius:9px;font:inherit;font-size:14px;color:var(--ink,#222);background:var(--surface,#fff)}'
      +'#authNav .an-input:focus{outline:none;border-color:var(--accent,#e0405f)}'
      +'#authNav .an-save{min-height:40px;border:0;border-radius:9px;background:var(--accent,#e0405f);color:#fff;font:inherit;font-weight:700;font-size:14px;cursor:pointer;touch-action:manipulation}';
    document.head.appendChild(st);
  }

  var cfg={apiKey:"AIzaSyD_MIekQmU9wOtam8vrckMyhgjHKD_ZR9o",authDomain:"kriterin.firebaseapp.com",projectId:"kriterin",storageBucket:"kriterin.firebasestorage.app",messagingSenderId:"46765593126",appId:"1:46765593126:web:25738b3ebc5f1168f0cce7"};
  var authP=null;
  function loadAuth(){
    if(authP) return authP;
    authP=(async function(){
      var appMod=await import("https://www.gstatic.com/firebasejs/10.12.0/firebase-app.js");
      var authMod=await import("https://www.gstatic.com/firebasejs/10.12.0/firebase-auth.js");
      var app; try{ app=appMod.getApp(); }catch(e){ app=appMod.initializeApp(cfg); }
      return { m:authMod, auth:authMod.getAuth(app) };
    })();
    return authP;
  }

  function closeMenu(){ var d=slot.querySelector('.an-drop'); var btn=slot.querySelector('.an-btn'); if(d)d.classList.remove('open'); if(btn)btn.setAttribute('aria-expanded','false'); }
  // Dışarı tıklayınca kapat — TEK dinleyici (render'da tekrar eklenmez)
  document.addEventListener('click', function(ev){ if(!slot.contains(ev.target)) closeMenu(); });

  function render(){
    var u=getU();
    if(u && u.name){
      var gosterilen=kisaAd(u.name);
      slot.innerHTML='<button class="an-btn" type="button" aria-haspopup="true" aria-expanded="false" aria-label="Hesap menüsü"><span class="an-name" title="'+esc(u.name)+'">'+esc(gosterilen)+'</span>'
        +'<span class="an-caret" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M6 9l6 6 6-6"/></svg></span></button>'
        +'<div class="an-drop" role="menu">'
          +'<a class="an-item" href="#" role="menuitem" data-editname>İsmi düzenle</a>'
          +'<a class="an-item" href="#" role="menuitem" data-logout>Çıkış yap</a>'
          +'<div class="an-edit">'
            +'<input class="an-input" type="text" maxlength="19" placeholder="Görünen ad" aria-label="Görünen ad" autocomplete="off" />'
            +'<button class="an-save" type="button">Kaydet</button>'
          +'</div>'
        +'</div>';
      var btn=slot.querySelector('.an-btn'), drop=slot.querySelector('.an-drop');
      btn.addEventListener('click', function(e){
        e.preventDefault();
        e.stopPropagation();          // belge dinleyicisi ayni tiklamada kapatmasin
        var open=drop.classList.toggle('open');
        if(!open) drop.classList.remove('editing');   // kapaninca duzenleme paneli de kapansin
        btn.setAttribute('aria-expanded', open?'true':'false');
      });
      slot.querySelector('[data-logout]').addEventListener('click', onLogout);

      var inp=slot.querySelector('.an-input');
      slot.querySelector('[data-editname]').addEventListener('click', function(e){
        e.preventDefault();
        drop.classList.add('editing');
        inp.value = getNick() || kisaAd(u.name);   // varsa liderlik adi, yoksa gosterilen ad
        setTimeout(function(){ inp.focus(); inp.select(); }, 0);
      });
      slot.querySelector('.an-save').addEventListener('click', onSaveName);
      inp.addEventListener('keydown', function(e){ if(e.key==='Enter'){ e.preventDefault(); onSaveName(e); } });
    } else {
      slot.innerHTML='<a class="an-login" href="#" data-login>Giriş</a>';
      slot.querySelector('[data-login]').addEventListener('click', onLogin);
    }
  }

  function onLogin(e){
    e.preventDefault();
    loadAuth().then(function(x){
      return x.m.signInWithPopup(x.auth, new x.m.GoogleAuthProvider()).then(function(res){
        var nm=(res.user && res.user.displayName)||'Hesabım';
        setU({name:nm}); render();
      });
    }).catch(function(err){ if(err && err.code!=='auth/popup-closed-by-user') alert('Giriş yapılamadı: '+(err&&err.message?err.message:err)); });
  }
  function onLogout(e){
    e.preventDefault();
    setU(null); render();
    loadAuth().then(function(x){ return x.m.signOut(x.auth); }).catch(function(){});
  }

  // Liderlik + bardaki gorunen adi degistirir. Sunucuya yazma yalnizca KB'nin
  // yuklu oldugu sayfada (gunun-sorusu) olur; diger sayfalarda "custom" bayragi
  // sayesinde ad, oyun sayfasi bir sonraki senkronda sunucuya tasir.
  function onSaveName(e){
    if(e){ e.preventDefault(); e.stopPropagation(); }
    var inp=slot.querySelector('.an-input'); if(!inp) return;
    var n=cleanName(inp.value);
    if(!n){ alert('Bu isim kullanılamaz, başka bir isim dene.'); inp.focus(); return; }
    var u=getU()||{}; u.name=n; setU(u);
    try{ localStorage.setItem('kriterin_nick', n); localStorage.setItem('kriterin_nick_custom','1'); }catch(_e){}
    if(window.KB && KB.setName){ try{ KB.setName(n); }catch(_e){} }
    var hn=document.getElementById('hiNick'); if(hn) hn.textContent=n;   // oyun sayfasindaysa selamlama da guncellensin
    render();
  }

  // Başka sekmede (storage) ya da aynı sayfada (anket/günün sorusu girişi) değişince güncelle
  window.addEventListener('storage', function(ev){ if(ev.key===KEY) render(); });
  window.addEventListener('kriterin-auth', render);
  render();
})();
