# Fatos — Newsletter [Tech] 22 de Setembro de 2026

## Anthropic — Claude Opus 5.5
- A Anthropic lançou o Claude Opus 5.5 na terça-feira, 22 de setembro de 2026.
- A empresa afirma que o Opus 5.5 iguala o Claude Fable 5.1 "na maioria das tarefas".
- A Anthropic diz que o Opus 5.5 custa cerca de 40% menos para rodar do que o Opus 5.
- Claude Sonnet 5.5 e Haiku 5.5 são esperados nas próximas semanas.
- O Opus 5.5 custa US$4 por milhão de tokens de input e US$20 por milhão de tokens de output.
- Os preços anteriores do Opus 5 eram US$5 por milhão de tokens de input e US$25 por milhão de tokens de output.
- A mudança representa um corte de 20% no preço por token.
- O custo de leitura de cache caiu 60%, para US$0,20 por milhão.
- Nos benchmarks da Anthropic, o Opus 5.5 marca 66,4% no Terminal-Bench 4.0.
- No mesmo teste, o Fable 5.1 marca 55,8% e o GPT-6 Astra, 57,9%.
- O Opus 5.5 marca 54,4% no FrontierCode v1.1.
- O Opus 5.5 marca 1.846 no GDPval-AA v2.1, contra 1.735, 1.708 e 1.542 dos modelos comparados.
- É o primeiro modelo lançado pela Anthropic depois de o CEO Dario Amodei anunciar o plano de "ditar o ritmo da fronteira" (pace the frontier), ou seja, desacelerar o desenvolvimento de IA.
- A Anthropic diz que o Opus 5.5 traz melhorias em comportamentos de risco, incluindo tentativas de escapar do sandbox de testes da empresa.
- O Opus 5.5 carrega guardrails no estilo do Fable 5.1: pedidos ligados a cibersegurança sinalizados por classificadores são redirecionados ao Opus 4.8, menos potente.
- Pedidos ligados a biologia sinalizados pelos guardrails são redirecionados ao Opus 5.
- O modelo foi testado antes do lançamento por parceiros externos, incluindo a METR.
- A Anthropic afirma que o Opus 5.5 supera o GPT-6 Astra da OpenAI no FrontierCode a cerca de 20% do custo por tarefa.
- Os limites de uso de cinco horas para assinantes sobem 20%.
**Fontes:**
- [S1] The Verge — https://www.theverge.com/ai-artificial-intelligence/998868/anthropic-claude-opus-5-5-cybersecurity
- [S2] The Decoder — https://the-decoder.com/claude-opus-5-5-matches-fable-5-1-at-40-percent-lower-cost-as-anthropic-promises-to-fix-claudish-writing/

## Xiaomi — MiMo-V2.6 e pesos abertos sob licença MIT
- A Xiaomi lançou e abriu o código do MiMo-V2.6-Pro e do MiMo-V2.6-Flash em 21 de setembro de 2026.
- Os dois modelos saíram sob licença MIT, com os pesos disponíveis no Hugging Face.
- O Pro tem 1,02 trilhão de parâmetros totais, com 42 bilhões ativos.
- O Pro tem janela de contexto de 1 milhão de tokens.
- O MiMo-V2.6-Pro marcou 46,32 no Intelligence Index v4.3 da Artificial Analysis.
- A pontuação empata com a do Grok 4.7 e fica à frente de Kimi K3 e Qwen3.8 Max.
- Isso faz do MiMo-V2.6-Pro o modelo de pesos abertos com maior pontuação no lançamento.
- O Pro custa US$0,435 por milhão de tokens de input e US$0,87 por milhão de tokens de output na API da própria Xiaomi.
- É cerca de um quinto do preço do Grok 4.7, de US$2 e US$6 por milhão.
- O Flash custa US$0,14 por milhão de tokens de input e US$0,28 por milhão de tokens de output.
- A Xiaomi apresenta o lançamento como um passo no caminho da autoaprimoração recursiva (RSI), escalando poder computacional de aprendizado por reforço para que os modelos ampliem a própria fronteira de capacidade.
- A Xiaomi diz que o Pro empata com Claude Opus 5 e GPT-5.6 Sol na maioria dos benchmarks de agentes.
- A empresa reconhece que o Pro fica atrás de Fable 5.1 e GPT-6 Astra no conjunto geral.
- Os dois modelos são nativamente omnimodais: aceitam texto, imagem, vídeo e áudio na entrada e produzem texto.
- O Flash é um MoE esparso com 309 bilhões de parâmetros totais e 15 bilhões ativos.
- A Xiaomi também lançou uma variante Pro-UltraSpeed, que segundo a empresa gera até 20 vezes mais rápido com a mesma qualidade.
- A Xiaomi abriu ainda o relatório técnico, um modelo MiMo-V2.6-Distill-Qwen-9B e recursos de pesquisa em aprendizado por reforço.
**Fontes:**
- [S3] Xiaomi MiMo — https://mimo.mi.com/docs/en-US/news/latest/v2-6
- [S4] SiliconANGLE — https://siliconangle.com/2026/09/22/xiaomi-introduces-mimo-v2-6-series-open-source-ai-model-family/
- [S5] DataNorth — https://datanorth.ai/news/xiaomi-releases-mimo-v2-6-pro-and-flash
- [S6] Artificial Analysis — https://artificialanalysis.ai/models/mimo-v2-6-pro

