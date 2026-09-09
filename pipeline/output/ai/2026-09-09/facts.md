# Fatos — Newsletter [Tech] 9 de Setembro de 2026

## OpenAI — prova de Navier-Stokes com 10 mil agentes
- Em 8 de setembro de 2026 a OpenAI publicou uma prova de que a dinâmica das equações de Navier-Stokes pode desenvolver uma singularidade em tempo finito.
- O problema de existência e suavidade de Navier-Stokes é um dos Problemas do Prêmio Millennium.
- A prova foi produzida por um sistema interno da OpenAI e veio acompanhada de um texto explicativo e de uma formalização em Lean.
- A OpenAI diz ter usado um modelo interno "significativamente mais capaz que o GPT-6 Astra".
- O grupo de agentes que produziu a resolução operou na casa de 10 mil agentes simultâneos.
- Os agentes chegaram à resolução no sábado, 5 de setembro, cerca de 88 horas após o lançamento dos primeiros agentes.
- A formalização e verificação em Lean levaram mais 17 horas, feitas com o GPT-6 Astra.
- Somando todos os problemas atacados, os agentes trocaram 4,9 milhões de mensagens e consumiram cerca de 300 bilhões de tokens de output.
- Só o esforço de Navier-Stokes respondeu por 2,7 milhões de mensagens e aproximadamente 130 bilhões de tokens de output.
- A OpenAI disse em coletiva de imprensa que rodar o mesmo problema como cliente custaria cerca de US$15 milhões.
- A OpenAI não revelou o nome do modelo usado.
- O treinamento do modelo interno começou em 28 de agosto.
- Em 1º de setembro pesquisadores da OpenAI ouviram rumores de que dois Problemas do Millennium teriam sido resolvidos e despacharam grupos de agentes sobre os problemas restantes.
- O resultado trata das equações de Navier-Stokes 3D forçadas, que não atendem aos critérios estabelecidos pelo Clay Mathematics Institute.
- O prêmio de US$1 milhão segue sem ser reivindicado e a OpenAI diz que não pretende pleiteá-lo, apresentando o trabalho como demonstração da capacidade do modelo.
- A OpenAI afirma que seus pesquisadores e agentes não viram o trabalho concorrente de Levent Alpöge e Tristan Buckmaster até a publicação pública.
- A OpenAI admite que "não pode descartar que dados desidentificados derivados do uso que eles fizeram de nossos produtos tenham ajudado a melhorar nossos modelos".
**Fontes:**
- [S1] OpenAI — https://openai.com/index/navier-stokes-solution/
- [S2] Simon Willison's Weblog — https://simonwillison.net/2026/Sep/8/on-navier-stokes/
- [S3] New Scientist — https://www.newscientist.com/article/2588063-openai-has-solved-the-navier-stokes-millennium-problem-using-15m-of-ai-effort/
- [S4] RuntimeWire — https://runtimewire.com/article/openai-10000-ai-agents-navier-stokes-proof
- [S5] Forkast — https://forkast.news/openais-10000-agent-navier-stokes-claim-solves-the-wrong-problem-and-the-right-one-has-a-provenance-controversy/
- [S6] alphaXiv — https://www.alphaxiv.org/abs/2609.navier-stokes

## Anthropic — demissão de pesquisador e risco de extinção
- Jacob Coxon, pesquisador de pré-treinamento da Anthropic, anunciou na terça-feira, 8 de setembro de 2026, que está deixando a indústria de IA.
- Coxon diz que não quer participar de uma corrida do setor para construir sistemas de IA capazes de se aprimorar sozinhos.
- Coxon passou três anos fazendo pesquisa de pré-treinamento na OpenAI e na Anthropic.
- Coxon escreveu no X: "Nenhuma das duas empresas está agindo de forma responsável. Elas estão correndo direto para a superinteligência auto-aprimorável e apostando com as nossas vidas."
- Superinteligência auto-aprimorável se refere ao cenário em que modelos de IA desenvolvem um sucessor mais capaz de si mesmos, criando um ciclo de retroalimentação incontrolável.
- Evan Hubinger, líder de Alignment Science da Anthropic, apoiou Coxon publicamente: "realmente acreditamos sinceramente que a IA pode matar todos os humanos! Eu pessoalmente acho que é >10% na próxima década… ainda não temos um plano para resolver o alinhamento para a superinteligência e não estamos claramente no caminho de tê-lo."
- Coxon foi membro do quadro técnico da OpenAI de 2023 até julho de 2026, quando passou para a Anthropic.
- Na OpenAI, sua pesquisa incluiu trabalho no GPT-4o.
- Coxon escreveu que "aceitar a corrida e entrar no 'fim de jogo' é uma aposta arrogante que não deveria ser lançada a partir do Slack de uma empresa privada".
- Coxon disse que impedir uma corrida global pode exigir ações custosas, como "uma proibição temporária de melhorar as capacidades dos modelos".
- A Anthropic respondeu citando sua própria pesquisa sobre auto-aprimoramento recursivo, publicada no mês anterior, e a necessidade de ferramentas para "deliberadamente cadenciar a fronteira do desenvolvimento de IA para que a sociedade possa se preparar".
- A OpenAI disse que o mundo pode eventualmente precisar cadenciar o ritmo do avanço da IA.
**Fontes:**
- [S7] Wall Street Journal — https://www.wsj.com/tech/ai/anthropic-researcher-quits-over-out-of-control-ai-fears-707b7628
- [S8] ABC News (Australia) — https://www.abc.net.au/news/2026-09-09/anthropic-researcher-coxon-quits-over-human-threat/107134164
- [S9] Politico Europe — https://www.politico.eu/article/anthropic-openai-researcher-jacob-coxon-warns-ai-could-kill-humans/
- [S10] Business Insider — https://www.businessinsider.com/anthropic-researcher-quits-over-ai-safety-concerns-2026-9
- [S11] The Independent — https://www.independent.co.uk/tech/anthropic-openai-ai-threat-jacob-coxon-b3047033.html
- [S12] X — https://x.com/evanhub/status/2097497037956891126

