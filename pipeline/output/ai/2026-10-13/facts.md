# Fatos — Newsletter [Tech] 13 de Outubro de 2026

## Meta — Muse Wonder, seus primeiros modelos de fronteira
- O Meta Superintelligence Labs lançou o Muse Wonder e o Muse Wonder Full na segunda-feira, 12 de outubro de 2026.
- Os dois modelos são a primeira tentativa da Meta de lançar um modelo de fronteira.
- O Muse Wonder está disponível via Meta Model API e via Muse Code.
- O preço do Muse Wonder é US$4 por milhão de tokens de input e US$20 por milhão de tokens de output.
- O preço de tokens de input em cache é US$0,20 por milhão.
- O Muse Wonder Full está disponível apenas para assinantes do Muse Code, não pela API.
- O Muse Wonder Full é oferecido nos planos Power Usage (US$50 por mês) e Maximum Usage (US$200 por mês) do Muse Code.
- Nenhum dos dois modelos Wonder tem pesos disponíveis para download.
- A ausência de pesos abertos rompe com o histórico de modelos abertos da Meta com o Llama.
- Segundo a Meta, os modelos foram treinados no data center Prometheus, de escala de gigawatt.
- A Meta descreve o Muse Wonder como seu modelo mais alinhado até hoje.
- A Meta diz que um relatório de segurança completo será publicado.
- A Artificial Analysis deu nota 56 ao Wonder Full em seu Intelligence Index.
- A nota 56 empata com o Claude Sonnet 5.5, da Anthropic.
- O Wonder Full ficou à frente do GPT-6 Astra (OpenAI), do Gemini 4 Argon (Google) e do Claude Fable 5.1 (Anthropic), que marcaram 53 cada.
- Entre esses modelos, apenas o Claude Opus 5.5 teve nota mais alta, 58.
- O Muse Wonder padrão marcou 52 no índice.
- Segundo testes da Meta, o Muse Wonder supera o Fable, o Opus e o Astra no MemoryBench, um benchmark de memória.
**Fontes:**
- [S1] Meta AI Research — https://research.meta.ai/blog/muse-wonder
- [S2] Meta Developers — https://dev.meta.ai/resources/blog/build-with-muse-wonder
- [S3] TechCrunch — https://techcrunch.com/2026/10/12/meta-releases-its-first-frontier-model-muse-wonder/
- [S4] VentureBeat — https://venturebeat.com/technology/metas-new-muse-wonder-and-muse-wonder-full-models-achieve-frontier-performance-but-only-the-weaker-one-is-available-via-api

## Character.AI — pedido de Chapter 11 com lance da Disney
- A Character Technologies (Character.AI) abriu um processo voluntário de Chapter 11 (recuperação judicial nos EUA) no Tribunal de Falências dos EUA para o Distrito de Delaware.
- O objetivo do processo é vender todos ou substancialmente todos os ativos da empresa.
- A empresa pretende manter a plataforma em operação durante a venda.
- A Disney é a stalking horse bidder (licitante que define o lance mínimo do leilão).
- A Disney oferece US$20 milhões por uma licença perpétua não exclusiva de parte da propriedade intelectual e de certos direitos de ação da Character.AI.
- O lance da Disney inclui também serviços de transição prestados por ex-funcionários da Character.AI contratados pela Disney.
- O lance da Disney está sujeito a ofertas maiores.
- O pedido lista passivos estimados entre US$50 milhões e US$100 milhões.
- No mês passado, a Disney contratou o ex-CEO da Character.AI, Karandeep Anand, como CTO.
- Segundo os autos, o Google é o maior credor, com mais de US$4 milhões a receber.
- A empresa espera concluir o processo de venda no fim de novembro ou início de dezembro de 2026.
- Antes do pedido, a Character.AI enfrentava processos judiciais e escrutínio sobre a segurança de seus chatbots.
- Segundo o Law360, a empresa atribuiu a situação aos altos custos de desenvolvimento.
**Fontes:**
- [S5] Business Wire (via Yahoo Finance) — https://finance.yahoo.com/technology/ai/articles/character-ai-initiates-voluntary-chapter-035000862.html
- [S6] The Verge — https://www.theverge.com/ai-artificial-intelligence/1009802/character-ai-files-for-bankruptcy-disney
- [S7] The Hollywood Reporter — https://www.hollywoodreporter.com/business/digital/disney-may-buy-character-ai-chatbot-chapter-11-bankruptcy-1236728629/
- [S8] Law360 — https://www.law360.com/articles/2537224/character-ai-files-ch-11-with-20m-sale-bid-from-disney
- [S9] TechCrunch — https://techcrunch.com/2026/10/13/just-5-years-in-interactive-chatbot-platform-character-ai-files-for-bankruptcy/

