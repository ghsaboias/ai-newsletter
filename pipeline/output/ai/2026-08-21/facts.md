# Fatos — Newsletter [Tech] 21 de Agosto de 2026

## DeepSeek — modelo multimodal experimental V4-Flash-Vision-Exp
- A DeepSeek colocou o DeepSeek-V4-Flash-Vision-Exp no ar em sua plataforma de API em 21 de agosto de 2026.
- É um modelo multimodal experimental, chamado pela API com `model='deepseek-v4-flash-vision-exp'`.
- O modelo iguala o DeepSeek-V4-Flash em capacidades de texto, incluindo agentes, raciocínio e conhecimento de mundo.
- Em benchmarks de agentes que exigem compreensão visual, a DeepSeek diz que o modelo dá um salto significativo sobre o V4-Flash, que é apenas de texto.
- A empresa afirma que isso aproxima o desempenho multimodal de agentes do Opus-4.8, da Anthropic.
- Na tabela publicada pela própria DeepSeek, o modelo supera o Opus-4.8 em três de onze benchmarks.
- No ApexBench o modelo marca 36,5 contra 26,2 do V4-Flash.
- No Agents' Last Exam marca 27,3 contra 25,2 do V4-Flash.
- Uma nota de rodapé da própria DeepSeek admite que a comparação é distorcida: nessas duas avaliações o V4-Flash, só de texto, "ignora os elementos multimodais nelas contidos".
- Ou seja, o modelo antigo é pontuado em testes com imagens que ele não consegue ver.
- O modelo é um mixture-of-experts esparso (arquitetura em que só parte dos parâmetros é ativada a cada consulta) com 13 bilhões de parâmetros ativos de um total de 284 bilhões.
- A janela de contexto é de 1.048.576 tokens e o output máximo é de 384 mil tokens.
- No OpenRouter, o preço é de US$0,22 por milhão de tokens de input e US$0,66 por milhão de tokens de output.
- Imagens são tokenizadas para cobrança: até 384 tokens cada, ao preço do V4-Flash.
- A DeepSeek lançou no mesmo dia o Harness 0.1.1, com suporte nativo ao novo modelo.
**Fontes:**
- [S1] DeepSeek API Docs — https://api-docs.deepseek.com/news/news260821/
- [S2] DeepSeek API Docs — https://api-docs.deepseek.com/updates/
- [S3] The Next Web — https://thenextweb.com/news/deepseek-v4-flash-vision-exp-opus-benchmarks
- [S4] OpenRouter — https://openrouter.ai/deepseek/deepseek-v4-flash-vision-exp

## Anthropic — IPO no tamanho do recorde da SpaceX
- A Anthropic espera igualar ou superar o tamanho do IPO recorde da SpaceX, segundo pessoas a par do assunto.
- A empresa se prepara para protocolar publicamente seu megaIPO já no fim de agosto de 2026.
- Apresentações recentes a investidores, conduzidas pelo CFO Krishna Rao, contornaram a questão do valuation.
- A SpaceX levantou US$75 bilhões na largada, na maior venda inicial de ações da história.
- O número final subiu para US$86,2 bilhões com o exercício da opção de lote suplementar (overallotment).
- Uma estreia maior que a da SpaceX faria de 2026 o melhor ano da história em volume de IPOs nos EUA.
- Empresas recém-listadas já levantaram US$160,6 bilhões até 19 de agosto, ante o recorde de US$195,2 bilhões de 2021.
- A Anthropic está a caminho de abrir capital antes da OpenAI, que agora mira uma listagem em 2027.
- As duas empresas protocolaram seus pedidos de listagem de forma confidencial.
- A Anthropic entregou seu rascunho de Formulário S-1 à SEC em 1º de junho de 2026, de forma confidencial.
- A empresa levantou US$65 bilhões a um valuation pós-money de US$965 bilhões no fim de maio.
**Fontes:**
- [S5] Bloomberg Tax — https://news.bloombergtax.com/financial-accounting/anthropic-expects-to-match-spacexs-record-ipo-size-or-top-it
- [S6] Yahoo Finance / Bloomberg — https://finance.yahoo.com/technology/ai/articles/anthropic-expects-match-spacex-record-175602035.html
- [S7] Reuters — https://www.reuters.com/business/ai-giant-anthropic-confidentially-files-us-ipo-2026-06-01/

