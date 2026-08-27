# Fatos — Newsletter [Tech] 26 de Agosto de 2026

## Alibaba — Qwen3.8-Flash-Next de pesos abertos
- A Alibaba lançou o Qwen3.8-Flash-Next em 26 de agosto de 2026.
- O modelo é multimodal, de pesos abertos e usa arquitetura Mixture-of-Experts (mistura de especialistas, em que só parte da rede é ativada a cada token).
- A empresa apresenta o modelo como a primeira prévia pública da arquitetura que vai sustentar a família Qwen4.
- O modelo tem 125 bilhões de parâmetros principais.
- Há ainda 51 bilhões de parâmetros adicionais em embeddings de N-gramas.
- Apenas 6 bilhões de parâmetros são ativados por token.
- A Alibaba afirma que o modelo iguala o Qwen3.7-Plus a cerca de um nono do custo de treinamento.
- A empresa diz que o modelo é mais capaz que o Qwen3.7-Plus em programação e trabalho colaborativo.
- Na tabela de benchmarks publicada pela Alibaba, o Qwen3.8-Flash-Next marca 62,5 no SWE-bench Pro contra 53,4 do Claude Opus 4.6 Max.
- No SWE-bench Multilingual, o placar é 81,0 contra 77,5 do Claude Opus 4.6 Max.
- No CoWorkBench, o modelo marca 73,9 contra 68,2 do Opus 4.6 Max.
- No JobBench, marca 55,7 contra 36,6 do modelo da Anthropic.
- No Humanity's Last Exam, o Claude Opus 4.6 Max fica à frente, com 40,0 contra 35,9 do Qwen.
- O checkpoint traz contexto nativo de 262.144 tokens.
- O model card descreve extensão do contexto até 1.000.000 de tokens.
- O modelo é distribuído sob a Qwen Community License 1.0.
- A arquitetura é híbrida, combinando Gated DeltaNet e Qwen Sparse Attention (atenção esparsa).
- A página de divulgação no ModelScope foi ao ar em 25 de agosto, com contagem regressiva apontando para lançamento às 23h no horário de Pequim.
- Foram lançadas as versões padrão e FP8.
**Fontes:**
- [S1] OfficeChai — https://officechai.com/ai/qwen-3-8-flash-next-benchmarks/
- [S2] NVIDIA Developer Forums — https://forums.developer.nvidia.com/t/qwen3-8-flash-next/381228
- [S3] Startup Fortune — https://startupfortune.com/alibabas-qwen38-flash-next-gives-builders-an-early-look-at-qwen4/
- [S4] Atoms — https://atoms.dev/blog/qwen3-8-flash-next-qwen4-preview-6b-active-parameters
- [S5] ByteIota — https://byteiota.com/qwen-38-flash-next-qwen4-architecture-preview/
- [S6] Bloomberg — https://www.bloomberg.com/news/articles/2026-08-26/alibaba-releases-smaller-cost-effective-qwen-ai-model

## Z.ai — Ox Alpha, o modelo stealth que liderou o OpenRouter
- A chinesa Z.AI, também conhecida como Zhipu, confirmou na quarta-feira, 26 de agosto, que o modelo stealth Ox Alpha é uma nova iteração de sua série GLM.
- A empresa disse que liberaria os pesos do modelo naquela mesma noite.
- A confirmação veio em resposta a perguntas da Bloomberg News.
- O Ox Alpha apareceu sem crédito de autoria no OpenRouter durante o fim de semana.
- O modelo subiu ao topo do ranking do OpenRouter, com mais que o dobro do uso do DeepSeek.
- Foi o maior lançamento da história desse marketplace.
- O ranking do OpenRouter mostra o Ox Alpha com 23,2 trilhões de tokens processados.
- Em segundo lugar aparece o DeepSeek V4 Flash 0731, com 11,6 trilhões de tokens.
- O Ox Alpha é um modelo de raciocínio voltado para programação e tarefas agênticas.
- O modelo aceita input de texto, imagem e vídeo.
- Patrick Collison, CEO da Stripe — que está adquirindo o OpenRouter —, chamou o lançamento em stealth de "very impressive" ("muito impressionante").
- O Ox Alpha foi listado no OpenRouter em 20 de agosto com custo zero.
- A janela de contexto listada é de 1.048.576 tokens, com output máximo de 131.072 tokens.
- O provedor do modelo não foi identificado e alegava capacidade para atender 100 trilhões de tokens por dia.
- Antes da confirmação, análises forenses independentes de tokenizador em 25 prompts já haviam batido as contagens de tokens do Ox Alpha com as do GLM-5.3, com diferença fixa de 75 tokens.
- O comunicado da Z.ai citou a série GLM, mas não um nome de produto específico.
- A Z.ai abriu capital em janeiro.
- A empresa divulga na segunda-feira seu primeiro relatório de resultados detalhado, cobrindo os seis meses desde o IPO (oferta pública inicial de ações).
**Fontes:**
- [S7] Bloomberg — https://www.bloomberg.com/news/articles/2026-08-26/china-s-z-ai-made-ox-alpha-stealth-model-that-rivals-deepseek
- [S8] The Edge Markets — http://www.theedgemarkets.com/node/815823
- [S9] The Next Web — https://thenextweb.com/news/ox-alpha-zhipu-glm-open-weights-censorship-fingerprint
- [S10] OpenRouter — https://openrouter.ai/rankings
- [S11] Capital & Compute — https://capitalandcompute.net/blog/ox-alpha-stealth-model-explained/

## Bill Gates — ensaio sobre os riscos da era da IA
- Bill Gates publicou em 26 de agosto um ensaio no GatesNotes.
- No texto, Gates escreve que a transição para a era da IA "será um dos períodos mais turbulentos da história da humanidade".
- Ele afirma que "neste momento, não estamos nos preparando adequadamente".
- Gates disse à MIT Technology Review: "Cruzamos o limiar em termos de capacidades biológicas, capacidades cibernéticas, capacidades psicossociais, capacidades de destruição do mercado de trabalho e até de falta de controle".
- Gates argumenta que qualquer modelo capaz de projetar moléculas inéditas deveria ser monitorado.
- Ele diz ver o risco de bioterrorismo como "cerca de 50 vezes mais assustador, mais provável do que o risco de uma pandemia natural".
- O ensaio tem quase 6.000 palavras.
- Gates propõe taxar tokens de IA e robôs para desestimular empresas de substituir funcionários humanos e reforçar o financiamento da rede de proteção social.
- Ele propõe reservar determinadas ocupações para pessoas, como o cuidado de idosos, sob um rótulo que chama de "Human Reserved" (reservado a humanos).
- Gates pede a criação de órgãos nacionais que definam prioridades de IA entre agências de governo.
- Ele defende uma nova organização internacional que combine elementos de regimes de inspeção nuclear, da regulação da aviação internacional e dos acordos de proteção da camada de ozônio.
- Gates diz que será necessária alguma cooperação entre Estados Unidos e China.
- Gates disse ao New York Times: "Em privado, as pessoas que entendem o quão bom isso está e o quanto está melhorando estão muito preocupadas".
- Segundo ele, em público essas mesmas pessoas dizem "não fale isso. É ruim para nós — o próximo trilhão de dólares que estamos tentando levantar".
- Gates rejeita a autorregulação do setor: "Autorregulação na ferramenta mais perigosa já inventada? Não, obrigado!".
**Fontes:**
- [S12] GatesNotes — https://www.gatesnotes.com/a-turbulent-ai-era-and-critical-choices-to-make
- [S13] MIT Technology Review — https://www.technologyreview.com/2026/08/26/1142946/bill-gates-ai-danger-threshold/
- [S14] The Verge — https://www.theverge.com/ai-artificial-intelligence/984923/bill-gates-is-deeply-worried-about-ai-and-hes-no-longer-staying-quiet
- [S15] The Decoder — https://the-decoder.com/bill-gates-warns-ai-is-more-dangerous-than-the-tech-industry-will-admit/
- [S16] Free Press Journal — https://www.freepressjournal.in/tech/bill-gates-warns-ai-transition-will-be-one-of-historys-most-turbulent-periods-calls-for-global-regulatory-framework

