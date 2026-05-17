#!/bin/bash
set -e

echo "=== Building AI Knowledge Base static site ==="

# Install dependencies
pip install -e . 2>/dev/null

# Generate data.json from knowledge markdown
python3 scripts/build_static.py ./knowledge ./site/data

echo "=== Build complete ==="
