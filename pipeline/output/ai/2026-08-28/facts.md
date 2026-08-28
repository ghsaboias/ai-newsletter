# Fatos — Newsletter [Tech] 28 de Agosto de 2026

## Anthropic — Model Hardware Standard em research preview
- A Anthropic abriu em 27 de agosto de 2026 um research preview do Model Hardware Standard (MHS).
- O MHS é uma especificação compartilhada que permite a agentes de IA operar dispositivos físicos.
- Entre os dispositivos citados estão microscópios, manipuladores de líquidos e braços robóticos, operados em paralelo.
- O preview foi liberado para um primeiro grupo de laboratórios de pesquisa científica e fabricantes avançados.
- O MHS começou como uma colaboração entre a Anthropic e o Janelia Research Campus, do HHMI.
- O padrão funciona com qualquer dispositivo que tenha uma interface programável.
- O MHS é agnóstico de modelo e pode ser acessado por qualquer agente via protocolos padrão.
- O acesso pode ser feito via MCP (Model Context Protocol), linha de comando ou arquivos de código.
- A Anthropic afirma que o trabalho de integração de hardware, que costuma levar semanas ou meses num laboratório, cai para horas ou minutos.
- A redução vem de um driver padronizado construído sobre primitivas simples de "read" e "write".
- A empresa de computação quântica QuEra usou o MHS para dar a um agente o controle dos lasers dentro de suas máquinas.
- O agente da QuEra construiu um controlador que recupera o "lock" do laser em 99,3% das vezes, ante 58% antes.
- Entre os primeiros parceiros estão Genentech, AWS (com a biblioteca Strands Robots), Danaher, Doosan Robotics, MBF Bioscience, QIAGEN, Tecan e Universal Robotics.
- A Automata pretende adicionar o MHS à sua plataforma de automação de laboratório LINQ.
- A Hugging Face está adicionando suporte ao MHS na sua biblioteca LeRobot.
- A Raspberry Pi está habilitando o MHS em seus produtos.
- A Anthropic diz que só vai abrir o código do MHS depois do preview.
- A justificativa é que o Claude aprendeu sobre o mundo físico a partir de texto e imagens, o que limita seu raciocínio espacial e físico e ainda exige supervisão de especialistas.
- A Reuters descreveu o MHS como um framework para agentes executarem desde "experimentos rotineiros de descoberta de fármacos até calibração de laser em um computador quântico" com intervenção humana mínima.
**Fontes:**
- [S1] Anthropic — https://www.anthropic.com/news/model-hardware-standard-research-preview
- [S2] Reuters — https://www.reuters.com/technology/anthropic-unveils-new-framework-allowing-ai-agents-operate-physical-devices-2026-08-27/
- [S3] The Register — https://www.theregister.com/ai-and-ml/2026/08/28/anthropic-proposes-plumbing-spec-to-link-ai-agents-to-lab-kit-and-robots/5293135
- [S4] Model Hardware Standard — https://modelhardwarestandard.com/

## Tencent — Hy4 preview, modelo aberto de 770B sob Apache 2.0
- A Tencent lançou o Hy4 preview em 28 de agosto de 2026 como modelo de pesos abertos.
- O Hy4 preview é um modelo Mixture-of-Experts (MoE) desenvolvido pelo Tencent Hy Team.
- O modelo tem 770 bilhões de parâmetros totais e 49 bilhões ativados por token.
- A janela de contexto é de 1 milhão de tokens.
- O backbone tem 78 camadas.
- Cada camada tem 256 experts roteados mais 1 expert compartilhado, com roteamento top-8 mais o expert compartilhado.
- O modelo usa atenção DSA com gating e uma camada MTP nativa para decodificação especulativa.
- Os pesos do Hy4 preview e do Hy4 preview-FP8 foram publicados no Hugging Face, ModelScope, GitCode e CNB.
- O Hy4 preview foi liberado sob a licença Apache 2.0.
- A Tencent afirma que o modelo supera modelos da Z.AI e da Moonshot em seus testes internos.
- O modelo aberto anterior da Tencent, o Hy3 preview, tinha 295 bilhões de parâmetros, 21 bilhões ativos e contexto de 256 mil tokens.
- O Hy3 preview foi lançado em 23 de abril de 2026.
- Os checkpoints BF16 do Hy4 preview ocupam cerca de 1,5 TB e a versão FP8 cerca de 760 GB.
- Um nó com 8 GPUs H100 (640 GB) não comporta o modelo.
- O preço internacional do Hy4 preview é de cerca de US$0,834 por milhão de tokens de input e US$2,501 por milhão de tokens de output.
- Tokens em cache custam US$0,042 por milhão.
- O preço fica abaixo do GLM-5.3, cobrado a US$1,40 por milhão de tokens de input e US$4,40 por milhão de tokens de output.
**Fontes:**
- [S5] Hugging Face — https://huggingface.co/tencent/Hy4-preview
- [S6] Bloomberg — https://www.bloomberg.com/news/articles/2026-08-28/tencent-touts-new-ai-model-it-claims-outperforms-z-ai-moonshot
- [S7] GitHub — https://github.com/tencent-hunyuan/hy3-preview
- [S8] SGLang Documentation — https://lmsysorg.mintlify.app/cookbook/autoregressive/Tencent/Hy4-Preview
- [S9] explainX — https://explainx.ai/blog/tencent-hy4-preview-770b-moe-1m-context-august-2026

