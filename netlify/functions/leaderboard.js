// Günün Sorusu liderlik tablosu — sunucu tarafı özet.
// Firestore'u okuyup JSON döner; Netlify CDN yanıtı ~5 dk önbelleğe alır,
// böylece binlerce ziyaretçi tek okumayla (aslında okumasız, CDN'den) beslenir.
// Bağımlılık yok: Firestore REST API + servis hesabı (JWT) ile çalışır.

const crypto = require('crypto');

let cachedToken = null, cachedExp = 0;

function getServiceAccount(){
  const raw = process.env.FIREBASE_SERVICE_ACCOUNT;
  if(!raw) throw new Error('FIREBASE_SERVICE_ACCOUNT ortam degiskeni tanimli degil');
  const txt = raw.trim().charAt(0) === '{' ? raw : Buffer.from(raw, 'base64').toString('utf8');
  return JSON.parse(txt);
}

function b64url(input){
  return Buffer.from(input).toString('base64').replace(/\+/g,'-').replace(/\//g,'_').replace(/=+$/,'');
}

async function getAccessToken(){
  const now = Math.floor(Date.now()/1000);
  if(cachedToken && now < cachedExp - 60) return cachedToken;
  const sa = getServiceAccount();
  const header = { alg:'RS256', typ:'JWT' };
  const claim = {
    iss: sa.client_email,
    scope: 'https://www.googleapis.com/auth/datastore',
    aud: 'https://oauth2.googleapis.com/token',
    iat: now,
    exp: now + 3600
  };
  const unsigned = b64url(JSON.stringify(header)) + '.' + b64url(JSON.stringify(claim));
  const signer = crypto.createSign('RSA-SHA256');
  signer.update(unsigned);
  const jwt = unsigned + '.' + b64url(signer.sign(sa.private_key));
  const res = await fetch('https://oauth2.googleapis.com/token', {
    method:'POST',
    headers:{ 'Content-Type':'application/x-www-form-urlencoded' },
    body: 'grant_type=urn:ietf:params:oauth:grant-type:jwt-bearer&assertion=' + encodeURIComponent(jwt)
  });
  const j = await res.json();
  if(!j.access_token) throw new Error('access token alinamadi: ' + JSON.stringify(j));
  cachedToken = j.access_token;
  cachedExp = now + (j.expires_in || 3600);
  return cachedToken;
}

async function runQuery(token, structuredQuery){
  const url = 'https://firestore.googleapis.com/v1/projects/kriterin/databases/(default)/documents:runQuery';
  const res = await fetch(url, {
    method:'POST',
    headers:{ 'Authorization':'Bearer '+token, 'Content-Type':'application/json' },
    body: JSON.stringify({ structuredQuery })
  });
  const arr = await res.json();
  if(!Array.isArray(arr)) throw new Error('sorgu hatasi: ' + JSON.stringify(arr));
  return arr.filter(x => x.document).map(x => x.document);
}

function val(f){
  if(f == null) return null;
  if('integerValue' in f) return Number(f.integerValue);
  if('doubleValue' in f) return f.doubleValue;
  if('stringValue' in f) return f.stringValue;
  if('booleanValue' in f) return f.booleanValue;
  return null;
}
function docId(name){ return name.split('/').pop(); }
function mapRow(d){
  const f = d.fields || {};
  return {
    uid: docId(d.name),
    name: val(f.name),
    bestStreak: val(f.bestStreak) || 0,
    avgTries: val(f.avgTries),
    avgSolveMs: val(f.avgSolveMs)
  };
}

exports.handler = async (event) => {
  try{
    const token = await getAccessToken();
    const streakQ = {
      from:[{ collectionId:'players' }],
      orderBy:[{ field:{ fieldPath:'bestStreak' }, direction:'DESCENDING' }],
      limit:100
    };
    const triesQ = {
      from:[{ collectionId:'players' }],
      where:{ fieldFilter:{ field:{ fieldPath:'eligible' }, op:'EQUAL', value:{ booleanValue:true } } },
      orderBy:[{ field:{ fieldPath:'avgTries' }, direction:'ASCENDING' }],
      limit:100
    };

    // GEÇİCİ TEŞHİS: /api/leaderboard?debug=1 — hangi projeye bağlanıyor + Firestore
    // ham cevabı (hata mı, boş mu?). Gizli anahtar döndürülmez.
    if(event && event.queryStringParameters && event.queryStringParameters.debug === '1'){
      let saProject=''; try{ saProject=getServiceAccount().project_id; }catch(e){}
      const r = await fetch('https://firestore.googleapis.com/v1/projects/kriterin/databases/(default)/documents:runQuery',
        { method:'POST', headers:{ 'Authorization':'Bearer '+token, 'Content-Type':'application/json' },
          body: JSON.stringify({ structuredQuery: streakQ }) });
      const raw = await r.text();
      return { statusCode:200, headers:{ 'Content-Type':'application/json', 'Cache-Control':'no-store' },
        body: JSON.stringify({ debug:true, saProject, httpStatus:r.status, rawSample: raw.slice(0,1200) }) };
    }

    // Her sorgu bağımsız: biri hata verse (ör. bileşik index hâlâ "building")
    // boş döner, diğeri yine gelir — tek sorgu tüm liderliği 503 yapmasın.
    const safe = (q) => runQuery(token, q).catch(() => []);
    const [streakDocs, triesDocs] = await Promise.all([ safe(streakQ), safe(triesQ) ]);
    const streak = streakDocs.map(mapRow);
    const tries = triesDocs.map(mapRow).sort((a,b) => {
      const t = (a.avgTries||0) - (b.avgTries||0);
      if(t) return t;
      return (a.avgSolveMs==null?Infinity:a.avgSolveMs) - (b.avgSolveMs==null?Infinity:b.avgSolveMs);
    });
    return {
      statusCode: 200,
      headers: {
        'Content-Type': 'application/json; charset=utf-8',
        // Tarayici 1 dk, Netlify CDN 5 dk onbellekler; bayatken arka planda yeniler.
        'Cache-Control': 'public, max-age=60',
        'Netlify-CDN-Cache-Control': 'public, s-maxage=300, stale-while-revalidate=600'
      },
      body: JSON.stringify({ streak, tries, at: Date.now() })
    };
  }catch(e){
    // Kurulmadıysa/hata olursa istemci canlı dinleyiciye düşer (site bozulmaz).
    return {
      statusCode: 503,
      headers: { 'Content-Type':'application/json', 'Cache-Control':'no-store' },
      body: JSON.stringify({ error: String((e && e.message) || e) })
    };
  }
};
