---
name: newsletter-finalize
description: >-
  Finaliza a newsletter pra publicação. Roda 4 passos em sequência depois que pt.md foi revisado: extract (sub-agente identifica entidades+fontes → sources.json), ingest (chamada externa pro daily-journal-platform → links.json), rewrite-links (sed substitui URLs originais por DJ → final.md), e substack (pandoc gera substack.html). Por padrão é dry-run; aceita `--execute` pra escrever no DB. Aciona quando o usuário diz "finalizar a newsletter", "rodar finalize", "publicar a newsletter", "/newsletter-finalize". Substitui pipeline/finalize.sh.
allowed-tools: Read, Write, Bash, Agent
---

## Quando essa skill roda

Depois de você ter revisado o `pt.md` (incluindo passes de rewrite, no-dashes, e o que mais quiser). É a **Fase 2** completa do pipeline, equivalente a `pipeline/finalize.sh`.

**Pré-requisitos:**
- `research.json` (vem de `newsletter-research`)
- `pt.md` (vem de `newsletter-generate` + revisão)

**Outputs (em ordem):**
- `sources.json` (extract)
- `links.json` (ingest, só em modo `--execute`)
- `final.md` (rewrite-links + byline + recomendações)
- `substack.html` (substack)

## Args

Invocada como `/newsletter-finalize [args]`. Parse do user message:

- `YYYY-MM-DD` — data específica (default hoje)
- `--execute` — escreve no DB. Default é **dry-run** (não cria `links.json`)
- `--limit N` — limita a ingest a N stories

Exemplos:
- `/newsletter-finalize` — hoje, dry-run
- `/newsletter-finalize --execute` — hoje, escrita real
- `/newsletter-finalize 2026-05-19 --execute`
- `/newsletter-finalize --execute --limit 3`

## Step 0: Date

Rode `date '+%Y-%m-%d'` se data não veio.

## Step 1: Paths e pré-requisitos

```
ROOT          = /Users/guilherme/ai-newsletter
DJ_DIR        = /Users/guilherme/daily-journal-platform
DAY_DIR       = $ROOT/pipeline/output/ai/$DATE
RESEARCH      = $DAY_DIR/research.json
PT_FILE       = $DAY_DIR/pt.md
SOURCES_FILE  = $DAY_DIR/sources.json
LINKS_FILE    = $DAY_DIR/links.json
FINAL_FILE    = $DAY_DIR/final.md
SUBSTACK_FILE = $DAY_DIR/substack.html
SOURCE_PROMPT = $ROOT/pipeline/prompts/SOURCE_EXTRACTION.md
```

Hard checks (parar imediatamente se faltar):
- `$RESEARCH` não existe → erro: rodar `/newsletter-research`
- `$PT_FILE` não existe → erro: rodar `/newsletter-generate` (e revisão)

Cada passo abaixo é **idempotente individualmente** — se o output já existe, pula. Pra re-rodar um passo: deletar seu output.

## Step 2: Extract (LLM)

Se `$SOURCES_FILE` já existe → printa contagem (`jq '.news_entities | length'`) e pula.

Senão:

1. Leia `$SOURCE_PROMPT`. Substitua **placeholders de chave única** (`{date}` e `{day_dir}`):
   ```
   {date}    → $DATE
   {day_dir} → $DAY_DIR
   ```
   ⚠ Atenção: `SOURCE_EXTRACTION.md` usa **`{x}`** (chave única), diferente do `{{X}}` do GENERATION.md / DRAFT_REWRITE.md.

2. Dispatch sub-agente:

```
Agent({
  description: "Extract sources for <DATE>",
  subagent_type: "general-purpose",
  prompt: "<conteúdo do SOURCE_EXTRACTION.md substituído>\n\n---\n\nExtract sources for <DATE>.\n- Research file: <RESEARCH>\n- Article file: <PT_FILE>\nSave to <SOURCES_FILE>."
})
```

Sub-agente tem Read/Write/Edit. Lê research+pt.md, monta JSON estruturado, salva.

3. Valida:
```bash
test -f "$SOURCES_FILE" || echo "ERRO: extract falhou"
jq empty "$SOURCES_FILE" && echo "JSON válido"
URL_COUNT=$(jq '.url_count' "$SOURCES_FILE")
ARTICLE_URLS=$(grep -oE 'https?://[^)]+' "$PT_FILE" | sort -u | wc -l | tr -d ' ')
[[ "$URL_COUNT" == "$ARTICLE_URLS" ]] && echo "✓ URLs batem ($URL_COUNT)" || echo "⚠ URL mismatch: JSON=$URL_COUNT, artigo=$ARTICLE_URLS"
```

## Step 3: Ingest (chamada externa, sem LLM)

Se `$LINKS_FILE` já existe → printa contagem (`jq 'length'`) e pula.

Senão, monta args e chama o script TS no daily-journal-platform:

```bash
INGEST_ARGS=("$SOURCES_FILE")
[[ "$EXECUTE" == true ]] && INGEST_ARGS+=("--execute")
[[ -n "$LIMIT" ]] && INGEST_ARGS+=("--limit" "$LIMIT")

(cd /Users/guilherme/daily-journal-platform && npx tsx scripts/ingest.ts "${INGEST_ARGS[@]}")
```

