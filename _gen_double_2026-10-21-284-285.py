#!/usr/bin/env python3
"""Generate 2 B2B articles for ribbonbow123 (next slot after #283)
Article 284 AM: 7-Layer Color Governance for OEM Custom Ribbon Programs (2026-10-21)
Article 285 PM: OEM vs In-House Ribbon Manufacturing decision framework (2026-10-21)
"""
import os
import json
from pathlib import Path

DIR = "/workspace/ribbonbow123"
SITE = "ribbonbow123.com"

ART_AM_NUM = "284"
ART_AM_SLUG = "oem-custom-ribbon-7-layer-color-governance-colorimetric-delta-e-lot-continuity-private-label-2026-10-21-am"
ART_AM_TITLE = "OEM Custom Ribbon Color Governance: The 7-Layer System for Controlling Color Drift Across Multi-Lot Production Programs (2026)"
ART_AM_DESC = "A 2026 color governance playbook for brand owners, category managers and QC leads running OEM custom ribbon programs. Covers the 7-layer ribbon color governance system — colorimetric standard, Delta E tolerance bands by application risk, lot continuity bridging, substrate declaration, print registration and ink system control, cross-illuminant metamerism testing, and change control with a substitution register — plus the business case for standing the system up."
ART_AM_KEYWORDS = "ribbon color governance, OEM custom ribbon color control, Delta E tolerance ribbon, ribbon lot continuity, metamerism ribbon testing, ribbon spectrophotometer standard, printed ribbon registration tolerance, private label ribbon color drift, B2B ribbon quality 2026, ribbon substitution register change control"

ART_PM_NUM = "285"
ART_PM_SLUG = "oem-vs-in-house-ribbon-manufacturing-insourcing-outsourcing-fixed-cost-tco-decision-framework-2026-10-21-pm"
ART_PM_TITLE = "OEM vs In-House Ribbon Manufacturing: The Fixed-Cost, Scale-Threshold and Risk-Asymmetry Decision Framework (2026)"
ART_PM_DESC = "A 2026 make-versus-buy playbook for brand owners, sourcing directors and category buyers evaluating insourcing custom ribbon manufacturing. Covers the hidden fixed-cost stack, the sustained-volume scale threshold, the risk asymmetry of lost-season exposure, the hybrid control model with dual sourcing and managed assets, and a five-question decision framework with defined thresholds."
ART_PM_KEYWORDS = "OEM vs in-house ribbon manufacturing, make or buy ribbon, insource ribbon conversion, ribbon manufacturing fixed costs, dual sourcing ribbon, managed asset model, B2B sourcing strategy 2026, private label make buy decision, ribbon supplier vs mill ownership"

DATE_AM = "2026-10-21T08:00:00+08:00"
DATE_PM = "2026-10-21T13:00:00+08:00"
DATE_AM_ISO = "2026-10-21"
DATE_PM_ISO = "2026-10-21"
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
        <p>&copy; 2026 Smith Ribbon Co., Ltd. (Xiamen Meisida Decoration Co., Ltd.) | OEM &amp; ODM Custom Ribbon Manufacturer</p>
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
    am_json = Path("/tmp/am_sections_2026_10_21_b.json")
    pm_json = Path("/tmp/pm_sections_2026_10_21_b.json")
    if not am_json.exists() or not pm_json.exists():
        print("Missing sections JSON files. Run section writer first.")
        return
    am_sections = json.loads(am_json.read_text())
    pm_sections = json.loads(pm_json.read_text())

    os.chdir(DIR)

    am_filename = f"blog-{ART_AM_SLUG}.html"
    am_html = build_html(ART_AM_NUM, ART_AM_SLUG, ART_AM_TITLE, ART_AM_DESC, ART_AM_KEYWORDS,
                         DATE_AM_ISO, "October 21, 2026 (08:00 CST)", am_sections, DATE_AM)
    Path(am_filename).write_text(am_html)
    print(f"Wrote {am_filename}")

    pm_filename = f"blog-{ART_PM_SLUG}.html"
    pm_html = build_html(ART_PM_NUM, ART_PM_SLUG, ART_PM_TITLE, ART_PM_DESC, ART_PM_KEYWORDS,
                         DATE_PM_ISO, "October 21, 2026 (13:00 CST)", pm_sections, DATE_PM)
    Path(pm_filename).write_text(pm_html)
    print(f"Wrote {pm_filename}")


if __name__ == "__main__":
    main()
