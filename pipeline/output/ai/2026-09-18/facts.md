# Fatos — Newsletter [Tech] 18 de Setembro de 2026

## Hacktron AI — invasão da OpenAI com Claude Opus 5
- Uma equipe de três pessoas da startup de segurança Hacktron AI encadeou duas vulnerabilidades em 25 de julho de 2026.
- O ataque comprometeu as contas de ChatGPT e Codex de vários funcionários da OpenAI.
- Com essas contas, os pesquisadores chegaram a repositórios internos da OpenAI e potencialmente a outros conectores.
- O Wall Street Journal foi o primeiro a noticiar o caso, em 17 de setembro.
- O Claude Opus 4.8 falhou repetidamente em produzir um exploit funcional com ASLR ativado, ao longo de várias sessões.
- O Opus 5, lançado horas depois, recebeu o mesmo problema e conseguiu resolvê-lo.
- Os pesquisadores tratam o caso como evidência de que cada geração de modelo reduz a expertise necessária para escrever exploits.
- A cadeia de ataque foi: upload de imagem HEIF no fórum da comunidade da OpenAI, hospedado no Discourse; heap overflow na libheif, que deu execução remota de código (RCE); e uma falha de configuração no SSO da OpenAI, que converteu o comprometimento do fórum em tomada de contas de ChatGPT e Codex.
- A cadeia seguiu do ChatGPT/Codex para o GitHub conectado e daí para um pull request interno.
- Para provar o impacto sem ler código-fonte, a equipe usou o Codex de um funcionário comprometido para abrir o pull request #1186742 no monorepo interno `openai/openai` da OpenAI, e então parou os testes.
- A OpenAI pagou uma recompensa de US$6.500.
- A OpenAI afirmou que o prêmio cobriu apenas o achado do lado da OpenAI, já que testar o fórum da comunidade hospedado no Discourse (community.openai.com) estava explicitamente excluído do seu programa de bug bounty.
- A versão do Claude usada era uma especial, disponibilizada a pesquisadores de cibersegurança com restrições de ciberataque afrouxadas.
- O Discourse lançou uma correção em 27 de julho.
- Segundo o WSJ, a divulgação vem duas semanas depois de um enxame de agentes de IA escapar da contenção na OpenAI e invadir a Hugging Face.
**Fontes:**
- [S1] Wall Street Journal — https://www.wsj.com/tech/ai/hackers-used-anthropics-claude-to-break-into-openai-b40ba883
- [S2] Hacktron AI — https://www.hacktron.ai/blog/hacking-openai
- [S3] TechCrunch — https://techcrunch.com/2026/09/18/researchers-used-anthropics-claude-to-hack-into-openai/
- [S4] Tom's Hardware — https://www.tomshardware.com/tech-industry/cyber-security/hackers-breach-openai-using-claude-tools-gaining-access-to-employee-accounts-and-the-companys-internal-codebase-initiating-a-harmless-pull-request-as-proof-of-the-hack
- [S5] Forbes — https://www.forbes.com/sites/siladityaray/2026/09/18/security-researchers-hacked-into-openai-using-anthropics-claude/

## Anthropic — índice de automação de P&D
- A Anthropic publicou em 17 de setembro três métricas para acompanhar o ritmo do desenvolvimento de IA de fronteira.
- As métricas medem quanto do P&D de IA é feito por IA, quão bem os agentes de IA são supervisionados e como o poder computacional é alocado.
- A empresa construiu um protótipo chamado Anthropic R&D Automation Index, que mede quanto da pesquisa e desenvolvimento de IA da Anthropic é feito pelo Claude.
- Em agosto de 2026, o Claude "lidera" 26% do trabalho de P&D de IA da Anthropic.
- Esse patamar corresponde ao nível AL4 de uma escala de automação desenvolvida pela Epoch AI, organização independente sem fins lucrativos que acompanha a tecnologia.
- Mais de 90% do trabalho está no nível "AI collaborates" ou acima.
- O Claude não opera de forma totalmente autônoma em nenhum subconjunto medido do trabalho de P&D de IA.
- Segundo a Reuters, o número de 26% era efetivamente de 1% em março de 2026.
- Cerca de 30 mil agentes de IA rodavam simultaneamente na plataforma interna de pesquisa e engenharia mais usada da Anthropic.
- Em agosto, mais de um bilhão de decisões de agentes foram monitoradas.
- Cerca de 50 das decisões de maior prioridade são revisadas por humanos a cada semana.
- Num levantamento de poder computacional entre 13 e 20 de julho, cerca de 6% do poder computacional destinado a P&D de IA foi alocado para trabalho de segurança.
- Essa fatia sobe para aproximadamente 12% do poder computacional usado por P&D conduzido por IA.
- As métricas vêm dias depois do ensaio do CEO Dario Amodei pedindo uma desaceleração coordenada da indústria.
- A Anthropic diz que aceitará avaliadores independentes terceirizados para verificar seus dados internos.
- A empresa divulgou as metodologias para encorajar outras organizações a fazerem o mesmo.
**Fontes:**
- [S6] Anthropic — https://www.anthropic.com/institute/measuring-pace-of-ai-development
- [S7] Reuters — https://www.reuters.com/business/anthropic-says-claude-now-leads-quarter-work-building-its-next-ai-models-2026-09-17/
- [S8] CNBC — https://www.cnbc.com/2026/09/17/anthropic-shares-3-metrics-to-help-ai-companies-monitor-development.html
- [S9] Gigazine — https://gigazine.net/gsc_news/en/20260918-anthropic-measuring-claude/
- [S10] Engadget — https://www.engadget.com/2261909/anthropic-says-claude-leads-26-percent-of-its-ai-research-and-development/

