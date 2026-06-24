---
name: newsletter-draft-review
description: >-
  Revisa o pt.md recém-gerado contra as 3 últimas edições, procurando repetições de story, phrasing e framing. Produz repetition.json com findings estruturados. Etapa 3 do pipeline (depois de newsletter-generate, antes de newsletter-rewrite). Aciona quando o usuário diz "revisar o draft", "rodar repetition-check", "checar repetição", "/newsletter-draft-review", ou pede explicitamente para revisar o pt.md. Substitui pipeline/repetition-check.sh.
allowed-tools: Read, Write, Bash, Agent, Grep, Glob
---

## Quando essa skill roda

Depois de `newsletter-generate` produzir o `pt.md`. É a **etapa 3** do pipeline:

1. `newsletter-research` → `research.json`
2. `newsletter-generate` → `pt.md`
3. **`newsletter-draft-review`** → `repetition.json` ← essa skill
4. `newsletter-rewrite` → `pt.md` (sobrescrito) + `rewrite-notes.json`

## Args

Invocada como `/newsletter-draft-review [args]`. Parse do user message:

- `YYYY-MM-DD` — revisar uma data específica
- (sem args) — usar a data de hoje

## Step 0: Estabelecer a data

Rode `date '+%Y-%m-%d %H:%M:%S %Z'` primeiro. Relógio do sistema é a fonte da verdade — não assuma data do contexto.

Defina `DATE` = hoje (ou arg explícito).

## Step 1: Paths e idempotência

```
ROOT       = /Users/guilherme/ai-newsletter
DAY_DIR    = $ROOT/pipeline/output/ai/$DATE
PT_FILE    = $DAY_DIR/pt.md
OUTPUT     = $DAY_DIR/repetition.json
PROMPT_MD  = $ROOT/pipeline/prompts/REPETITION_CHECK.md
```

Checks:
- **`$OUTPUT` já existe** → printa o issue count e para. Idempotente; usuário deleta pra re-rodar.
- **`$PT_FILE` não existe** → para com erro. Rodar `/newsletter-generate` primeiro.

## Step 2: Ler e substituir o prompt

Leia `$PROMPT_MD`. Substitua placeholders:

- `{{DATE}}` → `$DATE`

(O resto dos paths não vai no template — vai no contexto passado ao sub-agente abaixo.)

## Step 3: Dispatch do revisor

Um Agent só. Sem paralelismo — review é uma tarefa única, comparativa.

```
Agent({
  description: "Review draft for <DATE> against past editions",
  subagent_type: "general-purpose",
  prompt: "<conteúdo do REPETITION_CHECK.md com {{DATE}} substituído>\n\n---\n\nDraft atual: <PT_FILE>\n\nEdições anteriores estão em: /Users/guilherme/ai-newsletter/pipeline/output/ai/<DATA>/pt.md (uma pasta por data, formato YYYY-MM-DD). Descubra quais existem e busque repetições como achar melhor.\n\nEscreva a análise em JSON válido em: <OUTPUT>"
})
```

Sub-agente tem Read/Write/Grep/Glob/Bash. Confie nele pra descobrir as edições e decidir estratégia.

## Step 4: Validar

Depois que o sub-agente retorna:

```bash
test -f /Users/guilherme/ai-newsletter/pipeline/output/ai/$DATE/repetition.json || echo "ERRO: repetition.json missing"
jq empty /Users/guilherme/ai-newsletter/pipeline/output/ai/$DATE/repetition.json && echo "JSON válido"
jq '.issues | length' /Users/guilherme/ai-newsletter/pipeline/output/ai/$DATE/repetition.json
jq -r '.summary // "(no summary)"' /Users/guilherme/ai-newsletter/pipeline/output/ai/$DATE/repetition.json
```

## Step 5: Report

Printa:
- Issue count
- Summary (a linha que o revisor gera)
- Lista compacta dos issues, formato `[type] suggestion (≤120 chars)`:

```bash
jq -r '.issues[] | "  • [" + .type + "] " + (.suggestion | .[0:120])' /Users/guilherme/ai-newsletter/pipeline/output/ai/$DATE/repetition.json
```

Mantenha tight — sem narração de passos intermediários.

## Regras de comportamento

- **Confie no relógio do sistema.** Sempre `date` primeiro.
- **Checa contra TODAS as edições anteriores** (quando existem). Sem comparação, não tem review.
- **Idempotência primeiro.** Se `repetition.json` existe, para. Usuário re-roda deletando.
- **Sem acesso web.** Review compara apenas arquivos locais.
- **Um sub-agente, não paralelo.** Review é uma única passagem comparativa.
- **Severidade calibrada.** Issues do tipo `story` (mesma notícia recontada) são as mais sérias; `phrasing` e `framing` são menores. Não inflar finding count com nitpicks — o REPETITION_CHECK.md tem o critério.

## Por que substitui repetition-check.sh

O script antigo spawna processo Claude em tmux, polla por output, sinaliza via `tmux wait-for` — mesma overhead bash do research/generate. A skill colapsa em: orchestrator faz 2-3 Bash de setup → dispatcha 1 Agent → reporta.

**Mudança comportamental real**: a skill usa a lookup robusta de edições anteriores (ls-based), que sobrevive a gaps de calendário. O script antigo caminhava 3 dias do calendário — se você pulasse fim de semana, ele achava 1 ou 2 edições só.
