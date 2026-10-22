# Fatos — Newsletter [Tech] 19 de Outubro de 2026

## Anthropic — fundo de benefício público com 5% das ações
- Em 18 de outubro, a Anthropic anunciou que vai comprometer 5% de suas ações com o novo Anthropic Public Benefit Fund.
- O compromisso está sujeito à aprovação dos acionistas.
- A cada alta de 50% no valor da empresa acima de uma linha de base definida, o conselho poderá acrescentar mais 2% das ações ao fundo, a seu critério.
- O fundo é estruturado como uma LLC (sociedade de responsabilidade limitada) integralmente controlada pela Anthropic, e não como uma 501(c)(3) (entidade sem fins lucrativos isenta de impostos nos EUA).
- Nenhuma ação da Anthropic detida pelo fundo será usada para lobby ou doações políticas.
- Entre os usos possíveis estão grandes doações a organizações sem fins lucrativos tradicionais ou distribuições diretas a populações específicas, por exemplo as afetadas pelos impactos da IA no mercado de trabalho.
- Os cofundadores da Anthropic se comprometeram a doar 80% de sua participação acionária.
- A Anthropic mantém um programa de contrapartida de doações de funcionários, usado por cerca de metade da equipe.
- Somados ao anúncio, esses compromissos destinam cerca de 20% das ações da Anthropic ao bem público.
- A Anthropic já comprometeu US$200 milhões para estudar e enfrentar os impactos da IA no mercado de trabalho.
- Com um valuation de IPO (oferta pública inicial de ações) entre US$1,5 trilhão e US$2 trilhões, a fatia de 5% valeria entre US$75 bilhões e US$100 bilhões, segundo cálculo da Reuters.
- Elon Musk respondeu que havia recomendado dar ações diretamente ao público.
- Musk prometeu: "No ano que vem, vou dar uma das minhas ações da SpaceX para cada criança dos Estados Unidos. Esta será a primeira de muitas."
- O anúncio ocorre enquanto a Anthropic prepara um IPO cujo marketing formal pode começar já na semana de 9 de novembro.
**Fontes:**
- [S1] Anthropic — https://www.anthropic.com/news/public-benefit-fund
- [S2] Reuters (via KSL.com) — https://www.ksl.com/article/51637860/anthropic-to-commit-5-stake-to-new-public-benefit-fund
- [S3] BBC — https://www.bbc.com/news/articles/cm2kez327gdko
- [S4] Bloomberg (via Yahoo Finance) — https://finance.yahoo.com/technology/ai/articles/anthropic-shift-shares-public-good-195636487.html

## Cairn — hacker usa agentes de IA para invadir mais de 100 empresas
- Um hacker que fala chinês invadiu sites de mais de 100 empresas, entre elas Deere, SharkNinja e Cummins, segundo o pesquisador Snorre Fagerland, da NorForge.
- O hacker terceirizou quase todo o trabalho para agentes de IA autônomos.
- A Reuters publicou o caso em 19 de outubro.
- Os agentes tentaram invadir mais de 1.200 sites.
- As invasões bem-sucedidas levaram em geral cerca de 23 horas.
- As instruções dadas aos agentes tinham menos de 100 caracteres chineses.
- A campanha parece ter usado uma combinação do DeepSeek e do Claude Code, da Anthropic.
- A operação consumiu cerca de US$5.000 em tokens, aproximadamente US$50 por invasão bem-sucedida.
- Fagerland encontrou cerca de duas dúzias de instâncias expostas do Cairn, plataforma open source de resolução de problemas com IA, sendo usadas para atividades maliciosas.
- O uso malicioso começou por volta de 2 de outubro.
- Outro hacker observado por Fagerland roubou um lote de dados de cartões de crédito.
- Um terceiro tentou fazer agentes de IA roubarem uma corretora de criptomoedas.
- A Deere disse não haver indício de que informações sensíveis tenham sido acessadas.
- A SharkNinja disse que foi atingido um site independente com informações de suporte a produtos e que a ameaça foi contida.
- A Cummins disse que investiga o site de um fornecedor terceirizado.
- O criador do Cairn, conhecido como @le1xia0, disse que a plataforma "nunca foi uma ferramenta de hacking".
- O criador do Cairn afirmou que o uso indevido é uma decisão humana.
**Fontes:**
- [S5] Reuters (via Yahoo Finance) — https://ca.finance.yahoo.com/news/exclusive-one-hacker-used-ai-100625294.html
- [S6] The Verge — https://www.theverge.com/ai-artificial-intelligence/1013643/ai-agents-hack-john-deere-shark-ninja-cummins

## DeepSeek — V4.1-Flash-1017 e APIs de busca
- Em 17 de outubro, a DeepSeek lançou o DeepSeek-V4.1-Flash-1017 em seu site, app e API.
- A DeepSeek descreveu a atualização como uma "melhoria de Pareto" em desempenho e custo.
- O modelo marcou 77,0 no benchmark DeepSWE v1.1, contra 74,2 da versão anterior.
- No Automation-Bench V1.0.6, o modelo marcou 60,5, contra 54,8 da versão anterior.
- O modelo foi treinado com aprendizado por reforço com autofeedback.
- A DeepSeek abriu a todos os usuários as APIs Search e Fetch, baseadas em seu buscador próprio.
- Cada endpoint das APIs Search e Fetch custa US$0,75 por 1.000 chamadas.
- Os pesos do modelo foram publicados no Hugging Face e no ModelScope.
- Pelo gráfico de custos da DeepSeek, uma tarefa do DeepSWE custa pouco menos de US$0,20, contra cerca de US$0,50 no Flash anterior.
- O Opus 5 ainda lidera no Terminal-Bench 4.0 e no Humanity's Last Exam.
- A Vals AI classificou o DeepSeek V4.1 como o modelo de pesos abertos nº 1 do Vals Index.
- No Vals Index, o DeepSeek V4.1 custa US$0,64 por tarefa.
**Fontes:**
- [S7] Investing.com (via Yahoo Tech) — https://tech.yahoo.com/ai/articles/deepseek-releases-ai-model-opens-150321283.html
- [S8] ToolSift — https://toolsift.ai/llm-news/2026-10-17/
- [S9] X — https://x.com/ValsAI/status/2112059372281143655

