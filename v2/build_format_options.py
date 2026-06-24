#!/usr/bin/env python3
"""Build 3 restructured-format Substack drafts from the 2026-06-23 edition.
Same content, three different format strategies. Format-only experiment."""
import os, json, urllib.request

def creds():
    sid=os.environ.get("SUBSTACK_SID"); host=os.environ.get("SUBSTACK_PUB_HOST")
    if not(sid and host):
        for line in open(os.path.expanduser("~/daily-journal-platform/.env.local")):
            line=line.strip()
            if line.startswith("SUBSTACK_SID=") and not sid: sid=line.split("=",1)[1]
            elif line.startswith("SUBSTACK_PUB_HOST=") and not host: host=line.split("=",1)[1]
    return sid,host

# ---- PM helpers ----
def t(text,*marks):
    n={"type":"text","text":text}
    if marks: n["marks"]=[m if isinstance(m,dict) else {"type":m} for m in marks]
    return n
def lk(text,href): return t(text,{"type":"link","attrs":{"href":href,"target":"_blank","rel":"noopener noreferrer nofollow","class":None}})
def para(*content): return {"type":"paragraph","attrs":{"textAlign":None},"content":list(content)}
def H(level,*content): return {"type":"heading","attrs":{"level":level},"content":list(content)}
def hr(): return {"type":"horizontal_rule"}
def callout(*paras): return {"type":"calloutBlock","content":list(paras)}
def quote(*paras): return {"type":"blockquote","content":list(paras)}
def li(*content): return {"type":"list_item","content":[para(*content)]}
def ul(*items): return {"type":"bullet_list","content":list(items)}

B = "https://dailyjournal.news/news/2026-06-23/"
L = {
 'spacex_debt':B+'spacex-capta-us20bi-em-divida-e-revela-us1008bi-em-caixa-acao-cai-16',
 'spacex_refl':B+'spacex-fecha-contrato-de-computacao-de-us63bi-com-a-reflection-ai-no-colossus-2',
 'kospi':B+'kospi-despenca-999-e-aciona-circuit-breaker-em-rota-global-de-acoes-de-tecnologi',
 'fiveeyes':B+'five-eyes-alerta-que-ia-avancada-transformara-ataques-ciberneticos-em-meses-nao',
 'openai_cyber':B+'openai-lanca-versao-completa-do-gpt-55-cyber-e-cria-patch-the-planet-com-a-trail',
 'chevron':B+'chevron-e-microsoft-firmam-acordo-de-20-anos-para-data-center-a-gas-no-oeste-do',
 'oracle':B+'oracle-corta-21-mil-vagas-em-um-ano-e-cita-adocao-de-ia-em-balanco-anual',
 'groq':B+'groq-capta-us650-mi-para-expandir-nuvem-de-inferencia-apos-acordo-com-a-nvidia',
 'modular':B+'qualcomm-negocia-compra-da-modular-por-cerca-de-us4-bilhoes',
 'appsflyer':B+'appsflyer-capta-us1-bi-de-google-meta-unity-e-moloco-a-valuation-de-us27-bi',
 'bending':B+'bending-spoons-dona-do-vimeo-fixa-ipo-nos-eua-em-ate-us162-bi-e-mira-us19-bi',
 'lineshine':B+'supercomputador-chines-lineshine-destrona-el-capitan-e-lidera-o-ranking-top500',
 'halos':B+'nvidia-lanca-halos-for-robotics-sistema-de-seguranca-aberto-para-robos',
 'sakana':B+'sakana-ai-lanca-fugu-orquestrador-de-multiplos-agentes-que-age-como-um-unico-mod',
 'geo':B+'eua-e-ira-encerram-1-rodada-na-suica-com-roteiro-para-acordo-em-60-dias',
 'definium':B+'lsd-em-dose-unica-da-definium-passa-em-estudo-de-fase-3-para-depressao-grave',
 'fda':B+'fda-recua-e-abre-caminho-para-terapia-genica-da-regenxbio-contra-sindrome-de-hun',
}
SUB = "SpaceX capta US$20bi em dívida e revela US$100,8bi em caixa; EUA-Irã fecham primeira rodada na Suíça com US$12bi liberados; Oracle corta 21 mil vagas em um ano."
BYLINE = para(t("Por: Guilherme Saboia e Vinicius Gushiken"))

