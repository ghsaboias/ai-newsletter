---
name: newsletter-rewrite
description: >-
  Aplica os findings de repetition.json ao pt.md de forma cirúrgica (uma edição por finding, preservando o resto byte-a-byte). Etapa 4 do pipeline (depois de newsletter-draft-review). Produz pt.md sobrescrito, pt-original.md de backup, e rewrite-notes.json com applied/skipped/flagged. Aciona quando o usuário diz "rodar rewrite", "aplicar findings", "reescrever o draft", "/newsletter-rewrite", ou pede explicitamente para aplicar as repetições. Substitui pipeline/draft-rewrite.sh.
allowed-tools: Read, Write, Bash, Agent, Grep, Glob
---

## Quando essa skill roda

Depois de `newsletter-draft-review` produzir o `repetition.json` com findings. É a **etapa 4** do pipeline:

1. `newsletter-research` → `research.json`
2. `newsletter-generate` → `pt.md`
3. `newsletter-draft-review` → `repetition.json`
4. **`newsletter-rewrite`** → `pt.md` (sobrescrito), `pt-original.md`, `rewrite-notes.json` ← essa skill

## Args

Invocada como `/newsletter-rewrite [args]`. Parse do user message:

- `YYYY-MM-DD` — rewrite de uma data específica
- (sem args) — usar a data de hoje

## Step 0: Estabelecer a data

Rode `date '+%Y-%m-%d %H:%M:%S %Z'` primeiro. Relógio do sistema é a fonte da verdade.

Defina `DATE` = hoje (ou arg explícito).

## Step 1: Paths e idempotência

```
ROOT          = /Users/guilherme/ai-newsletter
DAY_DIR       = $ROOT/pipeline/output/ai/$DATE
PT_FILE       = $DAY_DIR/pt.md
PT_ORIGINAL   = $DAY_DIR/pt-original.md
REP_FILE      = $DAY_DIR/repetition.json
NOTES_FILE    = $DAY_DIR/rewrite-notes.json
REWRITE_MD    = $ROOT/pipeline/prompts/DRAFT_REWRITE.md
GENERATION_MD = $ROOT/newsletters/ai/prompts/GENERATION.md
MEMORY_DIR    = /Users/guilherme/.claude/projects/-Users-guilherme-ai-newsletter/memory
```

Checks (em ordem):

- **`$NOTES_FILE` já existe** → printa applied/skipped/flagged counts e para. Idempotente. Pra re-rodar: deletar `$NOTES_FILE` e (opcionalmente) restaurar `$PT_FILE` de `$PT_ORIGINAL`.
- **`$PT_FILE` não existe** → erro. Rodar `/newsletter-generate` primeiro.
- **`$REP_FILE` não existe** → erro. Rodar `/newsletter-draft-review` primeiro.

## Step 2: Skip se zero issues

```bash
ISSUE_COUNT=$(jq '.issues | length' "$REP_FILE")
```

Se `ISSUE_COUNT == 0` → printa "Sem repetições. Nada a reescrever." e para.

## Step 3: Backup retry-safe

```bash
if [[ ! -f "$PT_ORIGINAL" ]]; then
  cp "$PT_FILE" "$PT_ORIGINAL"
fi
```

Crucial: **só copia se `$PT_ORIGINAL` não existir**. Isso preserva o original verdadeiro em re-runs (se você re-rodar depois de uma falha, `$PT_FILE` já pode estar parcialmente editado — o `$PT_ORIGINAL` da primeira tentativa é o que vale).

## Step 4: Ler e substituir o prompt

Leia `$REWRITE_MD`. Substitua todos os placeholders:

- `{{DATE}}` → `$DATE`
- `{{PT_ORIGINAL}}` → `$PT_ORIGINAL`
- `{{PT_OUT}}` → `$PT_FILE`
- `{{REPETITION_JSON}}` → `$REP_FILE`
- `{{GENERATION_MD}}` → `$GENERATION_MD`
- `{{NOTES_JSON}}` → `$NOTES_FILE`
- `{{MEMORY_DIR}}` → `$MEMORY_DIR`

O texto resultante é o system prompt do sub-agente.

## Step 5: Dispatch do reescritor

Um Agent só. Edição cirúrgica é uma tarefa única — sem paralelismo.

```
Agent({
  description: "Apply repetition findings to <DATE> draft",
  subagent_type: "general-purpose",
  prompt: "<conteúdo do DRAFT_REWRITE.md com todos os placeholders substituídos>"
})
```

Sub-agente tem Read/Write/Edit. Ele:
1. Lê GENERATION.md (voz), memory files (constraints), repetition.json (findings), pt-original.md (base)
2. Aplica cada finding cirurgicamente — preserva o resto byte-a-byte
3. Escreve `pt.md` PRIMEIRO (artigo reescrito completo)
4. Escreve `rewrite-notes.json` POR ÚLTIMO (signal de completude com applied/skipped/flagged)

O DRAFT_REWRITE.md já tem as regras todas (safety valve, no meta-references, feminine for LLMs, caracterizações: variar antes de cortar, etc.) — confie nele.

## Step 6: Validar

Depois que o sub-agente retorna:

```bash
test -f "$NOTES_FILE" || echo "ERRO: rewrite-notes.json missing"
jq empty "$NOTES_FILE" && echo "JSON válido"
# pt.md deve ter mudado vs pt-original.md (a não ser que tudo tenha sido skipped)
diff -q "$PT_ORIGINAL" "$PT_FILE" >/dev/null && echo "AVISO: pt.md idêntico ao original"
```

## Step 7: Report

Printa, em ordem:

1. **Counts**: `Applied: N / Skipped: M / Flagged: K (de T findings)`

2. **Applied** (o que foi feito — usuário quer ver isso, não só os erros):

```bash
jq -r '.findings[] | select(.action == "applied") | "  • [applied] [" + .type + "] " + (.reason | .[0:140])' "$NOTES_FILE"
```

3. **Skipped** (não foi feito — checar se faz sentido):

```bash
jq -r '.findings[] | select(.action == "skipped") | "  • [skipped] [" + .type + "] " + (.reason | .[0:140])' "$NOTES_FILE"
```

4. **Flagged** (foi feito mas precisa olho humano):

```bash
jq -r '.findings[] | select(.action == "flagged") | "  • [flagged] [" + .type + "] " + (.reason | .[0:140])' "$NOTES_FILE"
```

5. **Diff command**: `diff $PT_ORIGINAL $PT_FILE`

Tight — sem narração de passos.

## Regras de comportamento

- **Confie no relógio do sistema.** Sempre `date` primeiro.
- **Backup é não-negociável.** Nunca sobrescrever `pt-original.md` se já existe.
- **Sub-agente escreve `pt.md` antes de `rewrite-notes.json`** (o NOTES é o signal de completude — se aparecer antes do PT, algo deu errado).
- **Idempotência primeiro.** Se `rewrite-notes.json` existe, para. Re-run = deletar.
- **Não toque no schema do `rewrite-notes.json`.** Outras ferramentas downstream podem ler.
- **Não adicione passos extras.** Skill é não-invasiva — só roda o DRAFT_REWRITE.md.

## Por que substitui draft-rewrite.sh

O script antigo usa tmux + run-agent.sh + tmux wait-for, igual aos outros scripts. A skill colapsa em: orchestrator faz 3-4 Bash de setup → dispatcha 1 Agent → reporta.

Sem mudança comportamental além do que outras skills da família já trouxeram (PT, dispatch direto via Agent tool, prompts inalterados a não ser que necessário).