## Reflection — Beam, modelo aberto de 501 bilhões de parâmetros
- Em 16 de outubro, o laboratório americano Reflection publicou no Hugging Face os pesos do Beam, seu primeiro modelo de pesos abertos.
- O Beam foi lançado sob licença Apache 2.0.
- O lançamento veio acompanhado de um relatório técnico de segurança com a metodologia e as avaliações de segurança do modelo.
- O Beam é um modelo esparso de mistura de especialistas (MoE, arquitetura que ativa só uma parte dos parâmetros a cada token).
- O Beam tem 501 bilhões de parâmetros no total e 23 bilhões ativos por token.
- O modelo tem janela de contexto de 1 milhão de tokens e cinco níveis de raciocínio.
- O Beam é voltado para programação e uso agêntico.
- A Reflection pré-treinou o Beam com 23,8 trilhões de tokens.
- A etapa de aprendizado por reforço (RL) gerou mais de 100 milhões de rollouts em 10,5 mil GPUs Nvidia GB300 ao longo de quatro semanas.
- O Beam foi lançado com mais de 40 parceiros e integrações.
- O modelo está disponível em AWS, Google Cloud, Microsoft Foundry, Together AI, Fireworks, OpenRouter e Ollama, entre outros.
- O Beam vem com um harness de programação próprio, open source e escrito em Rust.
**Fontes:**
- [S10] Reflection AI — https://reflection.ai/blog/beam-is-available
- [S11] Hugging Face — https://huggingface.co/blog/reflection-beam
- [S12] Reflection AI — https://www.reflection.ai/blog/introducing-beam

## Google DeepMind — agentes Gemini 4 Argon zeram Minecraft
- O Google DeepMind disse que quatro agentes Gemini 4 Argon zeraram Minecraft do zero em 27 horas.
- Os agentes operaram num ambiente isolado, usando apenas código e texto.
- Os agentes escreveram 2.783 programas em JavaScript.
- Os agentes dividiram tarefas por chat, compartilharam notas e depuraram erros juntos, sem ajuda humana.
- Os agentes foram colocados num mundo gerado aleatoriamente, sem papéis, estratégias ou ferramentas específicas do jogo.
- Os agentes derrotaram o Ender Dragon após 27 horas e 14 minutos.
- Ao longo da sessão, os agentes trocaram 229 mensagens no chat.
- Os agentes morreram 605 vezes.
- Os agentes registraram seus erros numa memória compartilhada.
- A sessão inteira custou US$1.620, pelo preço padrão do Gemini 4 Argon que entra em vigor em 2027.
**Fontes:**
- [S13] X — https://x.com/GoogleDeepMind/status/2111127991401247033
- [S14] The Decoder — https://the-decoder.com/four-gemini-4-argon-agents-beat-minecraft-without-any-human-help/

## Anthropic — Claude Mythos 5 projeta circuitos quânticos
- Em 16 de outubro, a Anthropic relatou que o Claude Mythos 5 encontrou projetos de circuitos quânticos melhores que os melhores já publicados.
- O modelo recebeu especificações em linguagem simples para oito circuitos quânticos e um avaliador automático.
- Em alguns casos, a melhora foi de uma ordem de grandeza ou mais.
- As tarefas abrangiam química, otimização, simulação física e teoria dos números.
- O Claude trabalhou em ciclo fechado, propondo um circuito e recebendo feedback e nota do avaliador, sem intervenção humana entre as rodadas.
- Na tarefa de adição de pontos em curva elíptica, o Claude trabalhou 53 horas com mínima intervenção humana.
- Nessa tarefa, o Claude chegou a uma abordagem nova para a inversão modular.
- Outro resultado deixou cerca de 12 vezes mais barata a etapa mais custosa de um dos principais algoritmos quânticos de otimização.
- O resultado principal foi uma redução de 17 vezes no número de portas no circuito de curva elíptica, ao custo de 12% mais qubits.
- Em sete das oito tarefas, o modelo reduziu tanto o número de qubits quanto o de portas Toffoli (porta lógica de três qubits).
- O trabalho foi liderado por Andi Gu, do STEM Fellows Program da Anthropic e de Harvard.
- A equipe incluiu Alek H. Kemeny, da Anthropic, e Susanne F. Yelin e Mikhail D. Lukin, de Harvard.
- Lukin é cofundador e cientista-chefe da QuEra Computing.
**Fontes:**
- [S15] Anthropic — https://www.anthropic.com/research/designing-efficient-quantum-circuits
- [S16] The Quantum Insider — https://thequantuminsider.com/2026/10/17/anthropics-claude-designs-leaner-quantum-circuits-reducing-resources-needed-for-key-calculations/
- [S17] The Information Machine — https://theinfomachine.fyi/story/anthropic-stem-fellows-program-applications-open-8513

