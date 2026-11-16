#!/bin/bash
# Build, QA, and the legal gate. Does not push. Launch (indexable pages) is
# python3 _build/build.py after setting NOINDEX = False in _build/config.py.
set -e
cd "$(dirname "$0")"
python3 _build/nhtsa_fetch.py
python3 _build/build.py
python3 _build/check.py
python3 _build/legal_gate.py check --no-queue
echo "build ok"
