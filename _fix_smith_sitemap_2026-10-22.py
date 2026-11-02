#!/usr/bin/env python3
"""Fix smithribbon sitemap:
1) blog/<name>.html -> blog/blog-<name>.html  (missing blog- prefix, 236 URLs)
2) URLs with no file on disk -> drop from sitemap (genuinely deleted/renamed pages)
Then refresh lastmod for ALL urls to today (site-wide fresh-signal update).
Backup first.
"""
import re, os, shutil, datetime

ROOT = "/workspace/smithribbon-web"
SM = os.path.join(ROOT, "sitemap.xml")
TODAY = "2026-10-22"

shutil.copy(SM, SM + ".bak-2026-10-22")
print("backup written:", SM + ".bak-2026-10-22")

s = open(SM, encoding="utf-8").read()
base = "https://smithribbon.com/"

# Work on each <url>...</url> block
blocks = re.findall(r"<url>.*?</url>", s, re.S)
print("blocks:", len(blocks))

fixed_prefix = 0
dropped = []
out = []
seen = set()

for b in blocks:
    m = re.search(r"<loc>(.*?)</loc>", b)
    if not m:
        out.append(b); continue
    u = m.group(1).strip()
    rel = u.replace(base, "")

    # candidate resolution order
    cands = [rel]
    if rel.startswith("blog/") and not os.path.basename(rel).startswith("blog-"):
        cands.insert(0, "blog/blog-" + os.path.basename(rel))

    resolved = None
    for c in cands:
        if os.path.exists(os.path.join(ROOT, c)):
            resolved = c
            break

    if resolved is None:
        dropped.append(rel)
        continue

    if resolved != rel:
        fixed_prefix += 1
        newu = base + resolved
        b = b.replace(u, newu)
        u = newu

    if u in seen:
        dropped.append(rel + "  [DUP]")
        continue
    seen.add(u)

    # refresh lastmod to today
    if "<lastmod>" in b:
        b = re.sub(r"<lastmod>.*?</lastmod>", f"<lastmod>{TODAY}</lastmod>", b, flags=re.S)
    else:
        b = b.replace("</loc>", f"</loc>\n    <lastmod>{TODAY}</lastmod>", 1)

    out.append(b)

header = re.search(r"^.*?<url>", s, re.S)
head = header.group(0)[:header.group(0).rfind("<url>")] if header else s[:s.find("<url>")]
tail = "</urlset>"
news = head + "\n" + "\n".join(out) + "\n" + tail
open(SM, "w", encoding="utf-8").write(news)

print(f"prefix fixed   : {fixed_prefix}")
print(f"dropped (dead): {len(dropped)}")
print(f"final URLs    : {len(out)}")

# save dropped list for redirect-page generation
with open(os.path.join(ROOT, "_dropped_2026-10-22.txt"), "w", encoding="utf-8") as f:
    for d in dropped:
        f.write(d + "\n")

# sanity: any remaining broken?
s2 = open(SM, encoding="utf-8").read()
rem = 0
for u in re.findall(r"<loc>(.*?)</loc>", s2):
    rel = u.replace(base, "")
    if not os.path.exists(os.path.join(ROOT, rel)):
        rem += 1
print(f"remaining broken after fix: {rem}")
print("lastmod all today:", s2.count(f"<lastmod>{TODAY}</lastmod>"), "/", s2.count("<lastmod>"))