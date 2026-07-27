# Fatos — Newsletter [Tech] 16 de Julho de 2026

## Thinking Machines — Inkling, modelo multimodal de pesos abertos
- A Thinking Machines Lab lançou o Inkling, seu primeiro modelo desenvolvido internamente, na manhã de quarta-feira, 15 de julho de 2026.
- A Thinking Machines Lab foi fundada por Mira Murati, ex-CTO da OpenAI.
- O Inkling é um transformer Mixture-of-Experts (MoE, arquitetura que ativa apenas parte dos parâmetros do modelo a cada token) com 975 bilhões de parâmetros totais e 41 bilhões ativos.
- O modelo suporta janela de contexto de até 1 milhão de tokens.
- O Inkling foi pré-treinado com 45 trilhões de tokens de texto, imagens, áudio e vídeo.
- Diferentemente dos modelos principais da OpenAI, da Anthropic e do Google, o Inkling é de pesos abertos: desenvolvedores e empresas de fora podem baixá-lo e modificá-lo diretamente.
- O Inkling é distribuído sob licença Apache 2.0, considerada amigável a uso empresarial.
- O modelo marca 77,6% no SWE-bench Verified, benchmark de engenharia de software.
- No SWE-bench Verified, o Inkling supera o rival aberto norte-americano Nvidia Nemotron 3, que marca 71,9%.
- O Inkling marca 91,4% no VoiceBench, benchmark de compreensão de voz, contra 94,4% do Gemini 3.1 Pro em esforço de raciocínio alto.
- O desempenho do Inkling é alto para modelos de pesos abertos, mas abaixo do estado da arte.
- O design MoE segue em boa parte o do DeepSeek-V3.
- Cada camada MoE contém 256 especialistas roteados e 2 especialistas compartilhados, com 6 especialistas roteados ativados por token.
- O Inkling usa um roteador baseado em sigmoide com viés de balanceamento de carga sem função de perda auxiliar.
- Junto com o Inkling, a empresa divulgou uma prévia do Inkling-Small, um modelo MoE de 276 bilhões de parâmetros com 12 bilhões ativos.
- O Inkling-Small tem um equilíbrio diferente entre desempenho e latência e iguala ou supera o irmão maior em vários benchmarks.
- Os pesos do modelo estão disponíveis para download no Hugging Face.
- O Inkling está disponível na Tinker com opções de contexto de 64 mil e 256 mil tokens.
- A empresa oferece o Inkling com 50% de desconto por tempo limitado.
- O model card lista data de lançamento de 15 de julho de 2026.
- O model card descreve um transformer decoder-only de 66 camadas, nativamente multimodal na entrada.
- Imagens são codificadas por um encoder hierárquico de patches e áudio por codificação em tokens discretos.
**Fontes:**
- [S1] Thinking Machines Lab — https://thinkingmachines.ai/news/introducing-inkling/
- [S2] Thinking Machines Lab — https://thinkingmachines.ai/model-card/inkling/
- [S3] TechCrunch — https://techcrunch.com/2026/07/15/thinking-machines-amps-up-its-bet-against-one-size-fits-all-ai-with-its-first-open-model-inkling/
- [S4] VentureBeat — https://venturebeat.com/technology/thinking-machines-open-sources-first-multimodal-language-model-inkling-focused-on-low-cost-and-resistance-to-censorship
- [S5] Hugging Face — https://huggingface.co/thinkingmachines/Inkling

## OpenAI — GPT-Red, modelo de red-teaming automatizado
- O GPT-Red é um modelo de red-teaming automatizado (busca sistemática de falhas de segurança simulando um atacante) treinado para encontrar vulnerabilidades de injeção de prompt em escala.
- A OpenAI diz que o objetivo é corrigir as vulnerabilidades antes de implantações mais amplas.
- O GPT-Red é treinado com aprendizado por reforço em self-play: o modelo atacante e um conjunto de LLMs defensores diversos são treinados simultaneamente em um amplo conjunto de cenários de red-teaming.
- O GPT-Red é recompensado por provocar uma falha válida, como uma injeção de prompt bem-sucedida; os modelos defensores são recompensados por resistir ao ataque e completar suas tarefas originais.
- A OpenAI treinou o GPT-Red na escala de computação de alguns de seus maiores treinamentos de pós-treinamento.
- A OpenAI descreve o esforço como uma quantidade de computação sem precedentes dedicada puramente a melhorar a segurança.
- Ao fim do treinamento, o GPT-Red conseguia quebrar quase todos os modelos contra os quais foi colocado, internos e de produção, até o GPT-5.5 inclusive.
- Depois de concluído o treinamento do GPT-Red, a OpenAI usou o modelo para gerar injeções de prompt no treinamento do GPT-5.6, que se tornou altamente resistente aos ataques do GPT-Red.
- Em um benchmark independente com cenários que o modelo não tinha visto no treinamento, o GPT-Red encontrou caminhos de ataque bem-sucedidos em 84% dos casos.
- Pesquisadores humanos de segurança tiveram sucesso em 13% dos casos no mesmo desafio.
- A OpenAI afirma que o GPT-Red descobriu um tipo de ataque que os pesquisadores não conheciam, batizado de "fake chain of thought" (cadeia de raciocínio falsa).
- No ataque, o GPT-Red insere uma entrada falsa na cadeia de raciocínio de outro modelo, enganando-o para agir com base em informações forjadas.
- O pesquisador da OpenAI Dylan Hunn disse: "Comparado a um red-teamer humano, o modelo é muito, muito bom em encontrar exatamente o que vai funcionar, exatamente o que é mais eficaz."
- Hunn disse que o modelo é "extremamente persistente em aprofundar um ataque que descobriu" e varia sistematicamente os ataques que encontra.
**Fontes:**
- [S6] OpenAI — https://openai.com/index/unlocking-self-improvement-gpt-red/
- [S7] MIT Technology Review — https://www.technologyreview.com/2026/07/15/1140514/meet-gpt-red-an-llm-super-hacker-openai-built-to-make-its-models-safer/
- [S8] Tech Times — https://www.techtimes.com/articles/320656/20260715/openai-built-ai-attack-itself-gpt-red-exposed-flaws-humans-missed.htm
- [S9] Help Net Security — https://www.helpnetsecurity.com/2026/07/16/openai-gpt-red-prompt-injection-test/