## Anthropic — mercado de US$30 trilhões no pitch de IPO
- A Anthropic deve dizer a investidores do IPO que sua oportunidade potencial de receita supera US$30 trilhões, segundo pessoas a par do assunto citadas pelo Wall Street Journal.
- O número superaria a estimativa de US$28,5 trilhões que a SpaceX apresentou a investidores antes de sua própria abertura de capital.
- A estimativa é construída a partir de todo o escopo de trabalho que modelos de IA poderiam executar.
- Esse enquadramento contabiliza trabalho humano, e não gasto com software.
- Para efeito de comparação, as 191 empresas de tecnologia do S&P 1500 somaram US$2,4 trilhões de receita no ano passado, segundo dados da FactSet citados pelo Journal.
- A Anthropic mais que dobrou a receita no segundo trimestre, para US$11,6 bilhões.
- No primeiro trimestre, a receita havia sido de US$4,73 bilhões.
- A empresa pode captar até US$100 bilhões na oferta.
- O valuation almejado é de cerca de US$2 trilhões.
- Ambas as marcas superariam a SpaceX, que captou US$86 bilhões e estreou com valuation de US$1,77 trilhão em junho.
- A Anthropic deve publicar o prospecto do IPO nas próximas semanas.
- Isso abre espaço para uma estreia já em setembro ou no início de outubro.
- A empresa entregou à SEC (a comissão de valores mobiliários dos EUA) um rascunho confidencial do Formulário S-1 em 1º de junho.
- Aswath Damodaran, professor de finanças da Universidade de Nova York, havia dito que a estimativa de mercado da SpaceX centrada em IA estava "chegando ao limite do plausível e passando dele".
**Fontes:**
- [S17] Wall Street Journal — https://www.wsj.com/tech/ai/anthropic-expected-to-tell-investors-it-sees-over-30-trillion-in-potential-revenue-a611efea
- [S18] Quartz — https://qz.com/anthropic-ipo-investors-30-trillion-market-opportunity-082526
- [S19] The Next Web — https://thenextweb.com/news/anthropic-ipo-30-trillion-addressable-market
- [S20] TipRanks — https://www.tipranks.com/news/anthropic-pitches-investors-a-30t-revenue-opportunity-bigger-than-spacexs-spcx-ipo-record
- [S21] Firstpost — https://www.firstpost.com/tech/anthropic-eyes-over-30-trillion-in-potential-revenue-as-ipo-plans-take-shape-14040761.html

## Meta — o Projeto OT de substituir equipes por agentes de IA
- No retiro de liderança de Zuckerberg no Havaí, em janeiro, a Meta concebeu o "Project OT", sigla de Organization Transformation (transformação organizacional).
- O plano previa uma empresa "AI native", em que a IA assumiria boa parte do trabalho diário de milhares de funcionários.
- Os trabalhadores virtuais seriam supervisionados por equipes humanas menores e "talent-dense" (densas em talento).
- Exercícios de planejamento de cenários chegaram a explorar reduzir muitas equipes em até 60%.
- A reestruturação seria feita em duas ondas: uma primeira leva de cortes em maio e outra em novembro.
- Na noite de 19 de maio, horas antes da primeira onda de demissões, Zuckerberg cancelou a rodada de novembro.
- No dia seguinte, a Meta ainda demitiu 10% de seus funcionários.
- Publicações internas mostraram que mudanças de código feitas por IA nas plataformas internas cresceram 220% em um ano.
- No mesmo período, mudanças que chegaram aos usuários subiram apenas 36%.
- Uma publicação interna de abril dizia que agentes de IA sem supervisão executavam "ações disruptivas de larga escala que humanos dificilmente executariam".
- Incidentes técnicos e de segurança graves subiram 40% em um ano.
- O tempo gasto por funcionários apagando incêndios subiu 70%.
- A Meta confirmou que o Project OT existiu e que os cenários mais drásticos previam cortes de até 60% em algumas equipes.
- A empresa disse que nunca pretendeu demitir 60% de toda a força de trabalho.
- A Meta reconheceu que alguns cenários consideravam reduções de até 60% em certas equipes, por demissões e realocações, mas disse que várias unidades grandes não estavam envolvidas.
- A Meta havia tornado obrigatória a instalação de software de rastreamento nos dispositivos de funcionários nos EUA para capturar digitação e cliques do mouse.
- O objetivo era ensinar seus agentes de IA a imitar como humanos interagem com computadores.
- A medida alimentou a revolta interna.
- Em uma reunião geral em julho, Zuckerberg admitiu que a tecnologia de agentes de IA não havia "acelerado" tão rápido quanto ele esperava.
- Na mesma ocasião, ele previu benefícios dentro de três a seis meses.
**Fontes:**
- [S22] Reuters — https://www.reuters.com/investigations/mark-zuckerberg-had-bold-plan-replace-meta-staff-with-ai-heres-how-it-imploded-2026-08-26/
- [S23] The Globe and Mail — https://www.theglobeandmail.com/business/article-zuckerberg-meta-staff-replace-ai/
- [S24] TimesLIVE — https://www.timeslive.co.za/news/sci-tech/2026-08-26-special-report-mark-zuckerberg-had-a-bold-plan-to-replace-meta-staff-with-ai-heres-how-it-imploded/
- [S25] Free Press Journal — https://www.freepressjournal.in/tech/meta-explored-upto-60-per-cent-team-cuts-in-ai-overhaul-before-zuckerberg-pulled-back-report

## DeepSeek — receita de US$70,7 milhões e nova rodada a US$74 bilhões
- A DeepSeek gerou cerca de 475 milhões de yuans (US$70,7 milhões) de receita nos primeiros sete meses de 2026.
- O valor é aproximadamente dez vezes o total de todo o ano de 2025.
- A informação foi publicada pelo The Information, citando pessoas a par do assunto.
- A empresa registrou prejuízo líquido de cerca de 715 milhões de yuans no período de sete meses.
- Em 2025, o prejuízo líquido do ano inteiro foi de 935 milhões de yuans.
- A DeepSeek negocia com investidores atuais e potenciais a captação de 50 bilhões de yuans em uma segunda rodada.
- A rodada avaliaria a empresa em 500 bilhões de yuans, cerca de US$74 bilhões.
- A margem bruta foi de 44,6% no total e de 82,9% nas vendas de API.
- No mesmo período de sete meses, o laboratório gastou cerca de 11 bilhões de yuans (aproximadamente US$1,6 bilhão) em infraestrutura, entre aluguel de servidores e compra de chips.
- Esse gasto é quase dez vezes os 1,2 bilhão de yuans gastos em todo o ano de 2025.
- A DeepSeek fechou sua primeira rodada externa no fim de maio, com valuation pós-money próximo de US$52 bilhões.
- Nessa rodada foram captados cerca de US$7 bilhões de um grupo descrito pela Reuters como uma coalizão industrial alinhada ao Estado — Tencent, a fabricante de baterias CATL, o fundo nacional de IA da China, NetEase e JD.com.
- A empresa busca agora quase US$8 bilhões adicionais a um valuation de cerca de US$74 bilhões.
- A DeepSeek contratou bancos para uma listagem em Xangai prevista para 2027.
**Fontes:**
- [S26] The Information — https://www.theinformation.com/articles/deepseeks-revenue-reaches-70-million-july-tenfold-jump-2025
- [S27] The Standard (Hong Kong) — https://www.thestandard.com.hk/finance/article/341002/DeepSeeks-first-seven-month-revenue-surged-tenfold-to-475-million-yuan-report-says
- [S28] AInvest — https://www.ainvest.com/news/deepseek-10x-revenue-jump-meets-cost-scale-82-9-api-margin-cover-month-1-6b-compute-bill-giveaway-pricing-bending-2608/