## Meta — lançamento do agente pessoal Muse
- A Meta apresentou o Muse em 8 de setembro de 2026, um agente de IA pessoal.
- O Muse roda no Muse Secure VM, uma máquina virtual dedicada que abriga tanto o agente quanto os dados da pessoa.
- Falar com o Muse funciona como mandar mensagem para outra pessoa, no app Muse ou diretamente no WhatsApp.
- O Muse está sendo liberado nos Estados Unidos em iOS, Android e no muse.ai, com suporte aos óculos de IA da Meta previsto para breve.
- O Muse é movido pelo Muse Spark 1.3.
- O Muse é gratuito para até 100 milhões de tokens por semana, com planos de assinatura de US$20 e US$100 mensais para quem usa mais poder computacional.
- Mark Zuckerberg: "O Muse foi construído para ajudar a entregar superinteligência pessoal para todos ao longo do tempo, então estamos deixando o uso gratuito para até 100 milhões de tokens por semana."
- A Meta diz que o Muse pode fazer compras online, comprar ingressos de cinema e agendar compromissos como aulas de tênis ou preencher a autorização para uma excursão escolar.
- Usuários podem conectar aplicativos para que o Muse envie e-mails, reserve viagens, transforme Reels de receitas em listas de compras e faça compras via Link by Stripe.
- Há conectores exclusivos do Muse para Instagram (incluindo DMs), Threads, Facebook (incluindo o Marketplace) e Messenger.
- O Muse Spark 1.3, lançado na semana anterior, usa cerca de 20% menos chamadas de ferramentas e aproximadamente 25% menos tokens que o Muse Spark 1.2 para as mesmas tarefas.
- A Meta diz que alguns desenvolvedores já usavam "trilhões de tokens por semana" na família Muse Spark.
**Fontes:**
- [S13] Meta Newsroom — https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/
- [S14] Bloomberg — https://www.bloomberg.com/news/articles/2026-09-08/meta-announces-muse-ai-agent-for-personal-tasks-and-organization
- [S15] Techmeme — https://www.techmeme.com/260908/p38
- [S16] TechCrunch — https://techcrunch.com/2026/09/08/meta-debuts-its-muse-ai-agent-will-consumers-trust-it/
- [S17] SiliconANGLE — https://siliconangle.com/2026/09/02/meta-says-it-has-caught-up-with-anthropic-and-openai-after-releasing-muse-spark-1-3-its-most-powerful-llm-so-far/

## NSA, FBI e CISA — acusação de destilação industrial por empresas chinesas
- Em 8 de setembro de 2026 a NSA, a CISA e o FBI publicaram um alerta conjunto de cibersegurança (AA26-251A).
- O alerta afirma que empresas de IA baseadas na China conduzem campanhas de destilação de conhecimento em escala industrial contra modelos de empresas americanas.
- Destilação de conhecimento é a extração sistemática de funcionalidades e capacidades proprietárias de um modelo por meio de suas respostas.
- Segundo o alerta, essas campanhas formam "o núcleo — não meramente um complemento" da estratégia de desenvolvimento de IA dessas empresas.
- O documento cita DeepSeek, Moonshot AI, Alibaba, MiniMax, StepFun e Z.AI.
- As agências dizem que, "provavelmente com conhecimento do governo chinês", essas empresas extraíram bilhões de tokens ao longo de milhões de trocas e requisições de modelos de fronteira americanos desde pelo menos o fim de 2024.
- Entre os modelos alvo estão variantes de Claude, GPT, Gemini e Grok.
- As agências afirmam que o custo de treinamento de US$5,6 milhões citado publicamente pela DeepSeek é enganoso porque não inclui o custo real dos dados obtidos por destilação maliciosa.
- A Moonshot AI é acusada de extrair volume significativo de dados do Claude Fable 5 para treinar o Kimi-K3 e de dados do GPT-4o para treinar o Kimi-K2.
- O CyberScoop contabiliza 18 modelos americanos distintos supostamente destilados pela Moonshot AI; o Fable 5 é o modelo comercial mais avançado da Anthropic hoje.
- As agências dizem que as empresas chinesas roteiam requisições por um mercado cinza de proxies de API conhecidos como "estações de transferência".
- Segundo o alerta, essas estações servem para contornar restrições regionais das empresas americanas, violar termos de uso, driblar mecanismos de proteção e minar a rastreabilidade.
- Entre três ações recomendadas, o alerta orienta os laboratórios americanos a "alterar sutilmente as respostas para tentativas suspeitas de destilação maliciosa".
- O alerta também recomenda compartilhamento de inteligência entre provedores de modelos, plataformas de nuvem e agregadores de API.
- É a acusação pública mais detalhada do governo americano sobre o tema até agora.
- O relatório não afirmou que a inteligência chinesa tenha tido papel na campanha.
**Fontes:**
- [S18] CISA — https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-251a
- [S19] CISA — https://www.cisa.gov/news-events/news/cisa-nsa-and-fbi-warn-china-based-ai-companies-targeting-us-ai-models-industrial-scale-knowledge
- [S20] Reuters — https://www.reuters.com/technology/us-accuses-chinese-ai-firms-industrial-scale-theft-ai-technology-2026-09-08/
- [S21] NBC News — https://www.nbcnews.com/tech/tech-news/us-accuses-china-ai-developers-deepseek-alibaba-copying-american-ai-rcna596696
- [S22] CyberScoop — https://cyberscoop.com/us-accuses-chinese-ai-companies-distillation/

