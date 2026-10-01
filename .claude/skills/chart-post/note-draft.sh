#!/usr/bin/env bash
# note-draft.sh <slug> [--id DRAFT_ID]
#   → salva posts/chart-<slug>.md + posts/chart-<slug>.png como RASCUNHO de Note no
#     Substack (via `sstats note-draft`). NÃO publica: o rascunho fica no composer de
#     Notes > Drafts, e o Gui posta de lá.
#   --id DRAFT_ID  substitui um rascunho existente (depois de editar a prosa/o chart)
#                  em vez de criar outro.
#
# Texto do Note = o corpo do .md depois do `---`, com a última linha no formato dos
# Notes publicados: "... na edição completa. <url>" (a URL vira link e o card do post
# entra como attachment). Recusa a rodar se o link ainda for o placeholder /p/<id>.
set -euo pipefail

SLUG="${1:?uso: note-draft.sh <slug> [--id DRAFT_ID]}"; shift
REPO="$(cd "$(dirname "$0")/../../.." && pwd)"
MD="$REPO/posts/chart-$SLUG.md"
PNG="$REPO/posts/chart-$SLUG.png"
test -f "$MD"  || { echo "ERRO: sem prosa em $MD"; exit 1; }
test -f "$PNG" || { echo "ERRO: sem png em $PNG (rode render.sh $SLUG)"; exit 1; }

TXT="$(mktemp)"; trap 'rm -f "$TXT"' EXIT
URL="$(python3 - "$MD" "$TXT" <<'PY'
import re, sys
body = open(sys.argv[1], encoding="utf-8").read().split("\n---\n", 1)[1].strip()
m = re.search(r'\[edição completa\]\((https?://[^)\s]+)\):?\s*$', body)
if not m:
    sys.exit("ERRO: o .md não termina com o link [edição completa](url)")
url = m.group(1)
if re.search(r'/p/\d+$', url) or '/publish/' in url:
    sys.exit(f"ERRO: link da edição ainda não é a URL pública canônica: {url}")
body = body[:m.start()] + "edição completa. " + url
open(sys.argv[2], "w", encoding="utf-8").write(body + "\n")
print(url)
PY
)"

sstats note-draft "$TXT" --image "$PNG" --link "$URL" "$@"
