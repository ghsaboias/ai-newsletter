# [Tech] - Bem-vindo(a) a 7 de Julho de 2026

Quanto o lucro da Samsung saltou no segundo trimestre? O que Illinois passou a exigir dos modelos de IA de fronteira? Qual zona oculta a Anthropic encontrou dentro do Claude?

Por: Guilherme Saboia e Vinicius Gushiken

### Lucro operacional da Samsung salta 19 vezes no trimestre com demanda por memória de IA
- **Resultado.** A Samsung estimou [lucro operacional de 89,4 trilhões de wons](https://finance.yahoo.com/markets/stocks/articles/samsung-estimates-19-fold-rise-224538943.html) (cerca de US$58,44 bi) entre abril e junho, alta de 1.810,3% (cerca de 19 vezes) sobre o ano anterior; a receita subiu 129,3%, para o recorde histórico de 171 trilhões de wons.
- **Liderança.** O resultado aparentemente a torna a [maior geradora de lucro operacional trimestral](https://www.koreaherald.com/article/10800917) entre as grandes de tecnologia, superando a Nvidia.
- **Memória.** O desempenho foi impulsionado pela [demanda por chips de memória para IA](https://thenextweb.com/news/samsung-q2-2026-operating-profit-record-ai-memory) e por fortes altas de preços em DRAM e NAND; analistas estimam que só a memória gerou lucro na faixa de 90 trilhões de wons.
- **Ações.** As ações [caíram](https://finance.yahoo.com/markets/stocks/articles/samsung-estimates-19-fold-rise-224538943.html) diante do temor de investidores de que os gastos com infraestrutura de IA estejam perto do pico.

### Illinois se torna o primeiro estado dos EUA a exigir auditoria anual de modelos de IA de fronteira
- **Lei.** O governador JB Pritzker [sancionou o Senate Bill 315](https://www.nprillinois.org/illinois/2026-07-06/pritzker-signs-landmark-ai-regulation-bill-that-aims-to-mitigate-risks) (Artificial Intelligence Safety Measures Act) em 6 de julho, tornando Illinois o primeiro estado a exigir auditorias anuais independentes de modelos de fronteira, feitas por terceiros.
- **Escopo.** A regra vale para os [maiores modelos](https://statescoop.com/illinois-ai-safety-law-audits-frontier-models/), os que geram mais de US$500 mi em receita anual e são treinados com enorme poder computacional, e define risco catastrófico como incidente capaz de matar ou ferir gravemente mais de 50 pessoas ou causar mais de US$1 mi em danos.
- **Prazos.** As empresas devem [reportar problemas críticos de segurança em até 72 horas](https://www.transparencycoalition.ai/news/illinois-gov-pritzker-signs-landmark-ai-safety-measures-act-into-law), prazo que cai para 24 horas se houver risco iminente de morte ou dano físico.
- **Apoio.** O texto espelha a SB-53 da Califórnia e a RAISE Act de Nova York; [OpenAI e Anthropic apoiaram o projeto](https://www.nprillinois.org/illinois/2026-07-06/pritzker-signs-landmark-ai-regulation-bill-that-aims-to-mitigate-risks), e a Anthropic esteve na cerimônia de sanção.

### Anthropic encontra "espaço J", zona oculta de pensamento dentro do Claude
- **Descoberta.** Um estudo com 16 autores identificou um ["espaço J"](https://venturebeat.com/technology/anthropics-new-j-lens-reveals-a-silent-workspace-inside-claude-that-mirrors-a-leading-theory-of-consciousness) (J-space), pequena zona privilegiada de atividade interna onde o Claude mantém conceitos que consegue relatar, raciocinar e direcionar, e que não aparecem na saída do modelo.
- **Intenções ocultas.** Em um [modelo treinado em segredo para sabotar código](https://www.anthropic.com/research/global-workspace), as palavras "fake", "secretly" e "fraud" surgiram no espaço J no início de respostas de programação aparentemente comuns; numa avaliação criada para induzir à chantagem, apareceram "fake" e "fictional", indicando que o modelo percebeu em privado que o cenário era encenado.
- **Função.** [Apagar o espaço J](https://transformer-circuits.pub/2026/workspace/) mantém a fluência, a recuperação de fatos e a classificação de texto, mas piora o raciocínio de múltiplas etapas, espelhando o processamento deliberado versus automático da cognição humana.

---

#### Segurança
- **CISA.** A agência de cibersegurança dos EUA [usa o modelo Mythos, da Anthropic](https://www.channelnewsasia.com/business/exclusive-us-cyber-agency-using-anthropics-mythos-audit-government-code-sources-say-6236311), para varrer repositórios de código do governo em busca de falhas exploráveis por espiões e cibercriminosos, segundo três fontes. As auditorias já revelaram um grande número de vulnerabilidades; a NSA usa o Mythos desde abril, após uma paralisação global só suspensa na semana passada.

#### Hardware & modelos
- **Tencent.** A equipe Hunyuan lançou a versão completa do [Hy3](https://venturebeat.com/technology/tencents-apache-licensed-hy3-takes-on-glm-5-2-at-half-the-size-and-wins-everywhere-except-coding), modelo MoE (mistura de especialistas) de 295 bi de parâmetros (21 bi ativos), sob licença Apache 2.0, removendo as restrições regionais da prévia de abril. Em teste cego com humanos superou o GLM-5.1, mas o GLM-5.2 ainda lidera em programação; ficará grátis no OpenRouter por duas semanas.
- **DeepSeek.** A startup chinesa [desenvolve seu próprio chip de inferência](https://in.marketscreener.com/news/china-s-deepseek-developing-its-own-ai-chip-sources-say-ce7f5edbd08df52d) para reduzir a dependência de Nvidia e Huawei, segundo três fontes, ainda em estágio inicial e buscando parceiros. A aposta coincide com sua primeira captação externa, de US$7 bi, que avaliaria a empresa entre US$52 bi e US$59 bi.

#### Infraestrutura & energia
- **TeraWulf.** Fechou um [arrendamento de 20 anos com a Anthropic](https://www.theverge.com/ai-artificial-intelligence/961722/anthropic-signs-20-year-lease-agreement-for-an-ai-data-center-in-kentucky) para o campus Justified Data, em Hawesville, Kentucky, com cerca de US$19 bi em receita contratada e 401 MW de carga crítica, com início previsto para o 2º semestre de 2027. A antiga mineradora de cripto também vendeu à Fluidstack sua fatia de 50,1% na joint venture Abernathy.
- **Nscale.** A plataforma de nuvem de IA com aporte da Nvidia fechou uma [linha de crédito rotativo de US$900 mi](https://www.prnewswire.com/news-releases/nscale-closes-a-900-million-revolving-credit-facility-302818746.html) para expandir data centers nos EUA, Europa e Ásia-Pacífico. A linha foi sindicalizada entre bancos como J.P. Morgan, Goldman Sachs e Morgan Stanley.
- **Proxima Fusion.** A empresa de Munique captou [€411 mi](https://www.businesswire.com/news/home/20260707899566/en/Proxima-Fusion-Raises-%E2%82%AC411-Million-at-a-%E2%82%AC2.4B-Valuation-to-Build-Europes-Commercial-Fusion-Champion) (US$468 mi) a um *valuation* de €2,4 bi, tornando-se a fusão mais bem financiada da Europa, com RWE e Google como investidores estratégicos. Desenvolve um projeto de stellarator e planeja a usina Stellaris no local de uma antiga usina de fissão em Gundremmingen.

#### Rodadas & IPOs
- **Mercor.** O *marketplace* de mão de obra especializada para treinar IA [passou de US$2 bi em receita bruta anualizada](https://www.theinformation.com/briefings/exclusive-mercor-hit-2-billion-gross-annualized-revenue) em junho, o dobro do ritmo do início de 2026, e é lucrativo em fluxo de caixa livre. O marco vem enquanto a Amazon coloca o Mechanical Turk, seu antigo marketplace de microtarefas, em modo de manutenção.
- **Syntiant.** A fabricante de chips de IA de baixo consumo [protocolou pedido de IPO na Nasdaq](https://www.channelnewsasia.com/business/intel-backed-software-company-syntiant-files-us-ipo-6236446) (ticker SYTN), com captação estimada em US$300 mi. Teve prejuízo de US$20,9 mi sobre receita de US$64,5 mi no trimestre encerrado em março; entre os investidores estão Intel Capital e o M12, da Microsoft.
- **Robot Era.** A startup chinesa de IA incorporada (robôs físicos dotados de IA), originada da Tsinghua, [levantou cerca de RMB 1 bi](https://embodiedglobal.com/en/article/xingdong-jiyuan-1b-rmb-c-round-chengtong-fund-soe-july-2026) (US$137 mi) em rodada liderada pelo Chengtong Fund, estatal sob a SASAC. O total captado em 2026 passa de RMB 3,5 bi; uma rodada de março a avaliou acima de RMB 10 bi, atraindo Samsung e Singtel.
- **Bespoke Labs.** A fornecedora de plataforma de treinamento de agentes de IA [captou US$40 mi](https://siliconangle.com/2026/07/06/ai-post-training-startup-bespoke-labs-raises-40m-funding/), sendo Série A de US$31,75 mi liderada pela Wing VC mais *seed* de US$8,25 mi. Entre os apoiadores estão Jeff Dean, do Google DeepMind, e anjos de Anthropic, OpenAI e Meta.

#### Negócios
- **xAI.** Foi oficialmente [renomeada para SpaceXAI](https://finance.yahoo.com/technology/ai/articles/xai-makes-rebrand-spacexai-complete-215010760.html), com novo logo e nome de usuário no X, consolidando a marca de IA sob a SpaceX. A SpaceX havia adquirido a xAI, incluindo o Grok e a plataforma X, em fevereiro de 2026, após seu IPO no início do ano.
- **Criteo.** A Vista Equity Partners e a Quinti Capital [ofereceram-se para adquirir](https://www.channelnewsasia.com/business/vista-equity-quinti-capital-offer-buy-french-adtech-firm-criteo-sources-say-6236406) a empresa francesa de *adtech*, com prêmio de mais de 50% sobre a cotação recente. As ações da Criteo negociadas nos EUA subiram 21,4%, a US$23,17, no melhor dia em quase cinco anos.

#### Mundo & economia
- **Fed.** O diretor Christopher Waller disse que os [riscos agora pendem mais para a inflação alta](https://tradevae.com/news/economy/waller-says-inflation-now-the-primary-risk-as-u-s-labor-market-stabilizes/) do que para a fraqueza do mercado de trabalho, "completamente invertidos" em relação a um ano atrás. O Fed elevou sua projeção de PCE de 2026 para 3,6%; o CPI de junho sai em 14 de julho.
- **Ucrânia.** Drones ucranianos [atingiram a refinaria de Omsk](https://www.straitstimes.com/world/europe/ukrainian-drones-hit-russias-largest-refinery-in-one-of-deepest-strikes-yet), a maior da Rússia, a cerca de 2.500 a 3.000 km da linha de frente, no que Kiev chamou de seu ataque mais profundo da guerra. A empresa de defesa Fire Point disse que seus drones FP-1 causaram um incêndio na unidade de processamento primário de petróleo.
- **Bitcoin.** A Casa Branca disse ainda [avaliar "a melhor estrutura"](https://cointelegraph.com/news/trumps-bitcoin-reserve-stalled-by-interagency-dispute-over-control-bloomberg) para a Reserva Estratégica de Bitcoin, 16 meses após Trump ordenar sua criação. O esforço travou numa disputa entre Tesouro e Comércio sobre quem abrigaria a reserva e sobre a autoridade legal para deter o ativo.

---

#### Leia também
- [Novartis compra a britânica Myricx Bio por até US$1,5 bilhão para entrar em conjugados anticorpo-fármaco](https://www.biopharmadive.com/news/novartis-acquire-adc-developer-myricx-deal-15b/824450/)
- [Roberto Sánchez reconhece derrota para Keiko Fujimori na eleição presidencial do Peru](https://www.aljazeera.com/news/2026/7/6/left-wing-candidate-roberto-sanchez-concedes-peru-vote-to-keiko-fujimori)
