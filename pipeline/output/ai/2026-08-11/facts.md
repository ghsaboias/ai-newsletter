# Fatos — Newsletter [Tech] 11 de Agosto de 2026

## Anthropic — Claude melhora um limite ligado à hipótese de Riemann
- A Anthropic anunciou em 10 de agosto que uma versão de pesquisa não lançada do Claude melhorou um limite inferior incondicional de longa data para a fração de zeros da função zeta de Riemann que ficam na linha crítica.
- O limite subiu de 41,6% para 67,2%.
- O modelo falhou em provar a própria hipótese de Riemann.
- O resultado saiu de duas sessões no Claude Code que somaram 31 milhões de tokens de output.
- O funcionário Jarred Sumner, que não é matemático, pediu que o Claude "desse uma tentativa de verdade" na hipótese de Riemann.
- O Claude gerou e testou 650 ideias, nenhuma das quais funcionou.
- Depois disso, passou cerca de um dia e meio coordenando aproximadamente 60 subagentes Claude.
- Os subagentes rodaram cerca de 2.400 comandos de shell e escreveram centenas de scripts em Python.
- Os subagentes revisaram as provas uns dos outros e procuraram contraexemplos.
- Os subagentes baixaram 54 artigos do arXiv para checar se a descoberta já não tinha sido feita.
- Os subagentes provaram novamente o resultado do zero, de forma independente, de forma independente.
- O Claude recomendou que um teórico dos números humano validasse o achado.
- O artigo é assinado pelo próprio modelo, descrito como um grande modelo de linguagem desenvolvido pela Anthropic.
- O artigo afirma que ao menos 67,250% dos zeros são simples e estão na linha crítica e que ao menos 83,625% são distintos.
- Com uma família de testes otimizada, as três constantes ficam em 0,6725, 0,6725 e 0,83625.
- O artigo vem acompanhado de uma formalização em Lean 4 dos Teoremas A–E.
- Os matemáticos da Anthropic Levent Alpöge e Ralph Furman analisaram o argumento e sua relação com pesquisas anteriores.
- Os teóricos dos números externos Brian Conrey e Dan Goldston examinaram o artigo em cima da hora.
- O trabalho não passou por revisão por pares convencional.
- A Anthropic diz não esperar que o método do Claude leve diretamente a uma prova da hipótese de Riemann.
- Os 67,2% não significam que os zeros restantes estejam fora da linha crítica.
**Fontes:**
- [S1] Anthropic — https://www.anthropic.com/research/riemann-zeta
- [S2] Anthropic — https://www-cdn.anthropic.com/564f962e60643842f5fcb4a17c9dbc8f608f1c37.pdf
- [S3] The AI Insider — https://theaiinsider.tech/2026/08/11/anthropic-says-claude-improved-a-longstanding-bound-tied-to-the-riemann-hypothesis/

## OpenAI — GPT-5.6-Cyber e a divisão do programa Daybreak
- A OpenAI anunciou em 10 de agosto que está dividindo seu programa de cibersegurança Daybreak em dois níveis de acesso.
- O Daybreak Blue dá acesso a modelos de propósito geral de fronteira, incluindo o GPT-5.6 Sol, com salvaguardas defensivas.
- O Daybreak Red dá acesso a modelos treinados especificamente para cibersegurança, voltados a pesquisa autorizada de vulnerabilidades, validação de exploits e testes de segurança.
- O GPT-5.6-Cyber é construído sobre o GPT-5.6 Sol e é oferecido pelo Daybreak Red.
- O GPT-5.6-Cyber é treinado para encontrar vulnerabilidades zero-day (falhas ainda desconhecidas do fabricante) e desenvolver cadeias de exploits.
- O modelo também foi treinado para recusar menos pedidos em tarefas cibernéticas de duplo uso e maior risco.
- Na avaliação interna Advanced Cybersecurity Completion Rate da OpenAI, o GPT-5.6-Cyber atende 95,0% dos pedidos de cadeia de exploit, bypass de autenticação e escalada de privilégios.
- Na mesma avaliação, o GPT-5.5-Cyber atende 57,3% dos pedidos.
- O acesso via Daybreak Blue atende 2,0% dos pedidos e o GPT-5.6 Sol padrão atende 1,5%.
- A OpenAI afirma que o modelo analisou o V8, motor JavaScript do Chrome, e encontrou duas vulnerabilidades até então desconhecidas.
- As duas falhas podem ser encadeadas para corromper memória e furar o sandbox de heap do V8.
- O Google corrigiu as falhas após divulgação coordenada e atribuiu a elas a designação CVE-2026-15903.
- O acesso a qualquer um dos dois níveis exige verificação de identidade, medidas de segurança da conta, monitoramento, restrições de uso aprovado e declarações legais.
- Chaves de segurança em hardware passam a ser obrigatórias para todas as contas Daybreak em 1º de setembro de 2026.
- A OpenAI classifica tanto o GPT-5.6 Sol quanto o GPT-5.6-Cyber como Alto em capacidade cibernética no seu Preparedness Framework, mas abaixo do limiar Crítico.
- A OpenAI diz que o GPT-5.6-Cyber não esteve envolvido no incidente de exploração da Hugging Face, nem nenhum outro modelo previsto para lançamento futuro.
- A OpenAI lançou o Daybreak em maio, junto do GPT-5.5-Cyber, pouco depois de a Anthropic lançar sua própria coalizão de cibersegurança, o Project Glasswing.
- A expansão vem depois de incidentes de segurança envolvendo modelos de IA divulgados por OpenAI, Anthropic e Meta nas últimas semanas.
**Fontes:**
- [S4] OpenAI — https://openai.com/index/expanding-daybreak-as-the-cyber-defense-window-narrows/
- [S5] The Decoder — https://the-decoder.com/openai-launches-gpt-5-6-cyber-to-help-defenders-find-vulnerabilities-before-attackers-do/
- [S6] VentureBeat — https://venturebeat.com/technology/openai-launches-gpt-5-6-cyber-with-reduced-refusals-95-completion-on-advanced-cybersecurity-tasks
- [S7] Neowin — https://www.neowin.net/news/openai-launches-gpt-56-cyber-and-expands-daybreak-with-red-and-blue-access-tiers/

