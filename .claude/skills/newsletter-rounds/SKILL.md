---
name: newsletter-rounds
description: >-
  Monta a seção "Funding Rounds da Semana" da edição de segunda da newsletter de
  AI/Tech: puxa as rodadas da semana do banco `deals` na mesma janela do job
  "Rodadas da semana" (DJ cron das 9h BRT em #feat-newsletter), revisa todos os itens
  com até 5 revisores Sonnet (valores, empresa, acurácia, relevância,
  duplicação/reciclagem), consolida, e anexa a seção no fim do draft do Substack, no
  formato publicado em 19/10. Chamada pelo newsletter-draft às segundas; também roda
  sozinha. Aciona com "rodadas da semana", "funding rounds", "/newsletter-rounds".
  Aceita `YYYY-MM-DD` (default: hoje; precisa ser segunda).
allowed-tools: Read, Write, Bash, Agent
---

## O que sai

No fim do draft, depois das Recomendações: régua, título centralizado **Funding
Rounds da Semana**, "Todos os investimentos em startups no mundo.", a linha em
negrito com o total ("US$ 5 bilhões em 65 rodadas entre 12 e 19 de outubro, sendo 3
no Brasil") e um parágrafo centralizado por rodada, ordenado por valor em USD:
nome + valor na moeda original + estágio; bandeira, país e setor; Liderança e
Valuation; resumo; link "Notícia no Daily Journal" e a data do anúncio. Fica atrás
do paywall que já existe (o Substack aceita um só). O `build.mjs` reproduz nó a nó a
seção publicada em 2026-10-19.

A fonte é a tabela `deals` do DJ, a mesma que alimenta o post do job no Slack, e a
janela é a dele: os 7 dias antes de segunda 12:00 UTC. Por isso os itens e a
numeração batem com a thread do Slack que o Gui vê às 9h.

## Args

`/newsletter-rounds [YYYY-MM-DD]`. `REPO` = `git rev-parse --show-toplevel`,
`D = $REPO/pipeline/output/ai/<DATE>`, `R = $D/rounds`. Quando o `newsletter-draft`
chama, ele roda a Fase 1 cedo e a Fase 2 no Step 4d; sozinha, rode as duas em
seguida.

## Fase 1 — dump + revisores (em background)

Pule se `$R/final.json` existe (a semana já foi revisada).

```bash
mkdir -p "$R" && cd ~/daily-journal-platform && bun --env-file=.env.local "$REPO/pipeline/tools/rounds/dump.ts" <DATE> "$R"
```

Imprime a manchete igual à do Slack e grava `digest.txt` (o texto do job) e
`items.json` (um item por rodada, na ordem do job: `output` com o texto do Slack,
`db` com a linha do banco, `linked_news`, `other_deals_same_company` e `hints`).

**Antes de dividir, leia a lista inteira** (`jq -r '.[] | "\(.n) \(.db.company_name)
| \(.db.amount_usd) | \(.db.announced_at[:10]) | \(.hints|join("; "))"'`). Um revisor
só vê a fatia dele, então duplicata entre fatias e reciclagem óbvia são suas: anote os
casos (mesma rodada em duas linhas, empresa com rodada anterior no banco, sede
discutível) e mande cada um como nota no prompt do bloco onde ele cai.

Divida em até 5 blocos contíguos por ordem (`n`), ~15 itens cada, em
`$R/batch<k>.json`, e dispare um Agent por bloco **no mesmo turno**, `model:
"sonnet"`, `run_in_background: true`, com este prompt:

```
Você revisa itens do digest semanal de rodadas de venture capital ("Rodadas da
semana", <período>) que vai na newsletter do Daily Journal (pt-BR). Hoje é <DATE>.

Entrada: <R>/batch<k>.json — itens <a> a <b>. Cada item tem:
- `output`: o texto exato que o job imprimiu. É ISSO que você revisa, só o que ele
  afirma: nome da empresa, valor + moeda, estágio, bandeira/país, setor, Liderança,
  Valuation, o resumo de uma linha, a data do anúncio. Não revise o que o output não diz.
- `db`: a linha do banco, com `source_excerpt` e uma `verification` automática
  anterior (veredito, motivo, fontes). Use como pista, não como verdade.
- `linked_news`: notícias do DJ ligadas ao deal, com `primary_source`.
- `other_deals_same_company` e `hints`: rodadas anteriores da mesma empresa e
  suspeitas de duplicata; use para detectar reciclagem.
<notas do bloco, se houver>

Para CADA item, confira em fontes independentes (comunicado da empresa ou do
investidor líder, filing, TechCrunch, Bloomberg/Reuters, blog do investidor):
1. Empresa: nome e grafia; país da SEDE (a bandeira), nunca o do investidor; setor.
2. Valor e moeda: o anunciado. É equity? Marque se mistura dívida, soma várias
   rodadas, é fundo (não empresa), M&A, IPO, subsídio, secundária, ou valuation
   lido como valor.
3. Estágio e líder(es): só é líder quem a fonte diz que liderou.
4. Valuation: só se reportado; tire se não tiver fonte.
5. Resumo (pt-BR, uma linha): correto? Se errado ou vago, proponha outro no mesmo
   estilo seco. Sem valor, estágio ou investidores no resumo.
6. Data e recência: a rodada foi anunciada pela primeira vez dentro de <período>?
   Anúncio antigo noticiado de novo, ou extensão de rodada já coberta = reciclada.
7. Relevância: é uma rodada de VC/startup de verdade? Rumor ("em negociação", fonte
   anônima, não fechada), empresa grande, estúdio, M&A e não-rodada saem.
8. Duplicata: a mesma rodada duas vezes no bloco.

Ferramentas: carregue as de web com ToolSearch ("select:WebSearch,WebFetch" e
"exa"). Paywall (Bloomberg, The Information): use a cobertura secundária.
Somente leitura: não altere banco nem arquivos do repo.

Grave <R>/review<k>.json, um array com um objeto por item:
{"n": <int>, "company": "...", "verdict": "ok"|"fix"|"drop", "drop_reason": "...",
 "issues": ["cada afirmação errada, curta"],
 "corrected": {só os campos que mudam, com os nomes do banco: "company_name",
   "amount_original", "currency", "amount_usd", "stage" (pre_seed|seed|series_a..f|
   growth|late|pre_ipo|null), "company_country" (ISO2), "sector_detail", "leads"
   (lista de nomes), "valuation_usd" (número ou null), "summary", "announced_at"
   (YYYY-MM-DD)},
 "evidence": ["url", ...], "confidence": "high"|"medium"|"low"}
Valor mudou em moeda que não é USD: mande `amount_usd` convertido também.
"drop" = não entra (não é rodada de VC, rumor, reciclada, duplicata). "fix" = entra
corrigido. Sem confirmar, diga em issues e baixe a confiança; não chute. Ao menos
uma URL de evidência por item.

Mensagem final: resumo de até 15 linhas com os drops e as correções mais
importantes. O arquivo é a entrega.
```

## Fase 2 — consolidar, montar, anexar

Espere os 5 `review<k>.json`. Revisor que voltou sem o arquivo ou com item faltando:
redispare só aquele bloco.

**Consolide em `$R/final.json`** (um objeto por `n`, mesmo esquema do review). Você
é o editor, não um somador:

- Confira você mesmo, com busca, todo `drop` e todo item de confiança `low`, as
  duplicatas entre blocos que você anotou e os itens em que o revisor só repetiu a
  `verification` do banco sem buscar nada novo.
- Duplicata: fica a linha com o nome real da empresa e os dados certos; a outra é
  `drop`.
- Reciclagem: rodada anunciada antes da janela sai, mesmo que a notícia seja nova.
- Rodada sem valor e com um investidor só, investimento estratégico com opção de
  compra, ou fonte única que é furo de veículo: entram, mas vão na lista de
  decisões do Gui na roll-up.

Monte e confira:

```bash
node "$REPO/pipeline/tools/rounds/build.mjs" <DATE> "$R/items.json" "$R/final.json" "$R/section.json" "$R/preview.md"
```

Imprime a manchete recalculada (total, contagem e Brasil já sem os drops). Leia o
`preview.md` inteiro antes de anexar: país, setor, Liderança e resumo de cada item.

**Anexe ao draft**, pull → append → push, e confira no servidor:

```bash
cd "$REPO" && python3 pipeline/tools/substack_mirror.py pull --dir "$D" \
  && python3 pipeline/tools/rounds/append.py "$D/substack-body.json" "$R/section.json" \
  && python3 pipeline/tools/substack_mirror.py push --dir "$D" \
  && python3 pipeline/tools/substack_mirror.py pull --dir "$D" --file "$R/after.json"
```

Em `after.json`: a seção existe uma vez, há um só nó `paywall`, e a contagem de
`captionedImage` é a mesma de antes do push. O `append.py` troca a seção se ela já
existe, então rodar de novo não duplica.

Sem `.substack-draft-id` (rodada sozinha num dia sem draft) → pare depois do
`build.mjs` e entregue o `preview.md`.

## Saída

```
Rodadas: <manchete do job> → <manchete final> (<k> fora, <m> corrigidas)
```

Depois, uma linha por item que saiu (empresa: motivo) e uma por correção que muda
o que o leitor lê (empresa: antes → depois). Por último, **Decisões para você**:
os itens que entraram com ressalva (veja a Fase 2). Avise para fechar abas abertas
do editor antes de abrir o draft: aba velha sobrescreve o push.