## Moonshot AI — 30% da receita das nuvens americanas pelo Kimi K3
- A chinesa Moonshot AI negocia acordos de divisão de receita com Microsoft, Amazon e Google, da Alphabet.
- Os acordos permitiriam que as gigantes americanas de nuvem hospedassem seu modelo Kimi K3.
- Três pessoas a par das conversas relataram as negociações à Reuters.
- A Moonshot, que prepara um IPO, busca até 30% da receita gerada por serviços ligados ao K3 no Azure, no AWS e no Google Cloud.
- Qualquer acordo seria o primeiro grande pacto de divisão de receita entre uma empresa chinesa de IA e uma grande empresa americana de nuvem.
- As conversas estão em estágio inicial.
- Pontos ainda em aberto incluem como a receita seria dividida, acesso a dados e auditoria do uso de tokens.
- A fatia de 30% inverte o arranjo usual, em que a plataforma fica com a comissão e o desenvolvedor do modelo recebe o restante.
- O secretário do Tesouro dos EUA, Scott Bessent, disse no mês passado que poderia incluir a Moonshot em uma lista negra comercial.
- Autoridades americanas acusam a empresa, sediada em Pequim, de ter copiado o Fable, o modelo mais sofisticado da Anthropic, para ajudar a criar o Kimi K3.
- As autoridades também acusam a Moonshot de adquirir chips da Nvidia ilegalmente.
- A Moonshot já assinou acordos semelhantes de divisão de receita com plataformas de nuvem menores.
- Em julho, a provedora chinesa de serviços de TI Chinasoft International divulgou ter um acordo de divisão de receita com a Moonshot.
**Fontes:**
- [S29] Reuters — https://www.reuters.com/business/retail-consumer/chinas-moonshot-talks-with-microsoft-amazon-google-over-k3-revenue-sharing-2026-08-26/
- [S30] Euronext (Reuters wire) — https://live.euronext.com/en/financial-news/exclusive-chinas-moonshot-talks-microsoft-amazon-google-over-k3-revenue-sharing
- [S31] The Globe and Mail — https://www.theglobeandmail.com/business/article-china-moonshot-ai-kimi-k3-microsoft-amazon-google/
- [S32] The Next Web — https://thenextweb.com/news/moonshot-k3-revenue-sharing-us-clouds
- [S33] The Decoder — https://the-decoder.com/chinese-moonshot-ai-negotiates-hosting-deals-with-microsoft-amazon-and-google/

## Huawei — proposta de exportar chips Ascend 950 para o Egito
- A Huawei respondeu a uma licitação do Cairo com uma proposta de exportar 1.408 chips de sua linha Ascend 950, a mais avançada da empresa, para uma nuvem de treinamento de IA.
- A proposta inclui mais 600 chips Ascend 950 ou do modelo anterior 910B para dois clusters de inferência.
- O plano de construção da infraestrutura é de 12 meses.
- Os data centers atenderiam usos militares, de vigilância e outras aplicações do setor público.
- O acordo seria a primeira exportação conhecida dos aceleradores Ascend da Huawei após mais de um ano de tentativas.
- Autoridades americanas montam um consórcio com Nvidia, AMD e Microsoft para contrapor a oferta.
- Pode ser a primeira vez que Estados Unidos e China disputam diretamente a mesma licitação governamental de data center de IA.
- A proposta é uma parceria com a iFlytek, gigante chinesa de vigilância.
- A oferta inclui reconhecimento de veículos e de indivíduos com base em um banco de dados nacional da população.
- A apresentação tem 102 páginas.
- Em um dos slides, exemplos de "aplicações básicas de vídeo" trazem a insígnia do Ministério da Segurança Pública da China.
- Huawei e iFlytek estão na lista negra dos EUA desde 2019.
- Embarques de chips de IA para o Egito exigem autorização de Washington desde 2023.
- Cerca de 2.000 aceleradores Huawei 950DT equivalem, em capacidade de treinamento, a apenas algumas centenas dos melhores chips da Nvidia disponíveis comercialmente.
**Fontes:**
- [S34] Bloomberg — https://www.bloomberg.com/news/articles/2026-08-26/huawei-egypt-ai-ascend-chips-test-us-tech-diplomacy-nvidia-amd-microsoft
- [S35] The Edge Malaysia — http://www.theedgemarkets.com/node/815796
- [S36] Free Malaysia Today — https://www.freemalaysiatoday.com/category/business/2026/08/26/huawei-courts-egypt-with-ai-chips-in-test-of-us-tech-diplomacy

## Huawei e HP — licenciamento cruzado de patentes de Wi-Fi
- Huawei e HP anunciaram em 26 de agosto de 2026 um acordo global plurianual de licenciamento cruzado de patentes.
- O acordo inclui licença para a HP usar determinadas patentes de Wi-Fi da Huawei.
- A licença cruzada cobre patentes usadas em tecnologia Wi-Fi, incluindo o padrão mais recente, o Wi-Fi 7.
- Em contrapartida, a Huawei ganha acesso a patentes da HP.
- Nenhuma das duas empresas divulgou os termos financeiros.
- A HP minimizou o acordo, classificando-o como uma licença rotineira de patentes essenciais a padrões.
- A HP disse que o acordo "não representa uma relação, parceria ou colaboração estratégica ou comercial mais ampla com a Huawei".
- O acordo vem depois de a Huawei processar a HP em 2025 por patentes de Wi-Fi 6.
- A disputa foi resolvida em novembro de 2025, quando a HP se tornou licenciada do pool de patentes da empresa italiana de gestão de propriedade intelectual Sisvel.
- O pool de Wi-Fi 6 da Sisvel reúne cerca de 2.000 patentes.
- O acordo é um sinal de adoção de tecnologia da Huawei fora da China, apesar de os EUA terem colocado a empresa em sua lista negra em 2019.
**Fontes:**
- [S37] Huawei — https://www.huawei.com/en/news/2026/8/hpi-global-patent-agreement
- [S38] Reuters — https://ktwb.com/2026/08/25/chinas-huawei-us-pc-maker-hp-sign-multi-year-wi-fi-patent-deal/
- [S39] CNBC — https://www.cnbc.com/2026/08/25/hp-partners-huawei-wifi-tech-us-entity-list.html
- [S40] South China Morning Post — https://www.scmp.com/tech/big-tech/article/3365229/huawei-hp-settle-disputes-multi-year-wi-fi-patent-cross-licensing-deal

