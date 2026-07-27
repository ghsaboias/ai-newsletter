# Fatos — Newsletter [Tech] 15 de Julho de 2026

## DeepSeek — preparação de IPO e salto de receita
- A DeepSeek começou os preparativos para uma oferta pública inicial (IPO).
- Está trabalhando com firmas de contabilidade e bancos para protocolar o pedido de listagem no mercado acionário da China continental.
- O protocolo pode ocorrer já no fim de 2026, mirando estreia em 2027.
- A receita anualizada (run rate) da DeepSeek chegou a US$400 milhões-US$500 milhões.
- Esse valor é cerca do dobro dos US$200 milhões-US$220 milhões estimados em 2025.
- Semanas depois de fechar uma rodada de ~US$7 bilhões a uma avaliação de ~US$50 bilhões no início de junho, a DeepSeek começou esta semana negociações para uma nova rodada.
- A nova rodada busca ao menos 10 bilhões de yuans (~US$1,5 bilhão) a uma avaliação pré-money de ~US$71 bilhões.
- O fundador Liang Wenfeng disse a investidores que a DeepSeek vai priorizar pesquisa de IA inovadora e continuar desenvolvendo modelos de código aberto, em vez de comercialização de curto prazo.
- Liang prometeu manter o desenvolvimento de modelos de IA de código aberto enquanto busca a inteligência geral artificial (AGI).
**Fontes:**
- [S1] The Information — https://www.theinformation.com/articles/deepseeks-annualized-revenue-nears-500-million-boosting-fundraise-ipo-plans
- [S2] The Asia Business Daily — https://www.asiae.co.kr/en/article/2026071509454936678
- [S3] TechCrunch — https://techcrunch.com/2026/07/14/deepseek-reportedly-in-talks-to-raise-1-5b-then-ipo/
- [S4] The Business Times — https://www.businesstimes.com.sg/startups-tech/technology/deepseek-prepares-ipo-filing-soon-2026-eyes-us71-billion-valuation-ft
- [S5] Crypto Briefing — https://cryptobriefing.com/deepseek-annualized-revenue-400m-500m/

## Google DiffusionGemma — modelo de difusão de texto aberto
- O Google lançou o DiffusionGemma, um modelo aberto experimental sob licença Apache 2.0.
- É um Mixture-of-Experts (MoE) de 26 bilhões de parâmetros.
- O modelo gera blocos de texto em paralelo via difusão, em vez de token por token.
- Entrega geração de texto até 4x mais rápida em GPUs.
- Alcança mais de 1.000 tokens por segundo em uma única NVIDIA H100.
- Alcança mais de 700 tokens por segundo em uma RTX 5090.
- Ativa apenas 3,8 bilhões de parâmetros durante a inferência.
- Cabe em 18GB de VRAM quando quantizado.
- Os pesos estão disponíveis no Hugging Face.
- O Google observa que a qualidade da saída é inferior à do Gemma 4 padrão.
- O Google posiciona o modelo para fluxos de trabalho locais e de baixa concorrência, como edição in-line, preenchimento de código (code infilling) e iteração rápida.
**Fontes:**
- [S6] Google AI (DEV Community) — https://dev.to/googleai/diffusiongemma-4x-faster-text-generation-fmd

