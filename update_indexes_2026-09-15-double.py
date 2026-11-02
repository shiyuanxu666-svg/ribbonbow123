"""Update en-blog.html, blog.html and sitemap.xml with the two new articles (164, 165) - 2026-09-15."""
import os, re

WORK = "/workspace/ribbonbow123"
BASE = "https://ribbonbow123.com"
TODAY = "2026-09-15"

ART164 = {
    "file": "blog-ribbon-oem-b2b-164-module-mill-side-q1-2027-ai-augmented-hidden-cost-radar-should-cost-reverse-engineering-architecture-b2b-oem-program-resilience-2026-09-15-am.html",
    "title": "Ribbon OEM B2B 164-Module: Mill-Side Q1-2027 AI-Augmented Hidden-Cost Radar & Should-Cost Reverse-Engineering Architecture for B2B OEM Program Resilience",
    "cat": "Q1-2027 AI-Augmented Hidden-Cost Radar",
    "date": "2026-09-15",
    "desc": "21-stage AI-augmented hidden-cost radar + 17-component should-cost reverse-engineering + 13-stage landed-cost engineering + 11-stage cost-driver heat-map + 9-stage supplier-quote benchmark + 7-stage carbon-adjusted TCO + 5-stage multi-currency FX hedging + 3-stage tariff-aware cost architecture. Cut landed-cost 19-38%, lift hidden-cost detection 24-41%, recover margin 11-23pp.",
}

ART165 = {
    "file": "blog-ribbon-oem-b2b-165-module-mill-side-q1-2027-supplier-certification-compliance-decoder-25-credential-roi-architecture-b2b-oem-program-resilience-2026-09-15-pm.html",
    "title": "Ribbon OEM B2B 165-Module: Mill-Side Q1-2027 Supplier-Certification & Compliance Decoder with 25-Credential ROI Architecture for B2B OEM Program Resilience",
    "cat": "Q1-2027 Supplier-Certification & Compliance Decoder",
    "date": "2026-09-15",
    "desc": "25-credential certification-and-compliance decoder + 21-stage tender-and-RFP qualification + 17-stage retailer-onboarding matrix + 13-stage audit-cycle management + 11-stage cost-of-non-compliance architecture + 9-stage credential-renewal calendar + 7-stage multi-stakeholder sign-off + 5-stage CSRD-ESRS-CBAM-disclosure + 3-stage co-branded rights-clearance. Lift tender-shortlist 21-39%, compress retailer-onboarding 18-34%, avoid cost-of-non-compliance 9-19pp.",
}


def build_card_en(art, emoji):
    return (
        f'<a href="{art["file"]}" class="blog-card-link" style="text-decoration:none;color:inherit;">'
        f'<div class="blog-card">'
        f'<div class="blog-card-image" style="background:linear-gradient(135deg,#1a5276,{emoji});">{emoji}</div>'
        f'<div class="blog-card-content">'
        f'<span class="blog-card-category">{art["cat"]}</span>'
        f'<h3><a href="{art["file"]}">{art["title"]}</a></h3>'
        f'<div class="blog-card-meta">📅 {art["date"]} · ⏱ 27-28 min read</div>'
        f'<div class="blog-card-desc">{art["desc"]}</div>'
        f'<span class="read-more">Read full playbook →</span>'
        f'</div></div></a>'
    )


def build_card_blog_html(art, emoji):
    """For the larger blog.html (uses different markup)."""
    return (
        f'<article class="blog-post-card" data-category="{art["cat"]}">\n'
        f'  <a href="{art["file"]}" class="blog-post-thumb" style="background:linear-gradient(135deg,#1a5276,{emoji});" aria-label="{art["title"][:60]}"></a>\n'
        f'  <div class="blog-post-content">\n'
        f'    <span class="blog-post-category">{art["cat"]}</span>\n'
        f'    <h3 class="blog-post-title"><a href="{art["file"]}">{art["title"]}</a></h3>\n'
        f'    <div class="blog-post-meta">📅 {art["date"]} · ⏱ 27-28 min read</div>\n'
        f'    <p class="blog-post-excerpt">{art["desc"]}</p>\n'
        f'    <a href="{art["file"]}" class="blog-post-link">Read full playbook →</a>\n'
        f'  </div>\n'
        f'</article>\n'
    )


def insert_into_grid(html, new_cards, marker_substring):
    """Insert new_cards at the start of the first blog-grid block in html, after marker_substring exists."""
    if marker_substring in html:
        m = re.search(r'(<div class="blog-grid">)', html)
        if m:
            grid_start = m.end()
            return html[:grid_start] + "\n" + new_cards + html[grid_start:]
    return None


def update_en_blog():
    path = os.path.join(WORK, "en-blog.html")
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()

    has164 = "b2b-164" in html
    has165 = "b2b-165" in html
    print(f"Existing b2b-164 in en-blog.html: {has164}, b2b-165: {has165}")
    if has164 and has165:
        print("Both articles already in en-blog.html, skipping")
        return

    new_cards = build_card_en(ART164, "#2a9d8f") + "\n" + build_card_en(ART165, "#7b2cbf") + "\n"
    new_html = insert_into_grid(html, new_cards, "b2b-")
    if new_html is None:
        print("ERROR: could not find blog-grid in en-blog.html")
        return

    with open(path, "w", encoding="utf-8") as f:
        f.write(new_html)
    print(f"UPDATED {path}  (added 2 cards at top of grid)")


def update_blog_html():
    """Update the larger blog.html (the original ribbonbow123 blog index)."""
    path = os.path.join(WORK, "blog.html")
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()

    if "b2b-164" in html and "b2b-165" in html:
        print("Both articles already in blog.html, skipping")
        return

    new_cards = build_card_blog_html(ART164, "#2a9d8f") + "\n" + build_card_blog_html(ART165, "#7b2cbf") + "\n"
    new_html = insert_into_grid(html, new_cards, "blog-post")
    if new_html is None:
        m = re.search(r'(<div\s+class="posts-grid")', html) or re.search(r'(<ul\s+class="blog-list")', html) or re.search(r'(<div\s+class="blog-list")', html)
        if m:
            grid_start = m.end()
            new_html = html[:grid_start] + ">\n" + new_cards + html[grid_start:]
    if new_html is None:
        print(f"WARNING: could not find grid in blog.html, falling back to manual injection before </body>")
        new_html = html.replace("</body>", new_cards + "\n</body>")

    with open(path, "w", encoding="utf-8") as f:
        f.write(new_html)
    print(f"UPDATED {path}  (added 2 cards)")


def update_sitemap():
    path = os.path.join(WORK, "sitemap.xml")
    with open(path, "r", encoding="utf-8") as f:
        sm = f.read()

    for art in (ART164, ART165):
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
        print(f"INSERTED into sitemap.xml: {art['file']}")

    with open(path, "w", encoding="utf-8") as f:
        f.write(sm)
    print(f"UPDATED {path}")


if __name__ == "__main__":
    update_en_blog()
    update_blog_html()
    update_sitemap()