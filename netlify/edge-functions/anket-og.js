// Anket linki paylaşımlarında önizleme başlığını anket ismiyle değiştirir.
// WhatsApp/Instagram gibi önizleme botları JavaScript çalıştırmadığı için
// "?id=X" linklerinde <title> ve og etiketleri burada (edge'de) yeniden yazılır.
// Firestore okuma kuralları herkese açık olduğundan REST ile anahtar gerekmez.

const esc = (s) =>
  String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");

export default async (request, context) => {
  const url = new URL(request.url);
  const id = url.searchParams.get("id");
  const res = await context.next();
  if (!id || id.startsWith("loc_") || !/^[A-Za-z0-9_-]{1,40}$/.test(id)) return res;

  let name = "";
  try {
    const ctl = new AbortController();
    const t = setTimeout(() => ctl.abort(), 1800);
    const r = await fetch(
      "https://firestore.googleapis.com/v1/projects/kriterin/databases/(default)/documents/surveys/" +
        encodeURIComponent(id),
      { signal: ctl.signal }
    );
    clearTimeout(t);
    if (r.ok) {
      const d = await r.json();
      name = (d.fields && d.fields.name && d.fields.name.stringValue) || "";
    }
  } catch (e) {}
  if (!name) return res;

  // Başlık her paylaşımda aynı kancayı gösterir; açıklama ankete göre kişiselleşir.
  const title = "Flörtünü Test Et";
  const desc = esc(name + " kriterlerini belirledi. Ankete katıl; uyum yüzdeni ve liderlik tablosunu gör!");
  let html = await res.text();
  html = html
    .replace(/<title>[^<]*<\/title>/, "<title>" + title + "</title>")
    .replace(/(property="og:title" content=")[^"]*(")/, "$1" + title + "$2")
    .replace(/(property="og:description" content=")[^"]*(")/, "$1" + desc + "$2")
    .replace(/(name="description" content=")[^"]*(")/, "$1" + desc + "$2");

  const headers = new Headers(res.headers);
  headers.delete("content-length");
  return new Response(html, { status: res.status, headers });
};

export const config = { path: "/anket.html" };
