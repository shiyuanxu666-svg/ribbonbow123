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
DATE = "2026-10-31"

ART = {
    "330": {
        "file": "blog-ribbon-oem-development-brief-12-fields-comparable-quotes-request-for-quotation-specification-guide-b2b-brand-procurement-2026-10-31-am.html",
        "title": "How to Write a Ribbon OEM Development Brief That Gets You Comparable Quotes &mdash; 12 Fields, Specification Guide and How to Read the Responses (2026)",
        "tag": "OEM &amp; Sourcing",
        "cat": "B2B Sourcing",
        "read": "24 min read",
        "desc": "A practical guide to writing a ribbon OEM development brief so quotations are comparable. Covers the 12 fields every brief needs, why two quotes for the same product differ by 30 percent, how to read factory responses, and the mistakes that cost buyers the most money.",
        "accent": "#1a5276",
        "accent2": "#2e86c1",
    },
    "331": {
        "file": "blog-ribbon-oem-certification-reading-verifying-scope-currency-oeko-tex-fsc-bsci-smeta-iso-9001-grs-chain-of-custody-private-label-buyers-guide-2026-10-31-pm.html",
        "title": "How to Read and Verify Ribbon Factory Certifications &mdash; Scope, Currency, OEKO-TEX, FSC, BSCI, SMETA, ISO 9001 and GRS for Private Label Buyers (2026)",
        "tag": "Certification &amp; Compliance",
        "cat": "B2B Sourcing",
        "read": "26 min read",
        "desc": "How to read and verify the certificates on your ribbon supplier's file rather than tick a box. Covers what a certificate actually proves, OEKO-TEX product classes, FSC chain of custody, what ISO 9001 does not prove, BSCI versus SMETA versus SEDEX, GRS transaction certificates, and a five-step verification routine.",
        "accent": "#7b2cbf",
        "accent2": "#a569bd",
    },
}

# newest first
ORDER = ["331", "330"]


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
        f'                <div class="date">October 31, 2026</div>\n'
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