## Nvidia e Poolside — licença de US$6 bilhões pelo "Model Factory"
- A Poolside fechou um acordo de licenciamento não exclusivo com a Nvidia no valor de US$6 bilhões, segundo carta a investidores obtida pela Newcomer.
- A Nvidia também investe US$1 bilhão na Poolside a um valuation pré-money de US$12 bilhões.
- A Nvidia licencia o "Model Factory", o sistema que a Poolside usou para construir seu modelo Laguna.
- A plataforma produz modelos de IA generativa voltados para desenvolvimento de software.
- A Nvidia está estendendo ofertas de emprego a 109 funcionários da Poolside que trabalharam no sistema.
- Os três fundadores da Poolside permanecem na empresa.
- A carta a investidores afirma que a transação "não é uma aquisição e não é um acquihire".
- A Poolside pretende distribuir os US$6 bilhões a seus investidores até o fim do ano que vem.
- A Nvidia já usou a mesma estrutura em acordos com a Groq (US$20 bilhões) e a Enfabrica (US$900 milhões).
- Como a licença é não exclusiva, a Poolside pode continuar vendendo a tecnologia a outros compradores.
- A Bloomberg noticiou em julho que a Nvidia avaliava investir até US$1 bilhão na Poolside.
- A Poolside buscava levantar US$2 bilhões a um valuation de US$12 bilhões, tendo obtido US$1 bilhão em compromissos.
- O valuation de US$12 bilhões é um salto ante os US$3 bilhões da empresa no ano anterior.
**Fontes:**
- [S8] Newcomer — https://www.newcomer.co/p/sources-poolside-strikes-6-billion
- [S9] The Decoder — https://the-decoder.com/nvidia-is-acquiring-poolsides-model-factory-and-109-employees-for-6-billion
- [S10] Crypto Briefing — https://cryptobriefing.com/nvidia-6b-poolside-ai-licensing-deal/
- [S11] Data Center Dynamics — https://www.datacenterdynamics.com/en/news/nvidia-to-invest-up-to-1bn-in-ai-firm-poolside-report/

## Google — Gemma passa de 1 bilhão de downloads
- O Google anunciou em 20 de agosto de 2026 que a família de modelos abertos Gemma superou 1 bilhão de downloads acumulados.
- Nos últimos dois anos, desenvolvedores publicaram mais de 100 mil variantes do Gemma.
- O Google chama esse ecossistema de "Gemmaverse".
- A empresa está lançando o repositório "Awesome Gemma" no GitHub, um diretório oficial de projetos, fine-tunes e ferramentas da comunidade.
- É a primeira vez que o Google divulga um total acumulado de adoção do Gemma desde o lançamento da família, no início de 2024.
- O anúncio foi assinado por Clement Farabet, vice-presidente do Google DeepMind, e pelo diretor de produto Olivier Lacombe.
- O recente Gemma Challenge no Kaggle recebeu mais de 1.600 inscrições de projetos.
- Os vencedores do desafio serão anunciados nas próximas semanas.
- No lançamento do Gemma 4, em abril de 2026, o número acumulado de downloads era de 400 milhões.
- Isso significa que os downloads mais que dobraram em cerca de quatro meses.
**Fontes:**
- [S12] Google — https://blog.google/innovation-and-ai/technology/developers-tools/gemma-one-billion-downloads/
- [S13] Unite.AI — https://www.unite.ai/googles-gemma-open-models-pass-1-billion-downloads-as-variants-top-100k/
- [S14] Google — https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/

## OpenAI — ChatGPT no Mac ganha acesso ao Apple Messages
- A OpenAI adicionou um plugin do Apple Messages ao aplicativo desktop do ChatGPT para macOS.
- O plugin lê e busca conversas, além de preparar e enviar mensagens.
- Funciona com iMessage, SMS e RCS.
- O recurso está disponível em todos os planos do aplicativo desktop para macOS.
- O plugin funciona apenas no ChatGPT Work e no Codex, não nas conversas normais do ChatGPT.
- Não é possível interagir com o ChatGPT remotamente pelo Messages.
- Por enquanto o recurso só funciona em Macs com Apple silicon, não em máquinas Intel.
- O usuário pode pedir ao ChatGPT que apague mensagens, redija e envie mensagens em seu nome ou busque informações enterradas no histórico.
- A OpenAI disse à Bloomberg que o plugin roda localmente na máquina do usuário e "não cria um índice de todas as mensagens de alguém".
- O envio exige aprovação por padrão.
- A OpenAI desaconselha ligar a aprovação persistente, alertando que isso "elimina sua última chance de revisar uma mensagem antes que o ChatGPT a envie como se fosse você".
- Em workspaces gerenciados, administradores podem desativar o plugin pelo controle já existente de Computer Use.
- A mesma atualização trouxe threads fixadas unificadas entre o app desktop e o iOS.
- A atualização também adicionou snapshots somente leitura de threads do Codex.
**Fontes:**
- [S15] 9to5Mac — https://9to5mac.com/2026/08/20/chatgpt-update-adds-apple-messages-integration-on-mac/
- [S16] TechCrunch — https://techcrunch.com/2026/08/20/chatgpt-can-now-send-texts-for-you-with-new-apple-messages-plugin/
- [S17] iClarified — https://www.iclarified.com/101839/chatgpt-for-mac-adds-apple-messages-plugin

