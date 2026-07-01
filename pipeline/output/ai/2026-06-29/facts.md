# Fatos — Newsletter [Tech] 29 de Junho de 2026

## xAI / Grok — beta privado e modelos mensais
- Em 28 de junho, dia em que completou 55 anos, Elon Musk afirmou que o Grok 4.5 entrou em beta privado na SpaceX e na Tesla.
- O Grok 4.5 é construído sobre o modelo de base V9 da xAI, de 1,5 trilhão de parâmetros.
- Dados da startup de programação Cursor foram adicionados em treinamento suplementar.
- Musk afirmou que avaliações internas preliminares mostram desempenho do Grok 4.5 próximo, e possivelmente superior, ao do Claude Opus, modelo de ponta da Anthropic.
- Musk prometeu que a xAI/SpaceX lançará um novo modelo de base "treinado completamente do zero" a cada mês até o fim do ano, em vez de atualizações incrementais com ajuste fino.
- Musk disse que a xAI já começou a treinar um modelo maior, de 2 trilhões de parâmetros.
- Esse modelo deve concluir o treinamento no fim de julho, antes de um lançamento mais amplo em agosto.
- Musk reconheceu que o atual modelo de base do Grok, o v8, concluiu o treinamento em dezembro e ainda contém "muitas falhas fundamentais".
- A nova arquitetura V9 busca corrigir essas falhas e aumentar a capacidade do modelo.
- Musk não deu data pública de lançamento do Grok 4.5.
- A xAI costuma liberar modelos aos assinantes do X em fases, após testes internos.
**Fontes:**
- [S1] X — https://x.com/elonmusk/status/2071184354756477041
- [S2] Times Now — https://www.timesnownews.com/technology-science/elon-musks-birthday-surprise-for-openai-and-anthropic-xai-to-launch-a-new-ai-model-every-month-article-154794705
- [S3] TradingKey — https://www.tradingkey.com/analysis/stocks/us-stocks/261997550-grok-spacex-tesla-musk-claude-opus-tradingkey
- [S4] Undercode News — https://undercodenews.com/grok-45-enters-private-beta-elon-musk-accelerates-the-ai-race-with-spacex-and-tesla-integration-video/

## Áustria — proposta de sediar a Anthropic na UE
- O secretário de Estado para a Digitalização da Áustria, Alexander Proell, escreveu à responsável por soberania tecnológica da Comissão Europeia, Henna Virkkunen.
- Proell pediu que os Estados-membros explorem "o estabelecimento e a participação estratégicos da Anthropic dentro da União Europeia".
- A Bloomberg foi a primeira a noticiar a carta.
- O lobby foi motivado por uma ordem do Departamento de Comércio dos EUA, no início de junho, para que a Anthropic cortasse o acesso de estrangeiros a seus dois sistemas mais avançados, citando segurança nacional.
- Proell argumentou que a Europa deveria oferecer à Anthropic "segurança jurídica, acesso ao mercado, capital e um conjunto de valores que combine com a empresa".
- Ele afirmou que ser cliente não é o mesmo que ter garantia de acesso.
- Os modelos restringidos foram identificados como o Fable 5 e o Mythos 5 da Anthropic.
- O bloqueio global desses modelos deflagrou um debate sobre "soberania de IA".
- A carta não especificou um mecanismo, como uma subsidiária europeia, um acordo de residência de dados ou uma participação acionária.
- O gabinete de Virkkunen não havia respondido publicamente à carta.
**Fontes:**
- [S5] The Next Web — https://thenextweb.com/news/austria-eu-host-anthropic-us-curbs
- [S6] The News International — https://www.thenews.com.pk/latest/1407453-austria-lobbies-eu-to-host-anthropic-seeking-ai-sovereignty
- [S7] Digg — https://digg.com/tech/2ckbvird