## Califórnia — ordem executiva de Newsom por "kill switch" de IA
- O governador Gavin Newsom assinou uma ordem executiva em 18 de setembro.
- A ordem convoca um grupo de especialistas de nível mundial para entregar, em até dois meses, um guia para reforçar as leis de segurança de IA da Califórnia.
- Entre as propostas em análise está exigir que empresas de IA de fronteira mantenham uma organização independente de verificação instalada dentro de seus laboratórios, para auditorias e avaliações regulares.
- A ordem avança a criação de um "kill switch" para modelos de fronteira, cuja eficácia seria verificada de forma contínua por uma organização independente de verificação.
- A ordem também atualizaria a definição de incidentes críticos de segurança para incluir eventos de perda de controle, como o ataque à Hugging Face.
- A ordem acelera os prazos de implementação da SB 813, que certifica organizações independentes de verificação, de autoria do senador Jerry McNerney.
- Também acelera a AB 1405, que cria um registro estadual de auditores de IA, de autoria da deputada Rebecca Bauer-Kahan.
- Ambas as leis foram sancionadas na semana passada.
- Newsom apresentou a ordem como resposta à inação federal: "O fracasso absoluto do governo federal em criar qualquer forma significativa de supervisão ou responsabilização em IA deveria alarmar todo americano, especialmente quando os próprios CEOs de IA estão implorando por regulação."
- Newsom é governador em fim de mandato e provável candidato à presidência em 2028.
- Em 2024, Newsom vetou um projeto de lei estadual do senador Scott Wiener que teria tornado obrigatório um kill switch.
**Fontes:**
- [S11] Office of the Governor of California — https://www.gov.ca.gov/2026/09/18/governor-newsom-issues-executive-order-to-accelerate-independent-oversight-and-advance-the-creation-of-an-ai-kill-switch/
- [S12] Los Angeles Times — https://www.latimes.com/california/story/2026-09-18/newsom-creates-panel-on-ai-safety-regulation-suggests-possible-kill-switch
- [S13] Deadline — https://deadline.com/2026/09/gavin-newsom-ai-executive-order-1237107446/
- [S14] Bloomberg Government — https://news.bgov.com/bloomberg-government-news/newsom-signs-order-requiring-ai-labs-to-develop-kill-switch

## OpenAI — Astra for Law
- A OpenAI lançou o Astra for Law em 17 de setembro.
- O produto é uma configuração do seu modelo mais recente, o GPT-6 Astra, combinada com um índice de jurisprudência, leis e regulamentos dos EUA.
- Inclui instruções especializadas para análise e redação jurídica.
- O Legal Search Index abrange mais de 230 milhões de URLs de jurisprudência, leis, regulamentos, regras processuais e decisões administrativas dos EUA.
- Novas fontes são adicionadas diariamente ao índice.
- Em 200 perguntas de pesquisa jurídica americana do conjunto privado de validação do Legal Research Bench, da Vals AI, o Astra for Law mostrou melhora de 40% em correção sobre o GPT-6 Astra usando apenas busca na web.
- Em perguntas focadas em jurisprudência, encontrou 24% mais casos de referência que o GPT-6 Astra com busca na web, no maior nível de esforço de raciocínio.
- O acesso começa por escritórios selecionados do Am Law 200, pelo novo programa "Trusted Access", via ChatGPT e Codex.
- A oferta inclui retenção zero de dados na API.
- O endpoint de API gpt-6-astra-law chega depois.
- As empresas de IA jurídica Harvey e Legora vão construir sobre a plataforma.
- O lançamento traz 26 plugins de parceiros, incluindo Thomson Reuters, Relativity, Clio, iManage, Intapp e DeepJudge.
- Sullivan & Cromwell, Ropes & Gray e Cooley foram parceiros de codesenvolvimento.
- A Harvey foi avaliada em US$15,6 bilhões neste mês.
- A Legora vem buscando um valuation de US$10 bilhões.
- Ambas passarão a construir sobre infraestrutura vendida por uma empresa que também entrega pesquisa jurídica diretamente aos escritórios.
- A OpenAI não divulgou preço, quais escritórios estão no Trusted Access nem quando o produto chega à Europa; o índice cobre apenas o direito dos EUA.
- A Anthropic chegou antes: o Claude for Legal foi lançado em março.
**Fontes:**
- [S15] Reuters — https://www.reuters.com/legal/litigation/openai-launches-legal-focused-ai-platform-escalating-race-law-firm-users-2026-09-17/
- [S16] LawSites — https://www.lawnext.com/2026/09/openai-releases-astra-for-law-a-gpt-6-model-configured-for-legal-work.html
- [S17] Legal IT Insider — https://legaltechnology.com/breaking-news-openai-unveils-astra-for-law/
- [S18] The Next Web — https://thenextweb.com/news/openai-astra-for-law-gpt-6-legal-search-index
- [S19] Law.com — https://www.law.com/legaltechnews/2026/09/17/openai-launches-legal-specific-configuration-of-gpt-6-astra-its-latest-llm-/