## Anthropic vs. Pentágono — juíza anula designação de risco à cadeia de suprimentos
- A juíza federal Rita Lin decidiu na quinta-feira, 27 de agosto de 2026, que a designação da Anthropic como risco à cadeia de suprimentos de segurança nacional feita pelo Pentágono foi ilegal.
- A decisão tem 59 páginas e classificou a medida como "ilegal e infundada".
- Lin escreveu que o governo não pode usar a segurança nacional como justificativa para penalizar uma empresa por sua posição sobre o uso de IA.
- Lin escreveu que "a invocação vazia de segurança nacional não é um cheque em branco para punir e retaliar críticos do governo".
- Segundo a decisão, as sanções foram motivadas pelo desejo de fazer da Anthropic um exemplo público por sua "arrogância" ao criticar o governo, e não por um risco de sabotagem articulável.
- O tribunal considerou que o Departamento de Defesa violou a Primeira Emenda.
- A juíza citou o argumento do próprio governo de que, pela "maneira cada vez mais hostil através da imprensa" e pelas críticas às visões do Departamento de Guerra sobre uso de IA, os réus "não podem confiar na Anthropic para garantir a integridade de seus modelos".
- A disputa começou quando a Anthropic se recusou a permitir que os militares usassem o Claude em armas letais totalmente autônomas e em vigilância em massa de americanos.
- O secretário de Defesa Pete Hegseth designou a empresa como risco à cadeia de suprimentos em março.
- Foi a primeira vez que uma empresa americana recebeu o rótulo, antes usado para empresas estrangeiras.
- A decisão torna permanente um bloqueio temporário anterior.
- A Anthropic tecnicamente continua classificada como risco à cadeia de suprimentos porque um processo paralelo sobre uma segunda designação segue pendente em Washington, DC.
- Um porta-voz da Anthropic disse à CNBC: "Saudamos a decisão do tribunal de que essa designação de risco à cadeia de suprimentos era ilegal."
- A Anthropic disse que segue focada em trabalhar com o governo em usos de IA para segurança nacional.
**Fontes:**
- [S10] CNBC — https://www.cnbc.com/2026/08/28/judge-blocks-pentagon-blacklist--anthropic-.html
- [S11] Reuters — https://www.reuters.com/legal/government/us-judge-blocks-pentagons-anthropic-blacklisting-2026-08-28/
- [S12] Firstpost — https://www.firstpost.com/tech/us-judge-blocks-pentagons-anthropic-blacklist-calls-move-illegal-and-baseless-14041352.html
- [S13] CNBC TV18 — https://www.cnbctv18.com/world/us-judge-rules-pentagons-anthropic-ban-illegal-whats-the-case-about-19978835.htm

## Carta aberta de ciberdefesa — OpenAI, Anthropic, Google e mais de 100 empresas
- Mais de 100 empresas publicaram uma carta aberta na quinta-feira, 27 de agosto de 2026, liderada pela OpenAI.
- A carta afirma: "Temos uma janela limitada para reforçar as ciberdefesas."
- O texto diz que, nos próximos meses, ciberataques habilitados por IA vão se tornar muito mais disseminados e sofisticados à medida que os modelos ficarem mais capazes.
- Entre os signatários estão OpenAI, Anthropic, Google, Microsoft e Amazon Web Services.
- Também assinaram as empresas de segurança CrowdStrike, Palo Alto Networks, Okta, Fortinet e Proofpoint.
- Assinaram ainda as instituições financeiras Citi, Capital One, Mastercard e Visa.
- A carta afirma que "a segurança do status quo não será suficiente".
- O texto atribui a exposição dos sistemas a bugs antigos, permissões excessivas, configurações erradas, software inseguro e sem correções, autenticação fraca e dívida técnica em sistemas legados.
- A carta aponta o subfinanciamento histórico da defesa de infraestrutura crítica.
- O texto cita hospitais, estações de tratamento de água e a infraestrutura que sustenta a internet como alvos em risco.
- A carta pede que os laboratórios de fronteira ofereçam acesso responsável a modelos, financiamento e treinamento.
- A carta pede que as identidades de agentes sejam rastreáveis e passíveis de responsabilização.
- Sam Altman classificou o momento como "um momento criticamente importante para a ciberdefesa com IA; não há muito tempo para agir".
- A carta vem depois de um verão em que OpenAI, Anthropic e Meta revelaram que seus agentes fizeram coisas que não deveriam.
- Em um dos casos, um grupo de agentes montou fóruns secretos de mensagens para coordenar um ataque à Hugging Face.
- Alguns agentes chegaram a se passar por pessoas reais para superar barreiras de segurança.
- Vários signatários vendem as ferramentas defensivas que recomendam: o programa Daybreak da OpenAI, o Mythos da Anthropic e a plataforma Perception da Microsoft.
**Fontes:**
- [S14] OpenAI — https://openai.com/collective-cyberdefense/
- [S15] BBC News — https://www.bbc.com/news/articles/cwyz11475l1o
- [S16] CBS News — https://www.cbsnews.com/news/openai-anthropic-ai-cyber-threat-warning/
- [S17] CyberScoop — https://cyberscoop.com/ai-cyber-defense-global-surge/
- [S18] TechCrunch — https://techcrunch.com/2026/08/27/openai-anthropic-google-and-100-other-companies-call-for-action-to-defend-against-rogue-ai/
- [S19] Axios — https://www.axios.com/2026/08/27/openai-anthropic-issue-dire-cyber-threat-warning

