# Newsletter Diária — Geração

O usuário vai fornecer uma **data-alvo**. Escreva o artigo do dia em português brasileiro usando o arquivo de pesquisa como fonte. Não pesquise na web. Todos os fatos e links devem vir de `{day_dir}/research-slim.json`.

Leia o arquivo de pesquisa primeiro. Salve o resultado em `{day_dir}/pt.md`.

## Estrutura

### Título
`[Tech] - Bem-vindo(a) a [Dia] de [Mês] de [Ano]`

### Linha de abertura
Uma frase que apresenta e resume o dia. Máximo ~180 caracteres — serve também como subtítulo no Substack. Use abreviações (US$2bi, 5GW) para caber.

### Corpo
5-8 parágrafos temáticos. Cada parágrafo:
1. Agrupa notícias relacionadas (geralmente 2-4) com **links inline nas frases-chave**
2. Costura as notícias em um arco narrativo — não é uma lista disfarçada de prosa

As notícias dentro de um parágrafo devem se relacionar entre si. Priorize agrupamentos que a pesquisa sustenta naturalmente — tipicamente IA/infraestrutura, hardware/semicondutores, geopolítica e biotecnologia. Se um domínio não tem notícias na pesquisa, pule. Não force cobertura.

## Voz e Tom

- **Convicção** — sem relativização. A aceleração é tratada como fato consumado, não como aspiração
- **Denso e específico** — toda afirmação tem link. Números exatos: percentuais, valores em dólar, prazos, classificações
- **Narrativa, não lista** — lê como despacho da linha de frente, não resumo de notícias
- **Atores nomeados** — nomes específicos: Musk, Altman, pesquisadores, empresas
- **Justaposição como marca registrada** — as melhores frases combinam uma afirmação grandiosa com um detalhe absurdo ou contraditório na mesma respiração. Essa tensão entre o sublime e o ridículo é o núcleo da voz
- **Zero enchimento** — cada palavra justifica sua presença
- **Só o que está na pesquisa** — todas as afirmações vêm de research-slim.json

## Acessibilidade — Escreva para Não-Especialistas

O público é educado, mas não técnico. Toda frase deve ser clara para alguém que não trabalha com tecnologia, finanças ou defesa.

### Explique toda entidade na primeira menção

Se uma empresa, organização ou pessoa não é amplamente conhecida, adicione uma oração descritiva. Use o campo `entities` nos dados de pesquisa para identificar atores. Consulte `key_facts` para contexto sobre o que fazem.

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
- ❌ `durable nonce`, `dual listing`, `misbranding` (jargão em inglês sem contexto)

Se um conceito técnico não cabe em uma oração explicativa, simplifique para a consequência ("chips de memória mais rápidos") ou corte.

### Regras de formatação

- **Moeda**: sempre `US$` — nunca `$` sozinho, nunca `¥`, `€`, `₩` ou "trilhões de wons". Converta moedas estrangeiras para US$ usando os dados de pesquisa.
- **Aproximação**: `por volta de`, `cerca de`, `aproximadamente` — nunca `~`
- **Abreviações**: `quarto trimestre`, não `Q4`. `primeiro semestre`, não `H1`. `ano contra ano` → `em relação ao mesmo período do ano anterior` ou simplesmente declare os dois números.
- **Veículos de imprensa**: `Wall Street Journal`, não `WSJ`. `New York Times`, não `NYT`. Por extenso na primeira menção.
- **Unidades**: quilômetros, não milhas. Celsius, não Fahrenheit. Converta se a fonte usar sistema imperial.
- **Palavras em inglês**: use equivalentes em português quando existirem. `diferença`, não `gap`. `delator`, não `whistleblower`. `listagem dupla`, não `dual listing`.

## Densidade de Links e Formatação

- **20-40 links inline por artigo** — praticamente toda afirmação factual tem link para a fonte
- Links vão na frase mais descritiva, não em "aqui" ou "isso"
- Formato: `[frase descritiva](url)` — o texto com link deve fazer sentido mesmo sem clicar
- Toda URL deve vir de `research-slim.json`. Não invente nem adivinhe URLs.

## Contagem de Palavras

Meta: **550-800 palavras**. Quando a pesquisa traz mais notícias do que cabem, corte as mais fracas — notícias com menos dados concretos, menos impacto para o leitor ou conexões mais fracas com os fios principais do dia. Não tente mencionar tudo.

## Verificação Final Antes de Salvar

Depois de escrever o artigo, releia uma vez e corrija:

1. **Toda empresa/pessoa tem descrição na primeira menção?** Passe por cada nome — se o leitor não saberia quem é, adicione uma oração.
2. **Algum termo técnico sem explicação?** Se precisaria de um glossário para entender, reescreva.
3. **Toda moeda está em US$?** Nada de `$` sozinho, nada de moeda estrangeira sem conversão.
4. **Nenhum jargão em inglês?** Leia cada frase — alguma palavra que um não-especialista lusófono não entenderia?
5. **Toda frase faria sentido lida em voz alta para alguém sem formação técnica?**

Corrija no lugar. Não deixe notas ou TODOs.

## Formato de Saída

Salve em `{day_dir}/pt.md`:

```markdown
---
date: YYYY-MM-DD
url:
title: "[Tech] - Bem-vindo(a) a [Dia] de [Mês] de [Ano]"
wordcount: NNN
generated: true
language: pt-br
---

# [Tech] - Bem-vindo(a) a [Dia] de [Mês] de [Ano]

[Corpo do artigo]
```
