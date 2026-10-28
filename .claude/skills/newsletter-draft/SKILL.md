---
name: newsletter-draft
description: >-
  Orquestra a geração do draft da newsletter de AI/Tech pelo caminho novo
  (research → facts → edition), inteiramente com sub-agentes em sessão, sem prosa
  intermediária (pt.md). Encadeia: research (skill newsletter-research → 3
  especialistas + dedup → research.json) → facts (agente facts → facts.md) →
  edição (agente generator → edition.md) → LINK+PAYWALL+PUSH (extract+paywall-teaser →
  ingest --execute → rewrite-links → push de UM draft no Substack, DJ-linkado +
  com paywall; antes do push, checks repetition-checker ∥ fact-verifier →
  repetition.json + fact-check.json, e TODOS os findings são corrigidos no
  edition.md) → COMPLETA o draft:
  imagens/vídeos (newsletter-images auto, tudo aprovado), recomendações
  (newsletter-recs) e inserção de parceiro do dia, se o board Publicidade tiver uma
  (newsletter-insertion, que cria o modelo quando falta); às segundas, as rodadas
  da semana revisadas (newsletter-rounds) no fim. Para se algum passo de
  CONTEÚDO falhar. Ao final devolve a URL do draft completo do Substack, pronto
  pra revisão humana NO EDITOR (só gosto: nada sinalizado fica pro Gui
  corrigir). NÃO inicia a revisão e — crítico — NÃO
  re-empurra depois do primeiro push (o draft do Substack vira a fonte da verdade).
  É o orquestrador do draft da newsletter de AI/Tech (substituiu o antigo caminho
  de prosa). Aciona quando o usuário diz "rodar o draft", "draftar a
  edição", "run newsletter draft", "rodar a newsletter", "/newsletter-draft". Aceita `YYYY-MM-DD` e a flag `mini`.
allowed-tools: Skill, Read, Write, Bash, Agent
---

## When this skill runs

User wants the day's draft built via the **agent chain** (`research → facts →
edition`), the architecture decided in `AGENT_MIGRATION.md` — no prose `pt.md`, no
generator, no draft-rewrite. It chains, in order:

1. `newsletter-research`  (skill) → `research.json`
2. `facts`               (agent)  → `facts.md`   (atomic fact base + `**Fontes:**` provenance)
3. `generator`        (agent)  → `edition.md`       (3-tier edition: Grandes / Médias / Leia também)
3.5. **LINK + PAYWALL + PUSH** (the product):
   - `extract` (agent, facts.md-driven, fired in Step 3 *with* the generator) → `sources.json`; `paywall-teaser` (agent, fired right after the edition gate) → `paywall-meta.json`
   - `ingest --propose` → `cluster-candidates.json`; **you pick same-story matches** → `cluster-decisions.json` (cluster into an existing DJ news instead of minting a new image-less card)
   - `ingest --execute` → `links.json` + ~1 DJ news page per *unclustered* story
   - **fix every finding**: `repetition-checker` ∥ `fact-verifier` (fired right after the edition gate, overlapping the LINK block) → `repetition.json` + `fact-check.json`; every finding, any severity, is fixed in `edition.md`
   - `rewrite-links --in edition.md --out edition-final.md` → DJ links baked into the md
   - `substack-preview.sh … --paywall-after-grandes` → **push ONE Substack draft** (DJ-linked + paywalled)
4. **Complete the draft** (sequential, each edits the live draft): `newsletter-images <DATE> auto` → `newsletter-recs <DATE>` → `newsletter-insertion <DATE>` → on Mondays, `newsletter-rounds <DATE>` (reviewers fired after research, section appended last)

When it finishes, **the complete Substack draft (DJ-linked, paywalled, with images,
recs and the day's partner insertion) is the artifact ready for the human review** (which happens *in Substack* now, and is
*approving/adjusting tiering* and taste edits, not rewriting prose). Nothing the
checks flagged is left for the reviewer: every finding is fixed before the push.
This skill does **not** start the review, and — critically —
**after the first push the Substack draft is source of truth; the skill never
re-pushes** (hand-added images/video/text in the editor must not be clobbered).
Step 4's images/recs/insertion are not a re-push: each one GETs the live draft,
inserts its nodes and PUTs it back, before anyone has opened the editor.

This is the whole daily job. "Run newsletter draft" replaces the old three-skill
prompt (draft, then images with everything approved, then recs, then send the URL):
the run ends by replying with the draft URL.

## Args

Invoked as `/newsletter-draft [args]`. Parse from the user message:

- `YYYY-MM-DD` — run for a specific date (overrides "today").
- `mini` — pass-through to research (1 cluster, 3-story cap); facts/edition then run
  normally on those 3 stories. Fast end-to-end smoke test.
- (no args) — today's date, full run.

## Step 0: Resolve the date ONCE

Run `date '+%Y-%m-%d %H:%M:%S %Z'`. Set `DATE` = today unless an explicit
`YYYY-MM-DD` was passed. **Resolve `DATE` here and pass it explicitly to every
step** — never let a child re-derive it (a run crossing midnight could split
across two day-dirs). Keep the start epoch for the final duration:

```bash
date '+%Y-%m-%d %H:%M:%S %Z'; date +%s   # second number = START, keep it
```

```
REPO    = /Users/guilherme/ai-newsletter          # raiz do repo (onde vivem os scripts)
DAY_DIR = $REPO/pipeline/output/ai/<DATE>
```

E confira que `.claude/agents/` está **plano** — este é um GATE:

```bash
REPO=/Users/guilherme/ai-newsletter   # exporte junto do START; os Steps 3.5d e 5 usam
find "$REPO/.claude/agents" -mindepth 2 -name '*.md' | grep . && echo "HALT: definição de agente em subdiretório"
```

Achou algo → **HALT**, não dispare agente nenhum. O Claude Code varre `agents/`
recursivamente: uma cópia em subdiretório (`_backup/`, `old/`) entra no registro
com o mesmo `name:` e pode vencer a colisão — foi o que aconteceu em 2026-07-30
(rodou o `repetition-checker` de 07-29, sem checagem de léxico e sem a tool
`Bash`, e nada acusou erro). Backup de agente é o git, nunca uma cópia dentro de
`agents/`. E as definições são carregadas **no início da sessão**: consertar os
arquivos não conserta a sessão em curso — arrume e rode numa **sessão nova**.

### Step 0.5 — partner insertion preflight (full run only)

The day's partner insertion needs only the Publicidade board, so check it now. If a
model has to be created, that runs in the background under the whole research →
push chain instead of adding ~10 min at the end:

```bash
D=$REPO/pipeline/output/ai/<DATE>; mkdir -p "$D"
python3 "$REPO/pipeline/tools/insertions.py" list --date <DATE> > "$D/insertions.json" \
  && jq -c '{count, warnings, missing: [.insertions[] | select(.model == null) | {number, cliente}]}' "$D/insertions.json" \
  || echo "WARN insertion preflight: board query failed — Step 4c retries"
