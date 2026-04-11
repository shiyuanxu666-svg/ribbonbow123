#!/bin/bash
# 🕷️ SEO自动检查脚本 — Smith Ribbon
# 使用：bash seo-check.sh
# 建议：通过 cron 每周自动运行，结果输出到日志

set -e

REPORT_FILE="/workspace/ribbonbow123/seo-toolkit/weekly-seo-report-$(date +%Y-%m-%d).txt"
SITE="https://ribbonbow123.com"
TODAY=$(date "+%Y-%m-%d %H:%M UTC")

echo "🎀 Smith Ribbon — Weekly SEO Check" > "$REPORT_FILE"
echo "Generated: $TODAY" >> "$REPORT_FILE"
echo "=================================" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"

check_url() {
  local url="$1"
  local name="$2"
  local code
  code=$(curl -s -o /dev/null -w "%{http_code}" --max-time 10 "$url" 2>/dev/null || echo "ERR")
  if [ "$code" = "200" ]; then
    echo "✅ $name: HTTP $code" >> "$REPORT_FILE"
  else
    echo "❌ $name: HTTP $code" >> "$REPORT_FILE"
  fi
}

echo "[1] Checking Key Pages..." >> "$REPORT_FILE"
check_url "${SITE}/"              "Homepage"
check_url "${SITE}/sitemap.xml"  "Sitemap XML"
check_url "${SITE}/robots.txt"    "Robots.txt"
check_url "${SITE}/keywords.html" "Keywords page"
echo "" >> "$REPORT_FILE"

echo "[2] Checking Blog Pages (sample)..." >> "$REPORT_FILE"
for blog in \
  "${SITE}/blog-custom-printed-ribbon.html" \
  "${SITE}/blog-satin-ribbon-manufacturing-oem-guide-2026.html" \
  "${SITE}/blog-wholesale-ribbon-sourcing-guide.html"; do
  check_url "$blog" "$(basename $blog)"
done
echo "" >> "$REPORT_FILE"

echo "[3] Checking Product Pages (sample)..." >> "$REPORT_FILE"
for prod in \
  "${SITE}/products-printed-ribbons.html" \
  "${SITE}/products-satin-ribbons.html" \
  "${SITE}/products-jacquard-ribbons.html"; do
  check_url "$prod" "$(basename $prod)"
done
echo "" >> "$REPORT_FILE"

echo "[4] Checking SEO Tags..." >> "$REPORT_FILE"
canonical=$(curl -s --max-time 10 "${SITE}/" | grep -oP 'rel="canonical"[^>]+href="[^"]+"' | head -1)
if [ -n "$canonical" ]; then
  echo "✅ Canonical: $canonical" >> "$REPORT_FILE"
else
  echo "❌ Canonical tag MISSING on homepage!" >> "$REPORT_FILE"
fi

org_schema=$(curl -s --max-time 10 "${SITE}/" | grep -c '"@type": "Organization"')
if [ "$org_schema" -gt 0 ]; then
  echo "✅ Organization Schema: present" >> "$REPORT_FILE"
else
  echo "❌ Organization Schema: MISSING" >> "$REPORT_FILE"
fi

faq_schema=$(curl -s --max-time 10 "${SITE}/" | grep -c '"@type": "FAQPage"')
if [ "$faq_schema" -gt 0 ]; then
  echo "✅ FAQPage Schema: present" >> "$REPORT_FILE"
else
  echo "❌ FAQPage Schema: MISSING" >> "$REPORT_FILE"
fi

echo "" >> "$REPORT_FILE"

echo "[5] Checking Smith Ribbon site..." >> "$REPORT_FILE"
SITE2="https://smithribbon.com"
check_url "${SITE2}/"             "Smithribbon Homepage"
check_url "${SITE2}/en-index.html" "English Homepage"
check_url "${SITE2}/sitemap.xml"  "Sitemap XML"
canonical2=$(curl -s --max-time 10 "${SITE2}/" | grep -oP 'rel="canonical"[^>]+href="[^"]+"' | head -1)
if [ -n "$canonical2" ]; then
  echo "✅ Canonical: $canonical2" >> "$REPORT_FILE"
else
  echo "❌ Canonical tag MISSING!" >> "$REPORT_FILE"
fi
echo "" >> "$REPORT_FILE"

echo "[6] Checking Backlinks (via Google)..." >> "$REPORT_FILE"
echo "   (Manual check required: https://search.google.com/search-console/links)" >> "$REPORT_FILE"
echo "   Or use: https://ahrefs.com/site-explorer — enter ribbonbow123.com" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"

echo "=================================" >> "$REPORT_FILE"
echo "✅ Report saved to: $REPORT_FILE"
echo "📊 Next steps:"
echo "   1. Review this report"
echo "   2. Fix any ❌ issues"
echo "   3. Run: bash seo-toolkit/ping-searchengines.sh"
echo "   4. Push to GitHub: git push origin main"

cat "$REPORT_FILE"
