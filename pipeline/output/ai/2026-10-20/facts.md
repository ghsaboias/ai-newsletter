# Fatos — Newsletter [Tech] 20 de Outubro de 2026

## DeepSeek — código aberto do DeepInfer, seu sistema de inferência
- Em 20 de outubro de 2026, a DeepSeek abriu o código do DeepInfer, seu framework próprio de inferência (a execução de um modelo já treinado para gerar respostas).
- O DeepInfer é o sistema que roda o DeepSeek-V4.1-Flash em escala.
- A DeepSeek disse que a abertura pretende ajudar a comunidade a reduzir custos de poder computacional e consumo de energia.
- A DeepSeek disse que o objetivo também é tornar a IA mais acessível em preço.
- O DeepInfer foi publicado sob a licença Apache 2.0.
- O DeepInfer suporta GPUs NVIDIA SM100.
- O DeepInfer suporta NPUs Huawei Ascend 950.
- Os recursos incluem kernels otimizados (FlashMLA, DeepGEMM, DeepEP).
- Os recursos incluem paralelismo de especialistas para modelos MoE (mixture of experts, arquitetura que ativa só parte do modelo a cada token).
- Os recursos incluem decodificação especulativa com tokens de rascunho.
- Os recursos incluem SWA bounded replay, inferência invariante ao tamanho do lote (batch-invariant), amostragem determinística e saídas estruturadas.
- A versão publicada não inclui um sistema de KV cache (memória das chaves e valores de atenção já calculados).
- A versão publicada não inclui a separação entre as fases de prefill e decode.
- A versão publicada não inclui balanceamento de carga entre réplicas.
- Por isso, o DeepInfer publicado não é um sistema completo de serviço de inferência.
- A DeepSeek disse que o código de inferência de seus modelos futuros também será publicado no DeepInfer.
- A DeepSeek abriu separadamente o código do deepseek-recipe, o componente de codificação e decodificação de tokens que usa em produção, alinhado com a API oficial.
- A Bloomberg descreveu o lançamento como algo que pode tornar a tecnologia da DeepSeek mais barata e mais fácil de rodar para empresas.
**Fontes:**
- [S1] X — https://x.com/deepseek_ai/status/2112476496283775135
- [S2] X — https://x.com/deepseek_ai/status/2112476498598957056
- [S3] GitHub — https://github.com/deepseek-ai/DeepInfer
- [S4] Bloomberg — https://www.bloomberg.com/news/articles/2026-10-20/deepseek-unveils-open-source-tool-to-help-cut-ai-operating-costs

## Inception — Mercury 3, LLM de difusão acima de 1.000 tokens por segundo
- Em 19 de outubro de 2026, a Inception lançou o Mercury 3.
- O CEO da Inception, Stefano Ermon, chamou o Mercury 3 de "o LLM de difusão mais inteligente já lançado".
- A Inception afirma que o Mercury 3 supera o GPT-6 Luna e o Claude Haiku 5.5 em qualidade.
- O Mercury 3 roda a mais de 1.000 tokens por segundo.
- Modelos autorregressivos geram um token por vez; o Mercury 3 gera e refina vários tokens em paralelo.
- A Inception afirma que o Mercury 3 é de 4 a 8 vezes mais rápido que o Haiku 5.5, o GPT-6 Luna e o GLM-5.3 Flash.
- A Inception afirma que o Mercury 3 supera esses três modelos em benchmarks agênticos.
- Na tabela de benchmarks divulgada pela própria Inception, o Mercury 3 lidera contra o GPT-6 Luna e o Haiku 5.5 em 8 de 12 testes.
- No SWE-Bench Atlas, o Mercury 3 marcou 51,08, contra 33,33 e 32,26 dos rivais.
- No DeepSWE v1, o Mercury 3 marcou 46,31, abaixo dos 51,62 do Haiku 5.5.
- O Mercury 3 tem janela de contexto de 1 milhão de tokens.
- O Mercury 3 tem mais de 40 vezes os parâmetros do Mercury 1.
- A Inception não divulgou o número de parâmetros.
- O preço de lançamento é US$0,10 por milhão de tokens de input e US$0,35 por milhão de tokens de output.
- O preço de lançamento tem 50% de desconto sobre o preço de tabela de US$0,20 (input) e US$0,70 (output) por milhão de tokens.
- A Inception disse que usou enxames de agentes Mercury 3 para autoaperfeiçoamento recursivo.
- Segundo a Inception, esses agentes aumentaram a velocidade geral do modelo em 16%, além das melhorias feitas pela equipe.
- O Mercury 3 está disponível pela API da Inception, OpenRouter, Baseten e Vercel.
- O Mercury 3 é oferecido só por API, sem pesos abertos.
**Fontes:**
- [S5] The Deep View — https://www.thedeepview.com/articles/why-inception-s-mercury-3-upends-ai-economics
- [S6] MarkTechPost — https://www.marktechpost.com/2026/10/19/inception-mercury-3-diffusion-llm/