## Anthropic — autorreplicação de IA em dispositivos IoT
- O Frontier Red Team da Anthropic publicou em 12 de outubro uma pesquisa sobre autorreplicação de modelos de IA.
- Os pesquisadores responsáveis são William Zhou e Daniel Freeman.
- A conclusão é que modelos de IA pequenos podem estar a meses de conseguir se autorreplicar em dispositivos IoT (internet das coisas) comerciais.
- Os exemplos citados de dispositivos são fornos inteligentes e TV boxes Android de marcas genéricas.
- Em uma demonstração, a equipe rodou o Gemma4-26B-A4B, do Google, distribuído em 15 TV boxes Android genéricas.
- Cada TV box custa cerca de US$55 e tem 4 GB de RAM.
- O conjunto produziu 0,39 token por segundo.
- Entre os modelos de pesos abertos testados, apenas o GLM-5.2, da Z.ai, completou a replicação de ponta a ponta.
- O GLM-5.2 chegou aos 8 nós em 4 de 5 tentativas.
- Um modelo de 9B parâmetros conseguiu rodar inferência em 8 de 9 tipos de hardware testados.
- A Anthropic mediu uma tendência de ganho de 13,7 pontos por ano no Epoch Capabilities Index para modelos abertos de até 30B parâmetros.
- Extrapolando essa tendência, a Anthropic projeta que um modelo pequeno atinja o nível do GLM-5.2 até o fim de 2026.
- Uma frota do tamanho da botnet Kimwolf (mais de 2 milhões de dispositivos) poderia hospedar cerca de 133 mil cópias do Gemma4-26B-A4B.
- Essa frota serviria cerca de 80 mil tokens por segundo.
- O poder de inferência equivaleria a no máximo cerca de 40 GPUs Nvidia H100.
- A replicação levaria dias por cópia.
- A Anthropic disse que um replicador desse tipo seria difícil de desligar porque "não há um ponto centralizado para desligar".
- A Anthropic reconheceu que ainda não existe um "replicador totalmente fora de controle".
**Fontes:**
- [S10] Anthropic — https://www.anthropic.com/research/self-replicating-ai
- [S11] CNBC — https://www.cnbc.com/2026/10/13/anthropic-ai-models-self-replication-smart-devices.html
- [S12] Technology.org — https://www.technology.org/2026/10/13/anthropic-small-ai-models-self-replicate-iot-devices/

## Anthropic — defesas contra ataques de destilação
- A Anthropic disse em 12 de outubro que novos métodos reduziram em cerca de 90% a 99% o volume de dados extraídos do Claude por ataques de destilação.
- Destilação, nesse contexto, é treinar um modelo com as respostas de outro modelo.
- Com o Claude Fable 5.1 e o Claude Opus 5.5, a Anthropic introduziu o "preserved thinking".
- O preserved thinking impede que contas de API criadas a partir de 31 de agosto de 2026 editem o contexto anterior do Claude.
- Um classificador de dois estágios detecta tentativas de extração.
- A taxa de falsos positivos do classificador é inferior a 0,1%.
- A Anthropic baniu dezenas de milhares de contas ligadas a destilação.
- Os banimentos ocorrem muitas vezes em menos de duas horas após o início de uma campanha.
- A Anthropic diz ter recusado receita significativa e trilhões de tokens de tráfego pago de destiladores.
- Dados da Anthropic mostram que transcrições de raciocínio dão grande ganho aos destiladores.
- Um modelo treinado com transcrições completas do Opus 4.8 marcou 80,4% no SWE-bench Verified.
- O mesmo modelo treinado com transcrições resumidas marcou 71,8%.
**Fontes:**
- [S13] Anthropic — https://www.anthropic.com/research/distillation-defenses
- [S14] LavX News — https://news.lavx.hu/article/anthropic-cuts-distillation-attacks-by-up-to-99-with-new-defenses
- [S15] Clauding — https://clauding.de/en/posts/anthropic-destillation-preserved-thinking/

## TypeSafe AI — rodada de US$870 milhões
- A TypeSafe AI captou US$870 milhões a um valuation de US$7,5 bilhões em 9 de outubro de 2026.
- A rodada foi liderada pela Andreessen Horowitz (a16z).
- Sequoia Capital, DCVC e investidores-anjo não identificados também participaram.
- A TypeSafe saiu do stealth em 15 de setembro de 2026.
- Na saída do stealth, a empresa anunciou um seed de US$40 milhões liderado pela DCVC.
- O seed foi feito a um valuation de cerca de US$200 milhões.
- O salto de valuation foi de cerca de 37 vezes em menos de um mês.
- A TypeSafe é a criadora do modelo Jev.
- O Jev devolve decisões ao código como valores tipados, em vez de texto.
- Segundo a a16z, o Jev custa entre 1/100 e 1/500 do preço de modelos de fronteira.
- Segundo a a16z, o Jev é 100 vezes mais rápido em tarefas de classificação com precisão comparável.
- O Jev atingiu 1 trilhão de tokens gerados em 3 dias após o lançamento.
- Segundo a empresa, cerca de um terço da Fortune 500 já usa o Jev.
- Os recursos vão financiar mais modelos da série "System One" e recursos corporativos.
- O CEO e cofundador Diogo Almeida é ex-pesquisador da OpenAI.
- Martin Casado, sócio-geral da a16z, entra no conselho.
**Fontes:**
- [S16] SiliconANGLE — https://siliconangle.com/2026/10/09/jev-creator-typesafe-closes-870m-round-at-7-5b-valuation/
- [S17] Andreessen Horowitz — https://a16z.com/announcement/investing-in-typesafe-ai/
- [S18] Seedtable — https://seedtable.com/companies/typesafe-ai/funding-rounds/series-a-2026-10

