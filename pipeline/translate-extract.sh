#!/bin/bash
#
# Steps 2+3: Translate EN→PT-BR, then extract sources
#
# Usage: ./translate-extract.sh 2026-02-24
#        ./translate-extract.sh 2026-02-24 --limit-urls 5
#        ./translate-extract.sh test --limit-urls 5
#

set -euo pipefail

DIR="$(cd "$(dirname "$0")" && pwd)"

# Separate translate args from extract args
DATE=""
LIMIT_URLS=""
prev_arg=""

for arg in "$@"; do
  case "$arg" in
    --limit-urls) ;; # value handled below
    20[0-9][0-9]-[0-9][0-9]-[0-9][0-9]) DATE="$arg" ;;
    test) DATE="test" ;;
    *)
      if [[ "$prev_arg" == "--limit-urls" ]]; then
        LIMIT_URLS="$arg"
      fi
      ;;
  esac
  prev_arg="$arg"
done

if [[ -z "$DATE" ]]; then
  echo "Usage: $0 YYYY-MM-DD [--limit-urls N]"
  exit 1
fi

"$DIR/translate.sh" "$DATE"

EXTRACT_ARGS=("$DATE")
[[ -n "$LIMIT_URLS" ]] && EXTRACT_ARGS+=("--limit-urls" "$LIMIT_URLS")

"$DIR/extract.sh" "${EXTRACT_ARGS[@]}"