## Anthropic e Blackstone — Ode, consultoria de implementação de IA
- A Ode with Anthropic é a empresa de implementação de IA de US$1,5 bilhão que a Anthropic lançou em maio como joint venture com Blackstone, Hellman & Friedman, Goldman Sachs e outros.
- A empresa agora tem nome e marca oficiais.
- O movimento segue a versão da própria OpenAI, a The Deployment Company.
- Os lançamentos evidenciam o reconhecimento crescente entre laboratórios de IA de fronteira de que conquistar clientes corporativos exige mais do que entregar modelos melhores.
- A Ode emprega 100 engenheiros e trabalha de perto com a equipe de IA aplicada da Anthropic.
- A Ode opera sob um princípio "Claude-first": implementa a tecnologia da Anthropic, incluindo recursos como o Claude Tag no Slack, sempre que possível.
- A Ode usará produtos de IA de concorrentes se necessário.
- A Ode é construída sobre a base da Fractional AI, empresa de serviços de IA aplicada adquirida em maio de 2026.
- A equipe da Fractional AI, ao lado de engenheiros da Anthropic, forma o núcleo operacional da Ode.
- Além dos sócios fundadores, o consórcio de investidores inclui Apollo Global Management, General Atlantic, GIC, Goldman Sachs, Leonard Green & Partners e Sequoia Capital.
- A Ode é liderada por Chris Taylor como CEO e Eddie Siegel como CTO.
- Taylor e Siegel ocupavam os mesmos cargos na Fractional AI, que fundaram em 2024 com Travis May.
- As gestoras de private equity que apoiam a Ode encaminharão suas próprias empresas de portfólio à joint venture como clientes potenciais.
- A Ode não limitará a venda de seus serviços a essas empresas.
**Fontes:**
- [S10] TechCrunch — https://techcrunch.com/2026/07/15/anthropic-blackstone-bet-the-next-trillion-dollar-ai-business-is-implementation-not-models/
- [S11] Hellman & Friedman — https://hf.com/anthropic-blackstone-and-hellman-friedman-introduce-ode-with-anthropic-an-enterprise-ai-services-firm/
- [S12] Technology.org — https://www.technology.org/2026/07/16/ode-with-anthropic-blackstone-ai-implementation/

## Google DeepMind e Isomorphic Labs — programa de bioresiliência
- O Google DeepMind e a Isomorphic Labs publicaram em 16 de julho de 2026 uma abordagem conjunta de bioresiliência.
- A abordagem cobre prevenção, detecção e resposta a ameaças biológicas.
- O agente AlphaEvolve, do DeepMind, pode otimizar algoritmos usados para produzir e analisar dados de sequenciamento metagenômico.
- A otimização permite análise de DNA mais rápida e precisa, barateando o rastreamento de doenças em escala mundial e ajudando a detectar novos surtos mais rápido.
- A Isomorphic Labs criou uma unidade dedicada para implantar rapidamente seu motor de design de fármacos e projetar contramedidas médicas.
- As contramedidas visam tanto pandemias de ocorrência natural quanto riscos potenciais decorrentes do uso indevido de IA avançada.
- A unidade tem como objetivo apoiar órgãos governamentais e organizações sem fins lucrativos durante surtos inéditos.
- As empresas exploram como o AlphaGenome e a anotação de função de proteínas poderiam detectar e caracterizar patógenos a partir de dados de sequência.
- A meta é identificar padrões inéditos e ameaças emergentes mais rápido do que os métodos tradicionais.
- As empresas afirmam que o cenário global de biossegurança evolui rapidamente, citando mudanças nos ecossistemas naturais, viagens globais e o potencial uso indevido de IA.
- As empresas enquadram a IA como fonte de risco de biossegurança e, ao mesmo tempo, ferramenta crítica de resposta.
- No último ano, a parceria se engajou com mais de 15 agências governamentais, organizações de biossegurança e grupos de pesquisa.
- O DeepMind e a Isomorphic Labs concedem a pesquisadores de confiança acesso a seus sistemas de IA mais recentes.
**Fontes:**
- [S13] Google DeepMind — https://deepmind.google/blog/our-approach-to-bioresilience/
- [S14] Isomorphic Labs — https://www.isomorphiclabs.com/articles/our-approach-to-bioresilience
- [S15] Blockchain.News — https://blockchain.news/news/google-deepmind-isomorphic-labs-bioresilience-plan

## xAI — processo contra usuário do Grok por CSAM gerado por IA
- A xAI abriu processo contra Terry Wayne Harwood, morador da Carolina do Sul, no Tribunal Distrital dos EUA para o Distrito Norte do Texas.
- A ação alega que Harwood violou os Termos de Serviço e a Política de Uso Aceitável da xAI.
- Segundo a ação, Harwood explorou os recursos de geração de imagens do Grok para transformar fotografias não sexuais em imagens sexualmente explícitas, sem o conhecimento ou consentimento das pessoas retratadas.
- O caso é uma das primeiras ações legais conhecidas de uma empresa de IA contra um de seus próprios usuários pela suposta criação de conteúdo sexual ilegal gerado por IA.
- A ação alega que Harwood criou múltiplas contas na xAI.
- A ação alega que Harwood usou "prompts enganosos" para contornar os mecanismos de segurança embutidos no Grok, projetados para impedir a geração de material explícito envolvendo menores.
- A xAI alega que Harwood subiu imagens não sexuais de adultos e de menores e tentou usar o Grok para gerar deepfakes sexualmente explícitos, incluindo material de abuso sexual infantil.
- Harwood foi preso no início deste ano sob acusações relacionadas ao material.
- A ação foi protocolada em 15 de julho de 2026.
- O caso chega em meio a um escrutínio mais amplo sobre as práticas de segurança do Grok.
- A xAI pediu desculpas publicamente no ano passado depois que o chatbot gerou conteúdo violento e antissemita, atribuindo o episódio a uma atualização problemática do sistema.
**Fontes:**
- [S16] International Business Times — https://www.ibtimes.sg/xai-sues-south-carolina-man-accused-using-grok-create-child-sexual-abuse-deepfakes-landmark-ai-89867
- [S17] Reuters — https://www.reuters.com/legal/litigation/musks-xai-sues-grok-user-over-sexualized-deepfakes-2026-07-15/
- [S18] OECD.AI — https://oecd.ai/en/incidents/2026-07-15-91fd