## Alibaba — Qwen de 5 a 10 trilhões de parâmetros e autoaprimoramento
- Na Apsara Conference, em Hangzhou, em 22 de setembro de 2026, o CEO da Alibaba, Eddie Wu, disse que a equipe do Qwen planeja treinar um modelo de 5 trilhões a 10 trilhões de parâmetros.
- O objetivo declarado é lidar com "tarefas mais complexas e de horizonte mais longo" e avançar rumo à superinteligência artificial (ASI).
- A Alibaba disse que o modelo de próxima geração, o Qwen 4, está em treinamento.
- O roteiro prevê que Qwen 4.5 e Qwen 5 escalem para 5 a 10 trilhões de parâmetros.
- Em um experimento de autoaprimoramento recursivo, o Qwen3.8-Max rodou mais de um mês de ciclos totalmente automatizados.
- Os ciclos cobriram design de pipeline, validação de dados, experimentação e diagnóstico de erros.
- O modelo completou 33 iterações nesse período.
- A pontuação do Qwen3.8-Max na Artificial Analysis subiu de 40 para 45.
- Em um experimento de design de chips, o modelo se autoaprimorou por mais de 60 horas ao longo de todo o ciclo de projeto.
- Nesse experimento, o modelo fez mais de 10 mil chamadas a ferramentas EDA (software de automação de projeto eletrônico) para produzir módulos de barramento de chip em nível de produção.
- O resultado reduziu a área do chip em 42% sem perda de desempenho.
- O modelo de ponta atual da Alibaba, o Qwen 3.8 Max, tem 2,4 trilhões de parâmetros.
- O modelo planejado seria, portanto, cerca de duas a quatro vezes maior.
- Wu disse que a Alibaba Cloud mira mais de 20 GW de capacidade global de data centers até 2032.
- Wu afirmou que a demanda dos clientes por IA "supera em muito nossa capacidade de fornecimento".
**Fontes:**
- [S7] Alibaba Cloud — https://www.alibabacloud.com/en/press-room/alibaba-unveils-roadmap-on-full-stack-ai-strategy?_p_lc=1
- [S8] The Business Times — https://www.businesstimes.com.sg/companies-markets/telcos-media-tech/alibaba-plans-ai-model-5-trillion-10-trillion-parameters-unveils-new-chip
- [S9] ET Enterprise AI — https://enterpriseai.economictimes.indiatimes.com/news/industry/alibaba-plans-10-trillion-parameter-ai-model-unveils-new-chip/134411732
- [S10] TechNode Global — https://technode.global/2026/09/22/alibaba-20gw-data-center-capacity-2032-qwen-zhenwu-ai-roadmap/

## Snorkel AI — rodada de US$350 milhões para dados de treinamento
- A Snorkel AI levantou US$350 milhões com um valuation de US$3,5 bilhões.
- O CEO Alex Ratner informou a rodada à Reuters em 22 de setembro de 2026.
- O valor equivale a quase três vezes o valuation de US$1,3 bilhão da rodada anterior, de US$100 milhões, em maio de 2025.
- A rodada foi liderada por Insight Partners e S32.
- Os investidores já existentes Addition, Greylock e Wells Fargo participaram.
- A receita anualizada recorrente ultrapassou US$350 milhões.
- Um ano antes, essa receita anualizada era de cerca de US$20 milhões.
- O crescimento vem do negócio de dados como serviço lançado em setembro de 2025.
- A empresa foi fundada em 2019 por pesquisadores vindos do laboratório de IA de Stanford.
- A Snorkel vendia software e migrou para fornecer conjuntos de dados prontos e ambientes de aprendizado por reforço diretamente aos laboratórios de IA.
- A "plataforma agêntica de desenvolvimento de dados" da empresa combina especialistas humanos com milhares de modelos e agentes de IA especializados.
- Os especialistas desenham cenários, tarefas e rubricas de avaliação, enquanto a IA automatiza a maior parte do controle de qualidade.
- A empresa diz que o dinheiro vai financiar pesquisadores e engenheiros, crescimento em clientes corporativos e no governo federal americano e avaliações ampliadas de modelos de terceiros.
- A Snorkel afirma que espera atingir a lucratividade ainda este ano.
- A empresa é sediada em San Francisco.
**Fontes:**
- [S11] Reuters — https://www.reuters.com/legal/transactional/snorkel-ai-valued-35-billion-amid-surging-demand-complex-ai-training-data-2026-09-22/
- [S12] CNA — https://www.channelnewsasia.com/business/exclusive-snorkel-ai-valued-35-billion-amid-surging-demand-complex-ai-training-data-6402476
- [S13] Finimize — https://finimize.com/content/snorkel-ais-350-million-raise-puts-training-data-center-stage

## Shopify e Meta — checkout agêntico com o Muse
- O CEO da Shopify, Tobias Lütke, anunciou no X na segunda-feira, 21 de setembro de 2026, que a empresa está "firmando uma parceria profunda com o Muse para habilitar checkout agêntico com Shop Pay em todas as lojas Shopify".
- O acordo permite que o agente pessoal de IA da Meta conclua compras em nome dos usuários no conjunto de lojas da Shopify.
- As compras acontecem via Shop Pay, o checkout de um toque da Shopify, que guarda dados de entrega e cobrança.
- Mark Zuckerberg confirmou o acordo na segunda-feira.
- O chefe de IA da Meta, Alexandr Wang, disse que a empresa quer "dar aos nossos musers acesso a uma ampla gama de lojas".
- O movimento é o oposto do da Amazon: a Shopify abre sua base de lojistas ao Muse, enquanto a Amazon bloqueou o agente em seu site de varejo.
- Nenhuma das empresas revelou os termos financeiros da parceria.
- Também não há prazo divulgado para quando o checkout agêntico do Shop Pay chegará a todos os usuários do Muse.
- A Meta lançou o Muse, um agente pessoal de IA para celular, em setembro de 2026.
- O Muse vasculha o catálogo da Shopify em busca do melhor resultado para o pedido do comprador.
- O checkout é feito pelo Universal Commerce Protocol.
- Na prática, lojistas da Shopify passam a ser descobertos e comprados dentro do Muse por padrão.
**Fontes:**
- [S14] MarketWatch — https://www.marketwatch.com/story/shopify-to-use-meta-s-muse-for-agentic-checkout-451ab392
- [S15] The Paypers — https://thepaypers.com/payments/news/meta-partners-with-shopify-to-bring-shop-pay-checkout-to-muse-ai
- [S16] Finviz — https://finviz.com/news/394069/meta-partners-with-shopify-to-introduce-ai-powered-shopping-and-checkout-in-muse
- [S17] MT Newswires — https://www.bitgetapp.com/news/detail/12560605855936
- [S18] American Banker — https://www.americanbanker.com/payments/news/shopify-adds-meta-muse-to-agentic-ai-strategy