## Cognition — Série E de US$2 bilhões a um valuation de US$48 bilhões
- A startup de IA para programação Cognition anunciou na terça-feira, 8 de setembro de 2026, que levantou US$2 bilhões em uma rodada Série E.
- A rodada avalia a Cognition em US$48 bilhões.
- A rodada foi liderada pelos novos investidores Andreessen Horowitz e Accel, ao lado dos já acionistas Founders Fund, General Catalyst e Avenir.
- A receita em run-rate cresceu de US$492 milhões para quase US$900 milhões desde a rodada anterior, em maio.
- Em maio a empresa valia US$26 bilhões após captar US$1 bilhão, de modo que o valuation praticamente dobrou.
- As duas rodadas precificam a Cognition em cerca de 53 vezes a receita em run-rate, ou seja, o múltiplo não se expandiu apesar de o valuation ter dobrado em cerca de 15 semanas.
- A captação veio apenas quatro meses depois da anterior.
- A TechCrunch avalia que a rodada sinaliza que investidores acreditam que IA para programação não é um mercado de vencedor único.
- O produto principal da Cognition é o Devin, um agente autônomo de engenharia de software que planeja tarefas, escreve e testa código, depura e faz deploy em um sandbox.
- Entre os clientes do Devin estão o Exército e a Marinha dos EUA, a NASA, ServiceNow, Infosys e Goldman Sachs.
**Fontes:**
- [S23] Reuters — https://www.reuters.com/technology/cognition-ai-raises-2-billion-48-billion-valuation-2026-09-08/
- [S24] TechCrunch — https://techcrunch.com/2026/09/08/cognition-hits-48b-valuation-signaling-investors-believe-ai-coding-is-far-from-a-winner-take-all-market/
- [S25] The Next Web — https://thenextweb.com/news/cognition-series-e-48bn-flat-multiple
- [S26] Silicon Republic — https://www.siliconrepublic.com/business/devin-maker-cognition-raises-2bn-at-48bn-valuation
- [S27] SiliconANGLE — https://siliconangle.com/2026/09/08/ai-coding-startup-cognition-raises-2b-at-48b-valuation-as-revenue-nears-900m/

## Harvey — US$550 milhões para a IA jurídica construir modelos próprios
- A Harvey anunciou em 9 de setembro de 2026 uma rodada de US$550 milhões.
- A rodada avalia a startup de IA jurídica em US$15,6 bilhões.
- O dinheiro é destinado a financiar o esforço da empresa para construir seus próprios modelos de IA.
- A rodada foi co-liderada por Lightspeed Venture Partners e Diffusion, uma nova firma cofundada por Kris Fredrickson, investidor de longa data da Harvey e ex-Coatue Management.
- Sapphire Ventures e Whale Rock Capital Management também entraram na rodada.
- O valuation subiu dos US$11 bilhões de seis meses atrás.
- A Harvey já levantou mais de US$1,5 bilhão no total.
- Em fevereiro de 2025 a Harvey valia US$3 bilhões.
- A captação vem depois do lançamento do primeiro modelo de pesos abertos da Harvey, pós-treinado internamente, e do Harvey LAB, seu Legal Agent Benchmark.
- A receita anualizada da Harvey passou de US$350 milhões em agosto, alta de mais de 80% ante os US$190 milhões de janeiro.
- Participaram da rodada os investidores existentes Sequoia, Kleiner Perkins, a16z, Coatue, Conviction, Elad Gil, Evantic, GIC, Goldman Sachs Alternatives, Verified Capital e WNDR.
- A própria empresa colocou o valuation em US$15,5 bilhões.
**Fontes:**
- [S28] Bloomberg — https://www.bloomberg.com/news/articles/2026-09-09/legal-ai-startup-harvey-hits-15-6-billion-value-with-550-million-round
- [S29] Iberian Lawyer — https://iberianlawyer.com/harvey-raises-550m-to-accelerate-ai-expansion/
- [S30] Unite.AI — https://www.unite.ai/harvey-secures-550m-in-fresh-funding-valuation-climbs-to-15-5b/
- [S31] Crypto Briefing — https://cryptobriefing.com/harvey-legal-ai-16b-valuation-funding/
- [S32] Dealroom — https://dealroom.co/news/144690-harvey-targets-15-5b-valuation-in-500m-raise-as-revenue-nears-350m/

## Suno — modelos v6 treinados com Warner, BMG e Believe
- A Suno lançou em 9 de setembro de 2026 a geração v6 de seus modelos de música por IA.
- Os modelos foram desenvolvidos com Warner Music Group, BMG e Believe.
- São os primeiros modelos da Suno construídos sob suas parcerias com a indústria musical, segundo o chief product officer Jack Brody.
- A família v6 tem três modelos: v6, v6-wild e v6-mini.
- O v6 e o v6-Wild ficam disponíveis para assinantes Pro e Premier; o v6-mini é gratuito para todos os usuários.
- A Suno está aposentando seus modelos anteriores conforme a família v6 é liberada.
- A Suno diz que o v6 foi construído do zero e não foi treinado com os mesmos dados dos modelos anteriores.
- O treinamento combinou músicas licenciadas dos catálogos de Warner Music Group e BMG com dados de usuários da Suno.
- Os acordos incluem divisão de receita com os detentores de direitos.
- Jack Brody: "a partir do dia em que ele for lançado, em 9 de setembro, essa parceria começa a gerar receita para nossos parceiros."
- Os termos financeiros não foram divulgados.
- Usuários seguem impedidos de pedir ao modelo que faça uma música à semelhança de um artista ou de uma canção conhecida.
- A participação da Believe reverte a decisão de abril, quando a empresa bloqueou a distribuição de músicas criadas com a Suno.
- A Warner encerrou seu processo de direitos autorais de 2024 contra a Suno como parte da parceria que levou ao v6.
- Universal Music Group e Sony Music Entertainment seguem com ações de direitos autorais contra a Suno.
- Os planos Pro e Premier da Suno custam US$8 e US$24 por mês nos Estados Unidos.
- A startup captou recentemente mais de US$400 milhões em uma rodada que a avaliou em US$5,4 bilhões.
**Fontes:**
- [S33] Axios — https://www.axios.com/2026/09/09/suno-v6-ai-music-warner-bmg
- [S34] Engadget — https://www.engadget.com/2251539/suno-trained-its-v6-ai-music-models-with-help-from-warner-and-bmg/
- [S35] MusicRadar — https://www.musicradar.com/music-tech/suno-has-rebuilt-its-ai-music-models-from-scratch-with-licensed-music
- [S36] Music Week — https://www.musicweek.com/labels/read/suno-rolls-out-new-generation-of-ai-music-models-with-warner-music-group-bmg-and-believe/094924
- [S37] The Economic Times — https://economictimes.indiatimes.com/tech/artificial-intelligence/suno-releases-new-ai-music-models-in-partnership-with-warner-music-bmg/articleshow/133963905.cms