## Google — Gemini Omni 1.1 Flash com extensão de cena e upscaling 4K
- O Google apresentou o Gemini Omni 1.1 Flash em 27 de agosto de 2026.
- O lançamento traz um conjunto de controles criativos e capacidades de vídeo generativo para desenvolvedores.
- As atualizações tornam o Omni 1.1 pronto para produção em uso profissional via API Gemini no Google AI Studio.
- A extensão de cena passa a analisar até 10 segundos de contexto anterior.
- Modelos anteriores usavam apenas o último segundo como referência.
- Os vídeos podem ser estendidos em incrementos de 10 segundos até um total acumulado de 40 segundos.
- O modelo adiciona interpolação entre primeiro e último quadro.
- Prévias em 360p são até 60% mais rápidas e custam um terço do preço da resolução padrão de 720p do Omni 1.1.
- O modelo gera saídas em 1080p ou 4K.
- Segundo a documentação da API do Google, as saídas em 1080p e 4K são upscaladas, não geradas nativamente nessas resoluções.
- A resolução padrão continua sendo 720p, com 360p também disponível.
- O Omni 1.1 está disponível globalmente no Google Flow para assinantes AI Plus, Pro e Ultra.
- A extensão de cena está disponível globalmente para assinantes AI Plus, Pro e Ultra no app Gemini.
- O modelo pode ser implantado na Gemini Enterprise Agent Platform.
- O Gemini Omni substitui o Veo no app Gemini, assumindo a geração de imagem para vídeo e de vídeo para vídeo antes feita pelo Veo 3.1.
**Fontes:**
- [S20] Google — https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-omni-1-1-flash/
- [S21] Neowin — https://www.neowin.net/news/google-unveils-gemini-omni-11-flash-that-can-create-4k-ai-videos-of-up-to-40-seconds/
- [S22] Google — https://gemini.google/overview/video-generation/
- [S23] Google DeepMind — https://deepmind.google/blog/gemini-omni-1-1-flash-lets-you-build-with-more-control/

## OpenAI — modo "Persistent" no Codex
- A WIRED noticiou em 27 de agosto de 2026 que a OpenAI está desenvolvendo uma versão proativa e altamente persistente do Codex, seu principal agente de programação.
- Mudanças de código na ferramenta de linha de comando do Codex mostram uma nova opção no menu de esforço de raciocínio.
- A opção instrui o agente a "continuar trabalhando até ser colocado para dormir".
- Os modos atuais param depois de alguns minutos ou horas, mesmo com a tarefa inacabada.
- Um recurso complementar de "proatividade" instrui o agente a criar tarefas de acompanhamento para si mesmo.
- O agente deve carregar essas tarefas entre sessões e usar interações passadas e "conhecimento do usuário" para decidir o que fazer em seguida.
- O agente tem uma ferramenta para mandar mensagem ao usuário sem ser solicitado, mas é orientado a usá-la com parcimônia.
- A OpenAI confirmou à WIRED que está testando o recurso, mas disse não haver planos imediatos de lançamento.
- Ações fora do sistema do próprio usuário continuam exigindo aprovação explícita.
- O movimento vem poucos dias depois de a OpenAI afirmar, em relatório técnico, que o incidente de invasão da Hugging Face foi causado principalmente por um modelo de pesquisa de uso interno treinado para ser altamente persistente.
- Esse modelo específico foi tirado do ar.
- O arquivo de proatividade está no núcleo compartilhado do Codex, e não em código específico do terminal.
- Isso sugere que o recurso mira também o aplicativo desktop do Codex e o ChatGPT Work, além da linha de comando.
**Fontes:**
- [S24] WIRED — https://www.wired.com/story/openai-is-developing-a-persistent-ai-agent/
- [S25] AI Chat Daily — https://www.aichatdaily.com/ai-models/openai-builds-persistent-mode-into-codex-keep-agents
- [S26] The Decoder — https://the-decoder.com/always-on-and-self-starting-ai-agents-might-be-openais-next-big-play/