## Miles Wang — startup de descoberta de medicamentos com IA
- Miles Wang, pesquisador da OpenAI cujo trabalho inclui usar IA para acelerar descobertas científicas e biológicas, está saindo da empresa para lançar uma startup.
- A startup vai construir modelos de IA para descoberta de medicamentos.
- Espera-se que vários outros pesquisadores da OpenAI se juntem a ele.
- Wang está em negociações para captar cerca de US$200 milhões a uma avaliação de US$2 bilhões.
- A Lightspeed está em conversas para liderar a rodada.
- A startup pode focar em encontrar novos usos para medicamentos aprovados pela FDA (agência reguladora de medicamentos dos EUA) e compostos que fracassaram em testes anteriores.
- O negócio reflete o crescente interesse de investidores em aplicar IA às ciências da vida.
- A Chai Discovery anunciou uma captação de US$400 milhões a uma avaliação de US$3,8 bilhões na mesma semana (14 de julho).
- A Isomorphic Labs, spinout da DeepMind, captou uma Série B de US$2,1 bilhões em maio.
- Wang contestou publicamente os números de US$200 milhões e US$2 bilhões.
- Ele se recusou a fornecer valores corrigidos.
- O negócio não é final e os termos podem mudar.
**Fontes:**
- [S7] TechCrunch — https://techcrunch.com/2026/07/14/openai-researcher-miles-wang-in-talks-to-launch-ai-drug-discovery-startup-valued-at-2b/
- [S8] Eastern Herald — https://easternherald.com/2026/07/15/openai-researcher-miles-wang-ai-drug-discovery/

## xAI Grok Build — exfiltração de repositórios inteiros
- Um pesquisador de segurança (cereblab) demonstrou que o Grok Build CLI v0.2.93, da xAI, empacotava os repositórios rastreados inteiros dos usuários.
- Isso incluía o histórico completo do git e segredos/arquivos .env commitados.
- Os dados eram enviados como git bundles para um bucket do Google Cloud Storage.
- O volume enviado era cerca de 27.800x maior do que a tarefa de programação exigia.
- O envio ocorria mesmo quando o agente era explicitamente instruído a não abrir arquivos.
- O botão de opt-out de privacidade não impedia o envio.
- Apenas colocar os arquivos no gitignore ou uma flag do lado do servidor (disable_codebase_upload) impedia a transferência.
- O comportamento contradiz o marketing "local-first" da xAI.
- Em 14 de julho, Elon Musk disse no X que todos os dados de usuários enviados antes da mudança seriam "completa e absolutamente deletados".
- A xAI implantou uma correção do lado do servidor que interrompeu os envios de repositórios inteiros.
- Sam Altman, da OpenAI, classificou o incidente como "preocupante" e disse que era "uma razão para preferir harnesses de código aberto".
**Fontes:**
- [S9] The Register — https://www.theregister.com/ai-and-ml/2026/07/14/musk-promises-purge-after-grok-build-caught-sending-entire-repos-to-the-cloud/5271123
- [S10] The Next Web — https://thenextweb.com/news/grok-build-uploaded-entire-git-repositories-secrets
- [S11] GitHub (cereblab) — https://github.com/cereblab/grok-build-exfil-repro
- [S12] X — https://x.com/sama/status/2077053226080436235

## Anthropic — Claude for Teachers para educadores dos EUA
- A Anthropic lançou o Claude for Teachers em 14 de julho.
- O produto dá a educadores verificados do ensino básico (K-12) dos EUA acesso gratuito a recursos premium do Claude.
- Quem se inscrever até 30 de junho de 2027 ganha um ano completo de acesso.
- O produto inclui uma biblioteca de habilidades (skills) de ensino e conectores para currículos baseados em evidências.
- Os currículos são mapeados para padrões acadêmicos dos 50 estados.
- A Anthropic afirma que os modelos nunca são treinados nas conversas dos educadores.
- Será testado no Detroit Public Schools Community District em um estudo sobre bem-estar e prática dos educadores.
- O lançamento junta-se a Google (Gemini) e OpenAI na corrida para levar IA às salas de aula dos EUA.
**Fontes:**
- [S13] Anthropic — https://www.anthropic.com/news/claude-for-teachers
- [S14] Chalkbeat — https://www.chalkbeat.org/2026/07/14/anthropic-launches-claude-for-teachers-as-ai-companies-battle-for-classrooms/
- [S15] Anthropic — https://claude.com/solutions/teachers
- [S16] The Verge — https://www.theverge.com/ai-artificial-intelligence/965544/anthropic-introduced-a-claude-product-for-k-12-teachers

