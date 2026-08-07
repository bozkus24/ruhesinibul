#!/usr/bin/env python3
"""Kriterin — hafif smoke test (bağımlılıksız).

Netlify'a deploy OLMADAN önce, geçmişte bizi yakan üç sınıf hatayı yakalar:

  1) authnav.js?v=N sürüm tutarsızlığı  (elle cache-bust footgun'u)
  2) JS syntax hataları  (bağımsız .js + inline <script> blokları)  -> node --check
  3) Kırık yerel referanslar  (href/src="/x" ama dosya yok)

Sıfır bağımlılık: yalnızca Python 3 stdlib + `node`. CI ubuntu imajında ikisi de hazır.
Herhangi bir kontrol düşerse çıkış kodu 1 (CI kırmızı).
"""
import json
import os
import re
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
errors = []
checked = {"pages": 0, "js_files": 0, "inline": 0, "jsonld": 0, "refs": 0}

# node --check'e girecek script tipleri (boş tip = klasik JS). ld+json ayrı
# doğrulanır; importmap/template gibi diğer tipler atlanır.
JS_TYPES = {"", "text/javascript", "application/javascript", "module"}


def rel(p):
    return os.path.relpath(p, ROOT)


def html_files():
    for name in sorted(os.listdir(ROOT)):
        if name.endswith(".html"):
            yield os.path.join(ROOT, name)


def read(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


# --- 1) authnav.js?v= sürüm tutarlılığı --------------------------------------
def check_authnav_version():
    versions = {}  # v -> [pages]
    for path in html_files():
        for v in re.findall(r'authnav\.js\?v=(\d+)', read(path)):
            versions.setdefault(v, []).append(rel(path))
    if not versions:
        return
    if len(versions) > 1:
        detail = "; ".join(f"v={v} -> {', '.join(pages)}" for v, pages in sorted(versions.items()))
        errors.append(f"[authnav-version] Sayfalar arasında tutarsız authnav.js sürümü: {detail}")


# --- 2) JS syntax (node --check) ---------------------------------------------
def node_check(code, as_module, label):
    suffix = ".mjs" if as_module else ".js"
    with tempfile.NamedTemporaryFile("w", suffix=suffix, delete=False, encoding="utf-8") as tf:
        tf.write(code)
        tmp = tf.name
    try:
        r = subprocess.run(["node", "--check", tmp], capture_output=True, text=True)
        if r.returncode != 0:
            msg = (r.stderr or r.stdout).strip().splitlines()
            first = next((l for l in msg if "SyntaxError" in l), msg[-1] if msg else "syntax error")
            errors.append(f"[js-syntax] {label}: {first.strip()}")
    finally:
        os.unlink(tmp)


def check_standalone_js():
    targets = ["authnav.js", "cerez.js", "sw.js",
               "netlify/functions/leaderboard.js",
               "netlify/edge-functions/anket-og.js"]
    for t in targets:
        path = os.path.join(ROOT, t)
        if not os.path.exists(path):
            continue
        checked["js_files"] += 1
        # edge/functions ve sw modül; authnav/cerez klasik ama modül olarak da geçer.
        as_module = t.startswith("netlify/") or t == "sw.js"
        node_check(read(path), as_module, t)


SCRIPT_RE = re.compile(r'<script\b([^>]*)>(.*?)</script>', re.IGNORECASE | re.DOTALL)
TYPE_RE = re.compile(r'type\s*=\s*["\']([^"\']*)["\']', re.IGNORECASE)


def check_inline_scripts():
    for path in html_files():
        checked["pages"] += 1
        for i, (attrs, body) in enumerate(SCRIPT_RE.findall(read(path))):
            if re.search(r'\bsrc\s*=', attrs, re.IGNORECASE):
                continue  # harici script, gövde yok
            if not body.strip():
                continue
            m = TYPE_RE.search(attrs)
            stype = (m.group(1).strip().lower() if m else "")
            label = f"{rel(path)} inline #{i + 1}"
            if stype == "application/ld+json":
                checked["jsonld"] += 1
                try:
                    json.loads(body)
                except json.JSONDecodeError as e:
                    errors.append(f"[jsonld] {label}: geçersiz JSON — {e.msg} (satır {e.lineno})")
            elif stype in JS_TYPES:
                checked["inline"] += 1
                node_check(body, stype == "module", label)
            # diğer tipler (importmap, text/template vb.) atlanır


# --- 3) Kırık yerel referanslar ----------------------------------------------
# Clean-URL / redirect eşlemeleri (netlify.toml ile uyumlu)
CLEAN_URLS = {
    "/": "index.html",
    "/gunun-sorusu": "gunun-sorusu.html",
}
# Netlify tarafından üretilen / dosya olmayan yollar — atla
SKIP_PREFIXES = ("/api/", "/.netlify/")

REF_RE = re.compile(r'(?:href|src)\s*=\s*"(/[^"#?]*)(?:[?#][^"]*)?"', re.IGNORECASE)


def check_local_refs():
    for path in html_files():
        for ref in REF_RE.findall(read(path)):
            if ref.startswith(SKIP_PREFIXES):
                continue
            if ref in CLEAN_URLS:
                target = CLEAN_URLS[ref]
            elif ref.endswith("/"):
                target = ref.strip("/") + "/index.html"
            else:
                target = ref.lstrip("/")
            checked["refs"] += 1
            fs = os.path.join(ROOT, target)
            if not os.path.exists(fs):
                # uzantısız temiz yol olabilir: x -> x.html dene
                if not os.path.splitext(target)[1] and os.path.exists(fs + ".html"):
                    continue
                errors.append(f"[dead-ref] {rel(path)} -> \"{ref}\" (dosya yok: {target})")


def main():
    check_authnav_version()
    check_standalone_js()
    check_inline_scripts()
    check_local_refs()

    print(f"Taranan: {checked['pages']} sayfa, {checked['js_files']} bağımsız .js, "
          f"{checked['inline']} inline JS, {checked['jsonld']} JSON-LD, "
          f"{checked['refs']} yerel referans.")
    if errors:
        print(f"\n❌ {len(errors)} sorun bulundu:\n")
        for e in errors:
            print("  - " + e)
        sys.exit(1)
    print("✅ Smoke test geçti — tüm kontroller temiz.")


if __name__ == "__main__":
    main()