## DeepSeek — DSpark, framework de decodificação especulativa
- A DeepSeek lançou o DSpark, um framework de decodificação especulativa para seus modelos de ponta V4.
- A empresa afirma que o DSpark aumenta a velocidade de resposta por usuário em até 85%.
- O ganho reduz gargalos de inferência e a dependência de infraestrutura de chips maior, em meio às restrições dos EUA a chips de IA.
- O DSpark usa um modelo-rascunho leve para propor tokens candidatos, que um modelo maior verifica em lotes.
- O DSpark acrescenta um método semi-autorregressivo que gera pequenos blocos de tokens de uma vez.
- O DSpark inclui um sistema de escalonamento baseado em confiança que ajusta o nível de verificação conforme a demanda de computação.
- A DeepSeek abriu o código completo do DeepSpec.
- O DeepSpec traz três algoritmos de modelo-rascunho (DSpark, DFlash, Eagle3), além de pipelines de preparação de dados, treinamento e avaliação.
- Esses pipelines também abrangem as famílias de modelos Qwen3 e Gemma.
- A DeepSeek relatou que o DSpark eleva a velocidade de geração em 60% a 85% no modelo V4 Flash e em 57% a 78% no V4 Pro, ante a base anterior MTP-1.
- O comprimento médio de aceitação melhorou de 26,7% a 30,9% em relação ao Eagle3, em modelos Qwen3 testados nas escalas de 4B, 8B e 14B parâmetros.
- Os checkpoints do DSpark se acoplam aos modelos de prévia já existentes DeepSeek-V4, em vez de constituírem um novo modelo base.
- O V4-Pro tem 1,6 trilhão de parâmetros no total, com 49 bilhões ativados.
- O V4-Flash tem 284 bilhões de parâmetros no total, com 13 bilhões ativados.
- Ambos suportam contexto de 1 milhão de tokens.
**Fontes:**
- [S8] South China Morning Post — https://www.scmp.com/tech/big-tech/article/3358647/faster-ai-lower-costs-dspark-eases-inference-bottlenecks-and-chip-strain-says-deepseek
- [S9] AI Weekly — https://aiweekly.co/alerts/deepseek-open-sources-deepspec-speculative-decoding-stack
- [S10] Hugging Face — https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-DSpark

## Coreia do Sul — complexo de memória da Samsung e SK Hynix
- Na segunda-feira, 29 de junho, o presidente Lee Jae Myung anunciou que a Samsung Electronics e a SK Hynix vão investir 800 trilhões de wons (US$519 bilhões) em um novo complexo de semicondutores na região sudoeste da Coreia do Sul.
- Cada empresa vai construir duas fábricas (fabs) de chips de memória.
- O plano mais amplo para chips soma 911 trilhões de wons (US$591 bilhões).
- O plano abrange novas fabs de memória no sudoeste, um polo de encapsulamento avançado na região de Chungcheong e um centro de cadeia de suprimentos no sudeste.
- Outros 81 trilhões de wons (US$52,5 bilhões) estão destinados a um polo de encapsulamento de chips na região de Chungcheong, perto de Seul.
- A cidade de Gwangju, no sudoeste, e a província de Jeolla do Sul acrescentam de 5 trilhões a 20 trilhões de wons.
- O presidente da Samsung, Lee Jae-yong, apontou Gwangju como a principal candidata ao próximo site de fabricação da empresa.
- O governo disse que o plano ajudará a dobrar a capacidade de produção de chips de memória da Coreia em cinco anos.
- O presidente Lee descreveu o pacote como um "grande salto adiante", baseado num "tríplice eixo" de semicondutores, IA física e data centers.
- O anúncio ocorre em meio à disparada da demanda por memória impulsionada por IA.
**Fontes:**
- [S11] Al Jazeera — https://www.aljazeera.com/news/2026/6/29/south-korea-announces-more-than-1-trillion-ai-chip-investment-drive
- [S12] KED Global — https://www.kedglobal.com/policy/newsView/ked202606290004
- [S13] The Korea Times — https://www.koreatimes.co.kr/southkorea/politics/20260629/samsung-sk-hynix-pledge-519-bil-for-southwestern-chip-hub
- [S14] Nikkei Asia — https://asia.nikkei.com/business/tech/semiconductors/south-korea-announces-520bn-chip-plant-project-with-samsung-sk-hynix

