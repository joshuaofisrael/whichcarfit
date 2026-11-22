#!/usr/bin/env python3
"""Which Car Fit static site. Run from the repo root:

  python3 _build/build.py

NOINDEX in _build/config.py is the single flag for the noindex meta.
Paths are always root relative. Canonicals always use https://whichcarfit.com/.
The CNAME file is always written. GA4_ID is empty until launch. See LAUNCH-NOTES.md.
"""
import html, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from config import (NOINDEX, BASE_URL, BRAND, DOMAIN, PUBLISHED, PUBLISHED_H,
                    INDEXNOW_KEY, CF_BEACON_TOKEN, CONTACT_EMAIL, LEGAL_LINE, GA4_ID)
from vehicles import VEHICLES

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NHTSA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "nhtsa")
E = html.escape
PAGES = []  # (path, lastmod) for the sitemap. 404 is excluded.
# Google AdSense publisher id (sitewide head tag only; no ad units yet).
ADSENSE_CLIENT = "ca-pub-5681559774142917"
# Optional news-photo thumbnails for model hubs. Path is root-relative.
MODEL_THUMBS = {
    ("Toyota", "RAV4"): {
        "src": "/assets/images/rav4-coastal-drive.png",
        "alt": "Unbadged SUV on a coastal road in natural daylight",
        "caption": "AI-generated image. Atmospheric photo for the RAV4 hub, not a factory shot of a specific year.",
    },
    ("Toyota", "Camry"): {
        "src": "/assets/images/rav4-coastal-drive.png",
        "alt": "Unbadged car on a coastal road in natural daylight",
        "caption": "AI-generated image. Atmospheric photo reused from the site photo bank, not a factory shot of a Camry.",
    },
    ("Tesla", "Model Y"): {
        "src": "/assets/images/model-y-charge-port.png",
        "alt": "Hand holding a charge plug at an unbadged electric car port",
        "caption": "AI-generated image. Atmospheric photo for the Model Y hub, not a factory shot of a specific year.",
    },
}
# Hubs that get a real comparison, not just the year table.
HUB_EXTRA = {
    ("Tesla", "Model Y"): '''<p>Tesla does not print a separate owner's manual for each Model Y year. The <a href="https://www.tesla.com/ownersmanual/2020_2024_modely/en_us/GUID-197C481B-B4D4-4973-9772-2AF488442CE1.html" rel="nofollow noopener" target="_blank">2020 to 2024 Model Y owner's manual</a> is one book. The <a href="https://www.tesla.com/ownersmanual/modely/en_us/Owners_Manual.pdf" rel="nofollow noopener" target="_blank">2025+ North America PDF</a> (cover software 2026.2.8) is a second book. Checked 20 Nov 2026. Both books print the same windshield blades and the same key fob cell. They do not describe the exterior lights the same way, so 2021, 2022, 2023, and 2024 are not separate pages here.</p>
<p>Windshield blades, in both books: driver side 26 inches (650 mm), passenger side 20 inches (500 mm). The connector has to match the blade already on the arm. Neither windshield chapter prints a rear blade length. The accessory key fob takes a CR2032, positive side up. The key card section does not print a coin cell. A phone key uses the phone, not a cell you buy for the car.</p>
<p>Lights: the 2020 to 2024 book says Model Y has LED signature lights along the headlight rim, and it does not print a bulb trade number. The 2025+ book describes a front lightbar and a tail lightbar (the front lightbar line says if equipped) that work as daytime running lights, parking lights, and tail lights. That book also does not print a bulb number. Do not copy the 2020 recall list onto a later car. NHTSA's recalls API, retrieved 20 Nov 2026, returned 24 campaigns for 2020, 23 for 2021, 20 for 2022, 17 for 2023, 5 for 2024, and 3 for 2025. Use the VIN lookup.</p>''',
    ("Toyota", "Camry"): '''<p>The 2019 through 2024 Camry books we opened on 20 Nov 2026 print one shared exterior bulb chart and a CR2032 key. Publishing six copies of that chart would be the same page with the year changed, so those years live on the <a href="/cars/toyota/camry/2023/">2023 Camry page</a>. The 2025 book is a different car and has its own page.</p>
<p>Books that match the 2023 chart: 2019 <a href="https://assets.sia.toyota.com/publications/en/om-s/OM06142U/pdf/OM06142U.pdf" rel="nofollow noopener" target="_blank">OM06142U</a> (light bulb table page 550), 2020 <a href="https://assets.sia.toyota.com/publications/en/om-s/OM06158U/pdf/OM06158U.pdf" rel="nofollow noopener" target="_blank">OM06158U</a> (page 558), 2021 <a href="https://assets.sia.toyota.com/publications/en/om-s/OM06242U/pdf/OM06242U.pdf" rel="nofollow noopener" target="_blank">OM06242U</a> (page 599), 2022 <a href="https://assets.sia.toyota.com/publications/en/om-s/OM06244U/pdf/OM06244U.pdf" rel="nofollow noopener" target="_blank">OM06244U</a> (page 589), 2023 <a href="https://assets.sia.toyota.com/publications/en/om-s/OM06259U/pdf/OM06259U.pdf" rel="nofollow noopener" target="_blank">OM06259U</a> (page 589), and 2024 <a href="https://assets.sia.toyota.com/publications/en/om-s/OM06291U/pdf/OM06291U.pdf" rel="nofollow noopener" target="_blank">OM06291U</a> (page 589). Each table lists front side marker W5W 5 W, front turn and parking 7444NA 28/8 W, rear turn WY21W 21 W, rear side marker W5W 5 W, and back-up 921 16 W. The footnote says bulbs not listed are LED. Each key chapter says lithium battery CR2032. None of these books prints a wiper inch length.</p>
<p>Two lines next to that chart do move, and neither one is a lamp you buy from the bulb table. The 2019 and 2020 specifications chapter lists a 19 x 8 J wheel. From 2021 the same line reads 19 x 8 1/2 J. The 2019, 2020, and 2021 tables still include a vanity light row. The 2022, 2023, and 2024 tables do not.</p>
<p>The 2025 file is the Camry Hybrid owner's manual, publication <a href="https://assets.sia.toyota.com/publications/en/om-s/OM06266U/pdf/OM06266U.pdf" rel="nofollow noopener" target="_blank">OM06266U</a>, software identifier camry.2025.2403.hev.vh. The key is a CR2450, not a CR2032. The light bulb table on page 492 lists front turn and parking 7444NA 28/8 W, rear turn WY21W 21 W, and back-up W16W 16 W. There is no W5W row and no 921 row. The maintenance chapter says lamps other than those three bulb-type positions are LEDs, and a Toyota dealer replaces those. NHTSA files this year as CAMRY HYBRID, not as CAMRY.</p>''',
    ("Honda", "CR-V"): '''<p>Two CR-V charts are on this site, and they are not the same car. Checked 21 Nov 2026.</p>
<p>The 2020 book (<a href="https://techinfo.honda.com/rjanisis/pubs/OM/AH/ATLA2020OM/enu/ATLA2020OM.PDF" rel="nofollow noopener" target="_blank">ATLA2020OM</a>) and the 2022 book print a halogen low beam of 55 W (H11) and a halogen high beam of 60 W (HB3), and they also list LED headlights that a dealer replaces as an assembly. Front turn signals are LED. Brake, taillight, rear turn, and rear side marker lights are LED. The back-up light is 16 W. Remote Transmitter Care prints CR1620 for a master key with a remote, and CR2032 for the keyless remote. Neither wiper chapter prints an inch length. Those two years live on the <a href="/cars/honda/cr-v/2020/">2020 CR-V page</a>. A 2021 CR-V owner's manual was not opened, so 2021 is not given either chart.</p>
<p>The 2023, 2024, and 2025 books drop the H11 and HB3 rows. Headlights are LED. Back-up lights are LED. The rear turn signal is 21 W amber. The keyless remote is a CR2032, and those books do not print a CR1620 cell. The 2023 and 2025 wiper chapters still do not print an inch length. The 2024 specifications page and the 2024 remote-battery page match this chart. The 2024 wiper chapter was not the page we opened. That chart is on the <a href="/cars/honda/cr-v/2025/">2025 CR-V page</a>.</p>
<p>NHTSA's recalls API, retrieved 21 Nov 2026, returned 7 campaigns for 2020, 4 for 2021, 3 for 2022, 3 for 2023, 2 for 2024, and 1 for 2025. A campaign count is not a reason to buy a bulb. Use the VIN lookup. Nearby charts: <a href="/cars/honda/accord/">Accord</a>, <a href="/cars/honda/civic/">Civic</a>, and the <a href="/cars/toyota/rav4/">RAV4</a>.</p>''',
    ("Chevrolet", "Equinox"): '''<p>The three Equinox books already on this site do not print one wiper table. Re-read of the 2022 book on 21 Nov 2026, with the 2020 and 2021 tables left as they were checked on 20 Nov 2026.</p>
<p>The <a href="https://www.chevrolet.com/ownercenter/content/dam/gmownercenter/gmna/dynamic/manuals/2020/chevrolet/equinox/2020-chevrolet-equinox-owners-manual.pdf" rel="nofollow noopener" target="_blank">2020 book</a> (document 13555863) prints 60 cm (23.6 in), 45.0 cm (17.7 in), and 30.0 cm (11.8 in), GM parts 84574893, 84574892, and 84215609. The <a href="https://www.chevrolet.com/ownercenter/content/dam/gmownercenter/gmna/dynamic/manuals/2021/chevrolet/equinox/2021-chevrolet-equinox-owners-manual.pdf" rel="nofollow noopener" target="_blank">2021 book</a> (document 14420010) keeps those centimeter lengths and those part numbers, and prints the inch side as 24, 18, and 12. The <a href="https://www.chevrolet.com/ownercenter/content/dam/gmownercenter/gmna/dynamic/manuals/2022/chevrolet/equinox/2022-chevrolet-equinox-owners-manual.pdf" rel="nofollow noopener" target="_blank">2022 book</a> (document 15230998, CRC 8/10/21) still prints 24, 18, and 12 inches. The driver part is now 84566977, not 84574893. The rear part is now 85118765, not 84215609. The passenger part stays 84574892.</p>
<p>All three books say to replace the remote battery with a CR2032. The 2022 headlamp chapter shows a bi-halogen bulb procedure and does not print a trade number. The same chapter says LED assemblies go to the dealer. Open the <a href="/cars/chevrolet/equinox/2020/">2020</a>, <a href="/cars/chevrolet/equinox/2021/">2021</a>, or <a href="/cars/chevrolet/equinox/2022/">2022</a> page for the full line and that year's recalls. The <a href="/fitment/wiper-blades/">wiper hub</a> lists every length we have copied.</p>''',
    ("Chevrolet", "Malibu"): '''<p>The 2020 Malibu book was opened again on 21 Nov 2026. Document 13555849, CRC 8/16/19. The maintenance replacement parts table on page 314 prints a driver blade of 650 mm (25.6 in), GM part 23353586, and a passenger blade of 450 mm (17.7 in), GM part 23353587. There is no rear wiper line in that table. The remote battery line is still CR2032. The LED Lighting section says the vehicle has several LED lamps and to contact the dealer for an LED assembly. It does not print a halogen trade number.</p>
<p>The <a href="/cars/chevrolet/malibu/2021/">2021</a> and <a href="/cars/chevrolet/malibu/2022/">2022</a> pages already quote 25.6 in and 17.7 in from those years' books. Those two PDFs were not opened again today, so this paragraph does not add part numbers for them. The refreshed chart is on the <a href="/cars/chevrolet/malibu/2020/">2020 Malibu page</a>.</p>''',
}