## SpaceXSI — X Subscription com Grok, Cursor e X Premium
- A SpaceXSI lançou a X Subscription em 12 de outubro.
- O plano reúne Grok, Grok Bot, Cursor e X Premium em uma única assinatura.
- A disponibilidade global será liberada ao longo dos dias seguintes.
- Os planos são: Free, Plus (US$8 por mês), Premium (US$30 por mês), Super (US$100 por mês) e Ultra (US$200 por mês).
- O Premium inclui os benefícios de SuperGrok, Cursor Pro e X Premium+.
- Esses benefícios custavam antes US$90 por mês somados.
- Grok e Cursor compartilham uma única cota de uso semanal.
- Modelos de terceiros no Cursor, como Claude ou GPT, não estão incluídos nos planos.
- Modelos de terceiros são cobrados a preço de tabela da API desde o primeiro uso.
- Cada plano da X Subscription inclui pelo menos o dobro de uso de programação com os modelos da própria SpaceXSI em relação ao plano equivalente do Cursor.
- Assinantes atuais podem manter seus planos.
- A SpaceXSI se chamava SpaceXAI.
- A SpaceXSI comprou a startup de programação Cursor em agosto.
**Fontes:**
- [S19] SpaceXSI — https://x.ai/news/x-subscription
- [S20] SpaceXSI Docs — https://docs.x.ai/x-subscription/overview
- [S21] Engadget — https://www.engadget.com/2284943/x-subscription-bundles-premium-grok-cursor/

## Anthropic e OpenAI — controle sobre publicações de avaliadores externos
- A Reuters informou em 13 de outubro que a Anthropic e a OpenAI buscaram controle significativo sobre o que avaliadores externos podem publicar.
- Segundo a Reuters, as empresas temem que os resultados revelem segredos comerciais.
- A Reuters cita duas pessoas a par das discussões.
- No mês passado, o CEO da Anthropic, Dario Amodei, disse que avaliadores externos deveriam poder publicar suas principais conclusões "sem controle editorial".
- A OpenAI concordou com essa posição dias depois.
- Até pelo menos 5 de outubro, as duas empresas buscavam controle editorial rígido.
- A Anthropic disse que os avaliadores com quem já trabalhou controlam seus métodos, conclusões e publicações.
- Para novas empresas de avaliação, a Anthropic se reserva o direito de comentar e aprovar os relatórios.
- A OpenAI disse que não busca direito de aprovação sobre o texto integral dos relatórios.
- A prática padrão da OpenAI é suprimir informações confidenciais.
- Os avaliadores podem informar se houve supressões relevantes.
- A avaliação independente é uma de quatro medidas de segurança de um acordo assinado pelo presidente Donald Trump e executivos de IA no fim de setembro.
- O acordo não tem mecanismo formal de cumprimento.
- A Anthropic nomeou a Faculty, braço de IA da Accenture, como sua primeira avaliadora integrada.
- Entre as ideias em discussão estão funcionários das empresas monitorando as equipes de avaliação integradas.
- Outra ideia em discussão é proibir que avaliadores trabalhem para duas empresas ao mesmo tempo.
**Fontes:**
- [S22] Reuters (via Investing.com) — https://www.investing.com/news/stock-market-news/exclusivebehind-ai-industrys-call-for-independent-reviews-a-fight-over-what-gets-made-public-4945991
- [S23] AI Affairs — https://www.aiaffairs.com/news/anthropic-openai-evaluator-publication-rights-scientists-ai-oversight/
- [S24] The Next Web — https://thenextweb.com/news/anthropic-openai-ai-evaluators-publication-control