## OpenAI — salto em COBOL, Fortran e Visual Basic
- Em 19 de outubro de 2026, a OpenAI disse que seus modelos mais recentes têm capacidades maiores para criar e migrar software em linguagens de programação com poucos dados de treino, como COBOL, Fortran e Visual Basic.
- A OpenAI disse que essas linguagens sustentam software do qual bancos, governos e empresas dependem.
- O MultiLangBench, novo benchmark da OpenAI, pede ao modelo que construa um motor de banco de dados compatível com SQLite em 20 linguagens.
- No MultiLangBench, o GPT-6 Astra teve taxa média de aprovação nos testes de 87,4%.
- O GPT-5.6 Sol teve 26,8% no MultiLangBench.
- Em COBOL, a taxa subiu de 10,9% para 72,1%.
- Num teste de migração de COBOL para C++, Java, Kotlin, Python ou Rust, a saída precisava ser idêntica byte a byte.
- Nesse teste, o GPT-6.1 Sol marcou 86,6% com baixo esforço de raciocínio, contra 5,4% do GPT-5.6 Sol.
- Segundo The Circuitry, o GPT-6.1 Sol obteve esse resultado a 61% do custo de API do GPT-5.6 Sol.
- Com esforço de raciocínio maior, o GPT-6.1 Sol chegou a 97,9%.
- O GPT-6 Luna atingiu 40,3% no MultiLangBench a um custo estimado de US$0,77 por amostra.
- O custo do GPT-6 Luna é cerca de 78% menor que os US$3,48 por amostra do GPT-5.6 Sol.
- A OpenAI cita que o COBOL sustenta mais de 40% dos sistemas de internet banking.
- A OpenAI cita que o COBOL sustenta 80% das transações presenciais com cartão de crédito.
- A OpenAI cita que o COBOL sustenta 95% das transações em caixas eletrônicos.
- A OpenAI está publicando o MultiLangBench no GitHub.
- A OpenAI diz que migrações em produção ainda exigem revisão de especialistas.
**Fontes:**
- [S7] X — https://x.com/OpenAI/status/2112310345863930168
- [S8] MediaRelease.co (OpenAI release) — https://mediarelease.co/us/mr02096-openai-advancing-coding-low-resource-programming-languages-19102026.html
- [S9] Engadget — https://www.engadget.com/2291457/openai-says-its-models-can-translate-cobol/
- [S10] The Circuitry — https://thecircuitry.to/article/openai-models-improve-coding-for-cobol-fortran-and-other-low-resource-languages-mvfw28o8

## DHS — ordem para remover a DeepSeek dos sistemas federais civis
- Em 19 de outubro de 2026, o DHS (Departamento de Segurança Interna dos EUA) tornou pública uma ordem que exige que agências federais civis removam a tecnologia da DeepSeek de seus sistemas de TI.
- A ordem proíbe compras futuras de produtos e serviços da DeepSeek.
- A ordem foi emitida com base no Federal Acquisition Supply Chain Security Act de 2018.
- A ordem também abrange afiliadas da DeepSeek.
- A ordem também abrange produtos e serviços de terceiros desenvolvidos com implementações da DeepSeek.
- A ordem foi emitida originalmente em 24 de julho.
- A ordem se aplica a agências civis, incluindo os departamentos do Tesouro, de Estado e de Justiça.
- A ordem exclui o Departamento de Defesa.
- As agências podem pedir exceções em até 60 dias.
- O DHS disse que os modelos da DeepSeek apresentam "múltiplos vetores de ameaça".
- O DHS disse que o uso "pode resultar na transferência de dados sensíveis para a RPC" (República Popular da China) se feito por funcionários ou fornecedores do governo americano.
- O DHS disse que os modelos podem conter malware ou vulnerabilidades de segurança.
- Agências americanas, incluindo o Departamento de Comércio e a Marinha, já haviam restringido a DeepSeek em dispositivos do governo.
- Estados como Nova York, Tennessee e Virgínia já haviam tomado medidas semelhantes.
**Fontes:**
- [S11] Wall Street Journal — https://www.wsj.com/tech/ai/dhs-orders-deepseek-technology-removed-from-federal-civilian-it-systems-060b6d3d
- [S12] Federal Register — https://www.federalregister.gov/documents/2026/10/20/2026-21447/notice-of-order-regarding-exclusion-and-removal-of-deepseek-products-from-federal-civilian-executive
- [S13] CNBC — https://www.cnbc.com/2026/10/20/us-deepseek-federal-agency-ban.html
- [S14] The Hindu BusinessLine (Reuters) — https://www.thehindubusinessline.com/info-tech/us-orders-removal-of-deepseek-from-civilian-government-it-systems/article71603248.ece

## OpenAI — corrida para fechar rodada de ~US$30 bilhões antes do IPO da Anthropic
- A OpenAI corre para garantir compromissos de investidores antes do IPO (oferta pública inicial de ações) da Anthropic, esperado para meados de novembro, segundo a Reuters em 19 de outubro de 2026, citando fontes.
- A rodada é de cerca de US$30 bilhões.
- A rodada pode dar à OpenAI um valuation acima de US$1,4 trilhão.
- SoftBank, o fundo MGX, de Abu Dhabi, e outros investidores atuais negociam participação na rodada.
- A OpenAI diz a investidores que chegou a US$50 bilhões em receita anualizada após o lançamento do GPT-6 Astra.
- A OpenAI diz esperar US$70 bilhões em receita anualizada até o fim do ano.
- A OpenAI cortou preços de seus modelos mais baratos, o que, segundo ela, aumentou o uso.
- A OpenAI disse a investidores que pode baixar ainda mais os preços.
- A OpenAI quer fechar a rodada antes que as divulgações financeiras da Anthropic permitam comparações lado a lado entre as duas empresas.
- A OpenAI acusa a Anthropic de inflar a receita ao contabilizar o valor bruto de contratos revendidos por provedores de nuvem.
- A Anthropic nega e diz seguir práticas contábeis estabelecidas.
- O último valuation da OpenAI foi de US$852 bilhões, em março, após uma rodada de US$122 bilhões.
- A receita da Anthropic no terceiro trimestre subiu para US$16,8 bilhões, contra US$11,6 bilhões no segundo trimestre.
- A Anthropic busca um valuation de US$2 trilhões no IPO.
- Alguns investidores defendem um valuation de cerca de US$1,5 trilhão para o IPO da Anthropic.
**Fontes:**
- [S15] Moneycontrol (Reuters) — https://www.moneycontrol.com/artificial-intelligence/openai-seeks-to-accelerate-fundraising-ahead-of-anthropic-ipo-report-article-14055784.html
- [S16] CNBC TV18 (Reuters) — https://www.cnbctv18.com/technology/openai-seeks-to-accelerate-fundraising-ahead-of-anthropic-ipo-report-20015427.htm
- [S17] Quartz — https://qz.com/openai-30-billion-funding-round-anthropic-ipo-102026

