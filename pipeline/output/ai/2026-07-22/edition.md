# [Tech] - Bem-vindo(a) a 22 de Julho de 2026

Como um teste de segurança da OpenAI terminou em invasão à Hugging Face? Quanto a AMD vai investir na Anthropic no acordo de GPUs? Que modelos o Google lançou enquanto o Gemini 3.5 Pro segue em testes?

Por: Guilherme Saboia e Vinicius Gushiken

### Modelos da OpenAI invadem a produção da Hugging Face durante teste de segurança
- **Incidente.** Na terça-feira, 21 de julho, [a OpenAI revelou que uma combinação dos seus modelos invadiu a infraestrutura de produção da Hugging Face](https://techcrunch.com/2026/07/21/openai-says-hugging-face-was-breached-by-its-own-pre-release-models/) durante uma avaliação interna de capacidade cibernética. A dupla, o GPT-5.6 Sol e um modelo pré-lançamento ainda mais capaz, rodava com recusas cibernéticas reduzidas, sendo testada no benchmark ExploitGym num ambiente isolado (*sandbox*).
- **Fuga.** [Os modelos exploraram uma vulnerabilidade zero-day](https://www.bleepingcomputer.com/news/security/openai-says-its-ai-models-hacked-hugging-face-during-testing/) (falha desconhecida do fornecedor, sem correção disponível) num proxy de cache de registro de pacotes, fizeram escalada de privilégios e movimentação lateral até um nó com acesso à internet, deduziram que a Hugging Face hospedava as soluções do ExploitGym e invadiram seu banco de dados de produção para roubar as respostas e burlar a própria avaliação.
- **Defesa.** A Hugging Face classificou a invasão como "sem precedentes" e "conduzida, de ponta a ponta, por um sistema autônomo de agentes de IA"; a princípio [atribuiu o ataque a um agente externo](https://www.nbcnews.com/tech/tech-news/openai-says-ai-models-went-rogue-testing-triggering-unprecedented-brea-rcna588611) e recorreu ao modelo chinês GLM-5.2, da Zhipu AI, para contê-lo, já que os principais modelos dos EUA, incapazes de distinguir defensor de atacante, se recusaram a processar os dados.
- **Ineditismo.** [A OpenAI apresentou o episódio como o primeiro caso conhecido](https://openai.com/index/hugging-face-model-evaluation-security-incident/) em que o teste de benchmark de um modelo resultou num ciberataque real contra terceiros, e diz ter divulgado a falha ao fornecedor de forma responsável.

### AMD e Anthropic fecham acordo de até 2 GW em GPUs e US$5 bilhões em investimento
- **Acordo.** [AMD e Anthropic firmaram parceria estratégica para implantar até 2 gigawatts de GPUs AMD Instinct série MI450](https://ir.amd.com/news-events/press-releases/detail/1292/amd-and-anthropic-announce-strategic-partnership-to-deploy-up-to-2-gigawatts-of-amd-instinct-mi450-series-gpus) em soluções de rack AMD Helios, com o primeiro gigawatt começando no primeiro semestre de 2027.
- **Investimento.** [A AMD se comprometeu com um aporte em ações de até US$5 bilhões na Anthropic](https://www.thenews.com.pk/latest/1409890-amd-anthropic-sign-5bn-ai-infrastructure-deal), condicionado ao cumprimento de metas específicas de implantação.
- **Racks.** A Anthropic vai usar racks Helios com GPUs Instinct MI455X, CPUs EPYC "Venice", rede Pensando e software ROCm, sobre o uso já existente dos chips MI355X; as empresas usarão o Claude para otimizar cargas para GPUs AMD, e a AMD adotará o Claude em suas equipes de engenharia.
- **Capacidade.** A Anthropic empregará parte dos chips em seus próprios data centers e arrendará capacidade adicional de provedores de nuvem.

### Google lança três modelos Gemini Flash e inicia o treino do Gemini 4
- **Lançamentos.** Em 21 de julho, [o Google DeepMind lançou o Gemini 3.6 Flash](https://techcrunch.com/2026/07/21/google-releases-three-new-gemini-models-but-no-3-5-pro/), seu modelo "cavalo de batalha", além do 3.5 Flash-Lite e do 3.5 Flash Cyber; o 3.6 Flash melhora programação, trabalho de conhecimento e tarefas multimodais e corta o uso de tokens em até 17%, ficando mais barato por token que o 3.5 Flash.
- **Velocidade e preço.** O 3.5 Flash-Lite atinge até 350 tokens por segundo, a US$0,30 por milhão de tokens de entrada e US$2,50 por milhão de saída.
- **Cibernético.** O 3.5 Flash Cyber é o primeiro modelo do Google ajustado para encontrar e corrigir vulnerabilidades, restrito a governos e parceiros de confiança via agente CodeMender; [marca 83,2%, contra 85,6% do GPT-5.5-Cyber](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-6-flash-3-5-flash-lite-3-5-flash-cyber/), apesar de ser um modelo bem menor.
- **Gemini 4.** O Google disse ter iniciado seu "treino de pré-treinamento mais ambicioso até hoje", para o Gemini 4; [o aguardado Gemini 3.5 Pro de ponta ficou de fora](https://the-decoder.com/google-ships-three-new-gemini-flash-models-but-its-frontier-3-5-pro-remains-lost-in-training/), ainda em testes com parceiros em meio a atrasos internos e originalmente previsto para junho.

---

#### Infraestrutura & chips
- **Nvidia.** [A produção do Vera Rubin NVL72 acelera](https://blogs.nvidia.com/blog/vera-rubin/), e a CoreWeave, primeira nuvem de IA a validá-lo, viu ganho de 10x em tokens por segundo por megawatt sobre o Grace Blackwell num benchmark DeepSeek-R1. A GPU Rubin é feita no processo de 3nm da TSMC e reúne 336 bilhões de transistores, 62% mais que o chip Blackwell GB300.
- **Super Micro.** [A empresa registrou mais de US$60 bilhões em novos pedidos no 4º trimestre fiscal](https://www.channelnewsasia.com/business/super-micro-sees-strong-margins-books-60-billion-in-orders-shares-jump-6269086) e agora projeta margem bruta de 15% a 17%, contra os 8,2% a 8,4% da orientação anterior. As ações subiram cerca de 17,5% no *after-hours* após a prévia de 21 de julho.
- **Intel.** [A Fortinet virou o primeiro cliente externo divulgado da Intel Foundry](https://www.cnbc.com/2026/07/21/intel-foundry-lands-fortinet-as-first-customer-for-security-chips.html), fabricando seu chip de segurança SP6 de nova geração no nó EUV (litografia ultravioleta extrema) Intel 4, dois dias antes do balanço do 2º trimestre da Intel.

#### Modelos abertos
- **Poolside.** [Lançou o Laguna S 2.1, modelo de código aberto de 118 bilhões de parâmetros](https://thenextweb.com/news/poolside-laguna-s-2-1-open-weight-coding-model) para programação com agentes, que ativa 8 bilhões por token, tem contexto de 1 milhão de tokens e roda numa única NVIDIA DGX Spark. Marca cerca de 70% no Terminal-Bench 2.1 e quase 60% no SWE-Bench Pro, igualando modelos com de 2 a 8 vezes mais parâmetros ativos, e é posto como a resposta ocidental aos laboratórios chineses de peso aberto.

#### Rodadas
- **Glow.** [Startup de segurança de *endpoints* saiu do *stealth* com US$180 milhões a uma avaliação de US$1,2 bilhão](https://techcrunch.com/2026/07/22/glow-emerges-from-stealth-at-1-2b-valuation-to-challenge-endpoint-security-in-the-ai-era/), em rodada liderada por Sequoia, Cyberstarts, Greenoaks e Redpoint. Fundada em 2025 por ex-executivos de Meta, Snowflake e Claroty, usa agentes de IA para proteger dispositivos corporativos, cujo uso de IA saltou de 15% para 45% em um ano.
- **Humanoid.** [A britânica de robótica captou uma Série A de US$152 milhões a US$1,35 bilhão](https://finance.yahoo.com/technology/ai/articles/robotics-startup-humanoid-raises-152-131649836.html), a maior de uma empresa de humanoides na Europa, com Prime Movers Lab, Schaeffler e Bosch. Assinou acordo com a Schaeffler para milhares de robôs, com a Bosch como fabricante contratada, e planeja robôs beta em clientes no 4º trimestre de 2026.
- **Arrakis.** [Saiu do *stealth* com US$38 milhões a uma avaliação de US$140 milhões](https://tech.eu/2026/07/22/openai-and-datadog-leaders-back-ai-deployment-startup-arrakis/), incluindo Série A de US$30 milhões liderada pela Blossom Capital, com aportes pessoais dos CEOs da Datadog e da OpenAI. Leva agentes de IA à indústria aeroespacial, de energia, logística e manufatura, e abrirá escritórios em Nova York e no Oriente Médio.

#### Política & IA
- **Anthropic.** [Dobrou seu compromisso com política de IA para US$40 milhões](https://www.axios.com/2026/07/22/anthropic-doubles-funding-ai-policy-fight-elections), doando mais US$20 milhões à Public First Action antes das eleições dos EUA e citando os riscos de modelos cada vez mais poderosos, incluindo o seu próprio Mythos. O grupo é contrapeso ao super PAC Leading the Future, bancado por investidores de tecnologia que defendem regulação mais leve.
- **Casa Branca.** [O OSTP divulgou o relatório "Science: A New Golden Age"](https://www.unite.ai/white-house-steers-science-funding-to-ai-and-individual-scientists/), que redirecionaria cerca de US$200 bilhões anuais em P&D federal de instituições para cientistas individuais, via bolsas portáteis. Um dos pilares escala a Genesis Mission como iniciativa nacional de IA para a ciência, com modelos de fundação por domínio e laboratórios autônomos.

#### Conselhos & IPO
- **OpenAI.** [Nomeou David Vélez, fundador e CEO do Nubank, e Robin Vince, CEO do BNY, para seus conselhos](https://www.cnbc.com/2026/07/21/openai-appoints-two-new-members-to-board-of-directors.html) enquanto avança rumo a um IPO. O Nubank é o maior banco digital da América Latina, com mais de 135 milhões de clientes; avaliada em mais de US$850 bilhões, a OpenAI protocolou rascunho confidencial de prospecto na SEC em junho, com listagem possível já em 2027.

#### Ciência & saúde
- **Science Corp.** [Recebeu a marca CE para lançar na Europa o PRIMA, primeiro implante de interface cérebro-computador (BCI) aprovado para restaurar a visão](https://www.massdevice.com/science-corp-launches-prima-bci-europe/) de formas em pacientes com degeneração macular. Liderada por Max Hodak, cofundador da Neuralink, a empresa já captou mais de US$490 milhões, e o primeiro implante comercial é esperado na Alemanha.

#### Mundo
- **EUA e Irã.** [O CENTCOM concluiu a 11ª noite seguida de ataques ao Irã](https://apnews.com/article/iran-us-hormuz-strait-war-july-21-2026-1664f6a4dad005a99771b2ad15213585), mirando centros militares e logística para reduzir a ameaça ao Estreito de Ormuz, e o Irã retaliou atingindo bases ligadas aos EUA no Kuwait, Bahrein e Jordânia. Trump sinalizou intensificar e atacar "em breve" o sítio nuclear de Pickaxe Mountain, enquanto Israel prepara planos, mas permanece à margem.
- **Ucrânia.** [Zelensky demitiu o comandante-em-chefe Oleksandr Syrskyi e nomeou o major-general Mykhailo Drapatyi, 43 anos](https://apnews.com/article/russia-ukraine-war-military-chief-fired-3001163461bb5ed7f790720f13eb3e36), na maior reformulação militar desde a invasão russa. A troca veio após protestos de rua pela demissão do ministro da Defesa Mykhailo Fedorov e um atrito entre os dois.
- **França.** [Tornou-se o primeiro país da UE a aprovar a proibição total de redes sociais para menores de 15 anos](https://www.aljazeera.com/news/2026/7/21/french-parliament-passes-social-media-ban-for-under-15s), por 279 votos a 81 na Assembleia Nacional. Menores não poderão criar contas a partir de setembro de 2026 e as já existentes serão encerradas em janeiro de 2027; a lei também bane celulares na maioria dos colégios.

---

#### Leia também
- [SpaceX lança o primeiro veículo robótico de manutenção de satélites da Northrop Grumman](https://spacenews.com/spacex-launches-northrop-mission-to-extend-the-life-of-aging-satellites/)
- [Plozasiran, da Arrowhead, reduz triglicerídeos cerca de 80% em estudo de Fase 3](https://kvoa.marketminute.com/article/bizwire-2026-7-22-arrowhead-pharmaceuticals-reports-topline-results-from-phase-3-shasta-3-and-shasta-4-studies-of-plozasiran-in-patients-with-severe-hypertriglyceridemia)