## Meta Muse — zero-day no aplicativo para macOS
- O pesquisador de segurança de macOS Patrick Wardle divulgou em 21 de setembro de 2026 um zero-day (falha explorável antes de existir correção) no aplicativo do Muse para Mac.
- A falha permite que qualquer aplicativo instalado localmente ou comando de terminal obtenha o token que autentica o usuário na sua conta Muse.
- O problema está em uma configuração não documentada chamada endo_voyager_dictation_endpoint.
- Qualquer processo local sem privilégios especiais pode reescrever essa configuração, sem precisar de permissões do macOS.
- A configuração controla para onde o tráfego de ditado do Muse é enviado, e pode ser apontada para um servidor controlado pelo atacante.
- Nas provas de conceito de Wardle, o agente sequestrado gravou arquivos maliciosos no disco.
- Ele também tirou fotos com a câmera.
- Ele obteve a localização de um iPhone vinculado.
- Em muitos casos, o usuário não recebia nenhuma indicação do que estava acontecendo.
- "Podemos manipular o agente e usar seus privilégios para fazer o que quisermos. Em vez de termos que escrever um ladrão de dados para Mac muito completo, podemos simplesmente usar o próprio assistente de IA", disse Wardle à Ars Technica.
- A Meta corrigiu a vulnerabilidade poucas horas depois da publicação da reportagem da Ars Technica.
- David Singleton, do Meta Superintelligence Labs, classificou o caso como escalada local de privilégios, não exploração remota, e disse que o risco prático era baixo.
- Wardle argumenta que a exploração tinha vetor remoto, por meio de um ataque de engenharia social no estilo ClickFix.
- Wardle observa que a API de ditado local da Apple teria evitado a falha por completo.
- Zuckerberg havia dito que o Muse foi "construído desde o início para privacidade e segurança".
**Fontes:**
- [S19] Ars Technica — https://arstechnica.com/security/2026/09/muse-metas-extraordinarily-privileged-ai-assistant-has-a-serious-0-day/
- [S20] The Verge — https://www.theverge.com/tech/998679/meta-muse-patch-zero-day-exploit-ai-agent
- [S21] 9to5Mac — https://9to5mac.com/2026/09/22/security-bite-the-last-24-hours-at-meta-were-not-a-musing/
- [S22] Malwarebytes — https://www.malwarebytes.com/blog/bugs/2026/09/metas-muse-ai-assistant-has-a-zero-day-that-can-turn-it-into-a-mac-backdoor

## China — investigação sobre DeepSeek e Moonshot por dados enviados ao Claude
- A Administração do Ciberespaço da China (CAC) investiga DeepSeek e Moonshot AI.
- A apuração busca determinar se o redirecionamento de consultas de usuários aos modelos Claude, da Anthropic, vazou dados sensíveis.
- A informação foi publicada pelo The Information em 22 de setembro de 2026.
- O regulador convocou representantes das sete empresas chinesas citadas em uma reportagem anterior para várias rodadas de interrogatório.
- As outras cinco empresas citadas são Alibaba, Zhipu, SenseTime, MiniMax e Xiaomi.
- A investigação segue acusações feitas pela Anthropic em setembro de que a DeepSeek redirecionou mais de 12,1 milhões de trocas ao Claude em um período de 14 dias em julho.
- Segundo a Anthropic, alguns usuários acreditavam estar conversando com os modelos da própria DeepSeek.
- A Anthropic também alegou que a Moonshot AI redirecionou quase 300 mil requisições de clientes ao Claude ao longo de 10 dias.
- Isso teria ocorrido por meio de 5.380 contas fraudulentas, a maioria registrada em Singapura e no Japão.
- A Anthropic afirma que a Moonshot capturou trocas para extrair capacidades de raciocínio e usá-las em treinamento.
- Os pedidos redirecionados envolveriam dados sobre instalações do Exército de Libertação Popular, dados policiais e de vigilância, sistemas corporativos internos e credenciais.
- As autoridades avaliam o caso à luz das regras chinesas de transferência de dados para fora do país.
- Nenhuma sanção foi anunciada.
- Separadamente, DeepSeek e Moonshot foram convidadas a fazer declarações em uma reunião do Conselho de Segurança da ONU sobre IA e segurança internacional em 23 de setembro.
- O CEO da OpenAI, Sam Altman, planeja se dirigir ao conselho nessa reunião.
**Fontes:**
- [S23] The News International — https://www.thenews.com.pk/latest/1417191-chinese-regulator-probes-deepseek-and-moonshot-over-secret-data-routing
- [S24] Let's Data Science — https://letsdatascience.com/news/china-probes-deepseek-and-moonshot-data-routing-740ed6c4
- [S25] The Information — https://www.theinformation.com/articles/china-probes-deepseek-moonshot-potential-data-leaks-anthropic
- [S26] The Straits Times — https://www.straitstimes.com/asia/deepseek-to-brief-un-security-council-on-ai-this-week-sources-say

