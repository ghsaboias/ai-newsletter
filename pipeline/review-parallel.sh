#!/bin/bash
#
# Parallel paragraph-level review.
#
# Usage:
#   pipeline/review-parallel.sh [DATE]              # spawn one tmux window per paragraph
#   pipeline/review-parallel.sh --final [DATE]      # spawn final serial window (subtitle + cross-paragraph sweep)
#   pipeline/review-parallel.sh --merge [DATE]      # merge review/pNN.out.md back into pt.md
#   pipeline/review-parallel.sh --status [DATE]     # show per-paragraph diff status
#
# Flow:
#   1. Run with no flag: splits pt.md into paragraphs and opens N tmux windows (2 panes each).
#      Each Claude is scoped to ONE paragraph, writes approved version to review/pNN.out.md.
#   2. When all paragraphs done: --merge, which rebuilds pt.md from .out.md files (backs up original).
#   3. Then --final to open a single window for subtitle, connector hygiene, ordering.
#
# Must run inside a tmux session.
#

set -euo pipefail

source "$(cd "$(dirname "$0")" && pwd)/_lib.sh"

MODE="spawn"
ARGS=()
for arg in "$@"; do
  case "$arg" in
    --final)  MODE="final" ;;
    --merge)  MODE="merge" ;;
    --status) MODE="status" ;;
    *)        ARGS+=("$arg") ;;
  esac
done

DATE=$(parse_date_arg "${ARGS[@]:-}")
init_day_dir

PT_FILE="$DAY_DIR/pt.md"
REVIEW_DIR="$DAY_DIR/review"

if [[ ! -f "$PT_FILE" ]]; then
  echo "Error: $PT_FILE not found" >&2
  exit 1
fi

# -------- splitter --------
# Split pt.md into: frontmatter, title, subtitle, body paragraphs.
# Body paragraphs are blank-line separated blocks that start with "**".
split_paragraphs() {
  mkdir -p "$REVIEW_DIR"
  python3 - "$PT_FILE" "$REVIEW_DIR" <<'PY'
import sys, re, os, pathlib

pt_path, review_dir = sys.argv[1], sys.argv[2]
text = pathlib.Path(pt_path).read_text()

# Strip frontmatter (--- ... ---) if present
fm_match = re.match(r'^---\n.*?\n---\n', text, re.DOTALL)
frontmatter = fm_match.group(0) if fm_match else ''
body = text[len(frontmatter):]

# Split into blocks by blank lines
blocks = [b for b in re.split(r'\n\s*\n', body) if b.strip()]

# First block starting with "# " is title
title = None
subtitle = None
paragraphs = []
for b in blocks:
    stripped = b.strip()
    if title is None and stripped.startswith('# '):
        title = stripped
    elif subtitle is None and title is not None and not stripped.startswith('**'):
        subtitle = stripped
    elif stripped.startswith('**'):
        paragraphs.append(stripped)
    else:
        # safety net: if subtitle wasn't set yet and block doesn't start with **, treat as subtitle
        if subtitle is None:
            subtitle = stripped
        else:
            paragraphs.append(stripped)

# Write manifest
with open(os.path.join(review_dir, '_manifest.txt'), 'w') as f:
    f.write(f"count={len(paragraphs)}\n")
    f.write(f"title={'set' if title else 'missing'}\n")
    f.write(f"subtitle={'set' if subtitle else 'missing'}\n")

# Write frontmatter + title + subtitle as _header.md (for reassembly)
with open(os.path.join(review_dir, '_frontmatter.md'), 'w') as f:
    f.write(frontmatter)
with open(os.path.join(review_dir, '_title.md'), 'w') as f:
    f.write((title or '') + '\n')
with open(os.path.join(review_dir, '_subtitle.in.md'), 'w') as f:
    f.write((subtitle or '') + '\n')
# Seed subtitle.out.md only if missing (preserve prior edits)
subtitle_out = os.path.join(review_dir, '_subtitle.out.md')
if not os.path.exists(subtitle_out):
    with open(subtitle_out, 'w') as f:
        f.write((subtitle or '') + '\n')

# Write each paragraph to pNN.in.md, seed pNN.out.md if missing
for i, p in enumerate(paragraphs, start=1):
    nn = f"{i:02d}"
    in_path = os.path.join(review_dir, f"p{nn}.in.md")
    out_path = os.path.join(review_dir, f"p{nn}.out.md")
    with open(in_path, 'w') as f:
        f.write(p + '\n')
    if not os.path.exists(out_path):
        with open(out_path, 'w') as f:
            f.write(p + '\n')

print(f"split: {len(paragraphs)} paragraphs", file=sys.stderr)
PY
}