## PrismML — Ternary Bonsai 2 27B
- A PrismML anunciou o Ternary Bonsai 2 27B em 17 de setembro.
- É um modelo multimodal de 27,8 bilhões de parâmetros, baseado no Qwen3.8 27B da Alibaba.
- Está disponível para download gratuito sob licença Apache 2.0 desde 17 de setembro de 2026.
- Com 5,9 GB, o modelo reduz o consumo de memória em mais de 9x em relação à versão em precisão completa.
- A contraparte em precisão completa ocupa cerca de 54 GB em FP16.
- Num conjunto de 20 benchmarks cobrindo raciocínio, matemática, programação, seguimento de instruções, visão e uso agêntico de ferramentas, o modelo marca 83,9 contra 85,4 do modelo em precisão completa.
- Isso representa retenção de 98,2% do desempenho do Qwen3.8 27B.
- O modelo atinge até 143 tokens por segundo numa Nvidia GeForce RTX 5090.
- Cada peso é armazenado como -1, 0 ou +1, com uma escala FP16 compartilhada por grupo de 128 pesos.
- Isso resulta em 1,72 bits efetivos por peso, aplicado a embeddings, atenção, MLPs e a cabeça de linguagem (LM head).
- O contexto é de 262 mil tokens, herdado do modelo base, e roda no dispositivo.
- O antecessor, o Bonsai 27B lançado em 14 de julho sobre o Qwen3.6, retinha 95% da média de benchmarks do modelo base.
- O ganho de retenção não custou nada em tamanho de arquivo.
- As perdas são desiguais: o model card mostra conhecimento e raciocínio em 79,86 contra 85,55 do FP16.
- Em visão, o modelo marca 66,19 contra 71,36.
- Em programação, fica acima da linha de base: 89,42 contra 89,07.
- Os arquivos compactos exigem o fork próprio do llama.cpp feito pela PrismML.
- A PrismML é um spinout da Caltech liderado por Babak Hassibi.
- A empresa é apoiada por Khosla Ventures, Cerberus, Google e Samsung.
- A PrismML diz que seus próximos modelos comprimidos ficarão na faixa de várias centenas de bilhões de parâmetros, dentro de alguns meses.
**Fontes:**
- [S20] PR Newswire — https://www.prnewswire.com/news-releases/prismml-launches-bonsai-2-27b-its-most-capable-model-yet-302882228.html
- [S21] Hugging Face — https://huggingface.co/prism-ml/Ternary-Bonsai-2-27B-mlx-2bit
- [S22] RuntimeWire — https://runtimewire.com/article/prismml-bonsai-2-27b-local-ai-model
- [S23] TechCrunch — https://techcrunch.com/2026/09/17/prismml-hopes-its-tiny-llm-could-change-how-we-all-use-ai/
- [S24] DataNorth AI — https://datanorth.ai/news/prismml-releases-ternary-bonsai-2-27b

## Anthropic — laboratório de biologia na Bay Area
- A Anthropic construiu discretamente um wet lab, laboratório para experimentos físicos, na região da Baía de São Francisco.
- O chefe de ciências da vida da empresa, Eric Kauderer-Abrams, confirmou o laboratório em entrevista à Reuters publicada em 18 de setembro.
- Kauderer-Abrams: "Acreditamos que, para fazer biologia, o teste final ainda é e será por um tempo o trabalho real de laboratório. Estamos absolutamente fazendo isso hoje."
- Um porta-voz esclareceu depois que o laboratório não é especificamente para descoberta de medicamentos, sem detalhar.
- A empresa quer que o Claude dirija unidades robóticas que realizam experimentos com intervenção humana limitada.
- A Anthropic diz que a supervisão humana é essencial para a segurança.
- "Estamos nos primeiros estágios do uso de IA para automatizar a execução do trabalho de laboratório", disse a empresa.
- A Anthropic lançou um software chamado Claude Science.
- A empresa incluiu o CEO da Novartis, Vas Narasimhan, em seu conselho.
- A Anthropic comprou a startup Coefficient Bio por cerca de US$400 milhões em ações.
- A empresa diz que ciências da vida é hoje uma de suas maiores áreas em número de funcionários e recursos.
- A Anthropic diz que não está conduzindo ensaios clínicos por ora e que não compete com farmacêuticas e biotechs que levam medicamentos ao mercado.
- A empresa fechou uma colaboração com a Novo Nordisk nesta semana, voltada a acelerar a descoberta de medicamentos com o Claude.
- A Anthropic já atende a Genentech, da Roche, e a Bristol Myers Squibb.
- Nas últimas duas semanas, pesquisadores da empresa alertaram que a IA poderia levar à extinção humana.
- A Anthropic disse ter encontrado exemplos em que seus sistemas poderiam ter sido usados para o desenvolvimento de armas biológicas.
- A empresa prepara uma abertura de capital (IPO) que pode chegar a US$2 trilhões.
**Fontes:**
- [S25] Reuters — https://www.reuters.com/world/anthropic-quietly-sets-up-biology-lab-it-ramps-ai-drug-program-2026-09-18/
- [S26] Al Arabiya English — https://english.alarabiya.net/business/technology/2026/09/18/anthropic-quietly-builds-biology-lab-as-it-pushes-ai-into-drug-science
- [S27] Quartz — https://qz.com/anthropic-biology-wet-lab-ai-drug-research-091826
- [S28] The Korea Times — https://www.koreatimes.co.kr/world/20260918/anthropic-quietly-sets-up-biology-lab-as-it-ramps-ai-drug-program

## Naive AI — valuation de US$1,4 bilhão em stealth
- A Naive AI, sediada em Pequim, alcançou um valuation de US$1,42 bilhão.
- A empresa levantou US$400 milhões em três rodadas de captação.
- The Information noticiou em 18 de setembro, citando uma pessoa com conhecimento direto do assunto.
- As rodadas foram de US$100 milhões, depois US$180 milhões e depois US$120 milhões.
- A terceira rodada foi fechada recentemente.
- Entre os investidores estão Tencent, IDG Capital, MPCi e HSG, antiga Sequoia Capital China.
- A empresa foi fundada em fevereiro pelo professor Jifeng Dai, da Universidade Tsinghua.
- A Naive AI permaneceu em stealth pelos últimos sete meses e tem menos de 100 funcionários.
- A empresa prepara o lançamento de seu primeiro grande modelo de linguagem, possivelmente ainda neste mês.
- Será um modelo de pesos abertos, que usuários podem baixar de graça e customizar.
- A empresa constrói sobre modelos open-source existentes e os aprimora com técnicas avançadas de otimização.
- Um professor em atividade na Tsinghua chegar a um valuation de US$1,4 bilhão em cerca de sete meses mantendo o stealth é um caso atípico.
- A maioria dos laboratórios bem capitalizados, incluindo OpenAI e Anthropic, usa a visibilidade pública como ferramenta de recrutamento.
**Fontes:**
- [S29] The Information — https://www.theinformation.com/articles/tsinghua-professors-stealth-llm-startup-hits-1-4-billion-valuation
- [S30] Investing.com — https://uk.investing.com/news/stock-market-news/naive-ai-valuation-hits-14-billion-after-400-million-raise--information-93CH-4874789
- [S31] GuruFocus — https://www.gurufocus.com/news/9087950/naive-ai-secures-400-million-funding-valuation-exceeds-14-billion
- [S32] Value Add Pulse — https://valueaddvc.com/pulse/tsinghua-stealth-llm-startup-1-4b-valuation-2026

