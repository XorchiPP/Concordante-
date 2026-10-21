#!/usr/bin/env sh
set -eu
cd "$(dirname "$0")"
python3 verify_boundary_gauge.py
python3 audit/verify_boundary_gauge.py
sha256sum -c SHA256SUMS
