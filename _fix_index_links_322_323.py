#!/usr/bin/env python3
"""Insert the two new 2026-10-29 article links into index.html's existing article list.

Locates the <ul> block that contains the most recent article link, then inserts the
new links at the top of that list so the list stays newest-first.
"""
import re

PATH = "/workspace/ribbonbow123/index.html"

ART322 = {
    "file": "blog-ribbon-oem-jewellery-watch-luxury-gift-packaging-trim-small-format-high-value-specification-private-label-buyers-guide-2026-10-29-am.html",
    "title": "Ribbon for Jewellery, Watch &amp; Luxury Gift Packaging Trim &mdash; Small-Format, High-Value Trim and How to Specify It (2026)",
}
ART323 = {
    "file": "blog-ribbon-oem-athletic-activewear-performance-apparel-trim-stretch-recovery-sweat-chlorine-wash-durability-branding-private-label-buyers-guide-2026-10-29-pm.html",
    "title": "Ribbon for Athletic &amp; Activewear Trim &mdash; Stretch, Sweat, Chlorine, Wash Durability and How to Specify It (2026)",
}

html = open(PATH, encoding="utf-8").read()

# Locate the <ul>...</ul> block that contains the newest existing article link.
anchor = "blog-ribbon-oem-die-cutting-laser-cutting"
pos = html.find(anchor)
if pos == -1:
    raise SystemExit("anchor article link not found in index.html")

ul_start = html.rfind("<ul", 0, pos)
ul_end = html.find("</ul>", pos)
if ul_start == -1 or ul_end == -1:
    raise SystemExit("could not locate enclosing <ul> block")
print(f"Found article list block: chars {ul_start}-{ul_end}")

block = html[ul_start:ul_end]
existing = re.findall(r'<li><a href="(blog-[^"]+\.html)">', block)
print(f"Existing entries in block: {len(existing)}")
for e in existing:
    print(f"  - {e[:80]}")

to_add = [a for a in (ART323, ART322) if a["file"] not in html]
if not to_add:
    print("Both articles already linked in index.html - no change needed.")
    raise SystemExit(0)

new_items = "".join(
    f'\n                <li><a href="{a["file"]}">{a["title"]}</a></li>'
    for a in to_add
)

# Insert right after the opening <ul ...> tag.
m = re.match(r'(<ul[^>]*>)', block)
if not m:
    raise SystemExit("opening <ul> tag not matched")
insert_at = ul_start + m.end()

html = html[:insert_at] + new_items + html[insert_at:]
open(PATH, "w", encoding="utf-8").write(html)
print(f"Inserted {len(to_add)} link(s) at position {insert_at}")
for a in to_add:
    print(f"  + {a['file'][:70]}")
