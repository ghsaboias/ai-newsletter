# Fatos — Newsletter [Tech] 23 de Outubro de 2026

## OpenAI — rodada de até US$30 bilhões a US$1,25 trilhão
- A OpenAI está perto de fechar uma rodada de captação de até US$30 bilhões.
- O valuation pre-money da rodada é de US$1,25 trilhão.
- A rodada é liderada por investidores dos Emirados Árabes Unidos e pela Coatue.
- A captação é apresentada como uma ponte "oportunista" antes de um possível IPO (oferta pública inicial de ações).
- Na quinta-feira (22 de outubro), a OpenAI disse aos investidores que pretende obter as assinaturas até o fim da próxima semana.
- O tamanho final da rodada ainda está sendo definido.
- A meta de valuation foi reduzida em US$150 bilhões em relação ao US$1,4 trilhão discutido antes nas negociações.
- Segundo o Financial Times, a demanda foi mais fraca que nas rodadas anteriores.
- Segundo o Financial Times, alguns investidores tiveram "indigestão" após aportes pesados em captações anteriores.
- Em paralelo à captação, a OpenAI negocia um acordo comercial para obter mais capacidade computacional dos Emirados Árabes Unidos.
- A OpenAI disse aos investidores, em fevereiro, que mira um gasto total de cerca de US$600 bilhões em poder computacional até 2030.
- A rodada anterior da OpenAI, em março, a avaliou em US$852 bilhões post-money.
- A OpenAI protocolou documentos confidenciais para um IPO em junho.
**Fontes:**
- [S1] CNBC — https://www.cnbc.com/2026/10/22/openai-funding-round-uae-investors.html
- [S2] Bloomberg — https://www.bloomberg.com/news/articles/2026-10-22/openai-shifts-value-to-1-25-trillion-as-funding-talks-finalize
- [S3] TechCrunch — https://techcrunch.com/2026/10/22/openai-working-on-new-30b-raise-at-1-25t-valuation-ahead-of-ipo/
- [S4] The Decoder — https://the-decoder.com/openai-lowers-valuation-target-raises-up-to-30-billion/
- [S5] Financial Times — https://www.ft.com/content/bb564eb1-79d4-4694-aa24-1155202a9abc

## METR e Redwood Research — falhas no monitoramento de agentes da OpenAI
- METR e Redwood Research divulgaram em 22 de outubro um teste de estresse do sistema interno da OpenAI de monitoramento de desalinhamento de agentes de IA.
- Um funcionário de cada organização conduziu o exercício presencialmente, de 21 de julho a 11 de agosto.
- Os avaliadores tiveram acesso a código interno, prompts do monitor e documentação.
- O trabalho foi feito em dispositivos fornecidos pela OpenAI, que nunca saíram das instalações da empresa.
- Os avaliadores estimaram que só cerca de 75% a 94% do tráfego agêntico interno da Responses API vindo de modelos ao menos tão fortes quanto o GPT-5.5 era elegível para monitoramento.
- No início do exercício, as execuções de treinamento por RL (aprendizado por reforço) não eram cobertas pelo monitoramento.
- Os avaliadores encontraram uma brecha que permitiria a agentes impedir o monitoramento de centenas de ações recentes; os detalhes foram censurados pela OpenAI.
- Encontraram também uma forma de agentes do Codex contornarem o sandbox e o Auto-Review.
- Encontraram ainda dois cabeçalhos controláveis pelo cliente que desativam o monitoramento para novos agentes.
- O monitor só era acionado quando o agente devolvia o controle ao usuário.
- Com isso, agentes podiam adiar indefinidamente o monitoramento continuando a agir.
- Eventos de compactação não eram monitorados.
- Cerca de 10% do tráfego interno elegível do Codex ficou sem monitoramento entre maio e julho de 2026.
- A OpenAI recebeu um relatório interno de 61 páginas.
- Os avaliadores concordaram em publicar apenas um resumo de alto nível.
- A OpenAI diz ter corrigido todas as vulnerabilidades que afetavam as proteções em produção.
- METR e Redwood não verificaram essas correções.
- A OpenAI disse que as conclusões "ajudaram a fortalecer as proteções à medida que expandimos o sistema e vão ajudar a moldar futuras colaborações de pesquisa com o METR e outros avaliadores externos".
**Fontes:**
- [S6] Redwood Research — https://blog.redwoodresearch.org/p/red-teaming-openais-internal-agent
- [S7] CNBC — https://www.cnbc.com/2026/10/22/metr-redwood-research-open-ai-test.html
- [S8] Reuters (via Yahoo Tech) — https://tech.yahoo.com/ai/chatgpt/articles/ai-safety-group-metr-finds-160243600.html
- [S9] The Verge — https://www.theverge.com/ai-artificial-intelligence/1017179/openais-misalignment-monitoring-system-had-a-number-of-novel-vulnerabilities-third-party-evaluators-found

