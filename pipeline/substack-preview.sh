#!/bin/bash
#
# Post a markdown file to Substack as a draft (create-or-update in place).
#
# Used by the newsletter-draft skill to publish the edition as a Substack draft
# with their ORIGINAL source links. The draft id is persisted per-suffix so
# re-runs update the same draft (stable URL) instead of spawning duplicates —
# and finalize.sh later updates the same "orig" draft with the DJ links.
#
# Usage: ./substack-preview.sh <date> <md_file> <suffix> [label] [callout_heading]
#   <suffix>          short tag: drives .substack-<suffix>-id and substack-<suffix>.json
#   <callout_heading> if set, wrap that section (e.g. "Leia também") in a callout box
#
# Credentials: $SUBSTACK_SID / $SUBSTACK_PUB_HOST, else ~/daily-journal-platform/.env.local
#

set -euo pipefail

source "$(cd "$(dirname "$0")" && pwd)/_lib.sh"

# Positional: <date> <md_file> <suffix> [label] [callout_heading]
# Optional flags (anywhere): --paywall-meta <file>, --paywall-after-grandes
POS=()
PAYWALL_META=""
PAYWALL_AFTER_GRANDES=false
while [[ $# -gt 0 ]]; do
  case "$1" in
    --paywall-meta)          PAYWALL_META="$2"; shift 2 ;;
    --paywall-after-grandes) PAYWALL_AFTER_GRANDES=true; shift ;;
    *)                       POS+=("$1"); shift ;;
  esac
done

DATE="${POS[0]:?usage: substack-preview.sh <date> <md_file> <suffix> [label] [callout]}"
MD_FILE="${POS[1]:?missing md_file}"
SUFFIX="${POS[2]:?missing suffix}"
LABEL="${POS[3]:-$SUFFIX}"
CALLOUT_HEADING="${POS[4]:-}"

init_day_dir

echo ""
echo "=== Substack preview ($LABEL): $DATE ==="
echo ""

if [[ ! -f "$MD_FILE" ]]; then
  echo "  Error: $MD_FILE not found."
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

# --- Markdown → HTML (same converter the substack step uses) ---
HTML_FILE="$DAY_DIR/.substack-${SUFFIX}.html"
pandoc "$MD_FILE" --from markdown-tex_math_dollars --to html -o "$HTML_FILE"

# --- Post (create or update in place) ---
ID_FILE="$DAY_DIR/.substack-${SUFFIX}-id"
# paywall meta is a positional arg to substack_post.py (4th), so it comes first
ARGS=("$HTML_FILE" "$SUBSTACK_SID" "$SUBSTACK_PUB_HOST")
[[ -n "$PAYWALL_META" ]] && [[ -f "$PAYWALL_META" ]] && ARGS+=("$PAYWALL_META")
ARGS+=(--id-out "$ID_FILE")
[[ -n "$CALLOUT_HEADING" ]] && ARGS+=(--callout-heading "$CALLOUT_HEADING")
[[ "$PAYWALL_AFTER_GRANDES" == true ]] && ARGS+=(--paywall-after-grandes)
if [[ -f "$ID_FILE" ]] && [[ -s "$ID_FILE" ]]; then
  ARGS+=(--draft-id "$(cat "$ID_FILE")")
  echo "  Updating existing draft $(cat "$ID_FILE")"
else
  echo "  Creating new draft"
fi

python3 "$DIR/tools/substack_post.py" "${ARGS[@]}"

# --- Record url for the draft.sh summary ---
if [[ -f "$ID_FILE" ]] && [[ -s "$ID_FILE" ]]; then
  DRAFT_ID="$(cat "$ID_FILE")"
  URL="https://${SUBSTACK_PUB_HOST}/publish/post/${DRAFT_ID}"
  printf '{"id":"%s","url":"%s","label":"%s"}\n' "$DRAFT_ID" "$URL" "$LABEL" \
    > "$DAY_DIR/substack-${SUFFIX}.json"
  echo ""
  echo "  $LABEL → $URL"
fi