## Dario Amodei — US$1 milhão ao super PAC Public First
- Dario Amodei, CEO da Anthropic, doou US$1 milhão em maio ao Public First, um super PAC (comitê de ação política que arrecada e gasta sem limites, sem coordenar com campanhas).
- O Public First apoia candidatos que compartilham o objetivo da Anthropic de impor regulação de segurança à inteligência artificial.
- A doação consta de registros da Comissão Federal Eleitoral (FEC) divulgados no fim da quarta-feira, 15 de julho.
- Aparentemente é a primeira doação política de sete dígitos de Amodei, embora ele já tenha doado quantias menores a políticos democratas.
- A doação vem enquanto o Public First e outras organizações alinhadas à Anthropic enfrentam a Leading the Future, uma rede rival de super PACs da indústria contrária a regulações onerosas de IA.
- Cada lado despeja milhões de dólares em lados opostos da disputa, muito acompanhada, pela vaga do deputado democrata Jerry Nadler, que se aposenta.
- A Anthropic, como empresa, doou US$20 milhões ao Public First em fevereiro de 2026, apoiando candidatos ao Congresso favoráveis a regras de segurança para IA.
- A Leading the Future, super PAC financiado por bilionários, planeja gastar US$125 milhões neste ano para eleger membros do Congresso favoráveis a uma regulação mais leve da tecnologia.
- O Public First Action disse em 30 de junho que arrecadou mais de US$80 milhões até a data, incluindo US$20 milhões nos 10 dias anteriores.
- O Public First Action está ligado a três PACs: Defending Our Values PAC (apoia republicanos), Jobs and Democracy PAC (apoia democratas) e o bipartidário Public First PAC.
**Fontes:**
- [S19] Politico — https://www.politico.com/news/2026/07/16/anthropics-ceo-gives-1-million-to-super-pac-amid-feud-of-ai-big-money-groups-01000461
- [S20] Los Angeles Times — https://www.latimes.com/business/story/2026-02-12/anthropic-pledges-20-million-to-candidates-who-favor-ai-safety
- [S21] Axios — https://www.axios.com/2026/06/30/ai-safeguards-public-first-action-raised-80-million

## Meta — alertas a pais sobre conversas de adolescentes com o chatbot
- A Meta anunciou na quinta-feira, 16 de julho, que passará a notificar os pais se seu filho adolescente falar sobre suicídio ou automutilação com o chatbot Meta AI.
- A Meta também trabalha na capacidade de acionar serviços de emergência quando as conversas de alguém sugerirem risco de automutilação.
- A Meta afirma ter construído um sistema de IA dedicado para identificar conversas em que um adolescente faz uma referência clara a se machucar.
- Todas as conversas sinalizadas por essa IA passam por revisão manual antes que um alerta seja enviado.
- A Meta diz que agirá com cautela quando a intenção do adolescente for ambígua: "Embora isso signifique que às vezes podemos notificar os pais quando talvez não haja motivo real de preocupação, achamos que este é o ponto de partida certo."
- Os alertas já estão ativos para pais que usam a Supervisão Parental do Instagram nos EUA, no Reino Unido, na Austrália e no Canadá.
- Os alertas serão liberados globalmente até o fim do ano.
- A configuração "Conteúdo Limitado" da Meta, que coloca adolescentes em uma experiência mais restritiva no Instagram, agora se aplica também ao Meta AI.
- Com a configuração, o chatbot recusa uma gama mais ampla de prompts.
- As mudanças chegam enquanto a Meta e outras empresas de tecnologia enfrentam escrutínio de reguladores e de pais sobre como chatbots de IA respondem a usuários em crise, especialmente adolescentes.
- A questão de responsabilidade civil vem moldando cada vez mais como as empresas de IA projetam e comercializam seus produtos.
**Fontes:**
- [S22] TechCrunch — https://techcrunch.com/2026/07/16/meta-now-alerts-parents-if-their-teen-discussed-suicide-or-self-harm-with-its-ai-chatbot/

## TSMC — lucro recorde no 2º trimestre e projeção elevada
- O lucro líquido da TSMC no segundo trimestre atingiu recorde de NT$706,56 bilhões (cerca de US$21,98 bilhões).
- O lucro subiu 77,4% em relação ao mesmo período do ano anterior.
- O resultado ficou muito acima da estimativa da Bloomberg, de NT$623,73 bilhões.
- Foi o quinto trimestre consecutivo de lucro recorde para a fabricante de chips.
- A receita trimestral foi recorde de NT$1,27 trilhão (cerca de US$39 a 40,2 bilhões), alta de 36% na comparação anual.
- A receita superou a faixa de projeção da própria empresa e ficou um pouco acima da previsão de analistas, de US$39,94 bilhões.
- A margem bruta alcançou 67,7%, acima das expectativas e da própria projeção da empresa.
- A TSMC elevou a projeção de crescimento de receita para 2026 a pouco acima de 40% em dólares, contra previsão anterior de mais de 30%.
- A empresa elevou a projeção de investimento de capital de 2026 para US$60 a 64 bilhões, ante US$52 a 56 bilhões — recorde histórico e alta de cerca de 14%.
- Cerca de 70% a 80% do orçamento de capital de 2026 vai para tecnologias de processo avançadas.
- Cerca de 10% vai para nós especiais e 10% a 20% para empacotamento avançado, testes e fabricação de máscaras.
- O CEO C.C. Wei disse: "A megatendência de IA está cada vez mais forte."
- Wei citou uma lacuna "muito grande" entre a demanda dos clientes e a oferta, e disse que a convicção plurianual da empresa é "muito alta".
- Wei disse que a IA agêntica está reavivando a demanda por CPUs.
- As ações da TSMC fecharam a US$419,48 e caíram 1,55% no after-hours, para US$412,99.
- Investidores avaliaram os planos de gasto mais pesados e a projeção de margens menores no trimestre corrente.
**Fontes:**
- [S23] Investing.com — https://www.investing.com/news/earnings/tsmc-q2-profit-blows-past-estimates-on-robust-aifueled-demand-4794650
- [S24] Investing.com — https://www.investing.com/news/transcripts/earnings-call-transcript-tsmc-lifts-2026-outlook-as-ai-demand-stays-hot-in-q2-2026-93CH-4794777
- [S25] TradingKey — https://www.tradingkey.com/analysis/stocks/more/262034508-tsmc-q2-earnings-beat-expectations-raises-full-year-outlook-tradingkey
- [S26] BiggoFinance — https://finance.biggo.com/news/US_TSM_2026-07-16