```

For each `missing` entry, fire the `insertion-designer` agent now, in the background,
with the same prompt `newsletter-insertion` uses (its Step 2) — and commit the new
model as that step says once the agent returns OK. `count == 0` → nothing to do; Step 4c will just
print the skip. Never block the chain on this.

## Orchestration model

This skill is **thin** and **gated**. Three jobs only:

1. **Run each step in order**: research via the `newsletter-research` *skill*;
   facts and the edition via the registered *agents* (`facts`, `generator`) dispatched
   with the `Agent` tool. (Research is a skill because it's a 3-agent fan-out +
   merge; facts and generator are single agents, so they're dispatched directly — there's
   no facts/generator child skill to delegate to.) **Maximize the back-half overlap:**
   `extract` reads only facts.md+research.json, so it's fired *with* the `generator`
   (Step 3), not after the edition; and the moment the edition gate passes, the three
   edition-only agents — `paywall-teaser` + the two checks (`repetition-checker`,
   `fact-verifier`) — are fired together and run in the background while
   `ingest` (Step 3.5) proceeds. Their findings are fixed in `edition.md` at Step
   3.5d, after ingest and before `rewrite-links` → push.
2. **Gate between the CONTENT + LINK steps.** After research/facts/edition/extract/ingest,
   verify the output exists/validates *before* starting the next. Missing/invalid →
   **STOP the chain and report which step failed**. This reproduces `set -euo
   pipefail`. The push is **create-once** (skips if `.substack-draft-id` exists).
   Findings don't halt the chain: they get fixed.
3. **Print one final roll-up.**

**Idempotent.** Each output is checked first; if it already exists, skip that step
(don't re-dispatch). Re-running resumes from the first incomplete step. To force a
clean rerun, delete the outputs you want regenerated (`research.json`, `facts.md`,
`edition.md`, `sources.json`, `links.json`, `edition-final.md`, `paywall-meta.json`). **The
push is the exception:** deleting outputs will **not** re-push — `.substack-draft-id`
is the create-once lock, and it's deliberate (the editor copy is canonical). To
genuinely re-push you'd remove `.substack-draft-id` too, which spawns a *new* draft;
don't, unless you mean to abandon the edited one.

**Don't read agent verbose output back into context.** Each agent returns a
one-line summary; trust the file on disk and the gate.

## Step 1: Research

Idempotency: if `$DAY_DIR/research.json` exists with `story_count > 0`, skip this
step. Otherwise:

```
Skill({ skill: "newsletter-research", args: "<DATE>" })   # append " mini" when the mini flag is set
```

Gate:

```bash
D=/Users/guilherme/ai-newsletter/pipeline/output/ai/<DATE>
if [ -s "$D/research.json" ] && jq -e '.story_count > 0' "$D/research.json" >/dev/null 2>&1; then
  echo "OK research: $(jq '.story_count' "$D/research.json") stories, $(jq '.source_count' "$D/research.json") sources"
else
  echo "HALT: research.json missing or empty"