## OpenAI Codex — 8 milhões de usuários e demanda pelo GPT-5.6 Sol
- A OpenAI atingiu 8 milhões de usuários ativos entre o Codex e o ChatGPT Work.
- A empresa resetou os limites de uso para todos os usuários para permitir que explorem o GPT-5.6 Sol.
- A informação foi dada pelo líder do Codex, Thibault Sottiaux, em 14 de julho.
- Sam Altman disse que "o crescimento do 5.6 sol está insano".
- Altman alertou que pode haver "alguns soluços em breve" enquanto a equipe de inferência trabalha para escalar a capacidade e atender à demanda.
- O número de 8 milhões representa alta ante os 6 milhões de usuários ativos anunciados por Sottiaux cerca de 24,5 horas antes.
- O salto levou comentaristas a perguntar se o Codex teria ultrapassado o Claude Code, da Anthropic.
**Fontes:**
- [S17] X — https://x.com/thsottiaux/status/2077114635308986427
- [S18] X — https://x.com/sama/status/2077106587307798989
- [S19] X — https://x.com/latentspacepod/status/2076840521574842401

## InstaLILY — Série B de US$60 milhões
- A InstaLILY fechou uma Série B de US$60 milhões liderada pela Energize Capital.
- A rodada eleva o total captado para quase US$100 milhões.
- Participaram a Insight Partners e os novos investidores estratégicos Home Depot Ventures e United Rentals.
- A empresa lançou a "Lily", que descreve como a primeira "AI Forward Deployed Engineer" (engenheira de IA implantada junto ao cliente) do mundo.
- A Lily aprende os processos de um negócio, constrói e mantém software personalizado e entra em operação em poucos dias.
- A receita da empresa cresceu 5x no último ano.
- Em um distribuidor nacional, o software construído pela Lily gerou mais de US$200 milhões em novas vendas anuais.
- Em uma empresa de serviços de campo, ela reduziu o tempo de diagnóstico de equipamentos de 15 minutos para menos de 10 segundos.
- Isso reduziu o custo de atendimento de um chamado em 98%.
**Fontes:**
- [S20] SiliconANGLE — https://siliconangle.com/2026/07/14/instalily-developer-ai-teammates-can-automate-complex-business-specific-work-raises-60m/
- [S21] ACCESS Newswire — https://www.accessnewswire.com/newsroom/en/computers-technology-and-internet/instalily-raises-60-million-series-b-and-launches-lily-the-worlds-1190835
- [S22] Pulse 2.0 — https://pulse2.com/instalily-raises-60-million-series-b-and-launches-lily-as-an-ai-forward-deployed-engineer/

## ASML — resultados do 2º trimestre e projeção elevada
- A ASML reportou vendas líquidas totais de €9,33 bilhões no 2º trimestre de 2026 (alta de 21% na comparação anual).
- O resultado superou a estimativa de analistas de €8,80 bilhões.
- A margem bruta foi de 54,0%.
- O lucro líquido foi de €2,92 bilhões, ante os €2,62 bilhões esperados.
- A ASML elevou sua projeção de vendas líquidas para 2026 para €43 bilhões-€45 bilhões (US$49 bilhões-US$51 bilhões).
- A faixa anterior era de €36 bilhões-€40 bilhões, uma alta de cerca de 16% no ponto médio.
- A ASML projetou vendas líquidas totais de €11,0 bilhões-€12,0 bilhões no 3º trimestre de 2026, com margem bruta de 55%-57%.
- Citando entrada de pedidos "extremamente forte", a ASML disse que planeja adicionar cerca de 30% à sua capacidade de EUV low-NA (litografia ultravioleta extrema) e de imersão DUV para 2027.
- A empresa investiga um aumento adicional de 30% para 2028.
**Fontes:**
- [S23] ASML — https://www.asml.com/en/news/press-releases/2026/q2-2026-financial-results
- [S24] Reuters — https://wkzo.com/2026/07/15/asml-tops-q2-estimates-on-ai-chip-demand/

