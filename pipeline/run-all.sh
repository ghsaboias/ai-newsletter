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
DJ_DIR="$HOME/daily-journal-platform"
LOOP_DIR="$DIR/output"

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
if [[ -n "$LIMIT_URLS" ]]; then
  SOURCES_FILE="$LOOP_DIR/$DATE.sources.test.json"
else
  SOURCES_FILE="$LOOP_DIR/$DATE.sources.json"
fi

if [[ ! -f "$SOURCES_FILE" ]]; then
  echo ""
  echo "Error: Sources file not found: $SOURCES_FILE"
  exit 1
fi

INGEST_ARGS=("$SOURCES_FILE")
[[ "$EXECUTE" == true ]] && INGEST_ARGS+=("--execute")
[[ -n "$INGEST_LIMIT" ]] && INGEST_ARGS+=("--limit" "$INGEST_LIMIT")

(cd "$DJ_DIR" && npx tsx scripts/ingest.ts "${INGEST_ARGS[@]}")

# --- Step 5: Rewrite links ---
"$DIR/rewrite-links.sh" "$DATE"

# --- Step 6: Publish ---
"$DIR/publish.sh" "$DATE"