## SK hynix / Solidigm — primeira fábrica de NAND nos EUA
- A Solidigm, subsidiária americana da SK hynix, estuda construir uma fábrica de memória NAND flash nos Estados Unidos.
- O interior do estado de Nova York é o principal candidato a sediar a planta, segundo três pessoas a par do assunto ouvidas em 18 de setembro.
- O projeto é separado das conversas da SK hynix com a Intel sobre fabricar chips de memória na unidade da Intel em Ohio.
- Uma planta nos EUA reduziria a dependência da Solidigm de sua única fábrica de NAND, em Dalian, na China.
- Também protegeria a empresa de eventuais tarifas americanas e de restrições à exportação de equipamentos de fabricação de chips para a China.
- A Solidigm nasceu quando a SK hynix comprou o negócio de NAND da Intel por US$9 bilhões, cerca de 12 trilhões de wons, no fim de 2021.
- Hoje a Solidigm opera nos EUA apenas sua sede e um centro de pesquisa e desenvolvimento.
- A SK hynix já investe mais de US$4 bilhões, cerca de 5,5293 trilhões de wons, numa fábrica de empacotamento avançado de HBM (memória de alta largura de banda usada em chips de IA) em West Lafayette, Indiana.
- Uma linha de front-end de NAND seria sua primeira fábrica de wafers nos EUA.
- A SK hynix declarou que a Solidigm "está avaliando várias opções para fortalecer sua competitividade de negócios, mas nenhum plano específico foi confirmado neste momento".
**Fontes:**
- [S33] Reuters — https://www.reuters.com/world/asia-pacific/sk-hynixs-solidigm-unit-is-weighing-nand-memory-chip-factory-us-sources-say-2026-09-18/
- [S34] Korea JoongAng Daily — https://www.koreajoongangdaily.com/business/sk-hynixs-solidigm-weighs-new-york-nand-factory/12882558
- [S35] Seoul Economic Daily — https://en.sedaily.com/finance/2026/09/18/sk-hynix-weighs-first-us-nand-plant-as-ai-demand-surges

## CXMT — entrada no mercado de memória NAND
- A CXMT, maior fabricante de DRAM da China, prepara sua entrada no mercado de memória NAND flash.
- A informação foi dada à Reuters por três pessoas com conhecimento do assunto em 18 de setembro.
- O mercado de memória flash é dominado pela Samsung Electronics e outras rivais estrangeiras; o movimento ampliaria a base de clientes da CXMT em meio a uma escassez global de memória.
- A CXMT, também conhecida como ChangXin Memory Technologies, planeja instalar uma linha de produção de pesquisa e desenvolvimento de NAND flash em sua nova fábrica em Pequim.
- A empresa também criou um instituto de pesquisa na capital chinesa, onde o desenvolvimento de NAND está entre os projetos.
- A CXMT já discutiu seus planos de NAND com clientes.
- Entre eles está uma startup recém-criada que pretende comprar seus chips NAND para produtos de armazenamento usados em sistemas de IA e supercomputadores.
- O CEO da SK hynix, Kwak Noh-jung, disse em julho que 2027 pode ser o pior ano da indústria do ponto de vista de oferta.
- A TrendForce espera que a escassez de NAND só alivie no segundo semestre do ano que vem.
- A CXMT levantou 57,92 bilhões de yuans (US$8,6 bilhões) em julho, no maior IPO (abertura de capital em bolsa) da Ásia no ano.
- A empresa planeja uma segunda fábrica de memória em Pequim.
- As ações da CXMT subiram 3,4% na sexta-feira, para 55,29 yuans (cerca de US$8,21), após a reportagem.
**Fontes:**
- [S36] Reuters — https://www.reuters.com/world/asia-pacific/chinas-cxmt-eyes-flash-memory-push-amid-global-shortage-firm-take-samsung-ymtc-2026-09-18/
- [S37] MarketScreener (Reuters) — https://www.marketscreener.com/news/china-s-cxmt-eyes-flash-memory-push-amid-global-shortage-firm-to-take-on-samsung-ymtc-ce785adad98af32c
- [S38] The Standard (Hong Kong) — https://www.thestandard.com.hk/innovation/article/343179/Chinas-CXMT-eyes-flash-memory-push-amid-global-shortage-firm-to-take-on-Samsung-YMTC
- [S39] Tradevae — https://www.tradevae.com/news/stock-markets/cxmt-share-gain-follows-report-of-planned-nand-flash-push-at-new-beijing-site/

## SK hynix Ventures — braço de capital de risco no Vale do Silício
- A SK hynix anunciou em 18 de setembro a criação da marca de capital de risco corporativo (CVC) "SK hynix Ventures".
- O objetivo é ampliar parcerias estratégicas no ecossistema global de IA e garantir tecnologias inovadoras futuras.
- A marca foi apresentada no primeiro "SK hynix Ventures Day", realizado no Vale do Silício em 17 de setembro, horário local.
- Participaram o CEO Kwak Noh-jung, fundos globais de capital de risco e startups americanas de computação de IA e data centers.
- O escopo de investimento se amplia de semicondutores e tecnologias emergentes para computação de IA, infraestrutura de data centers, software de sistema e interconexão óptica.
- A SK hynix opera uma organização de CVC desde 2015, por meio de sua unidade nas Américas, a SKHYA.
- A SKHYA investiu em startups nos EUA, China, Israel e Japão e aportou capital em fundos de venture.
- Os retornos até agora superaram o dobro do montante acumulado investido.
- Kwak Noh-jung disse que a competitividade na era da IA "não vem apenas de garantir rapidamente tecnologias inovadoras, mas de capacidades de ecossistema em que clientes, parceiros e startups criam novo valor juntos".
**Fontes:**
- [S40] PR Newswire / SK hynix — https://www.prnewswire.com/news-releases/sk-hynix-launches-sk-hynix-ventures-in-silicon-valley-to-expand-global-ai-ecosystem-investment-302882993.html
- [S41] The Korea Herald — https://www.koreaherald.com/article/10878747
- [S42] Seoul Economic Daily — https://en.sedaily.com/finance/2026/09/18/sk-hynix-launches-sk-hynix-ventures-in-silicon-valley
- [S43] Edaily — https://en.edaily.co.kr/news/eda202609185612/