# Optional hub title, description, and visible FAQs. Titles stay under 60 characters.
HUB_META = {
    ("Honda", "CR-V"): {
        "title": "Which CR-V bulb and key fob fits?",
        "desc": "2020 and 2022 CR-V low beam is H11 or LED. 2023 to 2025 headlights are LED, and the rear turn is 21 W amber.",
        "faqs": [
            ("Which key fob battery fits a Honda CR-V?",
             "The 2020 and 2022 books print CR1620 for a master key with a remote transmitter and CR2032 for the keyless remote. The 2023, 2024, and 2025 books print CR2032 only. A 2021 book was not opened."),
            ("Which wiper blade fits a Honda CR-V?",
             "None of the CR-V books we opened prints a driver, passenger, or rear inch length. The 2024 wiper chapter was not the page we opened. Do not borrow a length from another year."),
            ("Which bulb fits a Honda CR-V?",
             "2020 and 2022: halogen low beam H11 55 W or LED, halogen high beam HB3 60 W or LED, back-up light 16 W, rear turn LED. 2023 to 2025: headlights LED, back-up lights LED, rear turn 21 W amber."),
        ],
    },
    ("Chevrolet", "Equinox"): {
        "title": "Which Equinox wiper length fits?",
        "desc": "2020 Equinox wipers are 23.6, 17.7, and 11.8 in. 2021 and 2022 print 24, 18, and 12. The 2022 driver part changed.",
        "faqs": [
            ("Which wiper blade fits a Chevrolet Equinox?",
             "2020 prints 23.6, 17.7, and 11.8 inches with GM parts 84574893, 84574892, and 84215609. 2021 prints 24, 18, and 12 inches with the same part numbers. 2022 keeps 24, 18, and 12, changes the driver part to 84566977, and changes the rear part to 85118765."),
            ("Which key fob battery fits a Chevrolet Equinox?",
             "The 2020, 2021, and 2022 books each say to replace the remote battery with a CR2032, or equivalent."),
            ("Which headlight bulb fits a Chevrolet Equinox?",
             "The 2022 book shows a bi-halogen headlamp procedure and does not print a trade number. It also says LED assemblies are replaced at the dealer. Do not guess an H11 from a parts counter."),
        ],
    },
    ("Chevrolet", "Malibu"): {
        "title": "Which Malibu wiper length fits?",
        "desc": "2020 Malibu wipers are 25.6 in and 17.7 in, GM parts 23353586 and 23353587. The key fob battery is a CR2032.",
        "faqs": [
            ("Which wiper blade fits a 2020 Chevrolet Malibu?",
             "Driver side 650 mm (25.6 in), GM part 23353586. Passenger side 450 mm (17.7 in), GM part 23353587. The 2020 maintenance table does not print a rear wiper."),
            ("Which key fob battery fits a Chevrolet Malibu?",
             "The 2020 book says to replace the remote battery with a CR2032, or equivalent. The 2021 and 2022 pages quote the same cell from those years' books."),
            ("Which bulb fits a Chevrolet Malibu?",
             "The 2020 LED Lighting section says the vehicle has several LED lamps and to contact the dealer for an LED assembly. It does not print a halogen trade number."),
        ],
    },
}

def slugify(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")

def vpath(v):
    return f"/cars/{slugify(v['make'])}/{slugify(v['model'])}/{v['year']}/"

def vkey(v):
    return f"{slugify(v['make'])}-{slugify(v['model'])}-{v['year']}"

def url(path):
    return BASE_URL + path.lstrip("/")

def u(path):
    return path  # root relative, in both modes

def clip(d, n=155):
    d = re.sub(r"\s+", " ", d).strip()
    if len(d) <= n:
        return d
    c = d[:n]
    i = c.rfind(". ")
    if i > 80:
        return c[:i + 1]
    sp = c.rfind(" ")
    return (c[:sp] if sp > 40 else c).rstrip(",;:") + "."

def seo_title(text):
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) >= 60:
        raise SystemExit(f"title >= 60 ({len(text)}): {text}")
    return text

def article_ld(headline, path, published=None, modified=None, image=None):
    published = published or PUBLISHED
    modified = modified or published
    return {
        "@context": "https://schema.org", "@type": "Article",
        "headline": headline, "datePublished": published, "dateModified": modified,
        "image": url(image or "/og.png"),
        "author": {"@type": "Organization", "name": BRAND, "url": BASE_URL},
        "publisher": {"@type": "Organization", "name": BRAND, "url": BASE_URL,
                      "logo": {"@type": "ImageObject", "url": url("/logo.png")}},
        "mainEntityOfPage": url(path),
    }

def thumb_figure(thumb):
    """News-photo figure labelled AI-generated and linked to the image policy."""
    return (
        f'<figure class="thumb">'
        f'<a href="{u("/image-policy/")}" class="thumb-link">'
        f'<img src="{u(thumb["src"])}" alt="{E(thumb["alt"])}" width="1280" height="720" loading="lazy">'
        f"</a>"
        f'<figcaption><a href="{u("/image-policy/")}">{E(thumb["caption"])}</a></figcaption>'
        f"</figure>"
    )

def related_reads(items, heading="Related lookups"):
    """Next-read cards with thumbnails when the target has a known photo."""
    cards = []
    for href, label, blurb, thumb in items:
        img = ""
        if thumb:
            # Image-policy link must sit just before the <img> for check.py.
            img = (f'<a class="img-policy-ref" href="{u("/image-policy/")}">AI-generated image policy</a>'
                   f'<a class="next-thumb" href="{u(href)}">'
                   f'<img src="{u(thumb["src"])}" alt="" width="320" height="180" loading="lazy"></a>'
                   f'<p class="next-cap"><a href="{u("/image-policy/")}">AI-generated image. Image policy.</a></p>')
        cards.append(
            f'<li class="next-card">{img}'
            f'<div><a href="{u(href)}">{E(label)}</a>'
            f'<p>{E(blurb)}</p></div></li>')
    return (f'<section class="next-reads" aria-labelledby="next-h">'
            f'<h2 id="next-h">{E(heading)}</h2>'
            f'<ul class="next-list">{"".join(cards)}</ul></section>')

def compare_box(v, by_model):
    """Check-another box for lookup pages: sibling years and other models."""
    make_href = f"/cars/{slugify(v['make'])}/"
    model_href = f"/cars/{slugify(v['make'])}/{slugify(v['model'])}/"
    sibs = [o for o in by_model.get((v["make"], v["model"]), []) if o["year"] != v["year"]]
    year_links = " · ".join(
        f'<a href="{u(vpath(o))}">{E(o["year"])}</a>' for o in sibs) or "none checked yet"
    other = []
    seen = set()
    for o in VEHICLES:
        if o["make"] == v["make"] and o["model"] != v["model"] and o["model"] not in seen:
            seen.add(o["model"])
            other.append(o)
        if len(other) >= 4:
            break
    other_links = " · ".join(
        f'<a href="{u("/cars/" + slugify(o["make"]) + "/" + slugify(o["model"]) + "/")}">{E(o["model"])}</a>'
        for o in other) or f'<a href="{u(make_href)}">All {E(v["make"])} models</a>'
    return (
        f'<aside class="compare" aria-label="Check another vehicle">'
        f"<h2>Check another year or model</h2>"
        f'<p>Same {E(v["make"])} {E(v["model"])} year: {year_links}. '
        f'Or open the <a href="{u(model_href)}">year comparison table</a>.</p>'
        f"<p>Other {E(v['make'])} models: {other_links}. "
        f'Part hubs: {part_anchors()}.</p>'
        f'<p><a href="{u("/")}">Use the year picker</a> if you want a different make.</p>'
        f"</aside>"
    )

