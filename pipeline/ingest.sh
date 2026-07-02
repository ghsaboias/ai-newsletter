#!/bin/bash
#
# Step 4: Ingest extracted sources into Daily Journal database
#
# Wrapper around daily-journal-platform/scripts/ingest.ts
#
# Usage: ./ingest.sh 2026-02-24
#        ./ingest.sh 2026-02-24 --propose   # write cluster-candidates.json (no DB writes)
#        ./ingest.sh 2026-02-24 --execute   # apply cluster-decisions.json (if present) + write
#        ./ingest.sh 2026-02-24 --limit 3 --execute
#        ./ingest.sh 2026-02-24 --test   # uses sources.test.json
#        ./ingest.sh test                # also uses sources.test.json
#
# Clustering: --propose finds, per entity, the top existing-news candidates it might
# belong to (so the newsletter can reuse that news's image + avoid crowding the homepage)
# and writes cluster-candidates.json. A human/Claude picks the real matches into
# cluster-decisions.json. --execute then attaches to the chosen news, or creates as before.
#

set -euo pipefail

source "$(cd "$(dirname "$0")" && pwd)/_lib.sh"

DATE=""
EXECUTE=false
PROPOSE=false
TEST=false
LIMIT=""
prev_arg=""

for arg in "$@"; do
  case "$arg" in
    --execute) EXECUTE=true ;;
    --propose) PROPOSE=true ;;
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

init_day_dir

# Pick sources file — sources.test.json if --test or DATE is "test"
if [[ "$TEST" == true ]]; then
  SOURCES_FILE="$DAY_DIR/sources.test.json"
else
  SOURCES_FILE="$DAY_DIR/sources.json"
fi

if [[ ! -f "$SOURCES_FILE" ]]; then
  echo "Error: Sources file not found: $SOURCES_FILE"
  exit 1
fi

INGEST_ARGS=("$SOURCES_FILE")
[[ "$EXECUTE" == true ]] && INGEST_ARGS+=("--execute")
[[ "$PROPOSE" == true ]] && INGEST_ARGS+=("--propose")
[[ -n "$LIMIT" ]] && INGEST_ARGS+=("--limit" "$LIMIT")

(cd "$DJ_DIR" && npx tsx scripts/ingest.ts "${INGEST_ARGS[@]}")

revalidate_news_paths() {
  local links_file="$1"
  local secret="${CRON_SECRET:-}"
  local env_file line curl_bin path body code failures=0 count=0

  if [[ -z "$secret" ]]; then
    for env_file in "$DJ_DIR/.env.local" "$DJ_DIR/.env.vercel" "$DJ_DIR/.env.prod.tmp"; do
      [[ -f "$env_file" ]] || continue
      line=$(grep -m1 '^CRON_SECRET=' "$env_file" || true)
      [[ -n "$line" ]] || continue
      secret="${line#CRON_SECRET=}"
      secret="${secret%\"}"
      secret="${secret#\"}"
      secret="${secret%\'}"
      secret="${secret#\'}"
      break
    done
  fi

  if [[ -z "$secret" ]]; then
    echo "Error: CRON_SECRET not found; cannot revalidate Daily Journal news pages"
    return 1
  fi

  curl_bin=$(command -v curl || true)
  if [[ -z "$curl_bin" ]]; then
    echo "Error: curl not found; cannot revalidate Daily Journal news pages"
    return 1
  fi

  while IFS= read -r path; do
    [[ -n "$path" ]] || continue
    body=$(printf '{"path":"%s"}' "$path")
    code=$("$curl_bin" -sS -o /dev/null -w '%{http_code}' \
      -X POST 'https://dailyjournal.news/api/revalidate' \
      -H "Authorization: Bearer $secret" \
      -H 'Content-Type: application/json' \
      -d "$body")
    count=$((count + 1))
    if [[ "$code" == 2* ]]; then
      echo "  revalidated $path"
    else
      echo "  revalidate failed ($code): $path"
      failures=$((failures + 1))
    fi
  done < <(
    jq -r 'to_entries[].value' "$links_file" \
      | sed 's#^https://dailyjournal\.news##' \
      | grep '^/news/' \
      | sort -u
  )

  if [[ "$count" -eq 0 ]]; then
    echo "Error: no Daily Journal news paths found in $links_file"
    return 1
  fi

  if [[ "$failures" -gt 0 ]]; then
    echo "Error: $failures Daily Journal revalidation request(s) failed"
    return 1
  fi

  echo "OK revalidate: $count DJ news path(s)"
}

if [[ "$EXECUTE" == true && "$PROPOSE" == false && "$TEST" == false ]]; then
  LINKS_FILE="$DAY_DIR/links.json"
  if [[ -s "$LINKS_FILE" ]]; then
    revalidate_news_paths "$LINKS_FILE"
  else
    echo "Error: links.json missing/empty; cannot revalidate Daily Journal news pages"
    exit 1
  fi
fi