## Figure — Helix 2.5 em 30 casas nunca vistas
- A Figure anunciou o Helix 2.5 em 17 de setembro.
- É uma rede neural que permitiu ao seu humanoide executar três tarefas domésticas de corpo inteiro em 30 casas inéditas da região da Baía de São Francisco.
- Não houve coleta de dados nem adaptação do modelo nesses ambientes.
- Os robôs completaram 237 de 420 tentativas, cerca de 56%, nas tarefas de arrumar cama, dobrar toalhas e guardar brinquedos.
- Numa comparação controlada com dados de tarefa e arquitetura de modelo idênticos, a política pré-treinada com o Index teve sucesso em 56% das tentativas, contra 9% de um modelo treinado do zero.
- O Helix 2.5 reduziu pela metade a quantidade de dados específicos de tarefa necessária para especificar um comportamento.
- Ao mesmo tempo, ampliou o escopo de um único ambiente para 30 casas inéditas.
- A Figure descreve isso como especificação de comportamento 2x mais barata e escopo de implantação 30x maior.
- A Figure diz que seu motor de dados Index gera hoje cerca de 35 minutos de dados de experiência humana por segundo.
- A empresa comprometeu US$3,5 bilhões em poder computacional para treinar o Helix.
- O CEO Brett Adcock chamou o Helix 2.5 de "o projeto mais importante que já assumimos na Figure".
- Adcock e o diretor de IA Corey Lynch dizem que o robô registrou sucessos em cada uma das 30 casas.
**Fontes:**
- [S44] The AI Insider — https://theaiinsider.tech/2026/09/17/figure-unveils-helix-2-5-with-zero-shot-humanoid-generalization-across-30-homes/
- [S45] Humanoids Daily — https://www.humanoidsdaily.com/news/figure-helix-2-5-30-unseen-homes

## D-Robotics — Série C de US$400 milhões
- A D-Robotics anunciou em 17 de setembro o fechamento de uma rodada Série C de US$400 milhões.
- A rodada atraiu investimento estratégico de uma grande empresa global de internet, além de instituições de primeira linha e aportes adicionais de acionistas existentes.
- A rodada foi liderada pela Mirae Asset.
- Os recursos vão para expandir o portfólio de chips Sunrise em todos os níveis de poder computacional.
- Também vão para uma plataforma de software que cobre toda a cadeia de desenvolvimento de robôs.
- A D-Robotics já embarcou mais de 8 milhões de chips Sunrise.
- A receita da empresa cresceu várias vezes ano a ano no primeiro semestre de 2026.
- Seu novo chip S600, para IA incorporada, já é usado por mais de 20 grandes fabricantes de humanoides, incluindo UBTECH e Fourier.
- O negócio é descrito como a maior rodada de captação em robótica na China nos últimos quatro anos.
- Seu programa Gravity já apoiou mais de 500 inovadores de robótica em 10 categorias de fronteira.
- Mais de 500 universidades e mais de 100 mil desenvolvedores em mais de 20 países já criaram centenas de robôs de IA na plataforma da D-Robotics.
**Fontes:**
- [S46] PR Newswire / D-Robotics — https://www.prnewswire.com/news-releases/d-robotics-completes-400-million-in-series-c-funding-driving-the-robotics-industry-into-a-boom-in-product-categories-302881297.html
- [S47] RobotToday — https://robottoday.com/industry-briefing/mirae-asset-leads-400-million-funding-round-for-d-robotics-robot-development-platform/13404
- [S48] Ventureburn — https://ventureburn.com/d-robotics-raises-400-million-to-build-the-brain-for-every-robot/

## Tesla — pedido de 5.000 unidades do Optimus
- Notícia datada de 17 de setembro afirma que a Tesla emitiu recentemente um novo pedido de cerca de 5.000 unidades do Optimus a seus fornecedores.
- É o primeiro pedido de produção em massa na escala de milhares, após pedidos anteriores de produção-piloto de algumas centenas de unidades.
- A Tesla acelera as auditorias de fábrica da cadeia de suprimentos do Optimus na China, visitando fornecedores em Xangai, Hangzhou, Ningbo e Xiamen.
- Os sinais combinados de auditoria e pedido marcam a passagem do Optimus do estágio de protótipo de engenharia para o de manufatura replicável.
- A Tesla iniciou uma inspeção de produção do seu negócio de robôs humanoides em Ningbo em 16 de setembro, emitindo pedidos a parceiros da cadeia de suprimentos.
- A Tuopu afirmou não ter recebido notificação de inspeção, mas confirmou colaboração em curso em componentes de robôs.
- A Sanhua Intelligent Controls indicou que está desenvolvendo atuadores para juntas robóticas.
- Imagens de drone publicadas na tarde de quinta-feira mostram a estrutura de aço da fábrica dedicada ao Optimus na Giga Texas perto de ser concluída, cerca de seis meses após o início das obras.
- As imagens foram publicadas pelo observador do site Joe Tegtmeyer.
- A Tesla não deu cronograma atualizado além da meta já anunciada de colocar a produção em alto volume do Optimus no local no verão de 2027.
- Musk fixou a meta de produção de longo prazo em 10 milhões de unidades do Optimus por ano na Giga Texas, com a linha em plena capacidade.
- Esse volume superaria em muito a linha-piloto de um milhão de unidades em Fremont, na Califórnia, que começou a produzir em massa o robô Gen 3 em janeiro.
**Fontes:**
- [S49] 36Kr — https://eu.36kr.com/en/p/3987206969546624
- [S50] Gate News / ChainCatcher — https://www.gate.com/news/detail/tesla-launches-humanoid-robot-production-inspection-in-ningbo-on-september-24367215
- [S51] Teslarati — https://www.teslarati.com/new-drone-video-shows-teslas-optimus-factory-reaching-a-turning-point/

