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

  // Küçük stil (bir kez enjekte)
  if(!document.getElementById('authnav-css')){
    var st=document.createElement('style'); st.id='authnav-css';
    st.textContent='#authNav{position:relative;display:inline-flex;align-items:center}'
      +'#authNav a.an-login{cursor:pointer;color:var(--muted);font-weight:600;font-size:13.5px;text-decoration:none;white-space:nowrap}#authNav a.an-login:hover{color:var(--accent)}'
      +'#authNav .an-btn{display:inline-flex;align-items:center;gap:6px;cursor:pointer;background:none;border:0;padding:4px 2px;font:inherit}'
      +'#authNav .an-name{max-width:130px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;font-weight:700;font-size:13.5px;color:var(--accent)}'
      +'#authNav .an-caret{font-size:10px;color:var(--muted);transition:transform .18s}#authNav .an-btn[aria-expanded="true"] .an-caret{transform:rotate(180deg)}'
      +'#authNav .an-drop{position:absolute;top:100%;right:0;margin-top:8px;min-width:150px;background:var(--surface,#fff);border:1px solid var(--line,#eee);border-radius:11px;box-shadow:0 10px 30px rgba(0,0,0,.14);padding:5px;z-index:50}'
      +'#authNav .an-drop[hidden]{display:none}'
      +'#authNav .an-item{display:block;padding:9px 12px;border-radius:8px;color:var(--ink,#222);text-decoration:none;font-weight:600;font-size:13.5px;cursor:pointer;white-space:nowrap}#authNav .an-item:hover{background:var(--accent-soft,rgba(0,0,0,.05));color:var(--accent)}';
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

  function closeMenu(){ var d=slot.querySelector('.an-drop'); var btn=slot.querySelector('.an-btn'); if(d)d.hidden=true; if(btn)btn.setAttribute('aria-expanded','false'); }
  function onDocClick(ev){ if(!slot.contains(ev.target)) closeMenu(); }

  function render(){
    var u=getU();
    if(u && u.name){
      slot.innerHTML='<button class="an-btn" type="button" aria-haspopup="true" aria-expanded="false"><span class="an-name" title="'+esc(u.name)+'">'+esc(u.name)+'</span><span class="an-caret" aria-hidden="true">▾</span></button>'
        +'<div class="an-drop" hidden role="menu"><a class="an-item" href="#" role="menuitem" data-logout>Çıkış yap</a></div>';
      var btn=slot.querySelector('.an-btn'), drop=slot.querySelector('.an-drop');
      btn.addEventListener('click', function(e){ e.preventDefault(); var open=drop.hidden; drop.hidden=!open; btn.setAttribute('aria-expanded', open?'true':'false'); });
      slot.querySelector('[data-logout]').addEventListener('click', onLogout);
      document.addEventListener('click', onDocClick);
    } else {
      slot.innerHTML='<a class="an-login" href="#" data-login>Giriş</a>';
      slot.querySelector('[data-login]').addEventListener('click', onLogin);
      document.removeEventListener('click', onDocClick);
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

  // Başka sekmede (storage) ya da aynı sayfada (anket/günün sorusu girişi) değişince güncelle
  window.addEventListener('storage', function(ev){ if(ev.key===KEY) render(); });
  window.addEventListener('kriterin-auth', render);
  render();
})();
