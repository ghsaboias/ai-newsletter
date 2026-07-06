#!/usr/bin/env bash
# render.sh <slug>            → exporta posts/chart-<slug>.html como PNG 2× (retina),
#                               recortado justo no card #capture, em posts/chart-<slug>.png
# render.sh <slug> --eval JS  → avalia uma expressão JS na página do chart (medição de
#                               chartArea p/ posicionar a logo etc.) e imprime o resultado
#
# Plataforma:
#  - macOS: browser-tools (Brave REAL via CDP — headless trava no setup de perfil).
#    Idempotente: navega a aba existente se já houver uma (-t=chart-<slug>).
#  - Linux (Pi): Chromium headless via headless-render.js (CDP puro, sem deps npm).
#    Headless funciona no Linux; browser-tools/Brave é só no Mac.
# Se o PNG sair em branco/baixo, rode de novo (o Chart.js às vezes precisa de 2º passe).
set -euo pipefail

SLUG="${1:?uso: render.sh <slug> [--eval 'expressão JS']}"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO="$(cd "$SCRIPT_DIR/../../.." && pwd)"
POSTS="$REPO/posts"
HTML="$POSTS/chart-$SLUG.html"
FILE="file://$HTML"
SCALE=2   # captura em deviceScaleFactor 2

test -f "$HTML" || { echo "ERRO: sem html em $HTML"; exit 1; }

# ---------- Linux (Pi): Chromium headless ----------
if [ "$(uname -s)" = "Linux" ]; then
  if [ "${2:-}" = "--eval" ]; then
    exec node "$SCRIPT_DIR/headless-render.js" eval "$HTML" "${3:?uso: render.sh <slug> --eval 'expressão JS'}"
  fi
  exec node "$SCRIPT_DIR/headless-render.js" render "$HTML" "$POSTS/chart-$SLUG.png"
fi

# ---------- macOS: browser-tools (Brave real) ----------
BT="$HOME/agent-tools/browser-tools"

# nav se a aba já existe, senão abre (evita acumular abas duplicadas em re-render)
if "$BT/browser-list.js" 2>/dev/null | grep -q "chart-$SLUG\.html"; then
  "$BT/browser-nav.js" -t="chart-$SLUG.html" "$FILE" >/dev/null
else
  "$BT/browser-open.js" "$FILE" >/dev/null
fi

if [ "${2:-}" = "--eval" ]; then
  exec "$BT/browser-eval.js" -t="chart-$SLUG.html" "${3:?uso: render.sh <slug> --eval 'expressão JS'}"
fi

# altura do card (#capture) + 76 (padding do body: ~38px topo + 38px base) p/ dimensionar o viewport
H="$("$BT/browser-eval.js" -t="chart-$SLUG.html" "Math.ceil(document.getElementById('capture').getBoundingClientRect().height)+76")"
case "$H" in ''|*[!0-9]*) echo "ERRO: altura inválida ('$H') — chart não renderizou? rode de novo"; exit 1;; esac

# 800px de largura (card 720 + padding). Forçamos deviceScaleFactor=2 EXPLICITAMENTE.
# O daemon do browser-tools faz o resize com DSF=0 (= default do display); num Brave
# relançado sem retina (ex.: --remote-debugging-port na mão) isso vira 1×, e o crop ×2
# abaixo estoura os limites e o magick clampa → PNG em 720px (metade da resolução).
# Com DSF=2 fixo: screenshot 1600px de largura, recorte ×2 → card 1440px (retina), sempre.
"$BT/browser-resize.js" -t="chart-$SLUG.html" 800 "$H" >/dev/null
node --input-type=module -e "import {run} from '$BT/lib/client.js'; await run('chart-$SLUG.html','raw',['Emulation.setDeviceMetricsOverride', JSON.stringify({width:800,height:$H,deviceScaleFactor:2,mobile:false})]);" >/dev/null

# CRÍTICO: recarrega DEPOIS de fixar o DSF=2. O Chart.js rasteriza o <canvas> no DPR do
# load; se a página carregou em DPR=1 (Brave sem retina nativo), o canvas fica em 1× e o
# screenshot em 2× só faz UPSCALE → a região do gráfico sai pixelada (título/legenda em
# HTML continuam nítidos, mas o canvas não). Recarregando com o DSF=2 já aplicado, o
# Chart.js redesenha o backing store em 2× (nítido de verdade). O override persiste pelo reload.
"$BT/browser-nav.js" -t="chart-$SLUG.html" "$FILE" >/dev/null

# guarda anti-borrão: DPR precisa ser 2 E o buffer do canvas precisa ser 2× do tamanho CSS
CRISP="$("$BT/browser-eval.js" -t="chart-$SLUG.html" "(function(){var c=document.querySelector('canvas');return (window.devicePixelRatio===2 && c && c.width===c.clientWidth*2) ? 'ok' : ('dpr='+window.devicePixelRatio+' buf='+(c?c.width+'x'+c.height:'?')+' css='+(c?c.clientWidth+'x'+c.clientHeight:'?'));})()")"
[ "$CRISP" = "ok" ] || echo "aviso: render não-retina ($CRISP) — a região do gráfico pode sair pixelada"

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