## Coreia do Sul — megaplano de data centers de IA
- Como parte do mesmo anúncio de "três megaprojetos" de 29 de junho, o SK Group, o GS Group e a Naver vão investir 550 trilhões de wons (US$356 bilhões) em data centers de IA.
- A capacidade começa em 8,4 gigawatts e deve se expandir para 18,4 gigawatts até 2035.
- O ministro da Ciência, Bae Kyung-hoon, disse que um data center de IA adicional de 10 gigawatts será construído até 2035.
- Isso eleva a capacidade total planejada para acima de 18,4 gigawatts e o investimento total para mais de 1.000 trilhões de wons (US$648 bilhões).
- Incluindo as fabs de memória e os data centers, o presidente do SK Group, Chey Tae-won, disse que só o grupo investirá um total de 1.100 trilhões de wons.
- Separadamente, o GS Group revelou planos para um campus de data center de IA de 2,4 gigawatts em Donghae, na província de Gangwon.
- O valor do projeto do GS Group é estimado em cerca de 120 trilhões de wons (US$19,4 bilhões), incluindo GPUs e HBM (memória de alta largura de banda).
**Fontes:**
- [S15] The Korea Times — https://www.koreatimes.co.kr/southkorea/politics/20260629/samsung-sk-hynix-pledge-519-bil-for-southwestern-chip-hub
- [S16] Al Jazeera — https://www.aljazeera.com/news/2026/6/29/south-korea-announces-more-than-1-trillion-ai-chip-investment-drive
- [S17] The Herald Business — https://biz.heraldcorp.com/article/10792049

## CXMT — acordo de fornecimento de DRAM com a Tencent
- A fabricante chinesa de chips de memória CXMT (ChangXin Memory Technologies) assinou um contrato de fornecimento de DRAM (memória dinâmica de acesso aleatório) para servidores com a Tencent.
- O contrato vale cerca de 20 bilhões de yuans (aproximadamente US$3 bilhões / 4,5 trilhões de wons).
- O período estimado do contrato é de três a cinco anos.
- O acordo precede o IPO planejado da CXMT (abertura de capital em bolsa).
- Em maio, a CXMT recebeu aprovação para captar 29,5 bilhões de yuans (cerca de US$4,4 bilhões) no STAR Market de Xangai.
- Deve ser a maior abertura de capital da China continental desde 2022.
- A CXMT está em conversas sobre parcerias de fornecimento de longo prazo semelhantes com outras grandes empresas de internet chinesas.
- O prospecto de IPO da CXMT citou Tencent, Alibaba Cloud, ByteDance, Lenovo e Xiaomi como principais clientes.
- A CXMT opera duas fabs de DRAM de 12 polegadas em Hefei e uma em Pequim, com capacidade combinada de cerca de 300 mil wafers por mês.
- A CXMT começou a construir uma nova fábrica de DRAM em Xangai.
- A nova fábrica praticamente dobraria a produção, para cerca de 600 mil wafers por mês.
- Analistas alertam que o aumento do uso de DRAM doméstica para servidores pelas big techs chinesas pode se tornar um fardo de médio a longo prazo sobre as vendas de DRAM commodity da Samsung Electronics e da SK Hynix para a China.
**Fontes:**
- [S18] Seoul Economic Daily — https://en.sedaily.com/international/2026/06/29/chinas-cxmt-to-supply-tencent-45-trillion-won-in-dram-over
- [S19] Chosunbiz — https://biz.chosun.com/en/en-it/2026/06/29/JGCN5GCTDNBFRPR5DXEPRAZZXM/
- [S20] Meyka — https://meyka.com/blog/chinas-cxmt-signs-3-billion-dram-supply-deal-with-tencent-holds-talks-with-alibaba-bytedance-and-xiaomi-2606/