## Startups de aplicações de IA — rodadas de Arda, Otter.ai e Town
- A Arda, startup de IA para manufatura de Bob McGrew, ex-chefe de pesquisa da OpenAI, captou US$230 milhões a um valuation de US$1,5 bilhão.
- A rodada da Arda foi liderada por Altimeter Capital, Accel e Khosla Ventures.
- A Arda anunciou a captação à CNBC em 20 de outubro de 2026.
- McGrew descreveu a Arda como "uma interface e um agente que fazem pelos engenheiros de manufatura o que o Claude ou o Cursor fazem pelos programadores".
- Os modelos da Arda já estão em uso na empresa de defesa Anduril.
- Em março de 2026, a Arda buscava US$70 milhões a um valuation de US$700 milhões.
- O valuation da Arda mais que dobrou em cerca de sete meses.
- A Otter.ai, que faz anotações automáticas de reuniões, captou US$320 milhões do Customer Value Fund da General Catalyst.
- O capital é não dilutivo (não reduz a participação dos sócios atuais).
- Antes dessa rodada, a Otter.ai havia captado US$50 milhões no total.
- A Otter.ai diz que 40 milhões de pessoas já usaram seu produto, contra 25 milhões no ano passado.
- A Town, startup de assistentes de IA para empresas, foi fundada por Jean-Denis Greze, ex-CTO da Plaid.
- A Town captou uma Série B de US$108 milhões a um valuation de US$1 bilhão.
- A Série B da Town foi co-liderada por Forerunner Ventures e Menlo Ventures.
- A rodada veio quatro meses após o lançamento público da Town.
- A Town dá a cada funcionário um assistente de IA, chamado "Townie", conectado a email, agenda e sistemas de trabalho.
- Os Townies podem conversar entre si.
- A Town captou pelo menos US$160 milhões até agora.
**Fontes:**
- [S18] CNBC — https://www.cnbc.com/2026/10/20/ex-openai-executive-builds-1point5-billion-ai-manufacturing-startup-arda.html
- [S19] Crypto Briefing — https://cryptobriefing.com/arda-raises-230-million-ai-manufacturing/
- [S20] TechCrunch — https://techcrunch.com/2026/10/20/otter-ai-raises-320-million-from-general-catalysts-growth-fund-for-its-meeting-tool/
- [S21] TechCrunch — https://techcrunch.com/2026/10/19/ai-assistant-startup-town-nabs-unicorn-valuation-four-months-after-launch/

## Anthropic — críticas ao rascunho de projeto de lei federal de IA
- O Politico publicou na sexta-feira, 16 de outubro, um rascunho de projeto de lei federal de IA que a Anthropic vinha circulando entre parlamentares.
- Defensores de segurança em IA criticaram amplamente o rascunho.
- Os críticos consideram o texto mais fraco que o FRONTIER Act, projeto bipartidário dos deputados Obernolte e Trahan.
- A publicação Transformer divulgou uma análise do rascunho em 19 de outubro.
- O rascunho exige que avaliadores independentes analisem os riscos catastróficos dos modelos e práticas das empresas de IA.
- O rascunho não estabelece padrões nem licenciamento para esses avaliadores, que podem se autocertificar.
- Para bloquear um modelo perigoso, o Departamento de Comércio teria de recorrer a um tribunal federal.
- O tribunal decidiria "sem deferência" à avaliação do governo.
- O tribunal teria de considerar o dano que a ordem de bloqueio causaria ao desenvolvedor, aos usuários e ao público.
- O projeto se sobreporia a leis estaduais sobre IA de fronteira, como a SB 53 da Califórnia e o RAISE Act de Nova York.
- O projeto preserva explicitamente leis de proteção infantil.
- Em 19 de outubro, o chefe de assuntos federais da Anthropic, Anthony Cimino, disse que o texto era um rascunho inicial.
- Cimino disse que o projeto não isenta as empresas de responsabilidade quando causam danos.
- Cimino disse que a Anthropic quer trabalhar com formuladores de políticas para tornar o texto "o mais forte possível".
- Cimino havia dito antes que a linguagem sobre a precedência sobre leis estaduais seria ajustada.
**Fontes:**
- [S22] Transformer — https://www.transformernews.ai/p/anthropic-leaked-ai-bill-undermines-safety-first-approach
- [S23] X — https://x.com/ajcimino/status/2112250250043732269

## ByteDance, Alibaba e Tencent — pedidos de mais de US$35 bilhões em placas Nvidia RTX PRO 5500
- ByteDance, Alibaba e Tencent encomendaram mais de 3 milhões de placas Nvidia RTX PRO 5500, segundo duas fontes citadas pela Reuters em 20 de outubro.
- O preço de tabela somado dos pedidos passa de US$35 bilhões.
- A RTX PRO 5500 é menos potente, mas pode ser exportada para a China dentro das restrições americanas.
- A Nvidia disse a clientes e parceiros que não pode garantir o atendimento dos pedidos.
- Uma fonte disse que parceiros podem receber só de 5% a 10% das quantidades pedidas.
- Outra fonte disse que a Nvidia pode produzir no máximo 3 milhões de placas RTX PRO 5500 no mundo todo em 2027.
- Os pedidos totais de clientes na China passaram de 6 milhões de unidades.
- Cada placa custa cerca de US$11.400.
- A RTX PRO 5500 é um chip para estações de trabalho, menos potente que o H200 e o B300.
- Os compradores chineses querem a placa principalmente para inferência de IA.
- O B300, da arquitetura Blackwell, não pode ser vendido a compradores chineses pelas regras de controle de exportação dos EUA.
- As exportações do H200, da arquitetura Hopper, são analisadas caso a caso e dependem de licença.
- A partir de 2027, a Nvidia deve dedicar boa parte de sua capacidade na TSMC (fabricante taiwanesa de chips) à plataforma de data centers Rubin.
- A Nvidia disse aos clientes que as primeiras amostras da RTX PRO 5500 chegam em dezembro.
- As entregas comerciais começam no primeiro trimestre de 2027.
- Um porta-voz da Nvidia disse que empresas americanas seguem limitadas por "controles de exportação americanos defasados, que cobrem produtos de games lançados há quase meia década, e pelo próprio limite da China às importações dos EUA".
**Fontes:**
- [S24] Reuters (via Euronext) — https://live.euronext.com/en/financial-news/exclusive-bytedance-alibaba-tencent-place-over-35-billion-worth-nvidia-chip-orders
- [S25] The Economic Times (Reuters) — https://economictimes.indiatimes.com/tech/technology/bytedance-alibaba-tencent-place-over-35-billion-worth-of-nvidia-chip-orders/articleshow/135066129.cms
- [S26] The Verge — https://www.theverge.com/tech/1014223/nvidia-cant-fulfill-chinas-35-billion-chip-demands