## Anthropic e Theorem — verificação formal de 123 bibliotecas com Claude
- O Frontier Red Team da Anthropic, com a startup Theorem, usou o Claude para provar propriedades de segurança em mais de 100 bibliotecas reais de código aberto.
- As provas foram feitas no nível de código assembly RISC-V (arquitetura aberta de processador).
- A Anthropic chama o trabalho de primeiro esforço em larga escala de usar IA para aplicar verificação formal (prova matemática de propriedades de um programa) a software de produção no nível de assembly.
- Em poucas semanas, o Claude corrigiu os bugs que encontrou e provou que não há falhas (crashes) para nenhuma entrada de até 64 MB.
- As provas cobrem 239 pontos de entrada em 123 bibliotecas do OSS-Fuzz.
- As provas somam cerca de 180 milhões de linhas em Rocq (assistente de provas formais).
- Uma prova típica tem cerca de 600 mil linhas.
- Ao escrever as provas, o Claude encontrou bugs que passaram despercebidos por anos, apesar de trilhões de execuções de teste.
- Entre eles, o Claude redescobriu a CVE-2026-56132 (identificador público de vulnerabilidade) na libexpat.
- Em 36 pequenas tarefas de verificação montadas a partir de código do OSS-Fuzz, o Opus 5.5 prova metade com cerca de 40% menos tokens que o Opus 5.
- A Theorem publicou no GitHub 60 das provas, cobrindo 25 bibliotecas, entre elas OpenSSL, mbedtls e zstd.
- A Theorem lançou o OSS Verify, serviço gratuito de verificação para projetos de código aberto que se qualificarem.
- A Anthropic ressalva que "formalmente verificado" não significa "livre de bugs".
- As provas pressupõem um binário estático de thread única, com orçamento fixo de memória, rodando em CPU RISC-V com Linux.
**Fontes:**
- [S10] Anthropic — https://www.anthropic.com/research/formal-verification
- [S11] CellCog — https://cellcog.ai/blog/anthropic-formal-verification/
- [S12] MACCUS — https://maccus.fr/en/claude-formal-verification/

## Anthropic — doação do Agent Skills à Agentic AI Foundation
- A Anthropic doou o Agent Skills, padrão aberto que dá a agentes de IA conhecimento e fluxos de trabalho especializados, à Agentic AI Foundation (AAIF).
- A AAIF fica sob a Linux Foundation.
- A Anthropic cofundou a AAIF com Block e OpenAI no ano passado.
- A Anthropic já havia doado à AAIF o MCP (Model Context Protocol, padrão para conectar modelos a ferramentas e dados).
- Mais de 70 plataformas de agentes integraram o Agent Skills, entre elas ChatGPT, Cursor, GitHub Copilot e VS Code.
- Já foram publicadas 1 milhão de skills.
- Quase 280 milhões de skills foram instaladas.
- Engenheiros de Anthropic, Google, OpenAI e outras empresas vão manter o padrão como indivíduos.
- David Soria Parra e Mahesh Murag são os mantenedores principais.
- O primeiro roadmap prevê versões numeradas, um processo formal de propostas e orientações de segurança.
- A AAIF anunciou no mesmo dia quatro novos projetos: Agent Skills (Anthropic), Open Responses (OpenAI), OpenEnv (Hugging Face) e OpenSandbox (Alibaba).
- Com eles, a AAIF passou de 3 para 10 projetos hospedados em seu primeiro ano.
**Fontes:**
- [S13] Anthropic — https://www.anthropic.com/news/donating-agent-skills-to-the-agentic-ai-foundation
- [S14] Linux Foundation — https://www.linuxfoundation.org/press/agentic-ai-foundation-announces-four-new-projects-agent-skills-open-responses-openenv-and-opensandbox

## Microsoft — MAI-DxO e diagnóstico médico na Science
- A Microsoft publicou na revista Science um estudo sobre seu AI Diagnostic Orchestrator (MAI-DxO).
- O MAI-DxO funciona como um painel de médicos virtuais que propõem diagnósticos, escolhem perguntas e exames e debatem ao longo de várias rodadas.
- Em casos complexos do NEJM (New England Journal of Medicine), o MAI-DxO atingiu 83% de acurácia diagnóstica.
- Nos mesmos casos, médicos acertaram 22% sem material de referência e 36% com ele.
- Em casos de pronto-socorro da base MIMIC-IV-ED, o MAI-DxO atingiu 80% de acurácia, contra 47% dos médicos.
- A comparação foi feita com médicos generalistas, em um benchmark só de texto.
- Os autores escrevem que as comparações "não estabelecem superioridade sobre especialistas, equipes multidisciplinares ou a prática clínica real".
- Todos os autores do estudo são funcionários da Microsoft com participação acionária na empresa.
- Aplicado ao GPT-5.5, o orquestrador elevou a acurácia em casos complexos de 72% para quase 87%, a um custo um pouco menor.
- Em casos de pronto-socorro, o ganho foi pequeno: cerca de 85% com e sem o orquestrador.
- A Microsoft fará uma avaliação prospectiva no mundo real com o Beth Israel Deaconess Medical Center, em Boston.
- A Microsoft vai abrir o código do SDBench para casos selecionados do NEJM.
- Mustafa Suleyman disse que a Microsoft trabalha com a Mayo Clinic no treinamento de um modelo fundacional para saúde.
- O lançamento desse modelo está previsto para o ano que vem.
**Fontes:**
- [S15] Microsoft AI — https://microsoft.ai/news/building-medical-superintelligence/
- [S16] TechCrunch — https://techcrunch.com/2026/10/22/microsofts-mustafa-suleyman-says-its-ai-outperforms-doctors-on-hard-cases-as-he-chases-medical-superintelligence/
- [S17] The Verge — https://www.theverge.com/ai-artificial-intelligence/1016690/suleyman-microsoft-diagnostic-orchestrator-science-medical-superintelligence
- [S18] Becker's Hospital Review — https://www.beckershospitalreview.com/healthcare-information-technology/digital-health/microsoft-ai-diagnostic-tool-tops-generalist-physicians-83-to-36/

