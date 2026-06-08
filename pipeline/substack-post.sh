#!/bin/bash
#
# Post a newsletter draft to Substack via API.
#
# Usage: ./substack-post.sh              # today's date
#        ./substack-post.sh 2026-06-02   # specific date
#
# Reads:   pipeline/output/<topic>/<date>/substack.html
# Effect:  creates a draft post on Substack (not published automatically)
# Prints:  draft edit URL on success
#
# Credentials loaded from (first found):
#   1. $SUBSTACK_SID / $SUBSTACK_PUB_HOST in environment
#   2. ~/daily-journal-platform/.env.local

set -euo pipefail

DIR="$(cd "$(dirname "$0")" && pwd)"
source "$DIR/_lib.sh"

DATE=$(parse_date_arg "$@")
init_day_dir
HTML_FILE="$DAY_DIR/substack.html"

echo ""
echo "=== Substack post: $DATE ==="
echo ""

if [[ ! -f "$HTML_FILE" ]]; then
  echo "  Error: $HTML_FILE not found. Run substack.sh first."
  exit 1
fi

# --- Load credentials ---
if [[ -z "${SUBSTACK_SID:-}" ]] || [[ -z "${SUBSTACK_PUB_HOST:-}" ]]; then
  ENV_FILE="$HOME/daily-journal-platform/.env.local"
  if [[ ! -f "$ENV_FILE" ]]; then
    echo "  Error: SUBSTACK_SID/SUBSTACK_PUB_HOST not set and $ENV_FILE not found."
    exit 1
  fi
  # shellcheck disable=SC2046
  export $(grep -E '^(SUBSTACK_SID|SUBSTACK_PUB_HOST)=' "$ENV_FILE" | xargs)
fi

if [[ -z "${SUBSTACK_SID:-}" ]] || [[ -z "${SUBSTACK_PUB_HOST:-}" ]]; then
  echo "  Error: SUBSTACK_SID or SUBSTACK_PUB_HOST missing from env."
  exit 1
fi

META_FILE="$DAY_DIR/paywall-meta.json"

echo "  Publication: $SUBSTACK_PUB_HOST"
echo "  Input:       $HTML_FILE"
[[ -f "$META_FILE" ]] && echo "  Paywall:     $META_FILE" || echo "  Paywall:     (none — run paywall-teaser.sh to add)"
echo ""

ARGS=("$HTML_FILE" "$SUBSTACK_SID" "$SUBSTACK_PUB_HOST")
[[ -f "$META_FILE" ]] && ARGS+=("$META_FILE")

python3 "$DIR/tools/substack_post.py" "${ARGS[@]}"

echo ""
echo "  Open in Substack to review before publishing."
echo ""