## Baidu — IPO da unidade de chips Kunlunxin
- As ações da Baidu listadas em Hong Kong subiram mais de 7% em 29 de junho.
- A alta veio após relatos de que sua unidade de chips de IA Kunlunxin mira um IPO em Hong Kong que poderia avaliar a afiliada em US$50 bilhões.
- Segundo o The Information, investidores interessados no IPO foram solicitados a comprar semicondutores da Kunlunxin no valor de três a sete vezes o montante pretendido de subscrição.
- A meta de US$50 bilhões é um salto acentuado em relação à avaliação de cerca de US$3 bilhões em conversas de captação meses atrás.
- Em maio, a meta relatada era de US$14,7 bilhões.
- A Baidu protocolou de forma confidencial o pedido de listagem da Kunlunxin em Hong Kong no início do ano.
- Fundada entre 2011 e 2012, a Kunlunxin fornece chips principalmente à Baidu, que mantém participação controladora.
- A Kunlunxin ampliou as vendas externas nos últimos dois anos.
**Fontes:**
- [S21] DealStreetAsia — https://www.dealstreetasia.com/stories/baidus-ai-chip-unit-kunlunxin-eyes-50b-valuation-in-hong-kong-ipo-487035
- [S22] Meyka — https://meyka.com/blog/baidu-nasdaq-bidu-shares-surge-7-after-report-says-ai-chip-unit-kunlunxin-targets-50-billion-valuation-in-hong-kong-ipo-2606/
- [S23] CNBC — https://www.cnbc.com/2026/06/29/baidu-kunlunxin-hong-kong-ipo-50-billion-ai-chips.html

## China — dois unicórnios de robótica: AI² Robotics e X Square
- Duas fabricantes chinesas de robôs humanoides alcançaram o status de unicórnio (startup avaliada em mais de US$1 bilhão) nesta semana, com avaliação combinada acima de US$2,9 bilhões.
- A AI² Robotics captou quase 5 bilhões de yuans (US$736 milhões).
- Cada uma das duas empresas agora ultrapassa 20 bilhões de yuans em valor.
- A AI² Robotics (Zhiping Fang) concluiu uma série de novos aportes que somam quase 5 bilhões de yuans (cerca de US$700 a 736 milhões), com avaliação acima de 20 bilhões de yuans.
- A AI² Robotics se tornou a primeira empresa de inteligência incorporada da Grande Baía (Guangdong-Hong Kong-Macau) a superar uma avaliação de 20 bilhões de yuans.
- A AI² Robotics vai usar os recursos para escalar a produção.
- A empresa planeja iniciar no segundo semestre de 2026 a construção da primeira fábrica em larga escala da China continental dedicada a produzir dezenas de milhares de unidades humanoides.
- A AI² Robotics já possui uma linha semiautomatizada com capacidade anual de mais de 2.000 unidades.
- A X Square Robot fechou sua Série C na segunda-feira, 29 de junho.
- Foi a quarta rodada consecutiva da X Square Robot (B, B+, B++ e C) em 60 dias.
- A avaliação da X Square Robot passou de 20 bilhões de yuans (US$2,8 bilhões).
- A X Square Robot é a única empresa de IA incorporada com aporte como investidor-líder, em estágios diferentes, da Alibaba, ByteDance, Meituan e Xiaomi.
- O setor chinês de IA incorporada e robótica atraiu pelo menos 46 bilhões de yuans neste ano, superando todo o ano passado.
- Mais de 140 empresas disputam a "IA física", termo usado por Jensen Huang, da Nvidia.
**Fontes:**
- [S24] The Next Web — https://thenextweb.com/news/china-ai-funding-surge-deepseek-unicorns
- [S25] WEEX / The Paper — https://www.weex.com/news/detail/zhi-ping-fang-has-completed-a-new-round-of-financing-of-nearly-5-billion-yuan-with-a-valuation-exceeding-20-billion-yuan-g41wwxiqv4yfog77hn2377pn
- [S26] TMTPost — https://en.tmtpost.com/news/8045739
- [S27] PR Newswire APAC — https://en.prnasia.com/releases/apac/x-square-robot-secures-four-consecutive-financing-rounds-surpasses-us-2-8-billion-valuation-in-push-for-physical-ai-foundation-models-539059.shtml