## Skild AI — S1, modelo de robô que aprende com um único vídeo
- A Skild AI anunciou o S1 em 25 de agosto de 2026.
- O S1 é um modelo fundacional de robótica que usa um único vídeo de demonstração como prompt.
- O modelo executa a tarefa sem fine-tuning e sem pós-treinamento, de modo que os pesos nunca mudam.
- O vídeo usado como prompt é gravado em perspectiva egocêntrica, do ponto de vista de quem executa a tarefa.
- Em uma comparação controlada, com dados, arquitetura e poder computacional constantes, o modelo com prompt em vídeo obteve 66% de acerto em tarefas inéditas.
- Uma política com prompt em linguagem, treinada com o mesmo conjunto de 100 mil horas de dados, obteve 9%.
- A Skild diz que uma demonstração em vídeo equivaleu a cerca de 380 episódios de pós-treinamento.
- O modelo com prompt em linguagem precisaria de cerca de 380 demonstrações para igualar o resultado obtido em contexto.
- As quatro tarefas demonstradas e ausentes do pré-treinamento foram plantar em vaso, fazer panquecas, preparar café coado e montar um kit.
- As tarefas levam até dez minutos e envolvem dezenas de etapas de manipulação.
- Em tarefas inéditas, o ganho sobre o prompt em linguagem é de 7 vezes.
- Não há pesos para download, API pública, licença, preço nem artigo científico.
- A Skild está implantando o S1 com um conjunto limitado de parceiros industriais.
- Os fabricantes de robôs parceiros anunciados são ABB Robotics, Universal Robots e MiR.
- O S1 foi treinado em infraestrutura de IA da Nvidia.
- A Skild diz que o modelo precisa inferir a intenção de quem demonstra, porque a demonstração pode vir de outra cena, outro ponto de vista ou outro corpo de robô.
**Fontes:**
- [S41] Skild AI — https://www.skild.ai/blogs/s1
- [S42] DataNorth — https://datanorth.ai/news/skild-ai-launches-s1
- [S43] LavX News — https://news.lavx.hu/article/skild-ai-says-s1-can-learn-new-robot-tasks-from-one-video

## Nvidia — Jetson Orin Nano 2 para robótica de entrada
- A Nvidia anunciou o Jetson Orin Nano 2 em 25 de agosto de 2026, na conferência Hot Chips.
- É um computador de robótica para IA de borda de entrada (processamento no próprio dispositivo, sem depender da nuvem).
- O produto é voltado a robôs, drones de entrega e inspeção e sistemas de visão computacional.
- O módulo entrega 78 trilhões de operações por segundo de poder computacional de IA.
- Tem 8 GB de memória e uma CPU Arm de 8 núcleos.
- Oferece o dobro do desempenho de inferência do Jetson Orin Nano Super, no mesmo formato físico.
- O ganho vem de Tensor Cores aprimorados e maior largura de banda de memória.
- No modo de 15 watts, consome 40% menos energia para entregar o mesmo desempenho da geração anterior.
- Mais de 3 milhões de desenvolvedores já construíram sobre a pilha de robótica da Nvidia.
- Cognex, Doosan Bobcat e Matic estão entre os primeiros a adotar o Jetson Orin Nano 2.
- O módulo e o kit de desenvolvimento são esperados para o primeiro semestre de 2027.
**Fontes:**
- [S44] Nvidia Newsroom — https://nvidianews.nvidia.com/news/nvidia-announces-jetson-orin-nano-2-robotics-computer-to-redefine-entry-level-edge-ai

## AM Intelligence — pedido de 9.000 GPUs Rubin para Hyderabad
- A AM Intelligence, plataforma de infraestrutura de IA criada pelos fundadores da Greenko, anunciou na terça-feira, 25 de agosto de 2026, um pedido firme e vinculante de 9.000 GPUs Nvidia Rubin.
- As GPUs são para sua primeira fábrica de IA, em Hyderabad.
- As GPUs serão implantadas como sistemas de escala de rack Vera Rubin NVL72.
- A instalação terá 30 MW de capacidade.
- A entrega está prevista para o primeiro trimestre de 2027.
- A instalação será um dos primeiros clusters de poder computacional de fronteira da Ásia.
- Hyderabad é a primeira etapa de um plano de 1 GW de capacidade de compute-as-a-service (poder computacional vendido como serviço) na Índia, nos EUA, na Finlândia e na Malásia.
- A empresa pretende colocar inicialmente 200 MW de capacidade no mercado.
- O investimento inicial supera US$8 bilhões.
- A unidade de Hyderabad está sendo projetada para entregar cerca de 450 exaFLOPS de inferência em NVFP4.
- O NVFP4 é um novo formato de baixa precisão da Nvidia para rodar cargas de IA com mais eficiência.
- O sistema Vera Rubin NVL72 usa memória HBM4 (High Bandwidth Memory, memória de alta largura de banda de nova geração).
- Mahesh Kolli, fundador da Greenko, disse que a capacidade inicial já foi comprada por um cliente americano não identificado, por causa de um acordo de confidencialidade.
- O grupo pretende chegar a 5 GW de capacidade de data center até 2030, na Índia, na Europa e em outras regiões.
**Fontes:**
- [S45] The Hindu — https://www.thehindu.com/business/Industry/ami-orders-9000-nvidia-rubin-gpus-for-hyderabad-facility/article71390110.ece
- [S46] Bloomberg via Yahoo Finance — https://finance.yahoo.com/technology/ai/articles/india-ai-data-center-firm-orders-9000-nvidia-vera-rubin-systems-094222289.html
- [S47] Moneycontrol — https://www.moneycontrol.com/technology/greenko-backed-ami-orders-9-000-nvidia-rubin-gpus-for-hyderabad-ai-factory-plans-8-billion-compute-push-article-14015185.html
- [S48] The Times of India — https://timesofindia.indiatimes.com/city/hyderabad/am-intelligence-to-deploy-one-of-asias-1st-nvidia-vera-rubin-gpu-clusters-at-hyderabad-ai-factory/articleshow/133517338.cms

## Samsung — linha de 4 nm ultrapassa 80% de aproveitamento no Groq 3 LPX
- A Nvidia anunciou na conferência Hot Chips 2026 que o acelerador de inferência Groq 3 LPX entrou em produção em massa.
- O chip é fabricado no processo de 4 nanômetros da Samsung Electronics, na linha S5 do campus de Pyeongtaek.
- O aproveitamento (yield, a proporção de chips funcionais por lâmina) melhorou cerca de duas a três vezes em relação a abril.
- O índice ultrapassou os 80%, patamar de referência para produção em massa estável.
- A taxa de utilização da linha de 4 nanômetros de Pyeongtaek se aproximou de 100%.
- A tendência é apontada como ponto de virada para o negócio de foundry (fabricação de chips sob encomenda para terceiros), que acumula prejuízos há muito tempo.
- A Samsung também fornece HBM4 de sexta geração para a GPU Rubin.
- A empresa fornece ainda módulos de DRAM de baixo consumo SOCAMM2 para a CPU Vera e SSDs baseados em memória NAND.
- Com isso, a Samsung amplia seu papel na plataforma Vera Rubin da Nvidia, de componentes para hardware de IA completo.
- A Nvidia informou em 24 de agosto que o Groq 3 LPX está em produção plena, como extensão da plataforma Vera Rubin.
- A Nebius é a primeira nuvem de IA a adotar o chip, em sua Nebius Token Factory.
**Fontes:**
- [S49] Seoul Economic Daily — https://en.sedaily.com/finance/2026/08/26/samsung-becomes-key-partner-for-nvidias-vera-rubin-eyes
- [S50] Nvidia — https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Groq-3-LPX-Now-in-Full-Production-With-World-Class-Speed-for-Agentic-AI/default.aspx

