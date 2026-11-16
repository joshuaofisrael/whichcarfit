# Which Car Fit launch notes

Status 16 Nov 2026: v1 built with noindex on every page. Domain file is `CNAME` (`whichcarfit.com`). GitHub Pages should serve the site from branch `main`, folder `/`.

The committed default stays `NOINDEX = True` and `GA4_ID = ""` in `_build/config.py`. Changing `NOINDEX = True` to `NOINDEX = False` is the one-line launch switch. Paths stay root-relative. Canonicals stay `https://whichcarfit.com/`. The build rewrites `CNAME` (`whichcarfit.com`), `sitemap.xml` (every URL has `lastmod`), `robots.txt` (Googlebot, Bingbot, and the AI crawlers are allowed), `llms.txt`, and `15cffb11329a506a716afdc6f6099cae.txt` (IndexNow key). Do not put a secret in any of those files.

## Launch command

Do this only after whichcarfit.com answers on HTTPS. From the repo root:

1. Edit `_build/config.py`.
   - Set `NOINDEX = False` (the one-line switch).
   - Set `GA4_ID = "G-XXXXXXXXXX"` to the GA4 Measurement ID. Leave it empty and `python3 _build/check.py` exits 1 with `ga4-id-empty`. The same check exits 1 if any page is missing the Cloudflare Web Analytics beacon or the GA4 loader (`https://www.googletagmanager.com/gtag/js?id=`).
2. Rebuild, then require 0 issues and 0 holds:

```bash
python3 _build/build.py
python3 _build/check.py
python3 _build/legal_gate.py check --no-queue
./indexnow.sh
```

`check.py` prints `issues 0`. `legal_gate.py` prints `0 HOLD_REVIEW`. `./indexnow.sh` does nothing while `NOINDEX = True`.

The launch build removes the noindex meta (404 stays noindex), puts the Cloudflare beacon on every page, and loads Google Analytics 4 only after Accept on the consent banner. Consent Mode v2 defaults are denied. Cookie settings in the footer reopens the banner. The privacy page then names Google Analytics 4 and Cloudflare Web Analytics.

Preview rebuild, with both flags left as committed:

```bash
python3 _build/build.py
python3 _build/check.py
python3 _build/legal_gate.py check --no-queue
```

## What is published

74 model year pages. Each one is a year whose owner's manual was opened. The lead table is transcribed from that book. NHTSA recalls and complaint counts are from the public API. Where the manual does not print an inch length or a bulb number, the page says so.

The sitemap lists those year pages, make hubs, model hubs (with a year comparison table), part hubs, and the legal pages. 404 is noindex and is not in the sitemap. NOINDEX stays on until the domain is live.

Added after the first 28: Chevrolet Silverado 1500 2020 and 2021, Equinox 2020 to 2022, Malibu 2020 to 2022, Tahoe 2020 to 2022; GMC Sierra 1500 2020 and 2021; Nissan Rogue 2019 to 2025, Altima 2018 to 2025, Sentra 2020 to 2025; Hyundai Tucson 2020 and 2021, Elantra 2020, 2022, and 2023, Santa Fe 2020, 2022, and 2023; Mazda CX-5 2019 to 2022 (the model year is the edition code printed in the book when Mazda's folder year differs).

## Gaps

- Not every best selling model year has a page yet. General Motors, Nissan, Hyundai, Kia, Subaru, and Mazda books were not opened for this version because the PDF hosts blocked this environment or a year could not be tied to a specific manual.
- Ford often prints a Motorcraft wiper part number and does not print inches. Those pages do not convert the part number into a length.
- The 2026 Ram 1500 book we opened sends LED lamps to a dealer and does not print the halogen numbers used in earlier Ram books. Those numbers are not copied forward.
- Police Interceptor Utility has no NHTSA model name that the recalls API accepts. That page points to the VIN lookup and does not borrow Explorer campaigns.
- NHTSA files the Ford E-Series van as E-350 and E-450. The page shows both, under those names.
- IndexNow, Search Console, and Bing wait until the domain is live.
- No ads and no affiliate links. The ad disclosure says so.
