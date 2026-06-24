#!/bin/bash
#
# Merge per-cluster research JSON files into a single research.json.
#
# Extracted verbatim from research.sh so the script path and the agent
# orchestration path share one merge. Dedupes stories by id, counts stories
# and sources.
#
# Usage: merge-research.sh <date> <out.json> <partial.json> [partial.json ...]
#

set -euo pipefail

DATE="${1:?usage: merge-research.sh <date> <out.json> <partial.json> [...]}"
OUT="${2:?missing out.json}"
shift 2

if [[ $# -eq 0 ]]; then
  echo "Error: no partial files given" >&2
  exit 1
fi

jq -s '{
  date: "'"$DATE"'",
  stories: [.[].stories[] | {id, headline, key_facts, sources, category, entities}] | unique_by(.id),
} | .story_count = (.stories | length)
  | .source_count = ([.stories[].sources | length] | add)' \
  "$@" > "$OUT"

echo "merged $# file(s) → $OUT ($(jq '.story_count' "$OUT") stories, $(jq '.source_count' "$OUT") sources)"