## Firmus — data center de IA de 360 MW em Batam
- A australiana Firmus Technologies e a DayOne, sediada em Singapura, vão desenvolver um campus Nvidia DSX AI Factory de 360 megawatts em Batam, na Indonésia.
- O projeto faz parte de uma parceria de oito anos com a Nvidia.
- Batam é uma ilha próxima à costa de Singapura.
- O campus deve entrar em operação no primeiro trimestre de 2027.
- O acordo abrange até 170 mil aceleradores de IA da Nvidia nas plataformas Grace-Blackwell, Vera-Rubin e Vera, ao longo de 2027 e 2028.
- A estrutura envolve compartilhamento de receita e suporte de crédito.
- A Firmus espera receber de US$25 bilhões a US$30 bilhões em acordos firmados de aquisição (offtake) durante os primeiros seis anos da parceria com a Nvidia.
- A Firmus começou como uma operação de mineração de Bitcoin na Tasmânia em 2019.
- A Firmus foi avaliada em US$5,5 bilhões em uma rodada de abril liderada pela Coatue Management e com apoio da Nvidia.
- É amplamente esperado que a Firmus faça um IPO neste ano.
- A DayOne, apoiada pela Coatue Management e pelo SoftBank, também avalia um IPO.
- A Reuters relatou que o investidor do Golfo MGX considerava comprar a DayOne por uma avaliação de cerca de US$20 bilhões.
**Fontes:**
- [S28] The Straits Times — https://www.straitstimes.com/business/companies-markets/ai-start-up-firmus-to-build-data-centre-in-batam-with-nvidia
- [S29] The Business Times — https://www.businesstimes.com.sg/companies-markets/telcos-media-tech/australias-ai-startup-firmus-and-singapore-based-dayone-build-indonesia-data-centre-nvidia
- [S30] W.Media — https://w.media/firmus-dayone-to-co-develop-360mw-nvidia-ai-factory-in-batam/
- [S31] Tech Wire Asia — https://techwireasia.com/2026/06/nvidia-firmus-batam-ai-data-centre/

## EUA e Irã — colapso do cessar-fogo no Estreito de Ormuz
- O Comando Central dos EUA atacou alvos militares iranianos em Sirik, Bandar-e Lengeh e na Ilha de Qeshm.
- Os EUA disseram ter atingido 10 alvos próximos ao Estreito de Ormuz.
- O ataque foi resposta a um ataque iraniano com drone ao petroleiro Kiku.
- A Guarda Revolucionária do Irã (IRGC) lançou mísseis balísticos e drones contra sites militares dos EUA no Kuwait e no Bahrein no domingo, 28 de junho.
- O Irã alegou ter destruído oito instalações dos EUA.
- Os Emirados Árabes Unidos chamaram os ataques de "violação flagrante" da soberania.
- O ministro das Relações Exteriores do Irã, Abbas Araghchi, disse no domingo que, sob o acordo provisório com Trump, somente Teerã supervisionará o tráfego marítimo pelo Estreito de Ormuz.
- Os EUA insistem que a passagem deve permanecer aberta a todos.
- Apesar dos ataques, autoridades dos EUA e do Irã ainda devem realizar conversas técnicas em Doha na terça-feira.
- Um alto funcionário dos EUA disse que as conversas planejadas não foram canceladas.
- O petróleo Brent subiu acima de US$72 o barril na segunda-feira, 29 de junho, recuperando-se das mínimas de quatro meses em meio à renovação das tensões entre EUA e Irã.
- Ainda assim, o Brent acumulou queda de cerca de 23,6% no mês.
**Fontes:**
- [S32] Al Jazeera — https://www.aljazeera.com/news/2026/6/28/iran-attacks-kuwait-and-bahrain-in-response-to-us-strikes
- [S33] Antiwar.com — https://news.antiwar.com/2026/06/28/irans-irgc-says-it-targeted-eight-us-military-installations-in-response-to-us-attacks/
- [S34] Newser — https://www.newser.com/story/391862/iran-says-deal-gave-it-sole-control-of-strait.html
- [S35] The Straits Times — https://www.straitstimes.com/business/companies-markets/oil-prices-jump-after-tanker-hit-in-renewed-attacks-between-us-and-iran
- [S36] Trading Economics — https://tradingeconomics.com/commodity/brent-crude-oil