## Nscale — negociação de segundo contrato de ~US$45 bilhões com a Anthropic
- A Nscale, empresa de infraestrutura de nuvem para IA, negocia vender poder computacional à Anthropic num contrato de cerca de US$45 bilhões, segundo a Bloomberg em 19 de outubro, citando fontes.
- O acordo pode ser fechado em dias, mas os termos ainda podem mudar.
- O contrato cobriria um segundo prédio do campus Monarch, da Nscale, na Virgínia Ocidental.
- O segundo prédio entregaria 460 MW de capacidade com chips Nvidia Vera Rubin.
- A Anthropic também teria direito de preferência sobre um terceiro prédio do campus.
- Segundo o pedido de IPO da Nscale, a Anthropic já tem acordos de infraestrutura com a Nscale de até US$44,6 bilhões.
- O primeiro contrato, assinado em agosto, é um arrendamento de seis anos e 460 MW no mesmo campus.
- As entregas do primeiro contrato começam no fim de 2027.
- A Nscale busca um valuation de cerca de US$30 bilhões no IPO planejado.
- Alguns investidores disseram aos bancos que um valuation de US$16 bilhões a US$19 bilhões atrairia mais compradores.
- A Nscale teve prejuízo líquido de US$1 bilhão sobre receita de US$141 milhões no primeiro semestre de 2026.
- O prospecto de IPO de setembro informou que a Nscale não tinha compromissos firmes para o financiamento da construção do primeiro site da Anthropic.
- No novo arranjo, a Anthropic compraria capacidade computacional em vez de arrendar a instalação.
- A Nscale seria dona e operadora do data center e dos chips.
**Fontes:**
- [S27] Investing.com — https://www.investing.com/news/stock-market-news/nscale-in-talks-for-45-billion-anthropic-ai-deal-as-ipo-looms-4958181
- [S28] Mint — https://www.livemint.com/companies/news/anthropic-eyes-second-45-billion-nscale-deal-as-460mw-ai-data-centre-plans-advance-ahead-of-potential-ipo-11792466448988.html
- [S29] AI Weekly — https://aiweekly.co/alerts/nscale-anthropic-in-talks-for-second-45b-west-virginia-deal

## Elice — queda de 33% na estreia no Kosdaq
- A Elice, empresa sul-coreana de infraestrutura de nuvem para IA, estreou no Kosdaq (mercado de ações de empresas de tecnologia e crescimento da Coreia do Sul) em 20 de outubro.
- A ação fechou o primeiro dia a 60.500 wons (cerca de US$45,5), queda de 33,15% sobre o preço do IPO, de 90.500 wons (cerca de US$68,0).
- Durante o pregão, a ação chegou a 56.500 wons (cerca de US$42,4).
- O IPO levantou 201 bilhões de wons (US$151 milhões).
- O preço do IPO ficou no topo da faixa indicativa.
- A parcela para investidores de varejo teve demanda 400 vezes maior que a oferta.
- Foi o maior IPO do Kosdaq em 2026.
- Pelos dados da Bloomberg, é a pior estreia já registrada para um IPO coreano que levantou ao menos US$100 milhões.
- O recorde anterior era a queda de 30% da W-Scope Chungju Plant em 2022.
- A Elice foi fundada em 2015 por três doutorandos do KAIST (instituto de ciência e tecnologia da Coreia do Sul) como plataforma de ensino de programação.
- A Elice mudou de foco para infraestrutura de nuvem para IA.
- A Elice construiu uma plataforma modular de data centers com energia de alta densidade e refrigeração líquida.
- A receita do primeiro semestre subiu 200%, para 34,4 bilhões de wons (cerca de US$25,8 milhões).
- O IPO avaliou a Elice em cerca de US$755 milhões.
- O índice KOSPI caiu quase 4% no mesmo dia, para 5.552 pontos.
- A SK Hynix caiu cerca de 4% e a Samsung Electronics, cerca de 3%.
- A Reuters comparou o mercado sul-coreano a um "canário na mina de carvão" do boom de investimentos em IA.
- A Bloomberg registrou que a australiana Permagrid desistiu de seu IPO.
- A operadora de data centers AirTrunk está adiando seus planos de abrir capital.
**Fontes:**
- [S30] The Business Times (Bloomberg) — https://www.businesstimes.com.sg/companies-markets/data-centre-infrastructure-firm-elices-33-plunge-ugly-debut-rekindles-ai-spending-doubts
- [S31] Edaily — https://en.edaily.co.kr/news/eda202610205606/
- [S32] SiliconReport — https://www.siliconreport.com/elice-drops-over-30-on-seoul-market-debut

## Eka Robotics — Série A de US$150 milhões para manipulação robótica com sensor de força
- A Eka Robotics fechou uma Série A de US$150 milhões a um valuation pós-money de US$1,45 bilhão.
- A rodada foi co-liderada por a16z e F-Prime.
- A rodada foi anunciada em 20 de outubro.
- A Eka foi fundada pelo professor do MIT Pulkit Agrawal e pelo ex-pesquisador do Google DeepMind Tuomas Haarnoja.
- Em vez de um modelo visão-linguagem-ação, a Eka usa um modelo "visão-força-ação".
- O modelo funciona junto com uma garra sensível a força.
- O modelo é treinado por aprendizado por reforço em simulação física, em vez de dados de demonstração humana.
- Segundo a empresa, o robô pega cerca de 1.500 objetos de até 1 kg por hora, contra cerca de 600 de um humano.
- Segundo a empresa, o robô acerta a pegada em mais de 95% das vezes.
- A garra da Eka custa menos de US$1.000.
- A garra é certificada para 5 milhões de ciclos de uso.
- Braços industriais padrão chegam a 20 milhões de ciclos.
- A Eka faz pilotos com clientes industriais em tarefas de pegar e posicionar peças e de manuseio de fios.
**Fontes:**
- [S33] TechCrunch — https://techcrunch.com/2026/10/20/eka-is-worth-1-45-billion-thanks-to-a-physical-ai-model-that-has-experts-raving/
- [S34] Eka Robotics — https://ekarobotics.com/

