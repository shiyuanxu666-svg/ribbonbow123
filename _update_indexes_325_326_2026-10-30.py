#!/usr/bin/env python3
"""Update blog.html, en-blog.html, index.html and sitemap.xml for RB articles
#325 (2026-10-30 AM) and #326 (2026-10-30 PM).

Insert order: newest-first by published_time. #326 (13:00) goes above
#325 (08:00), which goes above the existing 2026-10-30 AM spec-guide article
(08:00) and the 2026-10-30 PM supplier-selection article (13:00, published
2026-10-28 - see PENDING_PUSH notes; the slot ordering follows the
article:published_time value stamped in each document).

Idempotent: re-running skips any article already present.
"""
import os
import re

WORK = "/workspace/ribbonbow123"
BASE = "https://ribbonbow123.com"
TODAY = "2026-10-30"

ART325 = {
    "file": ("blog-ribbon-oem-landed-cost-comparison-how-to-compare-two-valid-ribbon-quotes-"
             "true-unit-cost-freight-duty-moq-hidden-costs-b2b-procurement-2026-10-30-am.html"),
    "title": ("Landed Cost of OEM Ribbon &mdash; How to Compare Two Valid Quotes on Real Unit Cost, "
              "Freight, Duty and the Hidden Costs (2026)"),
    "cat": "Landed Cost &amp; Quotation Comparison",
    "date": TODAY,
    "time": "08:00",
    "desc": ("Two ribbon quotes can differ by 11 per cent on unit price and 34 per cent on landed cost. Covers the "
             "cost model - unit of account, one-time vs recurring, freight, duty, payment terms, cash cycle - the ten "
             "costs most often missing from a quotation, and a worked comparison that changes the sourcing decision."),
    "read": "18 min read",
    "grad": "#00695c,#26a69a",
}

ART326 = {
    "file": ("blog-ribbon-oem-rfq-guide-how-to-write-a-request-for-quotation-that-gets-comparable-answers-"
             "and-how-to-read-the-response-b2b-procurement-2026-10-30-pm.html"),
    "title": ("How to Write an RFQ for OEM Ribbon That Gets Comparable Answers &mdash; and How to Read "
              "the Quotations That Come Back (2026)"),
    "cat": "RFQ &amp; Supplier Response Guide",
    "date": TODAY,
    "time": "13:00",
    "desc": ("The RFQ decides the quality of the comparison that follows it. Covers the seven parts of a quotable "
             "enquiry, the eight questions that force a real number, how to read a response for performance signals, "
             "handling suppliers who reply with a question instead of a price, and an objective scoring method."),
    "read": "17 min read",
    "grad": "#6a1b9a,#8e24aa",
}

ARTS = [ART326, ART325]  # newest first


def card_en(art):
    grad = art["grad"]
    return (
        f'<a href="{art["file"]}" class="blog-card-link" style="text-decoration:none;color:inherit;">'
        f'<div class="blog-card">'
        f'<div class="blog-card-image" style="background:linear-gradient(135deg,{grad});">{art["cat"].split("&amp;")[0].split(" ")[0][:2].upper()}</div>'
        f'<div class="blog-card-content">'
        f'<span class="blog-card-category">{art["cat"]}</span>'
        f'<h3><a href="{art["file"]}">{art["title"]}</a></h3>'
        f'<div class="blog-card-meta">📅 {art["date"]} · ⏱ {art["read"]}</div>'
        f'<div class="blog-card-desc">{art["desc"]}</div>'
        f'<span class="read-more">Read full playbook →</span>'
        f'</div></div></a>'
    )


def card_blog(art):
    return (
        f'<article class="blog-card">\n'
        f'  <span class="blog-tag">{art["cat"]}</span>\n'
        f'  <h3><a href="{art["file"]}">{art["title"]}</a></h3>\n'
        f'  <p>{art["desc"]}</p>\n'
        f'  <div class="blog-meta">{art["date"]} &middot; {art["read"]}</div>\n'
        f'</article>\n\n'
    )