## Ucrânia — ataques a refinarias russas e déficit de combustível
- O presidente Zelensky disse que a Ucrânia atacou durante a noite duas refinarias de petróleo russas, nas regiões de Krasnodar (Slavyansk-na-Kubani) e Yaroslavl.
- A queda de destroços de um drone abatido matou uma pessoa perto de Slavyansk.
- Vladimir Putin reconheceu pela primeira vez, no domingo, que a Rússia enfrenta um "certo déficit" de combustível.
- Putin prometeu reforçar a proteção das instalações de petróleo e aumentar a produção de combustível.
- A intensificação da campanha de drones da Ucrânia causou escassez aguda de combustível e racionamento em postos por toda a Rússia.
- A escassez chegou à Sibéria, a milhares de quilômetros da linha de frente.
- A Rússia atacou a Ucrânia durante a noite com 142 drones de ataque e oito mísseis.
- As defesas aéreas ucranianas abateram 125 drones e sete mísseis.
- Um ataque russo na região de Kharkiv matou uma pessoa e feriu oito.
- Uma bomba aérea em Zaporizhzhia matou duas pessoas.
- A Ucrânia realizou pelo menos 13 ataques de longo alcance contra instalações industriais de defesa russas em junho.
- É o maior total mensal registrado em 2026.
**Fontes:**
- [S37] Barchart (AP) — https://www.barchart.com/story/news/3022239/ukrainian-strike-sets-fire-to-an-oil-refinery-in-southern-russia
- [S38] Fortune (AP) — https://fortune.com/2026/06/28/ukraine-drone-attacks-russian-refineries-fuel-shortages-siberia/
- [S39] WDEZ (Reuters) — https://wdez.com/2026/06/28/ukraine-hits-two-russian-oil-refineries-overnight/
- [S40] RBC-Ukraine — https://newsukraine.rbc.ua/news/drone-and-missile-barrage-hits-ukraine-overnight-1782633280.html
- [S41] UNITED24 Media — https://united24media.com/war-in-ukraine/ukraine-launches-record-wave-of-strikes-on-russias-defense-industry-in-june-20234

## BridgeBio — infigratinibe oral na acondroplasia (Fase 3)
- A BridgeBio publicou em 28 de junho os resultados da Fase 3 do estudo PROPEL 3, com infigratinibe oral em crianças com acondroplasia (forma mais comum de nanismo).
- A publicação saiu no New England Journal of Medicine (NEJM).
- Houve apresentação simultânea, de última hora, no ICCBH 2026, em Montreal.
- O estudo atingiu seu desfecho primário.
- A diferença na velocidade de crescimento anualizada (média dos mínimos quadrados) foi de +1,74 cm/ano em relação ao placebo (p<0,0001).
- Novos dados de escore Z de envergadura mostraram melhora de +0,37 desvio-padrão (DP) ante o placebo (p<0,0001).
- Foi descrito como o primeiro e único resultado de envergadura estatisticamente significativo, controlado por placebo, relatado em um estudo de acondroplasia em 52 semanas.
- Os resultados dão suporte a submissões planejadas à FDA (agência reguladora de medicamentos dos EUA) e à EMA (agência europeia de medicamentos), a partir do terceiro trimestre de 2026.
- O infigratinibe avança como possível primeira terapia oral para a acondroplasia.
- O infigratinibe (KK8398) é um inibidor oral seletivo de FGFR1-3.
- A Kyowa Kirin detém direitos exclusivos para desenvolver e comercializar o medicamento no Japão, sob parceria com a BridgeBio.
**Fontes:**
- [S42] Stock Titan — https://www.stocktitan.net/news/BBIO/bridge-bio-announces-publication-in-the-new-england-journal-of-o2jcwabskf27.html
- [S43] Kyowa Kirin — https://www.kyowakirin.com/media_center/news_releases/2026/pdf/e20260624_01.pdf