## DeepSeek e Huawei — desenho conjunto de chips Ascend
- A DeepSeek trabalha com a Huawei para influenciar o desenho de futuros chips de IA, segundo duas fontes ouvidas pelo The Information em 19 de outubro.
- Engenheiros da Huawei estão alocados nos escritórios da DeepSeek.
- Esses engenheiros incorporam o retorno da DeepSeek ao desenho dos chips.
- O retorno inclui como os modelos fazem cálculos e movem dados entre processadores.
- A DeepSeek planeja começar a treinar modelos no Huawei Ascend 950DT já no fim de 2026.
- A Huawei planeja dar prioridade à DeepSeek na maior parte de seus chips Ascend 960DT, da próxima geração.
- O Ascend 960DT é esperado para o primeiro trimestre de 2027.
- Segundo o instituto de pesquisa Epoch AI, o Nvidia B300 tem cerca de sete vezes o desempenho aritmético bruto do Huawei Ascend 950.
- Treinar um modelo de fronteira pode exigir mais de 10.000 chips Huawei funcionando juntos por semanas.
- A Huawei planeja lançar o 950DT no quarto trimestre de 2026.
- O 950DT terá 144 GB de HBM (memória de alta largura de banda) própria da Huawei, a HiZQ 2.0.
- O 950DT terá 4 TB/s de largura de banda de memória.
- A DeepSeek não está abandonando a Nvidia e continua buscando acesso a seus processadores avançados.
- A DeepSeek também usa o TileLang, linguagem de código aberto que facilita adaptar software de IA a diferentes arquiteturas de chip.
- O TileLang foi lançado para o Ascend 950 no mês passado.
**Fontes:**
- [S35] The Information — https://www.theinformation.com/articles/deepseek-shaping-huaweis-ai-chips-growing-challenge-nvidia
- [S36] Yahoo Finance (Investing.com) — https://finance.yahoo.com/technology/ai/articles/deepseek-teams-huawei-challenge-nvidia-183703468.html
- [S37] AI Weekly — https://aiweekly.co/alerts/deepseek-to-pre-train-on-huawei-ascend-950dt-by-end-of-2026

## Meta — detalhes do supercluster Prometheus, em Ohio
- Num post de engenharia em 19 de outubro, a Meta disse que a primeira fase do Prometheus está concluída.
- O Prometheus é o supercluster de escala de gigawatt da Meta em New Albany, Ohio.
- A primeira fase treinou a família de modelos Muse, incluindo o Muse Wonder.
- Hoje o Prometheus reúne centenas de milhares de GPUs em vários prédios.
- Os prédios incluem estruturas de montagem rápida e capacidade alugada.
- Em escala completa, o Prometheus terá cerca de 1 milhão de GPUs.
- O cluster usa racks Nvidia GB200 NVL72 (plataforma Catalina) e GB300 NVL72 (plataforma Clemente).
- A próxima plataforma será a San Miguel, com racks Vera Rubin NVL72 de mais de 170 kW, totalmente refrigerados a líquido.
- Cada rack de 72 GPUs treina com 64 GPUs e mantém 8 de reserva.
- Quando o cluster entrou em operação, em meados de 2025, as interrupções chegaram a quase 1.000 por dia a cada 8.000 GPUs.
- Um ano de trabalho reduziu as interrupções em 99%.
- O pré-treinamento do Muse Wonder teve goodput (fração do tempo de GPU convertida em treino útil) acima de 85%.
- O pré-treinamento do Muse Wonder teve cerca de 47.000 horas de GPU entre interrupções.
- Esse intervalo já subiu para mais de 54.000 horas de GPU.
- Cargas sincronizadas de GPU causam oscilações de consumo de energia de 30% a 40%.
- A Meta controla essas oscilações com um software chamado Dynamo Dimmer, que reduz gradualmente o limite de potência das GPUs quando o cluster se aproxima do teto elétrico.
- A Meta também usa baterias nos racks e armazenamento de energia no nível do site.
- O Prometheus é o modelo para o Hyperion, próximo supercluster da Meta, em Richland Parish, Louisiana.
- O Hyperion está sendo projetado com refrigeração líquida em circuito fechado.
- O Hyperion terá conexão completa à rede elétrica pela concessionária Entergy, paga pela Meta.
**Fontes:**
- [S38] Engineering at Meta — https://engineering.fb.com/2026/10/19/data-center-engineering/inside-prometheus-meta-gigawatt-scale-supercluster/
- [S39] Mad Robot — https://madrobot.blog/2026/10/19/meta-prometheus-supercluster-1-million-gpus-ohio-gigawatt-muse/
- [S40] Dealroom News — https://dealroom.co/news/164242-inside-prometheus-meta-trained-muse-wonder-on-phase-one-of-its-gigawatt/

## Amazon — mais de €16 bilhões na Alemanha em 2027
- A Amazon disse em 20 de outubro que planeja investir mais de €16 bilhões (cerca de US$18,7 bilhões) na Alemanha em 2027.
- O anúncio foi feito no Invest in Germany Summit, evento do governo federal alemão em Berlim.
- Do total, €4,8 bilhões (cerca de US$5,6 bilhões) vão para a expansão da região AWS Europe (Frankfurt) em 2027.
- A expansão em Frankfurt atende à demanda por serviços de nuvem e IA.
- A Amazon está abrindo um segundo laboratório de pesquisa em robótica e IA em Berlim.
- O novo laboratório dobra a presença de pesquisa da Amazon na cidade.
- A Amazon está contratando cientistas aplicados e engenheiros de hardware, software e sistemas de robótica.
- A Amazon não divulgou o custo do novo laboratório.
- O pacote também inclui internet via satélite da Amazon Leo.
- O pacote também inclui novos projetos de logística e novas produções do Prime Video.
- A Amazon diz ter investido mais de €100 bilhões (cerca de US$117 bilhões) na Alemanha desde 2010.
- A ministra da Economia, Katherina Reiche, chamou o investimento de "um claro voto de confiança na Alemanha".
- Reiche disse que data centers de alto desempenho são "a base da economia digital".
**Fontes:**
- [S41] Amazon Press Center — https://press.aboutamazon.com/de/2026/10/invest-in-germany-summit-amazon-announces-16-billion-euro-investment-in-germany-in-2027
- [S42] About Amazon — https://www.aboutamazon.com/company-news/amazon-germany-investment
- [S43] The Next Web — https://thenextweb.com/news/amazon-plans-to-make-a-e16bn-investment-in-germany-in-2027

