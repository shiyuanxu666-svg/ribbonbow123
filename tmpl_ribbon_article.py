#!/usr/bin/env python3
"""Shared HTML template for ribbonbow123 B2B articles (2026-10-25 cron slot).
Extracted from the established _gen_article_293/294 pattern so that both
new articles render identically to the existing corpus.
"""
import json
import html as html_mod

STYLE_CSS = """
        :root { --primary: #6a1b9a; --secondary: #8e24aa; --dark: #2c1a33; --light: #f8f5fb; --text: #2d2b2e; --muted: #6b6570; --accent: #c62828; }
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; line-height: 1.8; color: var(--text); background: var(--light); }
        a { color: var(--primary); text-decoration: none; }
        a:hover { text-decoration: underline; }
        nav { background: white; padding: 1rem 2rem; display: flex; justify-content: space-between; align-items: center; box-shadow: 0 2px 10px rgba(0,0,0,0.08); position: sticky; top: 0; z-index: 100; }
        .logo { font-size: 1.6rem; font-weight: bold; color: var(--primary); }
        .container { max-width: 960px; margin: 0 auto; padding: 2rem 1.5rem; background: white; }
        h1 { font-size: 2.1rem; color: var(--dark); margin: 1.5rem 0 1rem; line-height: 1.3; }
        h2 { font-size: 1.4rem; color: var(--dark); margin: 2rem 0 0.8rem; padding-top: 1rem; border-top: 2px solid var(--light); }
        h3 { font-size: 1.1rem; color: var(--dark); margin: 1rem 0 0.4rem; }
        p { margin-bottom: 1rem; font-size: 1.05rem; }
        .meta { color: var(--muted); font-size: 0.9rem; margin-bottom: 1rem; }
        .toc { background: var(--light); padding: 1.2rem; border-radius: 8px; margin: 1.5rem 0; }
        .toc h3 { margin-bottom: 0.6rem; color: var(--dark); }
        .toc ol { padding-left: 1.4rem; }
        .toc li { margin-bottom: 0.3rem; font-size: 0.95rem; }
        .kpi-box { background: #f7f0fb; border-left: 4px solid var(--primary); padding: 1rem 1.2rem; border-radius: 6px; margin: 1.5rem 0; }
        .kpi-box ul { margin: 0.6rem 0 0 1.1rem; padding: 0; }
        .faq h3 { color: var(--primary); }
        footer { background: var(--dark); color: white; padding: 2rem; text-align: center; margin-top: 3rem; }
        footer a { color: #fff; margin: 0 8px; }
"""


def faq_block_html(items):
    out = ['        <h2>Frequently Asked Questions</h2>', '        <div class="faq">']
    for q, a in items:
        out.append(f'            <h3>{html_mod.escape(q)}</h3>')
        out.append(f'            <p>{a}</p>')
    out.append('        </div>')
    return "\n".join(out)


def kpi_block_html(metrics):
    items = "".join(
        f"<li><strong>{html_mod.escape(k)}</strong> &mdash; {html_mod.escape(v)}</li>"
        for k, v in metrics
    )
    return f'<div class="kpi-box"><h2>Quantified Outcomes</h2><ul>{items}</ul></div>'