## Alibaba — chip Zhenwu V900 e meta de 20 GW
- A Alibaba apresentou o Zhenwu V900 em 22 de setembro, na Apsara Conference, em Hangzhou.
- O CEO Eddie Wu chamou o chip de "o chip de IA mais potente da China hoje".
- As especificações declaradas incluem o triplo do desempenho do antecessor M890.
- O chip tem 216 GB de HBM (memória de alta largura de banda usada em aceleradores de IA).
- O chip tem 1,2 TB/s de largura de banda entre chips.
- O chip suporta precisão FP8 e FP4.
- O Zhenwu V900 escala até 500 mil chips por cluster.
- Os números são informados pelo fabricante e não foram verificados por benchmarks independentes.
- O chip foi desenvolvido pela T-Head, subsidiária de semicondutores da Alibaba.
- A produção em massa e o lançamento comercial estão previstos para o primeiro trimestre de 2027.
- O M890, lançado em maio de 2026, já entregou mais de 560 mil unidades a mais de 400 clientes externos.
- A Alibaba acompanhou o chip com um roteiro de 20 GW de poder computacional global até 2032.
- A empresa também anunciou o plano de treinar um modelo de 5 trilhões a 10 trilhões de parâmetros.
- Fabricantes chineses de GPUs e chips de IA ficaram com 41% do mercado local de servidores aceleradores de IA em 2025.
- Em 2022, essa participação era próxima de zero.
- A Huawei lidera com cerca de 62% de participação, e a Alibaba fica em torno de 5%.
- As ações da Alibaba subiram após o anúncio.
- O anúncio veio poucos dias depois de a fabricante de memória CXMT dizer que sua plataforma de chips mais recente estava entrando em produção em massa.
**Fontes:**
- [S27] Yahoo Finance — https://finance.yahoo.com/technology/ai/articles/alibaba-zhenwu-v900-china-answer-090729183.html
- [S28] Fortune — https://fortune.com/2026/09/22/alibaba-powerful-ai-chip-xi-trump-us/
- [S29] Semafor — https://www.semafor.com/article/09/22/2026/chinese-chips-advance-despite-being-shut-out-of-us-technology
- [S30] Reuters — https://www.reuters.com/business/retail-consumer/alibaba-plans-ai-model-with-5-trillion-10-trillion-parameters-unveils-new-chip-2026-09-22/

## Boston Dynamics — centro de treinamento do Atlas na fábrica da Hyundai
- A Boston Dynamics abriu o Robotics Metaplant Application Center (RMAC) em 21 de setembro.
- O centro fica dentro da Hyundai Motor Group Metaplant America (HMGMA), nos arredores de Savannah, no estado americano da Geórgia.
- Robôs Atlas estão sendo treinados em trabalho automotivo real.
- As tarefas incluem preparar a logística e o sequenciamento de peças antes de colocá-las na ordem correta de montagem.
- A montagem de componentes é a meta para 2030.
- No ano que vem, as operações se mudam para um novo prédio cerca de dez vezes maior que o centro atual.
- A Boston Dynamics planeja começar a explorar casos de uso em outros setores além do automotivo em 2027.
- A Hyundai afirmou que vai implantar o Atlas em sua rede global, começando com 25 mil unidades em fábricas da Hyundai Motor e da Kia nos próximos anos.
- O diretor de produto e tecnologia, Zack Jackowski, disse que a empresa está "abrindo caminho para a IA física em escala empresarial", junto com o Hyundai Motor Group.
- Jackowski afirmou que a compra do Robotics and AI Institute (RAI) da Hyundai pelo SoftBank não afetará o desenvolvimento do Atlas.
**Fontes:**
- [S31] Boston Dynamics — https://bostondynamics.com/news/boston-dynamics-opens-robotics-metaplant-application-center-to-train-humanoid-robots-for-manufacturing-tasks/
- [S32] The Robot Report — https://www.therobotreport.com/boston-dynamics-opens-metaplant-application-center-train-atlas-humanoid-robots/

## Cognex — compra da RealSense por US$500 milhões
- A Cognex anunciou em 22 de setembro um acordo definitivo para comprar a RealSense.
- A RealSense fabrica câmeras de sensoriamento de profundidade para percepção robótica.
- O preço é de aproximadamente US$500 milhões em dinheiro, financiado integralmente com caixa e investimentos do balanço da Cognex.
- Além do preço, a Cognex vai criar um programa de retenção em dinheiro de três anos no valor de US$56,5 milhões na meta para funcionários da RealSense.
- A Cognex também concederá aproximadamente US$50 milhões em ações restritas a esses funcionários.
- Com isso, o pacote total chega a cerca de US$600 milhões.
- A RealSense deve gerar de US$80 milhões a US$90 milhões de receita em 2026.
- Isso representa crescimento de mais de 50% sobre 2025.
- A RealSense foi criada dentro da Intel em 2014.
- A unidade foi desmembrada em julho de 2025, sob o comando do CEO Nadav Orbach.
- A unidade esteve prestes a ser fechada durante a reestruturação conduzida por Pat Gelsinger na Intel.
- A Cognex estima o mercado de percepção robótica em cerca de US$600 milhões hoje.
- A empresa projeta crescimento de mais de 25% ao ano, chegando a aproximadamente US$1,6 bilhão em 2030.
- A conclusão do negócio é esperada para o quarto trimestre de 2026.
- Antes do fechamento, a RealSense vai desmembrar sua linha de autenticação facial em uma empresa independente focada em biometria.
**Fontes:**
- [S33] PR Newswire / Cognex — https://www.prnewswire.com/news-releases/cognex-to-acquire-realsense-expanding-machine-vision-leadership-into-high-growth-robotic-perception-market-302885738.html
- [S34] Calcalist (CTech) — https://www.calcalistech.com/ctechnews/article/s1tqir19fl
- [S35] Stock Titan — https://www.stocktitan.net/sec-filings/CGNX/8-k-cognex-corp-reports-material-event-d2e9c367f48d.html