fi
```

`HALT` → stop, do not run Step 2.

### Step 1.5 — Monday: fire the rounds review (full run only)

Only when `date -d <DATE> +%u` is `1`, and not in `mini`. Read
`.claude/skills/newsletter-rounds/SKILL.md` and run its **Fase 1** now: the dump plus
up to 5 Sonnet reviewers in the background. They need only the `deals` table, so
they run under facts → edition → push; Step 4d does the Fase 2. Fired here and not
at Step 0.5 so they don't share the window with the 3 researchers. A failed dump is
a `WARN` for the roll-up, never a halt.

## Step 2: Facts (agent)

Idempotency: if `$DAY_DIR/facts.md` exists, skip. Otherwise dispatch the `facts`
agent with a **paths-only** prompt (its methodology lives in its own system
prompt):

```
Agent({
  description: "Facts: research → facts.md",
  subagent_type: "facts",
  prompt: "Date: <DATE>.\nResearch (input): /Users/guilherme/ai-newsletter/pipeline/output/ai/<DATE>/research.json\nWrite the atomic fact base to: /Users/guilherme/ai-newsletter/pipeline/output/ai/<DATE>/facts.md"
})
```

Gate (facts.md exists, has `##` story sections, and every section carries a
`**Fontes:**` block — the link provenance the edition depends on):

```bash
D=/Users/guilherme/ai-newsletter/pipeline/output/ai/<DATE>
SEC=$(grep -c '^## ' "$D/facts.md" 2>/dev/null || echo 0)
FON=$(grep -c '^\*\*Fontes:\*\*' "$D/facts.md" 2>/dev/null || echo 0)
if [ -s "$D/facts.md" ] && [ "$SEC" -gt 0 ] && [ "$FON" -eq "$SEC" ]; then
  echo "OK facts: $SEC stories, $(grep -c '^- ' "$D/facts.md") fact bullets, $FON Fontes blocks"
else
  echo "HALT: facts.md missing, no sections, or Fontes blocks ($FON) != sections ($SEC)"
fi
```

`HALT` → stop, do not run Step 3. (The Fontes==sections check matters: a section
without a Fontes block leaves the edition with no links for that story.)

Then **tokenize the Fontes blocks** so the next step cites short tokens instead of
transcribing URLs (the fix for the URL-corruption class of bug):

```bash
python3 /Users/guilherme/ai-newsletter/pipeline/tools/link-tokens.py tokenize "$D/facts.md"
```

In place + idempotent — adds `[S<n>]` to each source line, prints the token count.

## Step 3: Edition (agent) + the parallel fan-out

Two outputs depend only on `facts.md` (+ `research.json`): the **edition**
(`generator`) and the **sources** (`extract`). `extract` reads facts.md +
research.json — **not** edition.md — and is the LINK-block long pole (~10 min), so
starting it here (rather than after the edition) hides it under the edition +
paywall + ingest + checks work. **Full run: fire BOTH in one message now.**
Dispatch only whichever lacks its output (idempotency): `generator` if `edition.md`
is missing, `extract` if `sources.json` is missing. **Mini run: dispatch
`generator` only** — `extract` feeds the LINK block that mini skips.

**First, gather the recent Grandes and the previous edition** — the lead (`###`)
headlines of the last few editions, plus the **path** of the most recent edition
file. The headlines feed the generator's **no-re-lead rule** (a story that
already led as a Grande in the last few days must not lead again — it demotes to
Média). The previous-edition path feeds its **continuity rule**: the generator
reads the file and reframes any story that already ran yesterday (any tier, not
just Grandes) as continuity instead of fresh news — that's what stops a Média
from re-running two days straight as if new. `edition-final.md` is preferred
over `edition.md` (it carries the human-reviewed tiering and headlines):

```bash
ROOT=/Users/guilherme/ai-newsletter/pipeline/output/ai
RECENT_GRANDES=""; PREV_EDITION=""; CHECK=<DATE>
for i in 1 2 3 4 5; do
  CHECK=$(date -j -v-1d -f "%Y-%m-%d" "$CHECK" "+%Y-%m-%d" 2>/dev/null || date -d "$CHECK - 1 day" "+%Y-%m-%d")
  for f in edition-final.md edition.md; do
    [ -s "$ROOT/$CHECK/$f" ] || continue
    RECENT_GRANDES+=$(grep '^### ' "$ROOT/$CHECK/$f" | sed "s/^### /- $CHECK: /")$'\n'
    [ -n "$PREV_EDITION" ] || PREV_EDITION="$ROOT/$CHECK/$f"
    break
  done
done
printf '%s' "${RECENT_GRANDES:-(nenhuma)}"   # paste into the generator prompt below
printf '%s\n' "${PREV_EDITION:-(nenhuma)}"   # ditto — the continuity-rule path
```

```
Agent({
  description: "edition: facts → edition.md",
  subagent_type: "generator",
  prompt: "Date: <DATE>.\nFact base (input): /Users/guilherme/ai-newsletter/pipeline/output/ai/<DATE>/facts.md\nWrite the three-tier edition to: /Users/guilherme/ai-newsletter/pipeline/output/ai/<DATE>/edition.md\n\nRecent Grandes (do NOT re-lead these — a story whose core event already led here demotes to Média, unless it has a genuinely new, dated in-window development to lead with):\n<paste RECENT_GRANDES, one 'YYYY-MM-DD: headline' per line — or '(nenhuma)'>\n\nEdição da véspera (READ this file before writing — any of today's stories whose core event already ran there, in ANY tier, must be framed as continuity per your Continuidade rule, never re-presented as fresh):\n<paste PREV_EDITION — the path — or '(nenhuma)'>"
})
Agent({                                    # FULL RUN ONLY — gated later at Step 3.5a
  description: "Extract sources → sources.json",
  subagent_type: "extract",
  prompt: "Date: <DATE>.\nfacts.md (input): <DAY_DIR>/facts.md\nresearch.json (metadata join): <DAY_DIR>/research.json\nWrite sources.json to: <DAY_DIR>/sources.json"
})
```