## Warp Sciences — startup de Kevin Weil estreia com US$215 milhões
- A Warp Sciences saiu do stealth com US$215 milhões em financiamento.
- A empresa vai montar nos EUA uma CRO (organização de pesquisa sob contrato) de química.
- A proposta combina químicos, IA e robótica para produzir e testar moléculas para descoberta de medicamentos.
- O aporte é uma Série A liderada pela Lightspeed.
- A rodada avalia a Warp em US$865 milhões post-money.
- IVP, Premji Invest e Lux Capital também investiram.
- O CEO e cofundador é Kevin Weil, ex-CPO (diretor de produto) e ex-VP de Ciência da OpenAI.
- Outro cofundador é Manohar Paluri, cofundador do FAIR (laboratório de pesquisa em IA da Meta) e ex-VP do Meta Superintelligence Labs.
- DJ Patil, ex-cientista-chefe de dados do governo dos EUA, é cofundador.
- O químico medicinal Sol Reisberg é cofundador.
- Weil disse que a IA acelerou a engenharia de software e a matemática, mas ainda não as ciências físicas.
- Weil disse que, para construir IA mais capaz para a ciência, é preciso gerar dados experimentais do mundo real em escala.
- Weil anunciou a empresa no X, dizendo que o objetivo é "tirar a IA de fronteira do navegador e levá-la ao laboratório".
**Fontes:**
- [S19] Business Wire — https://www.businesswire.com/news/home/20261022200104/en/Warp-Sciences-Emerges-From-Stealth-With-%24215-Million-to-Build-U.S.-Chemistry-Services-for-Drug-Research
- [S20] Bloomberg Law — https://news.bloomberglaw.com/pharma-and-life-sciences/ex-openai-science-head-launches-startup-with-215-million
- [S21] TechCrunch — https://techcrunch.com/2026/10/22/former-openai-science-lead-launches-warp-science-to-automate-wet-labs-with-robots/
- [S22] X (@kevinweil) — https://threadreaderapp.com/thread/2113294657673466060

## DeepSeek e MiniMax — registro sob as regras chinesas de exportação de IA
- A conta Yuyuan Tantian, ligada à emissora estatal CCTV, disse na noite de 22 de outubro que DeepSeek e MiniMax concluíram o registro exigido pelas novas regras.
- As duas empresas também concluíram os procedimentos para abrir o código e autorizar o uso de seus modelos no exterior.
- O registro vem após a proposta preliminar de Pequim, de 16 de outubro, de incluir 23 tecnologias ligadas a IA em seu catálogo de restrições de exportação.
- A lista inclui grandes modelos de linguagem, agentes de IA e clusters de computação.
- A exigência de registro entrou em vigor imediatamente.
- Oferecer acesso por API, apps web ou software como serviço baseados em modelos restritos fica isento das restrições de exportação.
- A implantação local de um modelo restrito no exterior fica sujeita ao controle de exportação.
- A publicação estatal disse que "as empresas de IA podem continuar seus esforços de comercialização normalmente".
- Segundo a publicação, o catálogo busca "definir limites em vez de simplesmente restringir a exportação de tecnologia de IA".
- A MiniMax criou uma via de solicitação para regiões excluídas por sua licença anterior, incluindo EUA, União Europeia, Reino Unido e Coreia do Sul.
- Nessas regiões, a implantação local exige revisão de conformidade e licença.
- O período de consulta pública sobre o catálogo preliminar vai de 16 de outubro a 15 de novembro de 2026.
**Fontes:**
- [S23] South China Morning Post — https://www.scmp.com/tech/policy/article/3371880/deepseek-minimax-secure-open-source-licenses-days-after-new-china-export-rules-state-media
- [S24] The Business Times (Bloomberg) — https://www.businesstimes.com.sg/international/deepseek-minimax-win-approval-deploy-models-overseas-state-media-says
- [S25] AI Affairs — https://www.aiaffairs.com/government/deepseek-minimax-china-draft-ai-export-registration/
- [S26] EL7.AI — https://el7.ai/en/news/2026-10-23-deepseek-and-minimax-gain-chinese-approval-for-global-ai-deployment
- [S27] Reuters (via Investing.com) — https://www.investing.com/news/stock-market-news/chinas-deepseekminimax-win-approval-for-ai-global-use-state-mediaaffiliated-entity-says-4968133

