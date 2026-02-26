#!/bin/bash
#
# Step 4: Ingest extracted sources into Daily Journal database
#
# Wrapper around daily-journal-platform/scripts/ingest.ts
#
# Usage: ./ingest.sh 2026-02-24
#        ./ingest.sh 2026-02-24 --execute
#        ./ingest.sh 2026-02-24 --limit 3 --execute
#        ./ingest.sh 2026-02-24 --test   # uses .sources.test.json
#        ./ingest.sh test                # also uses .sources.test.json
#

set -euo pipefail

DIR="$(cd "$(dirname "$0")" && pwd)"
DJ_DIR="$HOME/daily-journal-platform"
LOOP_DIR="$DIR/output"

DATE=""
EXECUTE=false
TEST=false
LIMIT=""
prev_arg=""

for arg in "$@"; do
  case "$arg" in
    --execute) EXECUTE=true ;;
    --test)    TEST=true ;;
    --limit)   ;; # value handled below
    20[0-9][0-9]-[0-9][0-9]-[0-9][0-9]) DATE="$arg" ;;
    test) DATE="test"; TEST=true ;;
    *)
      if [[ "$prev_arg" == "--limit" ]]; then
        LIMIT="$arg"
      fi
      ;;
  esac
  prev_arg="$arg"
done

if [[ -z "$DATE" ]]; then
  DATE=$(date +%Y-%m-%d)
fi

# Pick sources file — .test.json if --test or DATE is "test"
if [[ "$TEST" == true ]]; then
  SOURCES_FILE="$LOOP_DIR/$DATE.sources.test.json"
else
  SOURCES_FILE="$LOOP_DIR/$DATE.sources.json"
fi

if [[ ! -f "$SOURCES_FILE" ]]; then
  echo "Error: Sources file not found: $SOURCES_FILE"
  exit 1
fi

INGEST_ARGS=("$SOURCES_FILE")
[[ "$EXECUTE" == true ]] && INGEST_ARGS+=("--execute")
[[ -n "$LIMIT" ]] && INGEST_ARGS+=("--limit" "$LIMIT")

(cd "$DJ_DIR" && npx tsx scripts/ingest.ts "${INGEST_ARGS[@]}")