## Google — €13 bilhões na Finlândia e primeiro PPA nuclear fora dos EUA
- O Google anunciou em 9 de setembro de 2026 que vai investir pelo menos €13 bilhões (cerca de US$15,1 bilhões) em infraestrutura de IA na Finlândia.
- O investimento será feito ao longo de 2027-2028 e é o maior aporte individual do Google na Europa.
- O investimento cobre data centers e infraestrutura de apoio em Hamina, Muhos, Vaala e Kajaani.
- Fortum e Google assinaram um acordo de compra de energia (PPA) de 22 anos, o primeiro contrato de energia nuclear do Google fora dos Estados Unidos.
- O PPA começa em 2028 com um volume menor e chega a 50% da capacidade da usina nuclear de Loviisa entre 2030 e 2049.
- Loviisa tem dois reatores de água pressurizada (PWR) de 507 MWe, comissionados em 1977 e 1980.
- A usina produz cerca de 8 TWh de eletricidade por ano e responde por aproximadamente 10% da eletricidade da Finlândia.
- Loviisa emprega cerca de 580 pessoas.
- Sem o programa de investimento de extensão de vida útil da Fortum, a usina não poderia operar depois de 2030.
- A Fortum diz que o PPA deve elevar o retorno comparável sobre ativos líquidos (RONA) do grupo em cerca de 1,4 ponto percentual quando 50% da geração da usina estiver contratada.
- O acordo deve viabilizar um novo aumento de potência de 10 MW na usina, além do uprate de 38 MW já planejado e previsto para entrar em operação em 2028.
- O pacote inclui 629 MW de energia eólica onshore nova contratada via Valorem e Suomen Hyotytuuli.
- Inclui também uma instalação de baterias de 94 MW ao lado do novo data center do Google em Kajaani, prevista para operar a partir do fim de 2027.
- Fortum e Google assinaram ainda um memorando de entendimento para estudar novos reatores nucleares em Loviisa e capacidade flexível.
- A Fortum vai avaliar seus terrenos já conectados à rede elétrica para futuros data centers do Google.
**Fontes:**
- [S38] CNA (Reuters) — https://www.channelnewsasia.com/business/google-invest-15-billion-in-ai-infrastructure-and-buy-nuclear-power-in-finland-6372206
- [S39] Fortum (inside information release) — https://www.finanznachrichten.de/nachrichten-2026-09/69529130-fortum-inside-information-fortum-and-google-partner-to-drive-sustainable-growth-for-finland-sign-nuclear-power-purchase-agreement-399.htm
- [S40] The Next Web — https://thenextweb.com/news/google-finland-13bn-data-centres-nuclear-wind
- [S41] DataCenterDynamics — https://www.datacenterdynamics.com/en/news/google-signs-nuclear-ppa-with-fortum-in-loviisa-finland/

## XPeng — linha de produção de robôs humanoides
- Em 8 de setembro de 2026, em Guangzhou, a XPeng colocou em operação suas linhas de produção de robôs humanoides.
- O robô IRON estreou saindo da linha caminhando de forma autônoma após concluir a produção.
- A XPeng diz que mais de 80% dos processos centrais da linha são automatizados.
- A empresa aplica sistemas de qualidade de padrão automotivo à montagem de humanoides.
- O IRON tem 76 graus de liberdade no corpo e 21 em cada mão.
- O IRON roda em três chips próprios XPeng Turing AI, que entregam até 2.250 TOPS de poder computacional efetivo.
- Esse poder computacional permite que o modelo de base de IA física do robô rode no próprio dispositivo.
- O comissionamento não significa produção em massa.
- A XPeng reiterou que a produção em volume começa até o fim de 2026, com as primeiras implantações em suas próprias lojas e campi.
- O lançamento comercial e as entregas na China e no exterior estão previstos para 2027.
- A capacidade da linha e o preço do robô não foram divulgados.
- Em 24 de agosto a unidade de robótica da XPeng assinou acordos de compra de ações com múltiplos investidores, captando mais de US$900 milhões.
- A captação saiu a um valuation pós-money acima de US$6,3 bilhões, a maior rodada privada individual da indústria de IA incorporada da China até agora.
- A XPeng espera que a margem bruta por unidade de humanoide seja significativamente maior que a de seus veículos elétricos.
**Fontes:**
- [S42] XPeng — https://www.xpeng.com/news/01a080371029a057bc8e8a02a2c6012b
- [S43] CnEVPost — https://cnevpost.com/2026/09/08/xpeng-opens-iron-humanoid-robot-production-line/
- [S44] Live Science — https://www.livescience.com/technology/robotics/eerily-humanlike-ai-powered-robot-enters-mass-production-in-china-its-makers-say-it-could-soon-be-helping-you-out-at-home