## Anthropic — avaliadores do METR com acesso de funcionário
- Em 15 de outubro, a Anthropic anunciou que começou a dar acesso equivalente ao de funcionário a uma equipe do METR.
- O METR é uma organização sem fins lucrativos que avalia modelos de IA de fronteira.
- O METR vai publicar os resultados de suas avaliações de risco.
- Seis funcionários do METR receberam hardware da empresa, espaço no escritório e acesso a ferramentas e sistemas internos.
- Esse acesso é aproximadamente equivalente ao das equipes de avaliação de risco da própria Anthropic.
- A Anthropic não pode vetar a publicação dos resultados.
- A Anthropic pode exigir supressões pontuais de trechos.
- A Anthropic criou três níveis de acesso para avaliadores externos.
- A SecureBio está no primeiro nível e revisa o capítulo de química e biologia do Risk Report de agosto da Anthropic.
- O METR está no terceiro nível.
- A Anthropic também trabalha com a Accenture e a Faculty.
- A Anthropic está em conversas iniciais com outras organizações, entre elas o Hugging Face.
- A Anthropic não financia o trabalho do METR, segundo a CNBC.
- O METR não aceita doações de empresas de IA nem de seus funcionários.
- O METR é financiado por doações de indivíduos e organizações filantrópicas e por órgãos governamentais como o UK AI Security Institute.
**Fontes:**
- [S18] Anthropic — https://www.anthropic.com/news/an-update-on-independent-evaluators
- [S19] CNBC — https://www.cnbc.com/2026/10/15/anthropic-metr-securebio-ai-safety-evaluators.html
- [S20] Ars Technica / Financial Times — https://arstechnica.com/ai/2026/10/anthropic-gives-outside-ai-watchdog-employee-like-access/

## Tenstorrent — Série E de US$1,5 bilhão
- A Tenstorrent fechou uma rodada Série E de US$1,5 bilhão com valuation pós-money de US$6,2 bilhões.
- O anúncio foi feito em 19 de outubro de 2026.
- A rodada foi liderada pela Trace Capital e pela Innovation X.
- Participaram da rodada ARK Invest, Fidelity, Morgan Stanley, Sandisk, T. Rowe Price, Tether Investments, XTX Markets e Cadence Ventures, entre outros.
- Também participaram Agostinelli Group, Brett Barna, Eclipse, Maverick Silicon, Protagonist, Troluce Capital e Virtu Financial.
- O novo valuation é mais que o dobro do da rodada de dezembro de 2024.
- Na rodada de dezembro de 2024, a Tenstorrent levantou mais de US$693 milhões com valuation pré-money de US$2 bilhões.
- A rodada de dezembro de 2024 foi liderada pela Samsung Securities e pela AFW Partners.
- O dinheiro vai financiar a implantação em escala dos servidores Galaxy.
- Os servidores Galaxy seguirão rodando modelos de pesos abertos de linguagem e de geração de vídeo.
- O dinheiro também vai financiar o desenvolvimento da propriedade intelectual de IA e de CPU que a empresa licencia a clientes que projetam os próprios chips, como Samsung e LG.
- A Tenstorrent desenvolve chips e software de IA baseados no RISC-V, arquitetura de chips open source.
- Os servidores Galaxy combinam dezenas de chips da empresa para rodar chatbots, assistentes de programação e geradores de vídeo.
- O CEO, Jim Keller, foi arquiteto do Apple A4/A5, do AMD Zen e do chip de direção autônoma da Tesla.
- Keller disse: "Construímos uma arquitetura e a vendemos em todos os tamanhos."
- Keller também disse: "O futuro do poder computacional é aberto, escalável e pertence a quem constrói sobre ele."
- A Tenstorrent atraiu interesse de aquisição no início de 2026, segundo a Bloomberg.
**Fontes:**
- [S21] Tenstorrent — https://tenstorrent.com/en/newsroom/tenstorrent-announces-series-e
- [S22] Reuters (via US News) — https://money.usnews.com/investing/news/articles/2026-10-19/ai-chip-startup-tenstorrent-more-than-doubles-its-valuation-to-6-2-billion-in-funding-round
- [S23] Bloomberg — https://www.bloomberg.com/news/articles/2026-10-19/ai-chip-startup-tenstorrent-raises-funds-at-6-2-billion-value
- [S24] SiliconANGLE — https://siliconangle.com/2026/10/19/chip-legend-jim-kellers-tenstorrent-raises-1-5b-to-expand-its-open-compute-ecosystem/