Wait for the **edition** (the critical content step; `extract` keeps running in
the background and is gated at Step 3.5a). After `edition.md` is written, **expand
the link tokens** to real URLs:

```bash
D=/Users/guilherme/ai-newsletter/pipeline/output/ai/<DATE>
python3 /Users/guilherme/ai-newsletter/pipeline/tools/link-tokens.py expand "$D/edition.md" "$D/facts.md"
```

This replaces every `](S<n>)` with the source URL from `facts.md`'s token map and
**hard-fails (non-zero exit) on any unknown token or raw-URL regression** — so
every link in the edition traces to a Fontes URL *by construction* (this replaces
the after-the-fact link-provenance lint). If `expand` exits non-zero, **STOP**: it
prints the offending token(s). The fix is to re-run `generator` (delete `edition.md`
first) — never hand-patch a URL. Idempotent: a clean re-run on an already-expanded
`edition.md` is a no-op.

Gate (edition.md exists, **1-3 Grandes** `###` — capped at 3, no lower quota; the
writer picks the number within that cap — plus clusters `####` and a "Leia
também"):

```bash
D=/Users/guilherme/ai-newsletter/pipeline/output/ai/<DATE>
G=$(grep -c '^### ' "$D/edition.md" 2>/dev/null || echo 0)
C=$(grep -c '^#### ' "$D/edition.md" 2>/dev/null || echo 0)
if [ -s "$D/edition.md" ] && [ "$G" -ge 1 ] && [ "$G" -le 3 ] && [ "$C" -gt 0 ]; then
  echo "OK edition: $G grandes, $C cluster/leia-também headers"
else
  echo "WARN edition: got $G grandes / $C #### (Grandes capped at 3, ≥1 — the writer sets the number by the day's stories; >3 is a real problem, inspect: $D/edition.md)"
fi
```

Then gate the **subtitle** (line 3 of `edition.md`): one ` | `-separated segment
per Grande, at most one segment ending in `?`. This is the published format
(every edition since July was rewritten into it by hand), so a mismatch is a
generator bug — delete `edition.md` and re-run `generator`, don't hand-patch:

```bash
SUB=$(sed -n 3p "$D/edition.md")
S=$(awk -F' \\| ' '{print NF}' <<<"$SUB")
Q=$(grep -o '?' <<<"$SUB" | wc -l)
if [ "$S" -eq "$G" ] && [ "$Q" -le 1 ]; then echo "OK subtitle: $S segments, $Q question"
else echo "FAIL subtitle: $S segments for $G grandes, $Q questions — re-run generator: $SUB"; fi
```

An out-of-cap Grande count is worth surfacing — **>3 is a real problem** (the cap),
a low count is the writer's call on a thin/repetitive day — but `edition.md` still
exists, so flag it for the human review rather than hard-failing.

### As soon as the edition gate passes — fan out the edition-dependent work

Everything that needs only `edition.md` runs **concurrently** with the
extract→ingest→push block (none of it touches the push, so none of it should wait
for it):

- `paywall-teaser` → `paywall-meta.json` (the push consumes it) — **full run only**
- `repetition-checker` → `repetition.json` (fixed at Step 3.5d)
- `fact-verifier` → `fact-check.json` (fixed at Step 3.5d). **Passe
  a ele o caminho da edição da véspera** (o primeiro item da lista `PREV` logo
  abaixo, que você já resolve para o `repetition-checker`). Sem esse arquivo ele
  não consegue distinguir continuidade legítima de atribuição inventada e reporta
  como `high` toda referência correta a ontem — em 2026-08-19 os dois findings
  `high` eram falsos positivos e duas frases certas foram apagadas por causa
  disso.

First resolve the previous editions `repetition-checker` compares against — walk
back up to 3 prior days that have an edition file (prefer `edition.md`, fall back
to `v2.md`/`pt.md`):

```bash
ROOT=/Users/guilherme/ai-newsletter/pipeline/output/ai
PREV=(); CHECK=<DATE>
for i in 1 2 3; do
  CHECK=$(date -j -v-1d -f "%Y-%m-%d" "$CHECK" "+%Y-%m-%d" 2>/dev/null || date -d "$CHECK - 1 day" "+%Y-%m-%d")
  for f in edition.md v2.md pt.md; do
    if [ -s "$ROOT/$CHECK/$f" ]; then PREV+=("$CHECK: $ROOT/$CHECK/$f"); break; fi
  done
done
printf '%s\n' "${PREV[@]}"   # the list to paste into repetition-checker's prompt
```

Then **fire them in one message** (skip any whose output already exists; on a
**mini** run skip `paywall-teaser` — there's no push to feed; on the **free-edition
day** — `date -d <DATE> +%u` equals `TOPIC_FREE_WEEKDAY` in `config.sh`, Wednesday —
skip it too: that edition has no paywall, see Step 3.5f):

```
Agent({                                          # FULL RUN ONLY
  description: "Paywall teasers → paywall-meta.json",
  subagent_type: "paywall-teaser",
  prompt: "Date: <DATE>.\nedition.md (input): <DAY_DIR>/edition.md\nWrite paywall-meta.json to: <DAY_DIR>/paywall-meta.json\nWrite paywall-teaser.md to: <DAY_DIR>/paywall-teaser.md"
})
Agent({
  description: "Repetition check vs prior editions",
  subagent_type: "repetition-checker",
  prompt: "Date: <DATE>.\nCurrent edition: <DAY_DIR>/edition.md\nPrevious editions to compare against:\n<the PREV list, one 'YYYY-MM-DD: path' per line — or '(none found)'>\nWrite findings to: <DAY_DIR>/repetition.json"
})
Agent({
  description: "Fact-verify the edition",
  subagent_type: "fact-verifier",
  prompt: "Date: <DATE>.\nresearch.json: <DAY_DIR>/research.json\nfacts.md: <DAY_DIR>/facts.md\nEdition (edition.md): <DAY_DIR>/edition.md\nEdição da véspera (árbitro da classe 'atribuição inventada' — toda referência a 'na véspera'/'ontem'/'confirmada em <dia>' na edição de hoje tem de estar NESTE arquivo): <o primeiro item da lista PREV, só o caminho — ou '(nenhuma)'>\nWrite findings to: <DAY_DIR>/fact-check.json"
})
```

All three run in the background while you do Step 3.5; you fix the two checks'
findings at Step 3.5d (by then they're done). The paywall meta finishes in well under
a minute — long before ingest+rewrite complete — so it's ready for the push. If
**no** previous editions were found, still run `fact-verifier` (it needs none) and
either skip `repetition-checker` with a note or pass it "(none found)".

## Step 3.5: Link + paywall + push (the product)

This is the **LINK + PUSH** block — it turns the content (`edition.md`) into the
**DJ-linked + paywalled Substack draft** the human reviews. It runs a real
**production DB write** (`ingest --execute` creates ~1 DJ news page per story) and
a **live Substack push**. Per `AGENT_MIGRATION.md` decisions (b)/(c)/(d): DJ links
are baked **before** the push, the paywall is baked into the **same** push, and
**after the first push the Substack draft is source of truth — never re-push** (a
re-push clobbers the hand-added images/video/text).

**Mini mode skips this entire block.** `mini` is a content-chain smoke test — it
must **not** write to the production DB (`ingest --execute`) or push a live Substack
draft. On a `mini` run, stop after the edition gate (Step 3) + the two checks; print
"SKIP 3.5 (mini)".

**Create-once / idempotent-skip.** Every output here skips if it already exists.
Critically: **if `$DAY_DIR/.substack-draft-id` exists, the draft was already pushed
— DO NOT push again** (the editor copy is canonical now). Skipping the push on a
re-run is correct behavior, not a failure.

### Step 3.5a — gate extract (already dispatched in Step 3)

`extract` and `paywall-teaser` were already fired back in Step 3 — `extract`
alongside the `generator`, `paywall-teaser` right after the edition gate. Here you
just **wait for `extract` and gate it** before `ingest` consumes its `sources.json`
(on a re-run where `sources.json` already exists, nothing was dispatched — just
gate the file). Gate **extract** (sources.json exists, `source_count > 0`, and
`url_count` equals the actual URL total — the facts→sources coverage contract):

```bash
D=/Users/guilherme/ai-newsletter/pipeline/output/ai/<DATE>
if [ -s "$D/sources.json" ] && jq -e '.source_count>0 and (.url_count==([.news_entities[].sources[].url]|length))' "$D/sources.json" >/dev/null 2>&1; then
  echo "OK extract: $(jq '.source_count' "$D/sources.json") entities, $(jq '.url_count' "$D/sources.json") sources"
else
  echo "HALT: sources.json missing/invalid (source_count or url_count check failed)"
fi
```

`HALT` → stop, do **not** ingest. The paywall meta is **soft**: if
`paywall-meta.json` is missing, push *without* the paywall and warn — never halt
the chain on a missing teaser file.

### Step 3.5b — cluster candidates → you decide (homepage de-dup + image inheritance)

**Why:** the newsletter's own `ingest` mints one `auto_created` DJ news per story.
Those carry **no image** and **crowd the homepage** with duplicate cards for stories
that DJ's RSS feed may already cover (with an image). So before ingest, probe whether
each entity is **the same story** as an existing DJ news; cluster the genuine matches
into it (the entity's articles attach, its edition links point at the existing page,
which already has an image — no new card). Recall is programmatic; the same-story
**judgment is yours** — cosine alone can't make it (a true match can sit *below* a
broad "AI-business" attractor in similarity).

Idempotent: skip if already ingested (`links.json`) or decisions already authored.

```bash
D=/Users/guilherme/ai-newsletter/pipeline/output/ai/<DATE>
if [ -f "$D/links.json" ] || [ -f "$D/cluster-decisions.json" ]; then
  echo "SKIP cluster-propose (already ingested or decided)"
else
  /Users/guilherme/ai-newsletter/pipeline/ingest.sh <DATE> --propose
fi
```

This writes `$D/cluster-candidates.json` (read-only — no DB writes): per entity, the
top 3 existing-news candidates, each with `similarity`, `shared_entities`, `has_image`,
`article_count`, `headline`, `url`, plus a `suggested_news_id` hint (the strongest
candidate clearing both the similarity bar and the shared-entity floor).

**Now decide.** If `cluster-candidates.json` exists with entities, read it and for each
entity judge whether **any candidate is the SAME EVENT** (not merely the same topic or
sector). Decide per entity:

- **Cluster** only on a clear same-story match. High `shared_entities` (named orgs/people
  in common) is the strongest signal; `suggested_news_id` is a hint, **verify it** — the
  top-similarity candidate is sometimes a generic attractor with `shared_entities: 0`.
- **Prefer** a matching candidate with `has_image: true` (that's the payoff), but **never**
  cluster a non-matching story just to grab an image.
- **When in doubt, create.** A wrong cluster points the edition's link at the wrong story;
  that's worse than an extra homepage card.

Write your choices to `$D/cluster-decisions.json` (omit entities that should create):

```json
{ "decisions": [ { "index": 4, "action": "cluster", "newsId": "<news_id>" } ] }
```

`index` is the entity's `index` from `cluster-candidates.json`. Entities you omit (or mark
`"action": "create"`) mint a fresh news as before. Then proceed to ingest — it consumes
this file.

### Step 3.5c — ingest `--execute` (real production DB write)

Idempotency: if `links.json` exists, the day was already ingested — **skip**.

**Run this as ONE foreground Bash call with an explicit `timeout: 600000` (10 min).**
Ingest takes ~4 min for ~20 entities; the Bash tool's default 2-min timeout kills it
mid-run, leaving partial DB rows that the retry then collides with (duplicate-key
noise). **Never** run it with `run_in_background`, `nohup`, or a detached `&`: in the
headless Slack harness, Bash background tasks are killed the moment the turn ends and
their completion notification never arrives — a detached ingest finishes with nobody
watching and the chain stalls. Staying foreground keeps the turn (and the run) alive.
The same 10-min timeout applies to the `--propose` call in Step 3.5b.

```bash
D=/Users/guilherme/ai-newsletter/pipeline/output/ai/<DATE>
[ -f "$D/links.json" ] || /Users/guilherme/ai-newsletter/pipeline/ingest.sh <DATE> --execute
if [ -s "$D/links.json" ] && [ "$(jq 'length' "$D/links.json")" -gt 0 ]; then
  echo "OK ingest: $(jq 'length' "$D/links.json") DJ link mappings"
else
  echo "HALT: links.json missing/empty"
fi
```

`HALT` → stop. This creates ~1 `auto_created` DJ news page per story **now, before
review** — the orphan-page risk for any story later cut in review is **accepted**
(decision (c)).

`ingest.sh --execute` also revalidates every deduped `dailyjournal.news/news/...`
path in `links.json` via Daily Journal's `/api/revalidate`. If that revalidation
step fails, treat it as a hard failure and stop before rewriting links or pushing
the Substack draft; otherwise link previews can cache ISR 404s for freshly-created
pages.

### Step 3.5d — fix every finding in `edition.md`

Wait for both checks (`repetition.json`, `fact-check.json`). Then fix **every**
finding, any severity, in `edition.md`, before the link rewrite, so the push
carries the fixed text:

```bash
D=/Users/guilherme/ai-newsletter/pipeline/output/ai/<DATE>
python3 "$REPO/pipeline/tools/validate-findings.py" repetition "$D/repetition.json"
python3 "$REPO/pipeline/tools/validate-findings.py" fact-check "$D/fact-check.json"
python3 "$REPO/pipeline/tools/apply-lexicon.py" "$D/repetition.json" "$D/edition.md" --execute
jq -r '.issues[] | "[\(.severity)/\(.type)] \(.overlap)\n  → \(.suggestion)"' "$D/repetition.json"
jq -r '.fidelity_issues[] | "[\(.severity)] \(.issue) (\(.where)): \(.claim)"' "$D/fact-check.json"
jq -r '.dropped_facts[] | "[\(.severity)] dropped em \"\(.story)\": \(.fact)"' "$D/fact-check.json"
```

`apply-lexicon.py` handles the lexicon findings. Fix each remaining finding by
editing `edition.md` yourself, following its `suggestion`: rewrite the repeated
phrasing/framing, mark continuity for a repeated story, cut or correct the claim
the fact-check flagged (against `research.json`), put back the dropped fact.
Keep every link as it is. The roll-up lists what was fixed.

`$REPO` é a raiz do repo (Step 0), **não** `$ROOT` — `ROOT`, nos Steps 3/3.5, é o
diretório de *output*.

### Step 3.5e — rewrite-links → `edition-final.md` (bake DJ links into the md)

```bash
D=/Users/guilherme/ai-newsletter/pipeline/output/ai/<DATE>
/Users/guilherme/ai-newsletter/pipeline/rewrite-links.sh <DATE> --in "$D/edition.md" --out "$D/edition-final.md" --quiet
```

Soft gate — report how many anchors became DJ links; if `edition-final.md` carries **0**
`dailyjournal.news` links, **WARN** (the push would be unlinked) but let the human
decide; don't hard-fail:

```bash
DJ=$(grep -oE 'https?://[^) ]*dailyjournal\.news[^) ]*' "$D/edition-final.md" | sort -u | wc -l | tr -d ' ')
echo "  edition-final.md: $DJ DJ links"; [ "$DJ" -eq 0 ] && echo "  WARN: no DJ links in edition-final.md"
```

### Step 3.5f — push ONE Substack draft (DJ-linked + paywalled) — CREATE-ONCE

```bash
D=/Users/guilherme/ai-newsletter/pipeline/output/ai/<DATE>
if [ -s "$D/.substack-draft-id" ]; then
  echo "SKIP push: draft $(cat "$D/.substack-draft-id") already exists — editor copy is canonical, never re-push"
else
  PW=(); [ -f "$D/paywall-meta.json" ] && PW=(--paywall-after-grandes --paywall-meta "$D/paywall-meta.json")
  /Users/guilherme/ai-newsletter/pipeline/substack-preview.sh <DATE> "$D/edition-final.md" draft \
    "edição (DJ-linked + paywall)" "Leia também" "${PW[@]}"
fi
[ -f "$D/substack-draft.json" ] && echo "  Draft: $(jq -r '.url' "$D/substack-draft.json")"
```

`substack-preview.sh` does the md→HTML, loads Substack creds, wraps "Leia também"
in a callout box, and (when the meta is present) bakes the paywall after the
Grandes. The `draft` suffix persists the draft id to `.substack-draft-id` (the
doc's `--id-out` target) and writes `substack-draft.json` with the review URL. The
create-once guard above is what protects the hand-edited editor copy on any re-run.

**Free-edition day (Wednesday).** `substack-preview.sh` reads the weekday off
`<DATE>` and, when it is `TOPIC_FREE_WEEKDAY` (`newsletters/ai/config.sh`), drops
any paywall flags and retitles line 1 of the md from `[Tech]` to
`[Edição Gratuita]` before converting it. The push prints `Free edition (…)`;
check that the `Title:` line it prints starts with `[Edição Gratuita]`. Nothing
to pass by hand.

The teaser blockquote goes inside a Substack **audience-specific content block**
(`dynamicContent`, audiences `non_sub` + `free_sub`), so only readers who actually
hit the wall see "Abaixo, apenas para assinantes:" — paid and founding subscribers
read straight from the Grandes into the Médias. It renders in the editor as an
"SE / Público" box; leave it alone during review. `substack_post.py` builds it
(`wrap_for_free_readers`), so nothing changes in the skill's commands.

## Step 4: Complete the draft (images → recs → insertion → rounds)

Full run only (mini has no draft). Requires `$D/.substack-draft-id`; without it the
push failed, so **stop** and report. Run the three **one after another, never in
parallel**: each GETs the live draft, edits it and PUTs it back, so two at once
would overwrite each other's work. A failure in one is reported in the roll-up and
the next one still runs; none of them halts the run.

**4a. Images.** Skip if `$D/images-final.json` exists (a re-run must not wipe
images Gui swapped in the editor). Otherwise:

```
Skill({ skill: "newsletter-images", args: "<DATE> auto" })
```

`auto` = everything pre-approved: every pick, strong and optional, plus every
official video, goes in without the Slack approval round.

**4b. Recs.** Skip if `$D/recs.json` exists. Otherwise:

```
Skill({ skill: "newsletter-recs", args: "<DATE>" })
```

**4c. Partner insertion.** Always run (it's idempotent). If Step 0.5 fired an
`insertion-designer`, wait for it to finish first.

```
Skill({ skill: "newsletter-insertion", args: "<DATE>" })
```

No insertion that day → it prints a skip and the paywall teaser stays. With an
insertion, the ad replaces the teaser in the free-only block.

**4d. Rounds (Mondays only).** Wait for the Step 1.5 reviewers, then run the
`newsletter-rounds` **Fase 2**: consolidate `rounds/final.json`, build, append the
section after the recs, verify on the server. Skip on other days.

## Step 5: Final roll-up

One block, then the hand-off line:

```bash
D=/Users/guilherme/ai-newsletter/pipeline/output/ai/<DATE>
echo "=== Draft Complete: <DATE> ==="
[ -f "$D/research.json" ] && echo "  Research:   $(jq '.story_count' "$D/research.json") stories"
[ -f "$D/facts.md" ]      && echo "  Facts:      $(grep -c '^## ' "$D/facts.md") stories, $(grep -c '^- ' "$D/facts.md") bullets"
[ -f "$D/edition.md" ]         && echo "  Edition:    $(grep -c '^### ' "$D/edition.md") grandes, $(grep -c '^#### ' "$D/edition.md") clusters/leia-também"
[ -f "$D/sources.json" ]  && echo "  Sources:    $(jq '.source_count' "$D/sources.json") entities, $(jq '.url_count' "$D/sources.json") urls"
[ -f "$D/links.json" ]    && echo "  Ingest:     $(jq 'length' "$D/links.json") DJ pages (executed)"
[ -f "$D/paywall-meta.json" ] && echo "  Paywall:    $(jq '.teasers|length' "$D/paywall-meta.json") teasers"
[ -f "$D/images-final.json" ] && echo "  Images:     $(jq '[.[] | select(.file)] | length' "$D/images-final.json") images, $(jq '[.[] | select(.videoId)] | length' "$D/images-final.json") videos"
[ -f "$D/recs.json" ]     && echo "  Recs:       $(jq -r '[.items[].title] | join(" / ")' "$D/recs.json")"
[ -f "$D/rounds/section.json" ] && echo "  Rounds:     $(jq -r '.[3].content[0].text' "$D/rounds/section.json")"
[ -f "$D/insertions.json" ] && echo "  Insertion:  $(jq -r 'if .count == 0 then "none today" else ([.insertions[] | "#\(.number) \(.cliente)"] | join(", ")) end' "$D/insertions.json")"
[ -f "$D/repetition.json" ] && echo "  Repetition: $(jq -r '"\(.issues|length) issues (high \([.issues[]|select(.severity=="high")]|length) / med \([.issues[]|select(.severity=="medium")]|length) / low \([.issues[]|select(.severity=="low")]|length))"' "$D/repetition.json") (all fixed)"
[ -f "$D/fact-check.json" ] && echo "  Fact-check: $(jq '.fidelity_issues|length' "$D/fact-check.json") fidelity / $(jq '.dropped_facts|length' "$D/fact-check.json") dropped (all fixed)"
echo "  Duration:   $(( ($(date +%s) - START) / 60 ))m $(( ($(date +%s) - START) % 60 ))s"
```

Then list what Step 3.5d fixed, one line per finding (what was flagged → what changed).
On Mondays, add the `newsletter-rounds` Saída block (drops, fixes, decisions for Gui).

Then print the hand-off (point at the **Substack draft** — the review happens
there now). **The last line of the reply is the editor URL**:
`https://dailyjournalnews.substack.com/publish/post/<id from .substack-draft-id>`.
If a model was created today, show its banner PNG and copy too (see
`newsletter-insertion` Saída).

> Draft no Substack completo — **DJ-linkado, com paywall, imagens, recomendações e
> a inserção do dia** — em `substack-draft.json`. Próximo passo: **revisão humana no
> editor do Substack** — aprovar/ajustar o *tiering* (quais 3 viram Grandes, o que
> cai pra Média/Leia também) e trocar o que não agradar. **A partir daqui o draft do
> Substack é a fonte da verdade — não rode a skill de novo pra re-publicar** (ela
> nem re-empurra: o id em `.substack-draft-id` trava o create-once). Todos os
> findings de `repetition.json` e `fact-check.json` já foram corrigidos antes do push.

Do **not** re-print each step's output — research's skill and the agents already
summarized. The orchestrator adds only the gate lines and this roll-up.

## Behavioral rules

- **Sequential and gated.** Each step's input is the previous step's output. A
  missing/invalid output halts the chain — never run a downstream step on bad
  input. (`facts` needs `research.json`; `generator` needs `facts.md` *with*
  its Fontes blocks.)
- **One DATE, passed explicitly to every step.** Resolve once in Step 0.
- **Delegate / dispatch, don't reimplement.** Research → the `newsletter-research`
  skill (owns the 3-agent fan-out + dedup). Facts/generator → the registered agents,
  paths-only prompts (they own their methodology). This skill only sequences,
  gates, and rolls up.
- **Every finding gets fixed.** `repetition-checker` and `fact-verifier` are fired
  right after the edition gate (end of Step 3) and run in parallel *with* ingest.
  Step 3.5d fixes all their findings in `edition.md` before the push. Nothing
  flagged is left for the reviewer.
- **Link before push; review in Substack.** Step 3.5 bakes DJ links + the paywall
  into the md and pushes ONE Substack draft *before* the human review — that draft
  *is* the artifact reviewed. There is **no** separate finalize/re-push afterward.
- **Create-once — never clobber the editor copy.** The push is guarded by
  `.substack-draft-id`: once it exists, the skill **skips** the push on every
  re-run. After the first push the Substack draft is source of truth; hand-added
  images/video/text must never be overwritten from local md.
- **Stop before the human review.** Ends after the complete draft (Step 4),
  replying with the draft URL. Do not start the review.
- **Step 4 runs serially.** Images, recs, insertion and rounds each read-modify-write the
  live draft; running two at once loses one's edits.
- **Idempotent resume.** Re-running picks up at the first missing output. Force a
  rerun by deleting the output(s).
- **Tight output.** No step-by-step play-by-play; gate lines + final roll-up only.

## Why this exists

The old `newsletter-draft` chains the **prose path** (research → generate →
draft-review → rewrite → `pt.md`). The migration (`AGENT_MIGRATION.md`) cut the
prose generator and draft-rewriter and moved to **research → facts → edition directly**:
`facts` absorbs translate+gloss, `generator` absorbs select+tier+trim+link, and
human review shifts from rewriting prose to approving tiering. Step 3.5 also folds
in what the old `finalize.sh` did — extract → ingest → rewrite-links → push — but
**ahead of** the review (decision: link before push, review in Substack), so the
reviewed artifact is a DJ-linked + paywalled Substack draft, not a local `.md`.
This skill is the chain's orchestrator and the **cutover candidate** to replace
both `newsletter-draft` *and* `newsletter-finalize`. Until the cutover is committed
and the superseded `.sh` steps deleted, this runs alongside the old path, not
instead of it.
