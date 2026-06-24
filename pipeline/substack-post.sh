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
BANNER_FILE="${TOPIC_PAYWALL_BANNER:-$TOPIC_DIR/paywall-banner.json}"

echo "  Publication: $SUBSTACK_PUB_HOST"
echo "  Input:       $HTML_FILE"
[[ -f "$META_FILE" ]] && echo "  Paywall:     $META_FILE" || echo "  Paywall:     (none — run paywall-teaser.sh to add)"
if [[ -f "$META_FILE" ]]; then
  [[ -f "$BANNER_FILE" ]] && echo "  Banner:      $BANNER_FILE" || echo "  Banner:      (none — no $BANNER_FILE)"
fi
echo ""

# Banner rides with the paywall (between teaser and cut), so only pass it when
# a paywall meta exists — substack_post.py reads it as the 5th positional arg.
ARGS=("$HTML_FILE" "$SUBSTACK_SID" "$SUBSTACK_PUB_HOST")
if [[ -f "$META_FILE" ]]; then
  ARGS+=("$META_FILE")
  [[ -f "$BANNER_FILE" ]] && ARGS+=("$BANNER_FILE")
fi

# If draft.sh already created the source-linked original draft, update THAT one
# in place (its links become DJ links here) instead of spawning a new draft.
ORIG_ID_FILE="$DAY_DIR/.substack-orig-id"
if [[ -f "$ORIG_ID_FILE" ]] && [[ -s "$ORIG_ID_FILE" ]]; then
  ARGS+=(--draft-id "$(cat "$ORIG_ID_FILE")" --id-out "$ORIG_ID_FILE")
  echo "  Updating draft.sh draft $(cat "$ORIG_ID_FILE") (source links → DJ links)"
  echo ""
fi

python3 "$DIR/tools/substack_post.py" "${ARGS[@]}"

echo ""
echo "  Open in Substack to review before publishing."
echo ""