## LG CNS e Naver Cloud — refrigeração líquida na maior fábrica de IA da Coreia
- A LG CNS anunciou em 26 de agosto de 2026 que construirá infraestrutura de refrigeração líquida direct-to-chip com a Naver Cloud em seu data center de Samsong.
- A instalação tem 80 megawatts e deve figurar entre as maiores fábricas de IA da Coreia do Sul.
- O sistema de refrigeração foi projetado para rodar as futuras GPUs Vera Rubin da Nvidia.
- As GPUs pertencem à estatal National IT Industry Promotion Agency e serão operadas pela Naver Cloud.
- A construção e a validação têm conclusão prevista para 2027.
- A refrigeração líquida está se tornando obrigatória à medida que racks de GPU de alta densidade ultrapassam 200 kW.
- A refrigeração a ar convencional dá conta de cerca de 20 a 30 kW por rack.
- Espera-se que os racks Vera Rubin entreguem cerca de 3,3 vezes o desempenho de inferência da geração atual, a Blackwell Ultra, da Nvidia.
- O mercado global de refrigeração líquida para data centers deve crescer de US$4,07 bilhões em 2026 para US$27,65 bilhões até 2033, segundo a MarketsandMarkets.
**Fontes:**
- [S51] Aju Press — https://www.ajupress.com/view/20260826103715959
- [S52] Edaily — https://en.edaily.co.kr/news/eda202608265087/

## Canadá — tarifas de retaliação sobre US$20 bilhões em produtos americanos
- O governo do Canadá anunciou na terça-feira, 25 de agosto, tarifas de retaliação sobre C$27,6 bilhões (cerca de US$19,9 bilhões) em produtos americanos.
- Ottawa disse que a medida responde "dólar por dólar" às tarifas de 50% que Trump impôs a importações canadenses no fim de semana.
- As tarifas de retaliação atingem mais de 700 produtos americanos.
- As alíquotas vão de 15% a 50%.
- As tarifas entram em vigor em 8 de setembro.
- Os alvos incluem aço e alumínio, laticínios, eletrodomésticos, equipamentos agrícolas, celulose e papel, plásticos e eletrônicos.
- Ottawa dobrou de 25% para 50% a tarifa de retaliação sobre produtos americanos de aço e alumínio.
- O Canadá também anunciou um pacote adicional de C$7,5 bilhões (US$5,42 bilhões) de apoio a empresas e trabalhadores atingidos pela guerra comercial.
- O ministro das Finanças, François-Philippe Champagne, disse que os termos propostos pelo governo americano eram "antieconômicos, injustos e, em última instância, inaceitáveis".
- Segundo ele, Washington "pediu demais do Canadá e ofereceu pouco em troca".
- Trump chamou o Canadá, na terça-feira, de país "de longe o mais difícil e irracional" com quem lida.
- Ele sugeriu no Truth Social que os EUA parariam de fazer negócios com Ontário.
- Trump levantou repetidamente a possibilidade de rebatizar o Lago Ontário como "Lago América".
- Na segunda-feira, Trump havia dito que as tarifas americanas sobre carros, caminhões e autopeças canadenses subiriam para 50% em 1º de janeiro.
- O comércio bilateral entre EUA e Canadá somou cerca de US$872,3 bilhões em 2025.
- A escalada coloca em dúvida o futuro do acordo de livre-comércio USMCA.
**Fontes:**
- [S53] Al Jazeera — https://www.aljazeera.com/economy/2026/8/25/canada-hits-us-with-counter-tariffs-targeting-hundreds-of-products
- [S54] BBC — https://www.bbc.com/news/articles/c3v4xg5klx7o
- [S55] CNBC — https://www.cnbc.com/2026/08/25/canada-trump-tariffs-trade-carney-leblanc.html
- [S56] Foreign Policy — https://foreignpolicy.com/2026/08/25/us-canada-retaliatory-tariffs-trade-war-trump-ontario-ford/
- [S57] Los Angeles Times — https://www.latimes.com/world-nation/story/2026-08-25/canada-strikes-back-at-u-s-with-retaliatory-tariffs-as-trade-war-escalates

## Petróleo — Brent abaixo de US$90 com retorno de diplomatas americanos
- O Brent caiu 3,6% na terça-feira, 25 de agosto, para US$87,27 o barril.
- Foi a segunda queda seguida, depois de 13 altas em 14 pregões.
- O WTI caiu mais de 3%, para a mínima de uma semana.
- A queda veio depois de reportagem do New York Times segundo a qual o Departamento de Estado dos EUA se prepara para reenviar diplomatas a embaixadas no Oriente Médio evacuadas antes e durante a guerra com o Irã.
- O movimento sinaliza que Washington não espera um retorno às hostilidades plenas.
- A queda ocorreu apesar de os EUA terem anunciado na segunda-feira novas sanções ao Irã e a seus parceiros comerciais, sob a "Operation Economic Outcast".
- Dan Coatsworth, chefe de mercados da AJ Bell, disse que as sanções foram "menos severas do que o antecipado".
- A queda do petróleo aliviou expectativas de inflação.
- O rendimento do Treasury de 10 anos caiu cerca de 6 pontos-base na terça-feira, para 4,637%, ante 4,74% no fim da semana anterior, após tocar máximas de vários anos.
- As bolsas americanas fecharam em alta na terça-feira.
- O S&P 500 subiu 0,3%, ou 24,42 pontos, para 7.677,28.
- O Dow Jones subiu 160,24 pontos, para 53.577,40.
- O Nasdaq subiu 0,7%, ou 171,11 pontos, para 26.151,30.
- O petróleo voltou a cair na manhã de quarta-feira, 26 de agosto, com o Brent para entrega em outubro em baixa de 2,52%, a US$86,35.
- A queda foi atribuída à possibilidade de um acordo entre Irã e Omã para garantir uma rota de trânsito seguro pelo Estreito de Ormuz.
**Fontes:**
- [S58] AP via Barchart — https://www.barchart.com/story/news/4014034/falling-oil-prices-help-calm-the-stock-and-bond-markets
- [S59] Barchart — https://www.barchart.com/story/news/4031606/stocks-settle-higher-as-lower-crude-prices-ease-inflation-risks
- [S60] CNBC — https://www.cnbc.com/2026/08/25/stock-market-today-live-updates.html
- [S61] AFP — https://www-pp.afp.com/en/stocks-rise-and-oil-slips-traders-eye-iran-threat-nvidia-results