## Nvidia na China — chips de games e queda de participação
- Empresas de tecnologia chinesas compraram mais de 1 milhão de chips de games e de workstation da Nvidia em 2026, segundo o Financial Times em 13 de outubro.
- Os chips são principalmente RTX Pro 6000D, RTX Pro 5000 e RTX 5090.
- As compras visam cobrir a falta de poder computacional para IA.
- Fontes do setor ouvidas pelo FT estimam a oferta doméstica de chips de IA da China em cerca de 3,5 milhões de unidades neste ano.
- Cerca de 1 milhão dessas unidades são fabricadas no exterior.
- A demanda deve superar em muito 5 milhões de unidades.
- A produção doméstica de chips de IA da China mais que dobrou neste ano.
- Os chips comprados cumprem os controles de exportação dos EUA.
- Os chips são inferiores ao Ascend 910C, da Huawei, na maioria dos aspectos.
- Os chips são suficientes para tarefas mais simples, como a etapa de prefill da inferência de IA.
- A Nvidia está lançando um novo chip de workstation, o RTX Pro 5500.
- Empresas chinesas manifestaram interesse em pedidos de mais de 2 milhões de unidades do RTX Pro 5500.
- Os embarques do RTX Pro 5500 começam, na melhor das hipóteses, no fim do ano.
- Reguladores chineses avaliam se essa demanda é necessária.
- Separadamente, um relatório da IDC visto pela Reuters em 13 de outubro coloca a participação da Nvidia no mercado chinês de chips de IA para data centers em 34% no primeiro semestre de 2026.
- A Nvidia (NVDA) embarcou 678 mil aceleradores na China no semestre, queda de 44% na comparação anual.
- A Huawei embarcou 572 mil aceleradores no semestre, ante pouco mais de 300 mil um ano antes.
- A participação da Huawei foi de 28%.
- A T-Head teve 7%, a Cambricon 5%, a Kunlunxin 4% e a Hygon 3%.
- Os embarques totais de aceleradores de IA na China somaram cerca de 2,008 milhões de unidades no primeiro semestre.
- Os aceleradores não-GPU cresceram quase 80%, para 1,016 milhão de unidades.
- As GPUs somaram 991 mil unidades, queda de 26%.
- Foi a primeira vez que os aceleradores não-GPU superaram as GPUs.
**Fontes:**
- [S25] Financial Times — https://www.ft.com/content/9dbd99db-6b0c-43bd-b7be-849f129df098
- [S26] Tom's Hardware — https://www.tomshardware.com/pc-components/gpus/chinese-ai-companies-buy-1-million-nvidia-gpus-in-a-single-year-report-claims-export-control-compliant-chips-flood-the-market-to-bridge-gap-in-compute-demand
- [S27] TIKR — https://www.tikr.com/blog/chinese-tech-firms-bought-1-million-nvidia-gaming-chips-this-year-heres-where-it-shows-up
- [S28] Dealroom — https://app.dealroom.co/news/note/chinese-tech-firms-bought-more-than-1mn-nvidia-gaming-and-workstation-chips-this-year-to-work-around-export-controls
- [S29] Economic Daily News — https://money.udn.com/money/story/5599/9811194
- [S30] GuruFocus — https://www.gurufocus.com/news/9120338/nvidia-loses-ground-in-china-as-ai-chip-shipments-plunge-44
- [S31] The Inference — https://theinference.org/article/nvidia-falls-to-34-of-china-s-ai-chip-market-as-huawei-takes-28

## Broadcom — Hock Tan compara investidores de IA a apostadores de cassino
- O CEO da Broadcom, Hock Tan, falou na conferência Asia Future Forward, do DBS, em Singapura, em 12 de outubro.
- Tan disse que muitos investidores de IA "não têm ideia do que estão investindo".
- Tan disse que esses investidores criam expectativas tão extremas que "é quase como se estivessem num cassino".
- Tan disse que a receita anualizada de US$50 bilhões da OpenAI em setembro indica um modelo de negócio viável.
- Tan disse que essa receita dá pouca garantia de lucratividade de longo prazo, porque a OpenAI ainda perde dinheiro com treinamento.
- Tan alertou que a falta de capital pode se tornar o próximo limite ao crescimento do setor.
- Tan disse que as empresas de IA precisam de clientes que gerem retorno, e não de usuários "desperdiçando dinheiro" com tokens.
- Em 13 de outubro, a Samsung Electronics chegou a cair 8,8% e a SK Hynix, 9,2%.
- O Kospi, índice da bolsa sul-coreana, chegou a cair 7%.
- O índice de Taiwan caiu 2,5% e a TSMC, 2%.
- Nos EUA, em 12 de outubro, a Micron caiu quase 4%.
- O Philadelphia Semiconductor Index caiu 2,7%.
- Samsung e SK Hynix acumulam queda de cerca de 15% em cinco pregões.
- Outro fator citado para a queda foi o temor de concorrência da fabricante chinesa de memória CXMT.
- A CXMT anunciou avanço em uma tecnologia de DRAM que também está sendo desenvolvida pela SK Hynix e pela Micron.
**Fontes:**
- [S32] Bloomberg — https://www.bloomberg.com/news/articles/2026-10-12/broadcom-ceo-likens-many-ai-investors-to-casino-gamblers
- [S33] CNBC TV18 — https://www.cnbctv18.com/market/bunch-of-casino-gamblers-broadcom-ceo-remarks-trigger-broader-sell-off-among-chip-stocks-20010406.htm
- [S34] The Economic Times — https://economictimes.indiatimes.com/markets/stocks/news/ai-investors-or-casino-gamblers-what-broadcom-ceo-hock-tan-said-that-sparked-sharp-global-ai-selloff/articleshow/134911377.cms
- [S35] TokenPost — https://www.tokenpost.com/news/investing/30860
- [S36] MarketWatch — https://www.marketwatch.com/story/was-broadcom-ceo-bullish-or-bearish-on-ai-gamblers-comment-creates-storm-33f11787