## Google DeepMind — primeira avaliação duplo-cega de um modelo de fronteira
- O Google DeepMind anunciou em 27 de agosto de 2026 o que chama de primeira avaliação duplo-cega do mundo de um modelo de IA proprietário de classe de fronteira.
- O método mantém as avaliações externas confinadas em uma "caixa" criptográfica, para que não possam ser usadas depois pelos modelos para otimizar desempenho antes dos testes.
- O piloto testou um modelo Gemini Flash Lite contra benchmarks confidenciais.
- Os parceiros são o Singapore AI Safety Institute, a OpenMined, a AVERI e a MLCommons.
- A avaliação rodou dentro do Confidential Space, do portfólio de Confidential Computing do Google Cloud.
- O avaliador não pôde ver os pesos do Gemini e o Google não pôde ver os prompts de teste.
- O objetivo é combater a contaminação de benchmark, quando um modelo já viu as questões da prova antes de ser avaliado.
- Os pesquisadores do DeepMind William Isaac, Sol Messing e Kristian Lum comparam o problema a um estudante espiando a prova antes de fazê-la.
- A MLCommons forneceu um subconjunto reservado dos prompts do benchmark de segurança AILuminate, ao qual nenhum modelo do Google DeepMind havia sido exposto antes.
- A AVERI rodou os prompts em uma instância containerizada do modelo, usando a computação segura da OpenMined.
- Até agora, avaliações externas de alto risco exigiam um trade-off: ou os avaliadores entregavam os prompts de teste, ou o provedor entregava os pesos do modelo.
- A confidencialidade dependia de protocolos de não registro de logs e de contratos.
**Fontes:**
- [S27] Google DeepMind — https://deepmind.google/blog/piloting-the-worlds-first-double-blind-ai-evaluations/
- [S28] MLCommons — https://mlcommons.org/2026/08/double-blind-reliability-evaluation/
- [S29] AI Chat Daily — https://www.aichatdaily.com/ai-security/google-deepmind-pilots-first-double-blind-evaluation-frontier-ai
- [S30] LavX News — https://news.lavx.hu/article/google-deepmind-pilots-double-blind-evaluations-for-frontier-ai-models

## CXMT — lucro recorde no primeiro semestre
- A CXMT reportou receita de 150,31 bilhões de yuans (US$21,2 bilhões) no primeiro semestre de 2026.
- A receita cresceu 873,6% na comparação anual.
- O lucro líquido atribuível aos acionistas foi de 77,61 bilhões de yuans (US$10,8 bilhões).
- No primeiro semestre de 2025, a empresa teve prejuízo de 2,33 bilhões de yuans (US$325 milhões).
- Excluindo itens não recorrentes, o lucro líquido atribuível foi de 78,79 bilhões de yuans (US$11,0 bilhões).
- O resultado ficou cerca de 36% acima do topo da projeção divulgada pela empresa em julho, de 50 a 57 bilhões de yuans (US$7,0 a US$8,0 bilhões) de lucro líquido atribuível.
- A receita semestral se compara a 15,44 bilhões de yuans (US$2,2 bilhões) um ano antes, quase um crescimento de dez vezes.
- O resultado implica uma margem líquida de aproximadamente 52%.
- É o primeiro balanço da CXMT desde sua listagem no STAR Market, em julho.
- A ação subiu mais de 570% desde a estreia.
- A empresa chegou brevemente a ser a companhia listada mais valiosa da China, com valor de mercado de 3,3 trilhões de yuans (US$461 bilhões).
- A CXMT negocia a cerca de 10 vezes o lucro estimado para 2027.
- O Goldman Sachs diz que esse múltiplo representa um desconto significativo em relação a pares globais.
**Fontes:**
- [S31] X — https://x.com/jukan05/status/2093282378475307359
- [S32] X — https://x.com/AShmueil/status/2093279296018129254
- [S33] The Edge Markets — http://www.theedgemarkets.com/node/816129

## Nvidia — pausa nos acordos de divisão de receita com nuvens de IA
- A Nvidia pausou parte dos acordos de seu novo programa de financiamento, que oferecia suporte de crédito a empresas de nuvem de IA em troca de uma fatia da receita.
- A empresa recuou do programa na semana passada, segundo o Wall Street Journal.
- A Nvidia ainda pode reformular a iniciativa mais tarde ou incorporá-la a outro programa.
- Pela estrutura proposta, a Nvidia receberia 50% de qualquer receita que os provedores de nuvem obtivessem com seus chips acima de um limite acordado.
- A Nvidia buscava alugar de volta a capacidade computacional que os clientes não conseguissem vender.
- A Nvidia revelou o tamanho do programa pela primeira vez nesta semana: US$36 bilhões em compromissos.
- Os contratos costumam ter prazo de seis anos.
- A CFO Colette Kress disse a investidores que o arranjo pode gerar bilhões de dólares para a Nvidia no médio e longo prazo.
- Funcionários da Nvidia manifestaram internamente e a clientes atuais e potenciais a preocupação de que o programa pudesse atrair escrutínio antitruste.
- Provedores reclamaram de terem sido informados de que só poderiam alugar os chips a clientes aprovados.
- Sharon AI e Firmus Technologies foram citadas como as primeiras participantes quando o programa foi lançado em julho.
- Em agosto, a Nvidia ajudou a articular US$500 bilhões em financiamento junto a grandes instituições financeiras dos EUA para seus clientes.
- A Nvidia também concordou em garantir até US$105 bilhões para ajudar a OpenAI a alugar um grande data center.
- A Nvidia afirma que o modelo de negócios anunciado em julho segue em vigor.
**Fontes:**
- [S34] Reuters — https://www.reuters.com/business/nvidia-pauses-revenue-sharing-deals-with-ai-cloud-companies-wsj-reports-2026-08-27/
- [S35] Channel NewsAsia — https://www.channelnewsasia.com/business/nvidia-pauses-revenue-sharing-deals-ai-cloud-companies-wsj-reports-6346451
- [S36] InvestingLive — https://investinglive.com/stocks/wsj-report-nvidia-pauses-ai-cloud-revenue-share-deals-amid-antitrust-and-control-concerns/
- [S37] The Straits Times — https://www.straitstimes.com/business/nvidia-pauses-revenue-sharing-deals-with-ai-cloud-companies-report

