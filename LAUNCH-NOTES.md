# Which Car Fit launch notes

Status 16 Nov 2026: v1 built with noindex on every page. Domain file is `CNAME` (`whichcarfit.com`). GitHub Pages should serve the site from branch `main`, folder `/`.

The single switch is `NOINDEX` in `_build/config.py`. Leave it true until the domain answers on HTTPS. Then set it false, rebuild, push, and run `./indexnow.sh`.

## What v1 publishes

28 model year pages, not 80. Each one is a year whose owner's manual was opened on 16 Nov 2026. The lead table is transcribed from that book. NHTSA recalls and complaint counts are from the public API, retrieved the same day. Where the manual does not print an inch length or a bulb number, the page says so.

The sitemap has 72 URLs: those 28 year pages, make hubs, model hubs, the part hubs, and the legal pages. 404 is noindex and is not in the sitemap.

Year pages: 2018, 2020, and 2022 Ford F-150; 2020 and 2022 Ford Escape; 2023 Ford Ranger; 2020 Ford Fusion; 2020 Ford Mustang; 2020 Ford Expedition; 2019 and 2020 Ford Edge; 2021 Ford E-Series; 2021 Ford Police Interceptor Utility; 2020 Lincoln Nautilus; 2020, 2024, and 2026 Jeep Wrangler; 2023 Jeep Cherokee; 2025 Jeep Grand Cherokee; 2020, 2023, and 2026 Ram 1500; 2023 Dodge Durango; 2018 Honda Civic sedan; 2025 Honda CR-V; 2024 Toyota Grand Highlander; 2025 Toyota Corolla Hybrid; 2024 Toyota Corolla Cross Hybrid.

## Gaps

- Not every best selling model year has a page yet. General Motors, Nissan, Hyundai, Kia, Subaru, and Mazda books were not opened for this version because the PDF hosts blocked this environment or a year could not be tied to a specific manual.
- Ford often prints a Motorcraft wiper part number and does not print inches. Those pages do not convert the part number into a length.
- The 2026 Ram 1500 book we opened sends LED lamps to a dealer and does not print the halogen numbers used in earlier Ram books. Those numbers are not copied forward.
- Police Interceptor Utility has no NHTSA model name that the recalls API accepts. That page points to the VIN lookup and does not borrow Explorer campaigns.
- NHTSA files the Ford E-Series van as E-350 and E-450. The page shows both, under those names.
- IndexNow, Search Console, and Bing wait until the domain is live.
- No ads and no affiliate links. The ad disclosure says so.