## Micro1 — run rate bruto salta para US$500 milhões
- O run rate anual bruto da Micro1 passou de US$100 milhões para US$500 milhões nos últimos oito meses, segundo fonte citada pelo TechCrunch.
- O run rate anual líquido da empresa está entre US$150 milhões e US$200 milhões.
- A diferença entre bruto e líquido reflete o que a empresa paga aos especialistas humanos que produzem os dados de treinamento.
- O crescimento ocorre em meio ao boom do mercado de dados de treinamento para IA.
- Nesse mesmo mercado, a Nvidia negocia investir na fornecedora rival Mercor a um valuation de US$20 bilhões.
**Fontes:**
- [S18] TechCrunch — https://techcrunch.com/2026/08/20/ai-data-startup-micro1-reaches-500m-gross-run-rate-amid-ai-training-boom/

## Brasil — R$2,3 bilhões em computação para IA, divididos entre Huawei e fornecedores dos EUA
- O governo brasileiro anunciou na quinta-feira cerca de R$2,3 bilhões (US$444,2 milhões) para fortalecer o ecossistema nacional de IA.
- Os projetos foram divididos entre empresas dos Estados Unidos e da China, num movimento que equilibra as relações com as duas potências.
- Pouco mais da metade do total, R$1,3 bilhão (US$251 milhões), financia um projeto de infraestrutura de supercomputação no Rio de Janeiro.
- O projeto carioca é desenvolvido em parceria com as chinesas Huawei Technologies e iFlytek.
- O acordo de cooperação com as empresas chinesas está previsto para começar em julho de 2027.
- Cerca de R$1 bilhão será destinado a um edital para a compra de um supercomputador.
- O Brasil espera que a máquina fique entre as dez mais potentes do mundo em capacidade de processamento de IA.
- O equipamento será instalado no Rio Grande do Norte, escolhido pelo potencial energético.
- Lula participou da cerimônia de anúncio no estado na quinta-feira.
- O supercomputador do edital está especificado em 7,2 mil petaflops.
- O pacote também estrutura uma nuvem soberana brasileira, com dados armazenados em computadores no Brasil e software sob controle nacional.
- O centro de pesquisa carioca, com operação prevista para 2027, terá a missão de desenvolver um grande modelo de linguagem com competência em português e espanhol.
- O pacote inclui R$125 milhões para o desenvolvimento de chips livres de patente.
- Estão previstos R$1,27 bilhão ao longo de quatro anos para o centro de computação avançada no Rio.
- O pacote inclui ainda a formação de 3.000 profissionais brasileiros.
- Os recursos vêm do Fundo Nacional de Desenvolvimento Científico e Tecnológico (FNDCT), em desembolsos escalonados.
- O governo espera que o supercomputador do edital comece a operar até o fim do ano que vem.
**Fontes:**
- [S19] Al Jazeera / Reuters — https://www.aljazeera.com/economy/2026/8/21/brazil-launches-ai-supercomputer-push-while-balancing-us-and-chinese-tech
- [S20] Folha de S.Paulo — https://www1.folha.uol.com.br/tec/2026/08/governo-anuncia-r-25-bi-para-ia-com-supercomputador-no-rn-e-parceria-com-gigante-chines.shtml
- [S21] Estadão — https://www.estadao.com.br/brasil/governo-lanca-plano-de-ia-que-inclui-supercomputadores-nuvem-brasileira-e-parceria-com-a-china/

## Waymo — primeiro chip próprio, um ASIC de 5nm da TSMC
- Em post no blog de 20 de agosto, a Waymo detalhou pela primeira vez a arquitetura do computador de bordo de seus robotáxis.
- A empresa apresentou um ASIC (chip de aplicação específica) de 5 nanômetros de projeto próprio.
- A Waymo também nomeou os sete fornecedores com os quais monta o sistema.
- A empresa diz que só os ASICs entregam mais de 1.000 TOPS (trilhões de operações por segundo) de desempenho em aprendizado de máquina.
- Esse processamento é dedicado ao tratamento inicial dos dados dos sensores.
- O chip é fabricado no processo de 5nm da TSMC.
- Cada módulo de direção autônoma leva dois desses chips, rodando as mesmas cargas em paralelo.
- A redundância permite que um chip assuma o trabalho se o outro falhar.
- Antes disso, a Waymo usava FPGAs da Intel para o processamento dos sensores.
- Segundo a Waymo, o projeto do chip incorpora mais de 200 milhões de milhas de dados de direção autônoma.
- A empresa diz que o chip próprio diversifica seu fornecimento para além de terceiros como a Nvidia.
- Ainda assim, a Waymo lista como fornecedores AMD, Micron, Nvidia, Samsung, SanDisk, Socionext e TSMC.
- A Waymo afirma que o ASIC é "apenas um de vários componentes customizados empolgantes que estamos desenvolvendo".
- A empresa não disse quais são os outros componentes em desenvolvimento.
**Fontes:**
- [S22] The Verge — https://www.theverge.com/transportation/982653/waymo-brain-computer-chip-robotaxi-hardware-suppliers
- [S23] The Register — https://www.theregister.com/edge-and-iot/2026/08/20/waymo-has-designed-a-robocar-chip-to-stay-ahead-of-tesla/5290592
- [S24] SiliconANGLE — https://siliconangle.com/2026/08/20/waymo-details-the-custom-chip-in-its-autonomous-driving-system/
- [S25] The Next Web — https://thenextweb.com/news/waymo-custom-chip-robotaxi-tsmc-ojai
- [S26] Bloomberg via Yahoo Finance — https://uk.finance.yahoo.com/news/alphabet-waymo-built-custom-chip-140000003.html