## Intel Foundry — primeiro produto lógico em High NA EUV
- A ASML disse que a Intel Foundry entrou em manufatura de alto volume para um subconjunto dos processadores Intel Core Ultra Series 3, de codinome Panther Lake.
- A produção usa a tecnologia EXE High NA EUV da ASML no nó de processo Intel 18A.
- Com o anúncio, a Intel Foundry tornou-se a primeira empresa do setor a enviar um produto lógico de alto volume usando High NA EUV.
- Camadas específicas do Intel 18A foram duplamente qualificadas em High NA em Oregon, com rendimento (yield) equiparado ao da plataforma NXE.
- O equipamento High NA EUV custa cerca de US$400 milhões por máquina.
- Isso é aproximadamente o dobro do preço de uma ferramenta EUV padrão.
- A ferramenta é tecnicamente desafiadora de introduzir na produção.
- A Intel a usa apenas para camadas específicas do chip.
**Fontes:**
- [S25] ASML — https://www.asml.com/en/news/press-releases/2026/high-na-euv-reaches-new-readiness-milestone
- [S26] The Economic Times (Reuters) — https://economictimes.indiatimes.com/tech/technology/intel-turns-to-next-generation-asml-tool-to-help-make-its-laptop-chips/articleshow/132406879.cms

## Índia — Gabinete aprova o Semicon 2.0
- O Gabinete da União da Índia, presidido pelo primeiro-ministro Narendra Modi, aprovou o Semicon 2.0 (India Semiconductor Mission 2.0) em 15 de julho.
- O pacote tem dotação de Rs 1,27 lakh crore (cerca de US$13-14 bilhões).
- A nova alocação é um forte aumento em relação aos Rs 76.000 crore aprovados na primeira fase da India Semiconductor Mission.
- A primeira fase foi lançada em dezembro de 2021.
- O ISM 2.0 será executado ao longo de 10 a 12 anos.
- Estende incentivos além da fabricação para empresas de design de semicondutores, fabricantes de materiais e fornecedores de equipamentos.
- O objetivo é construir toda a cadeia de valor de chips da Índia.
**Fontes:**
- [S27] The Indian Express — https://indianexpress.com/article/business/cabinet-semiconductor-mission-2-0-10787705/
- [S28] PMIndia — https://www.pmindia.gov.in/en/news_updates/cabinet-approves-semicon-2-0-government-delivers-on-its-commitment-for-a-long-term-policy-support-to-semiconductors-in-india/?comment=disable
- [S29] CNBC-TV18 — https://www.cnbctv18.com/technology/india-semiconductor-mission-cabinet-approval-likely-budget-beneficiaries-19945808.htm

## Walden Robotics — saída do modo furtivo com US$300 milhões
- A Walden Robotics saiu do modo furtivo (stealth) com US$300 milhões em financiamento a uma avaliação de US$1,1 bilhão.
- A rodada foi co-liderada pela Toyota (Toyota Motor Corp, Toyota Invention Partners e Toyota Ventures) e pela Deviation Capital.
- Os investidores da rodada incluem NVIDIA, Boeing, AE Ventures, Samsung Ventures, Prologis Ventures e CoreWeave Ventures.
- A empresa, sediada em Cambridge, Massachusetts, foi um spinout do Toyota Research Institute em janeiro de 2026.
- Desde fevereiro, seus robôs de uso geral fazem trabalho de produção em uma fábrica da Toyota na América do Norte.
- A Walden constrói robôs de uso geral (humanoides sobre rodas) movidos por Large Behavior Models.
- Esses modelos aprendem e melhoram enquanto executam trabalho real em manufatura e logística.
**Fontes:**
- [S30] Las Vegas Sun (Business Wire) — https://lasvegassun.com/news/2026/jul/15/walden-robotics-launches-with-300-million-to-put-g/
- [S31] TipRanks — https://www.tipranks.com/news/nvidia-backed-wheeled-humanoid-maker-walden-robotics-hits-1-1b-valuation