## SK Hynix — suspensão do IPO da Solidigm nos EUA
- Na sexta-feira, 23 de outubro de 2026, a SK Hynix disse que sua subsidiária americana Solidigm suspendeu a análise de uma rodada pré-IPO e de um IPO posterior nos EUA.
- A empresa citou as condições do mercado de capitais e a trajetória do preço das ações.
- O IPO estava em estudo para ajudar a financiar uma nova fábrica da Solidigm nos EUA.
- A Solidigm é o antigo negócio de memória flash NAND e SSDs (unidades de estado sólido) da Intel.
- Pessoas a par dos planos disseram que a oferta poderia levantar US$15 bilhões.
- As mesmas fontes disseram que o IPO avaliaria a unidade em US$150 bilhões.
- A SK Hynix disse que a decisão não reflete mudança nas perspectivas de crescimento nem nas necessidades de investimento da Solidigm.
- A SK Hynix disse que as instalações atuais não dão conta da demanda crescente por memória para IA.
- A empresa disse que seguirá buscando outras formas de financiar a capacidade nos EUA.
- O governador do Financial Supervisory Service (FSS, órgão supervisor financeiro sul-coreano), Lee Chan-jin, disse nesta semana que os reguladores consideram a Solidigm sujeita às restrições sul-coreanas a listagens duplicadas.
- Essas restrições foram endurecidas em julho.
- A SK Hynix disse que as regras sobre listagem duplicada não foram o motivo direto da decisão.
- As ações da SK Hynix fecharam a sexta-feira em alta de 4,4%, depois de chegarem a cair 3% durante o pregão.
- As ações da SK Hynix caíram mais de 30% desde que o possível IPO da Solidigm foi noticiado, no fim de setembro.
- No mesmo período, o KOSPI (principal índice da bolsa sul-coreana) caiu 20%.
- Outras listagens ligadas a infraestrutura de IA também foram engavetadas.
- Entre elas, o IPO da australiana Firmus, apoiada pela Nvidia.
- Também foi engavetada a listagem em Singapura de um REIT (fundo imobiliário listado em bolsa) da AirTrunk, apoiada pela Blackstone.
**Fontes:**
- [S28] SK hynix Newsroom — https://news.skhynix.co.kr/fact-12/
- [S29] Yonhap News Agency — https://en.yna.co.kr/view/AEN20261023000900320
- [S30] Reuters (via Investing.com) — https://www.investing.com/news/stock-market-news/sk-hynix-drops-us-ipo-plan-for-solidigm-newspaper-reports-4967714
- [S31] The Korea Herald — https://www.koreaherald.com/article/10912278
- [S32] CNBC — https://www.cnbc.com/2026/10/23/sk-hynix-solidigm-ipo-.html
- [S33] CNA (Reuters) — https://www.channelnewsasia.com/business/sk-hynix-says-solidigm-suspends-review-us-ipo-citing-market-volatility-6484446

## SK Hyper — plano de 15 GW de data centers na Coreia do Sul
- A SK Hyper é a unidade de data centers de IA da SK Telecom.
- A SK Hyper negocia com big techs e investidores financeiros para financiar um plano de 15 gigawatts de capacidade de data centers na Coreia do Sul até 2035.
- A informação foi dada pelo CEO Chung Suk-geun à Bloomberg Television.
- Só a primeira fase, de 5 GW, exigiria cerca de US$350 bilhões, incluindo equipamentos.
- A SK Hyper quer garantir seu primeiro capital externo até o fim de 2026 ou o início de 2027.
- Depois disso, a empresa prevê novas captações ao longo de três a quatro anos.
- Os custos seriam divididos com inquilinos e investidores externos.
- Chung disse que o mercado sul-coreano de data centers tem hoje cerca de 1 GW.
- A fase inicial de 5 GW equivale a cerca de cinco vezes o mercado doméstico.
- A SK Hyper discute com hyperscalers (grandes provedores de nuvem) a instalação na Coreia de polos de inferência de IA que atendam também Japão e Taiwan.
- A SK Hyper desenvolve um projeto de 900 megawatts em Ulsan.
- A SK Hyper desenvolve também um data center de 100 megawatts com a AWS.
- As operações começam em fases a partir de 2029.
- A SK Telecom criou a SK Hyper em julho de 2026.
- A SK Telecom planeja investir 750 bilhões de wons (cerca de US$567 milhões) na unidade até 2030.
- Chung disse que o ritmo do investimento será ajustado à demanda real.
**Fontes:**
- [S34] The Business Times (Bloomberg) — https://www.businesstimes.com.sg/companies-markets/sk-groups-data-centre-arm-talks-fund-us350-billion-ai-buildout
- [S35] Seoul Economic Daily — https://en.sedaily.com/technology/2026/10/23/sk-hyper-seeks-350-billion-to-build-15gw-of-ai-data-centers
- [S36] Seoul Economic Daily — https://en.sedaily.com/finance/2026/10/23/sk-hyper-seeks-350-billion-to-build-ai-data-centers