## Estados Unidos — PCE de julho em 3,7%, acima do esperado
- O Bureau of Economic Analysis, do Departamento do Comércio, divulgou na quarta-feira, 26 de agosto, o índice de preços PCE de julho.
- O PCE (índice de preços de gastos com consumo pessoal) subiu 0,2% no mês.
- Em 12 meses, o índice subiu 3,7%.
- Ambos os números ficaram 0,1 ponto percentual acima do consenso da Dow Jones.
- O núcleo do PCE, que exclui alimentos e energia e é o indicador de tendência preferido do Fed, subiu 0,2% no mês.
- Em 12 meses, o núcleo subiu 3,3%, em linha com as projeções e sem mudança em relação a junho.
- A inflação de serviços acelerou para 0,3%, ante 0,1% em junho.
- Os preços de bens caíram 0,1%, após queda de 0,6% no mês anterior.
- O PCE cheio está em 3,7% por dois meses seguidos.
- A meta do Fed é de 2%.
- A renda pessoal subiu 0,4% em julho.
- Os gastos do consumidor subiram 0,2% no mês.
- Os gastos pessoais reais ficaram estáveis no mês.
- Os mercados precificam 39% de chance de uma alta de 25 pontos-base dos juros na reunião do FOMC de 15 e 16 de setembro.
- Susan Collins, presidente do Fed de Boston, disse na terça-feira que seria apropriado apertar a política monetária "em breve" caso não haja progresso sustentado na inflação.
- O presidente do Fed, Kevin Warsh, discursa na sexta-feira no simpósio de Jackson Hole, promovido pelo Fed de Kansas City.
- Será seu primeiro grande evento público desde a divulgação do dado.
**Fontes:**
- [S62] CNBC — https://www.cnbc.com/2026/08/26/feds-preferred-inflation-gauge-shows-core-prices-rose-3point3percent-annually-in-july.html
- [S63] CNN — https://www.cnn.com/2026/08/26/economy/pce-consumer-spending-inflation-july
- [S64] Trading Economics — https://tradingeconomics.com/united-states/pce-price-index-monthly-change
- [S65] Quiver Quantitative — https://www.quiverquant.com/news/U.S.+PCE+Inflation+Holds+at+3.7%25+as+Consumer+Spending+Rises+and+GDP+Grows+1.5%25
- [S66] Bureau of Economic Analysis — https://www.bea.gov/data/personal-consumption-expenditures-price-index
- [S67] Barchart — https://www.barchart.com/story/news/4031606/stocks-settle-higher-as-lower-crude-prices-ease-inflation-risks

## Ucrânia — Zelensky condecora Musk com a Ordem da Liberdade
- Um decreto presidencial publicado na quarta-feira, 26 de agosto, concedeu a Elon Musk a Ordem da Liberdade, a maior honraria da Ucrânia para estrangeiros.
- O decreto cita seus "méritos pessoais excepcionais" na proteção da vida e da liberdade humanas e no fortalecimento das relações entre Ucrânia e Estados Unidos.
- O decreto identifica Musk como "empresário, engenheiro, presidente-executivo da SpaceX e da Tesla, Estados Unidos".
- O texto não menciona o Starlink nem as negociações militares em curso.
- Kiev quer conectividade Starlink para sistemas não tripulados que operem até cerca de 200 km dentro da Rússia.
- O objetivo é caçar lançadores móveis de mísseis balísticos, como os Iskander, antes que disparem.
- Musk hoje permite o uso do Starlink dentro do território ucraniano, incluindo as regiões ocupadas pela Rússia.
- Ele restringe o uso sobre o território da própria Rússia, argumentando que o uso mais amplo seria uma escalada.
- Zelensky disse em 22 de agosto que Musk "pode mudar de ideia quando vir mais argumentos".
- A SpaceX cortou em fevereiro de 2026 o uso de terminais Starlink por forças russas em território ocupado.
- Zelensky credita a essa decisão parte dos avanços ucranianos no campo de batalha em 2026.
- Os ganhos se deram em operações de drones de "médio alcance", a 50-200 km da linha de frente.
**Fontes:**
- [S68] AP via ABC News — https://abcnews.com/Business/wireStory/zelenskyy-awards-elon-musk-ukraines-order-freedom-starlink-135965792
- [S69] Defence Matters — https://defencematters.eu/ukraine-starlink-russian-missile-launchers/
- [S70] dpa via Yahoo News — https://www.yahoo.com/news/world/articles/kiev-awards-elon-musk-highest-094832277.html
- [S71] The Kyiv Independent — https://kyivindependent.com/zelensky-says-musk-may-change-his-mind-on-using-starlink-against-russian-ballistic-missiles/

## Ucrânia — produção local dos mísseis Storm Shadow/SCALP liberada
- Zelensky disse em 25 de agosto, em entrevista coletiva em Kiev ao lado do presidente da Estônia, Alar Karis, que a Ucrânia recebeu aval de Reino Unido e França para produzir localmente os mísseis de cruzeiro de longo alcance Storm Shadow/SCALP.
- Zelensky afirmou: "Recebemos a confirmação do Reino Unido quanto à produção de mísseis SCALP de longo alcance. Havíamos conversado antes com o presidente Macron, e ele confirmou que os SCALP e a licença haviam sido desbloqueados".
- O SCALP/Storm Shadow é um míssil de cruzeiro franco-britânico.
- O míssil tem alcance de até 250 km (155 milhas).
- Ele foi projetado para ataques de precisão contra alvos fixos à noite e em condições meteorológicas ruins.
- Zelensky disse que a Ucrânia espera em 7 a 10 dias um roteiro de cooperação para o projeto do sistema antibalístico Freyja.
- Ele confirmou entregas futuras de sistemas de defesa aérea Crotale com mísseis VT-1, mísseis AIM e interceptadores Patriot adicionais.
- Separadamente, em 25 de agosto, empresas ucranianas e finlandesas assinaram documentos em uma mesa-redonda em Kiev presidida por Zelensky e pelo presidente finlandês Alexander Stubb.
- Os acordos cobrem produção de drones na Finlândia para a Ucrânia e para a Europa, desenvolvimento de sistemas marítimos não tripulados e a criação de uma fábrica de veículos terrestres não tripulados.
- Moscou reagiu com dureza: o Kremlin chamou a decisão sobre os mísseis de "combustível no fogo" e disse que a Rússia responderia à eventual produção de mísseis na Ucrânia.
**Fontes:**
- [S72] The Kyiv Independent — https://kyivindependent.com/uk-france-approve-storm-shadow-scalp-missile-production-in-ukraine-zelensky-says/
- [S73] RBC-Ukraine — https://newsukraine.rbc.ua/news/britain-and-france-clear-ukraine-to-produce-1787665137.html
- [S74] ArmyInform — https://armyinform.com.ua/en/2026/08/25/ukraine-and-finland-agree-to-produce-drones-unmanned-maritime-systems-and-unmanned-ground-vehicles/
- [S75] The Kyiv Independent — https://kyivindependent.com/ukraine-war-latest-zelensky-confirms-uk-france-approve-producing-scalp-storm-shadow-missiles-in-ukraine/