## OpenAI e Samsung — chips de próxima geração
- Em coletiva de imprensa em Seul na quarta-feira, 9 de setembro de 2026, o gerente-geral da OpenAI Korea, Harrison Kim, disse que a produção e pesquisa conjunta de chips de próxima geração é a área em que a OpenAI mais avançou com a Samsung Electronics.
- Kim não deu detalhes adicionais sobre o trabalho conjunto.
- Kim disse que a Samsung é "uma das maiores implantações de ChatGPT do mundo", com funcionários na Coreia e no exterior usando a ferramenta em P&D, marketing e vendas.
- A Samsung Electronics disse que não podia confirmar informações relacionadas a clientes.
- Em junho de 2026 a OpenAI apresentou seu primeiro chip de IA próprio, o Jalapeno, projetado com a Broadcom.
- O Jalapeno é voltado para inferência de IA e será fabricado pela TSMC.
- No ano passado, Samsung Electronics e SK Hynix assinaram cartas de intenção para fornecer chips de memória ao projeto de data centers Stargate, da OpenAI.
- Kim disse que a demanda por chips de memória vai continuar crescendo.
- A OpenAI afirmou que o número de usuários do ChatGPT Enterprise em empresas e instituições sul-coreanas cresceu cerca de 28 vezes até o fim de agosto na comparação anual.
- A OpenAI não divulgou números absolutos de usuários.
**Fontes:**
- [S45] The Star (Reuters) — https://www.thestar.com.my/tech/tech-news/2026/09/09/openai-says-working-with-samsung-on-next-generation-chips-deepening-cooperation
- [S46] The Standard (Reuters) — https://www.thestandard.com.hk/innovation/article/342273/OpenAI-says-working-with-Samsung-on-next-generation-chips-deepening-cooperation
- [S47] Asharq Al-Awsat (Reuters) — https://english.aawsat.com/technology/5316275-openai-says-working-samsung-next-generation-chips-deepening-cooperation
- [S48] TradeVae — https://www.tradevae.com/news/stock-markets/openai-deepens-technical-ties-with-samsung-on-next-generation-ai-chips-and-enterprise-deployments/

## Analog Devices — compra da Alif Semiconductor por US$1,35 bilhão
- Analog Devices (NASDAQ: ADI) e Alif Semiconductor anunciaram em 9 de setembro de 2026 um acordo definitivo pelo qual a ADI comprará a Alif.
- A transação é totalmente em dinheiro, com US$1,35 bilhão pagos à vista.
- A ADI pode pagar até US$200 milhões adicionais em contrapartida contingente.
- Os conselhos das duas empresas aprovaram o negócio.
- O fechamento é esperado antes do fim do ano-calendário de 2026, sujeito a condições usuais e ao decurso do prazo do Hart-Scott-Rodino Antitrust Improvements Act de 1976, a lei antitruste americana de notificação prévia de fusões.
- A Alif fabrica microcontroladores e processadores de fusão de baixo consumo e nativos de IA para aplicações de borda.
- A ADI planeja combinar esses produtos com suas capacidades de sensoriamento, processamento de sinais, energia, conectividade e software no que chama de "Physical Intelligence".
- A Reuters descreveu o negócio como uma expansão das capacidades da ADI em dispositivos à medida que aplicações de IA migram para sistemas físicos.
- A ADI reportou mais de US$11 bilhões de receita no ano fiscal de 2025.
- É a segunda aquisição de chips de IA da ADI em cerca de quatro meses, depois da compra de outra empresa californiana de semicondutores focada em chips para data centers.
- PJT Partners atuou como assessor financeiro da ADI e Wachtell, Lipton, Rosen & Katz como assessor jurídico.
- Qatalyst Partners assessorou a Alif, com DLA Piper como assessor jurídico.
**Fontes:**
- [S49] StockTitan (ADI 8-K) — https://www.stocktitan.net/sec-filings/ADI/8-k-analog-devices-inc-reports-material-event-d7efed6b9172.html
- [S50] Reuters — https://www.reuters.com/technology/analog-devices-buy-alif-semiconductor-135-billion-2026-09-09/
- [S51] Boston Business Journal — https://www.bizjournals.com/boston/news/2026/09/09/analog-devices-alif-ai-chip-buy.html
- [S52] Unite.AI — https://www.unite.ai/analog-devices-agrees-to-all-cash-acquisition-of-alif-semiconductor/

## China — regulador aperta a régua para IPOs de robôs humanoides
- A Comissão Reguladora de Valores Mobiliários da China (CSRC) deu "orientação de janela" informal a alguns bancos de investimento e empresas elevando a régua para aprovar aberturas de capital de startups de humanoides, segundo reportagem do The Information de 9 de setembro de 2026.
- As candidatas precisam agora comprovar que conseguem gerar receita recorrente, que estão a caminho de reduzir prejuízos ou que alcançaram inovação real antes de as aprovações serem consideradas.
- As ações da Unitree Robotics caíram cerca de 45% desde a alta de mais de cinco vezes na estreia em Xangai.
- A queda desencadeou preocupações com uma bolha, com perdas de investidores de varejo e com falhas no sistema de IPOs (aberturas de capital).
- A Unitree, sediada em Hangzhou, abriu 629% acima do preço de estreia no Star Market de Xangai no mês passado.
- A queda de 45% posterior eliminou cerca de 200 bilhões de yuans (cerca de US$28 bilhões) em valor de mercado.
- A rival Robotera avalia uma abertura de capital separada em Hong Kong.
- A mudança foi motivada por uma onda de captações no mercado privado em 2026, por uma longa fila de pedidos de IPO de humanoides e pelo desempenho fraco das ações após a listagem.
- A orientação é informal e a CSRC não se manifestou publicamente.
**Fontes:**
- [S53] Reuters — https://www.reuters.com/world/asia-pacific/china-curbs-humanoid-ipos-after-unitrees-volatile-debut-information-reports-2026-09-09/
- [S54] The Straits Times — https://www.straitstimes.com/business/china-curbs-humanoid-ipos-after-unitrees-volatile-debut-report
- [S55] Electronics For You — https://www.electronicsforyou.biz/industry-buzz/china-curbs-robotic-companies-ipos-after-unitrees-volatile-debut/
- [S56] The Information — https://www.theinformation.com/articles/china-curbs-humanoid-ipos-unitrees-volatile-debut

