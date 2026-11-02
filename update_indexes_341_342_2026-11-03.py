#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Update blog.html, en-blog.html, index.html and sitemap.xml for articles #341 / #342 — 2026-11-03 cron.

Newest first (article:published_time descending): #342 (13:00) then #341 (08:00).
Sitemap: append before </urlset>, 0 duplicates, lastmod 2026-11-03.
"""
import os
import re

WORK = "/workspace/ribbonbow123"
BASE = "https://ribbonbow123.com"
DATE = "2026-11-03"

ART = {
    "341": {
        "file": "blog-private-label-ribbon-programme-guide-specification-colour-standard-sample-ladder-supplier-evidence-reorder-protection-brand-buyers-guide-2026-11-03-am.html",
        "title": "Private Label Ribbon Programme Guide &mdash; Specification, Colour Standards, Sample Ladder, Supplier Evidence and Reorder Protection for Brand Buyers (2026)",
        "tag": "OEM &amp; Branding",
        "cat": "B2B Branding",
        "read": "21 min read",
        "desc": "A practical guide to running a private label ribbon programme: writing a buildable specification, capturing colour as a number, designing the sample ladder and securing the reorder.",
        "accent": "#1a5276",
        "accent2": "#2e86c1",
    },
    "342": {
        "file": "blog-ribbon-certification-verification-scope-expiry-evidence-claims-substantiation-supplier-compliance-audit-b2b-brand-procurement-2026-11-03-pm.html",
        "title": "Ribbon Certification Verification Guide &mdash; Scope, Expiry, Evidence and Claim Substantiation for Brand Procurement Teams (2026)",
        "tag": "B2B &amp; Compliance",
        "cat": "B2B Compliance",
        "read": "19 min read",
        "desc": "How to verify ribbon supplier certifications: reading scopes, tracking expiry, requesting evidence beyond the certificate, and substantiating your own on-pack compliance claims.",
        "accent": "#7d3c98",
        "accent2": "#a569bd",
    },
}

ORDER = ["342", "341"]


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
        f'                <div class="date">November 3, 2026</div>\n'
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