## Nokia e Nvidia — plataforma comercial de AI-RAN
- Em 15 de julho, a Nokia anunciou o que chamou de a primeira plataforma comercial de AI-RAN (rede de acesso via rádio acelerada por IA) do setor.
- A plataforma foi desenvolvida com a Nvidia.
- É construída sobre o software anyRAN da Nokia e a tecnologia de computação acelerada Aerial AI-RAN da Nvidia.
- A plataforma demonstrou ganhos de eficiência espectral de mais de 20%.
- A Nokia mira 50% até 2027 e mais de 100% até 2028.
- A disponibilidade comercial está planejada para 2027.
- As operadoras comprariam a capacidade via assinatura de software, em vez de troca de hardware.
- Há três opções de implantação: uma placa plug-in movida a GPU para sites AirScale existentes, um nó AI-RAN independente, ou servidores COTS (produtos comerciais de prateleira) nativos de nuvem.
- O CEO da Nokia, Justin Hotard, chamou o AI-RAN de "a maior inovação em rádio em décadas".
- O CEO da Nvidia, Jensen Huang, chamou a colaboração de "uma mudança geracional para as operadoras".
**Fontes:**
- [S32] StreetInsider — https://www.streetinsider.com/Corporate+News/Nokia+launches+commercial+AI-RAN+platform+with+Nvidia+partnership/26769984.html
- [S33] AI News — https://www.artificialintelligence-news.com/news/nokia-ai-ran-platform-nvidia/

## PJM — leilão de capacidade adiciona US$6,3 bilhões às contas de energia
- A PJM Interconnection, maior operadora de rede elétrica dos EUA, divulgou os resultados de um leilão de capacidade na terça-feira, 14 de julho.
- O leilão adicionaria US$6,3 bilhões em custos às contas de famílias e empresas ao longo dos próximos três anos.
- O aumento é impulsionado pela demanda de energia dos data centers.
- O leilão foi fechado a US$325 por megawatt-dia para 2028 e 2029.
- Esse é o valor máximo sob um teto de preços inicialmente negociado pelo governo Shapiro, da Pensilvânia.
- O teto foi negociado depois de o leilão de 2024 fechar a um recorde de US$269,92 por megawatt-dia.
- O leilão ficou 6.831 megawatts abaixo da meta de capacidade da PJM.
- O déficit é maior que o do ano anterior.
- Isso ocorre em meio à desativação de usinas de combustíveis fósseis e ao desenvolvimento proposto de data centers na região de 13 estados e em Washington, D.C.
**Fontes:**
- [S34] The New York Times — https://www.nytimes.com/2026/07/14/business/energy-environment/pjm-electricity-prices-data-centers.html
- [S35] Pennsylvania Capital-Star — https://penncapital-star.com/economy/pjm-interconnection-electricity-price-hits-cap-again-in-latest-auction/

## CoreWeave — derivativos para proteger contra queda no preço de memória
- A CoreWeave, empresa de nuvem voltada a IA, está estudando o uso de derivativos financeiros, incluindo opções de venda (puts), como possível hedge.
- O hedge seria contra uma futura queda nos preços de chips de memória e armazenamento.
- As discussões estão em estágio inicial e nenhum hedge foi executado.
- Para garantir o fornecimento, a CoreWeave e outras operadoras de nuvem assinaram acordos de longo prazo com fabricantes de memória e armazenamento, como Micron e SanDisk.
- Esses acordos garantem aos fornecedores um piso de preço para memória DRAM (memória dinâmica de acesso aleatório) e chips de armazenamento.
- Isso deixa os compradores expostos caso os preços caiam.
**Fontes:**
- [S36] CNA (Reuters) — https://www.channelnewsasia.com/business/exclusive-ai-cloud-company-coreweave-explores-wall-street-playbook-hedge-memory-chip-price-risk-6254781
- [S37] The Star (Reuters) — https://www.thestar.com.my/tech/tech-news/2026/07/15/exclusive-ai-cloud-company-coreweave-explores-wall-street-playbook-to-hedge-memory-chip-price-risk

