---
title: Guia de antenas
lead: A antena certa, bem montada, chega mais longe do que mais potência. Verifica a antena do teu companion e depois escolhe, liga e monta uma para um repetidor.
description: 'Escolhe e monta uma antena MeshCore para 868 MHz: verificar a antena de chicote de um companion, tipos de antena e ganho, conectores, perda do cabo por metro, filtros, montagem e como o ganho conta para o limite legal.'
eyebrow: Companion e repetidor · 868 MHz
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'f828c4aa'
  seeded: '2026-10-31'
  fields: {title: '3a76cb0e', lead: 'd82ec429', description: 'ce3f3e73', eyebrow: 'd2203a35'}
  sections: ['908e2678', 'f9b96f42', 'ca18da90', 'bcfb40ec', '851afd23', '8b7a2209', 'd8832cfa', '5b70b9e8', '14a38e92', 'a5dc1e34', 'de04ca41', 'a23f19c6', '93846db4']
  blocks: ['908e2678', '0868bca9', '081db416', 'ad1da217', '73844333', 'aa14f1b1', '07e4fbad', '32d64d0d', 'ef66133c', '558c115b', '5d28e314', '57d6e138', 'e9b3d055', 'dd757d4a', '2cbd0b58', '21c67ec0', '306a3ded', 'fa46c89f', '1e6ccb3a', 'a3e53320', '6ae131c0', '98f350c6', '138d049d', '3bd28746', '2fc98ff1', '5ea29ee5', 'cfbd64e1', '48833347', '56a82a5c', '4ef7e883', '711e4fee', '1f7844ed', '6b188411', '8da9aa78', '4c2d8bbc', 'a721a9d0', '69c1dc1a', 'a631dbfa', '3f9f3471', '5af4ae3b', 'fa5095fd', '65eeb436', '15aa0eca', 'a8f5b505', '57f35115', '8e5e4975', '89764d3d']
---

A altura, uma antena afinada e um cabo curto dão mais alcance do que
qualquer miliwatt extra. Este guia começa pelo companion, o rádio a partir
do qual envias mensagens. Depois trata da antena de um repetidor, um nó
que reencaminha mensagens a partir de um telhado ou mastro.

## O teu companion {#companion}

{{< callout type="warning" >}}
Coloca a antena antes de ligares o rádio. Um rádio LoRa que
transmite sem antena pode danificar o seu próprio chip.
{{< /callout >}}

A antena que veio com a tua placa serve. Coloca-a, segura o
nó na vertical e começa a enviar mensagens. Uma antena melhor
num companion traz pouco; um repetidor ao teu alcance traz muito.

