# Newsletter Diária — Geração

O usuário vai fornecer uma **data-alvo**. Escreva o artigo do dia em português brasileiro usando o arquivo de pesquisa como fonte. Não pesquise na web. Todos os fatos e links devem vir de `{day_dir}/research-slim.json`.

Leia o arquivo de pesquisa primeiro. Salve o resultado em `{day_dir}/pt.md`.

## Edições Anteriores — Não Repetir

Antes de escrever, **leia as 3 últimas edições** (caminhos listados abaixo) para entender o que o leitor recorrente já viu. Leia as três na íntegra — sem pular nenhuma. Se houver menos de 3 disponíveis, leia todas as que existirem.

{prev_editions}

Continuidade é legítima — desenvolvimentos reais de histórias em andamento devem aparecer. O que evitar:

1. **Story recontada sem ângulo novo.** Se a notícia já apareceu, lidere pelo desenvolvimento (o que mudou hoje), não pela recapitulação. Se não há ângulo novo, corte a notícia.
2. **Phrasings-fórmula.** Construções tipo *"X levantou US$Y em série Z liderada por W"*, *"A [empresa], fabricante [americana/chinesa] de [chips/IA] para..."*, *"Em paralelo,"*, *"Separadamente,"* — varie a estrutura ou abra pelo ator/fato concreto.
3. **Framings repetidos.** Se a mesma empresa lidera o mesmo bloco temático em 3 edições seguidas, reorganize. Se um país aparece sempre em seção isolada (ex: "drones russos"), absorva no fluxo da geopolítica.

Quando em dúvida sobre uma construção, releia o trecho equivalente da edição de ontem.

## Estrutura

### Título
`[Tech] - Bem-vindo(a) a [Dia] de [Mês] de [Ano]`

### Linha de abertura
Uma frase que apresenta e resume o dia. Máximo ~180 caracteres — serve também como subtítulo no Substack. Use abreviações (US$2bi, 5GW) para caber. 3 ou 4 frases sobre eventos diferentes, separadas por ";".

### Corpo
5-8 parágrafos temáticos. Cada parágrafo:
1. Começa com um rótulo curto em negrito (1-3 palavras) + ponto, inline no corpo do parágrafo. Exemplos usados em edições recentes: `**Modelos & agentes.**`, `**Big techs.**`, `**Semicondutores.**`, `**Energia & data centers.**`, `**Geopolítica.**`, `**Biotech.**`, `**Biotech.**`. O rótulo emerge do agrupamento do dia — se a pesquisa puxa pra outro tema, nomeie de acordo; não force encaixe nos exemplos.
2. Agrupe notícias relacionadas (geralmente 2-4) com **links inline nas frases-chave**. Se o agrupamento reúne dois arcos distintos, quebre (ver "Tamanho do parágrafo")

As notícias dentro de um parágrafo devem se relacionar entre si. Priorize agrupamentos que a pesquisa sustenta naturalmente — tipicamente IA/infraestrutura, hardware/semicondutores, geopolítica e biotecnologia. Se um domínio não tem notícias na pesquisa, pule. Não force cobertura.

### Bullets — seções com 3+ itens paralelos

Quando uma seção reúne 3 ou mais itens discretos do mesmo tipo (3 lançamentos numa conferência, 3 captações no dia), use bullets, não parágrafo corrido. Mantém o rótulo de seção em negrito; abaixo, uma frase-lead curta com dois-pontos ou os bullets direto. Cada bullet abre com o **nome próprio** em negrito (`**SpaceX.**`, `**Majorana 2.**`), não uma categoria. O corpo não repete o nome; o link inline vai na descrição. Menos de 3 itens: parágrafo normal.

### Tamanho do parágrafo — um arco por parágrafo

Cada parágrafo cobre **um arco**: uma história e suas ramificações diretas. O gatilho de quebra é qualitativo, não de comprimento — um arco denso (uma captação com todas as métricas, um ensaio de vacina) fica inteiro mesmo com 6-8 frases. Mas quando um bloco com rótulo reúne **dois eventos que se sustentam sozinhos** — ainda que sob o mesmo ator, tema ou rótulo — dê um parágrafo a cada um.

A continuação **não recebe novo rótulo em negrito** (segue sob o do bloco anterior). Abra-a por uma âncora concreta que reposicione o leitor:

- Temporal (honestidade de frescor; nunca sugira simultaneidade entre datas distintas): `Ainda ontem,`, `Hoje em Londres,`, `Separadamente,`
- Geográfica: `Em Pequim,`, `Na Ucrânia,`, `Em Utah,`
- Ator: `O governador de Illinois, JB Pritzker,`

Quando o parágrafo introduz um conjunto ("duas frentes", "três apostas"), feche-o com uma frase-placa curta que anuncia a separação e dê um parágrafo a cada membro — ou, se forem 3+ itens paralelos do mesmo tipo, bullets (ver acima). Ex.: "Em duas frentes estaduais, autoridades agem contra os data centers." → um parágrafo para Illinois, outro para Utah.

## Voz e Tom

- **Convicção** — a aceleração é tratada como fato consumado, não como aspiração
- **Denso e específico** — números exatos: percentuais, valores em dólar, prazos, classificações
- **Agrupamento temático** — cada parágrafo reúne notícias relacionadas em ordem de relevância. Continuidade entre edições é implícita: destaque o ângulo novo; leitor recorrente reconhece o arco.
- **Aberturas concretas** — abra cada frase pelo ator concreto ou por um marco temporal/causal específico. Ex: "A Microsoft fechou...", "Em Bruxelas, a Comissão...", "Depois da suspensão no Reino Unido...".
- **Só o que está na pesquisa** — todas as afirmações vêm de research-slim.json