def card_feature(art):
    """blog.html uses a feature-card layout with a background gradient thumb."""
    grad = art["grad"]
    return (
        f'  <a href="{art["file"]}" class="blog-post-thumb" style="background:linear-gradient(135deg,{grad});" '
        f'aria-label="{art["title"].replace("&mdash;", "mdash").replace("&amp;", "and")}"></a>\n'
        f'  <h3 class="blog-post-title" itemprop="headline"><a href="{art["file"]}">{art["title"]}</a></h3>\n'
        f'  <p class="blog-post-excerpt">{art["desc"]}</p>\n'
        f'  <div class="blog-post-meta"><time datetime="{art["date"]}T{art["time"]}:00+08:00" itemprop="datePublished">'
        f'{art["date"]}</time> · {art["read"]}</div>\n'
        f'  <a class="blog-post-link" href="{art["file"]}">Read more &rarr;</a>\n'
    )


def insert_at_top(html, cards_text, marker_regex):
    m = re.search(marker_regex, html, flags=re.IGNORECASE)
    if not m:
        m = re.search(r"</header\s*>", html, flags=re.IGNORECASE)
    if not m:
        return html + "\n" + cards_text
    end = m.end()
    return html[:end] + "\n" + cards_text + html[end:]


def update_blog(arts):
    path = os.path.join(WORK, "blog.html")
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()
    cards, changed = [], False
    for art in arts:
        if art["file"] in html:
            print(f"  BLOG: {art['file']} already present")
            continue
        cards.append(card_blog(art))
        changed = True
    if changed:
        updated = insert_at_top(html, "".join(cards), r'<div\s+class\s*=\s*["\']blog-list["\']')
        with open(path, "w", encoding="utf-8") as f:
            f.write(updated)
        print(f"  UPDATED blog.html with {len(cards)} new card(s)")


def update_blog_feature(arts):
    """blog.html also has a feature-grid of blog-post-* items; insert there too
    if the class pattern exists and the article is not already linked."""
    path = os.path.join(WORK, "blog.html")
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()
    missing = [a for a in arts if a["file"] not in html]
    if not missing:
        return
    print(f"  BLOG feature-grid: {len(missing)} to add")
    # The list insert already adds the link, so nothing more is needed for
    # presence. We only verify presence below.
    print("  BLOG feature-grid: covered by list insertion")


def update_en_blog(arts):
    path = os.path.join(WORK, "en-blog.html")
    if not os.path.exists(path):
        print(f"  SKIP en-blog.html (not found)")
        return
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()
    cards, changed = [], False
    for art in arts:
        if art["file"] in html:
            print(f"  EN-BLOG: {art['file']} already present")
            continue
        cards.append(card_en(art))
        changed = True
    if changed:
        updated = insert_at_top(html, "".join(cards), r'<div\s+class\s*=\s*["\']blog-grid["\']')
        with open(path, "w", encoding="utf-8") as f:
            f.write(updated)
        print(f"  UPDATED en-blog.html with {len(cards)} new card(s)")


def update_index(arts):
    path = os.path.join(WORK, "index.html")
    if not os.path.exists(path):
        print(f"  SKIP index.html (not found)")
        return
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()
    missing = [a for a in arts if a["file"] not in html]
    if not missing:
        print("  INDEX: articles already linked")
        return
    for art in missing:
        link = f'\n        <li><a href="{art["file"]}">{art["title"]}</a></li>\n'
        m = re.search(r'(<ul[^>]*id="blog-links"[^>]*>)', html, flags=re.IGNORECASE)
        if not m:
            m = re.search(r'(<ul[^>]*class="[^"]*blog[^"]*"[^>]*>)', html, flags=re.IGNORECASE)
        if m:
            html = html[:m.end()] + link + html[m.end():]
        else:
            html = html.replace("</body>", link + "</body>")
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  UPDATED index.html with {len(missing)} new link(s)")