## CXMT — DRAM 4F² para servidores até o fim do ano
- O presidente da CXMT, Cao Kanyu, falou na Integrated Circuit and Chiplet Conference, em Xangai, realizada em 9 e 10 de outubro.
- Cao disse que a CXMT lançará até o fim de 2026 um módulo de memória DDR5 RDIMM para servidores baseado na estrutura de célula 4F².
- A estrutura 4F² reduz a área da célula de memória em cerca de 33% em relação à 6F², padrão do setor.
- A CXMT construiu a estrutura sobre um transistor de porta vertical envolvente (VSG), voltado a resolver o vazamento de corrente.
- A Samsung prevê produção em massa de 4F² em 2028.
- A SK Hynix divulgou um roteiro para 4F² no ano passado.
- Pelos cronogramas anunciados, a CXMT estaria cerca de dois anos à frente da Samsung.
- A CXMT não informou velocidades, capacidades, rendimentos, clientes nem volumes.
- A CXMT não publicou comunicado sobre o produto.
- O lançamento marca a entrada da CXMT em memória para servidores, segmento dominado por poucos fabricantes estrangeiros.
- Até aqui, o negócio da CXMT era focado em eletrônicos de consumo.
**Fontes:**
- [S37] Seoul Economic Daily — https://en.sedaily.com/international/2026/10/12/chinas-cxmt-says-server-dram-with-4f2-design-due-this-year
- [S38] Tom's Hardware — https://www.tomshardware.com/pc-components/dram/cxmt-president-says-companys-first-4f2-dram-will-be-a-server-ddr5-rdimm-due-by-year-end-vertical-transistors-cut-each-memory-cells-footprint-by-a-third-on-paper-but-no-speeds-or-capacities-yet
- [S39] Global Times — https://www.globaltimes.cn/page/202610/1371987.shtml
- [S40] TrendForce — https://www.trendforce.com/news/2026/10/12/news-cxmt-accelerates-4f%c2%b2-dram-push-eyes-year-end-server-ddr5-rdimm-launch/

## Volta — empréstimo de US$5 bilhões com garantia parcial dos bancos
- JPMorgan e Goldman Sachs lideram a venda de um empréstimo de US$5 bilhões para a Volta Infrastructure Holdings, startup de nuvem para IA.
- Os bancos garantiram (underwriting) um term loan de US$1,3 bilhão.
- Um empréstimo de US$3,7 bilhões para chips ficou sem garantia dos bancos.
- A informação foi publicada pela Bloomberg em 12 de outubro.
- O empréstimo de US$3,7 bilhões vai comprar cerca de 36 mil GPUs da Nvidia.
- O de US$1,3 bilhão cobre pagamentos de aluguel à mineradora de bitcoin Bitdeer por um complexo de data centers na Noruega.
- A Anthropic assinou um contrato de seis anos de poder computacional nesse local.
- A operação relançada paga SOFR (taxa de juros de referência dos EUA) mais 625 a 650 pontos-base.
- O desconto de emissão original (OID) é de 97 a 98.
- O rendimento fica entre 11,21% e 11,75%.
- Uma tentativa anterior a SOFR mais 500 pontos-base não foi absorvida pelo mercado.
- O prazo para compromissos é 14 de outubro.
**Fontes:**
- [S41] Bloomberg — https://www.bloomberg.com/news/articles/2026-10-12/jpmorgan-goldman-curb-exposure-on-5-billion-volta-ai-loan-sale
- [S42] Mint (Bloomberg) — https://www.livemint.com/companies/jpmorgan-goldman-curb-exposure-on-5-billion-volta-ai-loan-sale-11791831660356.html
- [S43] AI Weekly — https://aiweekly.co/alerts/jpmorgan-goldman-underwrite-only-13b-of-voltas-5b-ai-loan

## NTT Data — data center da Anthropic em Osaka
- A NTT Data Group está em negociações finais para construir um data center para a Anthropic em uma área costeira do sul da província de Osaka, segundo o Nikkei em 13 de outubro.
- Seria o primeiro data center dedicado da Anthropic no Japão.
- Só a construção pode custar até ¥1 trilhão (US$6,3 bilhões).
- Com os servidores de GPU, o total pode chegar a vários trilhões de ienes.
- O local consumiria até 500 MW, o que o colocaria entre os maiores do Japão.
- As empresas pretendem assinar o acordo até o fim de março de 2027.
- A operação parcial pode começar já em 2028.
- Puxar 500 MW da rede elétrica seria lento.
- Por isso, o projeto vai avaliar primeiro alternativas como geração no local e células de combustível.
- As duas empresas não quiseram comentar.
**Fontes:**
- [S44] Nikkei Asia — https://asia.nikkei.com/business/technology/artificial-intelligence/ntt-to-build-first-data-center-for-anthropic-in-japan
- [S45] The Next Web — https://thenextweb.com/news/ntt-data-anthropic-osaka-data-centre
- [S46] The Asia Business Daily — https://www.asiae.co.kr/en/article/2026101314512729280

