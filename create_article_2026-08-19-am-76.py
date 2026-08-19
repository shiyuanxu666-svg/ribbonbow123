#!/usr/bin/env python3
"""Generate 2026-08-19 AM B2B article for ribbonbow123.com — 76-Module Cross-Border Tariff Engineering & Trade Compliance Architecture."""
import os, re, sys
sys.path.insert(0, "/tmp/seo-gen")
from art76_meta import *
from art76_s1_7 import *
from art76_s8_16 import *

BASE = "/workspace/ribbonbow123"
SECTIONS = [SECTION1, SECTION2, SECTION3, SECTION4, SECTION5, SECTION6, SECTION7,
            SECTION8, SECTION9, SECTION10, SECTION11, SECTION12, SECTION13, SECTION14, SECTION15, SECTION16]


def build_article(art, sections):
    sections_html = ""
    for h2, content in sections:
        sections_html += f'\n    <section class="post-section">\n      <h2>{h2}</h2>\n      <p>{content}</p>\n    </section>\n'
    og_url = f"https://ribbonbow123.com/{art['slug']}.html"
    word_count = 1800 + int(art["read_time"]) * 30
    short_d = art["description"][:197] + "..."

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{art["short_title"]}</title>
    <meta name="description" content="{short_d}">
    <meta name="keywords" content="{art["keywords"]}">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="{og_url}">
    <meta property="og:title" content="{art["short_title"]}">
    <meta property="og:description" content="{short_d}">
    <meta property="og:type" content="article">
    <meta property="og:url" content="{og_url}">
    <meta property="og:image" content="https://ribbonbow123.com/img/banner.png">
    <meta property="og:site_name" content="Smith Ribbon">
    <meta property="og:locale" content="en_US">
    <meta property="article:published_time" content="{art["datetime"]}">
    <meta property="article:section" content="{art["category"]}">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{art["short_title"]}">
    <meta name="twitter:description" content="{short_d}">
    <link rel="stylesheet" href="styles.css">
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "headline": "{art["short_title"]}",
        "description": "{short_d}",
        "author": {{
            "@type": "Organization",
            "name": "Smith Ribbon",
            "url": "https://ribbonbow123.com"
        }},
        "publisher": {{
            "@type": "Organization",
            "name": "Smith Ribbon",
            "logo": {{
                "@type": "ImageObject",
                "url": "https://ribbonbow123.com/img/banner.png"
            }}
        }},
        "datePublished": "{art["datetime"]}",
        "dateModified": "{art["datetime"]}",
        "image": {{
            "@type": "ImageObject",
            "url": "https://ribbonbow123.com/img/banner.png"
        }},
        "mainEntityOfPage": {{
            "@type": "WebPage",
            "@id": "{og_url}"
        }},
        "keywords": "{art["keywords"]}",
        "wordCount": {word_count},
        "inLanguage": "en-US"
    }}
    </script>
</head>
<body>
<header class="site-header"></header>

<main class="blog-container">
    <article>
        <div class="blog-meta">
            <span class="blog-date">{art["date_label"]}</span>
            <span class="blog-category">{art["category"]}</span>
        </div>
        <h1>{art["short_title"]}</h1>

        <div class="blog-content">
            <p>{art["description"]}</p>
{sections_html}
        </div>

        <footer class="post-footer">
            <p><strong>{art["footer_blurb"]}</strong> <a href="contact.html">Contact us today</a> for a custom quotation and the 76-module cross-border tariff engineering &amp; trade compliance architecture onboarding package.</p>
        </footer>
    </article>
</main>

<footer class="site-footer">
    <p>&copy; 2026 Xiamen Smith Ribbon &amp; Bow Co., Ltd. All rights reserved. | <a href="https://ribbonbow123.com">ribbonbow123.com</a></p>
</footer>
</body>
</html>'''
    return html


def update_blog_html(article):
    for blog_path in [os.path.join(BASE, "en-blog.html"), os.path.join(BASE, "blog.html")]:
        if not os.path.exists(blog_path):
            continue
        with open(blog_path, "r", encoding="utf-8") as f:
            content = f.read()
        card = f'\n        <!-- AM Article - {article["date_label"]} (08:00) -->\n        <article class="blog-card">\n            <span class="blog-tag">{article["category"]}</span>\n            <h3><a href="{article["slug"]}.html">{article["short_title"]}</a></h3>\n            <p>{article["description"][:240]}...</p>\n            <div class="blog-meta">{article["date_label"]}</div>\n        </article>\n'
        patterns = [
            r'(<section class="blog-hero">.*?</p>)',
            r'(<div class="blog-hero">.*?</p>)',
            r'(<header class="blog-header">.*?</header>)',
        ]
        inserted = False
        for pattern in patterns:
            if re.search(pattern, content, flags=re.DOTALL):
                content = re.sub(pattern, r'\g<1>\n' + card, content, flags=re.DOTALL)
                inserted = True
                break
        if not inserted:
            content = re.sub(r'(</h1>)', r'\g<1>\n' + card, content, count=1)
        with open(blog_path, "w", encoding="utf-8") as f:
            f.write(content)


def update_sitemap(article):
    sitemap_path = os.path.join(BASE, "sitemap.xml")
    with open(sitemap_path, "r", encoding="utf-8") as f:
        content = f.read()

    new_url = f'''
  <url>
    <loc>https://ribbonbow123.com/{article["slug"]}.html</loc>
    <lastmod>{DATE_ISO}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>'''
    if "</urlset>" in content:
        content = content.replace("</urlset>", new_url + "\n</urlset>")
    else:
        content = content + new_url
    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write(content)


def main():
    print(f"=== Generating {DATE_ISO} AM B2B Article for ribbonbow123.com (Module #76) ===")
    art = {
        "slug": SLUG,
        "short_title": SHORT_TITLE,
        "category": CATEGORY,
        "description": DESCRIPTION,
        "keywords": KEYWORDS,
        "read_time": READ_TIME,
        "date_label": DATE_LABEL,
        "datetime": DATE_AM,
        "footer_blurb": FOOTER_BLURB,
    }
    path = os.path.join(BASE, f"{SLUG}.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(build_article(art, SECTIONS))
    print(f"  [OK] Created: {SLUG}.html")
    update_blog_html(art)
    print("  [OK] Updated: en-blog.html, blog.html")
    update_sitemap(art)
    print("  [OK] Updated: sitemap.xml")
    print("\nDone.")


if __name__ == "__main__":
    main()