## Ligent Technologies — estreia em Hong Kong
- As ações da fabricante chinesa de equipamentos de fibra óptica Ligent Technologies subiram até 19,2% na estreia em Hong Kong, na terça-feira, 22 de setembro.
- O pico intradiário foi de HK$39,3 (US$5,01) por ação.
- A ação fechou o primeiro dia em alta de 4,6%, bem abaixo da máxima do dia.
- O IPO (oferta pública inicial de ações) levantou HK$5,67 bilhões (cerca de US$723 milhões).
- A empresa vendeu 172,01 milhões de ações a HK$32,96 (US$4,20) cada na oferta-base.
- Isso dava à Ligent um valor de mercado de cerca de HK$32,4 bilhões (US$4,13 bilhões) ao preço da oferta.
- A Ligent é controlada pelo conglomerado chinês Hisense Group Holding.
- A empresa havia mirado originalmente cerca de US$800 milhões na oferta.
- A companhia planeja gastar cerca de 52,9% dos recursos líquidos em P&D, sobretudo em produtos ópticos e chips mais rápidos.
- Outros 25,1% vão para a expansão da capacidade de produção.
- Em 2025 a Ligent foi a 5ª maior do mundo em receita com transceptores ópticos, com 4,0% de participação de mercado.
- No mesmo ano, foi a 3ª na China, com 10,1% de participação.
- A empresa produz em massa transceptores de 800G e 1,6T.
**Fontes:**
- [S36] The Standard — https://www.thestandard.com.hk/finance/article/343434/Ligent-Technologies-jumps-in-Hong-Kong-debut-outpacing-key-indices
- [S37] The Standard — https://www.thestandard.com.hk/finance/article/343434/Chinas-Ligent-closes-up-46pc-in-Hong-Kong-debut-as-AI-demand-draws-investors
- [S38] Nikkei Asia — https://asia.nikkei.com/business/markets/ipo/china-s-ligent-jumps-19-in-hong-kong-debut-as-ai-demand-draws-investors
- [S39] Reuters — https://www.reuters.com/business/media-telecom/chinas-ligent-technologies-seeks-723-million-hong-kong-ipo-2026-09-13/
- [S40] HKEXnews — https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0914/2026091400007.pdf

## Google e Georgia Power — 96 MW nucleares em Vogtle e Hatch
- A Georgia Power e o Google anunciaram em 21 de setembro um acordo em que o Google apoiará aumentos de potência (uprates) nas usinas nucleares de Vogtle e Hatch.
- As melhorias devem adicionar cerca de 96 megawatts de nova capacidade à rede elétrica.
- A assinatura do Google deve gerar cerca de US$900 milhões em benefícios aos clientes da Georgia Power ao longo da vida útil das unidades.
- O acordo foi protocolado na segunda-feira na Comissão de Serviços Públicos da Geórgia (Georgia PSC), nos processos 44280 e 56002.
- Os documentos criam uma nova estrutura tarifária Nuclear Uprate (NU-1), sob a qual o Google recebe Créditos de Emissão Zero.
- O acordo ainda depende da aprovação da comissão, incluindo um novo aumento estendido de potência (EPU) para Hatch 1 e 2.
- A Georgia Power disse aos reguladores que espera que a receita do Google gere "pressão para baixo" nas tarifas dos clientes.
- A empresa afirmou que também usaria créditos tributários federais e estaduais, além de uma garantia de empréstimo pendente do Departamento de Energia dos EUA, para compensar parte do custo das melhorias.
- A demanda crescente de data centers impulsiona a corrida para expandir usinas nucleares existentes.
- A Georgia Power já expande sua rede em ritmo sem precedentes.
**Fontes:**
- [S41] PR Newswire / Georgia Power — https://www.prnewswire.com/news-releases/georgia-power-agreement-with-google-to-provide-approximately-900-million-in-projected-benefits-for-customers-and-advance-nuclear-energy-in-georgia-302885197.html
- [S42] Atlanta Journal-Constitution — https://www.ajc.com/business/2026/09/georgia-power-is-upgrading-its-nuclear-reactors-and-google-is-buying-the-electricity/
- [S43] SRN News (Reuters) — https://srnnews.com/southern-co-unit-signs-deal-with-google-to-add-nuclear-capacity/
- [S44] POWER Magazine — https://www.powermag.com/google-georgia-power-have-deal-to-support-nuclear-power-plant-uprates/

## Kairos Power — investimento da Samsung C&T de até US$100 milhões
- A Kairos Power e a Samsung C&T anunciaram em 21 de setembro a assinatura de um term sheet vinculante.
- O documento prevê investimento estratégico e implantação comercial conjunta da tecnologia de reator de alta temperatura refrigerado a sal de flúor da Kairos.
- A Samsung C&T vai aportar até US$100 milhões em investimento direto e serviços de engenharia em espécie, sujeitos a aprovações regulatórias.
- Os recursos visam viabilizar a entrega da usina de demonstração Hermes 2, em Oak Ridge, no Tennessee.
- A Hermes 2 é um reator de 50 MWe conectado à rede.
- As obras começaram em abril de 2026.
- A usina vai fornecer 50 MW de eletricidade limpa à rede da TVA, sob um acordo de desenvolvimento de múltiplas usinas com o Google.
- O pacote inclui um investimento em participação acionária de US$70 milhões.
- O Google contratou a Kairos em 2024 para fornecer cerca de meio gigawatt de capacidade nuclear até 2035, à medida que data centers de IA elevam a demanda por eletricidade.
- A Samsung C&T já entregou 12 gigawatts em 10 unidades nucleares.
- Entre elas estão a usina de Barakah, nos Emirados Árabes Unidos, e as unidades 5 e 6 de Uljin, na Coreia do Sul.
**Fontes:**
- [S45] Kairos Power — https://www.kairospower.com/updates/kairos-power-and-samsung-c-t-agree-to-pursue-strategic-investment-and-collaboration-for-kp-fhr-deployment
- [S46] Tech Beat — https://techbeat.co/story/samsung-c-t-backs-kairos-power-with-up-to-100m-for-google-nuclear-reactor