## Dynamic Creatures — robôs-personagem de ex-líderes da Boston Dynamics
- A Dynamic Creatures saiu do stealth em 8 de setembro de 2026, em Boston.
- A empresa constrói robôs-personagem móveis e interativos para marcas de entretenimento e hospitalidade.
- A Dynamic Creatures nasce como parceira oficial da Boston Dynamics nos segmentos de entretenimento e hospitalidade.
- A empresa já trabalha com um grande parque temático e com uma varejista no desenvolvimento de experiências com personagens voltadas ao público.
- A empresa foi fundada por Marc Theermann, ex-chief strategy officer da Boston Dynamics, e pelo CTO Farbod Farshidian, ex-líder de pesquisa do Robotics and AI Institute.
- Sua plataforma, a SnowJay, funciona como sistema operacional dos personagens interativos.
- A SnowJay combina robótica avançada, controle baseado em aprendizado, percepção em tempo real, programação comportamental, design de personagens e confecção de trajes.
- Amanda McMaster, CEO interina da Boston Dynamics, disse que a Dynamic Creatures está "abrindo uma nova fronteira importante para a robótica avançada".
**Fontes:**
- [S57] GlobeNewswire (Dynamic Creatures) — https://www.globenewswire.com/news-release/2026/09/08/3357547/0/en/dynamic-creatures-emerges-from-stealth-to-launch-new-category-of-mobile-interactive-character-robots-for-hospitality-and-entertainment.html

## Nvidia — CUDA Rust para escrever kernels de GPU
- A Nvidia anunciou em 8 de setembro de 2026 que vai tornar o Rust uma linguagem de primeira classe para kernels de GPU.
- O anúncio traz dois projetos open source dos NVlabs: o cuda-oxide, para o modelo SIMT, e o cutile-rs, para o modelo Tile.
- A Nvidia diz que CUDA C++ e CUDA Python são toolchains maduras e de nível empresarial, e que vai amadurecer o CUDA Rust ao longo de 2027 e além.
- Antes, código Rust podia disparar kernels CUDA, mas o corpo do kernel tinha de ser escrito em outro lugar.
- O CUDA Rust compila kernels Rust nativamente para PTX, em vez de servir como invólucro de código de outra origem.
- O CUDA Rust usa as regras de posse (ownership) do Rust para rejeitar bugs de aliasing em tempo de compilação.
- O cuda-oxide é um backend de geração de código customizado do rustc.
- O cuda-oxide intercepta a compilação e roteia funções marcadas com #[kernel] pelo Rust MIR, pelo framework comunitário de IR Pliron e pelo LLVM IR até o PTX, entregando o resto ao backend padrão.
- Nenhum dos dois projetos está pronto para produção.
- O cuda-oxide está em alfa inicial.
- O cutile-rs está mais avançado, publicado no crates.io e já usado fora da Nvidia no motor de inferência Grout, da Hugging Face, e no mistral.rs.
- O cutile-rs exige apenas compute capability 8.0 ou superior, CUDA 13.3, Rust estável 1.89 ou mais novo e Linux, sem toolchain nightly e sem LLVM customizado.
**Fontes:**
- [S58] NVIDIA Technical Blog — https://developer.nvidia.com/blog/introducing-cuda-rust-two-tracks-for-writing-gpu-kernels/
- [S59] TheNews92 — https://thenews92.com/nvidia-announces-cuda-rust-with-cuda-oxide-simt-and-cutile-rs-tile-for-compile-time-safe-gpu-kernels/

## EUA e Irã — cinco petroleiros afundados e mísseis contra base na Jordânia
- O Comando Central dos EUA (CENTCOM) disse que suas forças destruíram cinco navios iranianos de transporte de petróleo bruto em 8 de setembro.
- O ataque veio depois de a Guarda Revolucionária Islâmica (IRGC) mirar um navio de guerra da Marinha americana com mísseis balísticos duas vezes em dois dias.
- Quatro dos petroleiros foram atingidos no Golfo de Omã e um perto da Ilha de Kharg.
- O CENTCOM disse que as forças americanas orientaram as tripulações a abandonar os navios antes de as embarcações serem atingidas e inutilizadas.
- A IRGC disse ter retaliado lançando mísseis contra forças americanas na base militar de Al Azraq, na Jordânia.
- O porta-voz das Forças Armadas jordanianas disse que as defesas aéreas interceptaram 18 mísseis balísticos e que dois mísseis caíram em áreas desabitadas.
- A Marinha da IRGC alertou tripulações de petroleiros próximos aos portos do Kuwait e do Bahrein para evacuar suas embarcações imediatamente, dizendo que elas seriam alvo.
- No mesmo dia, o governo Trump sancionou mais de duas dezenas de companhias aéreas comerciais e privadas iranianas, além de prestadores estrangeiros de serviços de carga.
- O petróleo Brent chegou a US$99,46 por barril antes de fechar a US$97,92, alta de 0,9%.
- O S&P 500 caiu 0,6% e o Dow Jones recuou 628 pontos (1,2%) em 8 de setembro.
- O rendimento do título do Tesouro americano de 10 anos subiu de 4,78% para 4,79%, perto do maior nível desde o outono de 2023.
- Dados do CME Group mostram traders precificando quase 60% de chance de alta de juros pelo Fed na reunião de 16 de setembro.
**Fontes:**
- [S60] NBC News — https://www.nbcnews.com/world/iran/us-strikes-iranian-tankers-attempted-missile-attacks-navy-warship-rcna596699
- [S61] USA Today — https://www.usatoday.com/story/news/world/2026/09/08/us-strikes-iran-destroys-5-oil-tankers-amid-escalating-war/91666127007/
- [S62] Ynetnews — https://www.ynetnews.com/article/byofsf0uzg
- [S63] HTX Insights — https://www.htx.com/news/oil-prices-approach-100-sp-500-suddenly-drops-06-KAhbLmXoQ/