## Omron — compra da OnLogic por US$675 milhões
- A Omron fechou acordo em 10 de outubro de 2026 (horário do Japão) para comprar a Interlogic e sua subsidiária OnLogic.
- A OnLogic é uma empresa americana que desenvolve e fabrica PCs industriais robustos.
- O preço é de US$675 milhões em enterprise value (valor da empresa livre de dívida e caixa).
- O pagamento será em dinheiro, principalmente com caixa próprio da Omron.
- A Omron pretende combinar os PCs industriais da OnLogic com sua tecnologia de controle de alta precisão, sensoriamento e robótica.
- O objetivo é desenvolver plataformas de IA física de próxima geração.
- A Omron está em transição a partir do perfil de fabricante de equipamentos de automação industrial.
- Mais de 90% das vendas da OnLogic vêm das Américas e da Europa.
- A OnLogic manterá a marca e o CEO Sean Larkin.
- A OnLogic operará como negócio independente.
- A conclusão está prevista para janeiro de 2027, sujeita a aprovações.
**Fontes:**
- [S47] Omron (TDnet filing) — https://fs2.magicalir.net/tdnet/2026/6645/20261009548915.pdf
- [S48] CNA (Reuters) — https://www.channelnewsasia.com/business/japans-omron-buy-us-industrial-pc-firm-onlogic-675-million-in-physical-ai-push-6454536
- [S49] The Ledger Asia — https://theledger.asia/omrons-us675-million-onlogic-deal-builds-a-physical-ai-platform/

## DayOne — financiamento adicional para data centers em Johor
- Um consórcio de sete bancos estruturou um financiamento adicional de RM15 bilhões (US$3,67 bilhões) para a plataforma de data centers da DayOne em Johor, na Malásia.
- Os bancos são CIMB, Crédit Agricole CIB, DBS, Maybank, OCBC, Standard Chartered e UOB.
- O anúncio foi feito em 13 de outubro.
- O novo financiamento é composto por um term loan offshore de US$2,4 bilhões e uma linha Murabahah (modalidade islâmica) de RM5,5 bilhões (cerca de US$1,35 bilhão).
- Somado aos RM15 bilhões obtidos em 2025, o financiamento da DayOne em Johor chega a RM30 bilhões (cerca de US$7,34 bilhões).
- Os recursos vão financiar a próxima fase de capacidade hyperscale.
- A DayOne opera duas instalações em Johor, no Nusajaya Tech Park e no Kempas Tech Park.
- As duas instalações somam 120 MW.
**Fontes:**
- [S50] UOB — https://www.uobgroup.com/uobgroup/newsroom/news-releases/2026/7-lender-consortium-for-dayone-johor.page
- [S51] DealStreetAsia (Reuters) — https://www.dealstreetasia.com/stories/data-centre-dayone-financing-malaysia-497927
- [S52] DatacenterDynamics — https://www.datacenterdynamics.com/en/news/dayone-secures-367bn-in-funding-for-malaysia-expansion/
- [S53] The Edge Malaysia — https://theedgemalaysia.com/node/821592

## Houthis — ataque ao aeroporto de Riad e possível entrada dos EUA
- Um míssil houthi atingiu um terminal de passageiros do Aeroporto Internacional King Khalid, em Riad, no sábado, 10 de outubro.
- O ataque matou 13 pessoas, entre elas um cidadão americano.
- Mais de 300 pessoas ficaram feridas.
- Perguntado se os EUA se juntariam aos ataques sauditas contra os houthis, Trump disse: "Talvez. Vamos analisar... Agimos muito rápido."
- Em setembro, Trump recusou duas vezes pedidos do príncipe herdeiro Mohammed bin Salman para bombardear os houthis.
- Em vez de bombardeios, Trump forneceu a Riad dados de inteligência e de alvos.
- Em 12 de outubro, um representante houthi ameaçou uma resposta "rápida e dolorosa" contra os EUA e seus interesses na região caso Washington entre no conflito.
- O representante alertou trabalhadores de instalações de petróleo e aeroportos sauditas de que esses locais são "alvos legítimos".
- O aeroporto de Riad seguia fechado.
- Os ataques houthis ao aeroporto mataram 20 pessoas em uma semana.
- O ministro da Energia saudita, príncipe Abdulaziz bin Salman, disse que o reino dará uma resposta "igualmente séria" aos ataques.
- O Brent fechou em alta de US$1,93 (1,8%), a US$106,65 o barril, em 12 de outubro.
- Foi o maior fechamento do Brent desde 15 de setembro.
- O setor de energia do S&P 500 teve fechamento recorde.
- O Goldman Sachs elevou sua previsão para o Brent em dezembro de US$85 para US$90 o barril.
- O Goldman estima um prêmio de risco de pouco mais de US$20 por barril.
- O chefe de segurança do Irã, Mohsen Rezaei, disse que o sistema de transporte com apoio dos EUA que leva petróleo do Golfo para fora do Estreito de Ormuz é um alvo explícito.
- Rezaei ameaçou cabos, data centers e instalações de IA ligados aos EUA nos Emirados Árabes Unidos.
**Fontes:**
- [S54] CNBC — https://www.cnbc.com/2026/10/11/trump-saudi-arablia-iran-houthis.html
- [S55] Newsweek — https://www.newsweek.com/trump-houthis-saudi-arabia-iran-war-12556349
- [S56] CBS News — https://www.cbsnews.com/live-updates/iran-war-us-trump-saudi-arabia-houthi/
- [S57] Updater News — https://updater.news/oil-energy-stocks-climb-after-houthi-strike-on-riyadh/
- [S58] Al Jazeera — https://1-e8259.azureedge.net/economy/2026/10/12/iran-sets-crosshairs-on-us-uae-oil-shuttle-out-of-strait-of-hormuz