## TSMC — mais US$100 bilhões no Arizona
- O CEO C.C. Wei disse que a TSMC investirá US$100 bilhões adicionais para ampliar sua capacidade de produção no estado americano do Arizona, somando-se às instalações que já tem lá.
- A empresa tem três polos de manufatura no mundo: Taiwan, Estados Unidos e Japão.
- O novo compromisso eleva o investimento total prometido pela TSMC nos EUA a US$265 bilhões.
- O aporte financiará quatro novas fábricas de chips.
- A meta final é ter 10 fábricas de wafers e 2 plantas de empacotamento nos Estados Unidos.
- O aporte adicional no Arizona é direcionado a fábricas de 2 nanômetros e abaixo, mais empacotamento avançado.
- A promessa segue um acordo comercial entre EUA e Taiwan de janeiro de 2026, no qual empresas taiwanesas se comprometeram com US$250 bilhões em investimentos nos EUA em troca de tarifas menores.
- O secretário de Comércio dos EUA, Howard Lutnick, disse que os US$250 bilhões incluem US$100 bilhões já comprometidos pela TSMC em 2025.
- Lutnick disse que os investimentos taiwaneses visam impulsionar a produção de semicondutores, energia e inteligência artificial nos Estados Unidos.
**Fontes:**
- [S27] The New York Times — https://www.nytimes.com/2026/07/16/business/tsmc-chips-investment-arizona.html
- [S28] The Washington Post / AP — https://www.washingtonpost.com/business/2026/07/16/taiwan-tsmc-chipmaking-ai-arizona-fab/1154d16c-80e3-11f1-8a16-393bd03340b0_story.html
- [S29] Investing.com — https://www.investing.com/news/earnings/tsmc-q2-profit-blows-past-estimates-on-robust-aifueled-demand-4794650
- [S30] TradingKey — https://www.tradingkey.com/analysis/stocks/more/262034508-tsmc-q2-earnings-beat-expectations-raises-full-year-outlook-tradingkey
- [S31] BiggoFinance — https://finance.biggo.com/news/US_TSM_2026-07-16
- [S32] Reuters — https://www.reuters.com/world/china/taiwan-aims-be-strategic-ai-partner-with-us-under-tariff-deal-2026-01-16/

## Hyundai — 100% da Boston Dynamics após put option do SoftBank
- O Hyundai Motor Group divulgou na quinta-feira, 16 de julho, que tornará a Boston Dynamics uma subsidiária integral ao adquirir a fatia de cerca de 10% do SoftBank Group.
- O grupo diz que a compra ajudará a implantar robótica avançada em suas operações.
- O SoftBank exerceu uma put option (direito de vender ações ordinárias) sobre sua fatia de 9,65%, conforme contrato assinado em 2020.
- Os termos do negócio não foram divulgados.
- A imprensa local reportou que a transação deve valer cerca de 500 bilhões de wons (US$335 milhões).
- Shin Yoonchul, analista da Kiwoom Securities, disse que o preço da transação implica uma avaliação de cerca de 5 trilhões de wons para a Boston Dynamics.
- A Hyundai adquiriu uma fatia de controle de 80% da Boston Dynamics do SoftBank em 2021 por cerca de 1 trilhão de wons (US$671 milhões).
- O grupo chega aos 100% cerca de cinco anos depois de completar a compra do controle.
- A estrutura atual de participação é: Hyundai Motor 28%, o presidente do grupo Euisun Chung 22,6%, Kia 17,2%, Hyundai Mobis 11,3%, Hyundai Glovis 11,25% e SoftBank 9,65%.
- A put option estava atrelada à condição de que o SoftBank poderia vender a fatia remanescente caso não ocorresse um IPO nos EUA até junho de 2026.
- A Boston Dynamics busca a comercialização do robô humanoide Atlas, com meta de produção em massa em 2028.
- O Hyundai Motor Group avalia um IPO da Boston Dynamics, incluindo uma listagem na Nasdaq americana.
- As ações da Hyundai Motor caíram mais de 30% desde que a imprensa local noticiou o plano pela primeira vez no mês passado.
- As ações da Hyundai Motor fecharam em queda de 2,1% na quinta-feira, contra queda de 6,4% do índice de referência KOSPI.
**Fontes:**
- [S33] CNA / Reuters — https://www.channelnewsasia.com/business/hyundai-motor-group-make-boston-dynamics-wholly-owned-purchase-softbank-stake-6257486
- [S34] BusinessKorea — https://www.businesskorea.co.kr/news/articleView.html?idxno=273168
- [S35] The Asia Business Daily — https://www.asiae.co.kr/en/article/2026071610132645049
- [S36] Seoul Economic Daily — https://en.sedaily.com/international/2026/06/19/hyundai-motor-group-acquires-softbanks-96-percent-stake-in

## Csquare — IPO de US$1,05 bilhão abaixo da faixa
- A Csquare precificou seu IPO (oferta pública inicial de ações) de 50 milhões de ações a US$21,00 cada.
- A empresa espera receita bruta de aproximadamente US$1,05 bilhão com a oferta, antes de descontos e comissões de subscrição.
- A receita bruta chegaria a US$1,2075 bilhão se os coordenadores exercerem integralmente a opção de lote suplementar.
- O preço de US$21 ficou abaixo da faixa divulgada de US$23 a US$27.
- O preço avalia a empresa, sediada em Dallas, em cerca de US$3,25 bilhões.
- Fundada em 2019, a Csquare possui e opera 64 data centers em 21 mercados metropolitanos na América do Norte e no Reino Unido.
- A empresa fornece serviços de colocation e conectividade a empresas, provedores de nuvem e companhias de telecomunicações.
- As ações deveriam começar a ser negociadas na Bolsa de Nova York sob o ticker "CSQR" em 16 de julho de 2026.
- A oferta deve ser fechada em 17 de julho de 2026, sujeita às condições habituais.
- A Csquare pretende usar os recursos líquidos para pagar parte de sua dívida em aberto e cobrir taxas e despesas da oferta.
- A empresa diz que o restante será destinado a fins corporativos gerais, incluindo aquisições, capital de giro e investimentos.
- A Brookfield, investidora da empresa, avaliava comprar uma parcela da oferta.
**Fontes:**
- [S37] Barchart / PR Newswire — https://www.barchart.com/story/news/3308469/csquare-inc-announces-pricing-of-initial-public-offering
- [S38] CNA / Reuters — https://www.channelnewsasia.com/business/csquare-ipo-raises-105-billion-investors-bet-ai-boom-6257181
- [S39] CNA / Bloomberg — https://www.channelnewsasia.com/business/brookfield-backed-csquare-prices-ipo-21-share-bloomberg-news-reports-6257181
- [S40] Financial Post / Bloomberg — https://financialpost.com/pmn/business-pmn/brookfield-backed-data-center-firm-raises-1-05-billion-in-ipo

