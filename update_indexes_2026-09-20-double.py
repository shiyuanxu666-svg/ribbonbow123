#!/usr/bin/env python3
"""Update en-blog.html, blog.html and sitemap.xml with articles 182-AM + 183-PM — 2026-09-20 double."""
import os, re

WORK = "/workspace/ribbonbow123"
BASE = "https://ribbonbow123.com"
TODAY = "2026-09-20"

ART182 = {
    "file": "blog-ribbon-oem-b2b-182-module-mill-side-q1-2027-private-label-oem-onboarding-22-stage-welcome-kit-architecture-b2b-oem-program-resilience-2026-09-20-am.html",
    "title": "Ribbon OEM B2B 182-Module Mill-Side Q1-2027 Private-Label OEM Onboarding 22-Stage Welcome-Kit Architecture B2B OEM Program Resilience",
    "cat": "Q1-2027 Private-Label OEM Onboarding 22-Stage Welcome-Kit Architecture",
    "date": TODAY,
    "desc": "182-module mill-side Q1-2027 private-label OEM onboarding 22-stage welcome-kit architecture (20-stage NDA/MSA/SOW/KPI-cascade waterfall, 18-document vendor-lifecycle binder, 15-stage EDI/API/CPQ/VMI digital-integration sprint, 13-stage sample-parallel-track, 11-stage artwork-onboarding pipeline, 9-stage color-stewardship transfer, 7-stage trade-compliance pre-clearance, 5-stage flow-down KPI cascade, 3-stage exit-protocol transition) for global brand procurement and Q1-2027 OEM-orchestration committees. Lift: 30-48% onboarding-cycle compression, 22-38% first-article-right lift, 14-26pp launch-readiness improvement.",
}
ART183 = {
    "file": "blog-ribbon-oem-b2b-183-module-mill-side-q1-2027-supplier-financial-health-tier-2-tier-3-rating-monitoring-procurement-resilience-architecture-b2b-oem-program-resilience-2026-09-20-pm.html",
    "title": "Ribbon OEM B2B 183-Module Mill-Side Q1-2027 Supplier-Financial-Health Tier-2 Tier-3 Rating & Monitoring Procurement-Resilience Architecture B2B OEM Program Resilience",
    "cat": "Q1-2027 Supplier-Financial-Health Tier-2 Tier-3 Rating & Monitoring Procurement-Resilience Architecture",
    "date": TODAY,
    "desc": "183-module mill-side Q1-2027 supplier-financial-health tier-2/tier-3 rating & monitoring procurement-resilience architecture (22-signal financial-health rating scorecard, 18-stage quarterly monitoring workflow, 15-stage early-warning rating-watch escalation ladder, 13-stage supplier-stress-test scenario-ladder, 11-stage working-capital-receivables-financing SCF-program, 9-stage bridge-order migration plan, 7-stage tariff/FX/commodity hedge ladder, 5-stage QBR sub-supplier governance cadence, 3-stage exit-substitution playbook) for global brand procurement and Q1-2027 finance controllers. End: 38-56% sub-supplier-failure early-warning lead-time extension, 21-38pp program-margin protection, 14-27pp OTIF resilience lift.",
}


def card_en(art, emoji):
    return (
        f'<a href="{art["file"]}" class="blog-card-link" style="text-decoration:none;color:inherit;">'
        f'<div class="blog-card">'
        f'<div class="blog-card-image" style="background:linear-gradient(135deg,#1a5276,{emoji});">{emoji}</div>'
        f'<div class="blog-card-content">'
        f'<span class="blog-card-category">{art["cat"]}</span>'
        f'<h3><a href="{art["file"]}">{art["title"]}</a></h3>'
        f'<div class="blog-card-meta">📅 {art["date"]} · ⏱ 42 min read</div>'
        f'<div class="blog-card-desc">{art["desc"]}</div>'
        f'<span class="read-more">Read full playbook →</span>'
        f'</div></div></a>'
    )