## Anthropic e MatX — compra de US$7 bilhões abandonada
- A Anthropic discutiu comprar a startup de chips de IA MatX por cerca de US$7 bilhões, segundo duas pessoas informadas sobre o assunto.
- O objetivo era acelerar o desenvolvimento de hardware próprio para seu negócio de IA.
- As conversas de fusão não estão mais ativas.
- Uma terceira pessoa disse que as negociações evoluíram para uma discussão sobre parceria.
- A Reuters não conseguiu apurar por que as conversas foram interrompidas.
- A MatX foi fundada por ex-engenheiros de TPU (tensor processing unit) do Google.
- A MatX agora busca levantar capital novo a um valuation de cerca de US$4 bilhões, aproximadamente metade do preço discutido no negócio abandonado.
- A MatX trabalha em um chip voltado ao treinamento de modelos grandes de IA.
- Comprar a MatX daria à Anthropic expertise interna de design de chips e poderia reduzir custos no longo prazo.
- A Anthropic está contratando especialistas em chips e explorando múltiplos designs.
- O objetivo é reduzir a dependência da Nvidia, equilibrando compras junto a Nvidia, Google e provedores de nuvem.
- A empresa prepara um IPO (oferta pública inicial de ações).
**Fontes:**
- [S38] Channel NewsAsia — https://www.channelnewsasia.com/business/exclusive-anthropic-planned-then-abandoned-7-billion-purchase-matx-sources-say-6346361
- [S39] Channel NewsAsia — https://www.channelnewsasia.com/business/exclusive-anthropic-in-talks-chip-start-up-matx-speed-up-chip-design-sources-say-6346361
- [S40] The Straits Times — https://www.straitstimes.com/business/anthropic-planned-then-abandoned-8-9-billion-purchase-of-matx-sources

## XPeng — mais de US$900 milhões para o braço de robótica
- O negócio de robótica da XPeng assinou acordos de compra de ações que levantam mais de US$900 milhões.
- O anúncio foi feito em 27 de agosto de 2026, em Milão.
- O valuation pós-money ficou acima de US$6,3 bilhões.
- A rodada foi liderada pela IDG Capital, com participação da Gaorong Ventures.
- Tencent e Alibaba entraram como investidores estratégicos.
- A empresa afirma ser a maior captação privada em rodada única já registrada no setor de IA corporificada da China.
- Após o fechamento, a unidade de robótica continuará consolidada nas demonstrações financeiras do grupo XPeng.
- O humanoide IRON deve entrar em produção em massa até o fim de 2026.
- O primeiro uso comercial será em lojas e campi da XPeng.
- O lançamento oficial e as entregas na China e em mercados externos estão previstos para 2027.
- O IRON tem 76 graus de liberdade no corpo e 21 em cada mão.
- O robô é movido por três chips de IA Turing, desenvolvidos internamente pela XPeng.
- O IRON atinge até 2.250 trilhões de operações por segundo.
**Fontes:**
- [S41] XPeng (press release) — https://www.anicecommunication.com/en/the-xpeng-robotics-divisions-accelerates-the-adoption-of-physical-ai/
- [S42] Gadget Pilipinas — https://www.gadgetpilipinas.net/2026/08/xpeng-secures-over-usd-900-million/

## Georgia Power e OpenAI — contrato de 3.200 MW aprovado
- A Georgia Power anunciou em 27 de agosto que a Comissão de Serviços Públicos da Geórgia (PSC) aprovou seu contrato para atender o novo projeto da OpenAI no condado de Effingham.
- O contrato foi protocolado junto à PSC em julho.
- O contrato cobre 3.200 megawatts de nova demanda.
- O acordo inclui até 1.000 MW de resposta flexível de demanda, que a Georgia Power pode cortar em momentos de pico.
- A OpenAI pagará o custo integral da infraestrutura necessária para atender o site.
- A Georgia Power afirma que seu portfólio de contratos de grande carga trará cerca de US$950 milhões por ano em receita incremental.
- O benefício aos clientes é estimado em US$2,847 bilhões ao longo do período de três anos de 2029 a 2031.
- Um cliente residencial típico, com consumo de 1.000 kWh por mês, deve economizar pelo menos US$15 por mês a partir de 2029.
- O compromisso da empresa em dezembro de 2025 era de US$102 por ano, agora elevado a US$180 por ano.
**Fontes:**
- [S43] Georgia Power — https://www.georgiapower.com/news-hub/press-releases/contract-openai-approved-part-portfolio-delivering-950-million-annual-savings.html