## Irã e Estreito de Ormuz — EUA retomam bloqueio e bombardeiam bases
- Os EUA reimpuseram um bloqueio naval ao Irã e intensificaram sua campanha de ataques aéreos na quarta-feira, 15 de julho.
- Os ataques atingiram um quartel do exército iraniano.
- Segundo autoridades iranianas, os ataques mataram ao menos sete soldados e feriram mais de 260 pessoas.
- A ação foi em retaliação a ataques do Irã a navios que tentavam passar pelo Estreito de Ormuz.
- O bloqueio naval contra embarcações que transitam de e para portos iranianos voltou a vigorar às 2000 GMT (1600 EDT) de 14 de julho.
- O bloqueio havia sido suspenso em junho.
- O Irã declarou o Estreito de Ormuz fechado.
- O petróleo Brent subiu acima de US$86 o barril e o WTI acima de US$80.
- O Brent subiu US$1,46, ou 1,72%, para US$86,19 o barril.
- O WTI ganhou US$1,11, ou 1,4%, para US$80,40 o barril.
- Trump ameaçou atacar usinas de energia e pontes do Irã na próxima semana, a menos que Teerã retorne às negociações.
- Trump cancelou a taxa planejada de 20% sobre navios que usam o Estreito de Ormuz.
- Ele a substituiu por acordos comerciais com aliados do Golfo.
- Ao menos 30 pessoas foram mortas no Irã desde o início dos renovados ataques dos EUA na semana passada, segundo um porta-voz do governo iraniano.
**Fontes:**
- [S38] AP News — https://apnews.com/article/iran-us-hormuz-strait-war-july-15-2026-b7c592f269d822407dd6b5641602bf25
- [S39] The Straits Times — https://www.straitstimes.com/world/middle-east/iran-reports-fresh-us-strikes-washington-reimposes-naval-blockade-in-return-to-war
- [S40] Euronews — https://www.euronews.com/2026/07/15/iran-launches-strikes-on-neighbours-as-us-resumes-blockade-and-trump-threatens-to-hit-powe
- [S41] The Kathmandu Post — https://kathmandupost.com/world/2026/07/15/trump-resumes-iran-port-blockade-and-threatens-strikes-on-energy-targets
- [S42] The Economic Times — https://economictimes.indiatimes.com/markets/commodities/news/oil-price-today-july-15-crude-oil-above-86-as-us-iran-exchange-fresh-strikes-bigger-surge-brewing/articleshow/132404132.cms

## Inflação nos EUA — CPI de junho esfria e derruba aposta em alta de juros
- O CPI (índice de preços ao consumidor) cheio caiu 0,4% em junho.
- Foi a maior queda mensal desde abril de 2020.
- Isso reduziu a taxa de inflação anual para 3,5%, ante 4,2% em maio.
- O núcleo do CPI ficou estável no mês e recuou para 2,6% na comparação anual.
- As chances de uma alta de juros em 29 de julho, segundo a ferramenta CME FedWatch, caíram de 47% para 17% minutos após a divulgação.
- O rendimento (yield) do Treasury de 10 anos caiu cerca de 6 pontos-base.
- Os preços da gasolina caíram 9,7% na comparação mensal.
- Essa foi a principal causa da queda do índice cheio.
- O presidente do Fed, Kevin Warsh, disse ao Congresso, em seu testemunho semestral, que o FOMC (Comitê Federal de Mercado Aberto) manteve a taxa dos fed funds em 3,5%-3,75% em sua reunião de junho.
- Warsh disse que o comitê não tem "tolerância para uma inflação persistentemente elevada".
**Fontes:**
- [S43] Realtor.com Economic Research — https://www.realtor.com/research/cpi-inflation-june-2026/
- [S44] American Banker — https://www.americanbanker.com/news/inflation-slowed-to-3-5-in-june-giving-fed-breathing-room
- [S45] Federal Reserve — https://www.federalreserve.gov/newsevents/testimony/files/warsh20260714a.pdf
- [S46] The New York Times — https://www.nytimes.com/2026/07/14/business/economy/warsh-fed-cpi-inflation.html