## ASML — aumento de preços de máquinas e resistência da TSMC
- A ASML discutiu diretamente com a TSMC preços mais altos para seus sistemas EUV avançados (litografia ultravioleta extrema, usada para gravar os chips mais modernos).
- A ASML planeja cobrar 10% a mais por seus sistemas DUV (litografia ultravioleta profunda, geração anterior).
- A TSMC está resistindo aos planos.
- The Information noticiou os planos na quarta-feira, 15 de julho, citando quatro fontes com conhecimento das discussões.
- A ASML também planeja expansão de capacidade em meio à demanda crescente por chips de IA, segundo a reportagem do The Information.
- Um resultado trimestral acima do esperado, impulsionado por IA, encorajou a ASML a aumentar preços das máquinas de litografia — algo que a empresa raramente faz.
- O plano monta uma confrontação incomum com sua maior cliente, a TSMC.
- Para litografia de ponta, os clientes têm poucas alternativas às ferramentas da ASML.
- Analistas observam que compradores ainda podem obter concessões em termos de serviço, prazos de entrega ou descontos de pacote que mantêm o custo total de propriedade próximo ao anterior.
**Fontes:**
- [S41] The Information — https://www.theinformation.com/articles/asml-plans-price-increases-chipmaking-equipment-despite-tsmc-resistance
- [S42] Yahoo Finance — https://finance.yahoo.com/markets/stocks/articles/asml-eyes-price-increases-chip-165859035.html
- [S43] MarketScreener / MT Newswires — https://www.marketscreener.com/news/asml-to-raise-equipment-prices-taiwan-semiconductor-pushes-back-ce7f5ed2da8af225
- [S44] DigiTimes — https://www.digitimes.com/news/a20260716VL201/asml-tsmc-duv-price-chipmakers-earnings.html
- [S45] Finimize — https://finimize.com/content/asml-tests-chip-tool-pricing-power-with-a-planned-hike

## Apple — caça a aquisições de chips para servidores de IA
- The Information noticiou em 15 de julho que a Apple explora aquisições de startups de semicondutores para reforçar seus esforços de construir chips de servidor para rodar IA.
- Nos últimos meses, a Apple conversou com banqueiros sobre possíveis negócios.
- A Apple também abordou startups de semicondutores para sondar o interesse delas em se vender.
- Os servidores de IA internos da Apple rodam atualmente com chips M2 Ultra de projeto próprio e vêm sofrendo com o desempenho em cargas de trabalho exigentes.
- O chip de servidor de próxima geração da Apple, de codinome Baltra, atrasou e não estreará em 2026 como planejado.
- O Baltra é desenvolvido em colaboração com a Broadcom como processador de servidor customizado para funções de IA na nuvem.
- O Baltra é destinado a inferência de IA e seria fabricado no processo de 3nm da TSMC.
- No início deste ano, a Apple tentou rodar modelos Gemini do Google em seus servidores internos como parte de uma Siri reformulada, mas os chips baseados em Mac não deram conta do modelo grande.
- As tarefas mais exigentes da nova Siri são atendidas por um modelo baseado em Gemini rodando em GPUs da Nvidia no Google Cloud.
- A Apple raramente faz grandes aquisições: comprou a PA Semi por US$278 milhões em 2008, a Beats por US$3 bilhões e a startup de IA Q.ai por quase US$2 bilhões neste ano.
- A compra da PA Semi foi o que colocou a Apple no negócio de fazer seus próprios chips.
- A Q.ai foi a segunda maior aquisição da Apple, atrás da Beats.
- A Apple tinha US$45,6 bilhões em caixa e equivalentes no fim de março.
- Na semana passada, a Apple fechou acordo com a Broadcom para comprar US$30 bilhões em chips fabricados nos Estados Unidos.
- A Bloomberg noticiou nesta semana que um chip de servidor baseado no M7 Ultra só ficará pronto em 2029.
- A Apple deve atualizar em breve sua infraestrutura com chips M5 Ultra.
**Fontes:**
- [S46] The Information — https://www.theinformation.com/articles/apple-hunts-ai-chip-acquisitions
- [S47] 9to5Mac — https://9to5mac.com/2026/07/15/report-apple-looking-into-buying-chip-startups-to-strengthen-its-ai-infrastructure/
- [S48] Engadget — https://www.engadget.com/2215912/apple-is-reportedly-shopping-for-ai-chip-companies/
- [S49] Techzine — https://www.techzine.eu/news/infrastructure/142924/apple-considers-acquiring-server-chip-companies/

## Cadence — AuraStack, plataforma agêntica para design de placas e empacotamento
- A Cadence (Nasdaq: CDNS) apresentou em 15 de julho o AuraStack AI Super Agent no Cadence Allegro AI Studio.
- A empresa chama o AuraStack de primeira plataforma de IA agêntica do mundo para design de placas de circuito impresso (PCB) e empacotamento avançado.
- A plataforma leva projetistas do planejamento de sistema ao produto final em um único ambiente nativo de IA.
- O AuraStack é acelerado por Nvidia Blackwell e Nvidia CUDA-X.
- O AuraStack coordena agentes de IA especializados em planejamento, implementação e análise multifísica integrada, comprimindo o ciclo de projeto de sistema até a manufatura.
- Com o AuraStack, a Cadence afirma ser a única fornecedora com soluções de IA agêntica cobrindo todo o fluxo de design de sistemas eletrônicos, do design de silício digital e analógico ao empacotamento avançado e ao design de PCB.
- O AuraStack se soma aos agentes ChipStack, InnoStack e ViraStack da Cadence.
- Ashutosh Mauskar, vice-presidente corporativo de gestão de produtos e desenvolvimento de negócios da Cadence, disse que o agente entrega tempo até o mercado 2 vezes mais rápido e produtividade 15 vezes maior.
- A Nvidia relatou desempenho multifísico 20 vezes mais rápido com o AuraStack e a plataforma Millennium M2000.
- A TSMC disse que anos de colaboração com a Cadence em roteamento automático de substratos elevaram a produtividade em 100 vezes.
- Clientes iniciais incluem Nvidia, TSMC, Schneider Electric e Forvia Hella.
- A Forvia Hella afirma que o posicionamento de componentes assistido por IA reduziu uma tarefa de projeto com cerca de 300 componentes de quatro dias para aproximadamente quatro minutos.
- O AuraStack funciona como interface de linguagem natural capaz de planejar e orquestrar fluxos de trabalho de múltiplas etapas de projeto e teste de circuitos.
- Esses fluxos rodam com maior precisão usando CPUs, GPUs e outros aceleradores.
- O AuraStack se integra a uma ampla gama de modelos abertos e proprietários.
**Fontes:**
- [S50] Morningstar / Business Wire — https://www.morningstar.com/news/business-wire/20260715175854/cadence-introduces-aurastack-ai-super-agent-the-worlds-first-agentic-ai-platform-for-pcb-and-advanced-packaging
- [S51] The Register — https://www.theregister.com/ai-and-ml/2026/07/15/cadences-aurastack-agent-melds-ai-with-hpc-to-speed-pcb-advanced-packaging-design/5271465
- [S52] Forbes — https://www.forbes.com/sites/marcochiappetta/2026/07/15/cadence-expands-ai-agents-with-aurastack-for-pcb-and-advanced-chip-packaging/
- [S53] Fierce Electronics — https://www.fierceelectronics.com/ai/cadence-aurastack-debuts-boost-pcb-and-packaging-designers
- [S54] GamesBeat — https://gamesbeat.com/cadence-introduces-aurastack-ai-to-offload-tasks-so-engineers-can-design-chips/

