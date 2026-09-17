# Juiz de deals — benchmark (17 set 2026)

Pergunta: qual modelo substitui a fila de revisão humana de /admin/deals? O juiz recebe o registro extraído + a notícia inteira e devolve keep/reject, tipo corrigido, stage e se o valor é teto.

Dataset: 84 deals dos últimos 30 dias (top 20 por valor, 9 aleatórios por tipo, todos os `review`/`rejected`, e os casos do post de 17 set). Rótulos meus, lendo cada notícia: 60 keep, 24 reject. `judge-bench/labels.json` tem a nota de cada um. Script: `daily-journal-platform/scripts/bench-deal-judge.ts`.

| modelo | acurácia | precisão (reject) | recall (reject) | rejeitou errado | deixou passar | tipo certo | p50 | US$/chamada | US$/semana (130 deals) |
|---|---|---|---|---|---|---|---|---|---|
| gemini-3.1-flash-lite (extrator atual) | 0.893 | 0.889 | 0.696 | 2 | 7 | 0.966 | 1,7 s | 0.00046 | 0.06 |
| **gemini-3.5-flash-lite** | **0.929** | **0.905** | 0.826 | 2 | 4 | 1.000 | **1,5 s** | 0.00059 | 0.08 |
| gemini-3.8-flash | 0.917 | 0.808 | **0.913** | 5 | 2 | 0.982 | 3,5 s | 0.00207 | 0.27 |
| gemini-3.1-pro-preview | 0.929 | 0.870 | 0.870 | 3 | 3 | 1.000 | 5,3 s | 0.0079 | 1.03 |
| grok-4.3 | 0.857 | 0.720 | 0.783 | 7 | 5 | 1.000 | 5,2 s | 0.00297 | 0.39 |

Custo = tokens × preço público da OpenRouter (1.340 tokens de entrada por chamada; os modelos com raciocínio gastam 200–450 tokens a mais na saída). Todos cabem em menos de US$ 1/semana; custo não decide.

## O que os erros dizem

- **Todos deixaram passar ACME** ("investimento de até US$ 600 mi" da Brookfield) e **Telecom Italia** (adesão a OPA em curso). O primeiro é o caso que o portão determinístico de teto (`hasAmountCeiling`) já pega; o segundo precisa de uma linha no prompt: adesão/aceitação de OPA não é fechamento.
- **Mechanize** (Google "finalizou" acqui-hire de "mais de US$ 1,5 bi", confirmado por LinkedIn) passou em 4 de 5. Rótulo discutível; a notícia afirma conclusão.
- Os "rejeitou errado" são quase todos ambiguidade do meu rótulo, não erro do modelo: Atlantic Aviation (US$ 10 bi é valuation, não preço — o modelo tem razão), USI (oferta de dívida iniciada, M&A é contexto), Excelland (estreia sem valor). Grok e o Pro rejeitam por partes erradas (Crux AI, Empirik, Crypto.com): correto em rigor, ruim para o feed.
- 3.8-flash é o mais rigoroso (2 passaram) ao custo de 5 rejeições a mais; a maioria dessas são os casos ambíguos acima.

## Decisão proposta

`google/gemini-3.5-flash-lite` como juiz de todo deal extraído, antes de gravar status. Sem fila: keep → published, reject → rejected (com `reason` gravado). Mais rápido, mais barato e mais preciso que o Pro; recall 0.83 sobe com as duas linhas de prompt acima e com o portão de teto rejeitando em vez de capar.

Se quiser recall acima de precisão: rodar 3.5-flash-lite e 3.8-flash e rejeitar quando qualquer um rejeitar. No dataset: recall 0.96, precisão ~0.79 (7 rejeições erradas em 84). Custo somado US$ 0.35/semana.

O que fica de fora do juiz: dedup e retrospectiva continuam determinísticos (o juiz vê uma notícia só).