Compra uma antena whip à parte só quando a fornecida estiver partida ou em falta.
Nem todas as whip vendidas para 868 MHz estão afinadas para essa frequência.
[Verifica-a com um NanoVNA](#nanovna), um analisador de antenas de bolso, antes
de confiares nela, ou pede emprestada a de uma placa que funcione.

Um nó junto a um transmissor forte ouve menos do que devia. Um pequeno
[filtro SAW (surface acoustic wave)](#filters) entre o rádio e a
antena mantém esse transmissor fora do recetor. Consulta primeiro a
ficha técnica do filtro:

- **Potência máxima de entrada.** O filtro também fica no caminho da tua própria
  transmissão. Uma placa que transmite 22 dBm (160 mW) num filtro de 15 dBm
  danifica o filtro.
- **Banda passante.** Tem de incluir a frequência do teu preset. Um filtro para
  868.65 a 869.25 MHz não deixa passar o canal EU/UK (Narrow) em
  869.618 MHz.

## Tipos de antena para um repetidor {#types}

Todas as antenas da mesh ficam na vertical. Escolhe o tipo conforme o
sítio onde estão os nós que queres alcançar:

- **Colinear de fibra de vidro.** Um tubo branco num mastro, com ganho em
  todo o horizonte. É a escolha habitual para um repetidor que serve uma
  localidade.
- **Dipolo.** Mais curto, com menos ganho e um feixe alto. Alcança melhor
  do que um colinear os nós abaixo e acima de ti, por exemplo a partir de
  um monte sobre um vale.
- **Yagi.** Uma haste com elementos transversais, apontada para um sítio.
  Alcança um único repetidor distante e pouco mais. Monta-a com os
  elementos na vertical, porque a polarização segue os elementos.

## O ganho e o feixe {#gain}

O ganho não acrescenta potência. Pega no sinal que iria para cima e para baixo
e envia-o ao longo do horizonte. É como uma lanterna que focas: a mesma pilha,
um feixe mais longo e mais estreito. Um dipolo e um colinear do mesmo fabricante
mostram-no:

| Antena | Ganho | Abertura vertical do feixe |
|---|---|---|
| Dipolo (Sirio SO 868-915-2) | 2.2 dBi | 88 graus |
| Colinear de fibra de vidro (Sirio SPO 868-915-6) | 5.8 dBi | 23 graus |

{{< gain >}}

O diagrama é um corte através do mastro, visto de lado. Roda-o à volta do
mastro e tens o feixe inteiro: um donut para o dipolo, um disco plano
para o colinear. Uma antena na vertical emite da mesma forma em todas as direções
à sua volta. Fora do feixe desenhado, o sinal não para; é mais fraco, mas ainda
chega para um nó próximo.

Num telhado, queres um feixe plano. Num monte muito acima dos nós,
um feixe de 23 graus passa por cima deles; um dipolo cobre-os. Uma Yagi
leva isto mais longe: 16.6 dBi num feixe com 23 graus de altura
e 25 graus de largura (Amphenol Procom
7176870), e nada para os lados.

O ganho mede-se em relação a uma referência. O dBi compara com uma antena ideal que
emite por igual em todas as direções. O dBd compara com um dipolo de meia onda,
que tem por si só 2.15 dBi: nem a antena mais simples emite alguma coisa a direito
para cima ou para baixo. Um dipolo mais comprido, de 1.25 comprimentos de onda, chega a 5.2 dBi.
Um colinear, por sua vez, empilha elementos de meia onda uns sobre os outros: quanto mais empilha,
maior o ganho. Comprime o mesmo sinal em metade do espaço e ali fica
duas vezes mais forte: 3 dB. Num quarto, 4 vezes mais forte: 6 dB.
Os fabricantes indicam o ganho em dBi; o limite legal conta-se em dBd, consulta
[Dentro do limite legal](#legal).

### Que ganho para o teu local {#choose-gain}

- **Montes, vales ou uma cidade densa: cerca de 3 dBi.** O feixe alto alcança
  os nós acima e abaixo de ti, e contorna as encostas e os edifícios no caminho.
  Também funciona no sentido inverso: a partir de um vale, um feixe plano passa
  por baixo de um repetidor no monte acima. A RAKwireless RAKARG12 é uma destas:
  um tubo de fibra de vidro de 36 cm.
- **Subúrbios ou uma localidade com telhados baixos: 5 a 6 dBi.** O colinear
  de fibra de vidro habitual.
- **Terreno plano e aberto: 8 a 10 dBi.** O feixe mais plano chega mais longe
  ao longo do horizonte. Montado no alto, passa por cima dos nós próximos.

O ganho no nome é o melhor valor em toda a banda da antena.
A RAKARG12, vendida como 3 dBi, tem 2.8 dBi entre 865 e 870 MHz. Lê a tabela
de ganho na ficha técnica para a frequência do teu preset.

Acima de 7 dBi, uma placa de 22 dBm ultrapassa o limite legal, a menos que as
perdas do cabo e do filtro compensem a diferença. Baixa a potência de transmissão
para compensar.

Um ganho alto só ajuda quando sabes onde estão os nós: ao longo do horizonte
à volta de um repetidor, ou num repetidor distante, no caso de uma Yagi. Um
companion na tua mão aponta para todo o lado, por isso o ganho baixo com que
veio é o que lhe serve melhor.

## Porquê na vertical {#vertical}

As antenas ouvem-se melhor quando apontam na mesma direção. A perda
aumenta com o ângulo entre elas: 45 graus custam 3 dB, metade do teu
sinal. A 90 graus, uma antena deitada contra uma vertical, em teoria não
chega nada. A mesh está na vertical, por isso a tua antena também tem de estar. Isto
vale também para um companion numa secretária: se o deitares, todos os
nós à tua volta ouvem menos.

## Conectores {#connectors}

Encomenda a antena com o conector
que a tua placa tem. Cada adaptador é mais uma junção para vedar e mais sinal
perdido.

- **SMA.** Um conector roscado com cerca de 6 mm de largura. A ficha na maioria
  das placas tem um orifício no centro; a antena tem o pino. Um conector deste
  tipo perde cerca de 0.03 dB a 868 MHz.
- **RP-SMA.** O mesmo corpo e a mesma rosca do SMA, com o pino e o orifício
  trocados. Parece-se com o SMA e não encaixa nele. Verifica qual dos dois
  a tua placa tem antes de encomendares.
- **U.FL (IPEX).** Uma ficha minúscula de encaixe por pressão na própria placa.
  Um cabo pigtail curto liga-a a uma ficha SMA na caixa. Está especificada para
  30 ciclos de ligação, por isso liga-a uma vez e deixa-a ficar.
- **N.** O conector roscado grande das antenas de fibra de vidro e dos cabos grossos.
  Perde no máximo 0.05 dB. Um repetidor precisa de um
  adaptador ou pigtail de N para o SMA da placa.

## Perda no cabo {#cable}

O cabo consome sinal antes de este sair da antena, nos dois sentidos. 3 dB
são metade da tua potência. Os valores dos fabricantes por metro, de 868 a 900 MHz:

| Cabo | Perda por metro | Perda em 5 m |
|---|---|---|
| RG174 | 1.02 dB | 5.1 dB |
| RG316 | 0.78 dB | 3.9 dB |
| RG58 | 0.45 dB | 2.2 dB |
| H-155 | 0.27 dB | 1.4 dB |
| LMR-240 | 0.25 dB | 1.2 dB |
| Ecoflex 10 | 0.13 dB | 0.7 dB |
| LMR-400 | 0.13 dB | 0.6 dB |

3 metros de RG174, o pigtail fino que vem com muitas placas, perdem metade
da tua potência. Monta a placa junto à antena com um pigtail curto, ou
leva cabo grosso até ela. Soma também cada adaptador e filtro no caminho.

## Filtros {#filters}

Um filtro fica entre o rádio e a antena. Deixa passar a tua banda e
bloqueia o resto, para que um transmissor forte próximo não abafe o
recetor. Precisas de um quando um nó ouve menos do que devia perto de outros
transmissores. Um repetidor num mastro com estações base de telemóveis é um
desses nós. Um filtro consome sinal nos dois sentidos: conta a perda dele como
a de um cabo.

| | Filtro SAW | Filtro de cavidade |
|---|---|---|
| Tamanho | Poucos milímetros, numa pequena placa | Um bloco ou tubo de metal |
| Perda de um bom filtro | menos de 2 dB | menos de 1 dB |
| Potência máxima de entrada de um bom filtro | 500 mW | vários watts |

O sysmocom cf866.5-kt30, por exemplo, é um filtro de cavidade para 863 a
870 MHz que perde no máximo 1.0 dB e aguenta 30 W. Foi feito para interiores,
por isso põe-no numa caixa vedada num mastro.

Os filtros variam muito, por isso consulta a ficha técnica antes de comprares.
A potência de entrada nominal tem de ser superior à tua potência de transmissão,
e a banda passante tem de incluir a frequência do teu preset.

## Montagem {#mounting}

- **Acima da beira do telhado.** A antena precisa de vista desimpedida em
  todas as direções que serve. Mesmo poucos metros acima dos telhados à
  volta ajudam. Em [Escolher um local](/repeater-guide/#site), no guia do
  repetidor, vês como verificar a vista.
- **Longe de metal.** Caleiras, mastros, outras antenas e telhados de
  metal junto à antena alteram o diagrama e a afinação. Monta-a no topo
  do mastro, não ao lado.
- **Na vertical.** Usa um nível de bolha. Vê [Porquê na vertical](#vertical).
- **Laço de escorrimento.** Deixa o cabo descer abaixo do conector antes de
  subir ou entrar. Assim, a água pinga em vez de escorrer para a junta.
- **Veda todos os conectores exteriores.** Água num conector aumenta a
  perda e corrói o pino. Veda-o contra a chuva e verifica a vedação todos
  os anos.
- **Raios.** Uma antena num telhado é um alvo. Um descarregador de gás no
  cabo dispara com uma sobretensão e envia-a para a terra. Segue
  [Hardware](/repeater-guide/#hardware) no guia do repetidor e as regras
  locais para a ligação à terra.

## Dentro do limite legal {#legal}

{{< callout type="legal" verified="2026-10-22" >}}
Na Europa, o MeshCore usa a sub-banda 869.40-869.65 MHz, com no máximo
**500 mW** de potência aparente radiada (e.r.p.). O limite conta o que sai da antena:
o ganho da antena soma, as perdas do cabo e do filtro subtraem. O ganho em dBi conta
menos 2.15 dB, porque o limite se mede em relação a um dipolo.
{{< /callout >}}

Um colinear de 5.8 dBi numa placa de 22 dBm fica dentro do limite. A mesma
antena numa placa com amplificador ultrapassa-o, enquanto não baixares a potência de
transmissão. Em [Potência: e.r.p. e a tua antena](/repeater-guide/#erp), no
guia do repetidor, encontras a conta e 2 exemplos resolvidos.

## Verificar uma antena com um NanoVNA {#nanovna}

Um NanoVNA é um analisador vetorial de redes de bolso. Mostra em que
frequência uma antena está afinada, e assim sabes antes de a montares. O
NanoVNA-H mede até 1.5 GHz, o que cobre os 868 MHz.

1. Calibra-o para 800 a 950 MHz com as peças open, short e load
   do respetivo kit.
2. Liga a antena através do adaptador que vai usar no nó. Segura-a
   na vertical e afastada do teu corpo e da mesa.
3. Lê a curva de SWR (relação de onda estacionária): mostra quanto sinal
   a antena devolve. O mínimo tem de ficar na frequência do teu preset,
   869.618 MHz para EU/UK (Narrow). Um mínimo a centenas de MHz de distância
   significa que a antena foi feita para outra banda.

Um quarto de onda a 868 MHz mede 86 mm (o comprimento de onda é 345 mm).
O comprimento, por si só, não te diz a banda, porque os fabricantes dobram
e carregam as whip; o NanoVNA diz.

## Fontes {#sources}

- Perda no cabo: [Belden 8216 (RG174)](https://catalog.belden.com/techdata/en/8216_techdata.pdf),
  a ficha técnica Huber+Suhner RG316,
  [Belden 8240 (RG58)](https://catalog.belden.com/techdata/en/8240_techdata.pdf),
  [SSB H-155](https://www.ssb.de/media/h155ssb-en.pdf),
  as fichas técnicas Times Microwave LMR-240 e LMR-400,
  [SSB Ecoflex 10](https://www.rigpix.com/otherusefulinfo/coax/ecoflex10.pdf).
- Antenas: [Sirio SPO 868-915-6](https://rigpix.com/antennas/sirio_spo8689156_manual.pdf),
  a ficha técnica Sirio SO 868-915-2,
  [Amphenol Procom 7176870](https://amphenolprocom.com/products/base-station-antennas/2236-7176870),
  [RAKwireless RAKARG12](https://docs.rakwireless.com/product-categories/accessories/rakarg12/datasheet/).
- Ganho como sinal comprimido em menos espaço: [RF Cafe, introdução às antenas](https://www.rfcafe.com/references/electrical/ew-radar-handbook/antenna-introduction-basics.htm).
- Conectores: as fichas técnicas Rosenberger 32S102 (SMA) e 53S101 (N), o
  catálogo Hirose U.FL.
- Filtros: a página do produto sysmocom cf866.5-kt30,
  [descarregadores de gás Citel](https://citel.us/en/gas-tube-surge-arrestors-for-coaxial-line-protection).
- Perda por polarização: [Universidade de Toronto, efeitos de Friis](https://www.waves.utoronto.ca/prof/svhum/ece422/notes/12-friiseffects.pdf).
- Ganho do dipolo por comprimento: [Wikipedia, antena dipolo](https://en.wikipedia.org/wiki/Dipole_antenna).
- Comprimento de onda: velocidade da luz segundo o [NIST](https://physics.nist.gov/cgi-bin/cuu/Value?c).
- NanoVNA: [NanoVNA-H](https://github.com/hugen79/NanoVNA-H).
- Limite legal: [Recomendação CEPT ERC 70-03](https://docdb.cept.org/document/845),
  Anexo 1, banda h1.7; o [guia do repetidor](/repeater-guide/#legal) indica
  as restantes.