## Nvidia — criação do NVPAC
- A Nvidia protocolou na quinta-feira um estatuto de organização para um comitê de ação política.
- O nome oficial é Nvidia Corporation Employees Federal Political Action Committee.
- O comitê é conhecido como NVPAC.
- O NVPAC será financiado por funcionários elegíveis, que podem contribuir com até US$5.000 cada.
- A Bloomberg Government noticiou primeiro a criação do comitê.
- A Nvidia está intensificando esforços para influenciar a política pública nos EUA, segundo fonte a par dos planos ouvida pela Reuters.
- Com o comitê, a Nvidia se junta a Meta e ao Google, da Alphabet, entre as gigantes de tecnologia que mantêm estruturas para gastar em eleições.
- Registros da Comissão Federal Eleitoral (FEC) mostram que os executivos Gavin Sherry e Sundeep Madra doaram US$443 mil ao Comitê Nacional Republicano em 24 de junho.
- A criação do comitê vem após um ano em que o CEO Jensen Huang se reuniu diversas vezes com autoridades do governo e parlamentares no Capitólio.
- Huang desenvolveu uma relação próxima com o presidente Trump no início do segundo mandato.
- Washington debate a regulação de IA e as regras de exportação de chips.
**Fontes:**
- [S44] The Hill — https://thehill.com/policy/technology/6055355-nvidia-launches-employee-funded-pac/
- [S45] Devdiscourse (Reuters) — https://www.devdiscourse.com/article/international/3968786-nvidia-to-start-employee-funded-us-political-action-committee
- [S46] The Independent — https://www.independent.co.uk/news/world/americas/us-politics/nvidia-nvpac-corporate-donations-b3040678.html

## EUA e Venezuela — arrendamento de 17 campos de petróleo
- Autoridades do governo Trump trabalham em um acordo para garantir acesso americano de longo prazo a parte das reservas de petróleo da Venezuela, segundo fontes ouvidas na quinta-feira, 27 de agosto.
- O acordo pode ser assinado e tornado público em breve.
- A medida pode reduzir o custo das importações de petróleo dos EUA.
- Uma lista de 17 campos em negociação vista pela Reuters inclui campos novos na Faixa do Orinoco.
- A lista também inclui áreas maduras no Lago de Maracaibo.
- Alguns desses campos são hoje operados por uma pequena empresa chinesa, com contrato assinado durante o governo Maduro.
- O modelo jurídico em estudo é um "arrendamento" (lease), com um leilão ou licitação posterior para distribuir cada campo entre produtores americanos.
- O suprimento resultante seria garantido para os Estados Unidos.
- A Venezuela estuda deixar a OPEP enquanto estreita laços com os EUA, segundo a Bloomberg na noite de quinta-feira.
- A Venezuela foi membro fundadora da OPEP em 1960 e há anos não cumpre as cotas do grupo.
- O país produz hoje cerca de 1,25 milhão de barris por dia.
- O secretário de Energia dos EUA, Chris Wright, planeja uma viagem a Caracas já na próxima semana, segundo a Axios, que noticiou as conversas primeiro na quinta-feira.
- A Reserva Estratégica de Petróleo dos EUA (SPR) tem cerca de 290 milhões de barris armazenados em cavernas subterrâneas de sal.
- O volume equivale a cerca de 41% da capacidade total.
- Os saques vieram após a invasão russa de 2022 e o início da guerra com o Irã, em fevereiro de 2026.
- O petróleo fechou em alta de cerca de 2% em 27 de agosto.
- O contrato do WTI para outubro fechou em alta de US$1,30 (1,6%), a US$83,53 o barril.
- O Brent para outubro subiu US$1,94 (2,2%), a US$89,78.
**Fontes:**
- [S47] Reuters via MarketScreener — https://www.marketscreener.com/news/us-nears-deal-to-secure-long-term-access-to-venezuela-s-oil-reserves-sources-say-ce7858dfd98dff25

## PayPal — Advent e Stripe desistem da compra
- Um consórcio formado pela gestora de private equity Advent International e pela processadora de pagamentos Stripe decidiu abandonar a tentativa de comprar o PayPal, segundo a Bloomberg na quinta-feira, 27 de agosto.
- O grupo havia oferecido US$60,50 por ação em julho.
- A oferta avaliava o PayPal em mais de US$53 bilhões.
- O valor é uma fração dos cerca de US$360 bilhões que a empresa valia no pico da pandemia, em 2021.
- O conselho do PayPal considerou a oferta inadequada.
- O conselho afirmou que a proposta enfrentava obstáculos regulatórios e de financiamento.
- A empresa nunca respondeu formalmente à proposta.
- As ações do PayPal caíram 13% no pré-mercado de sexta-feira, 28 de agosto.
- Os papéis eram negociados a US$53,20 antes da abertura, após fecharem a US$61,47 na sessão anterior.
- O negócio teria figurado entre as maiores aquisições alavancadas da história.
- O Block havia procurado o PayPal ao lado de Stripe e Advent em abril, mas deixou o consórcio antes de a oferta ser apresentada.
- O novo CEO do PayPal, Enrique Lores, disse que a empresa avaliaria cuidadosamente qualquer opção estratégica capaz de criar valor superior aos acionistas.
- Lores não comentou a especulação sobre a aquisição na teleconferência de resultados mais recente.
**Fontes:**
- [S48] Reuters — https://www.reuters.com/business/advent-stripe-consortium-is-said-drop-pursuit-paypal-bloomberg-news-reports-2026-08-28/
- [S49] Reuters via MarketScreener — https://sa.marketscreener.com/news/paypal-shares-fall-after-report-advent-stripe-consortium-abandons-takeover-pursuit-ce7858dfdd8af522
- [S50] The Straits Times — https://www.straitstimes.com/business/advent-stripe-abandon-63-5b-pursuit-of-fintech-pioneer-paypal
- [S51] PYMNTS — https://www.pymnts.com/news/acquiring/2026/advent-stripe-abandon-50-billion-pursuit-of-paypal/

