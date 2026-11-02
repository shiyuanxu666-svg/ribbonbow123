#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Update blog.html, en-blog.html, index.html and sitemap.xml for articles #336 / #337 — 2026-11-01 cron.

Newest first (article:published_time descending): #337 (13:00) then #336 (08:00).
Sitemap: append before </urlset>, 0 duplicates, lastmod 2026-11-01.
"""
import os
import re

WORK = "/workspace/ribbonbow123"
BASE = "https://ribbonbow123.com"
DATE = "2026-11-01"

ART = {
    "336": {
        "file": "blog-ribbon-oem-sourcing-development-process-guide-factory-brief-samples-approval-purchase-order-reorder-plan-private-label-buyers-guide-2026-11-01-am.html",
        "title": "Ribbon OEM Sourcing &amp; Development Process Guide &mdash; From Brief to Repeat Order: Factory Selection, Samples, Approval and Reordering for Private Label Buyers (2026)",
        "tag": "OEM &amp; Sourcing",
        "cat": "B2B Sourcing",
        "read": "23 min read",
        "desc": "A step-by-step guide to sourcing custom ribbon and decorative trim from an OEM factory: choosing between OEM, ODM and private label models, writing a brief that gets comparable quotations, evaluating factory capability and capacity before price, running the sample ladder so you approve the right thing, the real development timeline from brief to delivery, purchase order clauses that prevent disputes, reorder planning, and where ribbon programmes most commonly go wrong.",
        "accent": "#1a5276",
        "accent2": "#2e86c1",
    },
    "337": {
        "file": "blog-ribbon-certification-compliance-guide-oeko-tex-fsc-bsci-smeta-iso-9001-verification-scope-expiry-audit-file-brand-procurement-2026-11-01-pm.html",
        "title": "Ribbon Certification &amp; Compliance Guide &mdash; How to Read OEKO-TEX, FSC, BSCI, SMETA and ISO 9001, Verify Scope and Expiry, and Build a File That Survives an Audit (2026)",
        "tag": "Compliance &amp; Quality",
        "cat": "Compliance & Quality",
        "read": "24 min read",
        "desc": "A practical guide to ribbon and decorative trim certifications for brand owners and procurement teams. Explains the two categories of credential and why confusing them creates gaps, how to read OEKO-TEX Standard 100, FSC, BSCI, SMETA and ISO 9001 without over-reading them, why certificate expiry and silent scope changes are the biggest compliance risk, a step-by-step verification method using the issuing body's own database, how to match certification to your actual product risk, and how to build a compliance file that stands up to a retailer audit.",
        "accent": "#7d3c98",
        "accent2": "#a569bd",
    },
}

ORDER = ["337", "336"]


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