## Broadcom — mais de US$60 bilhões em dívida para chips de IA da Anthropic
- A Bloomberg noticiou na quinta-feira, 20 de agosto, que a Broadcom negocia com um grupo de credores levantar mais de US$60 bilhões em dívida.
- O financiamento é para um acordo de chips de IA que beneficia a Anthropic e outras empresas.
- O pacote pode incluir uma tranche de dívida júnior de cerca de US$30 bilhões.
- Há também uma tranche sênior com garantia real que pode variar de US$60 bilhões a US$70 bilhões, parcialmente garantida pela Broadcom.
- Os números em discussão levariam o total captado a até US$100 bilhões.
- Blackstone e Apollo Global Management negociam participar do financiamento.
- A nova dívida seria emitida por um veículo de propósito específico (SPV).
- A operação sucede uma parceria de junho entre Broadcom, Apollo e Blackstone que financiou uma expansão de US$35 bilhões na capacidade computacional da Anthropic com chips customizados da Broadcom.
- O compromisso inicial deveria adicionar 1 gigawatt de capacidade computacional.
- A parceria como um todo mira viabilizar mais de 20 gigawatts de poder computacional para os principais laboratórios de IA até 2028.
- A Broadcom projeta chips customizados para empresas como Alphabet e Meta.
- A empresa também tem acordos de fornecimento de chips com Anthropic e OpenAI.
**Fontes:**
- [S27] Reuters — https://www.reuters.com/technology/broadcom-seeks-more-than-60-billion-latest-ai-debt-deal-bloomberg-news-reports-2026-08-20/
- [S28] Reuters via Yahoo Finance — https://finance.yahoo.com/technology/ai/articles/broadcom-seeks-more-60-billion-203818587.html
- [S29] ETCIO — https://cio.economictimes.indiatimes.com/news/next-gen-technologies/broadcom-in-talks-for-over-60-billion-ai-chip-financing-deal-benefiting-anthropic/133390864

## Nvidia e Rebellions — conversas com a startup coreana de chips
- A Bloomberg noticiou em 21 de agosto que a Nvidia está em discussões iniciais com a projetista coreana de chips de IA Rebellions.
- As possibilidades em discussão incluem uma parceria técnica, um investimento ou até uma aquisição.
- Jensen Huang se reuniu esta semana com o cofundador e CEO da Rebellions, Sunghyun Park, na sede da Nvidia em Santa Clara, Califórnia.
- A Rebellions foi fundada em 2020 e fica em Bundang, na Coreia do Sul.
- A empresa levantou cerca de US$850 milhões de investidores como SK hynix, Samsung Ventures e Arm Holdings.
- Seu valuation mais recente foi de cerca de US$2,3 bilhões.
- A Rebellions constrói unidades de processamento neural (NPUs) para inferência de IA em data centers.
- Seus chips já foram implantados em aplicações comerciais na Coreia do Sul.
- A empresa vem se expandindo no exterior e prepara um IPO na Coreia para o primeiro semestre de 2027.
- O National Growth Fund da Coreia do Sul fez um investimento direto de 250 bilhões de wons (US$166 milhões) na Rebellions em março.
- Foi o primeiro investimento direto sob a iniciativa governamental "K-Nvidia".
- As conversas são preliminares e podem não resultar em transação.
- A Nvidia não respondeu a pedidos de comentário e a Rebellions se recusou a comentar.
**Fontes:**
- [S30] The Edge Malaysia (Bloomberg) — https://theedgemalaysia.com/node/815413
- [S31] Traders Union — https://tradersunion.com/news/companies/show/3061614-nvidia-eyes-rebellions-deal/
- [S32] Reuters — https://www.reuters.com/world/asia-pacific/south-korea-invest-166-million-ai-chip-startup-rebellions-2026-03-26/