**Nota:** o script TS gera `links.json` em **ambos** os modos (dry-run e execute). A diferença é só se escreve no DB do daily-journal-platform. Step 4 funciona em qualquer modo desde que sources.json esteja válido.

## Step 4: Rewrite links (sed, sem LLM)

Se `$FINAL_FILE` já existe → printa contagem de links externos restantes e pula.

Senão:

```bash
if [[ ! -f "$LINKS_FILE" ]]; then
  echo "ERRO: $LINKS_FILE não existe — rode finalize com --execute"
  exit 1
fi

cp "$PT_FILE" "$FINAL_FILE"
MAPPING_COUNT=$(jq 'length' "$LINKS_FILE")
echo "Substituindo $MAPPING_COUNT links..."

replaced=0
skipped=0
while IFS=$'\t' read -r source_url dj_url; do
  escaped_source=$(printf '%s' "$source_url" | sed 's/[&]/\\&/g')
  escaped_dj=$(printf '%s' "$dj_url" | sed 's/[&]/\\&/g')
  if grep -qF "$source_url" "$FINAL_FILE"; then
    sed -i '' "s|${escaped_source}|${escaped_dj}|g" "$FINAL_FILE"
    replaced=$((replaced + 1))
  else
    skipped=$((skipped + 1))
    echo "  ⚠ não achei: $source_url"
  fi
done < <(jq -r 'to_entries[] | "\(.key)\t\(.value)"' "$LINKS_FILE")

echo "Replaced: $replaced, Skipped: $skipped"

# Lista links externos que sobraram (devem ser zero ou só dailyjournal.news)
remaining=$(grep -oE 'https?://[^)]+' "$FINAL_FILE" | grep -v 'dailyjournal.news' | sort -u | wc -l | tr -d ' ')
echo "Links externos restantes: $remaining"
```

## Step 5: Inject byline + recomendações

Roda sempre que `$FINAL_FILE` existe e ainda não tem o byline / a seção. **Edits in-place, idempotente** (só roda se ainda não fez).

```bash
BYLINE="Por: Guilherme Saboia e Vinicius Gushiken"

if [[ -f "$FINAL_FILE" ]] && ! grep -qF "$BYLINE" "$FINAL_FILE"; then
  python3 -c "
import re
content = open('$FINAL_FILE').read()
content = re.sub(r'(# .+\n\n.+\n)', r'\1\n$BYLINE\n', content, count=1)
open('$FINAL_FILE', 'w').write(content)
"
  echo "Byline injetado"
fi

if [[ -f "$FINAL_FILE" ]] && ! grep -qF "Recomendações de hoje" "$FINAL_FILE"; then
  printf '\n**Recomendações de hoje:**\n' >> "$FINAL_FILE"
  echo "Recomendações section adicionada"
fi
```

## Step 6: Substack (pandoc, sem LLM)

Se `$SUBSTACK_FILE` já existe → printa size e pula.

Senão:

```bash
if [[ ! -f "$FINAL_FILE" ]]; then
  echo "ERRO: $FINAL_FILE não existe"
  exit 1
fi
pandoc "$FINAL_FILE" --from markdown-tex_math_dollars --to html -o "$SUBSTACK_FILE"
echo "✓ $SUBSTACK_FILE"
```

## Step 7: Report

Printa estado final de todos os outputs:

```bash
echo ""
echo "=== Finalize complete: $DATE ==="
echo "  sources.json : $(jq '.news_entities | length' $SOURCES_FILE 2>/dev/null || echo 'missing') entities"
echo "  links.json   : $(jq 'length' $LINKS_FILE 2>/dev/null || echo 'missing') mappings"
echo "  final.md     : $(test -f $FINAL_FILE && wc -w < $FINAL_FILE | tr -d ' ' || echo 'missing') words"
echo "  substack.html: $(test -f $SUBSTACK_FILE && wc -c < $SUBSTACK_FILE | tr -d ' ' || echo 'missing') bytes"
echo ""
echo "  Cola substack.html no editor HTML (</>) do Substack."
```

Modo dry-run: indique explicitamente "**dry-run** — rode com `--execute` pra escrever no DB e gerar `final.md`/`substack.html`".

## Regras de comportamento

- **Idempotência por passo.** Cada output é seu próprio checkpoint. Skill pula passos cujo output já existe. Pra re-rodar: deletar.
- **Dry-run é o default.** Só escreve no DB com `--execute` explícito.
- **Step 2 (extract) é o único com LLM.** Steps 3-6 são mecânicos — não dispatch sub-agente desnecessário.
- **Hard fail em pré-requisitos.** Sem research.json ou pt.md → para imediatamente.
- **Não invoca outras skills.** Tudo inline no orchestrator.

## Por que substitui finalize.sh

O script bash usa caffeinate + tmux + run-agent.sh pra orquestrar 4 sub-processos. Skill colapsa em: orchestrator faz Bash inline pros 3 mecânicos + dispatcha 1 Agent pro extract. Caffeinate não é necessário (o turno da skill é uma execução contínua, não daemoniza). Tmux some.

**Sem mudança comportamental** — mesmos inputs, mesmos outputs, mesmas flags.