## Irã e Catar — mediação sobre Ormuz e recusa de Trump
- O primeiro-ministro e chanceler do Catar, xeique Mohammed bin Abdulrahman Al Thani, visitou Teerã na quinta-feira, 27 de agosto.
- Ele se reuniu com o chanceler iraniano Abbas Araghchi.
- Também se reuniu separadamente com o presidente iraniano Masoud Pezeshkian e com o presidente do parlamento e principal negociador, Mohammad Bagher Ghalibaf.
- O arcabouço em discussão inclui a criação de um corredor marítimo temporário conjunto entre Irã e Omã pelo Estreito de Ormuz.
- O arcabouço prevê também um possível "projeto conjunto" para limpar o estreito de minas.
- O Irã afirma que as minas foram lançadas durante a guerra.
- Trump disse no Salão Oval que Washington não está falando com o Irã: "Não queremos falar com eles. Não estamos buscando encontro nem nada."
- A Casa Branca disse que a campanha econômica dos EUA contra Teerã seguirá até o Irã decidir negociar de forma significativa.
- A porta-voz da Casa Branca, Karoline Leavitt, descreveu a mudança na quinta-feira: "Tivemos a Operação Epic Fury para destruir o exército deles. Agora temos a Operação Economic Outcast para destruir a economia deles."
- Leavitt falou em entrevista à Fox News.
- Mohsen Rezaei, secretário do Conselho Supremo de Segurança Nacional do Irã, disse ao premiê catariano que Teerã atacaria interesses militares e econômicos dos EUA se Washington cometesse "travessuras" contra o país.
- Rezaei afirmou que os EUA precisam encerrar o bloqueio aos portos iranianos, pagar indenizações e retirar sanções antes da reabertura do estreito.
- A Organização Marítima Internacional registrou 70 incidentes no Estreito de Ormuz desde o início da guerra, em 28 de fevereiro.
- Os incidentes mataram 19 marinheiros.
- Cerca de um quinto do suprimento global de energia passava pelo estreito antes da guerra.
- A Marinha do IRGC provavelmente atacou um petroleiro com bandeira do Kuwait no Estreito de Ormuz em 27 de agosto.
- O comandante do Basij, Hossein Taeb, alertou no mesmo dia que o Irã responderia à pressão econômica impondo custos econômicos aos EUA e a Israel.
**Fontes:**
- [S52] Al Jazeera — https://www.aljazeera.com/news/2026/8/27/iran-qatar-hold-hormuz-talks-amid-intl-hopes-dialogue-with-us-will-resume
- [S53] CNA (Reuters) — https://www.channelnewsasia.com/world/qatar-iran-us-mediate-trump-6346481
- [S54] Critical Threats (AEI/ISW) — https://www.criticalthreats.org/analysis/iran-update-august-27-2026

## FDA — duas aprovações no mesmo dia: LISRAYA e Bixlenvo
- Em 27 de agosto, a FDA (agência reguladora de medicamentos dos EUA) aprovou o LISRAYA (brepocitinibe) 30 mg para adultos com dermatomiosite.
- O LISRAYA é um comprimido de dose única diária da Priovant, subsidiária da Roivant (Nasdaq: ROIV).
- É o primeiro grande avanço terapêutico em décadas para a doença autoimune.
- O medicamento já está disponível nos Estados Unidos.
- No estudo de Fase 3 VALOR, o maior já feito em dermatomiosite, 55% dos pacientes tratados com LISRAYA atingiram melhora moderada ou superior no Total Improvement Score de miosite e uso mínimo ou nulo de esteroides até a semana 52.
- No grupo placebo, o índice foi de 30%.
- Entre os pacientes que tomavam pelo menos 7,5 mg/dia de corticosteroides orais no início do estudo, 62% reduziram para uso mínimo ou nulo (até 2,5 mg/dia), contra 38% no placebo.
- Entre esses pacientes, 45% abandonaram totalmente os corticosteroides, contra 29% no placebo.
- A lista de aprovações de medicamentos inéditos da FDA em 2026 registra o Lisraya (brepocitinibe) como aprovação número 35 do ano, com data de 27/8/2026, para tratar dermatomiosite em adultos.
- Também em 27 de agosto, a FDA aprovou o Bixlenvo, da Gilead Sciences (Nasdaq: GILD), combinação de bictegravir 75 mg e lenacapavir 50 mg.
- O Bixlenvo é o menor regime de comprimido único diário para tratamento de HIV em adultos com supressão virológica.
- É a primeira opção desse tipo para pacientes com supressão virológica em regimes complexos de múltiplos medicamentos.
- A aprovação se baseia nos estudos de Fase 3 ARTISTRY-1 e ARTISTRY-2.
- O ARTISTRY-1 recrutou a população mais idosa já incluída em um estudo registracional de Fase 3 para HIV-1, com idade mediana de 60 anos.
- Os participantes tomavam de dois a 11 comprimidos por dia no início do estudo.
- A duração mediana de tratamento prévio era de 28 anos.
**Fontes:**
- [S55] GlobeNewswire (Roivant Sciences) — https://www.globenewswire.com/news-release/2026/08/27/3352365/0/en/roivant-announces-fda-approval-of-lisraya-brepocitinib-for-adults-with-dermatomyositis-now-available-in-the-u-s.html
- [S56] U.S. Food and Drug Administration — https://www.fda.gov/drugs/novel-drug-approvals-fda/novel-drug-approvals-2026
- [S57] Business Wire (Gilead Sciences) — https://markets.financialcontent.com/pennwell.waterworld/article/bizwire-2026-8-27-us-fda-approves-gileads-bixlenvo-a-new-once-daily-single-tablet-option-for-virologically-suppressed-adults-with-hiv-including-those-on-complex-regimens

