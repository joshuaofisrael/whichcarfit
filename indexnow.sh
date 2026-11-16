#!/bin/bash
# Ping IndexNow after the domain is live. Refuses while NOINDEX is still true.
cd "$(dirname "$0")"
if grep -q '^NOINDEX = True' _build/config.py; then
  echo "IndexNow skipped: NOINDEX is still on. Turn it off after whichcarfit.com resolves."
  exit 0
fi
KEY=15cffb11329a506a716afdc6f6099cae
if [ $# -gt 0 ]; then URLS=$(printf '"%s",' "$@"); else URLS=$(grep -o '<loc>[^<]*' sitemap.xml | sed 's/<loc>//' | sed 's/.*/"&"/' | paste -sd, -); fi
curl -s -o /dev/null -w "IndexNow HTTP %{http_code}\n" -H "Content-Type: application/json; charset=utf-8" https://api.indexnow.org/indexnow \
 -d "{\"host\":\"whichcarfit.com\",\"key\":\"$KEY\",\"keyLocation\":\"https://whichcarfit.com/$KEY.txt\",\"urlList\":[${URLS%,}]}"