def vehicle_related(v, by_model):
    """3-4 closely related next reads. Photo cards use that model's hub image."""
    items = []
    model_href = f"/cars/{slugify(v['make'])}/{slugify(v['model'])}/"
    thumb = MODEL_THUMBS.get((v["make"], v["model"]))
    items.append((model_href,
                  f"All {v['make']} {v['model']} years",
                  "Year table for key fob, wiper, and headlight lines from each checked book.",
                  thumb))
    sibs = [o for o in by_model.get((v["make"], v["model"]), []) if o["year"] != v["year"]]
    # A sibling card can use the model photo. A model with no photo keeps the
    # sibling link in the compare box instead, so the next-read row can show
    # three hubs that do have a photo.
    if thumb and sibs:
        sibs_sorted = sorted(sibs, key=lambda o: abs(int(o["year"]) - int(v["year"])))
        o = sibs_sorted[0]
        items.append((vpath(o),
                      f"{o['year']} {o['make']} {o['model']} parts",
                      "Same model, different year. Charts are not copied across years.",
                      thumb))
    for make, model in (("Tesla", "Model Y"), ("Toyota", "Camry"), ("Toyota", "RAV4")):
        if (make, model) == (v["make"], v["model"]):
            continue
        photo = MODEL_THUMBS.get((make, model))
        if not photo:
            continue
        items.append((f"/cars/{slugify(make)}/{slugify(model)}/",
                      f"{make} {model} parts",
                      "Key, wiper, and bulb lines from that model's owner's manual.",
                      photo))
        if len(items) >= 4:
            break
    if len(items) < 3:
        items.append(("/fitment/key-fob-battery/",
                      "Key fob battery hub",
                      "Every key fob cell we copied from an owner's manual.",
                      None))
    return items[:4]

def write(path, content):
    fp = os.path.join(ROOT, path.lstrip("/"))
    if path.endswith("/"):
        fp = os.path.join(fp, "index.html")
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    with open(fp, "w") as f:
        f.write(content)

LOGO = ('<svg width="34" height="34" viewBox="0 0 64 64" aria-hidden="true" focusable="false">'
        '<rect width="64" height="64" rx="14" fill="#0b3954"/>'
        '<circle cx="24" cy="26" r="10" fill="none" stroke="#ffb347" stroke-width="4"/>'
        '<circle cx="24" cy="26" r="3" fill="#e6f4f1"/>'
        '<path d="M32 26 h20 v6 h-6 v6 h-5 v-6 h-9 z" fill="#087e8b"/>'
        '</svg>')
NAV = [("/", "Home"), ("/cars/", "Cars"), ("/fitment/", "Part fit"),
       ("/fitment/key-fob-battery/", "Key fob"), ("/methodology/", "How we check")]
PARTS = [
    ("key", "key-fob-battery", "Key fob battery", "What battery the key fob takes, from the owner's manual."),
    ("wiper", "wiper-blades", "Wiper blades", "Front and rear wiper parts printed in the owner's manual."),
    ("head", "headlight-bulbs", "Headlight bulbs", "Low beam, high beam, and LED headlamp notes from the manual."),
    ("brake", "brake-lights", "Brake lights", "Brake and stop lamp types from the manual's bulb chart."),
    ("turn", "turn-signals", "Turn signals", "Front and rear turn signal types from the manual's bulb chart."),
]

def part_anchors():
    return " · ".join(
        f'<a href="{u("/fitment/" + slug + "/")}">{E(label)}</a>'
        for _, slug, label, _ in PARTS)

def latest(vs):
    # A hub page's lastmod should reflect the newest vehicle it lists,
    # since adding a vehicle changes that hub's own list, not just the new
    # vehicle's own page. Falls back to PUBLISHED when the list is empty.
    dates = [v["modified"] for v in vs]
    return max(dates) if dates else PUBLISHED

def load_nhtsa(v):
    fp = os.path.join(NHTSA_DIR, vkey(v) + ".json")
    if not os.path.exists(fp):
        return None
    with open(fp) as f:
        return json.load(f)

# AdSense low-value-content fix (20 Nov 2026): paths listed in _build/thin-noindex.txt
# get noindex,follow and stay out of the sitemap until they have real unique substance.
_THIN_NOINDEX = set()
try:
    import os as _os
    with open(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "thin-noindex.txt"), encoding="utf-8") as _fh:
        _THIN_NOINDEX = {l.strip().strip("/") for l in _fh if l.strip() and not l.startswith("#")}
except FileNotFoundError:
    pass


def _is_thin(path):
    return str(path).strip("/") in _THIN_NOINDEX


