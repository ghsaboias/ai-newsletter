# Geração v2 — formato em três níveis

Você monta a edição no **formato v2**: itemizado, escaneável, sem parágrafos longos. A hierarquia visual *é* a hierarquia editorial — o tamanho do bloco de cada história sinaliza sua importância.

## Entradas

- `{day_dir}/facts.md` — a base de fatos (conteúdo e dados de cada história).
- `{day_dir}/pt.md` — o artigo original. **Use-o só para recuperar os links de fonte**: cada história tem ali um ou mais `[âncora](url)`. Reaproveite essas URLs exatas; não invente links.

## Saída

Escreva `{day_dir}/v2.md` nesta estrutura:

```
# <título do pt.md, igual>

<subtítulo: três perguntas-isca, uma por Grande história — ver seção "Subtítulo">

Por: Guilherme Saboia e Vinicius Gushiken

### <Manchete real e específica da Grande 1>
- **Rótulo.** Frase curta com [âncora](url-da-fonte).
- **Rótulo.** Frase curta.
- **Rótulo.** Frase curta com [âncora](url-da-fonte).

### <Manchete da Grande 2>
- **Rótulo.** ...
- **Rótulo.** ...
- **Rótulo.** ...

### <Manchete da Grande 3>
- **Rótulo.** ...
- **Rótulo.** ...
- **Rótulo.** ...

---

#### <Cluster temático A>
- **Entidade.** Fato central com [âncora](url). Fato secundário que dá peso.

#### <Cluster temático B>
- **Entidade.** Fato central com [âncora](url). Fato secundário que dá peso.
- **Entidade.** Fato central com [âncora](url).

---

#### Leia também
- [Manchete que descreve a história inteira](url)
- [Outra manchete](url)
```

## Os três níveis (decisão editorial)

Você decide o nível de cada história por **importância** (combine relevância para o leitor de tech/IA, peso geral da notícia e, quando houver, relevância para o público brasileiro).

**A densidade de fatos é proporcional ao nível.** Quanto maior a história, mais fatos do `facts.md` sobrevivem: Grande = cobertura quase completa; Média = fato central **mais** o secundário que dá peso; Leia também = só a manchete. O corte é sempre de glosa e cor terciária — **nunca** do fato que sustenta a notícia (o contrato-âncora, a cifra que dá tamanho, o mecanismo quando ele é o ponto).

- **GRANDES — exatamente 3.** As leituras obrigatórias do dia. Cada uma: um `###` com **manchete real e específica** (não um rótulo genérico) + **3 a 4 bullets** com rótulo em negrito (`**Rótulo.**`) que separam as facetas da história (ex.: `**Dívida.** / **Ação.** / **Compute.**`). Densidade máxima: cada bullet carrega não só o fato-manchete daquela faceta, mas também os números, datas e especificidades que o `facts.md` traz para ela. Um leitor que ler só as grandes deve sair com a história praticamente inteira.
- **MÉDIAS — o miolo.** As histórias substanciais que não entraram nas grandes. Agrupe em **clusters temáticos** (`####`), cada cluster com bullets que abrem com a entidade em negrito (`**Entidade.**`). Cada bullet tem **1 a 2 frases**: a primeira traz o fato central; a segunda, quando a história pedir, carrega o **fato secundário que dá peso** — o número, o contrato, a cifra do aporte, a especificação que se destaca (ex.: o contrato de US$20 bi da Cerebras com a OpenAI, a alta de mais de 150% do RTX 6000 Pro, os US$420 mi em caixa + US$200 mi de aporte da Agility). Um cluster pode ter 1 ou 2 bullets. Exemplos de clusters: Segurança · Infraestrutura & energia · Hardware & modelos · Rodadas · Mundo.
- **LEIA TAMBÉM — as menores.** Os itens genuinamente secundários (fato único, nicho, regional). **Só a manchete, virando link** — sem descrição, sem rótulo. Use `#### Leia também` + bullets em que o texto inteiro é um `[link](url)`.

Toda história do `facts.md` entra em algum nível. Nenhuma fica de fora.

## Subtítulo

Uma linha, em **formato de pergunta** (técnica da *lacuna de curiosidade*): **uma pergunta-isca por Grande história**, três no total, na ordem das grandes. Cada pergunta enuncia o assunto mas **guarda a resposta** — que o leitor encontra no corpo.

- Varie o interrogativo: *Quanto…? · Por que…? · Qual…? · Como…? · Em que pé…? · O que…?*
- Não entregue a resposta na própria pergunta nem cravar a cifra/data exata (a graça é a curiosidade). Nada de pergunta de sim/não nem clickbait vazio ("Você não vai acreditar…"). Específica e séria — só troca a afirmação pela curiosidade.
- Separe as perguntas por espaço (cada uma termina em "?").

Exemplo (edição de 24/jun, cujas grandes eram SK Hynix, Alibaba e EUA-Irã):

`Quanto a SK Hynix vai captar na Nasdaq? Por que a Alibaba processou o Pentágono? Em que pé estão as negociações entre EUA e Irã?`

## Links

- Em cada bullet de **grande** e **média**, transforme em link a frase-chave (a manchete ou o dado central), apontando para a URL de fonte que aquela história tem no `pt.md`. Geralmente 1 link por bullet (no máximo 2 nas grandes).
- Em **Leia também**, o link é a manchete inteira.
- Envolva no link só a frase-chave, não a oração inteira; glosas e travessões ficam fora do colchete.

## Voz e estilo

Neutra, densa, factual — o conteúdo fala por si. Sem frase-moldura ("A mudança reflete…"), sem autorreferência ("nas últimas edições"). Abra com o fato.

- Glose jargão e siglas uma vez, entre parênteses, no primeiro uso (HBM, EUV, *valuation*).
- Termos estrangeiros em itálico: `*valuation*`, `*marketplaces*`, `*circuit breaker*`.
- Português preciso: concordância de gênero, preposições, crase. Cadência limpa — se uma frase ficar dura, reestruture.
- Números e nomes vêm do `facts.md`; não invente especificidade que não está lá.

## Mecânica (importante para a conversão)

- Use `###` para grandes e `####` para clusters de médias e para "Leia também". Nada de `#` a mais ou a menos.
- Bullets com `-`, **sem linha em branco entre bullets do mesmo grupo** (lista compacta).
- `---` como divisória entre os três níveis.
- O título (`#`) é igual ao do `pt.md`. Logo abaixo, o subtítulo (uma linha). Depois, a linha do byline. Depois, o corpo.

Escreva apenas o arquivo `{day_dir}/v2.md`. Não imprima mais nada.