## Verda — Série B de US$189 milhões na Finlândia
- A Verda, sediada em Helsinque, anunciou em 22 de setembro que levantou US$189 milhões (€163 milhões) em novo financiamento.
- A rodada inclui uma Série B sobressubscrita liderada pela Emergence Capital, além de investimento adicional.
- Entre os investidores estão MUFG Innovation Partners, Supermicro, Varma Mutual Pension Insurance, Lifeline Ventures, 6 Degrees Capital, byFounders e Tesi.
- Participaram também os investidores-anjo Ola Tørudbakken e Mark Saroufim.
- A rodada torna a Verda — antes chamada DataCrunch — o unicórnio mais recente da Europa, valendo pelo menos US$1 bilhão.
- A empresa não divulgou um valuation exato.
- A Verda atingiu US$165 milhões de receita anualizada recorrente em julho.
- A empresa planeja multiplicar sua capacidade de poder computacional no próximo ano.
- A Verda abriu recentemente escritórios em Londres e em San Francisco.
- Fundada em 2020, a Verda opera uma nuvem de IA de pilha completa, de data centers físicos e hardware até a plataforma e a pesquisa em IA.
- A empresa tem cerca de 250 funcionários, de mais de 40 nacionalidades.
- A Verda já levantou mais de US$450 milhões no total.
**Fontes:**
- [S47] Verda — https://verda.com/blog/verda-raises-189m
- [S48] The Next Web — https://thenextweb.com/news/finnish-ai-cloud-company-verda-raises-189m-and-it-is-now-the-latest-unicorn-in-europe
- [S49] Tech.eu — https://tech.eu/2026/09/22/verda-raises-189m-to-advance-its-ai-cloud-and-expand-compute-capacity/

## EUA, Dinamarca e Groenlândia — acordo de segurança no Ártico
- Trump assinou em 22 de setembro, na Assembleia Geral da ONU, um acordo com Dinamarca e Groenlândia voltado a reforçar a segurança no Ártico e no Atlântico Norte.
- O acordo alivia tensões geradas pelos pedidos repetidos de Trump para anexar a ilha.
- Em seu discurso na ONU, Trump disse que os EUA vão "iniciar imediatamente o processo de desenvolver uma grande presença militar nos locais apropriados".
- Trump incluiu nesse plano "a construção de duas bases militares muito importantes".
- A cerimônia trilateral ocorreu às 10h30 (horário do Leste dos EUA), com a primeira-ministra dinamarquesa Mette Frederiksen e o primeiro-ministro da Groenlândia, Jens-Frederik Nielsen.
- O texto do acordo seguia sem publicação até a assinatura.
- O chanceler dinamarquês Lars Løkke Rasmussen disse que o acordo coloca a segurança do Ártico sob a guarda coletiva da OTAN, em vez de deixá-la apenas a cargo de Washington e Copenhague.
- Trump havia publicado que o acordo dá aos EUA "controle permanente sobre a segurança, e todas as demais necessidades, na Groenlândia".
- Trump também afirmou que nenhum adversário americano poderia instalar forças no território sem aprovação por escrito de Washington.
- O secretário de Estado Marco Rubio chamou o texto de "acordo histórico" que "garante permanentemente os interesses de segurança dos EUA no Ártico a custo zero para o contribuinte americano".
- Frederiksen disse que o acordo "reconhece a soberania e a integridade territorial do Reino e o direito do povo groenlandês à autodeterminação".
- O acordo ainda precisa passar por procedimentos parlamentares para entrar em vigor.
**Fontes:**
- [S50] Associated Press — https://www.newser.com/article/084ac2a82952c2dff403c48bd3564113/trump-signs-us-denmark-greenland-agreement-to-bolster-arctic-security.html
- [S51] The Globe and Mail — https://www.theglobeandmail.com/world/article-trump-greenland-denmark-arctic-deal-us-military/
- [S52] CBC News — https://www.cbc.ca/news/world/denmark-greenland-us-security-deal-9.7353071
- [S53] ABC News — https://abcnews.com/Politics/trump-sign-agreement-leaders-greenland-denmark-united-nations/story?id=136636071
- [S54] Reuters — https://www.reuters.com/world/europe/trump-denmark-greenland-sign-deal-bid-end-arctic-standoff-2026-09-22/

## Irã — oferta para reabrir o Estreito de Ormuz
- Um alto funcionário iraniano disse à Reuters em 22 de setembro que o Irã pode reabrir o Estreito de Ormuz em até sete dias.
- A condição é que os EUA reduzam a pressão militar e suspendam o bloqueio aos portos iranianos.
- Teerã entregou sua proposta mais recente a Washington por meio de mediadores em 16 de setembro.
- O funcionário chamou a Assembleia Geral da ONU de "uma oportunidade de ouro para os EUA voltarem à diplomacia".
- O presidente iraniano Masoud Pezeshkian deixou Teerã rumo a Nova York na manhã de terça-feira.
- Não há planos de encontro entre Pezeshkian e Trump.
- Seria o primeiro evento com a presença dos dois desde que Trump lançou a "Operação Epic Fury" em fevereiro.
- O secretário de Estado Marco Rubio disse que os EUA estavam abertos a conversar com os iranianos na Assembleia Geral, "especialmente se houver perspectiva de levar a algo positivo".
- Trump tinha encontro marcado com os líderes dos seis países árabes do Golfo em 22 de setembro.
- Está na mesa uma proposta do Catar para uma arquitetura de segurança comum que inclua o Irã.
- Teerã está analisando a proposta catariana.
- A agência Kyodo informou que a iniciativa foi aprovada pelo líder supremo Mojtaba Khamenei e pelo Conselho Supremo de Segurança Nacional.
- O Irã busca o fim do bloqueio a seus portos e das operações militares americanas ligadas ao estreito.
- No domingo, o comando central militar do Irã disse ter sido informado de que os EUA preparavam a retomada de operações militares com apoio de países da região.
- O comando alertou que isso levaria a retaliação de Teerã "sem limitações e considerações".
**Fontes:**
- [S55] Reuters — https://www.reuters.com/world/middle-east/iran-ready-reopen-strait-hormuz-if-us-eases-military-pressure-lifts-blockade-2026-09-22/
- [S56] The Irish Times — https://www.irishtimes.com/world/middle-east/2026/09/22/iran-ready-to-reopen-strait-of-hormuz-if-us-eases-military-pressure-and-lifts-blockade/
- [S57] ThePrint / Reuters — https://theprint.in/world/iran-us-hint-at-revival-of-talks-as-trump-pezeshkian-due-to-attend-un/3050154/
- [S58] Iran International — https://www.iranintl.com/en/202609224536

