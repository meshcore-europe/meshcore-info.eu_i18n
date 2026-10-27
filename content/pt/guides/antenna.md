---
title: Guia de antenas
lead: A antena é metade do teu nó. A antena certa, bem montada, chega mais longe do que mais potência. Verifica a antena do teu companion e depois escolhe, liga e monta uma para um repetidor.
description: 'Escolhe e monta uma antena MeshCore para 868 MHz: verificar a antena de um companion, tipos de antena e ganho, conectores, perda do cabo por metro, filtros, montagem e como o ganho conta para o limite legal.'
eyebrow: Companion e repetidor · 868 MHz
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '45010ad0'
  seeded: '2026-10-26'
  fields: {title: '3a76cb0e', lead: '98430ade', description: 'ce3f3e73', eyebrow: 'd2203a35'}
  sections: ['908e2678', 'f9b96f42', '94c5bae4', 'bcfb40ec', '851afd23', '8b7a2209', 'd8832cfa', '5b70b9e8', '14a38e92', 'a5dc1e34', 'de04ca41', 'a23f19c6', '93846db4']
---

A altura, uma antena bem sintonizada e um cabo curto dão mais alcance do que qualquer miliwatt extra. Este guia começa pelo companion, o rádio a partir do qual envias mensagens. Depois trata da antena de um repetidor, um nó que reencaminha mensagens a partir de um telhado ou de um mastro.

## O teu companion {#companion}

{{< callout type="warning" >}}
Liga a antena antes de ligares o rádio. Um rádio LoRa que
transmite sem antena pode danificar o seu próprio chip.
{{< /callout >}}

A antena que veio com a tua placa cumpre a função. Liga-a, segura o
nó na vertical e começa a enviar mensagens. Uma antena melhor
num companion ganha pouco; um repetidor ao alcance ganha muito.

