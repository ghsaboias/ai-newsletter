# Extração de Fatos

Você decompõe o artigo finalizado da newsletter em uma **base de fatos** limpa e auditável — uma lista de fatos atômicos por história. É o mesmo formato dos arquivos `facts_*.md` de referência.

## Entrada

Leia `{day_dir}/pt.md` — o artigo PT-BR já revisado. Cada história aparece como um parágrafo (ou bloco de parágrafos) começando com um rótulo em negrito (`**Categoria.**`).

## Saída

Escreva `{day_dir}/facts.md` com esta estrutura exata:

```
# Fatos — Newsletter [Tech] <data por extenso>

## <Entidade/assunto> — <descritor curto>
- <um fato atômico por linha>
- <outro fato>

## <próxima história> — <descritor>
- ...
```

- **Título:** `# Fatos — Newsletter [Tech] <data>`, onde `<data>` é a data por extenso tirada do título do `pt.md` (ex.: "22 de Junho de 2026").
- **Uma seção `##` por história.** Use a entidade ou assunto central como cabeçalho, com um descritor curto depois de um travessão (ex.: `## SpaceX — dívida, caixa e contrato de computação`). Parágrafos consecutivos sob o mesmo tema pertencem à mesma seção.
- **Bullets `-`, um fato atômico por linha.** Quebre frases densas em fatos separados.

## Regras

1. **Preserve tudo:** todo número, valor, percentual, data, nome próprio, cargo e citação literal que aparece no `pt.md`. Não arredonde nem resuma a ponto de perder dados.
2. **Neutro e declarativo.** Sem editorializar, sem adjetivos de ênfase, sem moldura analítica.
3. **Não invente.** Use somente o que está no `pt.md`. Se um fato não está lá, não o inclua.
4. **Sem links.** A base de fatos é texto puro — não inclua URLs nem markdown de link (os links ficam no `pt.md`, que é consultado depois).
5. **Mantenha a ordem** das histórias como aparecem no `pt.md`.
6. **Cobertura completa:** toda história do `pt.md` vira uma seção. Não pule nenhuma.

Escreva apenas o arquivo `{day_dir}/facts.md`. Não imprima mais nada.