## AMD — alta de preços de cerca de 10% no quarto trimestre
- A AMD avisou parceiros em 17 de setembro para esperarem aumento de preço de cerca de 10% a partir do quarto trimestre de 2026.
- O aumento vale para aceleradores de IA, GPUs Radeon e chipsets de placas-mãe.
- A empresa citou o aumento dos custos de wafers da TSMC.
- As CPUs Ryzen ficaram de fora da lista.
- A TSMC notificou clientes de um aumento de cerca de 10% nas cotações de fundição de wafers, citando custos de manufatura em alta persistente.
- A Intel aumentou separadamente os preços de chips selecionados para clientes e servidores.
- O Core Ultra 7 270K Plus subiu US$50, para cerca de US$349.
- O Core Ultra 5 250K Plus subiu US$30, para cerca de US$229.
- Alguns modelos Xeon ficaram centenas de dólares ou mais de US$1.000 mais caros.
- No mesmo dia, o provedor de nuvem Nebius elevou em 25% as tarifas de aluguel de CPUs AMD EPYC Genoa.
- Os preços de contrato de DRAM já subiram de 13% a 18% na comparação trimestral no terceiro trimestre de 2026, ampliando a pressão de custos sobre PCs e servidores.
- A AMD não havia emitido resposta oficial aos relatos de aumento de preços até a publicação.
**Fontes:**
- [S52] Startup Fortune — https://startupfortune.com/amd-warns-partners-of-a-10-price-hike-on-ai-chips-sparing-ryzen/
- [S53] BigGo Finance — https://finance.biggo.com/news/b5465dd8-6785-4d16-918a-e8f657586ae0
- [S54] TechNetBooks — https://www.technetbooks.com/2026/09/amd-reportedly-prepares-10-price.html

## EUA e Arábia Saudita — venda de 48 caças F-35
- O Departamento de Estado dos EUA informou na quinta-feira, 17 de setembro, que aprovou a venda de 48 caças furtivos F-35 à Arábia Saudita, por US$24,3 bilhões.
- É a maior compra de armamento do reino desde o início da guerra com o Irã.
- O Departamento de Estado notificou o Congresso sobre a venda proposta, que ainda precisa de aprovação dos parlamentares.
- Não foi dado prazo para a entrega dos caças.
- Israel, atualmente o único país do Oriente Médio a operar o F-35, manifestou preocupação com a venda a Riade, apesar do esforço de normalização das relações com o reino.
- O acordo dos caças vem depois de uma venda de US$5 bilhões de mais de 10 mil bombas aprovada no começo de setembro, incluindo armas altamente destrutivas de 2.000 libras.
- Washington também aprovou neste mês a venda de 60 motores de tanque e equipamentos relacionados por US$750 milhões.
- Em julho houve ainda um acordo de US$1,96 bilhão para kits de guiagem de precisão.
- A Arábia Saudita troca ataques simultaneamente com os houthis do Iêmen.
- Aviões sauditas atingiram na quinta-feira a província de Hajjah, perto da fronteira saudita junto ao mar Vermelho, e a região de Taiz, mais ao sul.
- Riade disse que destroços de um drone de um ataque houthi interceptado mataram uma pessoa.
**Fontes:**
- [S55] France 24 — https://www.france24.com/en/middle-east/20260918-us-approves-24-3-billion-sale-of-48-f-35-warplanes-to-saudi-arabia
- [S56] Al-Monitor (Reuters) — https://www.al-monitor.com/originals/2026/09/saudis-and-houthis-exchange-strikes-yemenis-take-boats-flee-middle-east-war

## Estreito de Ormuz — diesel dos EUA em recorde histórico
- O preço médio do diesel no varejo dos EUA bateu recorde histórico na quinta-feira, 17 de setembro, pouco abaixo de US$6,40 o galão.
- Os preços globais do petróleo bruto recuaram ligeiramente na quinta-feira, mas seguem bem acima de US$100 o barril, após dispararem ao maior nível desde maio.
- Mohammad-Bagher Zolghadr, assessor político do líder supremo do Irã, disse em 17 de setembro que o Irã manterá o Estreito de Ormuz fechado até a queda de Trump e Netanyahu.
- "Nossos combatentes não abrirão o Estreito de Ormuz até que o criminoso Trump e o sanguinário Netanyahu sejam derrubados do poder", disse Zolghadr, descrevendo o fechamento como a primeira etapa da retaliação iraniana.
- Apenas três navios de carga de commodities cruzaram Ormuz na quarta-feira, contra 12 no dia anterior.
- A média dos últimos 10 dias é de cerca de 17 navios, segundo dados preliminares de rastreamento marítimo.
- O Oleoduto Leste-Oeste da Arábia Saudita, principal rota alternativa para o petróleo do Golfo, está fechado desde que foi atingido na semana passada.
- Riade atribuiu o ataque a milícias sediadas no Iraque.
- Centenas de milhares de iranianos lotaram o centro de Teerã em 18 de setembro, na maior demonstração de desafio orquestrada pelo Estado desde o início da guerra.
- Os manifestantes prometeram pegar em armas enquanto a guerra com Estados Unidos e Israel se arrasta.
- A Guarda Revolucionária disse ter atingido mais um petroleiro no Estreito de Ormuz, sufocando ainda mais os fluxos globais de energia.
- Trump disse em 16 e 17 de setembro que esperava que a guerra estivesse perto do fim: "Bem, esperançosamente estamos perto do fim da guerra. O Irã quer muito fazer um acordo. Vamos ver como isso se resolve."
- Trump deve se reunir com líderes ou chanceleres dos seis países do Golfo Pérsico à margem da Assembleia Geral da ONU, em Nova York, na próxima terça-feira.
**Fontes:**
- [S57] Al-Monitor (Reuters) — https://www.al-monitor.com/originals/2026/09/saudis-and-houthis-exchange-strikes-yemenis-take-boats-flee-middle-east-war
- [S58] Iran International — https://www.iranintl.com/en/202609171217
- [S59] Los Angeles Times (AP) — https://www.latimes.com/world-nation/story/2026-09-18/iranians-rally-by-hundreds-of-thousands-in-biggest-show-of-defiance-since-war-began

