#!/usr/bin/env python3
# One-shot repair: close the triple-quoted section bodies in the two new
# generator scripts. Each section body was written ending with a single
# double-quote before the comma instead of the triple-quote terminator.
# This fixes every remaining occurrence, then syntax-checks.
import ast
import re

FILES = [
    "/workspace/ribbonbow123/_gen_article_320_2026-10-29-am.py",
    "/workspace/ribbonbow123/_gen_article_321_2026-10-29-pm.py",
]

# A section body ends with:  <text>",
# and must end with:          <text>""",
# Detect lines that are the LAST line of a section body: they end with `",`
# and the following line is `    ),`  (closing the tuple) or `    ),`.

for fn in FILES:
    lines = open(fn, encoding="utf-8").read().split("\n")
    out = []
    fixed = 0
    for i, line in enumerate(lines):
        stripped = line.rstrip()
        nxt = lines[i + 1].strip() if i + 1 < len(lines) else ""
        # last line of a section body: ends with `",` and next line closes the tuple
        if stripped.endswith('",') and nxt in ('),', '),'):
            out.append(stripped[:-1] + '""",')
            fixed += 1
            continue
        out.append(line)
    src = "\n".join(out)
    open(fn, "w", encoding="utf-8").write(src)
    print(f"{fn.split('/')[-1]}: fixed {fixed} section terminator(s), "
          f"triple-quotes={src.count(chr(34)*3)}")
    try:
        ast.parse(src)
        print("   [OK] parses cleanly")
    except SyntaxError as e:
        print(f"   [ERR] line {e.lineno}: {e.msg}")
        print("   context:", (src.split(chr(10))[e.lineno - 1] or "")[:120])