## Anthropic — marca d'água em todo texto gerado pelo Claude
- A Anthropic informou em um documento de ajuda publicado na segunda-feira que o texto gerado por novos modelos Claude vai carregar marcas d'água embutidas.
- Os arquivos gerados vão incluir metadados de procedência assinados digitalmente onde houver suporte.
- A medida faz parte da conformidade com as regras de transparência da Lei de IA da União Europeia.
- A Anthropic assinou o Código de Prática sobre Transparência de Conteúdo Gerado por IA, previsto no Artigo 50(2) da Lei de IA da UE.
- Modelos Claude lançados na UE em ou após 2 de agosto de 2026 já saem com a marcação legível por máquina embutida.
- Modelos anteriores estão sendo adaptados durante o período de transição.
- A marcação vale globalmente, e não só na UE: "a marcação se aplicará à saída de modelos com suporte onde quer que o Claude seja oferecido, no mundo todo".
- A cobertura inclui a API do Claude, o Claude, o Claude Code, o Claude Cowork e o Claude Tag.
- A cobertura também inclui modelos da Anthropic servidos por terceiros como AWS, Google Cloud e Microsoft Foundry.
- O texto recebe uma marca d'água imperceptível tecida no próprio texto, que acompanha o conteúdo em copiar e colar.
- A Anthropic diz que a marca "pode persistir através de alguma edição".
- Arquivos com suporte (.svg, .png e .jpg) recebem metadados de procedência assinados seguindo o padrão C2PA.
- Edição pesada ou mudança de formato pode remover as marcações por completo.
- A Anthropic admite que a marca detectada não é prova conclusiva de que o Claude escreveu o conteúdo, já que usuários também pedem ao modelo que revise ou traduza textos próprios.
- A ausência de marca também não prova autoria humana.
- A ferramenta de detecção que permitiria a terceiros checar a marca ainda não foi lançada.
- A Anthropic não publicou o algoritmo de marca d'água nem uma taxa de falsos positivos.
- As obrigações de transparência do Artigo 50 da Lei de IA da UE passaram a valer em 2 de agosto de 2026.
- O artigo exige que provedores marquem em formato legível por máquina as saídas de IA generativa, incluindo áudio, imagem, vídeo e texto, de modo detectável como gerado ou manipulado artificialmente.
**Fontes:**
- [S8] The Register — https://www.theregister.com/ai-and-ml/2026/08/11/anthropic-pledges-to-embed-watermarks-to-help-discern-ai-slop-in-sop-to-eu/5285792
- [S9] The Decoder — https://the-decoder.com/anthropic-watermarks-all-claude-outputs-globally-with-marks-that-may-persist-through-some-editing/
- [S10] The Hindu — https://www.thehindu.com/sci-tech/technology/anthropics-claude-to-mark-all-ai-content-including-text/article71331079.ece
- [S11] Tech Times — https://www.techtimes.com/articles/323873/20260811/claude-now-watermarks-text-everywhere-mark-proves-processing-not-authorship.htm
- [S12] European Commission — https://digital-strategy.ec.europa.eu/en/policies/code-practice-ai-generated-content

## Anthropic e Riot Platforms — contrato de poder computacional de US$9,1 bilhões
- A Riot Platforms divulgou em 10 de agosto um contrato de locação de 20 anos para 191 MW de capacidade de data center em seu campus de Rockdale, no Texas.
- A Riot descreveu a contraparte apenas como um "laboratório de IA de fronteira líder".
- A Bloomberg identificou o cliente como a Anthropic.
- O contrato vai até junho de 2048.
- O acordo deve gerar US$9,1 bilhões em receita para a Riot no prazo inicial.
- Duas opções de extensão de cinco anos cada podem elevar o total a US$16,1 bilhões.
- A capacidade entra em operação por etapas: 96 MW até dezembro de 2027 e os 191 MW completos até junho de 2028.
- Os 191 MW equivalem aproximadamente ao consumo elétrico de cerca de 143 mil residências a qualquer momento.
- A ação da Riot subiu mais de 25% no after-hours de segunda-feira.
- A ação estava em alta de cerca de 21% na negociação pré-mercado de terça-feira.
- A Riot é uma mineradora de bitcoin de origem e minerou 1.587 bitcoins apenas no segundo trimestre de 2026.
- A empresa já assinou contratos de locação somando 241 MW de capacidade em seis meses, o equivalente a cerca de US$9,8 bilhões de receita contratada de longo prazo.
- O outro inquilino é a AMD.
- A Riot montou uma linha de financiamento interina de US$573 milhões via Morgan Stanley para bancar a fase inicial de construção do projeto.
- A Riot trabalha para colocar de pé um respaldo de crédito permanente.
- O contrato é a terceira grande compra de poder computacional da Anthropic em três meses.
- As três compras somam mais de US$60 bilhões em compromissos.
**Fontes:**
- [S13] Yahoo Finance — https://finance.yahoo.com/technology/ai/articles/anthropic-signs-9-1-billion-113731732.html
- [S14] FinanceFeeds — https://financefeeds.com/riot-platforms-just-signed-a-9-1-billion-ai-lease-reportedly-with-anthropic-and-shares-jumped-25/
- [S15] The Next Web — https://thenextweb.com/news/anthropic-riot-9bn-data-centre-deal
- [S16] Livemint — https://www.livemint.com/companies/anthropic-signs-9-1-billion-20-year-ai-cloud-deal-with-bitcoin-miner-riot-platforms-for-texas-data-centre-capacity-11786430274769.html
- [S17] SEC EDGAR — https://www.sec.gov/Archives/edgar/data/1167419/000110465926093406/riot-20260810x8k.htm
- [S18] TipRanks — https://www.tipranks.com/news/riot-stock-rockets-21-premarket-on-signing-9-1-billion-cloud-deal-with-anthropic
- [S19] TradingKey — https://www.tradingkey.com/analysis/stocks/us-stocks/262095019-anthropic-riot-91-billion-ai-compute-bitcoin-mining-data-center-transition-tradingkey