## Tesouro dos EUA — regra proposta contra investimentos em tecnologia na China
- Em 22 de outubro de 2026, o Tesouro dos EUA publicou uma proposta de regra para implementar o COINS Act.
- O COINS Act foi aprovado dentro da NDAA (lei anual de autorização de gastos de defesa) do ano fiscal de 2026.
- A regra atualiza o Outbound Investment Security Program, programa que fiscaliza investimentos de americanos no exterior.
- A lei cobre cinco setores: semicondutores e microeletrônica, IA, tecnologias quânticas, computação de alto desempenho e supercomputação, e sistemas hipersônicos.
- O secretário do Tesouro, Scott Bessent, acrescentou biotecnologia à proposta, além dos setores previstos na lei.
- A proposta rebatiza os sistemas de IA como "sistemas de superinteligência".
- A proposta prevê uma proibição ampla a investimentos de americanos no desenvolvimento desses sistemas em países de preocupação, citando avanços rápidos nesses países.
- A regra valeria para investimentos acima de US$50 mil.
- Investimentos financeiros, como compra de ações, ficam de fora.
- A regra mira China, Rússia, Coreia do Norte e outros "países de preocupação".
- Comentários por escrito podem ser enviados até 7 de dezembro de 2026.
- A data de vigência será fixada nas regras finais.
- Segundo a AP, a regra amplia um programa criado por uma ordem executiva de Joe Biden de 2023.
**Fontes:**
- [S37] U.S. Department of the Treasury — https://home.treasury.gov/news/press-releases/sb0667/
- [S38] U.S. Department of the Treasury — https://home.treasury.gov/system/files/206/COINS-NPRM.pdf
- [S39] U.S. Department of the Treasury — https://home.treasury.gov/policy-issues/international/outbound-investment-program
- [S40] Associated Press — https://apnews.com/article/treasury-china-tech-investments-rule-b742c292ff8eb19e6a4c8cf03d4d66b9
- [S41] The Hill — https://thehill.com/homenews/administration/6167231-treasury-proposes-curbs-artificial-intelligence/

## Nvidia e Western Digital — memória, queda dos chips e resultado da WD
- O CEO da Nvidia, Jensen Huang, disse à CNBC em 22 de outubro, durante a GTC Berlin, que não espera excesso de oferta de memória até 2029.
- Huang disse: "Uma das coisas ótimas sobre memória é que sempre dá para usar mais."
- As ações de memória haviam caído após uma coluna sul-coreana de 15 de outubro prever um "oceano vermelho" de nova oferta em 2029.
- As ações de memória também caíram depois que a chinesa CXMT apresentou uma nova arquitetura de projeto de DRAM (memória de acesso aleatório dinâmica).
- Perguntado sobre uma parceria com a CXMT, Huang disse: "Estamos de mente aberta."
- Huang disse que as restrições americanas a chips aceleraram o esforço da China para construir sua própria fabricação de semicondutores.
- Huang disse que a demanda das neoclouds (provedoras de nuvem especializadas em IA) supera de longe o capital disponível para elas.
- Huang previu que essa questão acabará sendo resolvida.
- Em 22 de outubro, o índice de semicondutores da Filadélfia (SOX) caiu 6,72%, para 10.731,98 pontos.
- No mesmo dia, o Nasdaq caiu 2,60%.
- A queda veio depois que a Lam Research apontou restrições na cadeia de suprimentos em suas projeções.
- A Western Digital reportou receita de US$4,38 bilhões no primeiro trimestre fiscal de 2027.
- A receita subiu 55% na comparação anual.
- A margem bruta non-GAAP (fora dos princípios contábeis padrão dos EUA) foi de 58,1%.
- A Western Digital elevou o dividendo trimestral em 17%, para US$0,175 por ação.
- A Western Digital projetou receita de cerca de US$5,1 bilhões no segundo trimestre fiscal.
- A projeção representa alta de 66% a 72% na comparação anual.
- A empresa projetou margem bruta non-GAAP de 60,5% e lucro por ação non-GAAP de US$5,80 no segundo trimestre fiscal.
- O CEO da Western Digital, Irving Tan, disse que a demanda por armazenamento está se estendendo a neoclouds e laboratórios de IA de fronteira.
- Tan disse que o primeiro disco HAMR (gravação magnética assistida por calor) da empresa está no cronograma para embarques em volume no primeiro semestre de 2027.
**Fontes:**
- [S42] CNBC — https://www.cnbc.com/2026/10/22/jensen-huang-nvidia-memory-selloff-shortage.html
- [S43] Edaily — https://en.edaily.co.kr/news/eda202610235045/
- [S44] VLSI.kr — https://www.vlsi.kr/en/daily-silicon-2026-10-23-en/
- [S45] Western Digital — https://www.westerndigital.com/en-ap/company/newsroom/press-releases/2026/2026-10-22-wd-reports-fiscal-first-quarter-2027-financial-results
- [S46] Western Digital Investor Relations — https://investor.wdc.com/news-releases/news-release-details/wd-reports-fiscal-first-quarter-2027-financial-results
- [S47] The Motley Fool — https://www.fool.com/earnings/call-transcripts/2026/10/22/wdc-wdc-q1-2027-earnings-call-transcript/