## Grandes bancos dos EUA — recordes de lucro no 2º trimestre
- Quatro dos maiores bancos dos EUA reportaram um lucro coletivo de US$43 bilhões no 2º trimestre, na terça-feira, 14 de julho.
- Os resultados quebraram recordes e superaram as projeções dos analistas.
- O JPMorgan Chase reportou lucro líquido de US$21,2 bilhões no 2º trimestre, ou US$7,70 por ação.
- Isso representa alta ante os US$15,0 bilhões (US$5,24 por ação) de um ano antes.
- O Goldman Sachs reportou lucro líquido de US$6,63 bilhões e lucro por ação diluído de US$20,98.
- O retorno anualizado sobre o patrimônio foi de 23,5%.
- O Goldman elevou seu dividendo trimestral para US$5,00 por ação.
- As ações do Goldman subiram 9% no dia.
- O lucro líquido do Citigroup subiu 45% na comparação anual, para US$5,8 bilhões (US$3,15 por ação).
- A receita foi de US$24,8 bilhões, impulsionada pelo crescimento em seus cinco negócios.
**Fontes:**
- [S47] The New York Times — https://www.nytimes.com/2026/07/14/business/jpmorgan-goldman-bofa-wells-fargo-bank-earnings.html
- [S48] SEC EDGAR — https://www.sec.gov/Archives/edgar/data/19617/000162828026048078/jpm-20260714.htm
- [S49] Goldman Sachs — https://www.goldmansachs.com/pressroom/press-releases/2026/2026-07-14-q2-results
- [S50] SEC EDGAR — https://www.sec.gov/Archives/edgar/data/831001/000110465926083383/c-20260714xex99d1.htm

## Stripe e Advent — oferta conjunta de US$53 bilhões pelo PayPal
- A empresa de pagamentos Stripe e a firma de private equity Advent International fizeram uma oferta conjunta para adquirir o PayPal por US$60,50 por ação.
- A oferta avalia o PayPal em mais de US$53 bilhões.
- Representa um prêmio de cerca de 28% sobre o fechamento do PayPal na terça-feira.
- A oferta, apresentada no início deste mês, é lastreada por cerca de US$50 bilhões em financiamento bancário comprometido.
- A proposta segue uma primeira aproximação feita no início de abril.
- A Stripe e a Advent deteriam o PayPal em conjunto, com participações iguais, em vez de dividir a empresa.
- Elas ainda não tinham recebido resposta do PayPal.
**Fontes:**
- [S51] CNA — https://www.channelnewsasia.com/business/exclusive-stripe-advent-offer-buy-paypal-more-53-billion-sources-say-6255126
- [S52] Bloomberg Law — https://news.bloomberglaw.com/private-equity/stripe-advent-offer-to-buy-paypal-for-53-billion-reuters-says
- [S53] The Economic Times — https://economictimes.indiatimes.com/news/international/business/stripe-advent-offer-to-buy-paypal-for-more-than-53-billion-sources-say/articleshow/132405251.cms