## Samsung — retorno recorde de até US$79,5 bilhões aos acionistas
- O conselho da Samsung aprovou na sexta-feira um plano de retorno aos acionistas para 2026 estimado entre 90 trilhões e 110 trilhões de wons (US$65,1 bilhões a US$79,5 bilhões).
- A empresa afirma ser o maior programa do tipo já feito por uma companhia coreana.
- O pacote é cerca de cinco vezes o recorde anual anterior da Samsung, de 20,3 trilhões de wons, estabelecido em 2020.
- A Samsung planeja distribuir cerca de 30 trilhões de wons em dividendos em dinheiro, incluindo os pagamentos regulares do terceiro trimestre de 2026.
- O conselho também aprovou uma recompra de cerca de 15 trilhões de wons em ações próprias para remuneração de funcionários.
- O tamanho e os detalhes do restante do retorno serão decididos em reunião do conselho no fim de janeiro de 2027, quando os resultados de 2026 estiverem fechados.
- O plano cumpre o compromisso da Samsung de devolver 50% do fluxo de caixa livre gerado entre 2024 e 2026.
- O anúncio veio dias depois de a SK hynix revelar um plano de recompra e cancelamento de ações de 40 trilhões de wons.
- O programa da SK hynix, anunciado na quarta-feira, foi o maior retorno a acionistas já anunciado por uma empresa listada sul-coreana.
- Os anúncios ocorrem em meio a um superciclo de chips de memória puxado pela IA.
**Fontes:**
- [S33] Samsung Global Newsroom — https://news.samsung.com/global/samsung-electronics-to-implement-largest-ever-shareholder-return-in-2026-estimated-at-krw-90-to-110-trillion
- [S34] CNBC — https://www.cnbc.com/2026/08/21/samsung-shareholder-return-package-sk-hynix-buyback-ai-chip-boom.html
- [S35] The Korea Times — https://www.koreatimes.co.kr/business/tech-science/20260821/samsung-electronics-plans-record-shareholder-return-of-up-to-796-bil
- [S36] Reuters — https://www.reuters.com/world/asia-pacific/samsung-electroncis-announce-more-than-72-billion-shareholder-return-programme-2026-08-20/

## YMTC — caminho aberto para um IPO de US$4,9 bilhões em Xangai
- Documentos divulgados na sexta-feira mostraram que o pedido de listagem da Yangtze Memory Technologies (YMTC) em Xangai foi aceito pela bolsa da cidade.
- O plano prevê uma venda de ações de 33 bilhões de yuans (US$4,91 bilhões) no STAR Market, o segmento de tecnologia da bolsa de Xangai nos moldes da Nasdaq.
- A operação ficaria entre as maiores já feitas naquele mercado, segundo a bolsa.
- A YMTC concluiu seu processo de tutoria pré-IPO em 20 de agosto.
- A empresa é assessorada pela CITIC Securities e pela China Securities, e havia protocolado seu relatório de tutoria em maio.
- A fabricante de memória flash tem apoio estatal.
- O valuation da empresa pode chegar a pelo menos 1 trilhão de yuans (US$148 bilhões).
- As expectativas de valuation foram impulsionadas pela escassez global de chips de memória puxada pela IA e por estreias recordes recentes de outras empresas de tecnologia chinesas.
**Fontes:**
- [S37] CNA (Reuters) — https://www.channelnewsasia.com/business/chinese-flash-memory-chipmaker-ymtc-plans-raise-49-billion-in-shanghai-ipo-6333456
- [S38] Caixin Global — https://www.caixinglobal.com/2026-08-20/ymtc-moves-closer-to-shanghai-ipo-102476082.html
- [S39] China Daily — https://www.chinadaily.com.cn/a/202608/20/WS6a865479a3106bc57421c74c.html

## Nvidia — desmentido sobre chip LPU feito para a China
- O The Information noticiou na quinta-feira, citando dois funcionários da Nvidia, que a empresa planejava iniciar remessas em pequenos lotes de um chip de IA projetado para clientes chineses até o fim de 2026.
- Segundo a reportagem, vários clientes já teriam feito pedidos.
- A Nvidia rejeitou publicamente a reportagem no mesmo dia: "Não temos vendas de LPU no mercado chinês hoje, e não há nenhum produto LPU específico para a China em nosso roadmap".
- O chip descrito é uma versão da LPU (Language Processing Unit) da Nvidia, desenvolvida com tecnologia licenciada da startup Groq.
- A LPU trabalha ao lado de GPUs para acelerar as respostas de chatbots de IA e estaria em conformidade com os controles de exportação dos EUA.
- Engenheiros teriam modificado o software da LPU para que ela funcione com processadores disponíveis na China.
- A adaptação seria necessária porque a arquitetura de próxima geração Vera Rubin não pode ser exportada para lá sob as regras americanas.
- A reportagem também afirmou que a Nvidia está ampliando as remessas de seus processadores H200, já liberados.
- A parceira de encapsulamento Amkor Technology teria finalizado mais de 1 milhão de unidades no segundo trimestre.
- Washington aprovou em maio a venda dos chips H200 a um grupo limitado de empresas chinesas, incluindo Alibaba, Tencent e ByteDance.
- As entregas desses chips começaram só recentemente.
**Fontes:**
- [S40] Reuters via WTVB — https://wtvbam.com/2026/08/20/nvidia-to-ship-ai-chip-for-china-by-year-end-the-information-reports/
- [S41] The Standard — https://www.thestandard.com.hk/innovation/article/340570/Nvidia-denies-report-of-China-specific-LPU-shipments-by-year-end
- [S42] Investing.com via Yahoo Finance — https://finance.yahoo.com/technology/ai/articles/nvidia-plans-china-ai-return-175431102.html
- [S43] Tradevae — https://www.tradevae.com/news/stock-markets/nvidia-to-send-modified-ai-chip-to-china-as-export-limits-keep-next-gen-design-out/
- [S44] Newsquawk — https://www.newsquawk.com/headlines/nvidia-nvda-intends-to-begin-small-batch-shipments-of-a-china-tailored-lpu-by-the-end-of-2026-reports-the-information-citing-sources