def page(path, title, desc, body, jsonld=None, crumbs=None, noindex=False, legal=False, modified=PUBLISHED):
    if _is_thin(path):
        noindex = True
    title = seo_title(title)
    desc = clip(desc)
    canon = url(path if path != "/404.html" else "/404.html")
    # 404 stays out of the sitemap. Other pages are listed even while the
    # NOINDEX flag is on, so the sitemap is ready for launch.
    if path != "/404.html" and not noindex:
        PAGES.append((path, modified))
    robots_no = noindex or NOINDEX or path == "/404.html"
    ld = []
    if path == "/":
        ld.append({"@context": "https://schema.org", "@type": "WebSite", "name": BRAND, "url": BASE_URL,
                   "publisher": {"@type": "Organization", "name": BRAND, "url": BASE_URL, "logo": url("/logo.png")}})
        ld.append({"@context": "https://schema.org", "@type": "Organization", "name": BRAND, "url": BASE_URL,
                   "logo": url("/logo.png")})
    if crumbs:
        ld.append({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n, "item": url(p)} for i, (p, n) in enumerate(crumbs)]})
    if jsonld:
        ld += jsonld if isinstance(jsonld, list) else [jsonld]
    ldh = "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in ld)
    nav = "".join(
        f'<a href="{u(p)}"' + (' aria-current="page"' if p == path else "") + f'>{n}</a>' for p, n in NAV)
    bc = ""
    if crumbs:
        bc = '<nav class="crumbs" aria-label="Breadcrumb"><ol>' + "".join(
            (f'<li><a href="{u(p)}">{E(n)}</a></li>' if i < len(crumbs) - 1 else f'<li aria-current="page">{E(n)}</li>')
            for i, (p, n) in enumerate(crumbs)) + "</ol></nav>"
    robots = "noindex, follow" if robots_no else "index, follow, max-image-preview:large"
    blocks = jsonld if isinstance(jsonld, list) else ([jsonld] if jsonld else [])
    og_type = "article" if any(isinstance(x, dict) and x.get("@type") == "Article" for x in blocks) else "website"
    if NOINDEX:
        beacon = "<!-- cf-beacon: added when NOINDEX is turned off -->"
        head_extra = ""
        banner = ""
        consent_js = ""
        cookie_link = ""
    else:
        beacon = ("<!-- Cloudflare Web Analytics --><script defer src='https://static.cloudflareinsights.com/beacon.min.js' "
                  f"data-cf-beacon='{{\"token\": \"{CF_BEACON_TOKEN}\"}}'></script><!-- End Cloudflare Web Analytics -->")
        # Consent defaults run before any analytics tag. The gtag loader is
        # type=text/plain so it does not fetch until consent.js copies it
        # after Accept. GA4_ID may be empty; the launch check rejects that.
        head_extra = (
            "<script>window.dataLayer=window.dataLayer||[];"
            "function gtag(){dataLayer.push(arguments);}"
            "gtag('consent','default',{'ad_storage':'denied','ad_user_data':'denied',"
            "'ad_personalization':'denied','analytics_storage':'denied','wait_for_update':500});"
            "</script>"
            f'<script type="text/plain" data-ga4-loader="1" data-ga4-id="{E(GA4_ID)}" '
            f'src="https://www.googletagmanager.com/gtag/js?id={E(GA4_ID)}"></script>'
        )
        banner = (
            '<div id="consent-banner" class="consent" hidden>'
            '<p>Google Analytics 4 stays off unless you accept. Cloudflare Web Analytics counts visits and does not use cookies. '
            f'<a href="{u("/privacy/")}">Privacy</a></p>'
            '<button type="button" class="btn" id="consent-accept">Accept</button>'
            '<button type="button" class="btn alt" id="consent-reject">Reject</button>'
            '</div>'
        )
        consent_js = f'<script src="{u("/assets/consent.js")}?v=1" defer></script>'
        cookie_link = f' | <a href="#consent-banner" id="cookie-settings">Cookie settings</a>'
    legal_html = f'<p class="legal-line">{LEGAL_LINE}</p>' if legal else ""
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(title)}</title><meta name="description" content="{E(desc)}"><link rel="canonical" href="{canon}">
<meta name="robots" content="{robots}">
<meta property="og:type" content="{og_type}"><meta property="og:site_name" content="{BRAND}"><meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}"><meta property="og:url" content="{canon}"><meta property="og:image" content="{url('/og.png')}"><meta property="og:image:alt" content="Which Car Fit key mark"><meta property="og:locale" content="en_US"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{E(title)}"><meta name="twitter:description" content="{E(desc)}"><meta name="twitter:image" content="{url('/og.png')}">
<link rel="icon" href="{u('/favicon.svg')}" type="image/svg+xml"><link rel="stylesheet" href="{u('/assets/style.css')}?v=4">{head_extra}{ldh}
</head><body><a class="skip" href="#main">Skip to content</a>
<header class="site"><div class="wrap"><a class="brand" href="{u('/')}">{LOGO}<span>{BRAND}</span></a><nav class="main" aria-label="Main">{nav}</nav></div></header>
<main id="main" class="wrap">{bc}{body}<!-- ad-slot: below-content (reserved; no ad code) --></main>
<footer class="site"><div class="wrap"><p class="fbrand"><strong>{BRAND}</strong>: key fob battery, wiper parts, bulb sizes, and NHTSA recalls by make, model, and year. Independent, and not affiliated with any car maker. Confirm every part on the vehicle and in the owner's manual.</p>
<p class="flinks"><a href="{u('/about/')}">About</a> | <a href="{u('/contact/')}">Contact</a> | <a href="{u('/privacy/')}">Privacy</a> | <a href="{u('/terms/')}">Terms of use</a> | <a href="{u('/disclaimer/')}">Disclaimer</a> | <a href="{u('/copyright/')}">Copyright and DMCA</a> | <a href="{u('/ad-disclosure/')}">Advertising disclosure</a> | <a href="{u('/image-policy/')}">Image policy</a> | <a href="{u('/methodology/')}">Sources and methods</a>{cookie_link}</p>
{legal_html}</div></footer>
{banner}<script src="{u('/assets/site.js')}?v=1" defer></script>{consent_js}{beacon}
</body></html>'''

def ext_link(title, href):
    return f'<a href="{E(href)}" rel="nofollow noopener" target="_blank">{E(title)}</a>'

def fit_map(v):
    return {k: (label, value) for k, label, value in v["fitment"]}

def vehicle_page(v, by_model):
    path = vpath(v)
    # Most vehicles were checked in the 16 Nov 2026 launch batch; a few added
    # later carry their own real checked date in v["checked_h"].
    checked = v.get("checked_h", PUBLISHED_H)
    name = f"{v['year']} {v['make']} {v['model']}"
    title = v.get("seo_title") or f"Which parts fit a {name}?"
    desc = f"Which key fob battery, wiper, and bulb fit a {name}? Figures are from that year's owner's manual, plus NHTSA recalls."
    rows = []
    for key, label, value in v["fitment"]:
        hub = next(p for p in PARTS if p[0] == key or (key == "rear" and p[0] == "wiper"))
        rows.append(
            f'<tr><th scope="row"><a href="{u("/fitment/" + hub[1] + "/")}">{E(label)}</a></th>'
            f'<td>{E(value)}</td><td>Owner\'s manual cited below</td></tr>')
    # lead answers
    fm = fit_map(v)
    lead = []
    for key in ("key", "wiper", "rear", "head", "brake", "turn"):
        if key in fm:
            lead.append(f"<li><strong>{E(fm[key][0])}:</strong> {E(fm[key][1])}</li>")
    nhtsa = load_nhtsa(v)
    problem_html, faqs_extra = problems_block(v, nhtsa, checked)
    faqs = [
        (f"What battery does the {name} key fob take?",
         fm["key"][1] + " Match the remote you hold to the description, because some model years print two different cells."),
        (f"Which wiper, bulb, and battery fit a {name}?",
         "Battery: " + fm["key"][1] + " Front wiper: " + fm["wiper"][1] + " Headlight: " + fm["head"][1] + " Brake light: " + fm["brake"][1] + " Turn signal: " + fm["turn"][1]),
        (f"Where do I find the tire size and the bulb chart for a {name}?",
         "Tire size and cold pressure are on the driver's door jamb label. The bulb types in the table on this page are taken from the owner's manual cited below, not from that label. If the manual lists more than one lamp package, match the row to the lamps on your vehicle."),
        (f"Where do I look up recalls on a {name}?",
         "Go to https://www.nhtsa.gov/recalls and enter the VIN from the driver's door jamb. The campaigns listed on this page are what NHTSA's public recalls API returned for this model year on " + checked + "."),
    ]
    sibs = [o for o in by_model.get((v["make"], v["model"]), []) if o["year"] != v["year"]]
    sib_html = ""
    if sibs:
        sib_html = "<h2>Other years</h2><ul class=\"cols\">" + "".join(
            f'<li><a href="{u(vpath(o))}">{E(o["year"])} {E(o["make"])} {E(o["model"])}</a></li>' for o in sibs) + "</ul>"
    other_models = []
    seen_models = set()
    for o in VEHICLES:
        if o["make"] == v["make"] and o["model"] != v["model"] and o["model"] not in seen_models:
            seen_models.add(o["model"])
            other_models.append(o)
    if other_models:
        sib_html += "<h2>Other " + E(v["make"]) + " models</h2><ul class=\"cols\">" + "".join(
            f'<li><a href="{u("/cars/" + slugify(o["make"]) + "/" + slugify(o["model"]) + "/")}">{E(o["model"])}</a></li>'
            for o in other_models) + "</ul>"
    srcs = "".join(
        f"<li>{ext_link(t, href)} ({E(pub)}, {E(date)}). {E(note)}</li>"
        for t, href, pub, date, note in v["sources"])
    srcs += f'<li>{ext_link("NHTSA recalls lookup by VIN", "https://www.nhtsa.gov/recalls")} (National Highway Traffic Safety Administration).</li>'
    if nhtsa:
        for g in nhtsa["groups"]:
            srcs += f'<li>{ext_link("NHTSA recalls API: " + g["model"] + " " + v["year"], g["recalls"]["url"])} retrieved {checked}.</li>'
            if g["complaints"].get("url"):
                srcs += f'<li>{ext_link("NHTSA complaints API: " + g["model"] + " " + v["year"], g["complaints"]["url"])} retrieved {checked}.</li>'
    note = f'<p class="note">{E(v["note"])}</p>' if v.get("note") else ""
    make_href = f"/cars/{slugify(v['make'])}/"
    model_href = f"/cars/{slugify(v['make'])}/{slugify(v['model'])}/"
    mid_related = related_reads(vehicle_related(v, by_model), "Next reads while you are here")
    end_related = related_reads(vehicle_related(v, by_model), "More part lookups")
    compare = compare_box(v, by_model)
    # Year pages reuse the model hub photo when one is assigned. A model with
    # no bank photo stays text-only rather than borrowing another car's picture.
    thumb = MODEL_THUMBS.get((v["make"], v["model"]))
    hero = thumb_figure(thumb) if thumb else ""
    body = f'''<article class="prose wide"><p class="byline">By {BRAND} editorial team</p><h1>{E(title)}</h1>
<p class="sub">Owner's manual checked {checked}</p>
{hero}
<div class="answer"><p><strong>Direct answer</strong></p><ul>{"".join(lead)}</ul></div>
{note}
<p>Confirm every part against the owner's manual and the vehicle itself. This is a guide, not a repair instruction. Lamp packages change by trim, and a later book can change a chart. See the <a href="{u('/fitment/')}">fitment guide</a> for how we read a chart, and the <a href="{u('/fitment/key-fob-battery/')}">key fob battery</a> hub if you only need the cell.</p>
<h2>Part fit</h2>
<div class="tablewrap"><table class="list"><thead><tr><th scope="col">Part</th><th scope="col">What the manual prints</th><th scope="col">Source</th></tr></thead><tbody>{"".join(rows)}</tbody></table></div>
{mid_related}
{problem_html}
{compare}
<section class="faq" aria-labelledby="faq-h"><h2 id="faq-h">Frequently asked questions</h2>{"".join(f"<details><summary>{E(q)}</summary><p>{E(a)}</p></details>" for q, a in faqs)}</section>
{sib_html}
{end_related}
<p>Related: <a href="{u(model_href)}">All {E(v["make"])} {E(v["model"])} years</a> · <a href="{u(make_href)}">All {E(v["make"])} models</a> · <a href="{u('/fitment/')}">How to read a fitment chart</a> · {part_anchors()} · <a href="{u('/cars/')}">All cars</a></p>
<section class="sources" aria-labelledby="src-h"><h2 id="src-h">Sources</h2><ul>{srcs}</ul>
<p class="note">Retrieved {checked}. {BRAND} is not affiliated with {E(v["make"])}. Names are used only to identify the vehicle.</p></section>
</article>'''
    article = article_ld(title, path, v["published"], v["modified"],
                         image=thumb["src"] if thumb else None)
    faqld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}
    crumbs = [("/", "Home"), ("/cars/", "Cars"), (make_href, v["make"]), (model_href, v["model"]), (path, v["year"])]
    write(path, page(path, title, desc, body, [article, faqld], crumbs, modified=v["modified"]))

def problems_block(v, nhtsa, checked=PUBLISHED_H):
    if not v["nhtsa"]:
        return ('''<h2>Common problems on record</h2>
<p>NHTSA's recalls API does not accept this model name, so this page does not invent a recall list and does not borrow another model's campaigns. Look up the VIN at <a href="https://www.nhtsa.gov/recalls" rel="nofollow noopener" target="_blank">nhtsa.gov/recalls</a>.</p>''', "")
    if not nhtsa:
        return ('''<h2>Common problems on record</h2>