## Petróleo — Brent abaixo de US$100 e ataques a navios em Ormuz
- O Brent caiu 3,4% em 21 de setembro, a US$100,34 o barril.
- O WTI caiu 4,5%, a US$95,78 o barril.
- Foram os menores fechamentos desde 8 de setembro e a quarta sessão consecutiva de queda.
- A Saudi Aramco carregou cerca de 14 milhões de barris de petróleo em sete supertanques dentro do Golfo no domingo.
- Ataques de drones forçaram a Arábia Saudita a fechar seu oleoduto Leste-Oeste em 13 de setembro.
- Dados de satélite do JPMorgan mostraram que o petróleo saudita que passa por Ormuz somou em média 2,9 milhões de barris por dia ao longo de seis dias.
- Em agosto, essa média era de cerca de 700 mil barris por dia.
- Outros dois navios-tanque foram atingidos ao cruzar Ormuz em 21 de setembro.
- Um deles, em rota de entrada, foi atingido por um projétil não identificado, ferindo levemente dois tripulantes.
- O outro, um navio de GLP em rota de saída, foi atingido por estilhaços de projétil.
- Pelo menos cinco ataques ou incidentes de segurança envolvendo navios-tanque foram registrados no estreito desde 16 de setembro.
- O Joint Maritime Information Center classifica o nível de ameaça no Estreito de Ormuz como SEVERO.
- Apenas 17 navios de carga de commodities foram vistos cruzando o estreito no fim de semana.
- Uma semana antes eram 37, e antes da guerra o tráfego era de cerca de 125 navios por dia.
- Cerca de 15% da frota mundial de navios VLCC (petroleiros de grande porte) está parada na costa de Omã para transferências de navio a navio.
- Os fretes de navios-tanque subiram fortemente com os navios presos em operações de transbordo e viagens mais longas.
- O petróleo acumula alta de mais de 65% em 2026.
- O diesel nos EUA atingiu novo recorde, acima de US$6,50 o galão.
- O Brent estava em torno de US$72 no fim de fevereiro, antes do início da guerra com o Irã.
**Fontes:**
- [S59] MarketWatch — https://www.marketwatch.com/story/oil-prices-fall-for-fourth-day-as-supply-concerns-ease-2nd-update-0be75bfa
- [S60] Al Arabiya / Reuters — https://english.alarabiya.net/News/saudi-arabia/2026/09/21/saudi-aramco-ramps-up-gulf-oil-exports-after-pipeline-attack-data-shows
- [S61] gCaptain — https://gcaptain.com/two-more-tankers-hit-in-strait-of-hormuz-as-attacks-mount/
- [S62] World Oil / Bloomberg — https://www.worldoil.com/news/2026/9/21/brent-falls-to-100-as-strait-of-hormuz-oil-flows-increase/
- [S63] France 24 — https://www.france24.com/en/middle-east/20260921-projectile-hits-tanker-as-it-enters-the-strait-of-hormuz

## Rússia — eleição para a Duma em meio a ataque recorde de drones
- O Rússia Unida, partido apoiado por Putin, caminhava para dominar a eleição parlamentar com 57,5% dos votos.
- O resultado parcial considerava mais de 71% das urnas apuradas.
- Foi a primeira eleição para a Duma estatal, de 450 assentos, desde a invasão em larga escala da Ucrânia, em fevereiro de 2022.
- O comparecimento ficou perto de 57%, com 111 milhões de eleitores aptos.
- A votação começou na sexta-feira e terminou no domingo.
- O partido liberal Yabloko, único partido registrado que se opõe à guerra, foi impedido de concorrer pela mais alta corte russa.
- A votação incluiu quatro regiões ucranianas anexadas ilegalmente, além da Crimeia.
- A Ucrânia lançou no último dia de votação o que Moscou classificou como o maior ataque de drones da guerra.
- O prefeito Sergei Sobyanin disse que mais de 1.600 drones foram abatidos, 450 deles se aproximando de Moscou.
- Os ataques mataram três pessoas na região de Moscou.
- Outras duas pessoas morreram na parte de Kherson controlada pela Rússia, incluindo uma autoridade eleitoral.
- Os ataques atingiram a refinaria de petróleo de Moscou.
- O ministério da Defesa russo disse que vai "continuar e intensificar" ataques de alta precisão contra alvos militares em Kiev.
- Drones russos atingiram Zaporizhzhia na segunda-feira, ferindo cinco pessoas.
- Moscou disse ter abatido 244 drones ucranianos na noite de domingo para segunda.
- A força aérea ucraniana disse ter abatido ou neutralizado 148 drones russos no mesmo período.
**Fontes:**
- [S64] CNBC — https://www.cnbc.com/2026/09/21/russia-election-putin-moscow-attack-ukraine.html
- [S65] The Independent — https://www.independent.co.uk/news/world/europe/ukraine-russia-war-live-putin-elections-drone-strikes-nato-b3053322.html
- [S66] The Jakarta Post / Reuters — https://www.thejakartapost.com/world/2026/09/21/russias-ruling-party-on-track-to-win-wartime-election-after-drones-strike-moscow
- [S67] ABC News Pakistan / Reuters — https://abcnews.com.pk/russian-election-enters-final-day-after-ukraine-targets-moscow-in-massive-drone-attack/
- [S68] The Guardian — https://www.theguardian.com/world/2026/sep/21/ukraine-war-briefing-russia-intensify-attacks-kyiv
- [S69] Associated Press — https://www.local10.com/news/world/2026/09/21/russia-targets-zaporizhzhia-after-ukraine-launches-1000-drone-weekend-barrage/