## Irã — acordo de paz declarado nulo e ataques dos EUA em Teerã
- Os EUA intensificaram os ataques na madrugada de quinta-feira, 16 de julho, atingindo alvos mais ao norte do que nas rodadas anteriores.
- A mídia estatal iraniana reportou ataques nos arredores de Teerã.
- A mídia estatal também reportou ataques americanos na província de Semnan, onde ficam a produção de mísseis balísticos e o programa espacial do Irã.
- Forças americanas dispararam contra um navio que os EUA acusaram de tentar furar seu bloqueio naval ao Irã.
- O Irã retaliou antes do amanhecer com mísseis e drones contra aliados dos EUA na região e alertou que seus ataques podem escalar.
- Autoridades iranianas dizem que os ataques dos EUA já mataram mais de 35 pessoas e feriram mais de 300.
- Teerã afirmou que as sucessivas ondas de ataques americanos anularam o memorando de entendimento assinado em 17 de junho, que sustentava o cessar-fogo.
- O principal negociador iraniano, Mohammed Bagher Ghalibaf, disse que o Irã está "em uma guerra essencial e existencial com os Estados Unidos".
- Ghalibaf disse que o país não tem motivo para continuar cumprindo os termos do acordo de paz e que suas forças armadas têm "completa liberdade de ação".
- O IRGC (Corpo da Guarda Revolucionária Islâmica) disse na manhã de quarta-feira que atacou a Quinta Frota dos EUA no Bahrein como parte de uma "resposta esmagadora".
- O IRGC disse que também atingiu um importante centro logístico militar americano em Mina Abdullah, no Kuwait.
- Ataques dos EUA na quarta-feira mataram sete militares iranianos.
- O Exército americano conduziu ataques diurnos raros na quarta-feira, incluindo uma onda de 90 minutos, após reimpor um bloqueio naval aos portos iranianos.
- Teerã ameaçou cortar mais exportações de energia da região, dizendo que os EUA "devem se preparar para o fechamento de todos os outros corredores de exportação que beneficiam os EUA e seus aliados".
- O ISW (Institute for the Study of War) reportou que forças americanas atingiram o quartel da 388ª Brigada de Assalto Mecanizado das Forças Terrestres Artesh em Iranshahr, província de Sistão-Baluchistão.
- Os ataques teriam matado sete soldados do Artesh, ferido outros 13 e destruído vários prédios.
- A 388ª Brigada fica a cerca de 200 quilômetros da costa iraniana, uma expansão notável em relação ao padrão de ataques costeiros de julho.
- O Brent superou brevemente US$86 por barril em 15 de julho antes de recuar para US$84,93, alta de 0,2% sobre o dia anterior.
- A Guarda Revolucionária do Irã ameaçou em 15 de julho interromper todas as exportações de energia do Oriente Médio por causa do bloqueio militar americano que impede petroleiros com petróleo iraniano de usar o Estreito de Ormuz.
- O Estreito de Ormuz respondia por cerca de um quinto dos embarques globais de petróleo e gás antes da guerra.
**Fontes:**
- [S55] AP News — https://apnews.com/article/iran-us-hormuz-strait-war-july-16-2026-f98ff56554de2336f0e85bb5fdcae769
- [S56] Al Jazeera — https://www.aljazeera.com/news/2026/7/15/iran-says-peace-deal-voided-fighting-existential-war-after-us-attacks
- [S57] France 24 — https://www.france24.com/en/middle-east/20260715-us-launches-wave-of-strikes-on-iran-tehran-threatens-to-halt-regional-energy-exports
- [S58] Institute for the Study of War — https://understandingwar.org/research/middle-east/iran-update-special-report-july-15-2026/
- [S59] Transport Topics — https://www.ttnews.com/articles/oil-prices-iran-block-exports

## Uber — aquisição da Delivery Hero por €13 bilhões
- A Uber Technologies (NYSE: UBER) e uma de suas afiliadas firmaram em 16 de julho um acordo de combinação de negócios com a Delivery Hero SE (ETR: DHER).
- A Uber oferecerá aos acionistas da Delivery Hero €41,50 por ação em dinheiro.
- O preço implica um valor patrimonial totalmente diluído de €13,0 bilhões.
- O preço representa prêmio de cerca de 127% sobre o preço médio ponderado por volume (VWAP) de três meses não afetado, anterior a 8 de maio de 2026.
- O preço representa prêmio de cerca de 34% sobre o VWAP de três meses anterior ao anúncio.
- A combinação estenderia a plataforma da Uber a um total de 99 países.
- O GMV (volume bruto de mercadorias) pró-forma combinado foi de US$236 bilhões em 2025.
- A Uber adquire 50 mercados que geraram US$42 bilhões de GMV em 2025.
- Em paralelo, a firma de investimentos nova-iorquina SSW Partners concordou em comprar os negócios da Delivery Hero em 14 mercados, onde Uber Eats e Delivery Hero competem.
- Esses 14 mercados geraram €11 bilhões de GMV em 2025 e serão vendidos por cerca de €1,4 bilhão.
- A venda à SSW Partners está condicionada à conclusão da oferta da Uber e a outras condições habituais.
- A Uber prometeu manter a sede da Delivery Hero em Berlim e não fazer mudanças em sua força de trabalho na cidade até pelo menos 2029.
- A Uber se comprometeu a empregar esforços comercialmente razoáveis para investir €2 bilhões na Alemanha até 2031.
- A oferta exige aceitação mínima de 50% das ações mais uma.
- A Uber já recebeu compromissos irrevogáveis de adesão à oferta equivalentes a 16,68%.
- Somados à participação de 24,77% e a instrumentos de 11,74%, o interesse econômico total da Uber passaria de 53%.
- A conclusão da oferta é esperada para o segundo semestre de 2027.
- O negócio avalia a Delivery Hero em cerca de US$14,8 bilhões.
- A oferta anterior da Uber, em maio, era de €33 por ação.
**Fontes:**
- [S60] Delivery Hero — https://www.deliveryhero.com/newsroom/delivery-hero-and-uber-to-join-forces-to-deliver-more-for-customers-vendors-and-riders/
- [S61] Uber Investor Relations — https://investor.uber.com/news-events/news/press-release-details/2026/Uber-Announces-Acquisition-Offer-for-Delivery-Hero/default.aspx
- [S62] The Next Web — https://thenextweb.com/news/uber-delivery-hero-agreed-takeover-41-50
- [S63] Bloomberg — https://www.bloomberg.com/news/articles/2026-07-16/uber-agrees-to-buy-delivery-hero-as-food-sector-consolidates