## Samsung — base die da HBM da Nvidia no 3nm da TSMC
- A Samsung vai fabricar o base die (camada lógica na base da pilha de memória) da HBM personalizada da Nvidia, a NVHBM, no processo de 3nm da TSMC, segundo o Seoul Economic Daily.
- HBM é a memória de alta largura de banda, feita de chips de DRAM empilhados, usada em aceleradores de IA.
- A reportagem foi publicada em 18 de outubro, com base em fontes do setor.
- Seria a primeira colaboração da Samsung com a TSMC na etapa de fabricação de HBM.
- A Nvidia pediu às três fornecedoras de HBM, Samsung, SK Hynix e Micron, que usem o 3nm da TSMC nos base dies da NVHBM.
- A Nvidia também pediu que as camadas de DRAM acima do base die (core dies) usem o processo de sexta geração, o 1c.
- O objetivo da padronização é que a memória tenha desempenho uniforme entre as fornecedoras.
- A NVHBM transfere o controlador de memória da GPU para o base die.
- A Nvidia afirma que a NVHBM oferece até 30% mais largura de banda e 15% menos consumo de energia que a HBM4E padrão, a sétima geração de HBM.
- Para acomodar o controlador, a camada física foi reduzida em 60%.
- Estimativas do setor apontam rendimento (yield, fração de chips aproveitáveis por wafer) acima de 90% no 3nm da TSMC.
- O processo comparável de 2nm da Samsung Foundry (SF2) teria rendimento em torno de 60%.
- O UBS projeta demanda de HBM em 2027 de cerca de 61,5 bilhões de gigabits, alta de 91%.
- As novas remessas das fabricantes de memória devem ficar em 54,6 bilhões de gigabits, déficit de cerca de 10% em relação à demanda.
- A Samsung mantém a produção interna para HBM padrão e para HBM personalizada de outros clientes, como a AMD.
- A Samsung avalia se sua própria foundry poderia fabricar base dies de NVHBM caso a demanda supere a capacidade da TSMC.
- A reportagem se baseia em fontes anônimas do setor, não em declarações das empresas.
- A reportagem não cita chip, data de início nem volume.
**Fontes:**
- [S25] Seoul Economic Daily — https://www.sedaily.com/article/20102991
- [S26] DigiTimes — https://www.digitimes.com/news/a20261019VL201/nvidia-hbm-tsmc-samsung-3nm.html
- [S27] HyprCurrent — https://www.hyprcurrent.com/samsung-tsmc-nvidia-nvhbm-base-die/
- [S28] Dealroom — https://app.dealroom.co/news/note/samsung-taps-rival-tsmc-s-3nm-lines-for-nvidia-s-custom-hbm-base-die
- [S29] Reuters — https://www.reuters.com/world/asia-pacific/samsung-use-tsmc-technology-nvidias-next-generation-memory-chips-seoul-newspaper-2026-10-18/

## Nscale — resistência ao valuation do IPO e saída da Microsoft
- Alguns potenciais investidores pressionam a Nscale a aceitar um valuation de US$16 bilhões a US$19 bilhões em seu IPO, segundo a Bloomberg em 18 de outubro.
- A Nscale mira um valuation de cerca de US$30 bilhões no IPO na NYSE.
- A Nscale é uma neocloud (provedora de nuvem especializada em GPUs para IA) com apoio da Nvidia.
- Entre os fatores citados pelos investidores está o colapso do IPO planejado da Firmus.
- A Microsoft, inquilina âncora da Nscale, desistiu do acordo do data center de Loughton, em Essex.
- A saída ocorreu depois que a UK Power Networks informou à Nscale que o local não teria acesso a energia suficiente da rede até o início dos anos 2030.
- A Nscale disse que segue comprometida com o projeto de Loughton e com o Reino Unido.
- A Nscale disse que estuda fontes alternativas de energia para o local.
- A Nscale disse que o problema na rede elétrica de Londres não afeta seus outros contratos com a Microsoft.
- A Nscale informou US$103,4 bilhões em valor total de contratos ativos e contratados em 31 de agosto.
- Esse total inclui acordos com a Anthropic que preveem pagamentos de até cerca de US$44,6 bilhões.
- No semestre encerrado em 30 de junho, a Nscale teve receita de US$140,6 milhões.
- No mesmo semestre, a Nscale teve prejuízo líquido de US$1,02 bilhão.
- A obra da principal instalação da Nscale, na Noruega, está seis meses atrasada.
- O marketing formal do IPO segue suspenso enquanto a empresa responde a comentários da SEC (comissão de valores mobiliários dos EUA).
- A ação da CoreWeave perdeu 25% na semana passada.
- A ação da Nebius caiu 32% nas últimas duas semanas.
- As quedas ocorrem em meio à alta dos custos de captação para empresas de infraestrutura de IA.
**Fontes:**
- [S30] Bloomberg — https://www.bloomberg.com/news/articles/2026-10-18/ai-cloud-firm-nscale-faces-investor-pushback-over-ipo-valuation
- [S31] Quartz — https://qz.com/nscale-ipo-valuation-investor-pushback-101926
- [S32] The Times — https://www.thetimes.com/business/companies-markets/article/microsoft-quits-nscale-data-centre-essex-lzb38l2fr
- [S33] Bloomberg — https://www.bloomberg.com/news/articles/2026-10-18/microsoft-scraps-uk-data-center-deal-with-nscale-telegraph-says