def card_blog(art, emoji):
    return (
        f'<article class="blog-post-card" data-category="{art["cat"]}">\n'
        f'  <a href="{art["file"]}" class="blog-post-thumb" style="background:linear-gradient(135deg,#1a5276,{emoji});" aria-label="{art["title"][:60]}"></a>\n'
        f'  <div class="blog-post-content">\n'
        f'    <span class="blog-post-category">{art["cat"]}</span>\n'
        f'    <h3 class="blog-post-title"><a href="{art["file"]}">{art["title"]}</a></h3>\n'
        f'    <div class="blog-post-meta">📅 {art["date"]} · ⏱ 42 min read</div>\n'
        f'    <p class="blog-post-excerpt">{art["desc"]}</p>\n'
        f'    <a href="{art["file"]}" class="blog-post-link">Read full playbook →</a>\n'
        f'  </div>\n'
        f'</article>\n'
    )


def insert_after_grid(html, new_cards):
    pattern = re.compile(r'(<div\s+class="[^"]*posts-grid[^"]*"\s*>)', re.IGNORECASE)
    m = pattern.search(html)
    if m:
        return html[:m.end()] + "\n" + new_cards + html[m.end():]
    pat2 = re.compile(r'(<ul\s+class="[^"]*blog-list[^"]*"\s*>)', re.IGNORECASE)
    m2 = pat2.search(html)
    if m2:
        return html[:m2.end()] + "\n" + new_cards + html[m2.end():]
    pat3 = re.compile(r'(<div\s+class="[^"]*blog-list[^"]*"\s*>)', re.IGNORECASE)
    m3 = pat3.search(html)
    if m3:
        return html[:m3.end()] + "\n" + new_cards + html[m3.end():]
    return html.replace("</body>", new_cards + "\n</body>")


def update_en_blog(arts):
    path = os.path.join(WORK, "en-blog.html")
    if not os.path.exists(path):
        print(f"SKIP {path} (not found)")
        return
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()
    emojis = ["#1abc9c", "#d4367c"]  # 182=teal, 183=magenta
    changed = False
    cards_to_add = []
    for i, art in enumerate(arts):
        if art["file"] in html:
            print(f"{art['file']} already in en-blog.html — skipping")
            continue
        cards_to_add.append(card_en(art, emojis[i % len(emojis)]) + "\n")
        changed = True
    if changed and cards_to_add:
        new_html = insert_after_grid(html, "\n".join(cards_to_add))
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_html)
        print(f"UPDATED {path} ({len(cards_to_add)} cards)")
    elif not changed:
        print(f"en-blog.html: no changes")


def update_blog_html(arts):
    path = os.path.join(WORK, "blog.html")
    if not os.path.exists(path):
        print(f"SKIP {path} (not found)")
        return
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()
    emojis = ["#1abc9c", "#d4367c"]
    changed = False
    cards_to_add = []
    for i, art in enumerate(arts):
        if art["file"] in html:
            print(f"{art['file']} already in blog.html — skipping")
            continue
        cards_to_add.append(card_blog(art, emojis[i % len(emojis)]) + "\n")
        changed = True
    if changed and cards_to_add:
        new_html = insert_after_grid(html, "\n".join(cards_to_add))
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_html)
        print(f"UPDATED {path} ({len(cards_to_add)} cards)")
    elif not changed:
        print(f"blog.html: no changes")


def update_sitemap(arts):
    path = os.path.join(WORK, "sitemap.xml")
    with open(path, "r", encoding="utf-8") as f:
        sm = f.read()
    changed = False
    for art in arts:
        if art["file"] in sm:
            print(f"{art['file']} already in sitemap.xml — skipping")
            continue
        block = (
            "  <url>\n"
            f"    <loc>{BASE}/{art['file']}</loc>\n"
            f"    <lastmod>{art['date']}</lastmod>\n"
            "    <changefreq>weekly</changefreq>\n"
            "    <priority>0.85</priority>\n"
            "  </url>\n"
        )
        sm = sm.replace("</urlset>", block + "</urlset>")
        changed = True
        print(f"INSERTED {art['file']} into sitemap.xml")
    if changed:
        with open(path, "w", encoding="utf-8") as f:
            f.write(sm)


if __name__ == "__main__":
    arts = [ART182, ART183]
    update_en_blog(arts)
    update_blog_html(arts)
    update_sitemap(arts)