## Supermicro — investigação interna não acha indício de que a cúpula sabia do contrabando
- A Super Micro Computer informou na quinta-feira que uma investigação independente conduzida por seu conselho não encontrou evidências de que membros atuais da alta administração soubessem do suposto esquema.
- O esquema alegado envolvia contrabandear para a China US$2,5 bilhões em equipamentos com chips da Nvidia.
- A apuração foi liderada pelo diretor independente principal Scott Angel, ex-sócio de auditoria da Deloitte, e pela presidente do comitê de auditoria, Tally Liu.
- Eles contrataram o escritório Munger, Tolles & Olson como advogados externos e a AlixPartners como consultoria de perícia contábil.
- A investigação também não encontrou evidências de que a empresa tenha vendido produtos sob controle de exportação a companhias ou pessoas banidas.
- Não foram encontradas evidências de que as demonstrações financeiras anteriores fossem não confiáveis.
- A apuração seguiu a acusação formal, feita pelo Departamento de Justiça dos EUA em março, contra o cofundador Yih-Shyan "Wally" Liaw, o gerente de vendas Ruei-Tsang Chang e o prestador de serviços Ting-Wei Sun.
- Eles são acusados de rotear servidores fabricados nos EUA por Taiwan e pelo Sudeste Asiático até a China.
- A própria Supermicro não foi indicada como ré no caso, e havia afastado Liaw e Chang.
- Ainda restam pontos em aberto: quatro funcionários da Supermicro foram detidos para interrogatório em Taiwan no mês passado.
- Em junho, a empresa recebeu uma intimação de um grande júri federal em Nova York.
**Fontes:**
- [S45] Fortune — https://fortune.com/2026/08/20/supermicro-investigation-ceo-nvidia-smuggling/
- [S46] MSNBC TV News (Fortune syndication) — https://msnbctv.news/supermicro-investigation-clears-ceo-in-2-5-billion-alleged-smuggling-scheme/
- [S47] Reuters — https://www.reuters.com/legal/government/super-micro-begins-independent-probe-after-criminal-case-against-cofounder-2026-04-07/

## Estados Unidos e Irã — Bessent promete "derrubar o regime" e sanciona rede do Hezbollah
- O secretário do Tesouro dos EUA, Scott Bessent, disse na quinta-feira que Washington vai "derrubar este regime" em Teerã por meio de isolamento econômico coordenado.
- Os EUA alertaram aliados e a China a aderirem à nova campanha de Donald Trump para isolar a economia iraniana.
- As declarações marcam o retorno de um alto funcionário americano à linguagem de mudança de regime, depois de meses em que Trump enquadrou a guerra como sendo sobre o programa nuclear iraniano.
- Perguntado se os EUA pressionariam a China, Bessent disse à CNBC que "muitas conversas são melhores em privado", mas pediu que Pequim "entre no programa".
- Bessent disse que daria mais detalhes das medidas em entrevista coletiva na segunda-feira.
- Segundo ele, a pressão econômica máxima torna menos provável um retorno a operações militares pesadas: "Se estamos fazendo a máxima pressão econômica, isso significa que provavelmente não haverá um reinício cinético em larga escala, mas eu enfatizo que isso é por ora".
- O Tesouro dos EUA voltou a designar o Hezbollah como Specially Designated Global Terrorist (organização terrorista global sob designação especial) na quinta-feira.
- Dez pessoas foram sancionadas por operar uma rede de correios que movimentava até centenas de milhões de dólares em dinheiro vivo.
- Segundo o Tesouro, a rede usa correios em voos comerciais entre Líbano, Turquia, Emirados Árabes Unidos e Irã.
- O Ministério das Relações Exteriores do Irã classificou as medidas ameaçadas como "terrorismo econômico" e "crimes contra a humanidade".
- O chanceler Abbas Araghchi chamou o "Dia D Econômico" de distração para a dívida americana e os custos crescentes de juros.
- Um novo grupo de ataque de porta-aviões dos EUA, liderado pelo USS George Washington, chegou ao Oriente Médio na quarta-feira.
- A guerra se aproxima da marca de seis meses.
**Fontes:**
- [S48] France 24 / AFP — https://www.france24.com/en/live-news/20260820-trump-pledges-economic-warfare-on-iran-prompting-tehran-derision
- [S49] Al Jazeera — https://www.aljazeera.com/news/liveblog/2026/8/20/iran-war-live-trump-announces-most-crushing-iran-sanctions
- [S50] Al Jazeera — https://www.aljazeera.com/news/2026/8/20/how-china-and-russia-could-hobble-trumps-plans-to-isolate-iran

