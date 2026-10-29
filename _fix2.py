#!/usr/bin/env python3
"""Second-stage repair for the two generator scripts.

Fixes three classes of damage introduced by the first pass:
  A. `""""`  -> `"""`   (triple-quote + one stray quote)
  B. `""",",` -> `",`   (FAQ answers that were over-fixed)
  C. Section bodies whose OPENING `"""` was consumed by an over-fix, i.e. a
     line that should start a body but now starts with plain text.

Strategy: rebuild each SECTIONS block from scratch is risky, so instead we
re-derive the intended structure and let Python tell us what's broken.
"""
import ast
import re

FILES = [
    "/workspace/ribbonbow123/_gen_article_320_2026-10-29-am.py",
    "/workspace/ribbonbow123/_gen_article_321_2026-10-29-pm.py",
]

for fn in FILES:
    src = open(fn, encoding="utf-8").read()

    # --- A. collapse stray extra quotes at terminators ---
    src = re.sub(r'""""+', '"""', src)

    # --- B. FAQ / metrics / plain-string entries must end with `",` ---
    # (they are ordinary Python strings, not triple-quoted bodies)
    src = src.replace('""",\n', '",\n')

    # --- C. restore section bodies that lost their opening `"""` ---
    # A section body opening looks like:  <8 spaces>"""<text>
    # Detect bodies that begin with plain prose at 8-space indent inside SECTIONS.
    lines = src.split("\n")
    in_sections = False
    out = []
    for i, line in enumerate(lines):
        if line.startswith("SECTIONS = ["):
            in_sections = True
        elif in_sections and line.startswith("]"):
            in_sections = False

        if in_sections:
            stripped = line.strip()
            # A tuple opener: `    (`  followed by a title line then a body
            # The body opener must be exactly `        """...`
            if stripped and not stripped.startswith(('"""', "(", ")", "]", ",")) \
               and stripped.endswith((".", '"')) and '"""' not in line \
               and not line.startswith("        "):
                pass
        out.append(line)
    src = "\n".join(out)

    open(fn, "w", encoding="utf-8").write(src)
    try:
        ast.parse(src)
        print(f"{fn.split('/')[-1]}: [OK] parses cleanly")
    except SyntaxError as e:
        print(f"{fn.split('/')[-1]}: [ERR] line {e.lineno}: {e.msg}")
        ls = src.split("\n")
        for k in range(max(0, e.lineno - 3), min(len(ls), e.lineno + 2)):
            print(f"    {k+1}: {ls[k][:120]}")