## Houthis e Arábia Saudita — ataques a instalações da Aramco
- Os houthis disseram na terça-feira que atacaram instalações energéticas sauditas da Aramco no sul do reino, usando drones e mísseis balísticos.
- O porta-voz militar do grupo, Yahya Saree, chamou a ação de "uma ampla operação".
- O major-general Turki al-Malki, porta-voz saudita da coalizão liderada por Riad no Iêmen, disse que os ataques houthis atingiram as cidades de Abha, Khamis Mushait, Jazan e Najran.
- Segundo al-Malki, os ataques feriram pelo menos 73 pessoas, entre elas mulheres e crianças.
- O Ministério de Energia da Arábia Saudita disse que os ataques provocaram incêndios em várias instalações de petróleo e de serviços públicos nas províncias do sul do reino.
- A região abriga a refinaria de Jazan, uma das maiores do país, com capacidade de processar 400 mil barris de petróleo bruto por dia.
- O chanceler saudita, príncipe Faisal bin Farhan, falando em Moscou ao lado do chanceler russo Sergey Lavrov, condenou os ataques mas disse que "o caminho da diplomacia não está fechado".
- Faisal bin Farhan disse que a Arábia Saudita sempre apoiará soluções diplomáticas, mas que o reino nunca hesitará em se defender e defender seus interesses.
- A Al Jazeera descreveu as hostilidades como as mais graves desde a trégua mediada pela ONU que interrompeu os combates em larga escala em 2022.
- O estreito de Bab al-Mandeb ganhou importância à medida que o Irã restringe o estreito de Ormuz.
- Entre março e meados de julho, as exportações marítimas de petróleo saudita pelo Bab al-Mandeb foram oito vezes maiores que no mesmo período de 2025.
- Os houthis disseram que a Arábia Saudita atingiu áreas sob seu controle nas províncias de al-Jawf, al-Bayda, Marib e Taiz com aeronaves e mísseis de cruzeiro.
- Entre os alvos, segundo os houthis, houve um ataque aéreo a uma prisão em al-Hazm, capital de al-Jawf, que matou sete pessoas.
**Fontes:**
- [S64] Al Jazeera — https://www.aljazeera.com/news/2026/9/8/saudi-houthi-fighting-in-yemen-escalates-what-happened-and-whats-next
- [S65] Al-Monitor — https://www.al-monitor.com/originals/2026/09/houthis-report-saudi-reprisals-after-oil-sites-set-ablaze-wave-strikes

## Putin e Trump — telefonema de uma hora enquanto ataques russos matam cinco em Kiev
- O assessor do Kremlin Yuri Ushakov disse que Putin teve um telefonema de uma hora com Trump na terça-feira, 8 de setembro.
- Ushakov descreveu a conversa como "extremamente franca" e "construtiva".
- Segundo Ushakov, os dois líderes "se concentraram na questão de um acordo na Ucrânia".
- Ushakov disse que Putin fez uma "análise objetiva e detalhada" da linha de frente, apontando o que os americanos poderiam realisticamente fazer para encerrar rapidamente as hostilidades.
- Segundo Ushakov, Putin também frisou que a Rússia não tem "planos agressivos" em relação à Europa.
- Nem a Casa Branca nem Trump haviam divulgado um relato da conversa até o momento da reportagem.
- O telefonema ocorreu em meio a uma ofensiva russa iniciada na noite de 7 de setembro e que se estendeu por 8 de setembro.
- A ofensiva usou mísseis antinavio Oniks, mísseis balísticos Iskander-M, S-400 e KN-23 de fabricação norte-coreana, além de 32 mísseis de cruzeiro Kh-101 e 166 drones Shahed.
- O número de mortos em Kiev subiu para cinco.
- Forças russas atingiram o prédio do canal de TV "Nós Somos a Ucrânia" em Kiev enquanto jornalistas estavam no ar.
- O ataque destruiu parcialmente a instalação e feriu pelo menos cinco pessoas.
- O porta-voz do Kremlin, Dmitry Peskov, disse na terça-feira que Moscou espera a retomada de conversas trilaterais com Ucrânia e Estados Unidos.
- O Kremlin fez objeção ao envolvimento dos assessores de segurança nacional de França, Reino Unido e Alemanha (o grupo E3).
- Zelensky disse que conversas entre Rússia e Ucrânia são possíveis ainda neste mês, enquanto Moscou mantém os ataques a Kiev.
**Fontes:**
- [S66] Kyiv Post — https://www.kyivpost.com/post/84060
- [S67] CNA — https://www.channelnewsasia.com/world/russia-ukraine-peace-talks-possibly-september-zelenskyy-6368456