<p>The NHTSA file for this page has not been retrieved yet. Look up the VIN at <a href="https://www.nhtsa.gov/recalls" rel="nofollow noopener" target="_blank">nhtsa.gov/recalls</a>.</p>''', "")
    chunks = ["<h2>Common problems on record</h2>",
              "<p>These are NHTSA recall campaigns and owner complaint counts. They are not a ranked list of what will fail, and a complaint is not a finding that a defect exists.</p>"]
    for g in nhtsa["groups"]:
        label = f"{v['make']} {g['model']} {v['year']}"
        rec = g["recalls"]
        chunks.append(f"<h3>Recalls filed for {E(label)}</h3>")
        if rec.get("error"):
            chunks.append("<p>The recalls API did not return a campaign list for this model name. Look up the VIN at <a href=\"https://www.nhtsa.gov/recalls\" rel=\"nofollow noopener\" target=\"_blank\">nhtsa.gov/recalls</a>.</p>")
        elif not rec.get("items"):
            chunks.append("<p>The recalls API returned no campaigns for this model year.</p>")
        else:
            trs = []
            for item in rec["items"]:
                camp = f"https://api.nhtsa.gov/recalls/campaignNumber?campaignNumber={item['id']}"
                flag = " Park the vehicle if NHTSA says so." if item.get("park") else ""
                trs.append(
                    f'<tr><td>{ext_link(item["id"], camp)}</td><td>{E(item["component"])}</td>'
                    f'<td>{E(item["date"])}{E(flag)}</td></tr>')
            chunks.append('<div class="tablewrap"><table class="list"><thead><tr><th scope="col">Campaign</th><th scope="col">Component</th><th scope="col">Report received</th></tr></thead><tbody>'
                          + "".join(trs) + "</tbody></table></div>")
        comp = g["complaints"]
        chunks.append(f"<h3>Owner complaints filed for {E(label)}</h3>")
        if comp.get("error"):
            chunks.append(f"<p>The complaints API returned an error ({E(comp['error'])}).</p>")
        elif comp.get("count") is None:
            chunks.append("<p>Complaint counts were not retrieved.</p>")
        else:
            top = comp.get("top") or []
            top_s = ", ".join(f"{E(name)} ({n})" for name, n in top[:3]) if top else "no component names were counted"
            n = comp["count"]
            noun = "complaint" if n == 1 else "complaints"
            chunks.append(
                f"<p>NHTSA's complaint API returned {n} {noun} for this model year, retrieved {checked}. "
                f"The components named most often were {top_s}. These are reports owners filed, not a confirmed defect list.</p>")
    return ("".join(chunks), "")

def hubs():
    makes = []
    for v in VEHICLES:
        if v["make"] not in makes:
            makes.append(v["make"])
    # /cars/
    cards = []
    for make in makes:
        vs = [v for v in VEHICLES if v["make"] == make]
        links = ", ".join(f'<a href="{u(vpath(v))}">{E(v["model"])} {E(v["year"])}</a>' for v in vs)
        cards.append(f'<li class="card"><h2><a href="{u("/cars/" + slugify(make) + "/")}">{E(make)}</a></h2><p>{links}</p></li>')
    car_faqs = [
        ("Which car should I look up?",
         "Pick the make, then the model, then the year whose owner's manual we opened. That year page lists the key fob battery, the wiper parts, and the bulb chart."),
        ("Which year should I open?",
         "Open the model year of your vehicle. Do not reuse a chart from a different year."),
    ]
    car_faq_html = "".join(f"<details><summary>{E(q)}</summary><p>{E(a)}</p></details>" for q, a in car_faqs)
    body = f'''<h1>Which car should I look up?</h1>
<p class="answer">Pick a vehicle for the key fob battery, wiper parts, and bulb types printed in that year's owner's manual, plus the NHTSA recalls on file for that model year.</p>
<ul class="cards">{"".join(cards)}</ul>
<p>Related: <a href="{u('/fitment/')}">How we read a key fob battery, a wiper size, and a bulb chart</a> · {part_anchors()}</p>
<section class="faq" aria-labelledby="faq-h"><h2 id="faq-h">Which part fits?</h2>{car_faq_html}</section>'''
    car_title = "Which car should I look up?"
    car_faq_ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in car_faqs]}
    write("/cars/", page("/cars/", car_title,
                         "Which car should I look up? Open the make and model, then the year whose owner's manual we checked.",
                         body, [article_ld(car_title, "/cars/"), car_faq_ld],
                         [("/", "Home"), ("/cars/", "Cars")], modified=latest(VEHICLES)))
    for make in makes:
        vs = [v for v in VEHICLES if v["make"] == make]
        models = []
        for v in vs:
            if v["model"] not in models:
                models.append(v["model"])
        blocks = []
        for model in models:
            years = sorted((v for v in vs if v["model"] == model), key=lambda v: v["year"])
            year_links = ", ".join(f'<a href="{u(vpath(v))}">{E(v["year"])}</a>' for v in years)
            blocks.append(f'<li class="card"><h2><a href="{u("/cars/" + slugify(make) + "/" + slugify(model) + "/")}">{E(model)}</a></h2><p>Years with a manual checked: {year_links}</p></li>')
        path = f"/cars/{slugify(make)}/"
        make_title = f"Which {make} model should I pick?"
        make_faqs = [
            (f"Which {make} model should I pick?",
             f"Open the model, then the year. This page lists the {make} models whose owner's manual we have opened. A part from one model is not a part for another."),
            (f"Which {make} year should I open?",
             "Each model card lists the years we checked. The year page quotes that year's book. Do not copy a part from one year onto another."),
            (f"Which key fob battery, wiper, or bulb fits a {make}?",
             "It depends on the model and the year. The year page has the key fob cell, the wiper line, and the bulb chart from that owner's manual, plus NHTSA recalls when the API returns them."),
        ]
        make_faq_html = "".join(f"<details><summary>{E(q)}</summary><p>{E(a)}</p></details>" for q, a in make_faqs)
        make_faq_ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in make_faqs]}
        body = f'''<h1>{E(make_title)}</h1>
<p class="answer">{E(make)} model years we have checked against an owner's manual. Each year has its own page. Do not copy a part from one year onto another.</p>
<ul class="cards">{"".join(blocks)}</ul>
<p>Related: {part_anchors()} · <a href="{u('/cars/')}">All cars</a> · <a href="{u('/fitment/')}">How to read a fitment chart</a></p>
<section class="faq" aria-labelledby="faq-h"><h2 id="faq-h">Which {E(make)} should I open?</h2>{make_faq_html}</section>'''
        write(path, page(path, make_title,
                         f"Which {make} model should I open? Each year page quotes that year's owner's manual for the key fob, wipers, bulbs, and NHTSA recalls.",
                         body, [article_ld(make_title, path), make_faq_ld],
                         [("/", "Home"), ("/cars/", "Cars"), (path, make)], modified=latest(vs)))
        for model in models:
            years = sorted((v for v in vs if v["model"] == model), key=lambda v: v["year"])
            items = "".join(
                f'<li><a href="{u(vpath(v))}">{E(v["year"])} {E(make)} {E(model)}</a>: {E(fit_map(v)["key"][1][:180])}</li>'
                for v in years)
            path = f"/cars/{slugify(make)}/{slugify(model)}/"
            def short(text, n=110):
                text = re.sub(r"\s+", " ", text).strip()
                return text if len(text) <= n else text[:n].rsplit(" ", 1)[0] + "..."
            comp = "".join(
                "<tr><td><a href=\"%s\">%s</a></td><td>%s</td><td>%s</td><td>%s</td></tr>" % (
                    u(vpath(v)), E(v["year"]),
                    E(short(fit_map(v)["key"][1])),
                    E(short(fit_map(v)["wiper"][1])),
                    E(short(fit_map(v)["head"][1])),
                ) for v in years)
            meta = HUB_META.get((make, model), {})
            faqs = meta.get("faqs") or [
                (f"Which key fob battery fits a {make} {model}?",
                 "It depends on the year, and sometimes on which remote is in the car. Open the year page. The short battery line for each year we have checked is in the table on this page."),
                (f"Which wiper blade fits a {make} {model}?",
                 "Use the year page. Some manuals print an inch length, and some print only a part number or say the length is not in the book. Do not reuse a length from a different year."),
                (f"Which bulb fits a {make} {model}?",
                 "The headlight, brake, and turn rows are on the year page, copied from that year's owner's manual. Trims in the same year can take different lamps."),
            ]
            faq_html = "".join(f"<details><summary>{E(q)}</summary><p>{E(a)}</p></details>" for q, a in faqs)
            faqld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
                {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}
            model_title = meta.get("title") or f"Which {make} {model} year should I pick?"
            thumb = MODEL_THUMBS.get((make, model))
            hero = thumb_figure(thumb) if thumb else ""
            # Related reads for the hub: year pages, sibling models, part hubs.
            next_items = []
            model_thumb = MODEL_THUMBS.get((make, model))
            for v in years[:2]:
                next_items.append((vpath(v),
                                   f"{v['year']} {make} {model} parts",
                                   "Full chart and NHTSA campaigns for that model year.",
                                   model_thumb))
            for photo_make, photo_model in (("Tesla", "Model Y"), ("Toyota", "Camry"), ("Toyota", "RAV4")):
                if (photo_make, photo_model) == (make, model):
                    continue
                photo = MODEL_THUMBS.get((photo_make, photo_model))
                if not photo:
                    continue
                next_items.append((f"/cars/{slugify(photo_make)}/{slugify(photo_model)}/",
                                   f"{photo_make} {photo_model} parts",
                                   "Key, wiper, and bulb lines from that model's owner's manual.",
                                   photo))
                if len(next_items) >= 4:
                    break
            if len(next_items) < 4:
                next_items.append(("/fitment/wiper-blades/",
                                   "Wiper blade hub",
                                   "Front and rear wiper lines copied from owner's manuals.",
                                   None))
            next_html = related_reads(next_items[:4], "Next reads")
            compare = (
                f'<aside class="compare" aria-label="Check another vehicle">'
                f"<h2>Check another model or part</h2>"
                f'<p>Open a year in the table, or browse <a href="{u("/cars/" + slugify(make) + "/")}">all {E(make)} models</a>. '
                f'Part hubs: {part_anchors()}.</p>'
                f'<p><a href="{u("/")}">Use the year picker</a> for a different make.</p>'
                f"</aside>"
            )
            extra = HUB_EXTRA.get((make, model), "")
            body = f'''<article class="prose wide"><p class="byline">By {BRAND} editorial team</p><h1>{E(model_title)}</h1>
{hero}
{extra}
<p class="answer">Each row is one model year whose owner's manual we opened. The cells are shortened. The year page has the full chart and the manual link.</p>
<div class="tablewrap"><table class="list"><thead><tr><th scope="col">Year</th><th scope="col">Key fob battery</th><th scope="col">Front wiper</th><th scope="col">Headlight</th></tr></thead><tbody>{comp}</tbody></table></div>
<ul>{items}</ul>
{compare}
{next_html}
<section class="faq" aria-labelledby="faq-h"><h2 id="faq-h">Which part fits this {E(model)}?</h2>{faq_html}</section>
<p>Related: <a href="{u('/cars/' + slugify(make) + '/')}">All {E(make)} models</a> · {part_anchors()} · <a href="{u('/cars/')}">All cars</a></p></article>'''
            hub_mod = latest(years)
            hub_pub = min(v.get("published", PUBLISHED) for v in years)
            write(path, page(path, model_title,
                             meta.get("desc") or f"Which {make} {model} year should I open? The table quotes each checked year's owner's manual.",
                             body, [article_ld(model_title, path, published=hub_pub, modified=hub_mod,
                                               image=thumb["src"] if thumb else None), faqld],
                             [("/", "Home"), ("/cars/", "Cars"), (f"/cars/{slugify(make)}/", make), (path, model)],
                             modified=hub_mod))

def fitment_pages():
    intro = f'''<h1>Which part fits my car?</h1>
