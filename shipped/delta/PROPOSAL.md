# Proposta: tirar a revisão humana do caminho

Base: 50 edições publicadas (2026-06-29 → 2026-09-07), diff `pipeline/output/ai/<d>/edition-final.md` + `paywall-teaser.md` vs. o post publicado no Substack (`shipped/<d>.md`, `shipped/<d>.teasers.md`). Números em `shipped/delta/REPORT.md`; script `shipped/analyze.py`.

Nota de atribuição: em ~20 dessas datas há `substack_mirror.py push` nas sessões do Slack, ou seja, parte das edições foram pedidas por Gui no thread e aplicadas pelo Michael. Para o objetivo (revisão desnecessária) tanto faz quem digitou: é tudo custo de revisão.

## Resposta em uma linha

A revisão hoje é três coisas, nesta ordem: **(1) reescrever o subtítulo** (45/50 edições; 100% em setembro), **(2) podar caudas de bullet nas Médias**, sobretudo reação de mercado, estatística diária de guerra e frase interpretativa (27% dos bullets, ~70 palavras/edição), e **(3) enxugar os teasers do paywall** (36/42 edições pagas). Seleção e tiering já estão aceitos (0 tier moves, 0 histórias adicionadas, 1% de cortes fora do cluster Mundo). Logo, o alvo não é pesquisa nem hierarquia: é um **passo de edição determinístico antes do push** mais três ajustes de prompt, com métrica automática para saber se funcionou.

## O que os dados dizem

| Padrão | Medida | Onde mora hoje |
|---|---|---|
| Subtítulo reescrito | 45/50 mudaram; 23 viraram formato `Manchete A \| Manchete B \| Manchete C` (5/5 em set.); 18 mantiveram perguntas mas editadas | `generator.md` §Subtítulo (l.232) exige 3 perguntas-isca |
| Reação de mercado cortada | 18 edições; continua em 5 das 8 desde a regra de 26/08 (Irã 03/09, Fed 04/09, SK hynix 07/09, PayPal 28/08, Nvidia "ação subiu 6%" 27/08) | `generator.md` l.313 tem a regra, mas a exceção "quando a matéria É de mercado" é exatamente o que Gui corta |
| Estatística diária de guerra/Ormuz cortada | 13 spans (drones lançados/abatidos, navios no estreito, dados Kpler, incidentes IMO) | `researcher-world.md` beat l.21-25; `generator.md` Médias l.163 |
| Frase-moldura / cauda interpretativa cortada | 14 spans ("O que mudou é o status formal: a", "Não se trata de dívida oculta: são", ", o que ampliaria a diferença", ", sinal de que…", ", num movimento que equilibra…") | `generator.md` l.273 diz "sem frase-moldura" mas sem padrões concretos |
| Cluster Mundo/Economia trimado | Mundo: 23% dos bullets podados ≥5 tokens e 5% cortados; Economia/Mercados 18%/9%; demais clusters 9%/1% | mesmo lugar |
| Oração de continuidade cortada | "na véspera"→"ontem", "que informaram o acordo nesta segunda-feira", "condições já noticiadas na véspera", "O que em 27 de agosto era… virou contrato definitivo: a" | `generator.md` §Continuidade l.187 manda "marcar a continuidade numa oração curta" |
| Teasers podados | 36/42 editados; padrão único: remover o 3º/4º elemento do guarda-chuva, quase sempre o de guerra/petróleo/bolsa ("mais uma noite de ataques russos", "o petróleo no nível mais alto", "as ações de uma fabricante chinesa caem") | `paywall-teaser.md` regra 6 (l.144) permite "duas ou três orações" |
| Léxico | entrada/saída→input/output (15×), de fronteira→avançado (5×), avaliação→valuation (3×), — → vírgula (8×): **todas antes de 26/08**, exceto 1 "de fronteira" (31/08) e 1 travessão (03/09) | regra de 26/08 funcionou |
| Bullet inteiro deletado | 7 no total, 0 desde 10/08 | regra de 26/08 funcionou |
| Manchete de Grande | 12/150 editadas (verbo dramático "sequestraram"→"usam"; "de fronteira"/"topo de linha"→"mais avançados"; encurtar) | `generator.md` l.276 |

