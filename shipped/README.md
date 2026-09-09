# shipped/ — o que foi de fato publicado no Substack

Ground truth da revisão humana. Uma edição por data:

- `<date>.json`        post publicado (`sstats post <id> --json`): title, subtitle, body_html, stats
- `<date>.md`          title + subtitle + body em markdown (pandoc) — é o que se diffa contra `pipeline/output/ai/<date>/edition-final.md`
- `<date>.body.json`   doc ProseMirror (`substack_mirror.py pull`), único lugar onde o bloco de teasers sobrevive
- `<date>.teasers.md`  bloco "Abaixo, apenas para assinantes" como publicado (vazio em quarta = edição gratuita)
- `delta/<date>.json`  diff estruturado local → publicado; `delta/REPORT.md` agrega; `delta/PROPOSAL.md` conclusões

```bash
./shipped/fetch.sh            # idempotente; só baixa o que falta (post id = <dir>/.substack-draft-id)
python3 shipped/analyze.py    # ou: analyze.py 2026-09-07
```