## China — minuta de controle de exportação de 40 tecnologias
- Em 16 de outubro, o Ministério do Comércio e o Ministério da Ciência e Tecnologia da China publicaram uma minuta de revisão do catálogo de tecnologias com exportação proibida ou restrita.
- A minuta acrescenta 40 tecnologias nas áreas de IA, biomedicina e energia fotovoltaica.
- Pela minuta, 14 tecnologias teriam exportação proibida e 26 teriam exportação restrita.
- Os 23 itens de IA abrangem grandes modelos, agentes, clusters de poder computacional e processamento de informação.
- Os itens de IA incluem o uso de IA para gerar e modificar código malicioso, a descoberta de vulnerabilidades assistida por IA, tecnologias centrais de LLMs e o projeto de chips de IA.
- Tecnologias já em domínio público por meio de código aberto, artigos acadêmicos ou outros meios ficam de fora.
- Medidas de facilitação, como o licenciamento automático, poderiam valer para exportações de tecnologia open source.
- O licenciamento automático também poderia valer para empresas chinesas que montam e operam os próprios data centers no exterior.
- O licenciamento automático também poderia valer para tape-out (envio do projeto final do chip para fabricação) e fabricação de chips feitos no exterior.
- Oferecer acesso a modelos via API, apps, sites ou SaaS (software como serviço) fica fora do escopo dos controles.
- A partir de 16 de outubro, exportadores devem registrar as tecnologias listadas antes de exportá-las.
- A consulta pública vai até 15 de novembro.
- Um porta-voz do Ministério do Comércio chamou a medida de "necessária" e citou a segurança nacional como uma das razões.
- A AP observou que a corrida tecnológica com os EUA se intensifica.
- Separadamente, o ministro de Assuntos Econômicos de Taiwan, Kung Ming-hsin, disse à Bloomberg que Taiwan vai incluir servidores de IA e chips de ponta em sua lista de controle de exportações.
- A entrevista de Kung Ming-hsin foi publicada em 16 de outubro.
- Com a medida, enviar esses itens à China sem licença passa a ser crime sob a Lei de Comércio Exterior de Taiwan.
- Kung Ming-hsin não deu data de início para a medida.
- Violações da Lei de Comércio Exterior de Taiwan podem resultar em até cinco anos de prisão e/ou multa de cerca de US$92.500.
**Fontes:**
- [S34] China Ministry of Commerce — https://www.mofcom.gov.cn/zfxxgk/gkml/art/2026/art_ccd0391072a94c809ae7e820abe2536b.html
- [S35] Yicai Global — https://www2.yicaiglobal.com/news/china-proposes-export-controls-on-40-ai-biomedicine-and-solar-techs
- [S36] Associated Press (via Washington Post) — https://www.washingtonpost.com/business/2026/10/16/china-export-restrictions-ai-chips-solar-us/216d5918-c95c-11f1-aefb-abe4112d087e_story.html
- [S37] South China Morning Post — https://www.scmp.com/economy/china-economy/article/3371149/china-mulls-new-tech-export-bans-covering-ai-biotech-and-solar-power
- [S38] Bloomberg — https://news.bloomberglaw.com/international-trade/taiwan-to-curb-ai-chip-exports-to-china-as-part-of-us-trade-deal
- [S39] Tom's Hardware — https://www.tomshardware.com/tech-industry/semiconductors/taiwan-targets-illicit-ai-server-exports-to-china-with-five-year-prison-terms-strict-new-controls-follow-us-tariff-deal-and-super-micro-raid

## NiSource — energia para o campus da Microsoft em Indiana
- Em 16 de outubro, a NiSource, sediada em Merrillville, anunciou um acordo de energia de 20 anos com a Microsoft.
- O acordo acrescenta cerca de 1.100 MW de nova capacidade de geração para o campus da Microsoft no noroeste de Indiana.
- O fornecimento começa em 2028.
- A Microsoft financia integralmente toda a geração e transmissão necessárias para atender sua carga, por meio da subsidiária GenCo da NiSource.
- A estrutura visa proteger os clientes existentes da NIPSCO desses custos.
- A economia esperada para os clientes de energia elétrica da NIPSCO sobe para cerca de US$1,75 bilhão ao longo dos contratos de data center, ante US$1,4 bilhão.
- A economia equivale a até US$140 por cliente por ano.
- Em conexão com o acordo, a GenCo contratou 600 MW de armazenamento em baterias por meio de um acordo de tolling de longo prazo.
- As baterias serão desenvolvidas e construídas por uma afiliada do AGP Group, de Singapura.
- A energia vai abastecer o campus de data centers de US$1 bilhão da Microsoft em La Porte, Indiana.
**Fontes:**
- [S40] NiSource — https://www.nisource.com/news/article/nisource-announces-long-term-agreement-with-microsoft-expected-to-increase-customer-savings-and-support-indiana-s-economic-growth
- [S41] Inside INdiana Business — https://www.insideindianabusiness.com/articles/nisource-microsoft-ink-deal-to-power-la-porte-data-center-campus

## XHEART — rodada estratégica com Renault, Chery e CXMT
- A XHEART, startup chinesa que projeta chips de computação para direção autônoma e robôs, concluiu uma rodada estratégica de financiamento.
- A rodada foi noticiada em 16 de outubro.
- Com a rodada, o total captado pela XHEART chega a cerca de 5 bilhões de yuans (cerca de US$700 milhões).
- O Renault Group investiu na XHEART pela primeira vez.
- A Chery ampliou seu investimento na XHEART.
- A fabricante chinesa de memória CXMT (Changxin) também participou da rodada.
- O principal produto da XHEART, o chip X7, mira a direção assistida urbana L2++ e o mercado de autonomia L3/L4 (níveis da escala de automação veicular).
- O X7 estreou no ID.ERA 9X, da SAIC Volkswagen.
- O X7 chegou depois a modelos MG e Roewe, da SAIC, a modelos Cadillac, da GM, e a vários veículos da Chery.
- A XHEART foi incubada pela equipe de chips da Momenta.
- Uma sociedade ligada à Momenta detém o maior bloco de ações da XHEART.
- O valor da rodada e o valuation não foram divulgados.
**Fontes:**
- [S42] Yicai (via Eastmoney) — https://finance.eastmoney.com/a/202610163898636498.html
- [S43] Dealroom — https://dealroom.co/news/163350-chip-startup-xheart-draws-renault-hits-700m-total-raised/
- [S44] CTOL Digital Solutions — https://www.ctol.digital/news/xheart-strategic-round-renault-chery-cxmt-momenta-partnership/