<p class="answer">Three fitment facts owners look up, and where each one is printed. This site copies the figure only when an owner's manual or a manufacturer parts table prints it.</p>
<h2>Key fob battery</h2>
<p>The owner's manual names the coin cell in the remote chapter. Some vehicles print two cells because the integrated key and the push button remote are different. Match the remote in your hand, not just the model year. See every page we have checked on the <a href="{u('/fitment/key-fob-battery/')}">key fob battery</a> hub.</p>
<h2>Wiper size</h2>
<p>Some manuals print an inch length. Ford's books often print a Motorcraft part number instead, and they do not print the inches next to it. We do not turn a part number into a length. Rear wipers are listed only when the manual prints a rear part. See the <a href="{u('/fitment/wiper-blades/')}">wiper blade</a> hub.</p>
<h2>Bulb chart</h2>
<p>The bulb chart is in the owner's manual, usually near the capacities or the light bulb section. It is not on the tire placard. The tire placard, on the driver's door jamb, is for tire size and cold pressure. Where a chart lists halogen and LED rows, both are on the page, because the trim decides which one you have. See <a href="{u('/fitment/headlight-bulbs/')}">headlights</a>, <a href="{u('/fitment/brake-lights/')}">brake lights</a>, and <a href="{u('/fitment/turn-signals/')}">turn signals</a>.</p>
<h2>Recalls</h2>
<p>Open recalls are looked up with the VIN at <a href="https://www.nhtsa.gov/recalls" rel="nofollow noopener" target="_blank">nhtsa.gov/recalls</a>. The year pages also list the campaigns NHTSA's public API returned for that model year.</p>'''
    faqs = [
        ("Which key fob battery fits my car?",
         "Open the year page for your make, model, and year, or use the picker on the home page. The cell is whatever that year's owner's manual prints, often a CR2032, and sometimes a second cell for a different remote. Do not buy from the model name alone."),
        ("Which wiper blade fits my car?",
         "Use the year page. If the manual prints an inch length, that length is on the page. If it prints only a part number, or does not print a length, the page says so. A length from another year is not a substitute."),
        ("Which bulb fits my car?",
         "Use the year page for the headlight, brake light, and turn signal rows. The tire label on the driver's door jamb does not list bulb numbers. Match the row to your trim when the manual lists more than one lamp package."),
        ("Where is the key fob battery printed?",
         "In the owner's manual chapter on the remote or the key. The cell type is a CR number such as CR2032. If the book lists two remotes, they can take two different cells."),
        ("Where do I look up a recall?",
         "Enter the VIN at https://www.nhtsa.gov/recalls. A campaign number on our year pages links to NHTSA's record for that campaign."),
    ]
    faq_html = "".join(f"<details><summary>{E(q)}</summary><p>{E(a)}</p></details>" for q, a in faqs)
    body = f'<article class="prose"><p class="byline">By {BRAND}</p>{intro}<section class="faq" aria-labelledby="faq-h"><h2 id="faq-h">Frequently asked questions</h2>{faq_html}</section></article>'
    faqld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}
    fit_title = "Which part fits my car?"
    article = article_ld(fit_title, "/fitment/")
    write("/fitment/", page("/fitment/", fit_title,
                            "Which key fob battery, wiper, or bulb fits? A year page copies the figure only when that owner's manual prints it.",
                            body, [article, faqld], [("/", "Home"), ("/fitment/", "Part fit")]))
    groups = {
        "key": ["key"],
        "wiper": ["wiper", "rear"],
        "head": ["head"],
        "brake": ["brake"],
        "turn": ["turn"],
    }
    for key, slug, label, blurb in PARTS:
        lis = []
        listed = []
        for v in VEHICLES:
            fm = fit_map(v)
            bits = []
            for part in groups[key]:
                if part in fm:
                    bits.append(f"{fm[part][0]}: {fm[part][1]}")
            if not bits:
                continue
            text = " ".join(bits)
            if len(text) > 220:
                text = text[:217].rsplit(" ", 1)[0] + "..."
            lis.append(f'<li><a href="{u(vpath(v))}">{E(v["year"])} {E(v["make"])} {E(v["model"])}</a>: {E(text)}</li>')
            listed.append(v)
        path = f"/fitment/{slug}/"
        part_title = f"Which {label.lower()} should I pick?"
        q = f"Which {label.lower()} fits my car?"
        a = (f"Pick the make, model, and year. The list on this page is every {label.lower()} line we copied from an owner's manual. "
             "Open that year for the full wording and the manual link. A part from a different year is not a match.")
        hub_faqs = [(q, a)]
        faq_html = "".join(f"<details><summary>{E(qq)}</summary><p>{E(aa)}</p></details>" for qq, aa in hub_faqs)
        faqld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": qq, "acceptedAnswer": {"@type": "Answer", "text": aa}} for qq, aa in hub_faqs]}
        others = " · ".join(
            f'<a href="{u("/fitment/" + oslug + "/")}">{E(olabel)}</a>'
            for _, oslug, olabel, _ in PARTS if oslug != slug)
        body = f'''<h1>{E(part_title)}</h1>
<p class="answer">{E(blurb)} Open the year page for the full chart and the manual link. A figure from one year is not a figure for the next year.</p>
<section class="faq" aria-labelledby="faq-h"><h2 id="faq-h">Which {E(label.lower())} fits my car?</h2>{faq_html}</section>
<ul>{"".join(lis)}</ul>
<p>Related: {others} · <a href="{u('/fitment/')}">How to read these charts</a> · <a href="{u('/cars/')}">All cars</a> · <a href="{u('/')}">Use the year picker</a></p>'''
        write(path, page(path, part_title,
                         f"Which {label.lower()} fits your car? Every line here is copied from that model year's owner's manual.",
                         body, [article_ld(part_title, path), faqld],
                         [("/", "Home"), ("/fitment/", "Part fit"), (path, label)], modified=latest(listed)))

def home(catalog):
    makes = []
    for v in VEHICLES:
        if v["make"] not in makes:
            makes.append(v["make"])
    cards = []
    for make in makes:
        vs = [v for v in VEHICLES if v["make"] == make]
        links = ", ".join(f'<a href="{u(vpath(v))}">{E(v["model"])} {E(v["year"])}</a>' for v in vs)
        cards.append(f'<li class="card"><h3><a href="{u("/cars/" + slugify(make) + "/")}">{E(make)}</a></h3><p>{links}</p></li>')
    part_links = "".join(f'<li><a href="{u("/fitment/" + slug + "/")}">{E(label)}</a></li>' for _, slug, label, _ in PARTS)
    body = f'''<section class="hero"><h1>Which battery, wiper, and bulb fits your car?</h1>
<p class="answer">Look up the key fob battery, wiper parts, and bulb sizes printed in the owner's manual for a make, model, and year, plus the NHTSA recalls on file for that model year. We do not invent a part number.</p>
<form class="picker" id="picker">
<label for="pick-make">Make<select id="pick-make" name="make" required></select></label>
<label for="pick-model">Model<select id="pick-model" name="model" required></select></label>
<label for="pick-year">Year<select id="pick-year" name="year" required></select></label>
<button class="btn" type="submit">Show this vehicle</button>
</form>
<p id="pick-status" class="note" role="status" hidden></p>
<script type="application/json" id="catalog">{json.dumps(catalog)}</script>
</section>
<h2>Cars by make</h2><ul class="cards">{"".join(cards)}</ul>
<h2>Look up by part</h2><ul class="cols">{part_links}</ul>
<h2>How a page is built</h2><p>We open that year's owner's manual and copy the key fob cell, the wiper part or length, and the bulb chart, with the manual linked on the page. Recalls and complaint counts come from NHTSA's public API for that model year. If the manual does not print a figure, the page says so. <a href="{u('/methodology/')}">Sources and methods</a>.</p>
<section class="faq" aria-labelledby="faq-h"><h2 id="faq-h">Which part fits my car?</h2>
<details><summary>Which key fob battery fits my car?</summary><p>Choose the make, model, and year in the picker above. The year page quotes the cell the owner's manual prints. Some cars have two remotes and two different cells.</p></details>
<details><summary>Which wiper blade fits my car?</summary><p>The year page lists the front and rear wiper line from that year's manual. Use an inch length only when the manual prints one.</p></details>
<details><summary>Which bulb fits my car?</summary><p>The year page lists the headlight, brake light, and turn signal lines from that year's bulb chart. The door jamb label is for tires, not bulbs.</p></details>
</section>'''
    home_faqs = [
        ("Which key fob battery fits my car?",
         "Choose the make, model, and year in the picker. The year page quotes the cell the owner's manual prints. Some cars have two remotes and two different cells."),
        ("Which wiper blade fits my car?",
         "The year page lists the front and rear wiper line from that year's manual. Use an inch length only when the manual prints one."),
        ("Which bulb fits my car?",
         "The year page lists the headlight, brake light, and turn signal lines from that year's bulb chart. The door jamb label is for tires, not bulbs."),
    ]
    home_faq = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in home_faqs]}
    write("/", page("/", "Which battery, wiper, or bulb fits?",
                    "Which key fob battery, wiper, or bulb fits your car? Pick the year. Figures come from that owner's manual, plus NHTSA recalls.",
                    body, home_faq, modified=latest(VEHICLES)))

