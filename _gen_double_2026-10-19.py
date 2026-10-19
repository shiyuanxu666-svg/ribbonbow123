#!/usr/bin/env python3
"""Generate 2 B2B articles for ribbonbow123 (2026-10-19 AM/PM)
Article 275 AM: OEM Private Label Ribbon Program Risk Mitigation Architecture (Q1 2027)
Article 276 PM: Custom Branded Ribbon OEM Cost Analysis 25-Component Hidden Landed Cost Decoder (Tariff-Aware)
"""
import os
import json
from pathlib import Path

DIR = "/workspace/ribbonbow123"
SITE = "ribbonbow123.com"

ART_AM_NUM = "275"
ART_AM_SLUG = "oem-private-label-ribbon-program-risk-mitigation-26-shock-14-recovery-pillar-architecture-b2b-procurement-2026-10-19-am"
ART_AM_TITLE = "OEM Private Label Ribbon Program Risk Mitigation: The 26-Shock, 14-Recovery-Pillar Architecture for Resilient B2B Private-Label Programs (2026 Q1 2027 Outlook)"
ART_AM_DESC = "A 2026 private-label OEM risk-mitigation playbook for global brand procurement, retail merchandising, and private-label controllers. Built for procurement directors, category managers, and sourcing managers running custom-branded ribbon programs across China, Vietnam, and India. Covers the 26-shock taxonomy (geopolitical, climate, FX, tariff, capacity, IP, quality, compliance, freight, cyber), the 14-recovery-pillar architecture, dual-sourcing bridge-order migration, safety-stock dynamic-replenishment, supplier-financial-health tier-2/tier-3 12-signal monitoring, and the Q1 2027 holiday-peak Valentine cascade. Engineered to lift program-resilience score 41 to 78 percent, compress shock-to-recovery MTTR 38 to 11 days, and protect 180,000 to 420,000 USD in private-label program revenue across the FY2026 to FY2028 horizon."
ART_AM_KEYWORDS = "OEM private label ribbon risk mitigation, private label program resilience, custom ribbon supplier risk tiering, ribbon dual sourcing strategy, ribbon supplier financial health, ribbon safety stock VMI, ribbon bridge order migration, ribbon factory tier 1 tier 2 tier 3, private label Q1 2027 capacity pre booking, ribbon geopolitical tariff shock, ribbon FX hedging forward contract, ribbon holiday peak Valentine capacity, B2B private label procurement 2026"

ART_PM_NUM = "276"
ART_PM_SLUG = "oem-ribbon-cost-analysis-hidden-landed-cost-decoder-25-component-should-cost-tariff-aware-multi-currency-fx-hedging-b2b-procurement-2026-10-19-pm"
ART_PM_TITLE = "OEM Ribbon Cost Analysis Hidden Landed Cost Decoder: The 25-Component Should-Cost Model with Tariff-Aware Multi-Currency FX Hedging for B2B Procurement (2026)"
ART_PM_DESC = "A 2026 cost-analysis and landed-cost-engineering playbook for OEM ribbon procurement. Built for procurement controllers, sourcing finance managers, and category buyers evaluating custom-branded ribbon quotes from Asia-based OEM mills. Covers the 25-component should-cost decoder (yarn, dye, weave, finish, conversion, overhead, tooling, sampling, packaging, freight, tariff, duty, FTA drawback, CBAM carbon, FX hedge, last-mile), the tariff-aware 9-scenario sensitivity heat-map across HS 5806/5807/5808, multi-currency FX hedging with forward contracts and NDF, EU CBAM Phase-2 carbon-adjusted TCO, dual-sourcing split-order migration, and supplier benchmark anonymization. Engineered to lift quote-transparency 38 to 71 percent, deliver 6 to 14 percent landed-cost savings, and recover 42,000 to 138,000 USD across the FY2026 to FY2028 horizon."
ART_PM_KEYWORDS = "OEM ribbon cost analysis, hidden landed cost decoder, ribbon should cost 25 component, ribbon tariff aware cost, ribbon FX hedging forward contract, ribbon CBAM carbon adjusted cost, ribbon HS code 5806 5807 5808, ribbon FTA duty drawback, ribbon multi currency procurement, custom ribbon supplier benchmarking, ribbon OEM quote decoder, B2B ribbon procurement 2026"