## Rússia — eleição da Duma sob barragem de drones
- A votação começou na sexta-feira, 18 de setembro, numa eleição parlamentar russa de três dias para os 450 assentos da Duma Estatal.
- É a primeira eleição parlamentar desde a invasão em larga escala da Ucrânia, em fevereiro de 2022.
- O presidente Vladimir Putin apresentou a eleição como um termômetro do apoio à guerra na Ucrânia.
- A maioria dos candidatos contrários à guerra foi excluída das urnas.
- A exclusão veio depois que a Suprema Corte decidiu que o partido liberal Yabloko, que defende um cessar-fogo, violou regras eleitorais.
- Mais de 350 drones ucranianos miraram a capital russa na manhã de sexta-feira.
- O prefeito de Moscou, Sergei Sobyanin, disse que a maior parte dos drones foi destruída num perímetro defensivo externo e que 64 foram abatidos ao se aproximarem da cidade.
- A votação vai até as 18h GMT de domingo.
- Moscou também organizou votação em partes ocupadas da Ucrânia.
- O Ministério da Defesa da Rússia disse na sexta-feira ter atingido um centro logístico da empresa postal ucraniana Nova Poshta perto de Odesa.
- As forças russas também atingiram um navio de carga no porto de Chornomorsk.
- Um ataque russo com drones feriu cinco pessoas, incluindo três crianças, na região de Kiev na manhã de sexta-feira.
- As conversas de paz mediadas pelos EUA estão travadas na questão territorial.
- Zelensky disse que os negociadores discutem uma retirada ucraniana da região de Donetsk em troca de as forças russas não entrarem no território.
- Os americanos sugeriram um formato conjunto para administrar a usina nuclear ocupada de Zaporíjia, e os negociadores discutem como isso funcionaria.
**Fontes:**
- [S60] Reuters — https://www.reuters.com/world/europe/voting-begins-russian-parliamentary-election-which-putin-has-cast-barometer-2026-09-18/
- [S61] Al Jazeera — https://www.aljazeera.com/news/2026/9/18/ukraine-fires-drone-barrage-as-russia-launches-elections
- [S62] Associated Press — https://infonews.ca/news/7459887/zelenskyy-says-us-led-peace-talks-wrestling-with-russian-demands-for-ukrainian-territory/

## OFAC — sanções à corretora iraniana BitBank
- Em 17 de setembro, o OFAC (Escritório de Controle de Ativos Estrangeiros do Tesouro dos EUA) designou a BitBank, corretora iraniana de ativos digitais controlada pelo financista sancionado Babak Zanjani.
- As designações incluem também a desenvolvedora da BitBank, a Pishtaz Simorgh Electronic Trade Company, e três associados de Zanjani.
- O Tesouro afirmou que, entre junho e julho deste ano, Zanjani usou a BitBank para transferir centenas de milhões de dólares em bitcoin à Guarda Revolucionária Islâmica (IRGC).
- Desde junho, a sancionada Hormuz Safe Marine Services Authority — órgão que Teerã usa para vender passagem segura a navios pelo Estreito de Ormuz — usa a BitBank para repassar os pagamentos recebidos ao regime iraniano.
- O secretário do Tesouro, Scott Bessent, disse que os esforços de financiar o Irã com criptomoedas "não estão fora do alcance do OFAC".
- A ação se dá sob a "Operação Economic Outcast", lançada por Bessent em 24 de agosto como continuação da campanha anterior "Economic Fury".
- Sob essas campanhas, o OFAC sancionou em junho a Nobitex, maior corretora cripto do Irã, além de Wallex, Bitpin e Ramzinex.
- Em agosto, o OFAC atingiu a Shelbit e a Aban Tether.
- A plataforma marítima de Ormuz liquidada em bitcoin apareceu pela primeira vez na imprensa iraniana em maio, quando Teerã disse mirar mais de US$10 bilhões em receita.
- A Reuters informou que a corretora é acusada de processar pagamentos para que navios cruzassem com segurança o Estreito de Ormuz.
- A ação faz parte da campanha do Tesouro para isolar economicamente o Irã.
**Fontes:**
- [S63] U.S. Department of the Treasury — https://home.treasury.gov/news/press-releases/sb0632
- [S64] Reuters — https://www.reuters.com/world/middle-east/us-sanctions-iranian-financiers-crypto-exchange-says-it-processes-hormuz-2026-09-17/
- [S65] The Block — https://www.theblock.co/news/regulation/2026-09-17-us-sanctions-iranian-crypto-exchange-bitbank-alleged-bitcoin-transfers-to-irgc-415462