## OpenAI — recompra de US$7 bilhões em ações de funcionários
- A OpenAI concluiu na segunda-feira uma venda secundária de ações de aproximadamente US$7 bilhões.
- A operação permitiu que funcionários atuais e ex-funcionários vendessem ações ao valuation de US$852 bilhões da empresa.
- A CNBC confirmou a operação na segunda-feira.
- O preço de US$852 bilhões é o mesmo da rodada recorde de captação de US$122 bilhões fechada em março de 2026.
- É a primeira vez que o valuation fica estável na sequência de ofertas de recompra da OpenAI.
- Nas duas ofertas anteriores, a OpenAI trouxe compradores externos como Thrive Capital e SoftBank para adquirir as ações.
- Desta vez a OpenAI usou o próprio caixa, segundo duas pessoas a par dos termos.
- A OpenAI protocolou seu prospecto de IPO (abertura de capital) de forma confidencial na SEC em junho de 2026.
- A empresa não divulgou data de listagem.
- Analistas leem a oferta de recompra e o preço estável como sinal de que um IPO não é iminente.
- A oferta anterior foi de US$6,6 bilhões a um valuation de US$500 bilhões, em outubro de 2025.
- Antes dela houve uma oferta de US$1,5 bilhão ao SoftBank em novembro de 2024, quando a empresa valia US$157 bilhões.
- O valor de US$7 bilhões foi noticiado primeiro pela Bloomberg.
- A OpenAI não quis comentar.
**Fontes:**
- [S20] CNBC — https://www.cnbc.com/2026/08/10/openai-wraps-7-billion-share-sale-ahead-of-potential-ipo-.html
- [S21] TechCrunch — https://techcrunch.com/2026/08/10/openai-reportedly-completed-a-7-billion-employee-tender-offer/
- [S22] Tech Funding News — https://techfundingnews.com/openai-closes-7b-tender-offer-at-852b-valuation-ahead-of-potential-ipo/
- [S23] Quartz — https://qz.com/openai-7-billion-employee-stock-tender-offer-ipo-081126

## Anthropic — preço do Claude Sonnet 5 fica permanente
- A Anthropic disse em 10 de agosto que vai tornar permanente o preço introdutório do Claude Sonnet 5.
- O preço mantido é de US$2 por milhão de tokens de input e US$10 por milhão de tokens de output.
- O preço introdutório valeria apenas até 31 de agosto, e depois disso subiria.
- A Anthropic lançou o Sonnet 5 em junho.
- A empresa apresentou o modelo como seu Sonnet mais agêntico até então.
- Segundo a Anthropic, o modelo faz planos, usa ferramentas como navegadores e terminais e roda de forma autônoma em um nível que, poucos meses antes, exigia modelos maiores e mais caros.
**Fontes:**
- [S24] X — https://x.com/claudeai/status/2086891169217122586
- [S25] X — https://x.com/claudeai/status/2072017450611142835

## Nvidia — Nemotron 3.5 Lightning e o roteador NeMo Switchyard
- A Nvidia lançou o Nemotron 3.5 Lightning, um modelo aberto de mistura de especialistas (MoE) com 30 bilhões de parâmetros e 3 bilhões de parâmetros ativos.
- O modelo é otimizado para execução de alto volume e baixa latência em agentes de IA sempre ligados e fluxos de trabalho agênticos.
- A Nvidia afirma que o Lightning entrega output até 4x mais rápido do que modelos comparáveis de sua categoria.
- A Nvidia diz que o modelo completa tarefas agênticas cerca de 30% mais rápido que o Qwen3.6-35B com precisão equivalente.
- Junto do modelo, a Nvidia lançou o NeMo Switchyard, uma biblioteca de roteamento de código aberto que envia cada etapa de um fluxo de agente ao modelo mais adequado.
- A Nvidia diz que a combinação mantém taxa de conclusão de tarefas em nível de fronteira e corta os custos de benchmark para cerca de um terço do custo de rodar apenas o Opus 4.8.
- Pesos, dados de treino e receitas foram publicados sob a licença permissiva OpenMDW-1.1.
- O modelo está disponível no Hugging Face, no ModelScope, no OpenRouter e no build.nvidia.com como microsserviço NIM.
- Entre os parceiros do Switchyard estão os frameworks de agentes Cognition, LangChain e Nous Research, que chamam o Switchyard diretamente.
- Também são parceiros os gateways de LLM Kong, LiteLLM e OpenRouter, que embutiram suporte ao Switchyard em seus produtos.
- O modelo estende a arquitetura híbrida Mamba-Transformer com MoE latente que a Nvidia introduziu com a família Nemotron 3.
- O modelo foi desenhado para harnesses de agentes como OpenClaw e Hermes Agent, apoiados pela pilha open source de segurança e gestão NemoClaw, da Nvidia, para rodar agentes sempre ligados.
**Fontes:**
- [S26] NVIDIA Technical Blog — https://developer.nvidia.com/blog/nvidia-nemotron-3-5-lightning-delivers-fast-accurate-specialized-task-execution-for-long-running-agents/?nvid=nv-csfg-698644
- [S27] NVIDIA Blog — https://blogs.nvidia.com/blog/nemotron-lightning-switchyard-rtx-dgx/
- [S28] VentureBeat — https://venturebeat.com/orchestration/nvidias-switchyard-router-reshuffles-ai-models-mid-task-cutting-task-costs-to-a-third

