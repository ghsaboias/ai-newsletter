#!/bin/bash
# Sync the newsletter's "Recomendações de hoje" video picks into a master
# Markdown archive, then commit & push.
#
# Source of truth is the *published* Substack post: recommendations are finalized
# by hand in the editor, so the generated recs.json is only a proposal. The
# archive is a pure projection of the published posts, produced by
# `sync-recommendations.py` (fetch via `sstats post`, extract via extract_recs).
#
# NOT append-only: each run re-fetches a recent WINDOW of editions and UPSERTS
# their sections from the current published HTML, so a recommendation added or
# changed on a post *after* the first sync is picked up on a later run. Nothing
# freezes after first sight. Re-running is safe: unchanged editions serialize
# byte-identically, so weekends (no edition) append nothing and produce no diff.
#
# Usage:
#   sync-recommendations.sh            # upsert the recent window (daily cron)
#   sync-recommendations.sh all        # full rebuild of the whole archive
#   sync-recommendations.sh 30         # upsert the last 30 editions
#
# The repo it commits to is derived from this script's own location. On the Pi
# it runs from ~/ai-newsletter, a clean clone kept in sync with origin.
#
# Cron (noon BRT, Pi is America/Sao_Paulo):
#   0 12 * * * bash ~/ai-newsletter/recommendations/sync-recommendations.sh >> ~/logs/newsletter-recs.log 2>&1

set -uo pipefail

# Cron has a minimal PATH; make sstats / python3 / git reachable.
export PATH="$HOME/.local/bin:/usr/local/bin:/usr/bin:/bin:$HOME/.npm-global/bin:$PATH"

# Repo root = parent of this script's directory (recommendations/..).
REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ARCHIVE="$REPO/recommendations/RECOMMENDATIONS.md"
PY="$REPO/recommendations/sync-recommendations.py"

# Translate the legacy arg into sync-recommendations.py flags.
case "${1:-}" in
    all)         PYARGS=(--rebuild --max 400) ;;
    ''|*[!0-9]*) PYARGS=(--window 14) ;;   # daily default
    *)           PYARGS=(--window "$1") ;;
esac

log() { echo "[$(date '+%Y-%m-%d %H:%M:%S %z')] $*"; }

command -v sstats  >/dev/null || { log "ERROR: sstats not found on PATH"; exit 1; }
command -v python3 >/dev/null || { log "ERROR: python3 not found on PATH"; exit 1; }
[[ -f "$PY" ]] || { log "ERROR: sync-recommendations.py missing at $PY"; exit 1; }

# Pull first so we extend the latest archive. This clone only ever commits the
# archive (and immediately pushes), so a fast-forward is always expected.
if ! git -C "$REPO" pull --ff-only --quiet; then
    log "WARN: git pull --ff-only failed; continuing with local copy"
fi

# Run the upsert/rebuild. Its human log goes to stderr (flows to the cron log);
# the space-separated list of changed dates is the only thing on stdout.
changed="$(python3 "$PY" "${PYARGS[@]}" --archive "$ARCHIVE")" || {
    log "ERROR: sync-recommendations.py failed"
    exit 1
}
changed="$(printf '%s' "$changed" | tr -s ' ' | sed 's/^ *//; s/ *$//')"

# Commit & push only the archive (leave any other working-tree files untouched).
git -C "$REPO" add "$ARCHIVE"
if git -C "$REPO" diff --cached --quiet; then
    log "archive unchanged; nothing to commit"
    exit 0
fi

count=$(printf '%s' "$changed" | wc -w | tr -d ' ')
git -C "$REPO" commit --no-gpg-sign -q -m "recs: sync ${count} edition(s) [${changed}]"
if git -C "$REPO" push --quiet; then
    log "committed & pushed ${count} edition(s): ${changed}"
else
    log "WARN: git push failed; will retry next run"
fi