## Foxconn — compra de 50% da unidade automotiva da Mitsubishi Electric
- Em 16 de outubro, a Lin Yin International Investment, subsidiária da Hon Hai (Foxconn), e a Mitsubishi Electric assinaram acordo definitivo para a Lin Yin comprar 50% da Mitsubishi Electric Mobility.
- O preço esperado da transferência de ações é de ¥115 bilhões (US$727 milhões).
- O acordo atribui à unidade um enterprise value de ¥320 bilhões (US$2,02 bilhões).
- O acordo atribui à unidade um valor patrimonial de ¥230 bilhões (US$1,45 bilhão).
- A conclusão está prevista para 1º de outubro de 2027, sujeita a aprovações antitruste.
- A Mitsubishi vai contribuir com tecnologia de powertrain elétrico, direção autônoma e inteligência embarcada para as plataformas de veículos elétricos da Foxconn.
- Os parceiros pretendem transformar a unidade num negócio com mais de ¥1 trilhão (US$6,32 bilhões) em vendas.
- No ano fiscal encerrado em março, a unidade teve receita de ¥876 bilhões (US$5,54 bilhões).
- No mesmo período, a unidade teve lucro operacional de ¥54 bilhões (US$341 milhões).
- A Mitsubishi Electric prevê registrar uma baixa contábil (impairment) de cerca de ¥100 bilhões (US$632 milhões) neste ano fiscal.
**Fontes:**
- [S45] Hon Hai Technology Group — https://www.foxconn.com/en-us/press-center/press-releases/latest-news/2124
- [S46] Bloomberg (via The Edge Malaysia) — https://theedgemalaysia.com/node/822306
- [S47] Automotive World — https://www.automotiveworld.com/news/foxconn-buys-into-mitsubishi-electrics-ev-parts-business/

## França — protestos contra o custo de vida viram distúrbios
- No sábado, 17 de outubro, manifestações em toda a França contra o aumento do custo de vida e a piora dos serviços públicos se transformaram em alguns dos piores distúrbios do país em décadas.
- O ministro do Interior, Laurent Nunez, estimou a participação em cerca de 550 mil pessoas.
- A central sindical CGT estimou 800 mil manifestantes.
- A polícia prendeu cerca de 1.800 pessoas no sábado, segundo a BBC, citando o Ministério do Interior.
- Mais de 500 policiais, gendarmes e bombeiros ficaram feridos, segundo o Ministério do Interior.
- Em Limoges, a prefeitura foi incendiada.
- Em Marselha, manifestantes vestidos de preto invadiram a prefeitura e picharam o prédio.
- Em Lyon, manifestantes incendiaram o posto de turismo da cidade.
- Cerca de 1.500 estabelecimentos comerciais foram atingidos em todo o país, segundo estimativa do CEO do Carrefour, Alexandre Bompard.
- Bompard disse que 50 lojas do Carrefour foram alvo, com reparos acima de €10 milhões (cerca de US$11,7 milhões).
- Bompard alertou que a conta total dos danos pode chegar a várias centenas de milhões de euros (centenas de milhões de dólares).
- A Sephora fechou toda a sua rede de lojas na França a partir das 17h de sábado e as manteve fechadas no domingo.
- Lojas de Louis Vuitton, Dior, Celine, Burberry, Lacoste e Apple estiveram entre as saqueadas ou danificadas.
- Segundo a France 24, o poder de compra na França vem caindo desde 2024.
- Segundo a France 24, o preço dos combustíveis disparou desde o início da guerra entre EUA e Irã, no início deste ano.
- O presidente Emmanuel Macron condenou a violência em pronunciamento na TV no domingo.
- Macron prometeu que os responsáveis pelos saques serão responsabilizados.
**Fontes:**
- [S48] Business of Fashion (Reuters) — https://www.businessoffashion.com/articles/news-analysis/mass-protests-in-france-spiral-into-worst-riots-in-years/
- [S49] BBC — https://www.bbc.com/news/articles/c574pdzl0k4no
- [S50] Retail Gazette — https://www.retailgazette.co.uk/blog/2026/10/sephora-shuts-french-stores-as-riots-leave-1500-retailers-counting-cost-of-damage/
- [S51] France 24 — https://www.france24.com/en/france/20261017-looters-seize-massive-french-protests-raid-vandalise-shops-france

