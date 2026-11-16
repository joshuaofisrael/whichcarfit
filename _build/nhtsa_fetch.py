#!/usr/bin/env python3
"""Retrieve NHTSA recalls and complaint counts for every vehicle page.

Writes _build/nhtsa/<slug>.json. Complaint bodies are not stored.
Run from the repo root: python3 _build/nhtsa_fetch.py
"""
import json, os, sys, urllib.parse, urllib.request
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from config import PUBLISHED
from vehicles import VEHICLES

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "nhtsa")
os.makedirs(OUT, exist_ok=True)
UA = "WhichCarFit/1.0 (public NHTSA API; vehicle safety lookup)"

def slugify(s):
    import re
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")

def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=90) as r:
        return json.load(r)

def recalls(make, model, year):
    q = urllib.parse.urlencode({"make": make, "model": model, "modelYear": year})
    url = "https://api.nhtsa.gov/recalls/recallsByVehicle?" + q
    try:
        data = get(url)
    except Exception as e:
        return {"url": url, "error": str(getattr(e, "code", e)), "items": []}
    items = []
    for row in data.get("results") or []:
        items.append({
            "id": row.get("NHTSACampaignNumber") or "",
            "component": row.get("Component") or "",
            "date": row.get("ReportReceivedDate") or "",
            "park": bool(row.get("parkIt")),
        })
    # stable, newest campaign id last is fine; sort by id
    items.sort(key=lambda x: x["id"])
    return {"url": url, "count": data.get("Count", len(items)), "items": items}

def complaints(make, model, year):
    q = urllib.parse.urlencode({"make": make, "model": model, "modelYear": year})
    url = "https://api.nhtsa.gov/complaints/complaintsByVehicle?" + q
    try:
        data = get(url)
    except Exception as e:
        return {"url": url, "error": str(getattr(e, "code", e)), "count": None, "top": []}
    counts = {}
    for row in data.get("results") or []:
        raw = row.get("components") or row.get("Component") or ""
        for part in [p.strip() for p in str(raw).split(",") if p.strip()]:
            counts[part] = counts.get(part, 0) + 1
    top = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))[:5]
    return {"url": url, "count": data.get("Count", len(data.get("results") or [])), "top": top}

def main():
    for v in VEHICLES:
        key = f"{slugify(v['make'])}-{slugify(v['model'])}-{v['year']}"
        groups = []
        for make, model in v["nhtsa"]:
            print("fetch", v["year"], make, model, flush=True)
            groups.append({
                "make": make,
                "model": model,
                "recalls": recalls(make, model, v["year"]),
                "complaints": complaints(make, model, v["year"]),
            })
        doc = {"retrieved": PUBLISHED, "groups": groups}
        path = os.path.join(OUT, key + ".json")
        with open(path, "w") as f:
            json.dump(doc, f, indent=1)
        rc = sum((g["recalls"].get("count") or 0) for g in groups)
        print(" ", key, "recall rows", rc)
    print("wrote", len(VEHICLES), "files")

if __name__ == "__main__":
    main()
