#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Update blog.html, en-blog.html, index.html and sitemap.xml for articles
#357 (AM) and #358 (PM) — 2026-11-06 cron.

Newest first (PM above AM by published_time). Sitemap: append before </urlset>,
0 duplicates, lastmod 2026-11-06.
"""
import os
import re

WORK = "/workspace/ribbonbow123"
BASE = "https://ribbonbow123.com"
DATE = "2026-11-06"
DATE_LONG = "November 6, 2026"

ART = {
    "357": {
        "file": ("blog-oem-custom-packaging-private-label-ribbon-programme-guide-nine-field-brief-"
                 "sample-ladder-artwork-ownership-decoration-method-moq-cost-drivers-first-order-"
                 "readiness-checklist-private-label-buyers-guide-2026-11-06-am.html"),
        "title": "OEM Custom Packaging &amp; Private-Label Ribbon Programme Guide &mdash; The Nine-Field Brief, Sample Ladder and First-Order Readiness Checklist (2026)",
        "tag": "B2B &amp; OEM",
        "cat": "B2B OEM Guides",
        "read": "18 min read",
        "desc": "How to build an OEM custom ribbon and packaging programme: the nine specification fields a factory cannot guess, a five-step sample ladder, artwork and tooling ownership rules, decoration method selection, MOQ cost drivers and a first-order readiness checklist.",
        "accent": "#1f4e79",
        "accent2": "#2e75b6",
    },
    "358": {
        "file": ("blog-ribbon-oem-quote-comparison-total-cost-analysis-normalise-two-supplier-"
                 "landed-cost-components-supplier-scoring-evidence-hidden-cost-traps-cost-"
                 "reduction-sequence-brand-procurement-guide-2026-11-06-pm.html"),
        "title": "Ribbon OEM Quote Comparison &amp; Total Cost Analysis &mdash; How to Compare Two Factory Quotations Properly (2026)",
        "tag": "B2B &amp; Costs",
        "cat": "B2B Cost Analysis",
        "read": "19 min read",
        "desc": "A practical method for comparing ribbon factory quotations: force both onto one specification, take the price apart, build a twelve-component landed cost, score suppliers on evidence, and cut cost without damaging the product.",
        "accent": "#7b3f00",
        "accent2": "#c0691a",
    },
}

# Newest first: PM (#358, 13:00) then AM (#357, 08:00)
ORDER = ["358", "357"]


def card_blog(a):
    return (
        '<article class="blog-card">\n'
        f'  <span class="blog-tag">{a["tag"]}</span>\n'
        f'  <h3><a href="{a["file"]}">{a["title"]}</a></h3>\n'
        f'  <p>{a["desc"]}</p>\n'
        f'  <div class="blog-meta">{DATE} &middot; {a["read"]}</div>\n'
        '</article>\n\n'
    )


def card_en(a):
    return (
        f'<a href="{a["file"]}" class="blog-card-link" style="text-decoration:none;color:inherit;">'
        f'<div class="blog-card">'
        f'<div class="blog-card-image" style="background:linear-gradient(135deg,{a["accent"]},{a["accent2"]});">'
        f'{a["accent2"].replace("#", "")}</div>'
        f'<div class="blog-card-content">'
        f'<span class="blog-card-category">{a["cat"]}</span>'
        f'<h3><a href="{a["file"]}">{a["title"]}</a></h3>'
        f'<div class="blog-card-meta">📅 {DATE} · ⏱ {a["read"].replace(" min read", "")} min read</div>'
        f'<div class="blog-card-desc">{a["desc"]}</div>'
        f'<span class="read-more">Read full playbook →</span>'
        f'</div></div></a>'
    )


def insert_after(html, text, marker_regex):
    m = re.search(marker_regex, html, flags=re.IGNORECASE)
    if not m:
        return html + "\n" + text, False
    return html[:m.end()] + "\n" + text + html[m.end():], True


def update_blog(arts):
    path = os.path.join(WORK, "blog.html")
    html = open(path, encoding="utf-8").read()
    cards, changed = [], False
    for k in arts:
        a = ART[k]
        if a["file"] in html:
            print(f"  BLOG: {k} already present")
            continue
        cards.append(card_blog(a))
        changed = True
    if not changed:
        return
    new_html, ok = insert_after(html, "".join(cards), r'<article\s+class\s*=\s*["\']blog-card["\']')
    open(path, "w", encoding="utf-8").write(new_html)
    print(f"  BLOG: inserted {len(cards)} card(s) ok={ok}")


def update_en_blog(arts):
    path = os.path.join(WORK, "en-blog.html")
    html = open(path, encoding="utf-8").read()
    cards, changed = [], False
    for k in arts:
        a = ART[k]
        if a["file"] in html:
            print(f"  EN-BLOG: {k} already present")
            continue
        cards.append(card_en(a))
        changed = True
    if not changed:
        return
    new_html, ok = insert_after(html, "".join(cards), r'<div\s+class\s*=\s*["\']blog-grid["\']')
    open(path, "w", encoding="utf-8").write(new_html)
    print(f"  EN-BLOG: inserted {len(cards)} card(s) ok={ok}")


def card_index(a):
    return (
        '            <div class="blog-card">\n'
        f'                <div class="date">{DATE_LONG}</div>\n'
        f'                <h3><a href="{a["file"]}">{a["title"]}</a></h3>\n'
        f'                <p>{a["desc"]}</p>\n'
        '            </div>\n'
    )


def update_index(arts):
    path = os.path.join(WORK, "index.html")
    if not os.path.exists(path):
        print("  INDEX: not found")
        return
    html = open(path, encoding="utf-8").read()
    cards, added = [], 0
    for k in arts:
        a = ART[k]
        if a["file"] in html:
            print(f"  INDEX: {k} already present")
            continue
        cards.append(card_index(a))
        added += 1
    if not cards:
        return
    new_html, ok = insert_after(html, "".join(cards), r'<div\s+class\s*=\s*["\']blog-grid["\']\s*>')
    open(path, "w", encoding="utf-8").write(new_html)
    print(f"  INDEX: inserted {added} card(s) ok={ok}")


def update_sitemap(arts):
    path = os.path.join(WORK, "sitemap.xml")
    xml = open(path, encoding="utf-8").read()
    entries = []
    for k in arts:
        a = ART[k]
        if a["file"] in xml:
            print(f"  SITEMAP: {k} already present")
            continue
        entries.append(
            "  <url>\n"
            f"    <loc>{BASE}/{a['file']}</loc>\n"
            f"    <lastmod>{DATE}</lastmod>\n"
            "    <changefreq>weekly</changefreq>\n"
            "    <priority>0.85</priority>\n"
            "  </url>\n"
        )
    if not entries:
        return
    idx = xml.rfind("</urlset>")
    xml = xml[:idx] + "".join(entries) + xml[idx:] if idx != -1 else xml + "".join(entries)
    open(path, "w", encoding="utf-8").write(xml)
    print(f"  SITEMAP: added {len(entries)} URL(s)")


if __name__ == "__main__":
    print("--- blog.html ---");    update_blog(ORDER)
    print("--- en-blog.html ---"); update_en_blog(ORDER)
    print("--- index.html ---");   update_index(ORDER)
    print("--- sitemap.xml ---");  update_sitemap(ORDER)
    print("Done.")
