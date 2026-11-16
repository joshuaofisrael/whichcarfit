# Which Car Fit (whichcarfit.com)

Key fob battery, wiper parts, bulb sizes, and NHTSA recalls by make, model, and year. Static site for GitHub Pages (branch `main`, folder `/`).

Joshua Israel Ventures LLC. Independent. Not affiliated with any car maker.

## Build

```
python3 _build/nhtsa_fetch.py
python3 _build/build.py
python3 _build/check.py
python3 _build/legal_gate.py check --no-queue
```

`NOINDEX = True` in `_build/config.py` is the single flag that puts a noindex meta on every page. `GA4_ID` stays empty until launch. Paths are root relative. Canonicals use `https://whichcarfit.com/`. `CNAME` contains `whichcarfit.com`.

The launch command (set `NOINDEX = False`, paste the GA4 Measurement ID, rebuild, check, legal gate, IndexNow) is in `LAUNCH-NOTES.md`. `./indexnow.sh` refuses to ping while the flag is on.

Facts come from the owner's manual linked on each year page and from NHTSA's public API. A figure that is not in the manual is left unstated. Do not copy one year's chart onto another year.