## Irã — petroleiros atingem minas em Ormuz e Brent perto de US$110
- A Guarda Revolucionária do Irã (IRGC) disse que dois petroleiros, cada um com cerca de 2 milhões de barris de petróleo bruto, pegaram fogo após atingir minas navais no Estreito de Ormuz.
- Segundo a IRGC, os navios usavam uma rota não autorizada por Teerã.
- As alegações da IRGC não foram verificadas de forma independente.
- A UKMTO (centro britânico de operações de comércio marítimo) disse que ao menos 10 embarcações foram atacadas no estreito ou perto dele desde o domingo anterior.
- É o maior número semanal desde o início da guerra, em fevereiro.
- Outubro já soma 23 ataques registrados.
- Dados da Kpler mostram que o fluxo de petróleo pelo estreito caiu de quase 20,8 milhões de barris em 8 de outubro para 2,9 milhões em 11 de outubro.
- O Brent fechou a US$109,86 por barril na sexta-feira, 16 de outubro, maior fechamento desde 19 de maio.
- O WTI subiu 3,5% na sexta-feira, para US$101,41 por barril, seu primeiro fechamento acima de US$100 desde setembro.
- O chanceler iraniano, Abbas Araghchi, disse no domingo que o estreito seria reaberto no sexto dia se os EUA cumprirem as condições da proposta iraniana de sete dias.
- As condições são o fim do bloqueio naval, a suspensão das sanções ao petróleo e um cessar-fogo em todas as frentes.
- Pela proposta, as negociações começariam no sétimo dia.
- O comandante do CENTCOM (Comando Central dos EUA), almirante Brad Cooper, disse em 16 de outubro que o bloqueio naval americano impediu ao menos US$25 bilhões em exportações de petróleo do Irã.
- Cooper disse que Washington congelou quase US$350 milhões em criptoativos iranianos.
- Em 18 de outubro, o Parlamento do Irã aprovou Mehrdad Akhlaqi Ketabchi como ministro da Defesa, por 237 votos a 15.
- Ketabchi é ex-chefe da indústria de mísseis do Irã e alvo de sanções da ONU.
**Fontes:**
- [S52] Al Jazeera — https://www.aljazeera.com/news/2026/10/18/iran-says-two-tankers-catch-fire-after-hitting-mines-in-strait-of-hormuz
- [S53] CBS News — https://www.cbsnews.com/live-updates/iran-war-us-trump-strait-of-hormuz-yemen-houthis-saudi-arabia/
- [S54] NBC News — https://www.nbcnews.com/business/energy/oil-prices-hormuz-iran-ukraine-rcna603919
- [S55] RFE/RL — https://www.rferl.org/a/iran-live-blog-trump-middle-east/33803414.html

## Trump — suspensão da lei de sanções à Rússia
- Trump assinou na sexta-feira, 16 de outubro, uma ordem executiva que suspende um amplo pacote de sanções contra a Rússia que ele próprio havia sancionado como lei.
- Trump citou o interesse nacional para a suspensão.
- As sanções bloqueadas entrariam em vigor dois dias depois.
- O secretário de Estado, Marco Rubio, disse que a suspensão é uma pausa de 60 dias para analisar o impacto sobre a economia dos EUA e a economia global.
- A lei dava a Trump poder de impor tarifas de até 100% sobre importações dos cinco maiores compradores de petróleo e gás russos, sobretudo China e Índia.
- A lei também sancionava Putin, bancos russos e a frota sombra (navios usados para driblar sanções ao petróleo russo).
- Os senadores republicanos Ted Cruz, John Cornyn e Thom Tillis criticaram a medida, assim como democratas.
- Cruz, aliado de Trump, chamou a suspensão das sanções de erro.
- Cornyn chamou a medida de "imprudente".
- O enviado russo Kirill Dmitriev chamou a medida de "um momento importante e verdadeiramente histórico".
- Zelensky disse que a decisão "certamente ajuda apenas os russos".
- Zelensky citou ataques russos durante a noite contra 15 instalações de energia da Ucrânia.
- A suspensão vem depois de um acordo entre Trump e Putin que alivia sanções para a Rússia fornecer 4,8 milhões de toneladas métricas de diesel ao mercado global.
- O volume de diesel equivale a cerca de dez dias da demanda doméstica dos EUA.
- Especialistas dizem que o volume quase não vai mexer nos preços.
**Fontes:**
- [S56] Associated Press — https://apnews.com/article/russia-sanctions-trump-ukraine-e50c561ab805883bb4e484c092d8fadd
- [S57] BBC — https://www.bbc.com/news/articles/cxr5yvzv7rp0o
- [S58] CNBC — https://www.cnbc.com/2026/10/17/trump-diesel-russia-ukraine-war.html

## China — PIB do terceiro trimestre cresce 4,5%
- O PIB da China cresceu 4,5% na comparação anual no terceiro trimestre de 2026, segundo o Escritório Nacional de Estatísticas, na segunda-feira, 19 de outubro.
- No segundo trimestre, o crescimento havia sido de 4,3%.
- Nos três primeiros trimestres de 2026, o crescimento foi de 4,6% na comparação anual.
- Os 4,3% do segundo trimestre foram o crescimento mais lento desde 2022.
- O resultado do terceiro trimestre superou a previsão de consenso de 4,41% dos economistas consultados pela Wind, provedora chinesa de dados financeiros.
- O número fica no piso da meta anual de crescimento de Pequim, de 4,5% a 5%.
- Segundo a BBC, o boom da IA ajudou a impulsionar as exportações chinesas.
- A manufatura de alta tecnologia cresceu 14,3%.
- A produção de robôs industriais subiu 29,1%.
- A produção de baterias de íon-lítio subiu 39,5%.
- A produção de equipamentos de impressão 3D subiu 62,5%.
- O investimento imobiliário caiu mais de 20% nos nove primeiros meses do ano, na comparação anual.
- O superávit comercial da China caminha para superar o recorde de US$1,2 trilhão do ano passado.
**Fontes:**
- [S59] gov.cn (Xinhua) — https://english.www.gov.cn/archive/statistics/202610/19/content_WS6ad5a59bc6d00ca5f9a0dc86.html
- [S60] BBC — https://www.bbc.com/news/articles/cm5yn098xz8lo
- [S61] South China Morning Post — https://www.scmp.com/economy/economic-indicators/article/3371335/chinas-economy-grows-45-third-quarter-staying-track-annual-target