## Binance e Circle — participação de US$100 milhões e acordo de cinco anos
- Circle e Binance anunciaram em 22 de setembro um novo acordo comercial de cinco anos para ampliar o acesso ao USDC em mercados emergentes.
- Junto com o acordo, a Binance fez um investimento estratégico de US$100 milhões no capital da Circle.
- A colocação privada foi concluída em 17 de setembro.
- A Binance comprou 1,24 milhão de ações Classe A a US$80,84 cada, um desconto de 5% sobre o preço de mercado.
- As ações têm lockup de até dois anos, período em que a Binance não pode vender, transferir nem fazer hedge dos papéis.
- A Binance manteve os direitos de voto.
- Pelo acordo, a Circle vai pagar à Binance uma taxa mensal de incentivo calculada como percentual do USDC mantido pelo serviço Modular Smart Contract Wallet da Circle.
- O novo arranjo substitui acordos anteriores entre as duas empresas, de novembro de 2024 e agosto de 2025.
- O co-CEO da Binance, Richard Teng, disse que o investimento de US$100 milhões e o compromisso de cinco anos "representam convicção de longa duração".
- Teng afirmou que "um dólar digital estável e confiável não deveria ser um privilégio".
- O acordo sinaliza o esforço da Circle para expandir o USDC além de sua base historicamente concentrada nos EUA e competir de forma mais direta com a Tether nos mercados internacionais de cripto.
- A ação da Circle chegou a subir mais de 3% na terça-feira antes de recuar para uma queda fracionária.
- A notícia vem enquanto o Departamento de Justiça e a promotoria federal de Manhattan investigam a Binance por supostas violações das sanções ao Irã.
**Fontes:**
- [S70] Circle — https://www.circle.com/pressroom/binance-invests-100-million-in-circle-expands-strategic-partnership-and-renews-commercial-agreement-for-five-years
- [S71] CoinDesk — https://www.coindesk.com/policy/2026/09/22/binance-buys-usd100-million-circle-stake-in-five-year-usdc-promotion-deal
- [S72] CNBC — https://www.cnbc.com/2026/09/22/circle-lands-100-million-from-binance-to-ramp-up-global-usdc-expansion-.html
- [S73] Investor's Business Daily — https://www.investors.com/news/circle-stock-spikes-as-binance-takes-100-million-slice/

## Boehringer Ingelheim e Envisagenics — até US$1 bilhão em alvos de splicing de RNA
- A Boehringer Ingelheim anunciou em 22 de setembro uma parceria com a Envisagenics, sediada em Nova York.
- O acordo pode valer mais de US$1 bilhão.
- O valor inclui um pagamento inicial não divulgado, financiamento de pesquisa, taxas de opção e marcos de desenvolvimento, regulatórios e comerciais.
- A Envisagenics também tem direito a royalties sobre vendas de produtos.
- A plataforma da Envisagenics usa IA para rastrear alterações de splicing de RNA específicas de câncer.
- As empresas chamam essas alterações de "uma das últimas fontes em grande parte inexploradas" de alvos terapêuticos.
- A Boehringer vai atacar os eventos de splicing identificados com anticorpos multiespecíficos, conjugados anticorpo-fármaco e engajadores de células T.
- A Boehringer pode obter licenças exclusivas sobre alvos selecionados.
- A Boehringer assume a liderança e a responsabilidade total por seleção de modalidade, desenvolvimento e comercialização do produto resultante.
- A CEO da Envisagenics, Maria Pineda, disse que a Boehringer está "focada em tumores sólidos agressivos com necessidade significativa não atendida e opções de tratamento limitadas".
- Pineda afirmou que as parceiras vão trabalhar em estreita colaboração na validação de alvos.
- O acordo se soma a uma onda de apostas em splicing de RNA na indústria farmacêutica.
- A Merck KGaA colocou mais de US$2 bilhões em valor potencial de acordo na Skyhawk Therapeutics, para condições neurológicas.
**Fontes:**
- [S74] BioSpace — https://www.biospace.com/deals/boehringer-ingelheim-bets-up-to-1b-in-ai-centered-solid-tumor-collab-with-envisagenics

## Nigéria — corte de 350 pontos-base na taxa básica
- O Banco Central da Nigéria cortou sua taxa básica (Monetary Policy Rate) em 350 pontos-base em 22 de setembro, de 26,5% para 23%.
- Foi a segunda redução de juros de 2026.
- A decisão foi tomada ao fim da 307ª reunião do Comitê de Política Monetária, em Abuja.
- A taxa volta à faixa de 23% pela primeira vez desde fevereiro de 2024.
- O compulsório (Cash Reserve Requirement) foi mantido em 45% para bancos de depósito e 16% para bancos mercantis.
- O corredor de operações permanentes foi recalibrado para +50/-300 pontos-base em torno da taxa básica.
- A inflação cheia caiu para 15,39% em agosto, ante 15,43% em julho e 23,14% um ano antes.
- A inflação de alimentos recuou a 19,57% na comparação anual.
- O comitê apontou riscos externos, incluindo o avanço das tarifas globais e tensões geopolíticas no Oriente Médio.
- Esses fatores podem elevar a inflação importada e perturbar os mercados de commodities.
- Analistas da United Capital esperavam manutenção da taxa.
- Eles argumentavam que a forte alta dos preços do petróleo bruto e da gasolina tornava o corte prematuro, com o Brent perto de US$105 em meados de setembro.
- O corte contraria a direção da política monetária nos mercados desenvolvidos.
- O Federal Reserve elevou os juros em 25 pontos-base, para a faixa de 3,75%-4,0%, em 16 de setembro.
- O Banco Central Europeu subiu suas taxas em 25 pontos-base em 10 de setembro.
- O Banco do Japão elevou sua taxa básica para cerca de 1,25% em 18 de setembro.
**Fontes:**
- [S75] Independent Nigeria — https://independent.ng/cbn-slashes-mpr-by-350bps-to-23/
- [S76] Businessfront — https://businessfront.com/finance/news/nigerias-apex-bank-cuts-interest-rate/
- [S77] The Journal Nigeria — https://thejournalnigeria.com/united-capital-sees-cbn-holding-rate-as-oil-petrol-prices-rise/
- [S78] The Nation — https://www.nation.com.pk/22-Sep-2026/major-central-banks-tighten-policy-energy-prices-fuel-inflation
