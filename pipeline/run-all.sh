#!/bin/bash
#
# Full newsletter pipeline: Generate → Translate → Extract → Ingest
#
# Usage: ./run-all.sh              # today's date
#        ./run-all.sh 2026-02-24   # specific date
#        ./run-all.sh 2026-02-24 --limit-urls 5
#        ./run-all.sh 2026-02-24 --execute
#        ./run-all.sh 2026-02-24 --limit 3 --execute
#

set -euo pipefail

DIR="$(cd "$(dirname "$0")" && pwd)"

# --- Args ---
DATE=""
EXECUTE=false
LIMIT_URLS=""
INGEST_LIMIT=""
prev_arg=""

for arg in "$@"; do
  case "$arg" in
    --execute)    EXECUTE=true ;;
    --limit-urls) ;; # value handled below
    --limit)      ;; # value handled below
    20[0-9][0-9]-[0-9][0-9]-[0-9][0-9]) DATE="$arg" ;;
    test) DATE="test" ;;
    *)
      if [[ "$prev_arg" == "--limit-urls" ]]; then
        LIMIT_URLS="$arg"
      elif [[ "$prev_arg" == "--limit" ]]; then
        INGEST_LIMIT="$arg"
      fi
      ;;
  esac
  prev_arg="$arg"
done

# Default to today
if [[ -z "$DATE" ]]; then
  DATE=$(date +%Y-%m-%d)
fi

echo "=== Full Newsletter Pipeline: $DATE ==="

# --- Step 1: Generate ---
"$DIR/generate.sh" "$DATE"

# --- Step 2: Translate ---
"$DIR/translate.sh" "$DATE"

# --- Step 3: Extract ---
EXTRACT_ARGS=("$DATE")
[[ -n "$LIMIT_URLS" ]] && EXTRACT_ARGS+=("--limit-urls" "$LIMIT_URLS")

"$DIR/extract.sh" "${EXTRACT_ARGS[@]}"

# --- Step 4: Ingest ---
INGEST_ARGS=("$DATE")
[[ "$EXECUTE" == true ]] && INGEST_ARGS+=("--execute")
[[ -n "$INGEST_LIMIT" ]] && INGEST_ARGS+=("--limit" "$INGEST_LIMIT")
[[ -n "$LIMIT_URLS" ]] && INGEST_ARGS+=("--test")

"$DIR/ingest.sh" "${INGEST_ARGS[@]}"

# --- Step 5: Rewrite links ---
"$DIR/rewrite-links.sh" "$DATE"

# --- Step 6: Publish ---
"$DIR/publish.sh" "$DATE"
