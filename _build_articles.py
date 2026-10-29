#!/usr/bin/env python3
"""Build ribbonbow123 B2B articles from JSON content files.

Avoids inline triple-quoted strings entirely: all prose lives in
_content_<num>.json, this script only assembles the shared template.
"""
import json
import sys
from pathlib import Path

ROOT = Path("/workspace/ribbonbow123")
sys.path.insert(0, str(ROOT))

from tmpl_ribbon_article import build_html

SITE = "ribbonbow123.com"

META = {
    320: ("_content_320.json", "2026-10-29T08:00:00+08:00", "October 29, 2026", "am"),
    321: ("_content_321.json", "2026-10-29T13:00:00+08:00", "October 29, 2026", "pm"),
}


def build(num):
    fname, date_iso, date_display, slot = META[num]
    data = json.loads((ROOT / fname).read_text(encoding="utf-8"))

    slug = data["slug"]
    url = f"https://{SITE}/blog-{slug}.html"

    cfg = {
        "url": url,
        "title": data["title"],
        "desc": data["desc"],
        "keywords": data["keywords"],
        "date_iso": date_iso,
        "date_display": date_display,
        "num": num,
        "sections": [(s["h"], s["p"]) for s in data["sections"]],
        "faq": [(q, a) for q, a in data["faq"]],
        "metrics": [(k, v) for k, v in data["metrics"]],
        "author_bullets": data["author_bullets"],
        "author_name": "Xiamen Smith Ribbon&amp;Bow Co., Ltd.",
        "author_url": "https://ribbonbow123.com/about.html",
        "logo_url": "https://ribbonbow123.com/img/banner.png",
        "site": f"https://{SITE}",
        "closing_paragraph": data["closing_paragraph"],
        "closing_cta": data["closing_cta"],
        "h2_title": data["h2_title"],
    }

    html = build_html(cfg)
    out = ROOT / f"blog-{slug}.html"
    out.write_text(html, encoding="utf-8")

    body_words = sum(len(p.split()) + len(h.split()) for h, p in cfg["sections"])
    print(f"  #{num} {slot}: {out.name} ({len(html):,} bytes, ~{body_words} body words)")

    # sitemap entry
    sm_path = ROOT / "sitemap.xml"
    sm = sm_path.read_text(encoding="utf-8")
    if url in sm:
        print(f"  [skip] sitemap already has article {num}")
    else:
        entry = (
            "  <url>\n"
            f"    <loc>{url}</loc>\n"
            f"    <lastmod>{date_iso.split('T')[0]}</lastmod>\n"
            "    <changefreq>monthly</changefreq>\n"
            "    <priority>0.7</priority>\n"
            "  </url>\n"
        )
        idx = sm.rfind("</urlset>")
        if idx == -1:
            raise SystemExit("</urlset> not found in sitemap.xml")
        sm_path.write_text(sm[:idx] + entry + sm[idx:], encoding="utf-8")
        print(f"  [ok] sitemap.xml + article {num}")

    return slug


if __name__ == "__main__":
    nums = [int(a) for a in sys.argv[1:]] or sorted(META)
    for n in nums:
        build(n)
    print("BUILD DONE")