def update_sitemap(arts):
    path = os.path.join(WORK, "sitemap.xml")
    with open(path, "r", encoding="utf-8") as f:
        xml = f.read()
    entries, changed = [], False
    for art in arts:
        if art["file"] in xml:
            print(f"  SITEMAP: {art['file']} already present")
            continue
        entries.append(
            f"  <url>\n"
            f"    <loc>{BASE}/{art['file']}</loc>\n"
            f"    <lastmod>{TODAY}</lastmod>\n"
            f"    <changefreq>weekly</changefreq>\n"
            f"    <priority>0.85</priority>\n"
            f"  </url>\n"
        )
        changed = True
    if entries:
        idx = xml.rfind("</urlset>")
        updated = xml[:idx] + "".join(entries) + xml[idx:] if idx != -1 else xml + "".join(entries)
        with open(path, "w", encoding="utf-8") as f:
            f.write(updated)
        print(f"  UPDATED sitemap.xml with {len(entries)} new URL(s)")


def validate():
    print("--- VALIDATION ---")
    sm = open(os.path.join(WORK, "sitemap.xml"), encoding="utf-8").read()
    locs = re.findall(r"<loc>(.*?)</loc>", sm)
    print(f"  sitemap locs: {len(locs)} unique: {len(set(locs))}")
    assert len(locs) == len(set(locs)), "DUPLICATE SITEMAP LOCS"
    future = [l for l in re.findall(r"<lastmod>(.*?)</lastmod>", sm) if l > TODAY]
    print(f"  future lastmod: {len(future)}")
    assert not future, f"FUTURE LASTMOD: {future}"
    for f_ in ("blog.html", "en-blog.html", "index.html"):
        p = os.path.join(WORK, f_)
        if not os.path.exists(p):
            continue
        h = open(p, encoding="utf-8").read()
        for art in ARTS:
            assert art["file"] in h, f"{art['file']} MISSING from {f_}"
        print(f"  {f_}: both articles linked OK")
    for art in ARTS:
        p = os.path.join(WORK, art["file"])
        h = open(p, encoding="utf-8").read()
        words = len(re.sub(r"<[^>]+>", " ", h).split())
        checks = {
            "title": "<title>" in h,
            "description": 'name="description"' in h,
            "keywords": 'name="keywords"' in h,
            "canonical": 'rel="canonical"' in h,
            "og:title": 'property="og:title"' in h,
            "og:image": 'property="og:image"' in h,
            "og:url": 'property="og:url"' in h,
            "published_time": 'article:published_time' in h,
            "twitter:card": 'name="twitter:card"' in h,
            "Article JSON-LD": '"@type": "Article"' in h,
            "BlogPosting JSON-LD": '"@type": "BlogPosting"' in h,
            "FAQPage JSON-LD": '"@type": "FAQPage"' in h,
            "FAQ section": "Frequently Asked Questions" in h,
        }
        bad = [k for k, v in checks.items() if not v]
        faq_count = h.count('"@type": "Question"')
        print(f"  {art['file'][:60]}... words={words} faq_schema={faq_count} "
              f"{'ALL OK' if not bad else 'MISSING: ' + str(bad)}")
        assert not bad, bad
        assert faq_count == 7, f"expected 7 FAQ, got {faq_count}"
        assert words >= 1200, f"too few words: {words}"
        # entity check
        assert "Xiamen Smith Ribbon" in h, "entity name missing"
        assert "2004" in h, "since 2004 missing"
        for bad_year in ("2007", "since 2007", "Since 2007"):
            assert bad_year not in h, f"wrong founding year {bad_year}"
    print("  ALL VALIDATION PASSED")


if __name__ == "__main__":
    print("--- Updating en-blog.html ---")
    update_en_blog(ARTS)
    print("--- Updating blog.html ---")
    update_blog(ARTS)
    update_blog_feature(ARTS)
    print("--- Updating index.html ---")
    update_index(ARTS)
    print("--- Updating sitemap.xml ---")
    update_sitemap(ARTS)
    print("--- Validating ---")
    validate()
    print("Done.")
