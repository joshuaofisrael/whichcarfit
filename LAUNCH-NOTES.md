# Which Car Fit launch notes

Status 16 Nov 2026: v1 built with noindex on every page. Domain file is `CNAME` (`whichcarfit.com`). GitHub Pages should serve the site from branch `main`, folder `/`.

The single switch is `NOINDEX` in `_build/config.py`. Leave it true until the domain answers on HTTPS. Then set it false, rebuild, push, and run `./indexnow.sh`.

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