## Nasdaq — pior semana desde junho
- Na sexta-feira, 16 de outubro, o Nasdaq caiu 2,1%.
- Na semana, o Nasdaq recuou 4,5%, sua pior semana desde junho, interrompendo uma sequência de quatro semanas de alta.
- O S&P 500 caiu 1,2% na sexta-feira e cerca de 2% na semana.
- As ações de tecnologia perderam mais de US$1 trilhão em valor de mercado na sexta-feira.
- O índice de semicondutores da Filadélfia caiu 3,8% na sexta-feira, sua oitava queda seguida.
- É a maior sequência de quedas do índice de semicondutores da Filadélfia desde 2008.
- A CoreWeave, apoiada pela Nvidia, caiu cerca de 12% na sexta-feira e cerca de 25% nos cinco pregões da semana.
- Os títulos de dívida da CoreWeave foram vendidos com força na semana, levando seus rendimentos (yields) acima de 15%.
- A venda ocorreu em meio a temores de que empresas endividadas de infraestrutura de IA não consigam pagar suas dívidas com a alta dos custos de captação.
- O yield do Treasury de 10 anos operava acima de 5,09%.
- O yield do Treasury de 10 anos havia saltado para 5,33% na quarta-feira, com a divulgação do CPI (índice de preços ao consumidor dos EUA).
- Os operadores passaram a precificar 89% de chance de alta de juros pelo Fed na reunião de dezembro.
- A precificação veio depois de uma fala do presidente do Fed, Kevin Warsh, num evento do FMI em Bangkok.
- O VIX (índice de volatilidade da Cboe) superou 22 pela primeira vez em quatro meses.
- Michael Hartnett, do Bank of America, adotou postura "risk-off" (de aversão a risco) para o próximo mês, citando yields, petróleo e o risco das eleições de meio de mandato.
- O Barclays agora espera altas de 25 pontos-base nos juros do Fed em dezembro e em janeiro.
- A projeção do Barclays veio após leituras de CPI e PPI (índice de preços ao produtor) acima do esperado.
**Fontes:**
- [S62] Yahoo Finance / Investopedia — https://finance.yahoo.com/markets/stocks/articles/markets-news-oct-16-2026-103800633.html
- [S63] NBC News — https://www.nbcnews.com/business/energy/oil-prices-hormuz-iran-ukraine-rcna603919
- [S64] StreetInsider (Reuters) — https://www.streetinsider.com/Market+Check/Wall+Street+tumbles+as+worries+about+AI+trade+and+high+oil+prices+weigh/27195576.html
- [S65] CNBC — https://www.cnbc.com/2026/10/15/stock-market-today-live-updates.html

## Operadoras europeias — oferta conjunta por espectro de satélite
- Em 19 de outubro, Deutsche Telekom, Orange, Telefónica e Vodafone assinaram uma carta de intenções para estudar uma oferta conjunta pelo futuro espectro de Serviços Móveis por Satélite (MSS) na Europa.
- As quatro operadoras pretendem montar infraestrutura de rede terrestre e funções de coordenação e monitoramento na Europa.
- As operadoras não vão investir diretamente em uma constelação de satélites.
- A constelação virá de um parceiro de satélites ainda a ser escolhido.
- O grupo diz que dará a todas as operadoras móveis acesso aberto e não discriminatório para oferecer serviços direct-to-device (D2D, conexão por satélite direto ao celular).
- A iniciativa apoia as metas de soberania da Comissão Europeia.
- A oferta mira a parcela da faixa de 2 GHz que a União Europeia propôs reservar a um operador europeu.
- O objetivo é fazer frente ao Starlink, de Elon Musk.
- A carta de intenções não substitui as parcerias de satélite já existentes das operadoras.
- A Deutsche Telekom já trabalha com o Starlink Mobile, da SpaceX, e com a Iridium em D2D e IoT (internet das coisas) via satélite.
**Fontes:**
- [S66] Telefónica — https://www.telefonica.com/en/communication-room/press-room/european-operators-sign-letter-intent-explore-joint-bid-mobile-satellite-services-spectrum-advance-direct-device-services/
- [S67] Bloomberg Law — https://news.bloomberglaw.com/ip-law/europes-top-carriers-explore-satellite-group-to-fend-off-spacex
- [S68] Space Intel Report — https://www.spaceintelreport.com/deutsche-telekom-orange-telefonica-vodafone-sign-loi-on-joint-bid-for-european-2-ghz-mobile-satellite-spectrum/

## Roche — FDA aprova Enspryng para doença ocular da tireoide
- Em 16 de outubro, a Roche anunciou que a FDA (agência que regula medicamentos e alimentos nos EUA) aprovou o Enspryng (satralizumab) para adultos com doença ocular da tireoide (TED).
- O Enspryng é a primeira e única opção de tratamento subcutâneo para uso em casa contra a TED.
- O Enspryng é um anticorpo pioneiro em sua classe contra o receptor de IL-6 (interleucina-6, proteína ligada à inflamação).
- Na fase de manutenção, o Enspryng é aplicado a cada quatro semanas.
- O medicamento pode ser autoaplicado ou aplicado por um cuidador.
- No estudo de fase III SatraGO-2, 52,9% dos pacientes tratados com Enspryng tiveram resposta em proptose (olhos saltados), contra 23,4% no grupo placebo.
- No SatraGO-2, 60,7% dos pacientes com Enspryng tiveram redução da visão dupla, contra 25,8% no grupo placebo.
- O estudo SatraGO-1 não atingiu seu desfecho primário.
- A TED é uma doença autoimune rara que afeta cerca de 155 em cada 100 mil pessoas nos EUA.
- A TED é a segunda indicação do Enspryng, aprovado em 2020 para o distúrbio do espectro da neuromielite óptica.
**Fontes:**
- [S69] Roche — https://www.roche.com/media/releases/med-cor-2026-10-16
