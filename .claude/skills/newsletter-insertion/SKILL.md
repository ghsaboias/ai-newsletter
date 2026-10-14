---
name: newsletter-insertion
description: >-
  Coloca a inserção de parceiro (anúncio) do dia no draft do Substack da newsletter
  de AI/Tech. Lê o board Publicidade (GitHub Project #5) atrás de cards "📧 Newsletter"
  com Data no ar = hoje; para cada um, acha o modelo do Cliente (post template do
  Substack, via newsletters/ai/insertions/registry.json) ou, se não houver, manda o
  agente insertion-designer criar a partir do card; depois insere no bloco
  só-para-não-assinantes+free, no lugar do teaser do paywall. Chamada pelo
  newsletter-draft; também roda sozinha. Aciona com "inserção do dia", "colocar o
  anúncio", "/newsletter-insertion". Aceita `YYYY-MM-DD` (default: hoje).
allowed-tools: Read, Write, Bash, Agent
---

## O que é uma inserção

Anúncio pago que vai **só para não-assinantes e assinantes free**: um nó
`dynamicContent` (audiences `non_sub` + `free_sub`) logo depois da `horizontal_rule`
que fecha as Grandes, antes do nó `paywall`. Em dia de inserção o anúncio **ocupa o
lugar do teaser** "Abaixo, apenas para assinantes:" (que sai). Anatomia do modelo:
banner 1272×312 com `href` → parágrafos centralizados (dado em negrito + complemento)
→ botão → `horizontal_rule`.

O modelo de cada Cliente é um **post template do Substack** (menu Templates do
editor; `sstats templates`). `newsletters/ai/insertions/registry.json` liga o
Cliente do board ao `template_id`. O template é a fonte da verdade: se o Gui edita a
copy lá, é a versão editada que entra.

## Args

`/newsletter-insertion [YYYY-MM-DD]`. Quando chamada pelo `newsletter-draft`, a data
vem dele. `REPO` = raiz do repo (`git rev-parse --show-toplevel`), `D =
$REPO/pipeline/output/ai/<DATE>`.

## Step 1: Inserções do dia

```bash
python3 "$REPO/pipeline/tools/insertions.py" list --date <DATE> > "$D/insertions.json"
jq -c '{count, warnings, i: [.insertions[] | {number, cliente, status, model: (.model.template_id // null)}]}' "$D/insertions.json"
```

Só contam cards **abertos**: card fechado já foi entregue ou foi cancelado. Para
cancelar uma inserção, basta fechar o card.

- `count == 0` → `SKIP insertion: nada no board para <DATE>` e pare. Dia comum: o
  teaser do paywall fica.
- `warnings` (card sem Cliente, dois cards do mesmo Cliente no mesmo dia) → reporte
  na roll-up. Card duplicado é erro do board, não escolha um sozinho: se os dois
  apontam pro mesmo Cliente, a inserção sai uma vez (o modelo é o mesmo) e o aviso
  vai pro Gui.

## Step 2: Modelo que falta → insertion-designer

Para cada inserção com `model == null`, dispare o agente (vários em paralelo, num
tiro só, se houver mais de um):

```
Agent({
  description: "Modelo de inserção: <Cliente>",
  subagent_type: "insertion-designer",
  prompt: "Card: #<number> (daily-journal-tech/publicidade).\nCliente (chave do registry): <cliente>\nData no ar: <DATE>\nCrie o modelo de inserção e registre-o."
})
```

O agente devolve `OK <Cliente>: template <id> …` ou uma linha de falha (`FALTA LINK`,
etc.). Falha → **não insira nada desse Cliente**, siga com os outros e ponha a falha
na roll-up. Depois de todos, refaça o Step 1 e confira que nenhum `model` ficou
`null` para os que deram OK.

Modelo novo é commitado (só os arquivos dele, nunca `git add -A`):

```bash
cd "$REPO" && git add newsletters/ai/insertions/registry.json newsletters/ai/insertions/<slug>* \
  && git commit -m "insertions: modelo da inserção <Cliente>" && git push
```

## Step 3: Inserir no draft

```bash
python3 "$REPO/pipeline/tools/insertions.py" insert --date <DATE> --dir "$D"
```

Relê o board, busca cada template, troca o teaser (ou uma inserção anterior) pelos
blocos do dia e confere server-side. Idempotente: rodar de novo troca, não empilha.
Recusa post já publicado. Se algum card ainda está sem modelo, sai com erro sem tocar
no draft: aí a inserção do dia não entra, e isso vai em destaque na roll-up.

Com duas inserções no mesmo dia (ex.: Locaweb e Praso em 21/10), as duas entram no
mesmo lugar, uma embaixo da outra, cada uma no seu bloco, na ordem dos cards.

## Saída

Uma linha por inserção: `Inserção: #<n> <Cliente> (template <id>[, modelo NOVO])`,
mais os avisos. Modelo novo: mostre o PNG do banner e o `sstats template <id> --text`,
porque o Gui vai querer ver o que foi ao ar no nome do parceiro.

Não mexa no status do card no board: ele vira Done quando a edição é publicada, pelo
fluxo do #dj-publicidade.
