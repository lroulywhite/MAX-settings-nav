#!/usr/bin/env python3
"""Rebuild src/stage.html and src/ex.json from the MAX | Explore Settings [Interaction] file.

Usage:  python3 tools/extract_stage.py "<path to MAX | Explore Settings [Interaction].html>"
Needs:  pip install playwright && playwright install chromium

The interaction file holds the real captured Settings page (the product shell, the page list, and the HTML of
every settings page) plus its own interaction layer. This tool keeps only the product pieces and drops the
interaction layer, so the walkthrough can reuse the real UI. It also lets mouse clicks through to the product
frame, which the original blocked.
"""
import json, pathlib, re, sys
from playwright.sync_api import sync_playwright

src = pathlib.Path(sys.argv[1]).resolve()
root = pathlib.Path(__file__).resolve().parent.parent

with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1920, "height": 1080})
    pg.goto(src.as_uri()); pg.wait_for_timeout(2500)
    d = pg.evaluate("DOC"); b.close()

m = re.search(r"<script\b[^>]*>(.*?)</script>", d, flags=re.S); s = m.group(1)
dec = json.JSONDecoder()
def grab(name):
    i = s.index("var %s=" % name) + len("var %s=" % name)
    return dec.raw_decode(s, i)[0]
EX, PAGES, INNER = grab("EX"), grab("PAGES"), grab("INNER")
tpl = re.search(r'<template id="tpl-base">(.*?)</template>', d, flags=re.S).group(1)
head = d[:d.index("<body")]
def j(o): return json.dumps(o, ensure_ascii=False).replace("<", "\\u003c").replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")

stage = (head + '<body class="dev-shellAttached ex-mode" app-scheme="momentus"><div id="screen-host"></div>'
  '<template id="tpl-base">' + tpl + '</template>'
  '<style>html,body{margin:0;width:1920px;overflow:hidden!important}#max-frame{pointer-events:auto!important}</style>'
  '<style id="hstyle">html,body{height:1480px!important}#screen-host{height:1480px!important}#max-frame{height:1440px!important}</style>'
  '<script type="application/json" id="data">' + j({"pages": PAGES, "inner": INNER}) + '</script>'
  '<script>(function(){var D=JSON.parse(document.getElementById("data").textContent);window.PAGES=D.pages;'
  'document.getElementById("screen-host").innerHTML=document.getElementById("tpl-base").innerHTML;'
  'var fr=document.getElementById("max-frame");fr.addEventListener("load",function(){parent.postMessage({maxReady:true},"*")});'
  'fr.srcdoc=D.inner;})();</script></body></html>')
(root / "src" / "stage.html").write_text(stage, encoding="utf-8")
(root / "src" / "ex.json").write_text(json.dumps([{"n": e["n"], "t": e.get("t", ""), "d": e["d"], "b": e.get("b", []), "r": e.get("r", "")} for e in EX], ensure_ascii=False, indent=1), encoding="utf-8")
print("Wrote src/stage.html and src/ex.json. Next: python3 build.py")