# ============ shared story bodies (short paragraphs) ============
def spacex_paras():
    return [
      para(t("A empresa de Elon Musk levou a mercado "), lk("a venda de ao menos US$20 bilhões em títulos de dívida",L['spacex_debt']),
           t(", com vencimentos de 5 a 30 anos e grau de investimento das três principais agências. No mesmo documento, revelou ter cerca de US$100,8 bilhões em caixa em 19 de junho.")),
      para(t("Ainda assim, a ação caiu ~16% na segunda — terceira sessão seguida de perdas (quase 24% em três dias) depois do IPO recorde. Parte dos recursos vai para data centers, inclusive no espaço.")),
      para(t("No domingo, fechou um "), lk("contrato de computação de US$6,3 bilhões com a Reflection AI",L['spacex_refl']),
           t(", com acesso imediato a chips Nvidia GB300 no Colossus 2. É menor que os da Anthropic (~US$1,25bi/mês) e do Google (~US$920mi/mês).")),
    ]
def kospi_para():
    return para(t("O índice coreano teve "), lk("a maior baixa diária desde março",L['kospi']),
        t(" e acionou um "), t("circuit breaker","em"), t(". Samsung e SK Hynix recuaram ~12% cada, um dia depois de o Kospi cruzar 9.100 pontos pela primeira vez. Nikkei -3,55%, Hang Seng -2% e o Stoxx 600 de tecnologia -3,2% na abertura."))
def ciber_para():
    return para(t("EUA, Reino Unido, Canadá, Austrália e Nova Zelândia publicaram uma "), lk("rara declaração conjunta",L['fiveeyes']),
        t(" pedindo controles básicos urgentes. No mesmo dia, a OpenAI lançou o "), lk("GPT-5.5-Cyber",L['openai_cyber']),
        t(" (85,6% no CyberGym) e o Patch the Planet, que já gerou 64 pull requests em projetos como cURL, Go e Python."))
def chevron_para():
    return para(t("O "), lk("Projeto Kilby",L['chevron']),
        t(" deve entregar ~2,67 GW (consumo de ~2 milhões de casas), entre os maiores complexos a gás para data center dos EUA. Turbinas da GE Vernova, gás da Chevron, primeira energia em 2028."))
def oracle_para():
    return para(t("A força global caiu para 141 mil (de 162 mil), e a empresa diz que "), lk("a adoção de IA “resultou em reduções”",L['oracle']),
        t(". Os cortes custaram ~US$1,8bi, mas o TD Cowen estima liberar US$8–10bi/ano em caixa — em meio ao capex de US$55,7bi para data centers de OpenAI e Meta."))
def geo_para():
    return para(t("Washington suspendeu sanções e, segundo a imprensa iraniana, "), lk("liberou US$12 bilhões",L['geo']),
        t(" congelados, com licença de 60 dias para retomar vendas de petróleo. As versões divergem no ponto nuclear: Bessent fala em trânsito livre em Ormuz e volta de inspetores; Teerã diz ter havido “discussão muito breve”."))
def lineshine_para():
    return para(t("O "), lk("LineShine destronou o El Capitan",L['lineshine']),
        t(" com 2,198 exaflops — primeira liderança chinesa desde 2017 e primeira máquina acima de 2 exaflops. Feito só com chips domésticos (~14 mi de núcleos), mas ficou em 4º no teste voltado a IA."))

# funding bullets
def funding_items():
    return [
      li(t("Groq. ","strong"), lk("US$650 mi",L['groq']), t(" (Disruptive, Infinitum) para a nuvem de inferência; mira 200 MW até 2027.")),
      li(t("Modular. ","strong"), t("Qualcomm em "), lk("conversas para comprar por ~US$4bi",L['modular']), t(" — 2× a avaliação de nove meses atrás.")),
      li(t("AppsFlyer. ","strong"), lk("US$1bi em série E",L['appsflyer']), t(" a US$2,7bi, com Google, Meta, Unity e Moloco em fatias minoritárias.")),
    ]
# leia também one-liners
def leia_items():
    return [
      li(t("IPO. ","strong"), t("Bending Spoons, dona do Vimeo, "), lk("fixa IPO em até US$1,62bi",L['bending']), t(" e mira US$19bi de valuation na Nasdaq.")),
      li(t("Robótica. ","strong"), t("Nvidia lança "), lk("Halos for Robotics",L['halos']), t(", sistema aberto de segurança para robôs; Agility é a primeira a adotar.")),
      li(t("Modelos. ","strong"), t("Sakana AI libera o "), lk("Fugu",L['sakana']), t(", orquestrador de múltiplos agentes que age como um modelo só.")),
      li(t("Biotech. ","strong"), lk("LSD em dose única da Definium",L['definium']), t(" passa na fase 3 para depressão grave (remissão de 12% vs 3%).")),
      li(t("FDA. ","strong"), t("Agência recua e "), lk("abre caminho para a terapia gênica da Regenxbio",L['fda']), t(" contra a síndrome de Hunter.")),
    ]