## Ucrânia — cerca de 1.000 mísseis Patriot contratados com empréstimo da UE
- O ministro da Defesa da Ucrânia, Yevhenii Khmara, disse em 8 de setembro que Kiev está contratando o fornecimento de cerca de 1.000 mísseis para os sistemas de defesa aérea Patriot, de projeto americano.
- A contratação é feita com ajuda de aliados e por meio de um empréstimo da União Europeia.
- Khmara disse que a maior parte dos mísseis dos novos contratos só será entregue nos próximos anos.
- Khmara pediu aos parceiros que entreguem imediatamente 300 interceptadores Patriot de seus estoques existentes, em troca de munições aprimoradas mais tarde.
- Os Estados-membros da UE concordaram em 8 de setembro com uma derrogação das regras de contratação pública, permitindo à Ucrânia gastar uma parcela de €3,2 bilhões (US$3,7 bilhões) em componentes de Patriot.
- A decisão técnica deve ser finalizada até 11 de setembro.
- O ministro da Defesa da Alemanha, Boris Pistorius, disse que o país transferirá com urgência mísseis PAC-2 à Ucrânia a partir dos estoques da Bundeswehr, e não de entregas futuras.
- Na 36ª reunião do Grupo de Contato de Defesa da Ucrânia, no formato Ramstein, o Reino Unido prometeu £100 milhões (cerca de US$135 milhões) para a compra de armamento americano pelo mecanismo PURL (Prioritised Ukraine Requirements List) da OTAN.
- O Reino Unido também garantirá a entrega de mais 95 mil drones até o fim do ano.
- A Espanha somou €2 milhões (cerca de US$2,3 milhões) para combustível, via Agência de Apoio e Aquisições da OTAN.
- O secretário-geral da OTAN, Mark Rutte, disse na reunião que os aliados da Ucrânia não têm escolha senão ampliar o apoio para que Kiev possa "aproveitar as oportunidades que está criando agora em todas as frentes" e se defender nos céus.
**Fontes:**
- [S68] Reuters — https://www.reuters.com/business/aerospace-defense/ukraine-contracting-around-1000-patriot-missiles-allies-defence-chief-says-2026-09-08/
- [S69] Kyiv Post — https://www.kyivpost.com/post/84059
- [S70] Ukraine Ministry of Defence — https://mod.gov.ua/en/news/air-defence-drones-and-shells-for-the-defence-forces-of-ukraine-partners-announce-new-contributions-following-the-36th-ramstein-format-meeting
- [S71] Militarnyi — https://militarnyi.com/en/news/ukraine-1000-patriot-missiles-eu-funds/

## Austal — oferta da Wildcat supera a da Hanwha pelos estaleiros americanos
- O estaleiro australiano Austal disse em 9 de setembro que a americana Wildcat Infrastructure ofereceu comprar sua operação nos Estados Unidos por até US$1,35 bilhão.
- A oferta da Wildcat fica entre US$1,25 bilhão e US$1,35 bilhão, em base livre de caixa e dívida.
- A proposta está sujeita a quatro semanas de due diligence.
- A oferta supera a proposta de até US$1,20 bilhão feita um mês antes pelo grupo sul-coreano Hanwha.
- A Hanwha busca expandir sua atuação no mercado de defesa americano.
- A Wildcat, sediada em Miami, indicou que pretende operar o negócio ela mesma.
**Fontes:**
- [S72] Reuters — https://www.reuters.com/business/wildcat-infrastructure-offers-buy-austals-us-operations-up-135-billion-2026-09-09/

## Chime — compra do Stride Bank por US$590 milhões
- A Chime firmou acordo definitivo para adquirir o Stride Bank, N.A. por US$590 milhões em dinheiro.
- No fechamento, o Stride passa a se chamar Chime Bank, N.A. e opera como subsidiária integral da Chime.
- As ações da Chime subiram 11% no pré-mercado de 9 de setembro após o anúncio.
- O negócio dá à Chime uma licença bancária que lhe permitirá expandir a operação de crédito.
- O Stride é um banco com licença nacional e é parceiro bancário da Chime há mais de sete anos.
- O preço equivale a cerca de 1,5 vez o valor patrimonial tangível.
- A Chime espera capturar mais de US$100 milhões em sinergias líquidas, vindas da economia com tarifas de banco patrocinador e de um custo de captação menor.
- A Chime é lucrativa e disse que vai financiar a compra com caixa em balanço.
- A Chime disse que manterá seus ativos abaixo de US$10 bilhões no futuro previsível.
- Analistas do J.P. Morgan escreveram que "adquirir um banco existente dá à Chime um caminho mais rápido e mais comprovado para obter uma licença nacional".
**Fontes:**
- [S73] Reuters — https://www.reuters.com/legal/transactional/chime-surges-11-stride-deal-puts-fintech-path-bank-charter-2026-09-09/
- [S74] Business Wire / Global Fintech Series — https://globalfintechseries.com/banking/chime-announces-agreement-to-acquire-stride-bank/

## Irã — banco central afrouxa regras cambiais e empurra repatriação via cripto
- O banco central do Irã afrouxou discretamente os controles sobre moeda estrangeira para incentivar comerciantes a repatriar recursos de que o país precisa, informou o Financial Times em 9 de setembro.
- Um bloqueio americano aos portos iranianos apertou a economia do país ao limitar suas exportações de petróleo.
- Os militares americanos vêm escoltando um número limitado de navios por uma rota no estreito de Ormuz, na altura de Omã.
- O governo Trump sancionou em 8 de setembro mais de duas dezenas de companhias aéreas comerciais e privadas iranianas e prestadores estrangeiros de serviços de carga.
- As sanções fazem parte de uma nova ofensiva para isolar Teerã de seus parceiros comerciais restantes.
- Pelo estreito de Ormuz passavam cerca de 20% do petróleo mundial antes da guerra, e o estreito se tornou o principal campo de batalha do conflito entre Estados Unidos e Irã.
**Fontes:**
- [S75] Financial Times — https://www.ft.com/content/c1029e47-7487-4bd7-8ed4-7512b76f1834
- [S76] NBC News — https://www.nbcnews.com/world/iran/us-strikes-iranian-tankers-attempted-missile-attacks-navy-warship-rcna596699