# -------- prompt generator --------
write_bootstrap_prompt() {
  local nn="$1"  # e.g. "03"
  local prompt_file="$REVIEW_DIR/p${nn}.prompt.md"

  cat > "$prompt_file" <<EOF
Você é um revisor paralelo do draft de newsletter de **$DATE**. Outros Claudes estão revisando outros parágrafos simultaneamente em outras janelas do tmux. Você é responsável **APENAS pelo parágrafo $nn**.

## Setup imediato (faz em paralelo)

Invoca a skill \`newsletter-review\` e lê estes arquivos em paralelo:

- \`pipeline/output/ai/$DATE/pt.md\` — draft completo, para contexto de cadência e tom (NÃO edita este arquivo)
- \`pipeline/output/ai/$DATE/review/p${nn}.in.md\` — **o SEU parágrafo** (a fonte congelada)
- \`pipeline/output/ai/$DATE/review/p${nn}.out.md\` — onde você grava a versão aprovada (começa igual ao .in.md)
- \`pipeline/output/ai/$DATE/repetition.json\` — achados de repetição do repetition-check
- \`pipeline/output/ai/$DATE/research.json\` — fatos e fontes (para cruzamento)
- \`/Users/guilherme/.claude/projects/-Users-guilherme-ai-newsletter/memory/MEMORY.md\` e todos os arquivos referenciados (editorial-principles, feedback_*, repetition-review-learnings)

Também use \`Grep\` nas 3 edições anteriores em \`pipeline/output/ai/YYYY-MM-DD/pt.md\` para caçar repetições de entidades, números e phrasing.

**Não começa o review antes de carregar tudo isso.**

## REGRA CENTRAL (diferença do fluxo serial normal)

- **NUNCA edite \`pt.md\`.** Ele será recomposto no final por \`review-parallel.sh --merge\`.
- Toda versão aprovada vai para \`review/p${nn}.out.md\` via **Write** (sobrescreve o arquivo inteiro com o parágrafo atualizado, preservando links markdown).
- O \`.out.md\` é a fonte da verdade para o seu parágrafo a partir do momento em que existe.

## O que está fora do seu escopo

- Subtítulo, ordenação dos parágrafos no edition, contagem de "Separadamente"/"Em paralelo"/em-dashes no documento inteiro, repetição entre parágrafos do MESMO draft — tudo isso vai numa passada final serial depois do merge. **Não se preocupe com isso agora.** Foque dentro do seu parágrafo.

## O que ESTÁ no seu escopo

Cheque, em ordem de severidade:

1. **Repetição de história** contra as 3 edições anteriores (grep por entidades, números específicos, phrasing)
2. **Repetição verbatim de phrasing** do modelo ("registros fiscais revelaram", "em três continentes", etc.)
3. **AI-pt-br patterns**:
   - Nominalized chains: "escalada de componentes tecnológicos para armamento direto"
   - Stacked prepositions: "contra os X km/h de pico de Usain Bolt"
   - Abstract domain labels: "No produto,", "No campo judicial,", "Na saúde,"
   - Passivas sem sujeito quando um nome seria mais claro ("a empresa" com duas empresas em cena)
   - Parenthetical aposto pileups
4. **Jargão sem explicação inline**: acrônimos na primeira ocorrência (RLHF, ARR, TCEQ, WWDC), termos técnicos em linguagem acessível
5. **Ancoragem de números**: "alta de 58%" frente a quê? "mais do que o dobro" em relação ao quê?
6. **Clareza de referência**: pronomes ambíguos, "plataformas" quando é "redes sociais", "a empresa" ambígua
7. **Caracterização breve** de entidades que o leitor pode não conhecer ("Eli Lilly, farmacêutica americana líder em...")
8. **Precisão factual**: cruzar com research.json; se dado parece stale, use \`mcp__exa__web_search_exa\` para verificar se há coisa mais recente
9. **Em-dashes**: reduzir quando não são aposto genuíno — colon se elabora, ponto se é pensamento novo
10. **Links preservados**: todos os \`[texto](url)\` do .in.md devem continuar no .out.md (ajuste só o texto âncora se o phrasing mudar)

## Loop de review (segue a skill newsletter-review)

Um achado por vez, na ordem de severidade acima. Para cada um:

1. **Diz o quê e por quê.** Se for repetição: mostra o texto de hoje + texto da edição anterior em blocos lado a lado. Se for style: cita a frase, nomeia o problema.
2. **Propõe o fix.** Default: UMA melhor rewrite. Use 3 opções só quando o problema é "unclear/confuso" ou "ninguém fala assim" (gênero de voz).
3. **Mostra o parágrafo INTEIRO no "before" e no "after"**, mesmo que só uma frase mude. Propostas no chat são prosa plana: **sem links markdown, sem URLs**. Links só aparecem no Write do .out.md.
4. **Não edita sem aprovação.** Espera Guilherme dizer ok/pl/aplica.
5. **Ao aprovar: Write no \`review/p${nn}.out.md\`** com o parágrafo completo, links preservados.
6. Próximo achado.

## Shortcuts que Guilherme usa

- \`ok\` / \`pl\` / \`aprovado\` / \`aplica\` → Write da última proposta no .out.md
- \`checa\` → verifique nos research.json / pt.md / edições anteriores e confirme o fato
- \`troca X por Y\` / \`X -> Y\` → swap literal, aplica direto
- \`corte X\` / \`remova X\` / \`tira X\` → delete
- \`me dá 3 alternativas\` → liste exatamente 3 variantes em prosa plana
- \`exa search rápido\` → use mcp__exa__web_search_exa para verificar dado recente
- \`caracteriza brevemente {entidade}\` → adiciona uma cláusula curta sobre quem/o que é
- \`é tecnicamente correto?\` / \`isso é accurate?\` → pare, verifique, explique em PT simples, reforme se necessário
- \`X não foi usado ainda né?\` → grep no pt.md e nas últimas 3 edições, confirme

## Proativo, não pergunte

Nunca pergunte "quer que eu reescreva?" — **já traz a proposta**. Se Guilherme flagar "unclear", já traz 3 opções. Se ele flagar algo factual, já faz o search.

## Comunicação

- **PT-BR, sempre.** Guilherme fala PT-BR.
- Conciso. Cadência > tamanho.
- Sem narração de "vou fazer X agora" antes do tool call — só faz.
- End-of-turn: 1-2 frases, o que mudou.

## Ao terminar o parágrafo

Quando Guilherme disser que está satisfeito ou "pronto" / "clean" / "próximo":
1. Confirma que \`review/p${nn}.out.md\` reflete a última versão aprovada (re-Write se necessário)
2. Imprime: \`✓ parágrafo $nn pronto — review/p${nn}.out.md\`
3. Aguarda. Ele pode voltar com ajustes a qualquer momento.

## Agora

Carrega o contexto em paralelo. Depois:
1. Mostra o parágrafo $nn em prosa plana (sem links)
2. Lista os achados que você identificou, em ordem de severidade, numa lista curta (sem propor rewrites ainda)
3. Pergunta: "Vamos pelo primeiro, ou tem outro ponto de partida?"

Começa.
EOF
}

# -------- spawn mode --------
spawn_windows() {
  if [[ -z "${TMUX:-}" ]]; then
    echo "Error: must run inside a tmux session" >&2
    exit 1
  fi

  split_paragraphs

  local manifest="$REVIEW_DIR/_manifest.txt"
  local count
  count=$(grep '^count=' "$manifest" | cut -d= -f2)

  if [[ "$count" -eq 0 ]]; then
    echo "Error: no paragraphs found in pt.md" >&2
    exit 1
  fi

  echo ""
  echo "=== Parallel review: $DATE ==="
  echo "  Paragraphs: $count"
  echo "  Scratch:    $REVIEW_DIR/"
  echo ""

  local session
  session=$(tmux display-message -p '#S')

  for i in $(seq 1 "$count"); do
    local nn
    nn=$(printf "%02d" "$i")
    local window_name="rev-p${nn}"
    local prompt_file="$REVIEW_DIR/p${nn}.prompt.md"

    write_bootstrap_prompt "$nn"

    # Skip if window already exists (resumable)
    if tmux list-windows -t "$session" -F '#W' | grep -qx "$window_name"; then
      echo "  skip  $window_name (already open)"
      continue
    fi

    # Top pane: claude with bootstrap prompt inlined
    local claude_cmd="cd $ROOT_DIR && claude \"\$(cat $prompt_file)\""
    tmux new-window -a -n "$window_name" -d "$claude_cmd"

    # Bottom pane: live diff of in vs out for this paragraph
    local watch_cmd="cd $ROOT_DIR && watch -n 2 -t 'echo \"── p${nn}: in → out ──\"; diff -u $REVIEW_DIR/p${nn}.in.md $REVIEW_DIR/p${nn}.out.md 2>/dev/null || echo \"(identical)\"'"
    tmux split-window -t "$session:$window_name" -v -l 25% "$watch_cmd"
    tmux select-pane -t "$session:$window_name.0"

    echo "  spawn $window_name"
  done

  echo ""
  echo "Windows opened in session '$session'. Switch with: Ctrl-b n / Ctrl-b w"
  echo ""
  echo "When all paragraphs are clean:"
  echo "  pipeline/review-parallel.sh --merge $DATE    # rebuild pt.md from .out.md files"
  echo "  pipeline/review-parallel.sh --final $DATE    # final serial window (subtitle + cross-paragraph)"
}

# -------- merge mode --------
merge_paragraphs() {
  if [[ ! -d "$REVIEW_DIR" ]]; then
    echo "Error: $REVIEW_DIR not found — run spawn first" >&2
    exit 1
  fi

  local backup="$PT_FILE.pre-parallel-merge"
  cp "$PT_FILE" "$backup"

  python3 - "$REVIEW_DIR" "$PT_FILE" <<'PY'
import sys, os, glob, pathlib

review_dir, pt_path = sys.argv[1], sys.argv[2]

frontmatter = pathlib.Path(os.path.join(review_dir, '_frontmatter.md')).read_text()
title = pathlib.Path(os.path.join(review_dir, '_title.md')).read_text().strip()
subtitle = pathlib.Path(os.path.join(review_dir, '_subtitle.out.md')).read_text().strip()

para_files = sorted(glob.glob(os.path.join(review_dir, 'p*.out.md')))
paragraphs = []
for pf in para_files:
    content = pathlib.Path(pf).read_text().strip()
    if content:
        paragraphs.append(content)

parts = []
if frontmatter:
    parts.append(frontmatter.rstrip() + '\n')
if title:
    parts.append(title + '\n')
if subtitle:
    parts.append(subtitle + '\n')
for p in paragraphs:
    parts.append(p + '\n')

merged = '\n'.join(parts) + '\n'
pathlib.Path(pt_path).write_text(merged)
print(f"merged: {len(paragraphs)} paragraphs → {pt_path}", file=sys.stderr)
PY

  echo ""
  echo "  ✓ merged: $PT_FILE"
  echo "  backup:   $backup"
  echo ""
  echo "Diff vs backup:"
  diff -u "$backup" "$PT_FILE" | head -60 || true
}

# -------- final mode --------
spawn_final() {
  if [[ -z "${TMUX:-}" ]]; then
    echo "Error: must run inside a tmux session" >&2
    exit 1
  fi
  if [[ ! -d "$REVIEW_DIR" ]]; then
    echo "Error: $REVIEW_DIR not found — run spawn first and merge" >&2
    exit 1
  fi

  local prompt_file="$REVIEW_DIR/_final.prompt.md"
  cat > "$prompt_file" <<EOF
Passada final serial do draft de newsletter de **$DATE**. Os parágrafos individuais já foram revisados em paralelo e mergeados em \`pt.md\`. Agora você faz o sweep cross-paragraph que não pôde ser feito em paralelo.

## Setup imediato (faz em paralelo)

Invoca a skill \`newsletter-review\` e lê:

- \`pipeline/output/ai/$DATE/pt.md\` — draft já mergeado (edita este agora)
- \`pipeline/output/ai/$DATE/repetition.json\`
- \`pipeline/output/ai/$DATE/research.json\`
- \`/Users/guilherme/.claude/projects/-Users-guilherme-ai-newsletter/memory/MEMORY.md\` e arquivos referenciados
- Últimas 3 edições para grep de repetições cross-edition

## Escopo desta passada

Nesta ordem:

1. **Subtítulo** — reflete os top-3 leads do edition final? Concreto e específico, não abstrato.
2. **Ordenação dos parágrafos** — o lead merece liderar? Parágrafos temáticos vizinhos estão juntos (ex: China trade + US-China tech friction no mesmo bloco)?
3. **Connector hygiene** no documento inteiro:
   - "Separadamente" — no máximo 1 por edition. Grep e corta excesso.
   - "Enquanto" como transição de abertura — overused, substitui.
   - "Na direção oposta" / "Na contramão" — 1 por draft.
   - "No produto," / "No campo X," / "Na saúde," — domain labels genéricos, substitui por sujeito concreto ou pivô temporal/causal.
   - "Em paralelo" — monitora frequência.
4. **Contagem de em-dashes** — reduz onde não é aposto genuíno.
5. **Entidades/números duplicados entre parágrafos** do MESMO draft — grep por nomes, empresas, números específicos (US$X bi, XX%, NN toneladas).
6. **Phrasing repetido** ("registros fiscais revelaram", construções recicladas).

## Loop

Um achado por vez. Sempre mostra o parágrafo inteiro (ou o trecho de dois parágrafos, se for cross-paragraph). Propostas em prosa plana. Aprovação → Edit em \`pt.md\`.

## Shortcuts

\`ok\` / \`pl\` / \`aprovado\` → aplica. \`checa\` → verifica. \`me dá 3\` → 3 alternativas.

## Comunicação

PT-BR, conciso, cadência > tamanho. Proativo (não pergunte, já proponha).

## Ao terminar

\`✓ draft limpo. Próximo: pipeline/finalize.sh $DATE --execute\`

## Começa agora

Carrega o contexto. Depois lista os achados cross-paragraph que você identificou, em ordem de severidade. Pergunta por onde começar.
EOF

  local session
  session=$(tmux display-message -p '#S')
  local window_name="rev-final"

  if tmux list-windows -t "$session" -F '#W' | grep -qx "$window_name"; then
    tmux select-window -t "$session:$window_name"
    echo "  $window_name already open — switched"
    return
  fi

  local claude_cmd="cd $ROOT_DIR && claude \"\$(cat $prompt_file)\""
  tmux new-window -a -n "$window_name" "$claude_cmd"
  echo "  spawn $window_name"
}

# -------- status mode --------
show_status() {
  if [[ ! -d "$REVIEW_DIR" ]]; then
    echo "No review dir yet — run spawn first" >&2
    exit 1
  fi

  echo ""
  echo "=== Review status: $DATE ==="
  echo ""
  for in_file in "$REVIEW_DIR"/p*.in.md; do
    local nn
    nn=$(basename "$in_file" .in.md)
    local out_file="$REVIEW_DIR/${nn}.out.md"
    if diff -q "$in_file" "$out_file" >/dev/null 2>&1; then
      echo "  $nn  ○ unchanged"
    else
      local added removed
      added=$(diff "$in_file" "$out_file" | grep -c '^>' || true)
      removed=$(diff "$in_file" "$out_file" | grep -c '^<' || true)
      echo "  $nn  ● edited (+$added/-$removed lines)"
    fi
  done
  echo ""
}

# -------- dispatch --------
case "$MODE" in
  spawn)  spawn_windows ;;
  merge)  merge_paragraphs ;;
  final)  spawn_final ;;
  status) show_status ;;
esac