## Nvidia — plataformas de financiamento de US$500 bilhões com Wall Street
- A Nvidia anunciou em 10 de agosto de 2026 parcerias estratégicas para criar plataformas independentes de financiamento de poder computacional.
- Os parceiros são Apollo, BlackRock, Blackstone, Brookfield, Goldman Sachs e KKR.
- O objetivo é mobilizar mais de US$500 bilhões em capital de terceiros para a construção de infraestrutura de IA ao longo do tempo.
- Os acordos são memorandos de entendimento, não contratos finais.
- A Nvidia afirma que as parcerias "permanecem sujeitas à assinatura dos acordos definitivos".
- A estrutura permite que clientes da Nvidia — hyperscalers, laboratórios de IA de fronteira e empresas — financiem GPUs e data centers com crédito institucional e capital privado, em vez de usar o próprio balanço.
- O modelo usa crédito institucional, fundos de seguradoras e capital privado para bancar GPUs e data centers.
- Larry Fink, CEO da BlackRock, chamou o projeto de início do "próximo futuro da engenharia financeira".
- Fink comparou a iniciativa à criação dos títulos lastreados em hipotecas nos anos 1970.
- Jon Gray, presidente da Blackstone, disse que o poder computacional para IA será visto como uma "classe de ativo financiável", do mesmo modo como credores hipotecários enxergam imóveis.
- Gray disse à CNBC que a demanda por IA está superando a oferta.
- Segundo Gray, o uso de IA nas empresas do portfólio da Blackstone cresceu sete vezes neste ano.
- A Nvidia não divulgou os termos financeiros, os compromissos de investimento de cada firma nem um cronograma para desembolsar os US$500 bilhões previstos.
**Fontes:**
- [S29] NVIDIA Newsroom — https://nvidianews.nvidia.com/news/nvidia-partners-with-apollo-blackrock-blackstone-brookfield-goldman-sachs-and-kkr-to-establish-ai-compute-infrastructure-financing-platforms-to-mobilize-over-500-billion-of-third-party-capital
- [S30] CNBC — https://www.cnbc.com/2026/08/10/nvidia-wall-street-asset-managers-500-billion-ai-push.html
- [S31] Reuters via Yahoo Finance — https://finance.yahoo.com/technology/ai/articles/wall-street-giants-partner-nvidia-163441421.html
- [S32] KKR — https://media.kkr.com/news-details?news_id=2fdd2c1c-a052-4552-aa58-90d7a3d997e0

## Intel — oferta de ações ampliada para US$20 bilhões
- A Intel precificou 210.526.315 ações a US$95 cada.
- A oferta pública subscrita foi ampliada para US$20 bilhões, ante os US$15 bilhões anunciados no dia anterior.
- A venda de ações atraiu mais de US$100 bilhões em demanda, segundo pessoas a par do assunto.
- O preço de US$95 representa um desconto de 6,5% em relação ao fechamento de sexta-feira.
- Os recursos líquidos devem somar aproximadamente US$19,7 bilhões.
- A Intel pretende usar os recursos para fins corporativos gerais, o que pode incluir investimentos de capital e capital de giro.
- A oferta deve ser fechada em 12 de agosto de 2026.
- Os bancos coordenadores receberam uma opção de 30 dias para comprar até 31.578.947 ações adicionais ao preço da oferta, descontadas as comissões de colocação.
- As ações da Intel caíram mais de 4% na segunda-feira, quando a oferta inicial de US$15 bilhões foi revelada.
- As ações subiram cerca de 1% na negociação pré-mercado de terça-feira, após a precificação ampliada.
**Fontes:**
- [S33] Business Wire via Yahoo Finance — https://finance.yahoo.com/markets/stocks/articles/intel-announces-upsize-pricing-20-063600058.html
- [S34] Bloomberg — https://www.bloomberg.com/news/articles/2026-08-10/intel-is-said-to-near-share-sale-upsize-to-raise-20-billion
- [S35] Quartz — https://qz.com/intel-stock-offering-20-billion-ai-chips-081126

## TSMC e Sony — joint venture de sensores de imagem em Kumamoto
- Em 11 de agosto de 2026, a Sony Semiconductor Solutions e a TSMC anunciaram a assinatura de um acordo definitivo juridicamente vinculante.
- O acordo estabelece a Advanced Vision Semiconductor Manufacturing Corporation, uma joint venture em Koshi City, na província de Kumamoto, no Japão.
- A Sony vai aportar cerca de 465 bilhões de ienes (cerca de US$2,92 bilhões) em dinheiro e ativos.
- O aporte da Sony inclui sua fábrica de chips recém-construída em Kumamoto, transferida por meio de uma cisão societária.
- A TSMC vai aportar cerca de 282 bilhões de ienes em dinheiro.
- O aporte combinado é de US$4,69 bilhões.
- A joint venture vai fabricar sensores de imagem para smartphones usando tecnologia de processo avançada.
- A produção em volume deve começar em 2029.
- A Sony será a única acionista controladora e vai consolidar a joint venture como subsidiária do Sony Group.
- O Diretor Representante da joint venture será indicado pela Sony.
- Os aportes de capital serão feitos em fases, conforme a demanda de mercado.
- Os investimentos adicionais necessários para atingir a capacidade de produção planejada estão sendo considerados sob a premissa de apoio do governo japonês.
- A criação da joint venture e a conclusão da transação dependem das aprovações regulatórias necessárias.
- O acordo definitivo segue um memorando de entendimento não vinculante assinado pelas duas empresas em 8 de maio de 2026.
**Fontes:**
- [S36] TSMC — https://pr.tsmc.com/english/news/3333
- [S37] SEC EDGAR — https://www.sec.gov/Archives/edgar/data/313838/000110465926093634/tm2622696d1_6k.htm
- [S38] Nikkei Asia — https://asia.nikkei.com/business/business-deals/tsmc-and-sony-announce-image-sensor-joint-venture-in-japan

