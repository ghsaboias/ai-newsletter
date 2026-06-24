#!/usr/bin/env python3
"""Build a Substack draft that demonstrates every JSON-constructable format,
each under a heading with a live example. POSTs to the publication."""
import os, json, urllib.request

def creds():
    sid=os.environ.get("SUBSTACK_SID"); host=os.environ.get("SUBSTACK_PUB_HOST")
    if not(sid and host):
        for line in open(os.path.expanduser("~/daily-journal-platform/.env.local")):
            line=line.strip()
            if line.startswith("SUBSTACK_SID=") and not sid: sid=line.split("=",1)[1]
            elif line.startswith("SUBSTACK_PUB_HOST=") and not host: host=line.split("=",1)[1]
    return sid,host

def t(text, *marks):
    n={"type":"text","text":text}
    if marks: n["marks"]=[m if isinstance(m,dict) else {"type":m} for m in marks]
    return n
def link(text,href): return t(text,{"type":"link","attrs":{"href":href,"target":"_blank","rel":"noopener noreferrer nofollow","class":None}})
def p(*content): return {"type":"paragraph","attrs":{"textAlign":None},"content":list(content)}
def h(level,text): return {"type":"heading","attrs":{"level":level},"content":[t(text)]}
def li(*content): return {"type":"list_item","content":[{"type":"paragraph","attrs":{"textAlign":None},"content":list(content)}]}

doc={"type":"doc","content":[
 p(t("Cada formato abaixo aparece sob um título com um exemplo ao vivo. Referência completa de JSON em "), link("substack_inventory.md","https://dailyjournal.news"), t(".")),

 h(2,"Títulos (Estilo ▾)"),
 h(3,"Título nível 3"),
 h(4,"Título nível 4"),
 p(t("Texto normal de parágrafo para contraste.")),

 h(2,"Marcações inline"),
 p(t("Este parágrafo combina "), t("negrito","strong"), t(", "), t("itálico","em"),
   t(", "), t("negrito itálico","strong","em"), t(", "), link("um link","https://dailyjournal.news"),
   t(", "), t("tachado","strikethrough"), t(", "), t("código inline","code"),
   t(", sobrescrito x"), t("2","superscript"), t(" e subscrito H"), t("2","subscript"), t("O.")),

 h(2,"Lista com marcadores"),
 {"type":"bullet_list","content":[
   li(t("Primeiro item da lista.")),
   li(t("Segundo item, com "), t("ênfase","strong"), t(".")),
   li(t("Terceiro item.")) ]},

 h(2,"Lista numerada"),
 {"type":"ordered_list","attrs":{"start":1,"type":None,"order":1},"content":[
   li(t("Passo um.")), li(t("Passo dois.")), li(t("Passo três.")) ]},

 h(2,"Citação / pull-quote"),
 {"type":"blockquote","content":[ p(t("“Uma frase de destaque, isolada do corpo do texto.”")) ]},

 h(2,"Bloco de destaque (callout)"),
 {"type":"calloutBlock","content":[
   p(t("Manchete da história: ","strong"), t("resumo de uma a duas linhas que funciona como caixa de chamada — é o bloco usado hoje no teaser de assinantes.")) ]},

 h(2,"Divisória"),
 p(t("Antes da divisória.")),
 {"type":"horizontal_rule"},
 p(t("Depois da divisória.")),

 h(2,"Botão (CTA)"),
 {"type":"button","attrs":{"url":"%%checkout_url%%","text":"Assine agora","action":None,"class":None}},
 {"type":"button","attrs":{"url":"https://dailyjournal.news","text":"Visite o site","action":None,"class":None}},

 h(2,"Nota de rodapé"),
 p(t("Uma afirmação que cita uma fonte sem poluir o texto com link inline"), {"type":"footnoteAnchor","attrs":{"number":1}}, t(".")),

 h(2,"Bloco de código"),
 {"type":"highlighted_code_block","attrs":{"language":"plaintext","nodeId":"inv-code-1"},"content":[t("$ pipeline/draft.sh 2026-06-23")]},

 h(2,"LaTeX"),
 {"type":"latex_block","attrs":{"persistentExpression":"E = mc^2","id":"INVLATEX01"}},

 h(2,"Poesia (espaçamento preservado)"),
 {"type":"preformatted_text_block","attrs":{"params":"","language":"en"},"content":[t("linha um\n  linha dois indentada\nlinha três")]},

 h(2,"Não construtíveis só com JSON"),
 p(t("Imagem ("), t("captionedImage","code"), t("): exige upload via /api/v1/image. Enquete ("),
   t("poll","code"), t("): exige criar a entidade server-side e referenciar o id. Gráfico financeiro: vira um "),
   t("captionedImage","code"), t(" (TradingView renderiza PNG). Ver substack_inventory.md §2 e §8.")),

 h(2,"Mural de pagamento (paywall)"),
 p(t("O conteúdo abaixo desta linha fica só para assinantes.")),
 {"type":"paywall"},
 p(t("Parágrafo pós-paywall (visível apenas para assinantes).")),

 # footnote bodies live as top-level blocks; Substack renders them at the end
 {"type":"footnote","attrs":{"number":1},"content":[ p(t("Fonte: comunicado oficial, 23/jun/2026.")) ]},
]}

sid,host=creds()
payload={"draft_title":"ZZ — DRAFT INVENTÁRIO DE FORMATOS (não publicar)",
 "draft_subtitle":"Um exemplo ao vivo de cada formato do editor","draft_body":json.dumps(doc,ensure_ascii=False),
 "draft_bylines":[{"id":473611573}],"draft_section_id":None,"audience":"only_paid","type":"newsletter"}
req=urllib.request.Request(f"https://{host}/api/v1/drafts",data=json.dumps(payload).encode(),method="POST",
 headers={"Content-Type":"application/json","Cookie":f"substack.sid={sid}","User-Agent":"Mozilla/5.0"})
r=json.loads(urllib.request.urlopen(req).read())
print("DRAFT_ID:",r.get("id"))
print("URL: https://%s/publish/post/%s"%(host,r.get("id")))
