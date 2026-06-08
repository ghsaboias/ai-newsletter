#!/bin/bash
# Sync the newsletter's "Recomendações de hoje" video picks into a master
# Markdown archive, then commit & push.
#
# Source of truth is the *published* Substack post (recommendations are added by
# hand in the editor, so they only exist there) fetched via `sstats post`.
#
# Idempotent: an edition already present in the archive (matched by its
# `## YYYY-MM-DD` header) is skipped, so re-running is safe and weekends — which
# have no edition — simply append nothing. A late-published edition is picked up
# by a later run because we always rescan the recent window.
#
# Usage:
#   sync-recommendations.sh            # scan the last 12 editions (daily cron)
#   sync-recommendations.sh all        # full backfill (scan up to 100 editions)
#   sync-recommendations.sh 30         # scan the last 30 editions
#
# The repo it commits to is derived from this script's own location, so on the
# Pi it runs from a DEDICATED clone (~/recs-archive) kept separate from the
# daily-draft clone (~/ai-newsletter), whose cron auto-commits pipeline output
# locally and must never be pushed.
#
# Cron (noon BRT, Pi is America/Sao_Paulo):
#   0 12 * * * bash ~/recs-archive/recommendations/sync-recommendations.sh >> ~/logs/newsletter-recs.log 2>&1

set -uo pipefail

# Cron has a minimal PATH; make sstats / jq / python3 / git / curl reachable.
export PATH="$HOME/.local/bin:/usr/local/bin:/usr/bin:/bin:$HOME/.npm-global/bin:$PATH"

# Repo root = parent of this script's directory (recommendations/..).
REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DJ="$HOME/daily-journal-platform"            # holds .env.local for sstats
ARCHIVE="$REPO/recommendations/RECOMMENDATIONS.md"
EXTRACT="$REPO/recommendations/extract_recs.py"

# How many recent editions to scan.
case "${1:-}" in
    all)         LIMIT=100 ;;
    ''|*[!0-9]*) LIMIT=12 ;;
    *)           LIMIT="$1" ;;
esac

log() { echo "[$(date '+%Y-%m-%d %H:%M:%S %z')] $*"; }

command -v sstats  >/dev/null || { log "ERROR: sstats not found on PATH"; exit 1; }
command -v jq      >/dev/null || { log "ERROR: jq not found on PATH"; exit 1; }
command -v python3 >/dev/null || { log "ERROR: python3 not found on PATH"; exit 1; }
[[ -f "$EXTRACT" ]] || { log "ERROR: extractor missing at $EXTRACT"; exit 1; }

# Pull first so we extend the latest archive. This clone only ever commits the
# archive (and immediately pushes), so it never diverges — a fast-forward is
# always expected.
if ! git -C "$REPO" pull --ff-only --quiet; then
    log "WARN: git pull --ff-only failed; continuing with local copy"
fi

# Seed the archive on first run.
if [[ ! -f "$ARCHIVE" ]]; then
    cat > "$ARCHIVE" <<'HEADER'
# Recomendações da Newsletter

Arquivo das recomendações (vídeos e entrevistas) publicadas na newsletter de
AI/Tech. Cada seção é uma edição; sem edição nos fins de semana.

Atualizado automaticamente ao meio-dia (BRT) por
`recommendations/sync-recommendations.sh` (cron na Pi). Fonte: post publicado no
Substack, via `sstats post`.
HEADER
    log "Created $ARCHIVE"
fi

# List recent editions as "YYYY-MM-DD<TAB>post_id", oldest first.
editions=$(cd "$DJ" && sstats emails -n "$LIMIT" 2>/dev/null \
    | jq -r '.rows[] | select(.post_id != null) | [.post_date[0:10], (.post_id|tostring)] | @tsv' \
    | sort)

if [[ -z "$editions" ]]; then
    log "ERROR: no editions returned from sstats emails"
    exit 1
fi

added=0
added_dates=""
while IFS=$'\t' read -r date id; do
    [[ -z "$date" || -z "$id" ]] && continue
    grep -q "^## ${date}\$" "$ARCHIVE" && continue   # already recorded

    html=$(cd "$DJ" && sstats post "$id" --html 2>/dev/null)
    sleep 3                                           # be gentle with Substack
    [[ -z "$html" ]] && { log "WARN: empty HTML for $date ($id)"; continue; }

    block=$(printf '%s' "$html" | python3 "$EXTRACT" --date "$date")
    [[ -z "$block" ]] && { log "skip $date — no recommendations section"; continue; }

    printf '\n%s\n' "$block" >> "$ARCHIVE"
    added=$((added + 1))
    added_dates="${added_dates}${date} "
    log "added $date ($(printf '%s' "$block" | grep -c '^https://'))  recs"
done <<< "$editions"

if [[ "$added" -eq 0 ]]; then
    log "no new editions to add"
    exit 0
fi

# Commit & push only the archive (leave any other working-tree files untouched).
git -C "$REPO" add "$ARCHIVE"
if git -C "$REPO" diff --cached --quiet; then
    log "archive unchanged after staging; nothing to commit"
    exit 0
fi
git -C "$REPO" commit --no-gpg-sign -q -m "recs: sync ${added} edition(s) [${added_dates% }]"
if git -C "$REPO" push --quiet; then
    log "committed & pushed ${added} edition(s)"
else
    log "WARN: git push failed; will retry next run"
fi
