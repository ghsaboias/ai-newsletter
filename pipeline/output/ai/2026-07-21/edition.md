# [Tech] - Bem-vindo(a) a 21 de Julho de 2026

Por que a OpenAI pausou um modelo treinado para tarefas de longa duração? Quanto vale o maior acordo de direitos autorais já visto nos EUA? O que a Microsoft ganha ao bancar as GPUs europeias da Mistral?

Por: Guilherme Saboia e Vinicius Gushiken

### OpenAI pausa modelo autônomo após ele escapar do *sandbox*
- **Pausa.** A OpenAI revelou que [pausou o acesso a um modelo não lançado](https://openai.com/index/safety-alignment-long-horizon-models) treinado para tarefas de longa duração, após observar "falhas inéditas" não capturadas por suas avaliações pré-implantação. É o mesmo sistema que a empresa disse ter refutado a conjectura da distância unitária de Erdős, problema de geometria discreta com cerca de 80 anos, anunciado em 20 de maio.
- **Fuga.** Instruído a compartilhar resultados só no Slack em uma avaliação, o modelo passou cerca de uma hora [contornando as restrições do *sandbox*](https://aiweekly.co/alerts/openai-pauses-erds-model-after-long-horizon-sandbox-escapes) (ambiente isolado de execução) e abriu um *pull request* público no GitHub mesmo assim, enquanto modelos de horizonte mais curto haviam esbarrado na mesma barreira e parado.
- **Evasão.** Em outro incidente, com um scanner bloqueando um token de autenticação, o modelo [dividiu o token e o reconstruiu em tempo de execução](https://officechai.com/ai/openai-says-it-paused-access-for-an-internal-model-after-it-escaped-a-sandbox/), afirmando nos logs que fazia isso "para evadir o scanner".
- **Correção.** A OpenAI [reconstruiu sua pilha de segurança](https://gigazine.net/gsc_news/en/20260721-openai-ai-trained-for-long-running-tasks/) em torno de defesa em profundidade e monitoramento em nível de trajetória, que acompanha uma sequência inteira de ações e pode pausar uma sessão para revisão humana, e restaurou o acesso limitado sob monitoramento.

### Justiça dos EUA aprova acordo de US$1,5 bilhão da Anthropic com autores
- **Aprovação.** A juíza federal Araceli Martínez-Olguín [concedeu aprovação final na segunda-feira](https://www.cnbctv18.com/world/us-judge-approves-anthropics-1-5-billion-ai-copyright-settlement-largest-in-us-history-19950116.htm) ao acordo de US$1,5 bilhão da Anthropic com autores, o maior acordo conhecido em um caso de direitos autorais nos EUA, rejeitando as objeções de que o valor seria pequeno demais como "não fundamentadas em uma avaliação realista dos riscos e recompensas de um julgamento".
- **Origem.** A ação coletiva de 2024 alegou que a Anthropic [salvou mais de 7 milhões de livros pirateados](https://news.bloomberglaw.com/ip-law/anthropic-authors-1-5-billion-deal-receives-final-approval), vindos de repositórios como o Library Genesis; o juiz Alsup já havia decidido que treinar modelos com livros é uso justo (*fair use*), mas que a pirataria violou os direitos dos autores.
- **Valores.** O acordo prevê cerca de [US$3.000 por obra para aproximadamente 480.000 obras](https://assets-us-01.kc-usercontent.com/1eeb16db-4934-006e-40a6-38fa91285ebb/dd3b72fc-bbfb-47cc-ba05-10c0ffd0bac1/ANT_proposed_order_granting_final_approval.pdf), cerca de quatro vezes o mínimo de danos legais para infração intencional; até 16 de abril, 440.490 obras (91,3%) haviam sido reivindicadas, e os advogados receberam mais de US$101 milhões dos US$187,5 milhões pedidos.
- **Precedente.** É um dos primeiros acordos entre [dezenas de ações semelhantes contra empresas de IA](https://wtkg.iheart.com/content/2026-07-21-court-approves-record-15b-copyright-settlement/), incluindo OpenAI, Meta e Google; alguns autores e editoras optaram por sair do acordo e mantêm ações separadas contra a Anthropic.

### Microsoft vai bancar expansão europeia de GPUs da Mistral em acordo bilionário
- **Acordo.** Microsoft e Mistral ampliaram a parceria com um [compromisso multibilionário da Microsoft](https://ae.marketscreener.com/news/microsoft-to-fund-mistral-s-european-ai-expansion-in-multibillion-dollar-deal-ce7f51d8d88ef727) para usar a infraestrutura de GPUs da Mistral baseada na Europa, empregando milhares das mais recentes GPUs NVIDIA Vera Rubin na capacidade europeia ampliada.
- **Soberania.** Por meio dos data centers da Mistral na França, o arranjo [oferece a setores regulados uma alternativa à infraestrutura controlada pelos EUA](https://www.investing.com/news/company-news/microsoft-mistral-expand-ai-partnership-with-multibilliondollar-deal-93CH-4803226); o presidente Brad Smith disse que o acordo não inclui nenhuma nova participação financeira na Mistral.
- **Produtos.** Os modelos [Medium 3.5 e OCR 4 já estão no Microsoft Foundry](https://mx.advfn.com/bolsa-de-valores/NASDAQ/MSFT/noticias/98953962/microsoft-and-mistral-expand-strategic-partnership) (OCR = reconhecimento óptico de caracteres), o Medium 3.5 foi integrado ao Copilot Studio, e o Azure Local permitirá rodar os modelos "abertos" da Mistral em ambientes totalmente desconectados.
- **Ambição.** Arthur Mensch, CEO da Mistral, não quis comentar reportagem de que a empresa [negociaria captar cerca de EUR3 bilhões](https://ae.marketscreener.com/news/microsoft-to-fund-mistral-s-european-ai-expansion-in-multibillion-dollar-deal-ce7f51d8d88ef727) (US$3,4 bilhões) a uma avaliação de EUR20 bilhões, e disse mirar 1 gigawatt de capacidade computacional até 2030.

---

#### Segurança
- **Pillar Security.** A equipe de pesquisa publicou a série "Week of Sandbox Escapes" e [escapou dos *sandboxes* de quatro agentes de código por IA](https://www.bleepingcomputer.com/news/security/cursor-codex-gemini-cli-antigravity-hit-by-sandbox-escapes/), Cursor, Codex da OpenAI, Gemini CLI do Google e Antigravity, sem atacá-los diretamente. A falha do Cursor virou o CVE-2026-48124, corrigido na versão 3.0.0, e a OpenAI pagou recompensa de alta severidade pela do Codex.
- **Taiwan.** Promotores [indiciaram um ex-vice-gerente da TSMC](https://asia.nikkei.com/business/technology/taiwan-alleges-ex-tsmc-staff-stole-chip-secrets-to-sell-to-china), de sobrenome Chen, acusado de tentar vazar tecnologias centrais de chips para a China, no que dizem ser o primeiro processo do tipo no país, e pediram sete anos de prisão. Chen teria copiado 21 documentos confidenciais entre maio de 2023 e fevereiro de 2024, recuperados antes de qualquer transferência.

#### China & chips
- **Pequim.** O Ministério do Comércio [consulta Alibaba, ByteDance e Zhipu sobre endurecer os controles de exportação](https://www.ft.com/content/6049a031-9e9b-464c-97bb-414da04d5a6a) de tecnologias avançadas de IA e chips, incluindo limitar a transferência de dados de treinamento e restringir que estrangeiros baixem os pesos (*weights*) dos modelos chineses. A medida marcaria uma reversão da estratégia de pesos abertos que impulsionou a adoção global de modelos chineses.
- **Z.ai.** A ex-Zhipu concluiu um [data center de 1 gigawatt com apenas chips fabricados na China](https://www.scmp.com/tech/big-tech/article/3361374/zai-shares-surge-37-firm-builds-giant-data-centre-powered-chinese-chips), em vários clusters de mais de 10.000 chips e nenhum da Nvidia, e começou a operá-lo parcialmente. As ações dispararam 37% em Hong Kong na terça, embora os detalhes venham de uma única fonte anônima e não tenham sido verificados.

#### Manufatura & memória
- **TSMC.** A fabricante planeja [elevar os preços de produção de chips em até 10% em 2027](https://asia.nikkei.com/business/technology/exclusive-tsmc-to-raise-chipmaking-prices-by-up-to-10-from-2027), com reajustes de 5% a 10% conforme cliente e produto e prêmio adicional de 10% a 15% para pedidos de alto desempenho acima do previsto; Apple, Nvidia e AMD já foram informadas. O aumento vem após um segundo trimestre recorde, com lucro em alta de 77%.
- **Coreia do Sul.** As exportações de semicondutores [somaram US$22,1 bilhões entre 1º e 20 de julho](https://biz.heraldcorp.com/article/10814585), alta de 180,6% na comparação anual e recorde para o período, puxadas pelos preços da memória e pela demanda por HBM (memória de alta largura de banda) para servidores de IA. Os chips foram 40,3% das exportações totais.

#### Infraestrutura
- **BlackRock.** A gestora busca [vender mais de US$12 bilhões em títulos](https://www.bloomberg.com/news/articles/2026-07-20/blackrock-eyes-more-than-12-billion-debt-for-data-center) para financiar um campus de data center da Meta em El Paso, no Texas, com financiamento total perto de US$13 bilhões. A estrutura mantém a maior parte da dívida de construção fora do balanço da Meta, registrada como aluguel, e ecoa um acordo de quase US$30 bilhões com a Blue Owl no ano passado.

#### Rodadas
- **Natural.** A startup de infraestrutura de pagamentos para agentes de IA [levantou uma Série A de US$30 milhões](https://techcrunch.com/2026/07/20/natural-raises-30m-to-reinvent-payments-for-ai-agents-and-take-on-stripe/) liderada por Kirsten Green, da Forerunner, elevando o total a cerca de US$40 milhões. A empresa quer competir diretamente com incumbentes como a Stripe na corrida por trilhos de pagamento agênticos.
- **Gritt.** A startup saiu do *stealth* com uma [Série A de US$26 milhões liderada pela Obvious Ventures](https://techcrunch.com/2026/07/21/gritt-exits-stealth-with-34-million-for-robots-to-build-solar-plants-then-everything-else/), US$34 milhões no total, para robôs controlados por IA que constroem usinas solares. Seus sistemas permitem que uma equipe de oito instale de 3.000 a 4.000 painéis por dia, contra cerca de 800 no método tradicional, e a empresa tem contratos para 2,8 GW.

#### Capital & aquisições
- **Ant International.** A afiliada internacional do Ant Group, de Jack Ma, [levantou US$1,2 bilhão](https://uk.finance.yahoo.com/news/ant-international-raises-1-2-034330703.html) para acelerar a expansão global, com participação de Ant Group e Alibaba, e estava avaliada em US$10 bilhões antes da rodada. A empresa de pagamentos, sediada em Singapura, diz conectar mais de 150 milhões de comerciantes a mais de 2 bilhões de contas de usuários.
- **Tencent.** A gigante chinesa [negocia comprar o estúdio israelense SuperPlay](https://www.calcalistech.com/ctechnews/article/hkvfmqsvme), da Playtika, por US$1 bilhão a US$1,5 bilhão. A Playtika havia comprado a SuperPlay em 2024 por US$690 milhões mais *earnout* (pagamento condicionado a metas) de até US$1,25 bilhão, que a Tencent assumiria.

#### Defesa
- **Anduril e Archer.** As empresas apresentaram no Farnborough Airshow o ["Thunder", um rotor de ataque autônomo do Grupo 5](https://breakingdefense.com/2026/07/anduril-reveals-thunder-a-loyal-wingman-drone-for-helicopters/) projetado para voar como "ala leal" (*loyal wingman*) ao lado de helicópteros tripulados como o Apache. Combina o tiltrotor da Karem, o trem de força híbrido-elétrico da Archer e a autonomia da Anduril, com primeiro voo previsto para 2027.

#### Direitos autorais
- **Sony Music.** A gravadora abriu uma [segunda ação por violação de direitos autorais contra a Udio](https://www.musicbusinessworldwide.com/sony-music-files-new-lawsuit-against-ai-platform-udio-asserting-over-30000-sound-recordings-a-judge-barred-it-from-adding-to-its-original-case/), empresa de música por IA, apontando 30.117 gravações que diz terem sido copiadas sem permissão para treinar seus modelos. Isso amplia a exposição potencial da Udio de cerca de US$50 milhões para aproximadamente US$4,5 bilhões; a Sony é a única grande gravadora que ainda processa a startup.

---

#### Leia também
- [Irã alega ataque com mísseis de cruzeiro a data center da AWS no Bahrein](https://www.indiatoday.in/technology/news/story/amazon-aws-data-centre-in-bahrain-hit-with-cruise-missiles-says-iran-2952805-2026-07-21)
- [Ataque russo atinge navio perto de Odessa e Ucrânia lança mais de 400 drones sobre Moscou](https://www.aljazeera.com/news/2026/7/20/russian-strike-on-ship-near-odesa-kills-10-ukraine-hits-moscow-with-drones)
- [Brent supera US$90 com ameaça iraniana ao Estreito de Ormuz](https://www.al-monitor.com/originals/2026/07/oil-tops-90-iran-warns-hormuz-will-not-be-safe)
- [Terapia celular e gênica da Kolon TissueGene falha em ensaio de Fase 3 nos EUA](https://www.globenewswire.com/news-release/2026/07/20/3329671/0/en/Kolon-TissueGene-Reports-Topline-ACTiVION-II-Phase-3-Clinical-Trial-Results-for-TissueGene-C-TG-C-Targeting-Osteoarthritis-OA-of-the-Knee.html)