## FDA — aprovação do Ziihera em primeira linha para câncer gastroesofágico HER2+
- Em 25 de agosto de 2026, a FDA (a agência reguladora de medicamentos dos EUA) aprovou dois esquemas com Ziihera (zanidatamabe-hrii) para tratamento de primeira linha de adenocarcinoma gastroesofágico HER2-positivo irressecável localmente avançado ou metastático.
- Um esquema combina Ziihera com Tevimbra (tislelizumabe) mais quimioterapia; o outro combina Ziihera apenas com quimioterapia.
- O anúncio foi feito pela Jazz Pharmaceuticals (Nasdaq: JAZZ), sediada em Dublin.
- No estudo de fase 3 HERIZON-GEA-01, o esquema com Ziihera, tislelizumabe e quimioterapia alcançou sobrevida global mediana de 26,4 meses.
- O braço de comparação, com trastuzumabe mais quimioterapia, teve sobrevida global mediana de 19,2 meses.
- A redução do risco de morte foi de 28%.
- É a maior sobrevida global mediana já relatada em um estudo de fase 3 nesse cenário, com ganho superior a sete meses.
- As duas combinações com Ziihera reduziram em 35% o risco de progressão da doença ou morte.
- A sobrevida livre de progressão mediana subiu para 12,4 meses, ante 8,1 meses do braço de controle.
- O benefício se manteve independentemente do status de PD-L1.
- Em tumores PD-L1-negativos (TAP abaixo de 1%), a sobrevida global mediana foi de 29,7 meses com a combinação com Tevimbra, contra 15,8 meses no braço de controle.
- O HERIZON-GEA-01 randomizou 914 pacientes.
- O estudo foi conduzido em cerca de 300 centros em mais de 30 países.
- O ensaio foi realizado em conjunto pela Jazz e pela BeOne Medicines.
- A Zymeworks, que originou o zanidatamabe, protocolou em 25 de agosto um Formulário 8-K informando ter recebido um pagamento por marco de US$250 milhões da Jazz com a aprovação.
- A Zymeworks segue elegível a até US$1,3 bilhão em marcos regulatórios e comerciais adicionais.
- A empresa também tem direito a royalties escalonados de 10% a 20%.
- A bula traz alertas de tarja preta para diarreia e toxicidade embriofetal.
- Também foram registradas taxas altas de diarreia, reações relacionadas à infusão e disfunção do ventrículo esquerdo.
- No braço com tislelizumabe, 59% dos 294 pacientes tiveram reações adversas graves.
- Nesse braço, 13% dos pacientes descontinuaram permanentemente o Ziihera.
**Fontes:**
- [S76] Jazz Pharmaceuticals via PR Newswire — https://www.prnewswire.com/news-releases/us-fda-approves-ziihera-zanidatamab-hrii-with-and-without-tislelizumab-plus-chemotherapy-in-first-line-her2-advanced-gastroesophageal-adenocarcinoma-302859470.html
- [S77] BioSpace — https://www.biospace.com/press-releases/beone-medicines-announces-u-s-fda-approval-for-tevimbra-based-regimen-for-first-line-her2-gea
- [S78] StockTitan — https://www.stocktitan.net/sec-filings/JAZZ/8-k-jazz-pharmaceuticals-plc-reports-material-event-b63b45c73748.html
- [S79] Nova Pharma News — https://novapharmanews.com/us/news/ziihera-1l-her2-gea-fda-approval

## República Democrática do Congo — surto de Ebola Bundibugyo passa de 5.650 casos
- Em 25 de agosto de 2026, a República Democrática do Congo relatou 5.656 casos confirmados de vírus Bundibugyo, com dados até 24 de agosto.
- Foram registradas 2.715 mortes relacionadas.
- Isso representa aumento de 72 casos confirmados e 35 mortes em um único dia, em relação ao boletim anterior, de 24 de agosto.
- Há 792 pacientes hospitalizados em isolamento.
- São 58 de 151 zonas sanitárias afetadas, distribuídas por seis províncias.
- Ituri segue como epicentro, com 4.716 casos e 2.119 mortes.
- A OMS afirmou que o surto se tornou o de crescimento mais rápido já registrado na RDC.
- A média foi de cerca de 90 casos confirmados por dia nos três primeiros meses.
- Esse ritmo é bem superior ao observado no mesmo período dos surtos da África Ocidental de 2014-2016 e da RDC de 2018-2020.
- A espécie Bundibugyo envolvida não tem vacina licenciada nem tratamento específico.
- A taxa de letalidade estava em 47% em meados de agosto.
- Já foram relatados casos importados em Uganda, França e Alemanha.
- O Comitê de Emergência do Regulamento Sanitário Internacional (RSI) da OMS se reuniu pela segunda vez em 18 de agosto.
- Em 24 de agosto, o comitê publicou recomendações temporárias atualizadas.
- As recomendações incluem uma nova seção sobre medidas sociais, grandes aglomerações e mobilidade doméstica.
- O Secretariado da OMS classifica o risco como "muito alto" para a RDC.
- A capacidade laboratorial passou de um único posto de testagem para 19 laboratórios, capazes de processar mais de 3.000 amostras por dia.
- A capacidade de tratamento subiu de menos de 10 leitos para mais de 1.300.
- O acompanhamento de contatos subiu de 9% na primeira semana do surto para 84% até 18 de agosto.
**Fontes:**
- [S80] ECDC — https://www.ecdc.europa.eu/en/ebola-outbreak-democratic-republic-congo-and-uganda
- [S81] WHO Regional Office for Africa — https://www.afro.who.int/countries/democratic-republic-of-congo/news/over-5200-cases-recorded-democratic-republic-congocrosses100-days-ebola-outbreak-declaration
- [S82] WHO — https://www.who.int/publications/m/item/who-rapid-risk-assessment-ebola-disease-caused-by-bundibugyo-virus--democratic-republic-of-the-congo-v4
- [S83] WHO — https://www.who.int/news/item/24-08-2026-second-meeting-of-the-ihr-emergency-committee-on-the-epidemic-of-ebola-bundibugyo-virus-disease-in-the-democratic-republic-of-the-congo-temporary-recommendations