## Tesouro dos EUA — o resgate dos títulos se desfaz em um dia
- O rendimento do Treasury de 10 anos subiu a até 4,71% na quinta-feira, o maior nível desde terça.
- O rendimento de 30 anos disparou a até 5,267%, acima do patamar em que estava quando o Tesouro agiu na quarta-feira.
- O movimento apagou as quedas que se seguiram à expansão surpresa do programa de recompra de títulos anunciada pelo Tesouro um dia antes.
- Os juros voltaram a subir depois que Bessent apareceu na CNBC e sinalizou mais recompras de títulos.
- Bessent disse: "Vamos anunciar — provavelmente no fim desta semana, início da próxima — um foco maior em consolidação fiscal".
- As ações americanas caíram com a alta dos juros: o S&P 500 fechou em baixa de 0,8%.
- O Nasdaq Composite caiu 1% e o Dow Jones recuou 700 pontos, ou 1,3%.
- O petróleo americano chegou a tocar US$89 por barril e fechou a US$87,83, alta de 2,3% no dia.
- O Brent, referência internacional, subiu mais de 2% e fechou a US$93,78.
- O preço médio nacional da gasolina nos EUA subiu mais 2 centavos ante quarta-feira, a US$4,10 por galão.
- O Tesouro revelou na tarde de quarta-feira que a dívida nacional americana em aberto superou US$40 trilhões pela primeira vez.
- Os pagamentos de juros da dívida estão a caminho de superar o Medicare como a maior linha de despesa isolada do governo.
- Analistas da Evercore ISI alertaram que "o aumento do ativismo do Tesouro — se sustentado — também pode tornar o dólar menos atraente".
- O índice do dólar caiu quase 1% desde a manhã de quarta-feira.
- Investidores leram a reversão da alta de quarta-feira como sinal de que o plano de recompras é apenas um remédio de curta duração para os custos de captação.
- As bolsas globais recuaram enquanto o petróleo superava os US$90.
**Fontes:**
- [S51] NBC News — https://www.nbcnews.com/business/markets/bond-yields-stocks-oil-prices-rcna593517
- [S52] The Irish Times — https://www.irishtimes.com/business/2026/08/20/global-stocks-retreat-as-oil-tops-90-and-us-yields-climb/

## Estados Unidos e Catar — venda de US$4,5 bilhões em aviões-tanque KC-46 da Boeing
- O Departamento de Estado dos EUA aprovou na quinta-feira uma possível Venda Militar Estrangeira ao Catar de US$4,5 bilhões.
- A operação cobre aeronaves de reabastecimento aéreo e equipamentos relacionados.
- O governo do Catar pediu até quatro KC-46A e oito motores turbofan PW4062.
- O pedido inclui ainda 10 receptores de alerta de radar AN/ALR-69A.
- Também constam 15 Guardian Laser Transmitter Assemblies, usados em sistemas de contramedidas infravermelhas para grandes aeronaves (LAIRCM), e oito processadores de reposição de sistemas LAIRCM.
- Os principais contratados seriam Boeing, Pratt & Whitney Military Engines, RTX Corporation e Northrop Grumman Corporation.
- Segundo os EUA, a venda amplia a capacidade do Catar de enfrentar ameaças atuais e futuras e reforça seu "papel estratégico na segurança regional".
- A notificação ao Congresso apenas autoriza a venda; o Catar não confirmou planos de assinar um pedido.
- A aprovação veio no mesmo dia em que Washington pressionou aliados a aderir à campanha econômica contra o Irã.
- O Catar tem atuado como mediador na guerra entre Estados Unidos e Irã.
**Fontes:**
- [S53] Defense News — https://www.defensenews.com/global/mideast-africa/2026/08/20/us-approves-possible-45-billion-sale-of-kc-46as-equipment-to-qatar/
- [S54] Aviation Week — https://aviationweek.com/defense/aircraft-propulsion/us-clears-kc-46-offer-qatar
- [S55] France 24 / AFP — https://www.france24.com/en/live-news/20260820-trump-pledges-economic-warfare-on-iran-prompting-tehran-derision