def privacy_analytics():
    if NOINDEX:
        return (
            "<p>This preview build does not load Cloudflare Web Analytics or Google Analytics 4. "
            "The launch build loads Cloudflare Web Analytics on every page. That product does not use cookies and does not track you across sites. "
            "Google Analytics 4 loads only after you accept the cookie banner. Consent Mode v2 starts with ad storage, ad user data, ad personalization, and analytics storage denied, and the Google Analytics script stays unloaded until you accept.</p>"
        )
    return (
        "<p>We use Cloudflare Web Analytics on every page to count visits. It does not use cookies and does not track you across sites. "
        "We use Google Analytics 4 only after you accept the cookie banner. Consent Mode v2 keeps ad storage, ad user data, ad personalization, and analytics storage denied until then, and the Google Analytics script does not load. "
        "If you accept, analytics storage is granted and Google Analytics 4 may set a cookie to measure visits. Accepting this banner does not grant ad storage. "
        "Use Cookie settings in the footer to change your choice. Choosing reject after an accept sets analytics storage back to denied. A hit may already have been sent.</p>"
    )

def privacy_cookies():
    if NOINDEX:
        return (
            "<p>This preview build sets no cookies. After launch, Google Analytics 4 may set a cookie only if you accept. "
            "That choice is stored in local storage on your device. Cloudflare Web Analytics does not use cookies. The site works if you reject Google Analytics 4.</p>"
        )
    return (
        "<p>Cloudflare Web Analytics does not use cookies. Google Analytics 4 may set a cookie only after you accept. "
        "The accept or reject choice is stored in local storage in your browser so the banner can stay dismissed. It stays on your device. "
        f"{BRAND} does not sell personal information.</p>"
    )

def simple(path, title, desc, h1, inner, crumb=None, legal=False, modified=None, published=None):
    body = f'<article class="prose"><h1>{E(h1)}</h1>{inner}</article>'
    if legal:
        body = f'<article class="prose"><h1>{E(h1)}</h1>{inner}<p class="legal-line">{LEGAL_LINE}</p></article>'
    mod = modified or PUBLISHED
    write(path, page(path, title, desc, body,
                     article_ld(title, path, published=published or PUBLISHED, modified=mod),
                     crumbs=[("/", "Home"), (path, crumb or h1)], legal=legal, modified=mod))

def static_pages():
    simple("/about/", f"About {BRAND}", "What Which Car Fit is and how the vehicle pages are checked.",
           f"About {BRAND}", f'''
<p>{BRAND} answers a narrow question: for this make, model, and year, what key fob battery, wiper part, and bulb types does the owner's manual print, and what has NHTSA published?</p>
<h2>What we cover</h2><p>High volume models sold in the United States, one page per model year whose manual we have opened. We add a year when that year's book has been read. We do not fill a year with a neighboring year's chart.</p>
<h2>Independence</h2><p>{BRAND} is not affiliated with, endorsed by, or sponsored by any car maker or parts seller. Make and model names are used only to identify the vehicle.</p>
<p>See <a href="{u('/methodology/')}">sources and methods</a> or <a href="{u('/contact/')}">send a correction</a>.</p>''')
    simple("/methodology/", f"Sources and methods | {BRAND}",
           "Where Which Car Fit's battery, wiper, bulb, and recall facts come from.",
           "Sources and methods", f'''
<p>Last checked {PUBLISHED_H}.</p>
<h2>Owner's manuals</h2><p>Battery type, wiper part or length, and bulb type come from that model year's owner's manual. The page number or the chart name is in the source note. If a chart lists two lamp packages, both stay on the page. If the manual does not print a figure, we do not borrow one from a parts counter, a forum, or another year.</p>
<h2>NHTSA</h2><p>Recall campaigns come from NHTSA's recalls API for that make, model, and model year. Complaint counts come from the complaints API. We store the count and the component names, not the complaint stories. A complaint is an owner report. It is not a finding that a part is defective. The VIN lookup at nhtsa.gov/recalls is the check for a specific car.</p>
<h2>What we leave out</h2><p>We do not print repair steps. We do not turn a Motorcraft part number into an inch length unless the manual prints the inches. We do not use another site's bulb chart as the source.</p>
<h2>Dates</h2><p>The published date is the day the page was first written. It does not change on a rebuild. The modified date changes when a fact on the page changes.</p>''', "Sources and methods")
    simple("/image-policy/", f"Image policy | {BRAND}", "How Which Car Fit uses images, diagrams, and car maker marks.",
           "Image policy", f'''
<p>Last updated 19 Nov 2026.</p>
<h2>Graphics</h2><p>The mark in the header and the sharing image are original drawings of a key. They are not photos of a vehicle and they are not a car maker's logo.</p>
<h2>Photos</h2><p>Some hub pages show one realistic, news style photograph. Those images are AI generated. They are atmospheric and unbadged. They are not factory photos, owner photos, or a claim about a specific trim. Every photograph on the site links back to this page and is labelled as AI generated in its caption.</p>
<h2>Names</h2><p>Make and model names appear in plain text so you can tell which vehicle a page describes. We do not display car maker logos, and the names do not imply affiliation.</p>
<h2>Questions</h2><p>If you believe an image uses your work, see the <a href="{u('/copyright/')}">copyright policy</a> or <a href="{u('/contact/')}">contact us</a>.</p>''',
           "Image policy", modified="2026-11-19")
    simple("/contact/", f"Contact {BRAND}", "Email Which Car Fit a correction or a question.",
           "Contact us", f'''
<p>Questions and corrections go to <a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a>.</p>
<h2>Corrections</h2><p>Send the page address, the line that looks wrong, and a link to the owner's manual or the NHTSA campaign that shows it. We change the checked date when we re verify a fact.</p>
<p class="note">The address above is the inbox for this site. See the <a href="{u('/privacy/')}">privacy policy</a> for what we do with a message.</p>''', "Contact")
    D = PUBLISHED_H
    legal = {
        "/terms/": ("Terms of Use", f'''<p>Last updated {D}. These terms govern your use of whichcarfit.com ("{BRAND}", "we", "us"). {BRAND} is a trade name of Joshua Israel Ventures LLC, a Florida limited liability company. By using the site you agree to these terms.</p>
<h2>Information only</h2><p>{BRAND} provides general information about published part fit and public safety filings. It is not repair instruction, and it is not professional advice. Always confirm a part on the vehicle and in the owner's manual. Recalls for a specific car are confirmed with the VIN at NHTSA.</p>
<h2>Accuracy</h2><p>We cite our sources and we leave out what we cannot verify. We do not warrant that a page is complete or current. Manuals are revised, and trims differ.</p>
<h2>Acceptable use</h2><p>You may view pages and share links for personal, non commercial use. You may not scrape the site in bulk, republish our original text, or try to disrupt the site.</p>
<h2>Intellectual property</h2><p>Original text, the compilation of these pages, and the site design belong to Joshua Israel Ventures LLC. Vehicle names and trademarks belong to their owners and are used only to identify the vehicles. Their use does not imply affiliation or endorsement.</p>
<h2>Third party services</h2><p>We link to owner's manuals, NHTSA, and other sources. The site is hosted on GitHub Pages. We are not responsible for those sites.</p>
<h2>Disclaimer of warranties and limitation of liability</h2><p>The site is provided "as is" and "as available". To the fullest extent permitted by law, Joshua Israel Ventures LLC disclaims all warranties and will not be liable for any indirect, incidental, special, consequential, or punitive damages, or any loss from use of the site or from a parts purchase. Our total liability for any claim relating to the site is limited to US$100.</p>
<h2>Indemnity</h2><p>You agree to indemnify Joshua Israel Ventures LLC against claims arising from your misuse of the site or your breach of these terms.</p>
<h2>Governing law</h2><p>These terms are governed by the laws of the State of Florida, United States, without regard to conflict of law rules.</p>
<h2>Changes</h2><p>We may update these terms. The date above is the latest version. Questions: <a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a>.</p>'''),
        "/privacy/": ("Privacy Policy", f'''<p>Last updated 19 Nov 2026. This policy explains how {BRAND} (whichcarfit.com), a trade name of Joshua Israel Ventures LLC, a Florida limited liability company, handles information.</p>
<h2>Analytics</h2>{privacy_analytics()}
<h2>Email</h2><p>If you email {CONTACT_EMAIL}, we receive your address and your message so we can reply. We keep them only as long as needed for that reply and for a correction log.</p>
<h2>Advertising</h2><p>To keep {BRAND} free, pages may load Google AdSense. The AdSense account meta and script are present sitewide. Ad units are not placed on pages yet. Google and its partners may use cookies or similar technologies to serve and measure ads once units are enabled. See <a href="https://policies.google.com/technologies/ads" rel="nofollow noopener" target="_blank">how Google uses cookies in advertising</a>. You can opt out of personalized advertising at <a href="https://www.google.com/settings/ads" rel="nofollow noopener" target="_blank">Google Ads Settings</a> and <a href="https://www.aboutads.info/choices/" rel="nofollow noopener" target="_blank">aboutads.info</a>. Consent Mode on this site keeps ad storage denied until you accept.</p>
<h2>Google advertising cookies and your choices</h2><p>Third-party vendors, including Google, use cookies to serve ads based on a user's prior visits to this website or other websites. Google's use of advertising cookies enables it and its partners to serve ads based on your visit to this site and/or other sites on the Internet. You may opt out of personalized advertising by visiting <a href="https://adssettings.google.com/" rel="nofollow noopener">Google Ads Settings</a>. Alternatively, you can opt out of a third-party vendor's use of cookies for personalized advertising at <a href="https://www.aboutads.info/choices/" rel="nofollow noopener">aboutads.info/choices</a>. For more information, see <a href="https://policies.google.com/technologies/partner-sites" rel="nofollow noopener">how Google uses information from sites or apps that use its services</a>.</p>
<h2>Cookies</h2>{privacy_cookies()}
<h2>Hosting</h2><p>The site is hosted on GitHub Pages, which may log IP addresses for security and operations.</p>
<h2>Your rights</h2><p>You can ask us to access, correct, or delete personal information we hold. Email {CONTACT_EMAIL}. Residents of some states may have additional rights, which we will honor.</p>
<h2>Children</h2><p>The site is not directed to children under 13. We do not knowingly collect personal information from children.</p>
<h2>Changes</h2><p>We will post changes on this page with a new date.</p>'''),
        "/disclaimer/": ("Disclaimer", f'''<p>Last updated {D}.</p>
<h2>Not a car maker</h2><p>{BRAND} is an independent site. It is not affiliated with, endorsed by, or sponsored by any car maker, dealer, or parts seller. Names are used only to identify the vehicles.</p>
<h2>Confirm the part</h2><p>Manuals change, and two trims of the same model year can take different lamps. The manual and the vehicle win over this page. This is a guide, not a repair instruction.</p>
<h2>Recalls</h2><p>Recall lists are what NHTSA published for the model year when we retrieved them. A specific car can differ. Check the VIN at NHTSA.</p>
<h2>Corrections</h2><p>Email <a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a> and we will correct a verified mistake.</p>
<h2>Limitation of liability</h2><p>To the extent permitted by law, Joshua Israel Ventures LLC is not liable for a loss from reliance on this site. See the <a href="{u('/terms/')}">terms of use</a>.</p>'''),
        "/copyright/": ("Copyright and DMCA Policy", f'''<p>Last updated {D}. Original text and the compilation of these pages are owned by Joshua Israel Ventures LLC. Facts are cited to the manuals and to NHTSA. See the <a href="{u('/image-policy/')}">image policy</a>.</p>
<h2>Reporting infringement</h2><p>If you believe material on this site infringes your copyright, email <a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a> with: your name and contact details; a description of the work; the URL on our site; a statement that you have a good faith belief the use is not authorized; a statement, under penalty of perjury, that the notice is accurate and that you are the owner or are authorized to act; and your physical or electronic signature. We will review notices and remove or disable material where appropriate.</p>
<h2>Counter notice</h2><p>If your material was removed and you believe that was a mistake, you may send a counter notice with the details required by 17 U.S.C. § 512(g).</p>
<h2>Repeat infringers</h2><p>We will act against repeat infringement where appropriate.</p>'''),
        "/ad-disclosure/": ("Advertising and Affiliate Disclosure", f'''<p>Last updated 19 Nov 2026. {BRAND} is free to use. Pages include the Google AdSense head script and publisher meta ({ADSENSE_CLIENT}) so the site can be reviewed. Ad units are not placed on pages yet, and there are no affiliate links today.</p>
<p>When ad units go live, Google may show ads on a page. The site may also link to a seller for the exact part type the manual names, such as a CR2032 when the manual says CR2032. We will not invent a compatibility claim to earn a fee. Any paid link will be labeled.</p>
<h2>Editorial independence</h2><p>No car maker pays for a change to a chart. Questions: <a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a>.</p>'''),
    }
    legal_mod = {
        "/privacy/": "2026-11-19",
        "/ad-disclosure/": "2026-11-19",
    }
    for path, (title, inner) in legal.items():
        simple(path, f"{title} | {BRAND}", f"{title} for {BRAND} (whichcarfit.com).", title, inner,
               title, legal=True, modified=legal_mod.get(path))

