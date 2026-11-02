#!/usr/bin/env python3
"""Read-only validation of index.html, en-blog.html, blog.html and sitemap.xml.
Reports exact counts and missing URLs with file/line evidence. Modifies nothing."""
import re, glob, os, subprocess

WORK = "/workspace/ribbonbow123"
A322 = "blog-ribbon-oem-jewellery-watch-luxury-gift-packaging-trim-small-format-high-value-specification-private-label-buyers-guide-2026-10-29-am.html"
A323 = "blog-ribbon-oem-athletic-activewear-performance-apparel-trim-stretch-recovery-sweat-chlorine-wash-durability-branding-private-label-buyers-guide-2026-10-29-pm.html"

def lines_with(path, needle):
    out = []
    for i, line in enumerate(open(path, encoding="utf-8").read().splitlines(), 1):
        if needle in line:
            out.append(i)
    return out

print("=== en-blog.html: occurrence + card-block + line evidence ===")
e = open(os.path.join(WORK, "en-blog.html"), encoding="utf-8").read()
cards = e.split('<div class="blog-card">')
for label, f in (("pre-existing die-cutting", "blog-ribbon-oem-die-cutting-laser-cutting"),
                 ("NEW #322 jewellery", A322),
                 ("NEW #323 athletic", A323)):
    ncards = sum(1 for c in cards if f in c)
    print(f"  {label:24s} string-count={e.count(f):2d}  card-blocks={ncards}  lines={lines_with(os.path.join(WORK,'en-blog.html'), f)}")

print("\n=== blog.html: occurrence + line evidence ===")
b = open(os.path.join(WORK, "blog.html"), encoding="utf-8").read()
bcards = b.split('<article class="blog-card">')
for label, f in (("NEW #322 jewellery", A322), ("NEW #323 athletic", A323)):
    ncards = sum(1 for c in bcards if f in c)
    print(f"  {label:24s} string-count={b.count(f):2d}  card-blocks={ncards}  lines={lines_with(os.path.join(WORK,'blog.html'), f)}")
i322, i323 = b.find(A322), b.find(A323)
print(f"  order check: #323 pos={i323} < #322 pos={i322} -> {'OK (PM before AM)' if i323 < i322 else 'WRONG'}")

print("\n=== index.html: occurrence + line evidence ===")
i = open(os.path.join(WORK, "index.html"), encoding="utf-8").read()
for label, f in (("NEW #322 jewellery", A322), ("NEW #323 athletic", A323)):
    print(f"  {label:24s} string-count={i.count(f):2d}  lines={lines_with(os.path.join(WORK,'index.html'), f)}")
print(f"  </body> count = {i.count('</body>')} (expect 1)")
# list every blog- link in index.html with its line, to show the list ordering
print("  article links in index.html (line -> slug tail):")
for n in lines_with(os.path.join(WORK, "index.html"), 'href="blog-'):
    line = open(os.path.join(WORK, "index.html"), encoding="utf-8").read().splitlines()[n-1]
    slug = re.search(r'href="(blog-[^"]+)"', line).group(1)
    print(f"    L{n}: ...{slug[-58:]}")

print("\n=== sitemap.xml: counts, dups, missing (with provenance) ===")
s = open(os.path.join(WORK, "sitemap.xml"), encoding="utf-8").read()
locs = re.findall(r"<loc>(.*?)</loc>", s)
slugs = {l.rsplit("/", 1)[-1] for l in locs}
dups = sorted({x for x in locs if locs.count(x) > 1})
files = {os.path.basename(x) for x in glob.glob(os.path.join(WORK, "blog-*.html"))}
missing = sorted(files - slugs)
print(f"  total locs={len(locs)}  unique={len(set(locs))}  dups={dups}")
print(f"  blog html files on disk={len(files)}  missing from sitemap={len(missing)}")
for m in missing:
    print(f"    MISSING: {m[:78]}")

# provenance: was each missing article ALREADY absent from the sitemap at git HEAD?
head_sitemap = subprocess.check_output(["git", "show", "HEAD:sitemap.xml"], cwd=WORK).decode("utf-8")
head_names = subprocess.check_output(["git", "ls-tree", "--name-only", "HEAD"], cwd=WORK).decode("utf-8").split("\n")
print("  provenance vs git HEAD (True = pre-existing gap, not caused by this run):")
for m in missing:
    existed = m in head_names
    was_absent = m not in head_sitemap
    print(f"    {m[:60]}... existed_at_HEAD={existed} absent_from_HEAD_sitemap={was_absent} => pre-existing={existed and was_absent}")

print("\n=== diff scope of this run ===")
d = subprocess.check_output(["git", "diff", "--stat"], cwd=WORK).decode("utf-8")
print(d)
print("  sitemap locs added by this run:")
sd = subprocess.check_output(["git", "diff", "--", "sitemap.xml"], cwd=WORK).decode("utf-8")
for l in sd.splitlines():
    if l.startswith("+") and "<loc>" in l:
        print("   ", l.strip())
print("  sitemap locs REMOVED by this run:", sum(1 for l in sd.splitlines() if l.startswith("-") and "<loc>" in l))