## Verizon e BT — joint venture internacional
- O BT Group e a Verizon concordaram em combinar suas operações corporativas internacionais em uma joint venture 50:50.
- A empresa conjunta atenderá mais de 3.000 clientes em mais de 180 países.
- A receita anual combinada é de cerca de US$4 bilhões.
- Como parte do acordo, a Verizon concordou em pagar ao BT um "pagamento de equalização" de US$625 milhões.
- As duas empresas terão direitos de voto iguais.
- A joint venture será constituída em Jersey e terá sede e residência fiscal no Reino Unido.
- Martijn Blanken foi nomeado CEO designado.
- A conclusão é esperada para 2027, sujeita a aprovações regulatórias.
- A Verizon espera uma perda estimada de US$700 milhões a US$800 milhões no segundo trimestre.
- O negócio aportado foi classificado como mantido para venda.
- O analista James Ratzer, da New Street Research, disse que o pagamento de US$625 milhões implica um múltiplo de venda de mais de 10 vezes o EBITDA (lucro antes de juros, impostos, depreciação e amortização).
- Ratzer chamou o acordo de "uma saída limpa e atraente para o BT".
**Fontes:**
- [S44] Verizon — https://www.verizon.com/about/news/verizon-bt-group-international-joint-venture
- [S45] TelcoNews — https://telconews.com/story/bt-verizon-form-50-50-venture-for-international-ops
- [S46] TradingView — https://www.tradingview.com/news/tradingview:2b9f4a51dfd74:0-verizon-to-form-50-50-joint-venture-with-bt-pays-625m-and-expects-q2-charges/
- [S47] TipRanks — https://www.tipranks.com/news/verizon-vz-bt-create-4-billion-telecom-venture-in-international-business-shake-up
- [S48] Advanced Television — https://www.advanced-television.com/2026/06/29/bt-verizon-international-connectivity-jv/

## Sérvia — protesto em Belgrado e renúncia de Vucic
- Cerca de 140.000 manifestantes protestaram em Belgrado em 28 de junho, a maior adesão em meses, exigindo eleições antecipadas.
- A estimativa independente da multidão superou em muito o número da polícia, de 36.000.
- Diferentemente de manifestações pacíficas anteriores, houve confrontos entre manifestantes e a polícia de choque.
- Dezenas de pessoas foram detidas, e seis policiais e dois manifestantes ficaram feridos.
- Os protestos liderados por estudantes começaram em novembro de 2024.
- O estopim foi o desabamento do teto de uma estação ferroviária em Novi Sad, que matou 16 pessoas.
- A tragédia foi amplamente atribuída à corrupção.
- O presidente Aleksandar Vucic está no poder, como presidente ou primeiro-ministro, há 12 anos.
- Em 27 de junho, Vucic disse que renunciaria em semanas.
- Vucic afirmou que a Sérvia realizaria eleições presidenciais e parlamentares antecipadas.
**Fontes:**
- [S49] Hurriyet Daily News — https://www.hurriyetdailynews.com/around-140-000-rally-in-belgrade-to-call-for-elections-210876
- [S50] SRN News (Reuters) — https://srnnews.com/serbia-president-vucic-says-to-resign-within-weeks-one-year-before-end-of-mandate/

## Chadchart — reeleição para governador de Bangkok
- O atual governador, o independente Chadchart Sittipunt, declarou vitória na eleição para governador de Bangkok na noite de domingo, 28 de junho.
- Ele caminha para um segundo mandato com vitória esmagadora.
- Resultados não oficiais mostraram Chadchart com cerca de 1,444 milhão de votos (94,99% das cédulas apuradas).
- Ele ficou muito à frente da rival mais próxima, Mallika Boonmeetrakool Mahasuk, que recebeu 288.171 votos.
- Chadchart disse que o resultado, com apoio maior que na vitória esmagadora de 2022, não é motivo de comemoração.
- Segundo ele, é um sinal de que o próximo mandato trará responsabilidade mais pesada.
- A certificação oficial pela Comissão Eleitoral ainda é necessária.
**Fontes:**
- [S51] The Nation Thailand — https://www.nationthailand.com/news/politics/40067996