## Uber e Delivery Hero — negociações avançadas de aquisição
- A Delivery Hero confirmou em 14 de julho que está em negociações avançadas com a Uber Technologies sobre uma possível oferta de aquisição a todos os acionistas.
- As ações da Delivery Hero fecharam em alta de 5,76%, a €39,10.
- Isso dá à empresa um valor de mercado de cerca de €11,2 bilhões (US$12,8 bilhões).
- Espera-se que o negócio avalie a empresa bem acima do preço recente de ~€36 por ação.
- A Uber já detém uma participação de 24,99%.
- Somados derivativos, seu interesse econômico chega a cerca de 36,8%.
- Uma aproximação anterior foi de €33 por ação.
**Fontes:**
- [S54] EQS News — https://www.eqs-news.com/news/ad-hoc/delivery-hero-confirms-advanced-negotiations-with-uber-technologies-in-respect-to-potential-takeover-offer/902cb90f-2052-443a-b6c1-17ebf890cc69_en
- [S55] The Independent — https://www.independent.co.uk/news/business/uber-delivery-hero-acquisition-b3014889.html
- [S56] Proactive Investors — https://www.proactiveinvestors.com/companies/news/1095430/uber-reportedly-in-advanced-talks-to-acquire-delivery-hero-1095430.html

## Celcuity — FDA aprova o Revtorpyk para câncer de mama avançado
- Em 14 de julho, a FDA aprovou o gedatolisibe (Revtorpyk), da Celcuity.
- A aprovação é para uso em combinação com fulvestranto, com ou sem palbociclibe.
- A indicação é para câncer de mama avançado HR-positivo, HER2-negativo, do tipo selvagem (wild-type) para PIK3CA, após ao menos uma linha de terapia endócrina.
- No estudo de Fase 3 VIKTORIA-1, a dupla gedatolisibe mais fulvestranto reduziu o risco de progressão da doença ou morte em 67% ante o fulvestranto isolado.
- A tripla, que adiciona palbociclibe, reduziu esse risco em 76%.
- A Celcuity, uma pequena biotech de capital aberto, posicionou o medicamento para superar tratamentos similares da Novartis e da Roche.
- O CEO Brian Sullivan quer que o medicamento se torne um "novo padrão de tratamento" no câncer de mama HR-positivo, HER2-negativo de segunda linha.
**Fontes:**
- [S57] Endpoints News — https://endpoints.news/celcuity-wins-approval-for-breast-cancer-drug-revtorpyk/
- [S58] The ASCO Post — https://ascopost.com/news/july-2026/gedatolisib-combinations-approved-by-fda-for-hr-positiveher2-negative-breast-cancer/
- [S59] CancerNetwork — https://www.cancernetwork.com/view/fda-approves-gedatolisib-for-hr-her2-pik3ca-wild-type-advanced-breast-cancer

## Neko Health — Série C de US$700 milhões para exames corporais preventivos
- A Neko Health, startup de health-tech de Estocolmo cofundada por Daniel Ek, do Spotify, anunciou uma Série C de US$700 milhões em 15 de julho.
- A rodada foi liderada pela Lightspeed Venture Partners e co-liderada pela O.G. Venture Partners.
- A rodada segue uma Série B de US$260 milhões em janeiro de 2025.
- Atraiu investidores como Atomico, General Catalyst, Lakestar, Liberty City Ventures e BDT & MSD.
- A Neko opera oito clínicas na Suécia e na Grã-Bretanha.
- As clínicas oferecem um exame corporal completo não invasivo de 60 minutos, mais um exame de sangue.
- O serviço custa £299 no Reino Unido.
- A empresa planeja abrir suas primeiras clínicas nos EUA, incluindo em Nova York, ainda este ano.
**Fontes:**
- [S60] The New York Times — https://www.nytimes.com/2026/07/15/business/dealbook/neko-health-ek-funding.html
- [S61] Tech.eu — https://tech.eu/2026/07/15/neko-health-raises-700m-as-demand-grows-for-preventive-health-scans/
- [S62] EU-Startups — https://www.eu-startups.com/2026/07/daniel-eks-neko-health-raises-e612-7-million-series-c-as-it-prepares-for-us-expansion/