def not_found():
    body = f'<h1>Page not found</h1><p>That page is not on this site. Try the <a href="{u("/cars/")}">car lookup</a> or the <a href="{u("/fitment/")}">part fit guide</a>.</p>'
    html_doc = page("/404.html", f"Page not found | {BRAND}", "That page is not on Which Car Fit.", body, noindex=True)
    with open(os.path.join(ROOT, "404.html"), "w") as f:
        f.write(html_doc)

def graphics():
    # Original mark only. No car maker logos.
    svg = LOGO.replace('width="34" height="34" ', 'xmlns="http://www.w3.org/2000/svg" ').replace(' aria-hidden="true" focusable="false"', "")
    with open(os.path.join(ROOT, "favicon.svg"), "w") as f:
        f.write(svg)
    try:
        from PIL import Image, ImageDraw
        font = None
        small = None
        for cand in ("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
                     "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"):
            if os.path.exists(cand):
                from PIL import ImageFont
                font = ImageFont.truetype(cand, 72)
                small = ImageFont.truetype(cand, 36)
                break
        im = Image.new("RGB", (128, 128), "#0b3954")
        d = ImageDraw.Draw(im)
        d.rounded_rectangle((8, 8, 120, 120), radius=24, fill="#0b3954", outline="#ffb347", width=4)
        d.ellipse((28, 28, 68, 68), outline="#ffb347", width=6)
        d.ellipse((42, 42, 54, 54), fill="#e6f4f1")
        d.rectangle((64, 42, 100, 54), fill="#087e8b")
        d.rectangle((88, 54, 100, 70), fill="#087e8b")
        im.save(os.path.join(ROOT, "logo.png"))
        og = Image.new("RGB", (1200, 630), "#0b3954")
        dr = ImageDraw.Draw(og)
        dr.rectangle((0, 0, 1200, 16), fill="#ffb347")
        dr.ellipse((80, 180, 280, 380), outline="#ffb347", width=16)
        dr.ellipse((150, 250, 210, 310), fill="#e6f4f1")
        dr.rectangle((270, 255, 470, 315), fill="#087e8b")
        dr.text((500, 220), "Which Car Fit", fill="#ffffff", font=font)
        dr.text((500, 320), "Key fob, wipers, bulbs, recalls", fill="#ffb347", font=small)
        og.save(os.path.join(ROOT, "og.png"))
    except Exception as e:
        print("graphics skipped", e)

def extras(catalog):
    with open(os.path.join(ROOT, "CNAME"), "w") as f:
        f.write(DOMAIN + "\n")
    with open(os.path.join(ROOT, f"{INDEXNOW_KEY}.txt"), "w") as f:
        f.write(INDEXNOW_KEY)
    # AdSense ads.txt (publisher id without the ca- prefix).
    pub = ADSENSE_CLIENT.replace("ca-", "", 1)
    with open(os.path.join(ROOT, "ads.txt"), "w") as f:
        f.write("")  # AdSense detached 21 Nov 2026 until the account is approved (see seo-central/site-seo-rules.md). Do not re-add.
    bots = ["*", "Googlebot", "Bingbot", "Mediapartners-Google", "OAI-SearchBot", "ChatGPT-User",
            "GPTBot", "PerplexityBot", "Perplexity-User", "ClaudeBot", "Claude-SearchBot", "Claude-User",
            "Google-Extended", "Applebot", "Applebot-Extended", "DuckAssistBot", "Amazonbot", "CCBot", "Bytespider"]
    with open(os.path.join(ROOT, "robots.txt"), "w") as f:
        f.write("".join(f"User-agent: {b}\nAllow: /\n\n" for b in bots) + f"Sitemap: {BASE_URL}sitemap.xml\n")
    # unique paths, preserve order
    seen = set()
    rows = []
    for p, m in PAGES:
        if p not in seen:
            seen.add(p)
            rows.append((p, m))
    with open(os.path.join(ROOT, "sitemap.xml"), "w") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for p, m in rows:
            f.write(f"<url><loc>{url(p)}</loc><lastmod>{m}</lastmod></url>\n")
        f.write("</urlset>\n")
    lines = [f"# {BRAND}", "",
             f"> {BRAND} ({DOMAIN}) lists the key fob battery, wiper parts, and bulb types printed in the owner's manual for specific model years, plus NHTSA recall campaigns for that model year. Checked {PUBLISHED_H}.",
             "",
             "Independent. Not affiliated with any car maker. Confirm parts on the vehicle and in the manual.",
             "",
             "## Guides",
             f"- [How to read a fitment chart]({url('/fitment/')})",
             f"- [Key fob battery]({url('/fitment/key-fob-battery/')})",
             f"- [Wiper blades]({url('/fitment/wiper-blades/')})",
             f"- [Headlight bulbs]({url('/fitment/headlight-bulbs/')})",
             f"- [Brake lights]({url('/fitment/brake-lights/')})",
             f"- [Turn signals]({url('/fitment/turn-signals/')})",
             f"- [Sources and methods]({url('/methodology/')})",
             "",
             "## Vehicles"]
    for v in VEHICLES:
        lines.append(f"- [{v['year']} {v['make']} {v['model']}]({url(vpath(v))})")
    with open(os.path.join(ROOT, "llms.txt"), "w") as f:
        f.write("\n".join(lines) + "\n")
    with open(os.path.join(ROOT, "_config.yml"), "w") as f:
        f.write("exclude: [README.md, LAUNCH-NOTES.md, _build, deploy.sh, indexnow.sh]\n")

def main():
    # reset sitemap accumulator if build() is called twice in one process
    global PAGES
    PAGES = []
    by_model = {}
    for v in VEHICLES:
        by_model.setdefault((v["make"], v["model"]), []).append(v)
    for group in by_model.values():
        group.sort(key=lambda x: x["year"])
    for v in VEHICLES:
        vehicle_page(v, by_model)
    hubs()
    fitment_pages()
    catalog = [{"make": v["make"], "model": v["model"], "year": v["year"], "url": vpath(v)} for v in VEHICLES]
    home(catalog)
    static_pages()
    not_found()
    graphics()
    extras(catalog)
    print(len(VEHICLES), "vehicles;", len(PAGES), "sitemap urls;", "NOINDEX" if NOINDEX else "LIVE")

if __name__ == "__main__":
    main()
