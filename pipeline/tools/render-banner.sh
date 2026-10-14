#!/usr/bin/env bash
# render-banner.sh <banner.html> <out.png>
#   Renders the #capture element of a partner-insertion banner to PNG at 2×.
#   The banner's #capture is 636×156 CSS px, so the PNG comes out 1272×312, the
#   size of every insertion banner so far. Chromium headless with a throwaway
#   profile, on the Pi (chromium) and on the Mac (Google Chrome).
set -euo pipefail

HTML="$(cd "$(dirname "${1:?uso: render-banner.sh <banner.html> <out.png>}")" && pwd)/$(basename "$1")"
OUT="${2:?uso: render-banner.sh <banner.html> <out.png>}"
REPO="$(cd "$(dirname "$0")/../.." && pwd)"

if [ -z "${CHROMIUM_BIN:-}" ]; then
  for b in chromium chromium-browser "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"; do
    if command -v "$b" >/dev/null 2>&1 || [ -x "$b" ]; then CHROMIUM_BIN="$b"; break; fi
  done
fi
[ -n "${CHROMIUM_BIN:-}" ] || { echo "ERRO: sem chromium/chrome"; exit 1; }
export CHROMIUM_BIN

exec node "$REPO/.claude/skills/chart-post/headless-render.js" render "$HTML" "$OUT"