# ============ OPTION A — Manchetes (headline-driven) ============
def option_A():
    c=[BYLINE, hr(),
       H(3,t("SpaceX capta US$20bi em dívida e revela US$100,8bi em caixa"))]
    c+=spacex_paras()
    c+=[hr(),
        H(3,t("Kospi despenca 9,99% e aciona circuit breaker")), kospi_para(),
        H(3,t("Five Eyes alerta: IA mudará ciberataques “em meses, não anos”")), ciber_para(),
        H(3,t("Chevron e Microsoft firmam data center a gás de 20 anos no Texas")), chevron_para(),
        H(3,t("Oracle corta 21 mil vagas em um ano e cita a IA")), oracle_para(),
        H(3,t("EUA e Irã fecham 1ª rodada na Suíça com roteiro para 60 dias")), geo_para(),
        H(3,t("Supercomputador chinês LineShine assume o topo do TOP500")), lineshine_para(),
        hr(),
        H(4,t("Rodadas de investimento")), ul(*funding_items()),
        hr(),
        callout(para(t("Leia também","strong")),
                *[{"type":"paragraph","attrs":{"textAlign":None},"content":item["content"][0]["content"]} for item in leia_items()]),
       ]
    return c

# ============ OPTION B — Caixa-resumo + seções temáticas ============
def option_B():
    c=[BYLINE,
       callout(
         para(t("Hoje em 3 pontos","strong")),
         para(t("• SpaceX capta US$20bi em dívida, mostra US$100,8bi em caixa — e a ação cai 16%.")),
         para(t("• Kospi despenca 9,99% e aciona circuit breaker; chips arrastam a Ásia.")),
         para(t("• Oracle corta 21 mil vagas em um ano e aponta o dedo para a IA.")),
       ),
       H(2,t("A manchete")),
       H(3,t("SpaceX: US$20bi em dívida, US$100,8bi em caixa")),
      ]
    c+=spacex_paras()
    c+=[
       H(2,t("Mercados")),
       para(t("Kospi −9,99%. ","strong"), *kospi_para()["content"][1:]),
       quote(para(t("“Meses, não anos” — o prazo que a aliança Five Eyes deu para a IA avançada transformar os ataques cibernéticos."))),
       H(2,t("Infraestrutura de IA")),
       para(t("Energia. ","strong"), *chevron_para()["content"][1:]),
       para(t("Empregos. ","strong"), *oracle_para()["content"][1:]),
       H(4,t("Rodadas de investimento")), ul(*funding_items()),
       H(2,t("Segurança")),
       para(t("Five Eyes + OpenAI. ","strong"), *ciber_para()["content"][1:]),
       H(2,t("Mundo")),
       para(t("EUA–Irã. ","strong"), *geo_para()["content"][1:]),
       H(2,t("Hardware")),
       para(t("TOP500. ","strong"), *lineshine_para()["content"][1:]),
       hr(),
       H(3,t("Leia também")), ul(*leia_items()),
      ]
    return c

# ============ OPTION C — Digest denso (bullet-first) ============
def option_C():
    c=[BYLINE,
       H(3,t("SpaceX capta US$20bi em dívida e revela US$100,8bi em caixa")),
       spacex_paras()[0], spacex_paras()[2],
       hr(),
       H(4,t("Mercados")),
       ul(li(t("Kospi −9,99%. ","strong"), *kospi_para()["content"][1:])),
       H(4,t("Infraestrutura & energia")),
       ul(li(t("Chevron + Microsoft. ","strong"), *chevron_para()["content"][1:]),
          li(t("Oracle. ","strong"), *oracle_para()["content"][1:])),
       H(4,t("Segurança")),
       ul(li(t("Five Eyes + OpenAI. ","strong"), *ciber_para()["content"][1:])),
       H(4,t("Capital")),
       ul(*funding_items()),
       H(4,t("Hardware & modelos")),
       ul(li(t("TOP500. ","strong"), *lineshine_para()["content"][1:]),
          li(t("Nvidia. ","strong"), t("lança "), lk("Halos for Robotics",L['halos']), t(", sistema aberto de segurança para robôs.")),
          li(t("Sakana AI. ","strong"), t("libera o "), lk("Fugu",L['sakana']), t(", orquestrador multiagente que age como um modelo só."))),
       H(4,t("Mundo")),
       ul(li(t("EUA–Irã. ","strong"), *geo_para()["content"][1:])),
       hr(),
       H(4,t("Leia também")),
       ul(*[item for item in leia_items() if item["content"][0]["content"][0]["text"] in ("IPO. ","Biotech. ","FDA. ")]),
      ]
    return c