## União Europeia e Ucrânia — acordo de drones e mísseis em Kiev
- A presidente da Comissão Europeia, Ursula von der Leyen, visitou Kiev e anunciou um novo "acordo de drones" entre a Ucrânia e a União Europeia.
- O anúncio ocorreu em cerimônia que marcava o Dia da Condição de Estado da Ucrânia.
- O acordo busca combinar a experiência de campo de batalha de Kiev com a capacidade industrial da UE para estabelecer projetos conjuntos e ampliar rapidamente a produção.
- Von der Leyen disse que o acordo vai "unir a engenhosidade ucraniana e a escala industrial da Europa".
- Von der Leyen disse que o acordo oferece a Kiev "enorme capacidade tecnológica e industrial" ao lado de "locais de produção seguros e protegidos".
- Mísseis balísticos russos atingiram vários distritos de Kiev nas primeiras horas de quinta-feira, 16 de julho.
- O prefeito Vitali Klitschko informou que duas pessoas foram mortas nos ataques e seis moradores ficaram feridos, incluindo um garoto de 16 anos.
- O ataque ocorreu horas depois da visita de von der Leyen a Kiev.
- O Exército ucraniano disse ter atingido durante a noite seis petroleiros russos e dois rebocadores no Mar Negro e no Mar de Azov.
- O estado-maior ucraniano afirmou que os petroleiros transportavam petróleo e derivados russos burlando sanções internacionais, além de combustível para as forças de Moscou.
- O primeiro-ministro britânico de saída, Keir Starmer, chegou a Kiev na quinta-feira para se encontrar com Volodymyr Zelensky, em viagem de alta segurança antes de deixar o cargo.
- Starmer deve assegurar a Zelensky que o compromisso britânico de apoiar a Ucrânia continuará depois que ele for sucedido por Andy Burnham.
- O Ministério da Defesa da Rússia afirmou na quinta-feira ter atingido instalações militares e industriais em Kiev.
- O ISW reportou que forças russas retomaram uma campanha de ataques contra a infraestrutura portuária ucraniana no Mar Negro.
- Bohdan Kostetskyi, sócio operacional da consultoria agrícola Barva Invest, afirmou em 15 de julho que os ataques russos recentes contra portos ucranianos praticamente pararam as exportações de grãos em águas profundas.
**Fontes:**
- [S64] Al Jazeera — https://www.aljazeera.com/news/2026/7/16/kyiv-under-fire-from-russian-missiles-after-eu-ukraine-sign-drone-deal
- [S65] The Independent — https://www.independent.co.uk/news/world/europe/ukraine-russia-war-live-putin-zelensky-ballistic-missile-strikes-b3015875.html
- [S66] Institute for the Study of War — https://understandingwar.org/research/russia-ukraine/russian-offensive-campaign-assessment-july-15-2026/

## AST SpaceMobile — serviço adiado para 2027 e captação de US$1 bilhão
- Em documento entregue à bolsa em 15 de julho, a AST SpaceMobile disse que sua campanha de lançamentos mira cerca de 45 satélites BlueBird no início de 2027.
- A empresa, sediada no Texas, perde assim sua meta de serviço comercial no fim de 2026.
- No documento, a empresa escreve que a projeção se baseia em "suas expectativas atuais quanto à disponibilidade de lançamento".
- A AST contava com a Blue Origin para lançar e operar 45 satélites BlueBird até o fim deste ano, o que lhe permitiria atender as parceiras AT&T e Verizon.
- O foguete New Glenn, da Blue Origin, explodiu na plataforma de lançamento na Flórida.
- No mesmo dia, a AST anunciou uma oferta privada de US$1 bilhão em notas seniores conversíveis com vencimento em 1º de fevereiro de 2034.
- A oferta tem opção de adicionar outros US$150 milhões.
- As notas podem ser convertidas em dinheiro, ações Classe A ou uma combinação das duas.
- As notas têm taxa de juros anual de 1,625% e preço inicial de conversão de cerca de US$79,57 por ação.
- O preço de conversão representa prêmio de 20% sobre o fechamento de 15 de julho, de US$66,31.
- A empresa também firmou operações de capped call com preço-teto inicial de US$149,20 por ação, para reduzir a diluição potencial em caso de conversão.
- O caixa preliminar era de US$2,723 bilhões em 30 de junho, contra US$3,459 bilhões em 31 de março — queda de cerca de US$736 milhões, ou 21%.
- A AST disse que os recursos podem financiar parcerias e/ou aquisições para verticalizar seu negócio e "mitigar riscos associados a provedores de lançamento terceirizados".
- A empresa também quer garantir acesso adicional à órbita para sua rede de banda larga celular baseada no espaço.
- As ações caíram para US$58,03 no after-hours, com investidores avaliando a diluição.
**Fontes:**
- [S67] PCMag — https://www.pcmag.com/news/ast-spacemobile-delays-service-launch-to-2027-eyes-acquisitions
- [S68] Stock Titan — https://www.stocktitan.net/sec-filings/ASTS/8-k-ast-space-mobile-inc-reports-material-event-d73bdb8682f3.html
- [S69] TS2 — https://ts2.tech/en/ast-spacemobile-nasdaqasts-looks-to-raise-1-billion-with-convertible-cash-down-21/
- [S70] FX Leaders — https://www.fxleaders.com/news/2026/07/16/asts-stock-slides-toward-58-after-1b-convertible-deal-revives-dilution-fears/
- [S71] SpaceNews — https://spacenews.com/ast-spacemobile-sees-new-glenn-setback-delaying-initial-commercial-service-into-2027/

## SpaceX — ação abaixo do preço de IPO pela primeira vez
- As ações da SpaceX caíram pela quarta sessão seguida na quarta-feira, 15 de julho.
- As ações caíram brevemente abaixo do preço de IPO de US$135 pela primeira vez.
- A ação recuou cerca de 1% na quarta-feira e fechou a US$135,27.
- A SPCX abriu a US$137,51, marcou mínima de US$132,15 e máxima de US$139,34, fechando a US$135,27 com volume de 57,57 milhões de ações.
- O IPO de 12 de junho levantou quase US$86 bilhões, um recorde.
- O IPO fez de Elon Musk o primeiro trilionário do mundo.
- A ação subiu inicialmente acima de US$200 nos dias após a abertura de capital, dando à empresa por um breve período uma avaliação rival à de gigantes como Amazon e Microsoft.
- Desde aquele pico, a ação perdeu valor praticamente toda semana.
- A ação caiu mais de 30% em relação às máximas de cerca de US$225.
- A reversão reflete em parte a preocupação de investidores com gastos em IA financiados por dívida e com o efeito de possíveis altas de juros do Federal Reserve sobre avaliações esticadas de tecnologia.
- A SpaceX recorreu ao mercado de títulos em junho para levantar US$25 bilhões e construir infraestrutura de tecnologia.
- O primeiro balanço da SpaceX após a listagem é esperado por analistas para a primeira semana de agosto.
- A SpaceX entrou no Nasdaq-100 na semana passada, o que trouxe investidores passivos à ação por meio de fundos de índice.
- A entrada foi possível por uma mudança recente de regra que encurtou o período de elegibilidade para 15 pregões no caso de empresas recém-abertas.
- A SpaceX prepara o 13º voo de teste do sistema Starship, com janela de 90 minutos abrindo às 18h45 (horário do leste dos EUA) de quinta-feira.
- O voo levará ao espaço, pela primeira vez, os satélites Starlink V3 de próxima geração.
**Fontes:**
- [S72] CNBC — https://www.cnbc.com/2026/07/15/spacex-spcx-stock-ipo-price.html
- [S73] TechCrunch — https://techcrunch.com/2026/07/15/spacex-slips-below-its-135-ipo-price-ahead-of-starship-launch/
- [S74] The Straits Times — https://www.straitstimes.com/business/companies-markets/spacex-shares-slide-below-ipo-price-for-the-first-time-as-blistering-rally-unravels
- [S75] Benzinga — https://www.benzinga.com/trading-ideas/movers/26/07/60481036/spacex-spcx-stock-falls-below-135-ipo-price
- [S76] Exa Markets — https://exa.ai/library/markets/stock/SPCX?date=2026-07-15&t=6a58d2110880b00ef466c913