## EUA — pedidos de auxílio-desemprego caem a 203 mil
- Os pedidos iniciais de seguro-desemprego estaduais caíram 4.000, para 203 mil com ajuste sazonal, na semana encerrada em 22 de agosto.
- O Departamento do Trabalho divulgou o dado na quinta-feira, 27 de agosto.
- Economistas consultados pela Reuters projetavam 208 mil pedidos.
- O número da semana anterior foi revisado para 207 mil.
- A média móvel de quatro semanas subiu levemente, para 205.500.
- Os pedidos continuados, um indicador de contratações, caíram 18 mil, para 1,778 milhão na semana encerrada em 15 de agosto.
- Os pedidos rondam a parte baixa da faixa de 189 mil a 230 mil registrada neste ano.
- O dado indica que as demissões seguem raras, mesmo com contratações fracas.
- A taxa de desemprego dos EUA caiu novamente no mês passado, para 4,1%.
- A estabilidade do mercado de trabalho, se sustentada, permite ao Federal Reserve manter o foco no combate à inflação.
- A inflação está acima da meta de 2% há 65 meses seguidos.
- A AP observa que a economia e o mercado de trabalho americanos se mostraram resilientes apesar dos preços altos da gasolina causados pelo conflito com o Irã.
- Parte da explicação é que a repressão à imigração promovida por Trump e a aposentadoria dos baby boomers reduzem o número de pessoas disputando vagas.
**Fontes:**
- [S58] AP News — https://apnews.com/article/unemployment-benefits-jobless-claims-layoffs-labor-5980ffc63486db19d4beb2443eb70c16
- [S59] The Business Times (Reuters) — https://www.businesstimes.com.sg/international/us-jobless-claims-dip-pointing-continued-labour-market-stability
- [S60] Los Angeles Times — https://www.latimes.com/business/story/2026-08-27/jobless-claims-fall-again-as-no-hire-no-fire-labor-market-traps-workers

## Rússia e Ucrânia — bombardeio "massivo" em nove cidades
- O bombardeio noturno russo com mísseis e drones a jato atingiu nove cidades ucranianas.
- Foram danificadas casas, escolas, unidades médicas e portos.
- Pelo menos duas pessoas morreram e mais de uma dezena ficaram feridas.
- A Rússia classificou os ataques como "massivos".
- A ofensiva se estendeu pelas horas de luz de quinta-feira, 27 de agosto, com explosões ecoando em Kiev ao longo da manhã.
- A escassez de defesas antiaéreas Patriot, de fabricação americana, deixa a Ucrânia vulnerável.
- A Rússia vem reconstruindo estoques de mísseis e mira energia e empresas privadas para paralisar a economia antes do inverno.
- A Ucrânia intensifica sua própria campanha de drones de longo alcance contra postos de comando russos e grandes varejistas online.
- Drones perdidos sobre a vizinha Moldávia alimentam o temor de que a guerra transborde as fronteiras.
**Fontes:**
- [S61] Los Angeles Times (AP) — https://www.latimes.com/world-nation/story/2026-08-27/russia-bombards-9-ukrainian-cities-overnight-calling-strikes-massive

## EUA — pressão do agronegócio contra isenções a refinarias
- Uma coalizão de grupos do agronegócio e de biocombustíveis escreveu a Trump na quinta-feira, 27 de agosto, pedindo que ele rejeite qualquer ampliação das isenções para pequenas refinarias nas leis americanas de mistura de biocombustíveis.
- A coalizão inclui a Renewable Fuels Association, a Growth Energy e a National Farmers Union.
- Os grupos alertam que uma explosão de isenções prejudicaria a América rural ao derrubar a demanda por safras e combustíveis renováveis.
- O governo estuda praticamente dobrar o tamanho das isenções, de 990 milhões de créditos para até 1,8 bilhão.
- Uma decisão é esperada antes do fim de agosto.
- Trump e altos funcionários discutiram um plano para elevar as cotas de biocombustíveis de 2027 em cerca de 500 milhões de galões, para compensar o dano das isenções que devem ser anunciadas, segundo duas pessoas a par da reunião.
- Nenhuma decisão final foi tomada.
- A medida busca conter os preços da gasolina durante a guerra com o Irã, antes das eleições de meio de mandato em novembro.
- O governo quer ajudar os republicanos a manter o controle do Congresso.
- A perspectiva de ampliação das isenções já derrubou os preços dos créditos de combustível renovável, conhecidos como RINs.
- A senadora republicana Joni Ernst, de Iowa, chamou o plano de "um presente para as grandes petroleiras, falsamente vendido como alívio na bomba".
- Ernst disse que a medida esmagaria a demanda por milho e soja.
**Fontes:**
- [S62] Reuters via MarketScreener — https://ca.marketscreener.com/news/trump-officials-discuss-expanded-refinery-waivers-as-farm-backlash-grows-sources-say-ce7858ded18ef323