O que **não** muda na revisão: tamanho dos bullets (mediana das Médias publicadas segue em 94 palavras, vs. 97 locais), tiering, ordem, clusters, Leia também (3 cortes em 125).

## Mudanças propostas (ordem de retorno)

### 1. Subtítulo no formato do Gui — `generator.md` §Subtítulo (l.232-248) + `SKILL.md` Step 3 gate (l.259)

Trocar a regra das perguntas-isca por: **uma manchete curta por Grande, separadas por ` | `**, mediana 9 palavras, máx. ~12, sentence case, sem cifra exata; **no máximo uma das três pode ser pergunta** (31% dos segmentos publicados são perguntas, nunca as três). Exemplos publicados para colar no prompt:

- `Ads no ChatGPT batem US$1 bi anualizado | Nvidia investe US$3,5 bilhões na MediaTek | Comissão Europeia enquadra ChatGPT como mecanismo de busca muito grande`
- `Cientista-chefe da OpenAI pede desaceleração | Agentes de IA já trabalham mais que humanos na OpenAI? | Nova droga desenhada com IA tem potencial rejuvenescedor?`
- `"Bem-vindos à era da AGI", diz cofundador da OpenAI | Agentes de IA usam wiki alemã para trocar mensagens durante avaliação | Thinking Machines negocia round de US$1 bilhão`

Gate no Step 3: contar segmentos `|` == número de `###`; falha → re-rodar generator. `substack_post.py` já lê o primeiro parágrafo como subtitle (l.264-322), nada muda lá.

### 2. Passo determinístico `edit-pass` entre generator e o fan-out — novo `pipeline/tools/edit-pass.py`, chamado no `SKILL.md` Step 3 logo após `link-tokens.py expand` (l.246) e antes do gate

Roda em `edition.md` (com tokens já expandidos), então extract/paywall/ingest/push herdam o texto limpo. Cada regra imprime `APPLY`/`SKIP` como o `apply-lexicon.py`. Regras, todas com evidência acima:

- **Mercado**: apagar oração (delimitada por `;`, `, e`, `:` ou `.`) cujo sujeito é `ações|papéis|ADR|índice|Nasdaq|S&P|Dow|Kospi|Treasury|rendimento|dólar|rial` com `%` ou preço. Sem exceção por tipo de matéria (o único caso que Gui mantém é o preço-manchete de commodity, que fica por ser a primeira menção; apagar só menções subsequentes de preço da mesma commodity no bullet).
- **Estatística diária de conflito**: apagar oração com `drones|mísseis|embarcações|navios|travessias|incidentes` + número em bullets cujo rótulo é Irã/Ormuz/Ucrânia/Rússia, salvo se for a única oração do bullet.
- **Amarra temporal**: apagar `na véspera|nesta (segunda…sexta)-feira|como noticiado|noticiad[oa] na véspera|um dia após` quando é oração adverbial solta; trocar "na véspera" por "ontem" quando não dá para apagar.
- **Moldura**: apagar prefixo `^(O que mudou é…|Não se trata de…|Do outro lado…|Diferentemente de…|Se acontecer,…|Meia dúzia de) …: ` e cauda `, (o que|sinal de que|num movimento que|lida como) …$`.
- **Léxico residual**: `de fronteira`→`avançado(s)`, `topo de linha`→`mais avançado(s)`, `quadro`→`frame` (3× pós-26/08), `cargas (de trabalho)`→`workflows`, `—`→`,`. Migrar para cá o que `apply-lexicon.py` faz só quando o repetition-checker aponta.

Validar com `shipped/analyze.py` em replay: rodar o passo sobre os 50 `edition-final.md` históricos e medir quanto do delta some (meta: metade dos spans deletados).

### 3. Generator, três cortes de prompt — `generator.md`

