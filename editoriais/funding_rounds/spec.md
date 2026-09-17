# Funding rounds semanal — spec (17 set 2026)

Fonte de verdade: `deals`. Formato: F6S (`example.md`). Canal: Slack `#feat-newsletter` (C0AH9DQPR1C). Cadência: segunda 9:00 BRT.

## Requisitos (cada um com dono)

| # | requisito | quem pediu | como se garante |
|---|---|---|---|
| R1 | Rodada velha não volta como nova | Vini/Gui, checkpoint 16 set | dedup determinístico + portão retrospectivo do `deals`; a semana é por `first_news_at`, não por data da notícia; linha com flag `retrospective` fica fora |
| R2 | Só rodada fechada. "Negocia", "busca", "planeja" ficam fora | Gui, 17 set | prompt do extrator já exclui; medido 5/5 rejeitados |
| R3 | Newsletter só `vc_round` | Gui, 17 set | filtro na query. Site continua com todos os tipos |
| R4 | Formato F6S: agrupado por estágio; valor, empresa, país, setor, investidores | Gui, 17 set | `lib/deals/weekly-digest.ts` |
| R5 | Um sistema só | Gui, 17 set | job da Pi apagado; tudo lê `deals` |
| R6 | Toda entrada linka pro DJ | notas do checkpoint (CTA) | link da `primary_news` |

## Fluxo

```
articles / newsletters / DJ newsletter / X  →  news            (existe, não muda)
news → regex → Gemini → portões → deals / deal_parties        (existe; 3 ajustes)
juiz (gemini-3.1-flash-lite) lê registro + notícia → keep/reject  (novo, 17 set)
segunda 12:00 UTC: cron lê deals → formata → posta no Slack   (novo)
```

Sem LLM na etapa nova. O formato é determinístico a partir das colunas.

## Query da semana

```sql
select d.*, n.slug as news_slug
from deals d join news n on n.id = d.primary_news_id
where d.deal_type = 'vc_round'
  and d.status = 'published'
  and d.first_news_at >= now() - interval '7 days'
  and not (d.review_flags ? 'retrospective')
order by d.stage nulls last, d.amount_usd desc nulls last
```

Partes: `deal_parties` com `role in ('lead','investor')`, lead primeiro.

## Formato (pt-BR)

```
*Rodadas da semana — 10 set a 17 set*
US$ 12,5 bi em 82 rodadas · 7 no Brasil · 8 sem valor divulgado

*Pre-seed* (10)
• US$ 2 mi — *Boxd* — Países Baixos — IA — Líder: BlueYard Capital — OVNI Capital, Antler e 2 mais — <link|DJ>
• US$ 2 mi — *Orbits* — IA — Líder: a16z — <link|DJ>
*Seed* (14)
• ...
*Série A* (…)
*Estágio não informado* (…)
```

Segmentos separados por " — ", omitidos quando vazios: valor (moeda original,
uma casa decimal; "valor não divulgado"), empresa, país (nome, sem bandeira —
decisão de 17 set), setor, "Líder: X", demais investidores (teto de 3 nomes
somando lead e demais, "e N mais"), link da notícia no DJ. Ordem dentro do
grupo: USD desc, sem valor por último.

Mapa F6S → deals:

| F6S | deals | falta |
|---|---|---|
| grupo por estágio | `stage` (pre_seed … pre_ipo) | 22 de 71 sem stage na última semana → grupo "não informado" |
| `$5m for Tellia` | `amount_original` + `currency`; sem valor → "valor não divulgado" | 7 de 71 sem USD |
| `from Paris, France` | `company_country` | cidade não existe; fica só país. 22 de 71 sem país |
| `(Agriculture, AgriTech)` | `sector` | 0 faltando |
| `with funding from X, Y and 2 more` | `deal_parties`: "Líder: X" e depois investors, "e N mais" acima de 3 | 19 de 71 sem lead, 11 sem parte nenhuma |
| cabeçalho `$2.5bn in 5.6k rounds` | `sum(amount_usd)`, `count(*)`, `count(is_brazil)` | — |

Cobertura de stage/país/lead é problema do extrator, não do digest. Entra no passo 3 abaixo, sem bloquear.

## Mudanças, em ordem

1. **Feito.** RPC `find_deal_candidate_news` deixa de excluir news demovidas (migração `20260917180000`).
2. **Feito (commit 2d3177c8).** `lib/deals/candidates.ts`: regex ganha empréstimo, financia+valor, aporta, investe+valor, emite, precifica, letras financeiras, AT1, estreia em bolsa, listagem, recebe+valor. Teste em `lib/__tests__/deals-candidates.test.ts` com as 11 manchetes perdidas de 7–14 set. Medido: 341 → ~420 news/semana pro LLM.
3. **Feito.** `lib/ai/prompts.ts`: excluir capex próprio e dívida soberana (falsos positivos Sabesp e Senegal). Pedir `stage`, `company_country` e lead sempre que o texto permitir.
4. **Feito 17 set** (105 chamadas, 16 deals novos, 9 merges, 2 timeouts no portão retrospectivo). `bun run scripts/backfill-deals.ts --days 10` pra fechar o buraco (Lightfield etc.).
5. **Feito. Primeiro post 17 set 18:27 BRT, 82 rodadas.** Novo `lib/deals/weekly-digest.ts` (query + formatação, função pura, testada) e `app/api/cron/deals-weekly-slack/route.ts`; entrada em `vercel.json` `0 12 * * 1`; `SLACK_BOT_TOKEN` (ou webhook do canal) no env da Vercel. Primeira execução manual com Bearer `$CRON_SECRET`.
6. **Feito (michael-slack d1746ee, serviço reiniciado com 46 jobs).** Apagado `pi:~/michael-slack/src/jobs/weekly-funding-rounds.ts`.

## Juiz (17 set, tarde)

Fila de revisão humana morreu: ninguém olhava. Segundo modelo decide (`lib/ai/deal-judge.ts`), benchmark em `judge-bench.md`. Gui escolheu gemini-3.1-flash-lite.

## Depois (fora deste MVP)

- Newsletter: skill `newsletter-draft` chama a mesma função e cola o bloco atrás da paywall.
- Stories/gráfico por país: mesma query, `group by company_country`.
- Classificador (Jev) no lugar do regex.
- Cidade da empresa, se o Vini fizer questão.

## Decisões em aberto

| decisão | default se ninguém falar |
|---|---|
| Idioma do post | pt-BR |
| Horário | Segunda 9h BRT (Gui, 17 set) |
| Onde roda | Vercel, no repo da plataforma. Michael-slack só tem a credencial; o dado e o código ficam juntos |
| Rodada sem valor entra? | Entra, no fim do grupo de estágio, como "valor não divulgado" |
| Ordem dentro do grupo | Valor USD desc; sem valor por último |