## SpaceX — lançamento do satélite SXM-11 da SiriusXM
- Um foguete Falcon 9 da SpaceX lançou com sucesso o satélite SXM-11 da SiriusXM.
- O lançamento partiu do Complexo de Lançamento Espacial 40, em Cabo Canaveral, às 22h25 EDT de 28 de junho (02h25 UTC de 29 de junho).
- O SXM-11 pesa cerca de 7,5 toneladas (15.000 libras).
- É o satélite mais potente da frota da SiriusXM.
- O SXM-11 substitui dois satélites geoestacionários antigos e amplia a cobertura, inclusive no Alasca.
- O satélite foi construído pela Lanteris Space Systems (ex-Maxar / Space Systems Loral) na plataforma IM-1300.
- O SXM-11 carrega um refletor de malha desdobrável de cerca de 10 metros.
- O destino do satélite era a órbita de transferência geoestacionária.
- O primeiro estágio do Falcon 9, o propulsor B1085, fez seu 17º voo.
- O propulsor pousou na barcaça-drone "A Shortfall of Gravitas".
- O B1085 voltou ao serviço 30 dias após sua missão anterior.
**Fontes:**
- [S52] Next Spaceflight — https://nextspaceflight.com/launches/details/8258/
- [S53] Space Launch Live — https://spacelaunchlive.com/launches/falcon-9-block-5-sirius-sxm-11/
- [S54] Spaceflight Now — https://spaceflightnow.com/2026/06/28/live-coverage-spacex-to-launch-7-5-ton-siriusxm-satellite-as-part-of-constellation-refresh/
- [S55] Florida Today — https://www.floridatoday.com/story/tech/science/space/2026/06/28/spacex-launch-day-heres-information-on-todays-siriusxm-satellite-launch-from-cape-canaveral-florida--live/90723205007/

## OpenAI — GPT-5.6 (Sol, Terra, Luna) em preview limitado
- A OpenAI iniciou o preview limitado do GPT-5.6, uma nova família de três modelos: o Sol (topo de linha), o Terra (equilibrado, para o trabalho do dia a dia) e o Luna (o mais rápido e barato).
- A nova convenção de nomes separa a geração (5.6) do nível de capacidade (Sol/Terra/Luna).
- Preço por 1 milhão de tokens (as unidades de texto que o modelo processa): o Sol custa US$5 (entrada) / US$30 (saída), o mesmo do GPT-5.5.
- O Terra sai por US$2,50 / US$15, metade do preço do GPT-5.5, com desempenho competitivo; o Luna, por US$1 / US$6.
- A OpenAI diz que o GPT-5.6 se destaca em programação, segurança cibernética e tarefas agênticas (em que o modelo executa etapas com autonomia) de longo horizonte.
- O Sol ganhou um modo "max" (raciocínio mais profundo) e um modo "ultra" (que distribui o trabalho entre subagentes).
- O Sol Ultra teria feito 91,9% no Terminal-Bench 2.1, teste de tarefas em linha de comando.
- A liberação começa pela API e pelo Codex para cerca de 20 organizações parceiras de confiança.
- A OpenAI apresentou os modelos e o plano de lançamento ao governo dos EUA a pedido dele, antes de uma liberação mais ampla; a disponibilidade geral está prevista para "as próximas semanas".
- O system card classifica os três modelos como High (alto) em cibersegurança e em risco biológico e químico sob o Preparedness Framework, mas abaixo do limiar High em autoaperfeiçoamento de IA.
**Fontes:**
- [S56] OpenAI — https://openai.com/index/previewing-gpt-5-6-sol/
- [S57] VentureBeat — https://venturebeat.com/technology/openai-unveils-gpt-5-6-sol-terra-and-luna-models-but-only-accessible-to-limited-preview-partners-for-now-per-us-gov
- [S58] The Verge — https://www.theverge.com/ai-artificial-intelligence/957845/openai-gpt-5-6-trump-administration-ai-preview
- [S59] DataCamp — https://www.datacamp.com/blog/gpt-5-6-sol-luna-terra
- [S60] Kie.ai — https://kie.ai/blog/gpt-5-6-sol-terra-luna-deep-dive