## Unitree — IPO em Xangai com procura 8.288 vezes maior que a oferta
- A Unitree Robotics informou em 10 de agosto de 2026, dia em que abriram as reservas online, que a fatia de varejo de seu IPO no STAR Market teve procura cerca de 8.288,82 vezes maior que a oferta.
- A demanda acionou um mecanismo de realocação de ações (clawback).
- Mais de 9,78 milhões de contas de varejo enviaram pedidos válidos por 53,64 bilhões de ações.
- A taxa final de sucesso no rateio online ficou em 0,0181%, cerca de um em cada 5.525 candidatos.
- A empresa precificou 40,45 milhões de ações a 150,8 iuanes (US$22,35) cada.
- A oferta levanta 6,10 bilhões de iuanes (cerca de US$904 milhões).
- O preço avalia a Unitree em cerca de 61 bilhões de iuanes (US$9 bilhões).
- O pagamento é devido até 12 de agosto.
- A Unitree será a primeira fabricante de robôs humanoides da China listada no mercado doméstico.
- O preço implica 219 vezes o lucro de 2025 e cerca de 36 vezes as vendas.
- Um relatório da Smart Analytics Global divulgado no mesmo dia estimou os embarques de humanoides da Unitree em cerca de 5.900 unidades no primeiro semestre de 2026.
- Os embarques cresceram 170% na comparação anual e representaram 31% do total mundial.
- A Unitree ficou em segundo lugar no ranking mundial, atrás da também chinesa AGIBOT.
- O mecanismo de realocação transferiu 3,2 milhões de ações da fatia institucional para a de varejo.
- A alocação final online subiu para 9,7 milhões de ações.
- A fatia institucional teve procura 2.760,67 vezes maior que a oferta.
**Fontes:**
- [S39] Reuters via The Star — https://www.thestar.com.my/tech/tech-news/2026/08/10/unitree039s-shanghai-ipo-more-than-8000-times-oversubscribed-by-retail-investors
- [S40] Global Times — https://www.globaltimes.cn/page/202608/1367902.shtml
- [S41] Reuters via SRN News — https://srnnews.com/unitrees-shanghai-ipo-more-than-8000-times-oversubscribed-by-retail-investors/
- [S42] TechGolly — https://techgolly.com/unitree-robotics-ipo-ignites-shanghai-market-with-5526-times-retail-oversubscription

## IBM e Together AI — cluster de inferência de US$240 milhões
- A IBM anunciou em 11 de agosto de 2026 um acordo plurianual de US$240 milhões com a Together AI.
- O acordo prevê a implantação de um grande cluster de sistemas Nvidia HGX B300 na IBM Cloud.
- A disponibilidade é esperada para o primeiro trimestre de 2027.
- É o primeiro cluster dedicado de grande escala construído para inferência na IBM Cloud.
- O cluster usa sistemas HGX B300 e rede Ethernet Nvidia Spectrum-X.
- Segundo a Nvidia, a combinação foi construída para entregar 30x mais produção de fábrica de IA em relação às gerações anteriores.
- A Together AI vai usar o cluster para servir inferência de modelos de código aberto a clientes corporativos.
- A plataforma da Together AI processa hoje cerca de 400 trilhões de tokens por mês.
- O acordo coloca a IBM no mercado de neoclouds ao transformar a Together AI em grande inquilina de nuvem em vez de concorrente direta.
- O acordo estende uma parceria IBM-Nvidia anunciada em março para levar GPUs Blackwell Ultra à IBM Cloud.
- A Together AI disse ter escolhido IBM e Nvidia pelos roadmaps de produto e pela velocidade de entrega de capacidade de GPU ao menor custo possível por token.
**Fontes:**
- [S43] PR Newswire (IBM) — https://www.prnewswire.com/news-releases/ibm-and-together-ai-sign-multi-year-agreement-to-scale-open-source-ai-inference-with-nvidia-ai-infrastructure-on-ibm-cloud-302847748.html
- [S44] Yahoo Finance — https://finance.yahoo.com/technology/ai/articles/ibms-240m-together-ai-deal-130423231.html
- [S45] Techzine — https://www.techzine.eu/news/infrastructure/143545/ibm-builds-240-million-inference-cluster/

