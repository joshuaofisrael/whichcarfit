#!/usr/bin/env python3
"""Site QA. Usage: python3 _build/check.py

Fails on broken JSON-LD, missing legal line, owner name outside legal pages,
broken root relative links, duplicate or over-long titles, wrong h1 count,
canonical host, description length, missing noindex while the flag is on,
missing sources on vehicle pages, a CNAME that is not whichcarfit.com, and
(in launch mode) an empty GA4_ID or a page missing the Cloudflare beacon or
the GA4 loader.
"""
import glob, html, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from config import NOINDEX, DOMAIN, BASE_URL, GA4_ID, CF_BEACON_TOKEN, INDEXNOW_KEY

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LEGAL = {"terms", "privacy", "disclaimer", "copyright", "ad-disclosure"}
FOOTER = ("/about/", "/contact/", "/privacy/", "/terms/", "/disclaimer/",
          "/copyright/", "/ad-disclosure/", "/image-policy/")
bad = 0
titles = {}
descs = {}
if not NOINDEX and not re.fullmatch(r"G-[A-Za-z0-9]+", GA4_ID or ""):
    print("ga4-id-empty", repr(GA4_ID))
    bad += 1
files = [f for f in glob.glob(ROOT + "/**/*.html", recursive=True) if "/_build/" not in f]
for f in files:
    h = open(f, encoding="utf-8").read()
    rel = os.path.relpath(f, ROOT)
    top = rel.split("/")[0]
    for m in re.findall(r'<script type="application/ld\+json">(.*?)</script>', h, flags=re.S):
        try:
            json.loads(m)
        except Exception as e:
            print("JSONLD", rel, e)
            bad += 1
    vis = re.sub(r"<script.*?</script>", "", h, flags=re.S)
    if top not in LEGAL and re.search(r"Joshua|Israel Ventures|©", vis):
        print("LLC/©", rel)
        bad += 1
    if top in LEGAL and "is a trade name of Joshua Israel Ventures LLC" not in h:
        print("nolegalline", rel)
        bad += 1
    if not re.search(r'<link rel="canonical" href="https://whichcarfit\.com/', h):
        print("canonical", rel)
        bad += 1
    if "github.io" in h:
        print("github.io", rel)
        bad += 1
    if h.count("<h1") != 1:
        print("h1count", rel, h.count("<h1"))
        bad += 1
    desc = re.search(r'<meta name="description" content="(.*?)"', h)
    if not desc:
        print("nodesc", rel)
        bad += 1
    elif len(html.unescape(desc.group(1))) > 155:
        print("longdesc", len(html.unescape(desc.group(1))), rel)
        bad += 1
    if NOINDEX:
        if "noindex" not in h:
            print("missing-noindex", rel)
            bad += 1
    elif "noindex" in h and rel != "404.html":
        print("noindex", rel)
        bad += 1
    if rel == "404.html" and "noindex" not in h:
        print("404-indexable", rel)
        bad += 1
    if "—" in h or "–" in h:
        print("dash", rel)
        bad += 1
    if re.match(r"cars/[^/]+/[^/]+/\d{4}/index\.html$", rel):
        sec = re.search(r'<section class="sources".*?</section>', h, re.S)
        if not sec or not re.search(r'href="https?://', sec.group(0)):
            print("nosource", rel)
            bad += 1
    t = html.unescape(re.search(r"<title>(.*?)</title>", h).group(1))
    if len(t) >= 60:
        print("longtitle", len(t), rel)
        bad += 1
    titles.setdefault(t, []).append(rel)
    if desc:
        descs.setdefault(html.unescape(desc.group(1)), []).append(rel)
    if rel == "index.html" and '"@type": "WebSite"' not in h:
        print("no-website", rel)
        bad += 1
    need_faq = (
        rel in ("index.html", "cars/index.html")
        or rel.startswith("fitment/")
        or re.match(r"cars/[^/]+/index\.html$", rel)
        or re.match(r"cars/[^/]+/[^/]+/index\.html$", rel)
        or re.match(r"cars/[^/]+/[^/]+/\d{4}/index\.html$", rel)
    )
    if need_faq and "FAQPage" not in h:
        print("nofaq", rel)
        bad += 1
    need_article = (
        rel == "cars/index.html"
        or rel.startswith("fitment/")
        or re.match(r"cars/[^/]+/index\.html$", rel)
        or re.match(r"cars/[^/]+/[^/]+/index\.html$", rel)
        or re.match(r"cars/[^/]+/[^/]+/\d{4}/index\.html$", rel)
    )
    if need_article and '"@type": "Article"' not in h:
        print("noarticle", rel)
        bad += 1
    if rel not in ("index.html", "404.html") and "BreadcrumbList" not in h:
        print("nocrumbs", rel)
        bad += 1
    for prop in ("og:title", "og:description", "og:url", "og:image"):
        if f'property="{prop}"' not in h:
            print("og", prop, rel)
            bad += 1
    for href in FOOTER:
        if f'href="{href}"' not in h:
            print("footer", rel, href)
            bad += 1
    for img in re.finditer(r"<img\b[^>]*>", h, flags=re.I):
        window = h[max(0, img.start() - 300):img.end()]
        if 'href="/image-policy/"' not in window:
            print("img-policy", rel, img.group(0)[:120])
            bad += 1
    for link in re.findall(r'<a [^>]*href="(https://whichcarfit\.com/[^"]*)"', h):
        print("abs-anchor", rel, link)
        bad += 1
    if rel == "privacy/index.html":
        if "Google Analytics 4" not in h or "Cloudflare Web Analytics" not in h:
            print("privacy-analytics", rel)
            bad += 1
        if not NOINDEX and "does not include that beacon" in h:
            print("privacy-stale", rel)
            bad += 1
    if NOINDEX:
        if "beacon.min.js" in h or "googletagmanager.com/gtag/js" in h:
            print("preview-analytics", rel)
            bad += 1
    else:
        if "beacon.min.js" not in h or CF_BEACON_TOKEN not in h:
            print("no-beacon", rel)
            bad += 1
        if f"https://www.googletagmanager.com/gtag/js?id={GA4_ID}" not in h:
            print("no-ga4-loader", rel)
            bad += 1
        if "gtag('consent','default'" not in h or "'analytics_storage':'denied'" not in h:
            print("no-consent-default", rel)
            bad += 1
        if "'ad_storage':'denied'" not in h or "'ad_user_data':'denied'" not in h or "'ad_personalization':'denied'" not in h:
            print("no-consent-v2", rel)
            bad += 1
        if 'src="/assets/consent.js' not in h or 'id="cookie-settings"' not in h or "Cookie settings" not in h:
            print("no-consent-ui", rel)
            bad += 1
    for link in re.findall(r'(?:href|src)="(/[^"#?]*)', h):
        p = os.path.join(ROOT, link.lstrip("/"))
        if not (os.path.isfile(p) or os.path.isfile(os.path.join(p, "index.html"))):
            print("broken", rel, link)
            bad += 1