## Federal Reserve — inflação perto de 4% e juros parados
- O Federal Reserve divulgou em 15 de julho seu Beige Book de julho de 2026.
- O relatório aponta que as vendas no varejo melhoraram e o setor imobiliário ficou misto.
- O relatório aponta que o emprego se fortaleceu e as pressões salariais aumentaram.
- As perspectivas relatadas eram de estáveis a positivas.
- Em discurso em Nova York em 15 de julho, o presidente do Fed de Nova York, John Williams, disse que a inflação geral está "inquestionavelmente alta demais, em cerca de 4 por cento".
- O patamar está bem acima da meta de longo prazo de 2% do FOMC.
- Williams disse que "a atual postura da política monetária está bem posicionada" para restaurar a meta.
- Williams disse que "o crescimento da economia é sólido e dentro da tendência, e o mercado de trabalho é igualmente sólido e estável".
- Williams espera crescimento do PIB real em torno de 2% a 2,25% neste ano e nos próximos dois anos.
- Williams espera que a taxa de desemprego caia muito gradualmente para 4% em 2028.
- Williams espera que a inflação geral caia para cerca de 3,25% até o fim do ano, siga em direção à meta de 2% em 2027 e a atinja em 2028.
- A diretora do Fed Lisa Cook disse em 15 de julho que os riscos "continuam fortemente inclinados para uma inflação mais alta".
- Cook disse que votou com o restante do FOMC para manter os juros estáveis no mês passado.
- Cook apoiou a decisão porque os dois principais fatores que pressionaram a inflação no último ano — tarifas e o conflito no Oriente Médio — deveriam, em tese, produzir apenas altas de inflação de curta duração.
- Cook disse que a "construção de data centers adicionou algum calor à economia".
- Cook observou que o crescimento do PIB em 2025 veio em 2,0% e que participantes do FOMC agora projetam 2,2% para 2026.
- Ambas as leituras superam as projeções do ano passado em cerca de meio ponto percentual.
- A produtividade do trabalho cresceu cerca de 2,5% ao ano nos últimos dois anos, segundo Cook.
- O FOMC volta a se reunir em duas semanas.
- Na reunião de 17 de junho, o FOMC manteve a faixa-alvo da taxa dos fundos federais em 3,5% a 3,75%.
**Fontes:**
- [S77] Federal Reserve — https://www.federalreserve.gov/monetarypolicy/files/BeigeBook_20260715.pdf
- [S78] Federal Reserve — https://www.federalreserve.gov/monetarypolicy/beigebook202607.htm
- [S79] Federal Reserve Bank of New York — https://tellerwindow.newyorkfed.org/2026/07/15/key-takeaways-from-president-williamss-speech-on-the-economic-outlook-and-monetary-policy-27/
- [S80] Federal Reserve Board — https://www.federalreserve.gov/newsevents/speech/cook20260715a.htm
- [S81] Federal Reserve — https://www.federalreserve.gov/newsevents/pressreleases/monetary20260617a.htm

## Alpaca — captação de US$435 milhões e entrada em prime brokerage
- A Alpaca anunciou em 16 de julho uma captação de US$135 milhões em equity liderada pela Peak XV, com participação relevante da Elefund.
- O novo financiamento totaliza US$435 milhões, incluindo dívida vinda principalmente da Payward, controladora da plataforma de ativos digitais Kraken, e do BMO.
- A Alpaca levantou US$135 milhões em equity e US$300 milhões em dívida.
- A rodada segue a Série D de US$150 milhões anunciada em janeiro de 2026, que avaliou a empresa em US$1,15 bilhão.
- A Alpaca afirma ter dobrado a receita ano a ano por três anos consecutivos.
- A Alpaca ultrapassou US$1,5 bilhão em ativos sob custódia nas ações que lastreiam ações tokenizadas.
- Os usuários ativos mensais da API cresceram quase 4 vezes nos últimos seis meses, à medida que a Alpaca expandiu capacidades de IA agêntica.
- A Alpaca usará o financiamento para acelerar sua infraestrutura de corretagem agent-first e de prime brokerage API-first.
- A infraestrutura permite que empresas financeiras e clientes institucionais construam e escalem produtos de investimento em mercados tradicionais e onchain.
- Yoshi Yokokawa, cofundador e CEO da Alpaca, disse que a empresa está "posicionada de forma única para se tornar a camada de infraestrutura padrão para os mercados de capitais globais tokenizados e os serviços financeiros nativos de IA".
- A Alpaca adquiriu uma corretora e prestadora de serviços de pagamento regulada pela IFSCA em GIFT City, estabelecendo presença regulada na Índia.
- A Alpaca adquiriu entidades reguladas no Reino Unido e na Europa e completou o passporting nos 30 países do Espaço Econômico Europeu.
- A Alpaca hoje suporta mais de 10 milhões de contas de corretagem em centenas de fintechs e instituições em mais de 40 países, com US$400 milhões em financiamento acumulado.
- A Alpaca avalia entrar no negócio de prime broking com a captação de US$435 milhões.
**Fontes:**
- [S82] Business Wire via Las Vegas Sun — https://lasvegassun.com/news/2026/jul/16/alpaca-raises-135-million-to-scale-agent-first-bro/
- [S83] Bloomberg — https://www.bloomberg.com/news/articles/2026-07-16/broker-alpaca-raises-435-million-explores-prime-broking-entry
- [S84] Fortune — https://fortune.com/2026/01/14/alpaca-fundraise-series-d-brokerage-infrastructure/