## Rússia e Ucrânia — "cessar-fogo energético" de Trump e acordo de diesel
- Na sexta-feira, 9 de outubro, Trump fechou acordo com Putin para comprar diesel russo.
- O objetivo é conter os altos preços de combustível antes das eleições de meio de mandato nos EUA.
- A Rússia forneceria inicialmente mais de 300 mil toneladas de diesel.
- Em novembro, o fornecimento seria de 500 mil toneladas.
- Depois, seria de 1 milhão de toneladas por período.
- O acordo opera sob uma isenção temporária de sanções do Tesouro dos EUA.
- No domingo, 11 de outubro, Trump publicou no Truth Social: "Com efeito imediato, há um CESSAR-FOGO ENERGÉTICO na guerra entre Rússia e Ucrânia. As duas partes concordaram. Não o quebrem!"
- Zelensky disse que o acordo era "novidade para mim".
- Após o anúncio, a Rússia atacou a usina termelétrica CHP-5, em Kharkiv.
- Em seguida, um ataque de míssil russo a um mercado perto de Kharkiv matou três pessoas e feriu pelo menos 22.
- Na segunda-feira, 12 de outubro, o chanceler russo, Sergey Lavrov, disse que Zelensky não "merece uma trégua".
- Zelensky disse que a Rússia atingiu seis instalações de energia ucranianas naquele dia, ferindo 33 pessoas.
- No mesmo dia, a UE adotou quase 1.600 novas sanções contra o complexo militar-industrial russo.
- Zelensky disse que a Ucrânia poderia realizar eleições se a Rússia aceitasse um cessar-fogo total de 60 dias.
- Um ataque russo com bomba guiada a uma área residencial de Zaporizhzhia em 10 de outubro matou 23 pessoas, entre elas quatro crianças.
- Um ataque de drone ucraniano em 11 de outubro paralisou o data center da Yandex em Vladimir.
- Foi o terceiro ataque a instalações da Yandex em quatro dias.
- O ataque interrompeu serviços de táxi e bancários em dezenas de cidades russas e no Cazaquistão, em Belarus e na Armênia.
**Fontes:**
- [S59] The Guardian — https://www.theguardian.com/world/2026/oct/11/zelenskyy-trump-ukraine-russia-energy-ceasefire
- [S60] Kyiv Independent — https://kyivindependent.com/russia-struck-kharkivs-power-plant-shortly-after-trump-announced-energy-ceasefire/
- [S61] BBC News — https://www.bbc.com/news/live/cqe8ry0xxp85t
- [S62] PBS NewsHour (AP) — https://www.pbs.org/newshour/world/trump-claims-russia-and-ukraine-agree-to-energy-ceasefire-despite-continued-attacks
- [S63] Philadelphia Inquirer (AP) — https://www.inquirer.com/news/nation-world/russia-ukraine-trump-energy-ceasefire-zelensky-putin-yandex-20261011.html
- [S64] Rig & Refinery — https://rigandrefinery.com/articles/brent-hits-107-bbl-as-hormuz-attacks-overrun-diesel-deal-5cf5b976

## FMI — previsão de crescimento global de 3,1% em 2026
- O FMI divulgou o World Economic Outlook de outubro de 2026 em 13 de outubro, nas reuniões anuais em Bangkok.
- O FMI projeta crescimento global de 3,1% em 2026.
- A previsão de julho era de 3,0%.
- O crescimento em 2025 foi de 3,5%.
- Para 2027, a previsão é de 3,4%.
- A revisão para cima se deve em grande parte ao investimento em infraestrutura de IA.
- Países fornecedores de hardware de IA tiveram revisões para cima, entre eles Coreia do Sul, Malásia, México e Tailândia.
- O FMI projeta inflação global cheia de 4,7% em 2026.
- A inflação deve recuar para 4,1% em 2027.
- A alta da inflação é puxada principalmente por preços de energia e alimentos.
- O relatório alerta que uma reavaliação da lucratividade e da produtividade da IA pode reduzir fortemente o investimento e provocar correções nas bolsas.
- Segundo o relatório, os riscos são predominantemente de baixa.
- O FMI prevê crescimento de 1,1% para a zona do euro em 2026.
**Fontes:**
- [S65] Associated Press — https://apnews.com/article/imf-economy-growth-ai-war-oil-23aa01c0c6922fbf0b564a0ff9b2c8e5
- [S66] The Straits Times — https://www.straitstimes.com/asia/se-asia/imf-says-ai-investment-propping-up-global-growth-but-war-and-debt-threaten-outlook
- [S67] International Monetary Fund — https://bankar.me/wp-content/uploads/2026/10/text.pdf
- [S68] Euronews — https://www.euronews.com/2026/10/13/imf-forecasts-31-global-growth-in-2026-with-eurozone-at-11

