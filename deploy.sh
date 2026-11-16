#!/bin/bash
# Build, QA, and the legal gate for the committed flags. Does not push.
# Launch (NOINDEX = False and a real GA4_ID) is documented in LAUNCH-NOTES.md.
set -e
cd "$(dirname "$0")"
python3 _build/nhtsa_fetch.py
python3 _build/build.py
python3 _build/check.py
python3 _build/legal_gate.py check --no-queue
echo "build ok"