## Tractian — Série D de US$130 milhões e status de unicórnio
- Em 22 de outubro de 2026, a Tractian anunciou uma Série D de US$130 milhões.
- A rodada foi liderada pela Sapphire Ventures e coliderada pela Catalyst, da M&G.
- A rodada avalia a empresa em US$1,4 bilhão.
- Também participaram N47, General Catalyst, Bosch Ventures, 53 Stations, Monashees, Endeavor Catalyst, Norte Ventures e Y Combinator.
- A Tractian fabrica seus próprios sensores de vibração, ultrassom e elétricos.
- A Tractian desenvolve modelos de IA, entre eles o JANUS, que diagnosticam falhas em máquinas.
- A empresa planeja avançar em data centers, defesa, infraestrutura de energia e Europa.
- O valuation é 94% maior que os US$800 milhões da Série C, de novembro de 2024.
- A receita anualizada passou de US$100 milhões em setembro de 2026.
- Em 2024, a receita anualizada era de US$40 milhões.
- A Tractian foi fundada em 2019 por Igor Marinelli, Gabriel Lameirinhas e Leonardo Vieira.
- A empresa é originalmente brasileira, com sede principal em Atlanta (EUA).
- A Tractian tem mais de 700 funcionários.
- A Tractian tem mais de 2.000 clientes, entre eles Eli Lilly, Whirlpool, Coca-Cola e Embraer.
- Segundo a Bloomberg Línea, a Tractian é o segundo unicórnio de IA da América Latina.
- O primeiro foi a legaltech Enter, avaliada em US$1,2 bilhão no início deste ano.
**Fontes:**
- [S48] PR Newswire — https://www.prnewswire.com/news-releases/tractians-130m-series-d-values-the-company-at-1-4b-to-scale-physical-ai-for-asset-heavy-industries-302917313.html
- [S49] Sapphire Ventures — https://sapphireventures.com/blog/sapphire-ventures-deepens-tractian-partnership-series-d/
- [S50] Bloomberg Línea — https://www.bloomberglinea.com.br/startups/tractian-capta-us-130-milhoes-e-se-torna-o-mais-novo-unicornio-de-ia-brasileiro/
- [S51] Pequenas Empresas & Grandes Negócios — https://revistapegn.globo.com/startups/noticia/2026/10/tractian-capta-us-130-milhoes-em-serie-d-e-se-torna-unicornio.ghtml

## Formic — US$50 milhões para robótica de uso geral em fábricas
- A Formic, sediada em Chicago, captou US$50 milhões em capital de crescimento em 22 de outubro de 2026.
- O financiamento inclui uma Série B liderada pela Mercato Partners.
- Light Ray Ventures, Lightscape Partners e Citi participaram da Série B.
- O pacote inclui também financiamento em dívida da S2G Investments.
- A Axios noticiou a rodada como US$50 milhões no total, em entrevista exclusiva com o CEO Saman Farid.
- A Formic aluga robôs a fabricantes por uma mensalidade única, sem investimento inicial.
- A empresa opera centenas de robôs em mais de 100 instalações, em mais de 30 estados americanos.
- A frota opera com 99,6% de disponibilidade.
- 97% dos clientes renovam o contrato.
- A Formic acumula mais de 750 mil horas de produção real.
- O dinheiro será usado para expandir da automação de tarefas específicas para a robótica de uso geral.
- A empresa também vai entrar em novas aplicações, como fabricação em metal.
- A Formic trabalha com a Physical Intelligence para adaptar os modelos fundacionais de robótica dessa empresa usando dados de manufatura da frota da Formic.
**Fontes:**
- [S52] Business Wire — https://www.businesswire.com/news/home/20261022651853/en/Formic-Raises-%2450-Million-to-Scale-Physical-AI-Across-American-Manufacturing
- [S53] Axios — https://www.axios.com/pro/all-deals/2026/10/22/formic-50m-robotics-deployments
- [S54] The AI Insider — https://theaiinsider.tech/2026/10/23/formic-raises-50m-to-expand-from-factory-automation-into-general-purpose-robotics/

## Merck e Moderna — vacina de mRNA contra melanoma na Fase 3
- No estudo de Fase 3 INTerpath-001, a vacina intismeran autogene combinada ao Keytruda reduziu em 42% o risco de recorrência ou morte em comparação com o Keytruda sozinho.
- A razão de risco (HR) foi de 0,58.
- O estudo envolveu pacientes com melanoma em estágio IIB a IV totalmente removido por cirurgia.
- O acompanhamento mediano foi de 24,6 meses.
- A combinação reduziu em 38% o risco de metástase à distância ou morte.
- A sobrevida livre de recorrência em dois anos foi de 82,2% com a combinação, contra 70,0% com o Keytruda sozinho.
- Após o regime de seis meses da vacina, uma análise de sensibilidade pré-especificada mostrou redução de 58% no risco de recorrência ou morte.
- Os dados de sobrevida global ainda não estão maduros.
- O estudo incluiu 1.137 pacientes.
- A vacina é uma terapia de mRNA que codifica até 34 neoantígenos, desenhados a partir das mutações do tumor de cada paciente.
- Os resultados serão apresentados no Simpósio Presidencial do ESMO 2026 (congresso da Sociedade Europeia de Oncologia Médica).
- Os resultados foram aceitos para publicação no New England Journal of Medicine.
- As ações da Moderna chegaram a cair 25% na quinta-feira, depois que dados parciais vazaram em um site de oncologia.
- A queda ocorreu apesar de os resultados serem positivos em relação às expectativas.
- As ações da Moderna acumulavam alta de mais de 530% no ano.
- Segundo a Reuters, a Moderna fechou em queda de mais de 17%.
- A Merck fechou em queda de cerca de 1,8%.
- As empresas disseram que estão em contato com os reguladores.
**Fontes:**
- [S55] Merck — https://www.merck.com/news/merck-and-moderna-will-present-results-from-landmark-phase-3-interpath-001-trial-for-intismeran-autogene-plus-keytruda-pembrolizumab-at-esmo-2026-presidential-symposium/
- [S56] CNBC — https://www.cnbc.com/2026/10/22/moderna-stock-cancer-vaccine-data-leak.html
- [S57] Reuters (via Investing.com) — https://www.investing.com/news/stock-market-news/merckmoderna-cancer-vaccine-cuts-melanoma-death-or-recurrence-risk-by-42-shares-fall-4967507