def build_html(cfg):
    """cfg is a dict with: url, title, desc, keywords, date_iso, date_display,
    num, sections, faq, metrics, author_bullets, author_name, author_url,
    logo_url, site, closing_paragraph, closing_cta, h2_title."""
    SITE = cfg["site"]
    TITLE = cfg["title"]
    DESC = cfg["desc"]
    KEYWORDS = cfg["keywords"]
    DATE_ISO = cfg["date_iso"]
    DATE_DISPLAY = cfg["date_display"]
    NUM = cfg["num"]
    SECTIONS = cfg["sections"]
    FAQ = cfg["faq"]
    METRICS = cfg["metrics"]
    AUTHOR_BULLETS = cfg["author_bullets"]
    AUTHOR_NAME = cfg["author_name"]
    AUTHOR_URL = cfg["author_url"]
    LOGO_URL = cfg["logo_url"]
    url = cfg["url"]

    word_count = sum(len(p.split()) + len(h.split()) for h, p in SECTIONS) + 240
    plain_title = html_mod.unescape(TITLE)
    article_schema = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": plain_title,
        "description": DESC,
        "author": {"@type": "Organization", "name": AUTHOR_NAME, "url": AUTHOR_URL},
        "publisher": {"@type": "Organization", "name": AUTHOR_NAME, "url": SITE},
        "datePublished": DATE_ISO.split("T")[0],
        "dateModified": DATE_ISO.split("T")[0],
        "mainEntityOfPage": {"@type": "WebPage", "@id": url},
        "keywords": KEYWORDS,
    }
    blog_schema = {
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "headline": plain_title,
        "description": DESC,
        "image": LOGO_URL,
        "author": {"@type": "Organization", "name": AUTHOR_NAME, "url": AUTHOR_URL},
        "publisher": {
            "@type": "Organization",
            "name": AUTHOR_NAME,
            "logo": {"@type": "ImageObject", "url": LOGO_URL},
        },
        "datePublished": DATE_ISO.split("T")[0],
        "dateModified": DATE_ISO.split("T")[0],
        "mainEntityOfPage": {"@type": "WebPage", "@id": url},
        "keywords": KEYWORDS,
        "articleSection": "B2B Sourcing",
        "wordCount": word_count,
    }
    faq_schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": html_mod.escape(q),
                "acceptedAnswer": {"@type": "Answer", "text": html_mod.escape(a)},
            }
            for q, a in FAQ
        ],
    }
    sf = json.dumps(faq_schema, indent=4, ensure_ascii=False)
    sa = json.dumps(article_schema, indent=4, ensure_ascii=False)
    sb = json.dumps(blog_schema, indent=4, ensure_ascii=False)
    toc_html = "\n".join(f"                <li>{html_mod.escape(h)}</li>" for h, _ in SECTIONS)
    body_parts = []
    for h, p in SECTIONS:
        body_parts.append(f'        <h2>{html_mod.escape(h)}</h2>')
        body_parts.append(f'        <p>{p}</p>')
    body = "\n\n".join(body_parts)
    faq_html = faq_block_html(FAQ)
    metrics_html = kpi_block_html(METRICS)
    bullets_html = "".join(f"<li>{b}</li>" for b in AUTHOR_BULLETS)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{TITLE} | Smith Ribbon</title>
    <meta name="description" content="{html_mod.escape(DESC)}">
    <meta name="keywords" content="{html_mod.escape(KEYWORDS)}">
    <meta name="robots" content="index, follow">
    <meta name="geo.region" content="CN-35" />
    <meta name="geo.placename" content="Xiamen, Fujian, China" />
    <link rel="canonical" href="{url}">
    <meta property="og:title" content="{TITLE}">
    <meta property="og:description" content="{html_mod.escape(DESC)}">
    <meta property="og:type" content="article">
    <meta property="og:image" content="{LOGO_URL}">
    <meta property="og:site_name" content="Smith Ribbon">
    <meta property="og:url" content="{url}">
    <meta property="og:locale" content="en_US">
    <meta property="article:published_time" content="{DATE_ISO}">
    <meta property="article:modified_time" content="{DATE_ISO}">
    <meta property="article:author" content="{AUTHOR_NAME}">
    <meta property="article:section" content="B2B Sourcing">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{TITLE}">
    <meta name="twitter:description" content="{html_mod.escape(DESC)}">
    <meta name="twitter:image" content="{LOGO_URL}">
    <script type="application/ld+json">
{sa}
    </script>
    <script type="application/ld+json">
{sb}
    </script>
    <script type="application/ld+json">
{sf}
    </script>
    <style>{STYLE_CSS}</style>
</head>
<body>
    <nav>
        <div class="logo">Smith Ribbon</div>
        <div><a href="https://ribbonbow123.com/">Home</a> | <a href="https://ribbonbow123.com/blog.html">Blog</a> | <a href="https://ribbonbow123.com/about.html">About</a></div>
    </nav>
    <div class="container">
        <h1>{TITLE}</h1>
        <p class="meta">By {html_mod.escape(AUTHOR_NAME)} | Published {html_mod.escape(DATE_DISPLAY)} | Category: B2B Sourcing | Article #{NUM}</p>
        <div class="toc">
            <h3>Table of Contents</h3>
            <ol>
{toc_html}
            </ol>
        </div>

{body}

{metrics_html}

{faq_html}

        <h2>{cfg["h2_title"]}</h2>
        <p>{cfg["closing_paragraph"]}</p>
        <ul>
            {bullets_html}
        </ul>
        <p>{cfg["closing_cta"]}</p>
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


def write_article(cfg, dir_path, site, slug, date):
    from pathlib import Path
    out = build_html(cfg)
    Path(f"{dir_path}/blog-{slug}.html").write_text(out, encoding="utf-8")
    print(f"Wrote blog-{slug}.html ({len(out):,} bytes)")

    sm_path = Path(f"{dir_path}/sitemap.xml")
    sm = sm_path.read_text(encoding="utf-8")
    url = f"https://{site}/blog-{slug}.html"
    if url in sm:
        print(f"[skip] sitemap already has article {cfg['num']}")
    else:
        entry = (
            "  <url>\n"
            f"    <loc>{url}</loc>\n"
            f"    <lastmod>{date}</lastmod>\n"
            "    <changefreq>monthly</changefreq>\n"
            "    <priority>0.7</priority>\n"
            "  </url>\n"
        )
        idx = sm.rfind("</urlset>")
        if idx == -1:
            raise SystemExit("</urlset> not found in sitemap.xml")
        sm_path.write_text(sm[:idx] + entry + sm[idx:], encoding="utf-8")
        print(f"[ok] sitemap.xml updated with article {cfg['num']}")
