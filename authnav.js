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
    st.textContent='#authNav{display:inline-flex;align-items:center;gap:9px}#authNav .an-name{max-width:120px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;font-weight:700;font-size:13.5px;color:var(--accent)}#authNav a.an-act{cursor:pointer;color:var(--muted);font-weight:600;font-size:13.5px;text-decoration:none;white-space:nowrap}#authNav a.an-act:hover{color:var(--accent)}';
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

  function render(){
    var u=getU();
    if(u && u.name){
      slot.innerHTML='<span class="an-name" title="'+esc(u.name)+'">'+esc(u.name)+'</span><a class="lnk an-act" href="#" data-logout>Çıkış</a>';
    } else {
      slot.innerHTML='<a class="lnk an-act" href="#" data-login>Giriş</a>';
    }
    var li=slot.querySelector('[data-login]'); if(li) li.addEventListener('click', onLogin);
    var lo=slot.querySelector('[data-logout]'); if(lo) lo.addEventListener('click', onLogout);
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