## Guerra com o Irã — Waltz fala em mais um ano; Brent a US$114
- O embaixador dos EUA na ONU, Mike Waltz, disse ao Financial Times que os EUA estão preparados para um conflito prolongado com o Irã.
- Waltz disse que os EUA ainda podem enfrentar um impasse daqui a um ano.
- Esse impasse seria sem acordo sobre o programa nuclear iraniano nem retorno do tráfego marítimo pelo Estreito de Ormuz aos níveis de antes da guerra.
- Waltz disse que a Marinha dos EUA pode manter o bloqueio aos portos iranianos "no futuro previsível".
- Waltz disse que os objetivos americanos exigem que o Irã se desfaça de seu urânio altamente enriquecido.
- Waltz disse que os objetivos americanos exigem também que o Irã aceite um acordo sobre enriquecimento em seu território.
- O Brent atingiu US$114 o barril na sexta-feira.
- A alta veio depois que a Guarda Revolucionária do Irã disse ter inutilizado sete petroleiros perto do Estreito de Ormuz.
- Na quinta-feira, o Brent fechou a US$113,17, alta de 4,00%.
- Foi o maior nível de fechamento do Brent desde maio.
- A Saudi Aramco disse que o fluxo pelo oleoduto Leste-Oeste, que contorna Ormuz, mais que triplicou, de 2 milhões para 7 milhões de barris por dia.
- Trump acusou o Irã, no Truth Social, de "inventar ataques falsos, minas" para elevar o preço do petróleo antes das eleições de meio de mandato de 3 de novembro.
- Um porta-voz do CENTCOM (Comando Central dos EUA) disse que as rotas marítimas foram liberadas de minas.
- Segundo o CENTCOM, 95% das embarcações conseguem passar.
- Os Emirados Árabes Unidos relataram na sexta-feira um vazamento de óleo de petroleiro que atingiu as praias de Umm Al Quwain.
- As praias de Umm Al Quwain foram fechadas.
- A guerra, que Trump inicialmente esperava durar de quatro a cinco semanas, se aproxima do nono mês.
**Fontes:**
- [S58] CBS News — https://www.cbsnews.com/live-updates/iran-war-trump-us-oil-gas-prices-strait-of-hormuz-midterms/
- [S59] Financial Times — https://www.ft.com/content/70379a26-c20e-4501-aec9-a9a0089cdd3d
- [S60] Investing.com — https://www.investing.com/news/economy-news/us-prepares-for-prolonged-iran-conflict-trump-envoy-tells-ft-4968075
- [S61] The Island (via Al Jazeera) — https://island.lk/iran-says-seven-ships-hit-in-hormuz-strait-warns-us-of-wider-response/
- [S62] The Closing Print — https://www.theclosingprint.net/2026/10/post-market-summary-2026-10-22/

## Starshield — Trump pediu a Musk liberação na Ucrânia
- O presidente Trump ligou para Elon Musk na quarta-feira e pediu que ele suspendesse as restrições impostas ao Starshield na Ucrânia, segundo autoridades americanas ouvidas pelo WSJ.
- O Starshield é a versão militar do Starlink, usada na Ucrânia.
- Musk, chefe da SpaceX, havia limitado o sistema.
- O sistema funcionava de forma mais normal na quinta-feira, logo após a conversa.
- Algumas autoridades ucranianas disseram que o sistema não voltou a funcionar plenamente.
- Trump se recusou a confirmar a ligação, mas disse: "No fim das contas, ele restabeleceu."
- Fontes do Ministério da Defesa ucraniano disseram à BBC que drones continuavam perdendo conexão a 161 km/h (100 mph).
- Segundo essas fontes, não havia confirmação de que as restrições tinham sido suspensas.
- Autoridades ucranianas disseram na manhã de sexta-feira que as restrições continuavam em vigor.
- Serhii Beskrestnov, assessor de Zelensky, disse que não havia indício de que as restrições tivessem sido suspensas.
- Segundo a CNN, Trump buscou informações sobre a lentidão e procurou Musk depois que autoridades ucranianas relataram interrupções.
**Fontes:**
- [S63] Wall Street Journal — https://www.wsj.com/world/trump-called-musk-and-asked-him-to-lift-ukraine-starlink-restrictions-5aeebc6e
- [S64] BBC — https://www.bbc.com/news/articles/cq74pjpmx0e8o
- [S65] CNN — https://www.cnn.com/2026/10/23/world/trump-musk-restored-ukraines-starshield-intl
- [S66] Associated Press — https://apnews.com/article/starlink-starshield-ukraine-russia-trump-vance-musk-1a9279f37cfd4d2a65c8ce4cc3af6f41