DATE_AM = "2026-10-19T08:00:00+08:00"
DATE_PM = "2026-10-19T13:00:00+08:00"
DATE_AM_ISO = "2026-10-19"
DATE_PM_ISO = "2026-10-19"
AUTHOR_NAME = "Smith Ribbon Co., Ltd."
AUTHOR_URL = "https://ribbonbow123.com"
LOGO_URL = "https://ribbonbow123.com/img/banner.png"

def build_html(article_num, slug, title, desc, keywords, date_iso, date_display, sections, date_attr):
    url = f"https://{SITE}/{slug}.html"
    sections_html = []
    for h2_title, paragraph in sections:
        sections_html.append(
            f'        <h2>{h2_title}</h2>\n'
            f'        <p>{paragraph}</p>'
        )
    body = "\n\n".join(sections_html)
    schema_article = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": title,
        "description": desc,
        "author": {"@type": "Organization", "name": AUTHOR_NAME, "url": AUTHOR_URL},
        "publisher": {"@type": "Organization", "name": AUTHOR_NAME, "url": SITE},
        "datePublished": date_iso,
        "dateModified": date_iso,
        "mainEntityOfPage": {"@type": "WebPage", "@id": url}
    }
    schema_blog = {
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "headline": title,
        "description": desc,
        "image": LOGO_URL,
        "author": {"@type": "Organization", "name": AUTHOR_NAME, "url": AUTHOR_URL},
        "publisher": {
            "@type": "Organization",
            "name": AUTHOR_NAME,
            "logo": {"@type": "ImageObject", "url": LOGO_URL}
        },
        "datePublished": date_iso,
        "dateModified": date_iso,
        "mainEntityOfPage": {"@type": "WebPage", "@id": url},
        "keywords": keywords,
        "articleSection": "B2B Sourcing",
        "wordCount": sum(len(p.split()) + len(h.split()) for h, p in sections) + 200
    }
    sa = json.dumps(schema_article, indent=4, ensure_ascii=False)
    sb = json.dumps(schema_blog, indent=4, ensure_ascii=False)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Smith Ribbon</title>
    <meta name="description" content="{desc}">
    <meta name="keywords" content="{keywords}">
    <meta name="robots" content="index, follow">
    <meta name="geo.region" content="CN-35" />
    <meta name="geo.placename" content="Xiamen, Fujian, China" />
    <link rel="canonical" href="{url}">
    <!-- Open Graph -->
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{desc}">
    <meta property="og:type" content="article">
    <meta property="og:image" content="{LOGO_URL}">
    <meta property="og:site_name" content="Smith Ribbon">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{title}">
    <meta name="twitter:description" content="{desc}">
    <meta name="twitter:image" content="{LOGO_URL}">
    <meta property="og:url" content="{url}">
    <meta property="og:locale" content="en_US">
    <meta property="article:published_time" content="{date_attr}">
    <meta property="article:modified_time" content="{date_attr}">
    <meta property="article:author" content="{AUTHOR_NAME}">
    <meta property="article:section" content="B2B Sourcing">
    <!-- Article Schema -->
    <script type="application/ld+json">
{sa}
    </script>
    <script type="application/ld+json">
{sb}
    </script>
    <style>
        :root {{ --primary: #e91e63; --secondary: #9c27b0; --dark: #2c3e50; --light: #f8f9fa; --text: #333; --muted: #666; --border: #e0e0e0; --accent: #0066cc; }}
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; line-height: 1.8; color: var(--text); background: #fafafa; }}
        a {{ color: var(--primary); text-decoration: none; }}
        a:hover {{ text-decoration: underline; }}
        nav {{ background: white; padding: 1rem 2rem; display: flex; justify-content: space-between; align-items: center; box-shadow: 0 2px 10px rgba(0,0,0,0.08); position: sticky; top: 0; z-index: 100; }}
        .logo {{ font-size: 1.6rem; font-weight: bold; color: var(--primary); }}
        .container {{ max-width: 960px; margin: 0 auto; padding: 2rem 1.5rem; background: white; }}
        h1 {{ font-size: 2.2rem; color: var(--dark); margin: 1.5rem 0 1rem; line-height: 1.3; }}
        h2 {{ font-size: 1.4rem; color: var(--dark); margin: 2rem 0 0.8rem; padding-top: 1rem; border-top: 2px solid var(--light); }}
        p {{ margin-bottom: 1rem; font-size: 1.05rem; }}
        .meta {{ color: var(--muted); font-size: 0.9rem; margin-bottom: 1rem; }}
        .toc {{ background: var(--light); padding: 1.2rem; border-radius: 8px; margin: 1.5rem 0; }}
        .toc h3 {{ margin-bottom: 0.6rem; color: var(--dark); }}
        .toc ol {{ padding-left: 1.4rem; }}
        .toc li {{ margin-bottom: 0.3rem; font-size: 0.95rem; }}
        footer {{ background: var(--dark); color: white; padding: 2rem; text-align: center; margin-top: 3rem; }}
        footer a {{ color: #fff; margin: 0 8px; }}
    </style>
</head>
<body>
    <nav>
        <div class="logo">Smith Ribbon</div>
        <div><a href="https://ribbonbow123.com/">Home</a> | <a href="https://ribbonbow123.com/blog.html">Blog</a> | <a href="https://ribbonbow123.com/about.html">About</a></div>
    </nav>
    <div class="container">
        <h1>{title}</h1>
        <p class="meta">By {AUTHOR_NAME} | Published {date_display} | Category: B2B Sourcing | Article #{article_num}</p>
        <div class="toc">
            <h3>Table of Contents</h3>
            <ol>
{chr(10).join(f'                <li>{h}</li>' for h, _ in sections)}
            </ol>
        </div>
{body}
    </div>
    <footer>
        <p>&copy; 2026 Smith Ribbon Co., Ltd. (Xiamen Meisida Decoration Co., Ltd.) | OEM & ODM Custom Ribbon Manufacturer</p>
        <p>
            <a href="https://ribbonbow123.com/">Home</a>
            <a href="https://ribbonbow123.com/blog.html">Blog</a>
            <a href="https://ribbonbow123.com/about.html">About</a>
            <a href="mailto:xmmsd@126.com">Contact</a>
        </p>
    </footer>
</body>
</html>
"""
    return html


def main():
    am_json = Path("/tmp/am_sections_2026_10_19.json")
    pm_json = Path("/tmp/pm_sections_2026_10_19.json")
    if not am_json.exists() or not pm_json.exists():
        print("Missing sections JSON files. Run section writer first.")
        return
    am_sections = json.loads(am_json.read_text())
    pm_sections = json.loads(pm_json.read_text())

    os.chdir(DIR)

    am_filename = f"blog-{ART_AM_SLUG}.html"
    am_html = build_html(ART_AM_NUM, ART_AM_SLUG, ART_AM_TITLE, ART_AM_DESC, ART_AM_KEYWORDS,
                         DATE_AM_ISO, "October 19, 2026 (08:00 CST)", am_sections, DATE_AM)
    Path(am_filename).write_text(am_html)
    print(f"Wrote {am_filename}")

    pm_filename = f"blog-{ART_PM_SLUG}.html"
    pm_html = build_html(ART_PM_NUM, ART_PM_SLUG, ART_PM_TITLE, ART_PM_DESC, ART_PM_KEYWORDS,
                         DATE_PM_ISO, "October 19, 2026 (13:00 CST)", pm_sections, DATE_PM)
    Path(pm_filename).write_text(pm_html)
    print(f"Wrote {pm_filename}")

if __name__ == "__main__":
    main()
