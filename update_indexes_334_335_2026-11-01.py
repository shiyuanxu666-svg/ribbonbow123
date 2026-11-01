#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Update blog.html, en-blog.html, index.html and sitemap.xml for articles #330 / #331 — 2026-10-31 cron.

Newest first (article:published_time descending): #331 (13:00) then #330 (08:00).
Sitemap: append before </urlset>, 0 duplicates, lastmod 2026-10-31.
"""
import os
import re

WORK = "/workspace/ribbonbow123"
BASE = "https://ribbonbow123.com"
DATE = "2026-11-01"

ART = {
    "334": {
        "file": "blog-private-label-ribbon-programme-guide-brief-samples-approval-gates-reorder-economics-packaging-documentation-metrics-private-label-buyers-guide-2026-11-01-am.html",
        "title": "Private Label Ribbon Programme Guide &mdash; From Development Brief to Repeat Order: Samples, Approval Gates, Reorder Economics, Packaging and Documentation for Brand Owners (2026)",
        "tag": "OEM &amp; Sourcing",
        "cat": "B2B Sourcing",
        "read": "25 min read",
        "desc": "A practical guide to structuring a private label ribbon and decorative trim programme as a repeatable supply programme rather than a series of purchase orders. Covers the four private label models, what a development brief must contain, how to run the sample ladder, how to build an approval gate schedule, reorder economics including MOQ exposure per SKU, packaging specification, the documentation set to fix before the first shipment, the programme metrics worth tracking, and where programmes usually come apart.",
        "accent": "#1a5276",
        "accent2": "#2e86c1",
    },
    "335": {
        "file": "blog-ribbon-landed-cost-model-cost-analysis-12-components-tariff-freight-working-capital-quality-loss-oem-brand-procurement-2026-11-01-pm.html",
        "title": "Ribbon Landed Cost &amp; Cost Analysis &mdash; The 12 Components of a Defensible Model, Tariff, Freight, Working Capital and Quality Loss for OEM Brand Owners (2026)",
        "tag": "Cost &amp; Pricing",
        "cat": "Cost & Pricing",
        "read": "24 min read",
        "desc": "A working cost model for buying ribbon and decorative trim, and why the quoted factory price is often less than half of the delivered cost. Covers all twelve landed cost components from ex-works value to internal conversion labour, how to read a factory's cost structure out of the quotation itself, where the money actually goes, how to compare two valid quotations on a normalised basis, and the cost-reduction levers that actually move the number.",
        "accent": "#b9770e",
        "accent2": "#e0a458",
    },
}

ORDER = ["335", "334"]


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
        f'                <div class="date">November 1, 2026</div>\n'
        f'                <h3><a href="{a["file"]}">{a["title"]}</a></h3>\n'
        f'                <p>{a["desc"]}</p>\n'
        '            </div>\n'
    )


def update_index(arts):
    """index.html — insert newest cards at the top of the Latest News blog-grid."""
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
    print("--- blog.html ---");       update_blog(ORDER)
    print("--- en-blog.html ---");    update_en_blog(ORDER)
    print("--- index.html ---");      update_index(ORDER)
    print("--- sitemap.xml ---");     update_sitemap(ORDER)
    print("Done.")