## Meta — acordo bilionário com procuradores estaduais sobre segurança de adolescentes
- A Meta anunciou em 26 de agosto de 2026 um acordo com um grupo bipartidário de 52 procuradores-gerais de estados, territórios e do Distrito de Columbia dos EUA.
- O acordo encerra o litígio sobre segurança infantil no meio do julgamento.
- As fontes divergem sobre o valor principal.
- O comunicado da própria Meta fala em pagamento de aproximadamente US$18 bilhões.
- O pagamento seria feito em parcelas anuais ao longo de 10 anos.
- Segundo a Meta, cerca de 70% da soma (aproximadamente US$12,7 bilhões) vai para os estados participantes ao longo da década.
- Os 30% restantes (aproximadamente US$5,3 bilhões) só serão liberados sob duas condições.
- A primeira condição é que YouTube e TikTok implementem limite diário de uma hora, Modo Noturno e medidas de verificação de idade.
- A segunda condição é que YouTube e TikTok paguem, cada um, valor equivalente à parcela de 30%.
- Metade da parcela está atrelada ao pagamento do YouTube e metade ao do TikTok.
- A Meta vai contabilizar despesa legal de cerca de US$10 bilhões no terceiro trimestre de 2026 por causa do acordo.
- A empresa diz que essa despesa não estava contemplada na faixa de gastos informada na teleconferência de resultados do segundo trimestre.
- O The Verge, lendo os termos do acordo, calcula o pagamento em US$17,1 bilhões ao longo de 10 anos, com os mesmos US$5,3 bilhões condicionados a YouTube e TikTok.
- Segundo o The Verge, o julgamento do qual a Meta escapou poderia lhe custar centenas de bilhões de dólares.
- O documento judicial afirma que a Meta concordou em pagar até US$16,68 bilhões.
- O mesmo documento diz que a empresa "nega as alegações contra ela e nega ter qualquer responsabilidade perante os autores".
- Os autores da ação no documento são um conjunto de 29 estados.
- O gabinete do procurador-geral da Califórnia, Rob Bonta, descreve o valor como US$17 bilhões ao longo de 10 anos, resolvendo reivindicações de 51 procuradores-gerais.
- O acordo obriga a Meta a aceitar um auditor independente com "acesso amplo a informações e recursos".
- A empresa também fica sujeita a uma liminar que proíbe novas declarações falsas, enganosas ou fraudulentas sobre seus recursos de segurança.
- Entre os termos de produto: limite diário padrão de duas horas, cumulativo entre Facebook e Instagram, que adolescentes só podem desativar com permissão de um responsável.
- O limite é contado mesmo quando o usuário tem várias contas detectadas.
- O Modo Noturno bloqueia por padrão o acesso à meia-noite até as 6h, cobrindo Feed, Stories, Explore e Reels.
- Também é exigido o "School Mode": notificações silenciadas por padrão entre 8h e 15h.
- O acordo prevê avisos a cada 15 minutos de uso contínuo e aos 60 e 90 minutos de uso diário.
- Adolescentes poderão escolher um feed não algorítmico, que passa a ser a opção padrão por adesão.
- Contagens de curtidas ficam ocultas e a reprodução automática de vídeos fica desligada.
- Filtros de cirurgia plástica e de maquiagem extrema ficam proibidos para adolescentes.
- Mensagens diretas estão excluídas das restrições de limite de tempo, Modo Noturno e School Mode.
- A Meta terá de criar um padrão de verificação de idade sujeito a testes independentes.
- A taxa de falsos positivos não pode passar de 10% para usuários de 16 e 17 anos e de 3% para usuários de 13 a 15 anos.
- A empresa deve incorporar sinais de idade dos sistemas operacionais e lojas de aplicativos da Apple e do Google.
- Usuários que se declararem maiores de 18 anos e não concluírem o teste de verificação de idade em duas semanas terão restrições na conta e recomendações de conteúdo adequadas à faixa etária.
- As restrições visam impedir que adultos mal-intencionados contatem adolescentes.
- A Meta também deve tentar vincular contas de um mesmo usuário para evitar burla das novas regras.
- A empresa deve oferecer um processo de recurso aos usuários.
- A maioria dos termos deve permanecer em vigor por 10 anos.
- As proteções se aplicam automaticamente a menores de 18 anos no Instagram e no Facebook nos estados e territórios participantes, sujeito à homologação judicial.
- C.J. Mahoney, diretor jurídico da Meta, cobrou publicamente que TikTok e YouTube adotem o mesmo modelo "imediatamente", porque adolescentes transitam por dezenas de aplicativos.
- Mahoney disse: "Nossos novos compromissos de Limite de Tempo, os recursos de Modo Noturno e os limites de uso durante o horário escolar apontam o caminho certo para todo o nosso setor, mas esse arcabouço só vai funcionar se todos os nossos pares se juntarem a nós".
- O acordo saiu no meio da segunda semana de um julgamento federal em Oakland movido por 29 estados.
- A ação é coliderada por Califórnia, Colorado, Kentucky e Nova Jersey.
- As ações da Meta subiram cerca de 5% na negociação pré-mercado.
- A Califórnia sozinha pode receber de US$1,5 bilhão a US$2,1 bilhões, se o tribunal homologar o acordo.
- O julgamento começou em 18 de agosto de 2026, em tribunal federal em Oakland, na Califórnia, e deveria se estender até o início de outubro.
- Mark Zuckerberg era esperado para depor.
- Adam Mosseri, chefe do Instagram, havia deposto na véspera do acordo.
**Fontes:**
- [S84] Meta Newsroom — https://about.fb.com/news/2026/08/agreement-with-state-attorneys-general-supporting-teens/
- [S85] The Verge — https://www.theverge.com/policy/985032/meta-state-ag-kids-online-safety-settlement
- [S86] NPR — https://www.npr.org/2026/08/26/nx-s1-5944781/meta-settlement-child-safety-lawsuit
- [S87] NBC News — https://www.nbcnews.com/tech/social-media/meta-settles-social-media-addiction-suit-16-billion-rcna594492
- [S88] CNBC — https://www.cnbc.com/2026/08/26/meta-social-media-trial-settlement.html

## Pensilvânia — processo contra a Snap pelo design do Snapchat
- O procurador-geral da Pensilvânia, Dave Sunday, processou a Snap Inc. em 25 de agosto de 2026.
- A ação acusa a empresa de não proteger crianças do uso compulsivo do Snapchat.
- A acusação inclui mentir sobre a frequência com que conteúdo adulto aparece no aplicativo.
- A alegação é que a Snap mente sobre a frequência de material adulto, como uso de drogas ou conteúdo sexual, para manter a classificação 13+ nas lojas de aplicativos.
- A petição tem 49 páginas.
- O processo foi protocolado no Tribunal de Causas Comuns da Filadélfia.
- A base legal é a Unfair Trade Practices and Consumer Protection Law (UTPCPL), a lei de práticas comerciais desleais e proteção ao consumidor da Pensilvânia.
- A ação pede tutela declaratória, liminar permanente, penalidades civis por violações intencionais e custas.
- A acusação central é que a Snap responde ao questionário de classificação etária da App Store da Apple de modo a obter a classificação 13+.
- A mesma prática rende classificação "Teen" no Google Play e na Microsoft Store.
- Segundo a ação, conteúdo sexual, referências a drogas e temas adultos estão facilmente disponíveis e chegam a ser recomendados a usuários que a empresa sabe ter 13 anos.
- A petição aponta mecânicas específicas de engajamento como indutoras deliberadas de vício comportamental em menores: conteúdo efêmero, rolagem infinita, notificações push, reprodução automática, Snapscores e Snapstreaks.
- Sunday disse que o recurso de sequências (streaks) "atribui um valor tangível às amizades e influencia o sentimento de autoestima de uma criança".
- Ele afirmou que o objetivo final da ação é uma revisão completa de como o Snapchat é comercializado e anunciado.
- É o segundo processo de Sunday contra uma empresa de redes sociais no mês.
- Ele processou o TikTok em 11 de agosto de 2026, com fundamentos semelhantes de proteção ao consumidor.
- Sunday disse que seu gabinete está "olhando ativamente para outras empresas também".
- A petição afirma que os usuários abrem o Snapchat em média 30 vezes por dia.
- Dados do Pew Research Center citados na coletiva indicam que 55% dos adolescentes americanos usam o Snapchat.
- Isso equivale a cerca de 450 mil dos 807 mil adolescentes da Pensilvânia.
- A Snap rejeitou a ação, dizendo que as alegações "distorcem fundamentalmente" a plataforma.
- A empresa observou que o Snapchat abre em uma câmera, e não em um feed de conteúdo, e foi construído para incentivar a autoexpressão e a conexão autêntica com amigos.
- A Pensilvânia se junta a pelo menos outros sete estados que já moveram ações judiciais contra a Snap por falhas de segurança infantil.
- Entre esses estados estão Arkansas, Flórida, Kansas, Nevada, Novo México e Texas.
**Fontes:**
- [S89] The Hill — https://thehill.com/policy/technology/6050412-pa-attorney-general-snapchat-lawsuit/
- [S90] Commonwealth of Pennsylvania, Office of Attorney General — https://wjactv.com/resources/pdf/8a251700-24f8-414f-92a2-102efa4bb1df-20260825PAv.SnapchatComplaintvfPublicRedacted.pdf
- [S91] City & State Pennsylvania — https://www.cityandstatepa.com/politics/2026/08/snap-decision-ag-sunday-files-lawsuit-against-social-media-giant-over-lack-teen-safeguards/415633/
- [S92] Bloomberg Law — https://news.bloomberglaw.com/litigation/pennsylvania-sues-snapchat-over-childrens-compulsive-app-usage