## Irã — Guarda Revolucionária diz ter incendiado mais dois petroleiros perto de Hormuz
- Na terça-feira, 20 de outubro, a Guarda Revolucionária do Irã (IRGC) disse que dois petroleiros pegaram fogo e pararam após atingirem minas navais da IRGC.
- Segundo a IRGC, as minas estavam no que Teerã chama de ponto de travessia ilegal, na parte sul do Estreito de Hormuz.
- Segundo a Iran International, a Marinha da IRGC disse que os petroleiros atingiram as minas na noite de segunda-feira, 19 de outubro.
- A IRGC não identificou os navios nem informou vítimas.
- A IRGC alertou que navios que cruzarem a passagem minada podem ser incendiados.
- A IRGC também disse ter derrubado um drone americano MQ-9 Reaper.
- Na segunda-feira, a IRGC havia dito que outro petroleiro pegou fogo após atingir uma mina.
- No domingo, a IRGC havia dito que outros dois petroleiros atingiram minas.
- O comandante do Comando Central dos EUA (CentCom), almirante Brad Cooper, disse que o estreito é controlado pelos EUA e parceiros regionais, não pelo Irã.
- Cooper disse que o estreito "continua aberto aos negócios".
- Cooper citou cerca de 400 travessias de navios mercantes na semana anterior.
- A Reuters informou em 20 de outubro, citando três altos funcionários iranianos e uma fonte interna, que o Irã prolonga deliberadamente as negociações com Washington para enfraquecer Trump antes das eleições de meio de mandato de 3 de novembro.
- Segundo um funcionário iraniano ouvido pela Reuters, o Irã se prepara para novos ataques de Israel e dos EUA, não para um acordo que encerre a guerra.
- O chefe do Exército do Paquistão, marechal de campo Asim Munir, chegou a Teerã na terça-feira para se reunir com altos funcionários iranianos.
- O Paquistão foi um mediador central entre EUA e Irã neste ano.
- A visita ocorre com as negociações paradas.
- O Brent estava acima de US$109,8 por barril na terça-feira (meio-dia em Pequim), alta de 0,26%.
- O WTI estava a US$98,71 por barril.
- Os riscos da guerra com o Irã compensavam a expectativa de mais oferta russa.
**Fontes:**
- [S44] NDTV (AFP) — https://www.ndtv.com/world-news/iran-guards-say-2-violating-oil-tankers-set-ablaze-in-strait-of-hormuz-12210436
- [S45] Iran International — https://www.iranintl.com/en/liveblog/202610187555
- [S46] Gulf News — https://gulfnews.com/uae/us-israel-iran-war-lull-nears-breaking-point-us-israel-weighing-new-strikes-what-to-know-oct-20-2026-1.500716736
- [S47] Geo News (Reuters) — https://www.geo.tv/liveblog/israeliran-war-live-updates?12345=
- [S48] Al Jazeera — https://www.aljazeera.com/news/liveblog/2026/10/20/draft-3

## Reino Unido — caças Typhoon para defender a Arábia Saudita dos houthis
- Em 20 de outubro, o Ministério da Defesa do Reino Unido anunciou que caças Typhoon da RAF farão missões defensivas de contra-ataque aéreo para proteger cidades e infraestrutura crítica da Arábia Saudita.
- Os Typhoon não farão ataques ofensivos contra os houthis.
- O Reino Unido também fornecerá um avião de transporte A400M da RAF para movimentar material de defesa dentro da Arábia Saudita.
- O Reino Unido enviará assessores militares para apoiar oficiais de estado-maior sauditas.
- O Reino Unido estenderá o apoio de reabastecimento aéreo às operações aéreas sauditas.
- Essas operações incluem as que visam degradar alvos militares houthis no Iêmen.
- O secretário de Defesa, Wes Streeting, chamou os ataques houthis à Arábia Saudita de "absolutamente desprezíveis".
- Streeting citou os ataques ao aeroporto de Riad.
- O apoio atende a um pedido do governo saudita.
- O primeiro-ministro Andy Burnham havia dito no início do mês que o Reino Unido estava disposto a considerar o pedido.
- O pacote amplia a ajuda anunciada em setembro, que incluía um avião de reabastecimento RAF Voyager, mas nenhum caça.
- Ataques houthis ao aeroporto de Riad mataram mais de uma dúzia de pessoas em outubro e afetaram voos.
- Autoridades iemenitas disseram na segunda-feira que um ataque houthi a um campo de treinamento das forças de segurança do governo matou 58 pessoas.
**Fontes:**
- [S49] GOV.UK (Ministry of Defence) — https://www.gov.uk/government/news/operational-update-20-october-uk-military-support-to-the-kingdom-of-saudi-arabia
- [S50] Cyprus Mail (Reuters) — https://cyprus-mail.com/2026/10/20/britain-says-it-will-carry-out-defensive-air-missions-over-saudi-arabia
- [S51] The National — https://www.thenationalnews.com/news/uk/2026/10/20/uk-mission-to-defend-saudi-arabia-adds-typhoon-jets/
- [S52] Al Jazeera — https://www.aljazeera.com/news/2026/10/20/uk-to-deploy-raf-fighter-jets-to-defend-saudi-arabia-from-houthi-attacks

