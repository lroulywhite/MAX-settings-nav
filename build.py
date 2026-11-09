#!/usr/bin/env python3
"""Build the single-file Settings walkthrough.

Usage:  python3 build.py
Output: index.html and dist/settings-walkthrough.html (the same file).
        index.html is what GitHub Pages serves; either file works as a Genially embed.
"""
import json, pathlib

ROOT = pathlib.Path(__file__).parent
SRC = ROOT / "src"

def js(obj):
    s = json.dumps(obj, ensure_ascii=False)
    return s.replace("</", "<\\/").replace("<!--", "<\\!--").replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")

stage = (SRC / "stage.html").read_text(encoding="utf-8")
ex = json.loads((SRC / "ex.json").read_text(encoding="utf-8"))


out = (SRC / "outer.template.html").read_text(encoding="utf-8")
out = out.replace("__EX_JSON__", js(ex)).replace("__STAGE_JSON__", js(stage))
assert "__STAGE_JSON__" not in out

(ROOT / "dist").mkdir(exist_ok=True)
(ROOT / "dist" / "settings-walkthrough.html").write_text(out, encoding="utf-8")
(ROOT / "index.html").write_text(out, encoding="utf-8")
print("Wrote index.html and dist/settings-walkthrough.html,", round(len(out) / 1024), "KB")