**Exemplos de frases que funcionam** (de edições finalizadas):

- "A TSMC fechou o primeiro trimestre com lucro recorde de cerca de US$17,8 bilhões, 58% acima do mesmo trimestre de 2025, e margem bruta de 66,2%."
- "A Eli Lilly, farmacêutica americana líder em remédios para diabetes e obesidade, fechou a compra da biotech CrossBridge Bio, de Houston, por até US$300 milhões."
- "As ações da Intel subiram 53% em cerca de duas semanas, a maior alta da história da empresa, acrescentando mais de US$100 bilhões ao valor de mercado."

## Acessibilidade — Escreva para Não-Especialistas

O público é educado, mas não técnico. Toda frase deve ser clara para alguém que não trabalha com tecnologia, finanças ou defesa. Se uma empresa, organização ou pessoa não é amplamente conhecida, adicione uma oração descritiva. Use o campo `entities` nos dados de pesquisa para identificar atores. Consulte `key_facts` para contexto sobre o que fazem.

- ✅ `a FANUC, maior fabricante de robôs industriais do Japão`
- ✅ `Karen Hao, jornalista de tecnologia do Wall Street Journal`
- ✅ `o Drift Protocol, plataforma de derivativos na blockchain Solana`
- ✅ `a Shimizu, construtora japonesa`
- ❌ `a FANUC colabora com a NVIDIA` (leitor não sabe o que é a FANUC)
- ❌ `Karen Hao publicou...` (leitor não sabe quem ela é)

Nomes que não precisam de explicação: OpenAI, Google, Microsoft, Apple, Meta, Amazon, Tesla, Nvidia, Samsung, SpaceX, NASA, Elon Musk, Sam Altman, Trump.

### Simplifique termos técnicos

Nunca assuma que o leitor conhece jargão. Reescreva ou adicione contexto inline:

- ✅ `máquinas de litografia ultravioleta extrema (EUV)` na primeira menção, depois `EUV`
- ✅ `um recurso da Solana que permite pré-assinar transações sem prazo de validade`
- ✅ `certificação de segurança de dados (SOC 2)`
- ❌ `DRAM 1c`, `HBM4`, `plataforma Rubin` (sem significado para não-especialistas)
- ❌ `durable nonce`, `dual listing`, `run rate`, `pregões`, `rali` (jargão em inglês ou de mercados sem contexto — explique em uma oração ou use linguagem corrente)

Se um conceito técnico não cabe em uma oração explicativa, simplifique para a consequência ("chips de memória mais rápidos") ou corte.

### Regras de formatação

- **Moeda**: sempre `US$` — nunca `$` sozinho, nunca `¥`, `€`, `₩` ou "trilhões de wons". Converta moedas estrangeiras para US$ usando os dados de pesquisa.
- **Aproximação**: `por volta de`, `cerca de`, `aproximadamente` — nunca `~`
- **Tempo e abreviações**: `quarto trimestre`, não `Q4`. `primeiro semestre`, não `H1`. `ano contra ano` → `em relação ao mesmo período do ano anterior` ou simplesmente declare os dois números. Para datas dos últimos 14 dias, prefira `ontem`, `semana passada`, `mês passado` a dias da semana. Taxas de crescimento sempre vêm com o período ancorado: `subiu 14% em 12 meses`, não `subiu 14%`.
- **Veículos de imprensa**: `Wall Street Journal`, não `WSJ`. `New York Times`, não `NYT`. Por extenso na primeira menção.
- **Unidades**: quilômetros, não milhas. Celsius, não Fahrenheit. Converta se a fonte usar sistema imperial.
- **Palavras em inglês**: use equivalentes em português quando existirem. `diferença`, não `gap`. `delator`, não `whistleblower`. `listagem dupla`, não `dual listing`.
- **Pontuação**: prefira ponto, dois-pontos e vírgula. Em dash (—) apenas em apostos onde vírgulas ambiguariam.

## Densidade de Links e Formatação

- **1-2 links por história** — coloque o link no fato mais curioso ou surpreendente
- Links vão na frase mais descritiva, não em "aqui" ou "isso"
- Formato: `[frase descritiva](url)` — o texto com link deve fazer sentido mesmo sem clicar
- Toda URL deve vir de `research-slim.json`. Não invente nem adivinhe URLs.

## Comprimento

Mantenha o comprimento **próximo ao das edições anteriores que você acabou de ler**, proporcional à quantidade de histórias do dia. Dia com muitas histórias importantes, texto mais longo; dia com poucas histórias, texto mais curto. Quando a pesquisa traz mais notícias do que cabem, corte as mais fracas — menos dados concretos, menos impacto, conexões mais fracas com os fios principais. Não tente mencionar tudo.

## Formato de Saída

Salve em `{day_dir}/pt.md`:

```markdown
---
date: YYYY-MM-DD
url:
title: "[Tech] - Bem-vindo(a) a [Dia] de [Mês] de [Ano]"
generated: true
language: pt-br
---

# [Tech] - Bem-vindo(a) a [Dia] de [Mês] de [Ano]

[Corpo do artigo]
```