## Petróleo — alta de 5% com impasse entre Trump e Irã sobre Ormuz
- Os futuros do Brent fecharam em alta de US$4,17, ou 4,99%, a US$87,72 o barril em 10 de agosto.
- Os futuros do West Texas Intermediate americano fecharam em alta de US$3,95, ou 5,05%, a US$82,13.
- Foram os maiores ganhos percentuais para os dois contratos desde 29 de julho.
- A alta reverteu a queda da semana anterior, quando os dois referenciais recuaram mais de 7%.
- A queda tinha vindo da expectativa de que Irã e Omã estivessem perto de um acordo para reabrir o Estreito de Ormuz.
- O estreito escoava um quinto do petróleo e do gás natural liquefeito do mundo antes do início do conflito no Oriente Médio, no fim de fevereiro.
- O presidente Donald Trump disse que o Irã deve pagar indenização por "todas as pessoas que eles mataram e feriram gravemente".
- Teerã, por sua vez, exige reparações de guerra, o fim das sanções e a suspensão do bloqueio naval americano antes de reabrir o estreito.
- Os estoques de petróleo bruto na Reserva Estratégica de Petróleo dos EUA caíram cerca de 6,1 milhões de barris na semana passada, para 298,7 milhões de barris.
- É o nível mais baixo desde janeiro de 1983, segundo dados do Departamento de Energia dos EUA.
- A consultoria Energy Aspects disse em 10 de agosto que apenas cinco embarcações por dia, em média, estão cruzando Ormuz.
- O número está bem abaixo dos 14 navios por dia registrados depois do memorando de entendimento entre EUA e Irã em junho.
- Militantes houthis reivindicaram um ataque à refinaria de Jazan, na Arábia Saudita, no dia anterior.
- O Brent está cerca de 16% acima dos níveis anteriores à guerra.
- Entre 4 e 6 de agosto, o tráfego pelo estreito ficou entre oito e 15 embarcações por dia, segundo a plataforma de rastreamento marítimo MarineTraffic.
- Antes do conflito, o estreito registrava cerca de 130 travessias.
**Fontes:**
- [S46] Reuters — https://lufkindailynews.com/news_reuters/business/oil-rises-4-as-iran-us-both-demand-compensation-and-hormuz-hopes-fade/article_189dacca-2e0d-52ed-8b0a-9d4254b596de.html
- [S47] Barchart — https://www.barchart.com/story/news/3761838/crude-prices-soar-as-strait-of-hormuz-reopening-in-doubt
- [S48] Al Jazeera — https://www.aljazeera.com/economy/2026/8/10/oil-prices-climb-as-iranian-demands-cloud-outlook-for-strait-of-hormuz

## Archer Aviation — compra de Wisk, Insitu e SkyGrid da Boeing
- A Boeing e a Archer Aviation anunciaram em 10 de agosto a assinatura de acordos definitivos.
- Pelos acordos, a Archer vai adquirir as subsidiárias Wisk Aero, SkyGrid e Insitu da Boeing.
- A Wisk Aero desenvolve eVTOL (aeronaves elétricas de decolagem e pouso vertical) autônomos.
- A SkyGrid faz software de gestão de espaço aéreo.
- A Insitu fabrica drones militares.
- A Insitu é um negócio de defesa lucrativo, com mais de US$200 milhões de receita anual e operações em 35 países.
- A Insitu já fabricou mais de 3.500 sistemas de aeronaves não tripuladas.
- A Insitu fica em Bingen, no condado de Klickitat, no estado de Washington, e tem escritórios nos EUA, na Austrália, no Reino Unido e nos Emirados Árabes Unidos.
- A transação é integralmente em ações e torna a Boeing a maior acionista externa da Archer, com participação de quase 20%.
- A Boeing também concordou em investir até US$55 milhões em uma futura rodada de captação da Archer.
- A Boeing vai receber warrants para comprar até US$200 milhões em ações da Archer no futuro.
- A Boeing ganha o direito de indicar um membro do conselho.
- A Boeing mantém acesso à tecnologia central de voo autônomo da Wisk para aeronaves comerciais e de defesa atuais e de próxima geração, por meio de um acordo de compartilhamento tecnológico.
- A Archer diz que a combinação cria uma "plataforma de IA física de ponta a ponta" ao lado do seu modelo de fundação para aeroespacial e defesa, o ZEE.
- As ações da Archer subiram cerca de 20%, a US$6,69, em 10 de agosto.
- As concorrentes se moveram pouco: Joby subiu 2%, EHang caiu 1% e a Boeing ficou praticamente estável.
- A Archer entrou no pregão com queda de 26% no ano.
- Nos resultados do segundo trimestre, divulgados no mesmo dia, a Archer registrou US$5 milhões de receita e prejuízo líquido de US$263,2 milhões.
- O prejuízo aumentou ante os US$217,7 milhões do trimestre anterior.
- A Archer encerrou o período com US$1,56 bilhão em liquidez.
- Só a Insitu somaria mais receita anual do que toda a receita trimestral da Archer quando o negócio for concluído.
- A conclusão é esperada até o fim do ano, sujeita à análise antitruste sob a lei Hart-Scott-Rodino.
**Fontes:**
- [S49] Archer Aviation — https://www.investors.archer.com/news/news-details/2026/Archer-to-Shape-Physical-AI-Future-of-Aerospace-and-Defense-with-Acquisition-of-Boeings-Wisk-Aero-Insitu-and-SkyGrid-Subsidiaries-Boeing-to-Invest-in-Archer-and-Collaborate/default.aspx
- [S50] The Seattle Times — https://www.seattletimes.com/business/boeing-aerospace/boeing-is-selling-flying-taxi-venture-wisk-wa-based-insitu-to-archer/
- [S51] The Air Current — https://theaircurrent.com/industry-strategy/archer-acquires-wisk-skygrid-insitu-from-boeing/
- [S52] Yahoo Finance — https://finance.yahoo.com/markets/stocks/articles/archer-aviation-soars-20-boeing-135854785.html
- [S53] 24/7 Wall St. — https://247wallst.com/cards/archer-aviation-inc-q2-2026-earnings-achr-01kzpmtp87xv6hzce8s5r5awvz