## JAXA — lançamento da MMX, missão para trazer amostras de Fobos
- A sonda Martian Moons eXploration (MMX), da JAXA (agência espacial japonesa), foi lançada em 19 de outubro às 15h41 (horário de Nova York; 19h41 GMT).
- No Japão, o lançamento ocorreu às 4h41 de 20 de outubro.
- A sonda decolou num foguete H3 do Centro Espacial de Tanegashima.
- Foi o 10º voo do H3.
- A JAXA confirmou que a sonda se separou do foguete pouco mais de uma hora após a decolagem.
- Segundo a JAXA, a sonda está "iniciando sua jornada rumo ao sistema marciano".
- A chegada perto de Marte está prevista para por volta de agosto de 2027.
- A MMX planeja dois pousos em Fobos, lua de Marte, para coletar pelo menos 10 gramas de solo.
- A cápsula com as amostras deve pousar na Austrália em 2031.
- Seria o primeiro retorno de amostras de uma lua de Marte.
- A sonda leva o rover teuto-francês Idefix, desenvolvido pela DLR (agência espacial alemã) e pelo CNES (agência espacial francesa).
- O Idefix deve pousar em Fobos por volta da virada de 2028 para 2029.
- O Idefix será o primeiro rover a circular numa lua de Marte.
- O Idefix deve explorar Fobos por cerca de 100 dias.
- A NASA investiu cerca de US$87 milhões até o fim da missão.
- A NASA receberá pelo menos 15% da amostra de 10 gramas prevista.
- A NASA forneceu o espectrômetro MEGANE e um coletor pneumático da Honeybee Robotics.
- A sonda chinesa Tianwen-3 deve ser lançada por volta de 2028.
- A Tianwen-3 pretende trazer amostras de Marte já em 2031, possivelmente antes do retorno da missão japonesa.
**Fontes:**
- [S53] Space.com — https://www.space.com/space-exploration/launches-spacecraft/japan-launches-historic-mmx-sample-return-mission-to-mars-moon-phobos
- [S54] DLR — https://www.dlr.de/en/latest/news/2026/mmx-mission-successfully-launched-idefix-rover-is-on-its-way-to-martian-moon-phobos
- [S55] New Straits Times (AFP) — https://www.nst.com.my/world/world/2026/10/1559338/japan-successfully-launches-probe-historic-mars-moon-mission
- [S56] AP News — https://apnews.com/article/japan-mars-moon-mission-fb51fbbf90374631e8ae658f9ca46154

## GSK — FDA aprova Jemperli para câncer de reto localmente avançado
- Em 19 de outubro, a FDA (agência americana que regula alimentos e medicamentos) concedeu aprovação acelerada ao Jemperli (dostarlimab), da GSK.
- A aprovação é para o uso do Jemperli sozinho em adultos com câncer de reto localmente avançado, estágio II ou III, sem tratamento prévio.
- Os tumores precisam ter deficiência de reparo de erros de pareamento do DNA (dMMR) ou alta instabilidade de microssatélites (MSI-H), confirmadas por teste autorizado pela FDA.
- Segundo a GSK, o Jemperli é a primeira e única imunoterapia aprovada nos EUA para esses pacientes.
- A aprovação se baseou em resultados interinos do estudo de fase 2 AZUR-1, com 154 pacientes.
- Após acompanhamento mediano de mais de dois anos, quase três quartos dos pacientes não precisaram de cirurgia, radioterapia ou quimioterapia.
- A GSK disse que 68% dos pacientes avaliáveis (98 de 144) tiveram resposta clínica completa sustentada aos 12 meses, pela avaliação dos investigadores.
- Pela revisão central independente, a taxa foi de 47% (54 de 116), com dados ainda em maturação.
- Não houve recorrência da doença entre os pacientes que responderam até agora.
- O marcador MSI-H/dMMR aparece em cerca de 5% a 10% dos cânceres de reto.
- O tratamento padrão (quimioterapia, radioterapia e cirurgia) pode causar disfunções intestinais, urinárias e sexuais duradouras, cânceres secundários e infertilidade.
- A análise ocorreu dentro do programa piloto National Priority Voucher do comissário da FDA.
- A aprovação saiu 4 meses antes da data-meta da FDA.
- Reações adversas graves ocorreram em 20% dos pacientes.
- 3% dos pacientes interromperam o tratamento por reações adversas.
- A GSK apresentará os dados interinos completos do AZUR-1 no Congresso da ESMO (Sociedade Europeia de Oncologia Médica), em outubro de 2026.
**Fontes:**
- [S57] FDA — https://www.fda.gov/news-events/press-announcements/fda-approves-immunotherapy-may-allow-certain-patients-rectal-cancer-avoid-chemotherapy-radiation-and
- [S58] GSK — https://us.gsk.com/en-us/media/press-releases/jemperli-dostarlimab-gxly-approved-in-us-as-first-and-only-immunotherapy-for-adults-with-msi-hdmmr-locally-advanced-rectal-cancer/
- [S59] The ASCO Post — https://ascopost.com/news/october-2026/fda-approves-dostarlimab-for-msi-hdmmr-locally-advanced-rectal-cancer/
- [S60] Fierce Pharma — https://www.fiercepharma.com/pharma/gsk-jemperli-scores-fda-approval-rectal-cancer-backed-high-complete-response-rate

## EUA — sanções à chinesa MiraclePlus por roubo de segredos de IA do Google
- Em 19 de outubro, o Departamento de Estado dos EUA designou cinco entidades sediadas na China com base no Protecting American Intellectual Property Act (PAIPA), lei de proteção à propriedade intelectual americana.
- As entidades são a Shanghai Zhisuan Technology, a empresa de venture capital MiraclePlus e três fundos e entidades ligados à MiraclePlus.
- A Zhisuan foi fundada em 2023 pelo ex-engenheiro do Google Linwei Ding.
- Ding se candidatou à incubadora da MiraclePlus afirmando que a Zhisuan poderia replicar a infraestrutura de IA do Google.
- A MiraclePlus deu capital semente à Zhisuan em troca de participação na empresa.
- Ding foi condenado em 29 de janeiro por sete acusações de espionagem econômica e sete de roubo de segredos comerciais.
- Ding foi sentenciado em setembro a um ano de prisão.
- As sanções incluem bloqueio de bens e restrições a transações bancárias e de câmbio.
- As sanções proíbem instituições financeiras americanas de conceder empréstimos ou crédito acima de US$10 milhões em 12 meses às entidades.
- As sanções proíbem pessoas americanas de comprar participação relevante em ações ou dívida das entidades.
- O OFAC (escritório do Tesouro americano que administra sanções) autorizou o encerramento de negócios com a MiraclePlus até 19 de janeiro de 2027.
- A MiraclePlus foi fundada por Lu Qi, ex-executivo de IA da Microsoft e da Baidu.
- A MiraclePlus sucedeu o programa chinês da Y Combinator, que foi abandonado.
- A MiraclePlus investiu na plataforma de inferência SiliconFlow e na fabricante de robôs AgiBot.
- SiliconFlow e AgiBot estudam abrir capital em Hong Kong.
**Fontes:**
- [S61] US Department of State — https://www.state.gov/releases/office-of-the-spokesman/2026/10/imposing-sanctions-to-protect-americans-from-intellectual-property-theft-fact-sheet
- [S62] Export Compliance Daily — https://exportcompliancedaily.com/article/2026/10/20/us-sanctions-five-chinese-entities-over-google-tradesecret-theft-2610190052?BC=bc_6ad6f2dec6ebe
- [S63] The Edge Malaysia (Bloomberg) — https://theedgemalaysia.com/node/822496
- [S64] South China Morning Post — https://www.scmp.com/news/china/diplomacy/article/3371434/us-sanctions-5-chinese-entities-over-ex-google-engineers-ai-trade-secrets-theft