- **§Voz e estilo l.313 (mercado)**: remover a exceção "quando a matéria É de mercado… fica por inteiro, inclusive o contexto cross-asset". Nova redação: o preço só entra quando é a manchete do bullet (rótulo Petróleo/Diesel/Bitcoin) e só uma vez; nunca ações/ADR/índice/Treasury como cauda, nem em matéria de resultados.
- **§Continuidade l.187 ("Marque a continuidade numa oração curta")**: rebaixar de regra a permissão. Abrir pelo fato novo basta; a oração "na véspera/um dia após" só quando o número mudou e a relação é o ponto. Gui corta a amarra quase sempre que ela aparece.
- **§Os três níveis, MÉDIAS l.163**: adicionar o teste do terceiro fato: a segunda frase carrega **um** fato secundário; o terceiro (recorde/superlativo explicativo, "primeiro processo de classe angstrom", "melhor resultado do partido em qualquer eleição", "sem converter a luz em sinais elétricos") sai. E: no cluster Mundo, item recorrente (Irã, Ormuz, Ucrânia, petróleo) só entra como Média se houver **evento discreto datado**; recap de preço/tráfego/ataques noturnos vai para Leia também ou some. Isto corta a maior fonte de poda (23% do cluster) e 10 das 21 histórias cortadas.
- **§Manchetes l.276**: acrescentar "sequestrar/invadir" à lista de verbos a evitar quando o fato é uso/acesso; banir "de fronteira" e "topo de linha" também em manchete.

### 4. Teasers — `paywall-teaser.md` regra 6 (l.144) e §Processo (l.184)

- Cada guarda-chuva cobre **duas** histórias (três só quando são espelho uma da outra). Gui removeu o 3º/4º elemento em 20 das 26 edições editadas no formato atual.
- Nunca tease o cluster Mundo com item de guerra/petróleo/bolsa; o teaser `**Mundo.**` fica com 1-2 eventos discretos (sanção, decisão judicial, eleição). "Mais uma noite de ataques russos", "o petróleo no nível mais alto" e "as ações caem" foram cortados todas as vezes.
- Sem qualificador de recência/ranking ("o lançamento de fronteira da semana", "cruza uma marca redonda").

### 5. Pesquisa: cortar a fonte — `researcher-world.md` l.23-25

Trocar "Markets: major equity/commodity/crypto moves tied to news events" e "oil/energy prices" por: cobrir mercado só quando o movimento **é** o evento (recorde, circuit breaker, IPO). Não gerar item diário de preço de petróleo/Brent, tráfego em Ormuz ou contagem de drones; conflito entra só por evento discreto (ataque a alvo novo, acordo, sanção, decisão). Isso evita que o generator tenha de rebaixar/podar depois.

### 6. Fechar o loop: medir a cada publicação — `shipped/` + job no michael-slack

- `shipped/fetch.sh` + `shipped/analyze.py <date>` viram passo pós-publicação (job em `~/michael-slack/src/jobs/`, ou trailing step do `/newsletter-recs` que já roda depois do push): posta no thread a linha `sub=… bedit=n/N market=… teaser=…` da edição do dia. É o KPI de "revisão necessária": meta = `sub=unchanged`, `bedit ≤ 10%`, `teaser=unchanged`.
- Apontar `evals/tools/score.py` para `shipped/<date>.md` como ground truth (hoje usa `evals/dataset/<date>/published-body.json`, que para em 25/08 e não fecha aspas curvas, cf. memória).
- Adicionar `shipped/*.json` e `shipped/*.body.json` ao `.gitignore` (≈100 KB por dia de HTML e ProseMirror; os `.md` e `.teasers.md` são o que vale versionar).

## O que não mexer

- Tiering, número de Grandes, clusters, Leia também: aceitos como estão.
- Regra de bullet inteiro (Ressalva/Múltiplo/Contexto) e léxico de 26/08: já convergiram, não retocar.
- Tamanho dos bullets: Gui não encurta por orçamento de palavras; qualquer "máx. N palavras" no prompt vai cortar coisa que ele mantém.

## Sequência sugerida

1. (#1) subtítulo: só prompt, zero risco, elimina o item nº 1 já amanhã.
2. (#2) `edit-pass.py`: uma tarde, validado em replay contra os 50 diffs antes de entrar no fluxo.
3. (#3, #4, #5) prompts: uma sessão nova para os agentes carregarem (memória: edições em `.claude/agents/*.md` só valem em sessão nova).
4. (#6) job de medição: para saber em uma semana se `bedit` caiu de 27% para perto de 10%.