## Brasil — IPCA de julho em 0,07% e inflação de volta abaixo do teto
- O IBGE informou em 11 de agosto que o IPCA subiu 0,07% em julho.
- O índice desacelerou ante os 0,16% de junho.
- É a menor taxa para meses de julho em quatro anos, desde 2022.
- A inflação em 12 meses caiu para 4,44%, ante 4,64% nos 12 meses anteriores.
- A taxa voltou a ficar abaixo do teto da meta de inflação do Banco Central, de 4,5%, depois de furar o teto em maio.
- No acumulado do ano, a inflação chega a 3,44%.
- O grupo Habitação teve a maior alta e o principal impacto sobre o índice, com avanço de 0,99% e contribuição de 0,15 ponto percentual.
- O resultado foi puxado pela energia elétrica residencial, que acelerou de 1,53% em junho para 3,09% em julho.
- O grupo Alimentação e Bebidas caiu 0,67%.
- O tomate ficou 29,09% mais barato, a batata recuou 19,59% e a cenoura caiu 14,41%.
- Foi o quarto mês consecutivo de desaceleração.
- Foi o menor resultado mensal desde agosto de 2025, quando o IPCA marcou 0,11%.
- O número veio em linha com a mediana de 0,07% do boletim Focus do Banco Central publicado em 10 de agosto.
- O mercado ainda espera IPCA de 5,02% para o fim de 2026.
**Fontes:**
- [S54] Folha de S.Paulo — https://www1.folha.uol.com.br/mercado/2026/08/inflacao-desacelera-a-007-em-julho-e-fica-abaixo-do-teto-da-meta.shtml
- [S55] CBN / Globo — https://cbn.globo.com/economia/noticia/2026/08/11/ipca-desacelera-para-007percent-em-julho-e-inflacao-em-12-meses-fica-abaixo-do-teto-da-meta.ghtml
- [S56] Agência Brasil — https://www.jornalcorreiodonorte.com.br/politica-e-economia/2026/08/2617753-inflacao-recua-para-007-em-julho-e-volta-para-meta-do-governo.html

## Singapura — projeção de crescimento elevada para 4,5%-5,5% com o boom de IA
- O Ministério do Comércio e Indústria de Singapura disse em 11 de agosto que espera crescimento do PIB entre 4,5% e 5,5% em 2026.
- A projeção anterior era de 2% a 4%.
- Beh Swan Gin, secretário permanente do ministério, disse em coletiva virtual em 11 de agosto que o boom global de investimento em IA foi mais forte que o esperado desde a projeção anterior, feita em maio.
- Segundo ele, isso dá impulso significativo à produção e às exportações ligadas a IA.
- É a segunda revisão para cima da projeção, que foi fixada em 2%-4% em fevereiro, antes da eclosão da guerra no Irã.
- A projeção original, feita no ano passado, era de 1%-3%.
- O PIB final do segundo trimestre cresceu 5,9% na comparação anual, acima da estimativa prévia de 5,7%.
- As indústrias produtoras de bens se expandiram 10,5%, ante 7,9% no primeiro trimestre.
- A indústria de transformação acelerou para 12,5% de crescimento, ante 7,3%.
- O crescimento do primeiro semestre ficou em 6,1%.
- As exportações-chave subiram 27,4% no segundo trimestre, puxadas pela demanda por semicondutores e eletrônicos para IA.
- A demanda ajudou a compensar os efeitos negativos da guerra no Irã e das tarifas comerciais americanas.
- Economistas privados acompanharam o governo: o Maybank elevou sua projeção para 2026 a 5,2%, ante 4,8%.
- O UOB elevou sua projeção para 5%, ante 4,8%.
- O RHB manteve sua projeção em 4,5%, citando riscos remanescentes.
**Fontes:**
- [S57] The Straits Times — https://www.straitstimes.com/business/singapore-upgrades-2026-growth-forecast-to-4-5-to-5-5-on-stronger-ai-boom
- [S58] The Edge Singapore — https://www.theedgesingapore.com/news/singapore-economy/singapore-raises-growth-forecast-high-55-ai-boom
- [S59] Trading Economics / Statistics Singapore — https://tradingeconomics.com/singapore/gdp-growth-annual
- [S60] The Straits Times — https://www.straitstimes.com/business/singapores-key-exports-rise-27-4-in-q2-as-ai-lifts-electronics-shipments

## Banco central da Austrália — juros mantidos em 4,35%
- O Conselho de Política Monetária do Reserve Bank of Australia manteve a taxa básica em 4,35% em 11 de agosto.
- A decisão vem depois de três altas ao longo de 2026.
- O conselho disse que a inflação segue "alta demais".
- A inflação não deve voltar ao redor do ponto médio de 2,5% da faixa de meta antes do fim de 2027.
- O conselho alertou que há riscos de alta para essa projeção e que pode elevar mais os juros se esses riscos se materializarem.
- O RBA reduziu sua projeção de inflação cheia para dezembro a 3,6%, ante 4% na estimativa anterior.
- A projeção de inflação de núcleo por média aparada caiu para 3,3%, ante 3,5%.
- A revisão veio depois de o choque do petróleo causado pelo conflito no Oriente Médio ter repassado menos que o temido.
- A decisão foi unânime, revertendo a divisão de 8 a 1 registrada em maio.
- O banco disse que a oferta global de petróleo vai levar tempo para se recuperar.
- Segundo o RBA, há indicações de que os preços mais altos de combustível estão sendo repassados a outros bens e serviços, somando-se diretamente à inflação, além das pressões domésticas de capacidade.
- O RBA observou que o crescimento nos principais parceiros comerciais da Austrália foi mais forte que o esperado, porque o impulso do investimento ligado a IA superou os efeitos adversos do conflito no Oriente Médio.
**Fontes:**
- [S61] Reserve Bank of Australia — https://www.rba.gov.au/media-releases/2026/mr-26-19.html
- [S62] Proactive Investors — https://www.proactiveinvestors.com/companies/news/1096845/rba-holds-cash-rate-at-4-35-as-inflation-eases-but-further-hike-remains-on-table-1096845.html
- [S63] Reserve Bank of Australia — https://www.rba.gov.au/publications/smp/2026/aug/financial-conditions.html

