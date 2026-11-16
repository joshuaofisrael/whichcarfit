#!/usr/bin/env python3
"""Site QA. Usage: python3 _build/check.py

Fails on broken JSON-LD, missing legal line, owner name outside legal pages,
broken root relative links, duplicate titles, wrong h1 count, canonical host,
description length, missing noindex while the flag is on, missing sources on
vehicle pages, and a CNAME that is not whichcarfit.com.
"""
import glob, html, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from config import NOINDEX, DOMAIN, BASE_URL

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LEGAL = {"terms", "privacy", "disclaimer", "copyright", "ad-disclosure"}
bad = 0
titles = {}
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
        if "FAQPage" not in h:
            print("nofaq", rel)
            bad += 1
        sec = re.search(r'<section class="sources".*?</section>', h, re.S)
        if not sec or not re.search(r'href="https?://', sec.group(0)):
            print("nosource", rel)
            bad += 1
    t = re.search(r"<title>(.*?)</title>", h).group(1)
    titles.setdefault(t, []).append(rel)
    for link in re.findall(r'(?:href|src)="(/[^"#?]*)', h):
        p = os.path.join(ROOT, link.lstrip("/"))
        if not (os.path.isfile(p) or os.path.isfile(os.path.join(p, "index.html"))):
            print("broken", rel, link)
            bad += 1
for t, fs in titles.items():
    if len(fs) > 1:
        print("duptitle", t, fs)
        bad += 1
cname = os.path.join(ROOT, "CNAME")
if not os.path.exists(cname) or open(cname).read().strip() != DOMAIN:
    print("cname")
    bad += 1
robots = open(os.path.join(ROOT, "robots.txt"), encoding="utf-8").read()
for bot in ("Googlebot", "Bingbot", "GPTBot", "ClaudeBot", "PerplexityBot", "OAI-SearchBot", "CCBot", "Google-Extended", "Applebot-Extended", "Bytespider"):
    if bot not in robots:
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
print("files", len(files), "issues", bad)
sys.exit(1 if bad else 0)