## Charter — fusão de US$34,5 bilhões com a Cox é concluída
- A Charter Communications (NASDAQ: CHTR) anunciou na quinta-feira que concluiu a transação com a Cox Communications e a aquisição da Liberty Broadband.
- As operações haviam sido anunciadas em maio de 2025.
- A Cox Enterprises recebeu cerca de 33,6 milhões de units ordinárias da parceria já existente da Charter, com valor implícito de aproximadamente US$5 bilhões.
- A Cox Enterprises recebeu também US$6 bilhões em units preferenciais conversíveis da Charter Holdings, com cupom de 6,875%.
- O pagamento incluiu ainda cerca de US$4 bilhões em dinheiro.
- Com isso, a Cox Enterprises e suas subsidiárias detêm cerca de 26% das ações da companhia combinada em base totalmente diluída.
- A empresa combinada atenderá 37 milhões de clientes em 45 estados americanos.
- A Charter já era a maior provedora de TV a cabo do país, com 31 milhões de clientes, e soma os 6 milhões de assinantes da Cox.
- O negócio é avaliado em cerca de US$34,5 bilhões.
- Em até um ano, a controladora passará a se chamar Cox Communications, mas continuará operando sob a marca Spectrum em todos os mercados.
- A companhia seguirá sediada em Stamford, Connecticut.
- Chris Winfrey continua como CEO.
- O último obstáculo regulatório caiu uma semana antes, quando a Comissão de Serviços Públicos da Califórnia aprovou o negócio.
- A FCC (agência reguladora de telecomunicações dos EUA) liberou a fusão em fevereiro.
- A liberação veio depois de a Charter garantir que traria de volta aos EUA todos os empregos terceirizados no exterior da Cox em até 18 meses.
- A Charter também se comprometeu a pagar um salário mínimo de US$20 por hora e a encerrar iniciativas de DEI (diversidade, equidade e inclusão).
**Fontes:**
- [S56] Charter Communications — https://corporate.charter.com/newsroom/charter-and-cox-communications-complete-transaction
- [S57] Forbes via Yahoo Finance — https://uk.finance.yahoo.com/news/charter-communications-closes-34-5-153752586.html
- [S58] The Hollywood Reporter — https://www.hollywoodreporter.com/business/business-news/charter-communications-completes-cox-liberty-broadband-deal-1236677613/

## El Niño — governos se preparam para impactos históricos
- O Sri Lanka organizou a entrega de água para quase 72 mil pessoas em sete distritos, disse um alto funcionário na quinta-feira.
- O país enfrenta uma seca ligada ao forte El Niño deste ano.
- O nível da água em centenas de pequenos reservatórios do país caiu para cerca de 10%.
- As famílias devem receber cerca de 75 litros de água a cada dois ou três dias.
- O governo destinou 4,8 bilhões de rupias (US$14 milhões) do orçamento para a distribuição de água.
- O ministro do Meio Ambiente, Dammika Patabendi, disse que o governo esperava o pico do El Niño por volta de novembro, mas agora acredita que ele virá antes.
- Na Indonésia, o governo diz que incêndios florestais queimaram mais de 200 mil hectares desde o início do ano.
- A área é cerca de três vezes o tamanho de Jacarta, a capital do país.
- Só em julho, os incêndios destruíram 95 mil hectares.
- Equipes de semeadura de nuvens estão de prontidão na Indonésia.
- Honduras colocou 80% do país, incluindo a capital, em alerta de seca.
- Os EUA afirmam que enviarão um hospital militar à costa do Peru no ano que vem para ajudar o país a lidar com os efeitos do El Niño.
- Na Colômbia, o operador da rede elétrica XM estimou em 95% a probabilidade de um El Niño "muito forte" entre outubro e dezembro.
- O ministério de minas e energia colombiano disse que planeja um leilão de energia firme para reforçar a oferta.
- O ministério vem conversando com o regulador de energia e gás CREG para lançar a chamada.
**Fontes:**
- [S59] Al Jazeera — https://www.aljazeera.com/news/2026/8/20/governments-brace-for-historic-el-nino-impacts-on-global-weather-extremes
- [S60] BNamericas — https://www.bnamericas.com/en/news/colombia-plans-firm-energy-auction-to-mitigate-el-nino-impact

## Arctos e Atlanta Falcons — 10% do time a um valuation de US$10,6 bilhões
- A firma de private equity Arctos concordou em comprar 10% do Atlanta Falcons, segundo duas pessoas a par do assunto.
- O negócio tem valor de empresa de US$10,6 bilhões.
- A Arctos comprará a participação em duas tranches ao longo dos próximos 18 meses.
- Espera-se que a NFL vote sobre o negócio em outubro.
- Seria o quarto investimento da Arctos em uma franquia da NFL.
- Os outros times são Los Angeles Chargers, Buffalo Bills e Cleveland Browns.
- O dono Arthur Blank, cofundador da Home Depot, detém pouco menos de 73% do time.
- Blank comprou a franquia em 2002 por US$545 milhões, o que implica uma valorização de cerca de 19 vezes.
- Na temporada 2025, os Falcons ficaram fora dos playoffs pelo oitavo ano consecutivo.
**Fontes:**
- [S61] CNBC — https://www.cnbc.com/2026/08/20/arctos-agrees-to-buy-10percent-of-atlanta-falcons-at-10point6-billion-valuation-sources.html