## MoonLake — sonelokimabe atinge todos os desfechos na fase 3
- A MoonLake Immunotherapeutics informou em 10 de agosto que o ensaio de fase 3 IZAR-1 do sonelokimabe atingiu todos os desfechos clínicos na semana 16.
- O ensaio envolveu adultos com artrite psoriásica ativa que nunca haviam usado biológicos.
- O desfecho primário foi atingido com 42,1% dos pacientes tratados com 60 mg de sonelokimabe com indução alcançando resposta ACR50.
- 66,5% dos pacientes alcançaram ACR20 e 41,2% atingiram atividade mínima de doença (MDA) na semana 16.
- Entre os pacientes com envolvimento de pele concomitante, 61% atingiram PASI90 na semana 16.
- Pelo protocolo de abertura de dados acordado com a FDA (agência reguladora de medicamentos dos EUA), foram divulgadas apenas as taxas de resposta absolutas do braço de 60 mg.
- As comparações contra placebo seguem cegas até a conclusão do programa de fase 3.
- A análise cega de segurança do IZAR-1 apontou perfil consistente com estudos clínicos anteriores, sem novos sinais de segurança.
- Os ensaios IZAR-1 e IZAR-2 somam cerca de 1.500 adultos.
- O IZAR-2 testa pacientes refratários a inibidores de TNF, como o Humira da AbbVie, e compara o sonelokimabe diretamente com o Skyrizi (risanquizumabe), também da AbbVie.
- O IZAR-2 deve concluir o recrutamento no terceiro trimestre de 2026.
- A MoonLake encerrou o segundo trimestre com US$537,0 milhões em caixa, equivalentes de caixa e títulos de dívida negociáveis de curto prazo.
- A empresa projeta caixa suficiente até meados de 2028.
- A MoonLake espera protocolar o pedido de licença de produto biológico (BLA) até o fim de setembro de 2026 para sua indicação principal.
**Fontes:**
- [S64] MoonLake Immunotherapeutics — https://ir.moonlaketx.com/news-releases/news-release-details/moonlake-announces-positive-topline-results-phase-3-izar-1-trial
- [S65] Fierce Biotech — https://www.fiercebiotech.com/biotech/moonlakes-nanobody-boosts-all-clinical-endpoints-phase-3-psoriatic-arthritis
- [S66] Dermatology Times — https://www.dermatologytimes.com/view/sonelokimab-meets-primary-end-point-in-phase-3-psoriatic-arthritis-trial
- [S67] MarketScreener / S&P Capital IQ — https://sa.marketscreener.com/news/moonlake-immunotherapeutics-reports-positive-topline-results-from-the-phase-3-izar-1-trial-of-sonelo-ce7859dadb8eff21

## Justiça dos EUA — milhares de ações por vício de jovens em redes sociais avançam
- A 9ª Corte de Apelações dos EUA decidiu em 10 de agosto que Meta, Google (da Alphabet), TikTok (da ByteDance) e Snap terão de enfrentar mais de 3.000 processos federais.
- As ações alegam que as empresas projetaram suas plataformas para viciar usuários jovens.
- A corte, sediada em San Francisco, rejeitou o pedido das empresas de reverter uma decisão de instância inferior, concluindo que o recurso veio cedo demais no litígio.
- O painel entendeu que a Seção 230 da Lei de Decência nas Comunicações de 1996 oferece uma defesa contra responsabilização, e não imunidade contra ser processado.
- Com isso, o recurso interlocutório das empresas foi considerado prematuro.
- A juíza Jacqueline Hong-Ngoc Nguyen escreveu que a Meta argumenta que essa imunidade deveria ser implícita, e que a corte discorda.
- A corte também negou o pedido da Meta de adiar um julgamento movido por 29 procuradores-gerais estaduais.
- Esse processo alega que a empresa coletou e usou ilegalmente dados de crianças, projetou plataformas para manter jovens fisgados e enganou consumidores sobre segurança.
- Os casos federais foram movidos por estados, municípios, distritos escolares e indivíduos.
- Os casos federais estão centralizados perante a juíza federal Yvonne Gonzalez Rogers, em Oakland, na Califórnia.
- As ações pedem indenizações, multas e restituição.
- Cerca de 3.300 processos adicionais estão consolidados na Justiça estadual da Califórnia.
- Em março, um júri de Los Angeles considerou Meta e Google negligentes por projetar plataformas que causam danos a jovens e concedeu US$6 milhões a um autor de 20 anos.
- Um júri do Novo México condenou a Meta a pagar US$375 milhões por ter enganado consumidores sobre a segurança de suas plataformas.
- Na semana passada, um juiz concluiu que a Meta criou um dano coletivo (public nuisance) e ordenou o pagamento de US$567 milhões adicionais.
**Fontes:**
- [S68] Reuters — https://www.yahoo.com/news/us/articles/us-appeals-court-allows-thousands-161341261.html
- [S69] CBS News — https://www.cbsnews.com/news/social-media-addiction-lawsuits-court-rules/
- [S70] The Next Web — https://thenextweb.com/news/social-media-addiction-lawsuits-ninth-circuit-section-230