# ============ OPTION D — Híbrido (best of A+B+C) ============
def leia_callout(keys):
    items=[it for it in leia_items() if it["content"][0]["content"][0]["text"].strip().rstrip(".") in keys]
    paras=[para(t("Leia também","strong"))]
    for it in items:
        paras.append({"type":"paragraph","attrs":{"textAlign":None},"content":it["content"][0]["content"]})
    return callout(*paras)

def option_D():
    # GRANDES — manchete H3 + parágrafos curtos
    c=[BYLINE,
       H(3,t("SpaceX capta US$20bi em dívida e revela US$100,8bi em caixa"))]
    c+=spacex_paras()
    c+=[
       H(3,t("Kospi despenca 9,99% e aciona circuit breaker")), kospi_para(),
       H(3,t("EUA e Irã fecham 1ª rodada na Suíça com roteiro para 60 dias")), geo_para(),
       hr(),
       # MÉDIAS — clusters temáticos + bullets densos
       H(4,t("Segurança")),
       ul(li(t("Five Eyes + OpenAI. ","strong"), *ciber_para()["content"][1:])),
       H(4,t("Infraestrutura & energia")),
       ul(li(t("Chevron + Microsoft. ","strong"), *chevron_para()["content"][1:]),
          li(t("Oracle. ","strong"), *oracle_para()["content"][1:])),
       H(4,t("Rodadas de investimento")),
       ul(*funding_items()),
       H(4,t("Hardware & modelos")),
       ul(li(t("TOP500. ","strong"), *lineshine_para()["content"][1:]),
          li(t("Nvidia. ","strong"), t("lança "), lk("Halos for Robotics",L['halos']), t(", sistema aberto de segurança para robôs.")),
          li(t("Sakana AI. ","strong"), t("libera o "), lk("Fugu",L['sakana']), t(", orquestrador multiagente que age como um modelo só."))),
       hr(),
       # Leia também as a callout box (from A) — the genuinely minor items
       leia_callout({"IPO","Biotech","FDA"}),
      ]
    return c

def post(title, content):
    sid,host=creds()
    doc={"type":"doc","content":content}
    payload={"draft_title":title,"draft_subtitle":SUB,"draft_body":json.dumps(doc,ensure_ascii=False),
     "draft_bylines":[{"id":473611573}],"draft_section_id":None,"audience":"only_paid","type":"newsletter"}
    req=urllib.request.Request(f"https://{host}/api/v1/drafts",data=json.dumps(payload).encode(),method="POST",
     headers={"Content-Type":"application/json","Cookie":f"substack.sid={sid}","User-Agent":"Mozilla/5.0"})
    r=json.loads(urllib.request.urlopen(req).read())
    print(f"{title}\n  https://{host}/publish/post/{r.get('id')}\n  id={r.get('id')}")
    return r.get('id')

def update(draft_id, title, content):
    sid,host=creds()
    doc={"type":"doc","content":content}
    payload={"draft_title":title,"draft_subtitle":SUB,"draft_body":json.dumps(doc,ensure_ascii=False),
     "draft_bylines":[{"id":473611573}],"draft_section_id":None,"audience":"only_paid","type":"newsletter"}
    req=urllib.request.Request(f"https://{host}/api/v1/drafts/{draft_id}",data=json.dumps(payload).encode(),method="PUT",
     headers={"Content-Type":"application/json","Cookie":f"substack.sid={sid}","User-Agent":"Mozilla/5.0"})
    r=json.loads(urllib.request.urlopen(req).read())
    print(f"updated {draft_id}\n  https://{host}/publish/post/{r.get('id')}")
    return r.get('id')

if __name__=="__main__":
    update(203302947, "FORMATO D — Grandes/Médias/Pequenas [2026-06-23]", option_D())