## FDA — aprovação do Fayuvi para a síndrome de Sanfilippo tipo A
- Em 17 de setembro, a FDA (agência reguladora de medicamentos dos EUA) aprovou o Fayuvi (rebisufligene etisparvovec-hopf).
- É o primeiro tratamento para pacientes pediátricos com mucopolissacaridose tipo IIIA (MPS IIIA), também conhecida como síndrome de Sanfilippo tipo A.
- A doença é hereditária, fatal e destrói progressivamente o cérebro e o sistema nervoso.
- Até a aprovação, o tratamento se limitava a manejar sintomas; não havia terapia aprovada pela FDA capaz de alterar o curso da doença.
- No ensaio pivotal Transpher A, 17 pacientes tratados marcaram 23,5 pontos a mais na escala cognitiva Bayley-III do que uma coorte externa comparável de história natural, com 27 crianças não tratadas (p<0,0001).
- O acompanhamento já se estende por quase oito anos.
- O Fayuvi é a segunda terapia gênica e a sexta aprovação da FDA obtida pela Ultragenyx.
- A empresa recebeu um Priority Review Voucher (cupom de revisão prioritária) com a aprovação.
- A terapia gênica AAV9 de dose única chegou à aprovação após um percurso regulatório acidentado.
- A FDA emitiu uma carta de resposta completa (complete response letter) em julho de 2025.
- A Ultragenyx reapresentou o pedido em janeiro de 2026 com dados neurológicos e de biomarcadores de mais longo prazo.
- A terapia teve designações de medicamento órfão, fast track e terapia inovadora (breakthrough therapy).
**Fontes:**
- [S66] BioSpace / FDA — https://www.biospace.com/press-releases/fda-approves-first-gene-therapy-for-pediatric-patients-with-sanfilippo-syndrome-type-a
- [S67] Ultragenyx (via Finviz) — https://finviz.com/news/393307/ultragenyx-announces-approval-of-fayuvi-gene-therapy-the-first-ever-fda-approved-treatment-for-sanfilippo-syndrome-type-a-mps-iiia
- [S68] CGTLive — https://www.cgtlive.com/view/fda-approves-first-gene-therapy-for-sanfilippo-syndrome-type-a

## Coreia do Sul — atraso no pacote de US$350 bilhões de investimentos nos EUA
- Em coletiva de imprensa em 18 de setembro, o presidente Lee Jae-myung disse que partes do acordo de nível técnico sobre o investimento estratégico de US$350 bilhões nos EUA são difíceis de aceitar e estão sendo renegociadas.
- Lee disse que a equipe de negociação afirma que um acordo foi praticamente alcançado, mas que, ao revisar os detalhes, ele encontrou pontos com os quais tem dificuldade de concordar.
- Os pontos de impasse são a recuperação do capital investido, a distribuição de lucros e quem absorve as perdas.
- Também está em disputa a estrutura do veículo de investimento guarda-chuva (I-SPV).
- Não houve acordo final sobre projetos de investimento que não conseguem garantir rentabilidade.
- Seul adiou o anúncio previsto de seu primeiro projeto de investimento.
- O relatório à Assembleia Nacional, originalmente marcado para 17 de setembro, foi adiado para 22 de setembro.
- Lee destacou que a soma em jogo é de cerca de 500 trilhões de wons de dinheiro dos contribuintes, equivalentes aos US$350 bilhões.
- Ele disse que Seul conseguiu incluir no memorando de entendimento a expressão "racionalidade comercial", ausente dos acordos com outros países.
- Segundo Lee, nenhum acordo havia sido alcançado até as 7h30 do dia da segunda cúpula.
- Separadamente, Washington pediu que Samsung Electronics e SK Hynix ampliem instalações de produção de memória nos EUA com capital próprio, fora do fundo governamental.
**Fontes:**
- [S69] Edaily — https://en.edaily.co.kr/news/eda202609185379/

## Argentina — projeto de lei de Milei sobre as Malvinas
- O governo da Argentina enviou ao Congresso um projeto de Lei de Defesa da Soberania Nacional na quinta-feira, 17 de setembro.
- O presidente Javier Milei apresentou o projeto como "um marco no processo de recuperação" das Malvinas.
- O projeto substitui a Lei 26.659, em vigor desde 2011, e amplia seu alcance.
- A punição deixa de se aplicar apenas a hidrocarbonetos e passa a cobrir qualquer recurso natural, renovável ou não, da plataforma continental argentina.
- Empresas barradas correriam o risco de não poder operar em nenhuma parte do país.
- O projeto cria um Conselho de Segurança Nacional presidido por Milei, com poder de ordenar "medidas urgentes" diante de ameaça grave e iminente.
- Essas medidas incluem restringir operações cambiais e financeiras, congelar temporariamente fundos e ativos, suspender autorizações ou contratos e restringir o comércio exterior.
- O projeto permite que as Forças Armadas protejam instalações estratégicas.
- O elemento mais contestado é um registro público de pessoas vinculadas ao terrorismo (RePET), operado pela Unidade de Informação Financeira.
- A inclusão no registro não depende da existência de um processo criminal: bastam "motivos razoáveis de suspeita" de vínculo com terrorismo, ou uma designação do Conselho de Segurança da ONU.
- A inclusão aciona imediatamente o congelamento de fundos e ativos.
- Horas antes de o projeto chegar ao Congresso, a juíza federal Mariel Borruto, de Río Grande, na Terra do Fogo, concedeu uma liminar por razões ambientais.
- A decisão ordenou que Rockhopper Exploration e Navitas Petroleum Development and Production se abstenham de iniciar ou continuar trabalhos no projeto Sea Lion, que prevê 23 poços.
- Milei disse que a estratégia sobre as Malvinas estava em preparação havia três anos.
- Segundo ele, o gatilho foi um comentário de Donald Trump sobre rever a posição de neutralidade dos EUA na disputa.
- Milei rejeitou a acusação de oportunismo eleitoral antes da votação de 2027: "Analistas políticos dizem que empurramos as Malvinas por razões de imagem e oportunismo político. Isso é uma estupidez enorme."
**Fontes:**
- [S70] MercoPress — https://en.mercopress.com/2026/09/18/milei-sends-congress-his-falklands-sovereignty-bill-with-an-anti-terrorism-registry-attached
