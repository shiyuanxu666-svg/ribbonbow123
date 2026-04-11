#!/bin/bash
# SEO搜索引擎Ping脚本
# 用途：通知搜索引擎「sitemap有更新」，促使爬虫重新抓取
# 使用：bash ping-searchengines.sh
# 建议：每次网站内容更新后运行

set -e

SITE="ribbonbow123.com"
HOME_URL="https://ribbonbow123.com"
SITEMAP_URL="https://ribbonbow123.com/sitemap.xml"

echo "🎀 Smith Ribbon — Search Engine Ping Script"
echo "=========================================="
echo ""

# 1. Google
echo "[1/5] Pinging Google..."
curl -s -A "SmithRibbonBot/1.0" \
  "https://www.google.com/ping?sitemap=${SITEMAP_URL}" \
  -w "\n    Status: %{http_code}\n" \
  -o /dev/null || echo "    (Google ping via URL submitted)"

# 2. Bing
echo "[2/5] Pinging Bing..."
curl -s -A "SmithRibbonBot/1.0" \
  "https://www.bing.com/ping?sitemap=${SITEMAP_URL}" \
  -w "\n    Status: %{http_code}\n" \
  -o /dev/null || echo "    (Bing ping via URL submitted)"

# 3. Yandex
echo "[3/5] Pinging Yandex..."
curl -s -A "SmithRibbonBot/1.0" \
  "https://webmaster.yandex.ru/ping?sitemap=${SITEMAP_URL}" \
  -w "\n    Status: %{http_code}\n" \
  -o /dev/null || echo "    (Yandex ping submitted)"

# 4. Baidu
echo "[4/5] Pinging Baidu..."
curl -s -A "SmithRibbonBot/1.0" \
  "https://ping.baidu.com/sitemap?site=${HOME_URL}&sitemap=${SITEMAP_URL}" \
  -w "\n    Status: %{http_code}\n" \
  -o /dev/null || echo "    (Baidu ping submitted)"

# 5. Sitemaps.org 验证
echo "[5/5] Verifying sitemap accessibility..."
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" "${SITEMAP_URL}")
if [ "$HTTP_CODE" = "200" ]; then
  echo "    ✅ Sitemap is accessible (HTTP 200)"
else
  echo "    ⚠️  Sitemap returned HTTP $HTTP_CODE — please check"
fi

echo ""
echo "=========================================="
echo "✅ Done! Google/Bing typically re-crawl within 24-48 hours."
echo "💡 Tip: Also submit manually at https://search.google.com/search-console/sitemaps"
echo "   and https://www.bing.com/webmasters/manage-sitemaps"