## Elon Musk — cerca de US$1 bilhão na Skydance
- Elon Musk investiu cerca de US$1 bilhão na Skydance, segundo pessoas a par do assunto.
- O aporte saiu junto com investimentos de outros acionistas da Skydance, entre eles a conselheira Laurene Powell Jobs.
- A Paramount concluiu a compra da Warner Bros. Discovery em 6 de outubro.
- A empresa combinada passou a se chamar Skydance.
- A Skydance é comandada pelos co-CEOs David Ellison e Ynon Kreiz.
- A Skydance projeta US$6 bilhões em cortes de custos em três anos.
- A Skydance carrega dívida de quase US$80 bilhões.
- Larry Ellison investiu US$1 bilhão na compra do Twitter por Musk, em 2022.
- Larry Ellison garantiu pessoalmente mais de US$40 bilhões do capital da oferta da Paramount pela Warner Bros. Discovery.
- A Skydance planeja demissões após a aquisição da Warner Bros. Discovery, enquanto tenta reduzir a dívida de cerca de US$80 bilhões.
**Fontes:**
- [S67] Semafor — https://www.semafor.com/article/10/22/2026/elon-musk-makes-1-billion-investment-in-ellisons-skydance
- [S68] CNBC — https://www.cnbc.com/2026/10/22/elon-musk-skydance-investment.html
- [S69] Forbes — https://www.forbes.com/sites/antoniopequenoiv/2026/10/22/musk-invests-1-billion-in-skydance-as-it-stares-down-high-debt-after-wbd-acquisition/

## Grécia — proibição de redes sociais para menores de 15 anos
- O Parlamento grego aprovou na noite de 22 de outubro uma lei que proíbe menores de 15 anos de usar redes sociais.
- A votação veio após um debate de mais de 16 horas.
- A lei entra em vigor em 1º de janeiro de 2027.
- Apenas o partido governista Nova Democracia apoiou o projeto.
- O PASOK se absteve.
- SYRIZA, Solução Grega, KKE, Niki e Rumo à Liberdade votaram contra.
- As plataformas são responsáveis pela verificação de idade.
- As plataformas estão sujeitas a multas de até 6% do faturamento global, segundo o ministro de Governança Digital e IA, Dimitris Papastergiou.
- Os pais não podem autorizar o uso.
- Contas já existentes não ficam isentas.
- A verificação de idade pode usar o app estatal Kids Wallet.
- O Kids Wallet informa às plataformas apenas se o usuário tem mais ou menos de 15 anos.
- Mais de 20 países aprovaram leis semelhantes, segundo levantamento da AFP.
- A Austrália foi o primeiro país a adotar a medida, proibindo menores de 16 anos.
**Fontes:**
- [S70] Greek Ministry of Health — https://www.moh.gov.gr/articles/ministry/grafeio-typoy/press-releases/14881-yperpshfi-sthke-apo-thn-olome-leia-ths-boylh-s-to-nomosxe-dio-gia-thn-prostasi-a-twn-anhli-kwn-sta-me-sa-koinwnikh-s-dikty-wshs
- [S71] AFP — https://www.afp.com/en/new-greece-law-bans-social-media-under-15s
- [S72] DW — https://www.dw.com/en/greece-joins-countries-putting-age-limits-on-social-media-banning-access-for-kids-under-15/a-79739606
- [S73] The Next Web — https://thenextweb.com/news/greece-passes-law-banning-social-media

## Mercados — pior dia do Nasdaq desde junho e queda forte dos juros
- O Nasdaq caiu 2,6% na quinta-feira (22 de outubro), para 26.008,86 pontos.
- O S&P 500 caiu 1,21%, para 7.663,43 pontos.
- O Dow Jones subiu 11,89 pontos (0,02%), para 52.867,98 pontos.
- O índice de semicondutores da Filadélfia despencou 6,7%, sua maior queda diária desde 23 de junho.
- O índice está mais de 26% abaixo do recorde de fechamento de 22 de junho.
- O rendimento do título do Tesouro americano de 10 anos caiu abaixo de 5% pela primeira vez em quase um mês.
- A queda de quase 0,2 ponto percentual no rendimento de 10 anos foi a mais forte em um único dia em mais de três anos.
- O S&P 500 teve seu pior dia desde julho.
- A maioria das ações americanas subiu, já que a fraqueza se concentrou em tecnologia.
- O mercado precifica a probabilidade de o Fed (banco central dos EUA) subir os juros em mais 25 pontos-base até o fim do ano.
- Os pedidos de seguro-desemprego estão perto das mínimas em várias décadas.
- A Meta caiu 7,0% após registrar seu primeiro fluxo de caixa negativo em mais de uma década.
- A Lockheed Martin subiu 7,0% após elevar suas projeções anuais de vendas e lucro.
**Fontes:**
- [S74] Reuters (via Investing.com) — https://www.investing.com/news/stock-market-news/nasdaq-futures-drop-over-1-as-ai-worries-resurface-oil-climbs-4965180
- [S75] Wall Street Journal — https://www.wsj.com/livecoverage/stock-market-today-dow-sp-500-nasdaq-10-22-2026
- [S76] Associated Press — https://apnews.com/article/stocks-markets-rates-earnings-oil-33767691a4a0730b96d6f0c5100ea9b2
