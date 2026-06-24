#!/usr/bin/env bash
# render.sh <slug>
# Exporta posts/chart-<slug>.html como PNG 2× (retina), recortado justo no card
# #capture (sem a margem branca do body), em posts/chart-<slug>.png.
# Idempotente: navega a aba existente se já houver uma, senão abre. Alvo por
# substring de URL (-t=chart-<slug>), então NÃO precisa capturar tab ID.
#
# Render via browser-tools (NÃO headless — Brave headless trava no setup de perfil).
# Roda com o Brave/Chrome real aberto. Se o PNG sair em branco/baixo, rode de novo
# (o Chart.js às vezes precisa de um segundo passe).
set -euo pipefail

SLUG="${1:?uso: render.sh <slug>}"
POSTS="/Users/guilherme/ai-newsletter/posts"
BT="$HOME/agent-tools/browser-tools"
HTML="$POSTS/chart-$SLUG.html"
FILE="file://$HTML"
SCALE=2   # browser-screenshot.js captura em deviceScaleFactor 2

test -f "$HTML" || { echo "ERRO: sem html em $HTML"; exit 1; }

# nav se a aba já existe, senão abre (evita acumular abas duplicadas em re-render)
if "$BT/browser-list.js" 2>/dev/null | grep -q "chart-$SLUG\.html"; then
  "$BT/browser-nav.js" -t="chart-$SLUG.html" "$FILE" >/dev/null
else
  "$BT/browser-open.js" "$FILE" >/dev/null
fi

# altura do card (#capture) + 76 (padding do body: ~38px topo + 38px base) p/ dimensionar o viewport
H="$("$BT/browser-eval.js" -t="chart-$SLUG.html" "Math.ceil(document.getElementById('capture').getBoundingClientRect().height)+76")"
case "$H" in ''|*[!0-9]*) echo "ERRO: altura inválida ('$H') — chart não renderizou? rode de novo"; exit 1;; esac

# 800px de largura (card 720 + padding) → deviceScaleFactor 2 = PNG 1600px de largura
"$BT/browser-resize.js" -t="chart-$SLUG.html" 800 "$H" >/dev/null

# rect final do card (já no viewport definitivo) p/ recortar justo: "left top width height"
RECT="$("$BT/browser-eval.js" -t="chart-$SLUG.html" "(function(){var r=document.getElementById('capture').getBoundingClientRect();return Math.round(r.left)+' '+Math.round(r.top)+' '+Math.round(r.width)+' '+Math.round(r.height);})()")"
read -r CL CT CW CH <<< "$RECT"
case "$CW$CH" in ''|*[!0-9]*) echo "ERRO: rect do card inválido ('$RECT')"; exit 1;; esac

TMP="$("$BT/browser-screenshot.js" -t="chart-$SLUG.html")"
test -f "$TMP" || { echo "ERRO: screenshot falhou ($TMP)"; exit 1; }

# recorta no card #capture (coordenadas CSS × SCALE) → sem margem branca do body
magick "$TMP" -crop "$((CW * SCALE))x$((CH * SCALE))+$((CL * SCALE))+$((CT * SCALE))" +repage "$POSTS/chart-$SLUG.png"

echo "ok: $POSTS/chart-$SLUG.png  (card recortado: $((CW * SCALE))×$((CH * SCALE))px)"
echo "inspecionar overlap: magick \"$POSTS/chart-$SLUG.png\" -crop WxH+X+Y +repage /tmp/x.png  (depois Read /tmp/x.png)"