## Bumble — fechamento de capital pela Ithaca Holdings
- A Bumble anunciou em 13 de outubro um acordo definitivo para ser comprada pela Ithaca Holdings.
- A operação é toda em dinheiro e avalia a empresa de aplicativo de namoro em US$1,3 bilhão.
- A Bumble é listada na Nasdaq sob o ticker BMBL.
- Os acionistas receberão US$6,05 por ação em dinheiro.
- O valor representa prêmio de cerca de 138% sobre o fechamento de 9 de outubro, antes do anúncio.
- O prêmio é de cerca de 119% sobre o preço médio ponderado por volume (VWAP) de 30 dias.
- Os co-CEOs da Ithaca, Ravi Gupta e John Hegeman, se tornarão co-CEOs da Bumble.
- Gupta e Hegeman vão trabalhar em parceria com a fundadora Whitney Wolfe Herd.
- A Ithaca descreve sua missão como aplicar tecnologia de fronteira para renovar empresas em um mundo transformado pela IA.
- Afiliadas da Blackstone e Wolfe Herd aprovaram o negócio por consentimento escrito de acionistas.
- O acordo de fusão foi assinado em 12 de outubro.
- Segundo o TechCrunch, o negócio vem após anos de queda no número de assinantes e na receita da Bumble.
**Fontes:**
- [S69] Bumble Inc. — https://ir.bumble.com/news/news-details/2026/Bumble-Inc--to-Be-Acquired-by-Ithaca-Holdings-the-Long-Term-Holding-Company-for-Enduring-Technology-Businesses/default.aspx
- [S70] FT.com (Business Wire) — https://markets.ft.com/data/announce/detail?dockey=600-202610130824BIZWIRE_USPRX____20261013_BW006131-1
- [S71] EDGAR Tools — https://app.edgar.tools/news/8b529f5dd86af977
- [S72] TechCrunch — https://techcrunch.com/2026/10/13/bumble-agrees-to-a-1-3b-acquisition-deal-as-online-dating-faces-a-reset/

## FDA — aprovação do Hovilpri contra herpes simplex
- A FDA (agência reguladora de medicamentos dos EUA) aprovou o Hovilpri (pritelivir) em 9 de outubro de 2026.
- É a 46ª aprovação de medicamento novo da FDA no ano.
- O Hovilpri é indicado para adultos imunocomprometidos com lesões mucocutâneas de herpes simplex (HSV) que não responderam a outras terapias.
- O medicamento é um inibidor oral de helicase-primase.
- Segundo a Asahi Kasei, é a primeira terapia para HSV aprovada pela FDA com novo mecanismo de ação em quase 30 anos.
- O medicamento foi desenvolvido pela AiCuris, hoje parte da Asahi Kasei Therapeutics.
- No estudo de Fase 3 PRIOH-1, 63% dos pacientes tratados com Hovilpri tiveram cicatrização completa das lesões até o dia 28.
- No grupo com tratamento à escolha do investigador, a taxa foi de 34%.
- O medicamento recebeu as designações Fast Track e Breakthrough Therapy e teve Priority Review.
- O Hovilpri deve estar disponível nos EUA antes do fim de 2026.
**Fontes:**
- [S73] FDA — https://www.fda.gov/drugs/novel-drug-approvals-fda/novel-drug-approvals-2026
- [S74] Asahi Kasei — https://www.asahi-kasei.com/news/2026/e261013

## SpaceX — CRS-35 leva os últimos painéis solares novos da ISS
- Um Falcon 9 lançou a Cargo Dragon na missão CRS-35, da NASA, a partir de Cape Canaveral, às 6h33 (horário da costa leste dos EUA) de 13 de outubro.
- A cápsula leva mais de 6.300 libras de experimentos científicos e suprimentos.
- O compartimento externo (trunk) da Dragon leva o quarto e último par de Roll-Out Solar Arrays (ROSA) para a Estação Espacial Internacional (ISS).
- Os painéis foram fabricados pela Redwire.
- Cada painel fornece mais de 20 kW por mais de 10 anos.
- A NASA descreveu a carga como incluindo o último conjunto de ROSA da ISS.
- A Dragon deve ficar cerca de um mês na estação.
- A cápsula deve amerissar na costa da Califórnia em meados de novembro.
- A carga inclui equipamentos para fabricar retinas artificiais em microgravidade.
- A carga inclui modelos 3D de tecido cardíaco.
- A carga inclui organoides cerebrais para pesquisa de doenças neurodegenerativas.
- A Dragon se acopla ao módulo Harmony em 15 de outubro.
- Uma versão do ROSA vai ajudar a alimentar o Space Reactor 1 Freedom (SR-1 Freedom), da NASA, com lançamento previsto para 2028.
**Fontes:**
- [S75] Spaceflight Now — https://spaceflightnow.com/2026/10/13/spacex-launches-nasa-science-and-cargo-to-the-international-space-station/
- [S76] NASA — https://www.nasa.gov/news-release/nasa-sets-coverage-for-spacex-35th-station-resupply-launch-arrival/