for t, fs in titles.items():
    if len(fs) > 1:
        print("duptitle", t, fs)
        bad += 1
for d, fs in descs.items():
    if len(fs) > 1:
        print("dupdesc", fs)
        bad += 1
cname = os.path.join(ROOT, "CNAME")
if not os.path.exists(cname) or open(cname).read().strip() != DOMAIN:
    print("cname")
    bad += 1
robots = open(os.path.join(ROOT, "robots.txt"), encoding="utf-8").read()
for bot in ("Googlebot", "Bingbot", "GPTBot", "ClaudeBot", "PerplexityBot", "OAI-SearchBot", "CCBot", "Google-Extended", "Applebot-Extended", "Bytespider"):
    if not re.search(rf"User-agent: {re.escape(bot)}\nAllow: /", robots):
        print("robots-missing", bot)
        bad += 1
if f"Sitemap: {BASE_URL}sitemap.xml" not in robots:
    print("robots-sitemap")
    bad += 1
sm = open(os.path.join(ROOT, "sitemap.xml"), encoding="utf-8").read()
locs = re.findall(r"<loc>(.*?)</loc>", sm)
if any("404" in x for x in locs):
    print("sitemap-404")
    bad += 1
if f"<loc>{BASE_URL}</loc>" not in sm and f"<loc>{BASE_URL.rstrip('/')}/</loc>" not in sm:
    # home is https://whichcarfit.com/
    if f"<loc>{BASE_URL}</loc>" not in sm:
        print("sitemap-home")
        bad += 1
for loc in locs:
    if not loc.startswith(BASE_URL):
        print("sitemap-host", loc)
        bad += 1
        continue
    rel = loc[len(BASE_URL):]
    p = os.path.join(ROOT, rel)
    if not (os.path.isfile(p) or os.path.isfile(os.path.join(p, "index.html")) or (rel == "" and os.path.isfile(os.path.join(ROOT, "index.html")))):
        print("sitemap-missing", loc)
        bad += 1
for block in re.findall(r"<url>(.*?)</url>", sm, flags=re.S):
    loc_m = re.search(r"<loc>(.*?)</loc>", block)
    loc = loc_m.group(1) if loc_m else "?"
    if not re.search(r"<lastmod>\d{4}-\d{2}-\d{2}</lastmod>", block):
        print("sitemap-lastmod", loc)
        bad += 1
keyfile = os.path.join(ROOT, INDEXNOW_KEY + ".txt")
if not os.path.isfile(keyfile) or open(keyfile, encoding="utf-8").read().strip() != INDEXNOW_KEY:
    print("indexnow-key")
    bad += 1
llms = os.path.join(ROOT, "llms.txt")
if not os.path.isfile(llms) or DOMAIN not in open(llms, encoding="utf-8").read():
    print("llms")
    bad += 1
ads = os.path.join(ROOT, "ads.txt")
if not os.path.isfile(ads):
    print("ads-txt-missing")
    bad += 1
else:
    ads_body = open(ads, encoding="utf-8").read().strip()
    if "google.com, pub-5681559774142917, DIRECT, f08c47fec0942fa0" not in ads_body:
        print("ads-txt-bad", ads_body[:120])
        bad += 1
if not NOINDEX:
    sample = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()
    if 'name="google-adsense-account" content="ca-pub-5681559774142917"' not in sample:
        print("adsense-meta")
        bad += 1
    if "pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-5681559774142917" not in sample:
        print("adsense-script")
        bad += 1
print("files", len(files), "issues", bad)
sys.exit(1 if bad else 0)
