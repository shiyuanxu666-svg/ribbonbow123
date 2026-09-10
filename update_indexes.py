"""Update en-blog.html and sitemap.xml with the two new articles."""
import os, re

WORK = "/workspace/ribbonbow123"
BASE = "https://ribbonbow123.com"
TODAY = "2026-09-10"

ART141 = {
    "file": "blog-ribbon-oem-b2b-141-module-mill-side-master-service-agreement-msa-statement-of-work-sow-governance-architecture-b2b-oem-program-resilience-2026-09-10-am.html",
    "title": "Ribbon OEM B2B 141-Module: Mill-Side MSA & SOW Governance Architecture for B2B OEM Program Resilience",
    "cat": "MSA / SOW Governance",
    "date": "2026-09-10",
    "desc": "22-clause MSA + 18-clause SOW + 15-stage change-control + 13-tier SLA matrix + 11-stage governance RACI. Compress contract cycle 19-32%.",
}

ART142 = {
    "file": "blog-ribbon-oem-b2b-142-module-mill-side-18-stage-on-site-factory-acceptance-test-fat-pre-shipment-quality-engineering-architecture-b2b-oem-program-resilience-2026-09-10-pm.html",
    "title": "Ribbon OEM B2B 142-Module: 18-Stage On-Site FAT & Pre-Shipment Quality-Engineering Architecture for B2B OEM Program Resilience",
    "cat": "FAT & Pre-Shipment QA",
    "date": "2026-09-10",
    "desc": "18-stage on-site FAT + 5 engineering lanes + 4 sampling tiers + 3 photo-evidence layers. Lift AQL pass 3.2pp, cut rework 71%.",
}


def build_card(art, emoji):
    return (
        f'<a href="{art["file"]}" class="blog-card-link" style="text-decoration:none;color:inherit;">'
        f'<div class="blog-card">'
        f'<div class="blog-card-image" style="background:linear-gradient(135deg,#1a5276,{emoji});">{emoji}</div>'
        f'<div class="blog-card-content">'
        f'<span class="blog-card-category">{art["cat"]}</span>'
        f'<h3><a href="{art["file"]}">{art["title"]}</a></h3>'
        f'<div class="blog-card-meta">📅 {art["date"]} · ⏱ 26 min read</div>'
        f'<div class="blog-card-desc">{art["desc"]}</div>'
        f'<span class="read-more">Read full playbook →</span>'
        f'</div></div></a>'
    )


def update_en_blog():
    path = os.path.join(WORK, "en-blog.html")
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()

    # Find a marker to insert before. The blog.html uses blog-card grid. Look for the existing most recent b2b-140 article.
    # If 140 exists, insert before its block; else before the first blog-card div.
    m = re.search(r'(<div class="blog-grid">)(.*?)(</div>\s*<footer)', html, re.DOTALL)
    if not m:
        # Try simpler pattern
        m = re.search(r'(<div class="blog-grid">)', html)
        if not m:
            print("ERROR: cannot find blog-grid in en-blog.html")
            return
        grid_start = m.end()
        # find end of grid - assume first closing </div></div> after many cards
        # Use a more flexible pattern - just look for next cta-section
        end_m = re.search(r'<div class="cta-section">', html[grid_start:])
        grid_end = grid_start + end_m.start() if end_m else grid_start + 5000
    else:
        grid_start = m.end(1)
        grid_end = m.start(2) + len(m.group(2))

    # Detect existing recent markers
    has140 = "b2b-140" in html
    has139 = "b2b-139" in html
    print(f"Existing b2b-140 in en-blog.html: {has140}, b2b-139: {has139}")

    card141 = build_card(ART141, "#159895")
    card142 = build_card(ART142, "#d4367c")
    new_cards = card141 + "\n" + card142 + "\n"

    # Insert at top of grid
    new_html = html[:grid_start] + "\n" + new_cards + html[grid_start:]
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_html)
    print(f"UPDATED {path}  (added 2 cards at top of grid)")


def update_sitemap():
    path = os.path.join(WORK, "sitemap.xml")
    with open(path, "r", encoding="utf-8") as f:
        sm = f.read()

    # Check if 141/142 already there
    for art in (ART141, ART142):
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
        # Insert before </urlset>
        sm = sm.replace("</urlset>", block + "</urlset>")
        print(f"INSERTED into sitemap.xml: {art['file']}")

    with open(path, "w", encoding="utf-8") as f:
        f.write(sm)
    print(f"UPDATED {path}")


if __name__ == "__main__":
    update_en_blog()
    update_sitemap()