Compra uma antena de haste à parte só quando a fornecida estiver partida ou em falta. Nem
todas as antenas de haste vendidas para 868 MHz estão sintonizadas para essa frequência. [Verifica-a com um
NanoVNA](#nanovna), um analisador de antenas de bolso, antes de confiares nela, ou pede uma emprestada de uma placa que
funciona.

Um nó junto a um transmissor forte ouve menos do que devia. Um pequeno
[filtro SAW (onda acústica de superfície)](#filters) entre o rádio e a
antena mantém esse transmissor fora do recetor. Consulta primeiro a sua
ficha técnica:

- **Potência máxima de entrada.** O filtro também fica no caminho da tua própria
  transmissão. Uma placa a transmitir 22 dBm (160 mW) para um filtro classificado para 15 dBm
  avaria o filtro.
- **Banda de passagem.** Tem de incluir a frequência do teu preset. Um filtro para
  868.65 a 869.25 MHz não deixa passar o canal EU/UK (Narrow) em
  869.618 MHz.

## Tipos de antena para um repetidor {#types}

Todas as antenas na mesh ficam na vertical. Escolhe o tipo conforme a localização dos nós que queres alcançar:

- **Colinear de fibra de vidro.** Um tubo branco num mastro, com ganho em todo o horizonte. A escolha habitual para um repetidor que serve uma cidade.
- **Dipolo.** Mais curto, com menos ganho e um feixe alto. Chega melhor do que uma colinear a nós abaixo e acima de ti. Isso importa numa colina acima de um vale.
- **Yagi.** Uma barra com elementos transversais, apontada a um só lugar. Chega a um único repetidor distante e pouco mais. Monta-a com os elementos na vertical, porque a sua polarização segue os elementos.

## Ganho e o feixe {#gain}

O ganho não acrescenta potência. Pega no sinal que iria para cima e para baixo
e envia-o ao longo do horizonte. Como uma lanterna que focas: a mesma pilha,
um feixe mais longo e mais estreito. Um dipolo e uma colinear do mesmo fabricante
mostram-no:

| Antena | Ganho | Largura de feixe vertical |
|---|---|---|
| Dipolo (Sirio SO 868-915-2) | 2.2 dBi | 88 graus |
| Colinear de fibra de vidro (Sirio SPO 868-915-6) | 5.8 dBi | 23 graus |

{{< gain >}}

O diagrama corta o mastro ao meio, visto de lado. Roda-o à volta do
mastro e tens o feixe inteiro: um donut para o dipolo, um disco plano
para a colinear. Uma antena na vertical envia da mesma forma em todas as direções à sua
volta. Fora do feixe desenhado o sinal não para; é mais fraco, ainda
suficiente para um nó próximo.

Num telhado, um feixe plano é o que queres. Numa colina bem acima dos nós,
um feixe de 23 graus passa por cima das suas cabeças; um dipolo cobre-os. Uma Yagi
leva isto mais longe: 16.6 dBi num feixe com 23 graus de altura
e 25 graus de largura (Amphenol Procom
7176870), e nada para os lados.

O ganho conta em relação a uma referência. dBi compara com uma antena ideal que
envia igualmente em todas as direções. dBd compara com um dipolo de meia onda,
que tem por si só 2.15 dBi: até a antena mais simples não envia nada diretamente
para cima ou para baixo. Um dipolo mais longo, de 1.25 comprimentos de onda, chega aos 5.2 dBi. Uma colinear
empilha, em vez disso, elementos de meia onda uns sobre os outros: quanto mais empilha, maior
o ganho. Concentra o mesmo sinal em metade do espaço e aí fica
duas vezes mais forte: 3 dB. Num quarto, 4 vezes mais forte: 6 dB.
Os fabricantes indicam o ganho em dBi; o limite legal conta em dBd, consulta
[Dentro do limite legal](#legal).

### Qual o ganho para o teu local {#choose-gain}

- **Colinas, vales ou uma cidade densa: cerca de 3 dBi.** O feixe alto chega
  a nós acima e abaixo de ti, e contorna as encostas e os edifícios no caminho.
  Também funciona ao contrário: a partir de um vale, um feixe plano passa por baixo de um
  repetidor na colina acima. A RAKwireless RAKARG12 é um exemplo: um
  tubo de fibra de vidro com 36 cm.
- **Subúrbios ou uma vila com telhados baixos: 5 a 6 dBi.** A colinear
  de fibra de vidro habitual.
- **Terreno plano e aberto: 8 a 10 dBi.** O feixe mais plano chega mais longe
  ao longo do horizonte. Montada alto, passa por cima dos nós próximos.

O ganho no nome é o melhor valor em toda a banda da antena.
A RAKARG12, vendida como 3 dBi, tem 2.8 dBi entre 865 e 870 MHz. Lê a tabela
de ganho na ficha técnica à frequência do teu preset.

Acima de 7 dBi, uma placa de 22 dBm ultrapassa o limite legal, a não ser que a perda no cabo e no filtro
compense a diferença. Baixa a potência de transmissão em conformidade.

Um ganho alto só ajuda quando sabes onde estão os nós: ao longo do horizonte
à volta de um repetidor, ou num único repetidor distante para uma Yagi. Um companion na tua
mão aponta para todos os lados, por isso o ganho baixo com que veio é o que melhor lhe serve.

## Porquê na vertical {#vertical}

As antenas ouvem-se melhor quando apontam na mesma direção. A perda cresce com o ângulo entre elas: 45 graus custam 3 dB, metade do teu sinal. A 90 graus, uma antena deitada contra uma na vertical, em teoria não chega nada. A mesh está na vertical, logo a tua antena também. Isto vale também para um companion numa secretária: deita-o e todos os nós à tua volta ouvem menos.

## Conectores {#connectors}

Encomenda a antena com o conector
que a tua placa tem. Cada adaptador é mais uma junção para vedar e mais sinal
perdido.

- **SMA.** Um conector roscado com cerca de 6 mm de largura. A tomada na maioria das placas
  tem um furo no centro; a antena tem o pino. Um conector deste
  tipo perde cerca de 0.03 dB a 868 MHz.
- **RP-SMA.** O mesmo corpo e a mesma rosca que o SMA, com o pino e o furo
  trocados. Parece SMA e não encaixa com ele. Verifica qual
  a tua placa tem antes de encomendares.
- **U.FL (IPEX).** Uma tomada minúscula de encaixe por pressão na própria placa. Um
  cabo pigtail curto vai dela até uma tomada SMA na caixa. Está classificada para
  30 ciclos de ligação, por isso liga-a uma vez e deixa-a ficar.
- **N.** O conector roscado grande nas antenas de fibra de vidro e no cabo
  grosso. Perde no máximo 0.05 dB. Um repetidor precisa de um
  adaptador ou pigtail de N para o SMA da placa.

## Perda no cabo {#cable}

O cabo custa sinal antes de este sair da antena, nos dois sentidos. 3 dB
é metade da tua potência. Os valores dos fabricantes por metro, de 868 a 900 MHz:

| Cabo | Perda por metro | Perda em 5 m |
|---|---|---|
| RG174 | 1.02 dB | 5.1 dB |
| RG316 | 0.78 dB | 3.9 dB |
| RG58 | 0.45 dB | 2.2 dB |
| H-155 | 0.27 dB | 1.4 dB |
| LMR-240 | 0.25 dB | 1.2 dB |
| Ecoflex 10 | 0.13 dB | 0.7 dB |
| LMR-400 | 0.13 dB | 0.6 dB |

3 metros de RG174, o pigtail fino fornecido com muitas placas, perdem metade
da tua potência. Monta a placa junto à antena com um pigtail curto, ou
leva cabo grosso até ela. Soma cada adaptador e filtro no caminho ao total.

## Filtros {#filters}

Um filtro fica entre o rádio e a antena. Deixa passar a tua banda e
bloqueia o resto, para que um transmissor forte nas proximidades não sature o
recetor. Precisas de um quando um nó ouve menos do que devia perto de outros
transmissores. Um repetidor num mastro com estações base de telemóvel é um
nó desses. Um filtro custa sinal nos dois sentidos: conta a sua perda como
a do cabo.

| | Filtro SAW | Filtro de cavidade |
|---|---|---|
| Tamanho | Alguns milímetros, numa placa pequena | Um bloco ou tubo de metal |
| Perda de um bom | menos de 2 dB | menos de 1 dB |
| Potência máxima de entrada de um bom | 500 mW | vários watts |

O sysmocom cf866.5-kt30, por exemplo, é um filtro de cavidade para 863 a
870 MHz que perde no máximo 1.0 dB e aguenta 30 W. É feito para interiores,
por isso coloca-o numa caixa vedada num mastro.

Os filtros diferem muito, por isso consulta a ficha técnica antes de comprares. A sua
potência de entrada classificada tem de exceder a tua potência de transmissão, e a sua banda de passagem tem de incluir
a frequência do teu preset.

## Montagem {#mounting}

- **Acima do beiral do telhado.** A antena precisa de uma vista desimpedida em todas as direções que serve. Mesmo uns poucos metros acima dos telhados vizinhos ajudam. [Escolher um local](/repeater-guide/#site) no guia de repetidores mostra como verificar a vista.
- **Longe de metal.** Caleiras, mastros, outras antenas e telhados metálicos junto à antena alteram o seu padrão e a sua sintonia. Monta-a no topo do mastro, não ao lado.
- **Na vertical.** Usa um nível de bolha; ver [Porquê na vertical](#vertical).
- **Laço de gotejamento.** Deixa o cabo pender abaixo do conector antes de subir ou entrar. Assim a água pinga em vez de escorrer para dentro da junção.
- **Veda todos os conectores exteriores.** Água num conector aumenta a perda e corrói o pino. Veda-o contra a chuva e verifica a vedação todos os anos.
- **Relâmpagos.** Uma antena num telhado é um alvo. Um descarregador a gás no cabo dispara com uma sobretensão e envia-a para a terra. Segue [Hardware](/repeater-guide/#hardware) no guia de repetidores e as regras locais para a ligação à terra.

## Dentro do limite legal {#legal}

{{< callout type="legal" verified="2026-10-22" >}}
Na Europa o MeshCore usa a sub-banda 869.40-869.65 MHz, com no máximo
**500 mW** de potência efetiva radiada (e.r.p.). O limite conta o que sai da antena:
o ganho da antena soma, a perda no cabo e no filtro subtrai. O ganho em dBi conta
2.15 dB menos, porque o limite é medido em relação a um dipolo.
{{< /callout >}}

Uma colinear de 5.8 dBi numa placa de 22 dBm fica dentro do limite. A mesma
antena numa placa com amplificador não fica, até baixares a potência de
transmissão. [Potência: e.r.p. e a tua antena](/repeater-guide/#erp) no
guia de repetidores tem a soma e 2 exemplos resolvidos.

## Verificar uma antena com um NanoVNA {#nanovna}

Um NanoVNA é um analisador vetorial de redes de bolso. Mostra a que
frequência uma antena está sintonizada, para saberes antes de a montares. O
NanoVNA-H mede até 1.5 GHz, o que cobre 868 MHz.

1. Calibra-o para 800 a 950 MHz com as peças de circuito aberto, curto-circuito e carga
   do seu kit.
2. Liga a antena através do adaptador que vai usar no nó. Segura-a
   na vertical e afastada do teu corpo e da mesa.
3. Lê a curva de SWR (relação de onda estacionária): mostra quanto sinal
   a antena devolve. O mínimo tem de ficar na frequência do teu preset, 869.618
   MHz para EU/UK (Narrow). Um mínimo a centenas de MHz de distância significa que a antena é
   feita para outra banda.

Um quarto de onda a 868 MHz são 86 mm (o comprimento de onda é 345 mm). O comprimento
por si só não te diz a banda, porque os fabricantes dobram e carregam as hastes; o
NanoVNA diz.

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
- Conectores: as fichas técnicas Rosenberger 32S102 (SMA) e 53S101 (N), o catálogo Hirose U.FL.
- Filtros: a página do produto sysmocom cf866.5-kt30,
  [descarregadores a gás Citel](https://citel.us/en/gas-tube-surge-arrestors-for-coaxial-line-protection).
- Perda por polarização: [Universidade de Toronto, efeitos de Friis](https://www.waves.utoronto.ca/prof/svhum/ece422/notes/12-friiseffects.pdf).
- Ganho do dipolo por comprimento: [Wikipedia, Dipole antenna](https://en.wikipedia.org/wiki/Dipole_antenna).
- Comprimento de onda: velocidade da luz do [NIST](https://physics.nist.gov/cgi-bin/cuu/Value?c).
- NanoVNA: [NanoVNA-H](https://github.com/hugen79/NanoVNA-H).
- Limite legal: [Recomendação ERC 70-03 da CEPT](https://docdb.cept.org/document/845),
  Anexo 1, banda h1.7; o [guia de repetidores](/repeater-guide/#legal) lista o resto.
