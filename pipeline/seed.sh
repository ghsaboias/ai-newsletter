#!/bin/bash
#
# Add seed URLs for the next newsletter research
#
# Usage: ./seed.sh <url>                    # today's date
#        ./seed.sh 2026-03-28 <url>         # specific date
#        ./seed.sh <url1> <url2> ...        # multiple URLs
#

set -euo pipefail

source "$(cd "$(dirname "$0")" && pwd)/_lib.sh"

DATE=""
URLS=()

for arg in "$@"; do
  if [[ "$arg" =~ ^20[0-9]{2}-[0-9]{2}-[0-9]{2}$ ]]; then
    DATE="$arg"
  elif [[ "$arg" =~ ^https?:// ]]; then
    URLS+=("$arg")
  else
    echo "  Unknown argument: $arg"
    exit 1
  fi
done

if [[ -z "$DATE" ]]; then
  DATE=$(date +%Y-%m-%d)
fi

if [[ ${#URLS[@]} -eq 0 ]]; then
  echo "Usage: ./seed.sh [YYYY-MM-DD] <url> [url2] ..."
  exit 1
fi

init_day_dir
SEEDS_FILE="$DAY_DIR/seeds.md"

for url in "${URLS[@]}"; do
  echo "$url" >> "$SEEDS_FILE"
  echo "  + $url"
done

TOTAL=$(wc -l < "$SEEDS_FILE" | tr -d ' ')
echo "  Seeds: $TOTAL URLs in $SEEDS_FILE"