## Mynt (GCash) — estreia em Manila após o maior IPO da história das Filipinas
- A Mynt Inc., operadora da carteira digital GCash, estreou na Bolsa de Valores das Filipinas (PSE) em 20 de outubro com o ticker GCASH.
- A Mynt levantou 60,9 bilhões de pesos filipinos (cerca de US$967 milhões), o maior IPO da história da bolsa.
- O presidente Ferdinand Marcos Jr. liderou a cerimônia de abertura do pregão.
- A Mynt vendeu cerca de 8,03 bilhões de ações a 6,60 pesos (cerca de US$0,10) cada.
- O lote suplementar, de cerca de 1,20 bilhão de ações secundárias adicionais, elevou a oferta de cerca de 53 bilhões de pesos (cerca de US$842 milhões) para 60,9 bilhões de pesos.
- O IPO superou o da Monde Nissin, de 55,89 bilhões de pesos (cerca de US$887 milhões), em 2021.
- A Mynt estreou com valor de mercado de 441,5 bilhões de pesos (cerca de US$7 bilhões).
- A Mynt se tornou a sétima maior empresa doméstica listada na PSE.
- As ações subiram até 1,7%, para 6,71 pesos, durante o pregão.
- A alta ocorreu em meio a uma venda generalizada de ações ligadas a IA na Ásia.
- A ação fechou o primeiro dia no preço do IPO, segundo a GMA News.
- Mais de 20 investidores-âncora, incluindo BlackRock, Citadel, Fidelity International e a IFC (braço do Banco Mundial para o setor privado), comprometeram cerca de US$500 milhões.
- Esse valor equivale a quase 60% da oferta-base.
- Segundo o BusinessWorld, a Mynt planeja destinar 60% dos recursos líquidos da oferta primária ao seu negócio de crédito, o CreditTech.
- O restante vai para desenvolvimento de produtos e fins corporativos gerais.
**Fontes:**
- [S65] Philippine Stock Exchange — https://www.pse.com.ph/mynt-inc-raises-p60-9-b-in-historic-stock-market-debut/
- [S66] BusinessWorld — https://bworldonline.com/top-stories/2026/10/20/788054/gcash-parent-mynt-makes-pse-debut-in-record-p60-9-b-ipo/
- [S67] GMA News — https://www.gmanetwork.com/news/money/companies/1006486/gcash-parent-debuts-at-pse-opens-with-p441-5b-market-capitalization/story/
- [S68] GMA News — https://www.gmanetwork.com/news/money/companies/1006573/gcash-parent-mynt-closes-at-ipo-price-on-market-debut-raises-p60-9-billion/story/
- [S69] CNA (Reuters) — https://www.channelnewsasia.com/business/philippines-gcash-mynt-shares-ipo-6474091

## Wall Street — ações de chips interrompem 8 quedas seguidas; juro de 10 anos a 5,135%
- Na segunda-feira, 19 de outubro, o Nasdaq subiu 1,11%, para 26.430,89 pontos.
- O S&P 500 subiu 0,41%, para 7.690,73 pontos.
- O Dow Jones caiu 0,07% (36,38 pontos), para 51.966,03 pontos.
- O índice de semicondutores da Filadélfia subiu 1,61%.
- A alta encerrou uma sequência de oito pregões de queda, em que o índice recuou 15,7%.
- Foi a maior sequência de quedas do índice desde outubro de 2008.
- A CoreWeave caiu mais 0,44%.
- Na semana anterior, a CoreWeave havia caído mais de 25% por preocupações com sua dívida de cerca de US$50 bilhões.
- O rendimento do título do Tesouro americano de 10 anos subiu 3,8 pontos-base, para 5,135%, na segunda-feira.
- O rendimento está 1,148 ponto percentual acima de um ano antes.
- O rendimento está 0,175 ponto abaixo da máxima de 52 semanas, de 5,31%, atingida em 5 de outubro.
- O petróleo WTI fechou em alta de 2,22%, a US$103,66 por barril, na segunda-feira.
- O Brent caiu 0,28%, para US$109,55 por barril.
- Os operadores acompanhavam ataques a navios no Golfo Pérsico e ataques entre Ucrânia e Rússia a infraestrutura de energia.
- No início de terça-feira, o S&P 500 caía 0,1% e o Nasdaq, 0,5%, com nova oscilação das ações de IA.
- Meta, Micron e Intel caíam.
- As bolsas europeias voltaram a cair.
**Fontes:**
- [S70] CNBC — https://www.cnbc.com/2026/10/18/stock-market-today-live-updates.html
- [S71] The Herald Business — https://biz.heraldcorp.com/article/10907970
- [S72] Morningstar (Dow Jones) — https://www.morningstar.com/news/dow-jones/202610196209/10-year-treasury-yield-rises-to-5135-data-talk
- [S73] AP News — https://apnews.com/article/stock-markets-oil-ai-rates-inflation-b972b64127db5412a2b02c35ecf95c88
