#!/bin/bash
#
# Step 6: Publish newsletter to ai-newsletter Jekyll site
#
# Usage: ./publish.sh 2026-02-24
#        ./publish.sh test
#        ./publish.sh 2026-02-24 --dry-run
#
# Reads .final.md (with DJ links) if available, otherwise .pt.md.
# Adds Jekyll frontmatter, copies to posts/_posts, commits and pushes.
#

set -euo pipefail

source "$(cd "$(dirname "$0")" && pwd)/_lib.sh"

DATE=$(parse_date_arg "$@")
DRY_RUN=false
for arg in "$@"; do
  [[ "$arg" == "--dry-run" ]] && DRY_RUN=true
done

NEWSLETTER_DIR="$(cd "$DIR/.." && pwd)"
POSTS_DIR="$NEWSLETTER_DIR/posts/_posts"

# Prefer .final.md (has DJ links), fall back to .pt.md
FINAL_FILE="$LOOP_DIR/$DATE.final.md"
PT_FILE="$LOOP_DIR/$DATE.pt.md"

if [[ -f "$FINAL_FILE" ]]; then
  SOURCE_FILE="$FINAL_FILE"
elif [[ -f "$PT_FILE" ]]; then
  echo "  ⚠ No .final.md found, using .pt.md (original links)"
  SOURCE_FILE="$PT_FILE"
else
  echo "Error: Neither $FINAL_FILE nor $PT_FILE found"
  exit 1
fi

echo ""
echo "=== Publish: $DATE ==="
echo ""
echo "  Source: $SOURCE_FILE"

# --- Extract title from frontmatter ---
TITLE=$(sed -n 's/^title: *"\(.*\)"/\1/p' "$SOURCE_FILE" | head -1)
if [[ -z "$TITLE" ]]; then
  # Try without quotes
  TITLE=$(sed -n 's/^title: *//p' "$SOURCE_FILE" | head -1)
fi

if [[ -z "$TITLE" ]]; then
  echo "Error: Could not extract title from frontmatter"
  exit 1
fi

echo "  Title:  $TITLE"

# --- Generate Jekyll filename ---
# Slugify: lowercase, replace spaces/special chars with hyphens, trim
SLUG=$(echo "$TITLE" | tr '[:upper:]' '[:lower:]' | \
  sed 's/[àáâã]/a/g; s/[éê]/e/g; s/[íî]/i/g; s/[óôõ]/o/g; s/[úû]/u/g; s/ç/c/g' | \
  sed 's/[^a-z0-9]/-/g' | sed 's/--*/-/g' | sed 's/^-//; s/-$//')

POST_FILE="$POSTS_DIR/$DATE-$SLUG.md"
echo "  Output: $POST_FILE"

# --- Build Jekyll post ---
# Strip original frontmatter, prepend Jekyll frontmatter
BODY=$(awk 'BEGIN{n=0} /^---$/{n++; next} n>=2{print}' "$SOURCE_FILE")

JEKYLL_POST="---
layout: post
date: $DATE
title: \"$TITLE\"
---

$BODY"

if [[ "$DRY_RUN" == true ]]; then
  echo ""
  echo "  --- Preview (first 10 lines) ---"
  echo "$JEKYLL_POST" | head -10
  echo "  ..."
  echo ""
  echo "  (dry run — nothing written)"
  exit 0
fi

# --- Write and push ---
echo "$JEKYLL_POST" > "$POST_FILE"
echo ""
echo "  ✓ Written to $POST_FILE"

cd "$NEWSLETTER_DIR"
git add "$POST_FILE"
git commit -m "Add newsletter $DATE"
git push

echo ""
echo "  ✓ Pushed to GitHub — will auto-deploy to Pages"
