---
title: Guía de antenas
lead: Unha antena axeitada e ben montada chega máis lonxe que unha potencia maior. Comproba a antena do teu companion e despois escolle, conecta e monta unha para un repetidor.
description: 'Escolle e monta unha antena de MeshCore para 868 MHz: comprobar a antena de látego dun companion, tipos de antena e ganancia, conectores, perda do cable por metro, filtros, montaxe e como conta a ganancia para o límite legal.'
eyebrow: Companion e repetidor · 868 MHz
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'f828c4aa'
  seeded: '2026-11-02'
  fields: {title: '3a76cb0e', lead: 'd82ec429', description: 'ce3f3e73', eyebrow: 'd2203a35'}
  sections: ['908e2678', 'f9b96f42', 'ca18da90', 'bcfb40ec', '851afd23', '8b7a2209', 'd8832cfa', '5b70b9e8', '14a38e92', 'a5dc1e34', 'de04ca41', 'a23f19c6', '93846db4']
  blocks: ['908e2678', '0868bca9', '081db416', 'ad1da217', '73844333', 'aa14f1b1', '07e4fbad', '32d64d0d', 'ef66133c', '558c115b', '5d28e314', '57d6e138', 'e9b3d055', 'dd757d4a', '2cbd0b58', '21c67ec0', '306a3ded', 'fa46c89f', '1e6ccb3a', 'a3e53320', '6ae131c0', '98f350c6', '138d049d', '3bd28746', '2fc98ff1', '5ea29ee5', 'cfbd64e1', '48833347', '56a82a5c', '4ef7e883', '711e4fee', '1f7844ed', '6b188411', '8da9aa78', '4c2d8bbc', 'a721a9d0', '69c1dc1a', 'a631dbfa', '3f9f3471', '5af4ae3b', 'fa5095fd', '65eeb436', '15aa0eca', 'a8f5b505', '57f35115', '8e5e4975', '89764d3d']
---

A altura, unha antena ben sintonizada e un cable curto dan máis alcance que
calquera milivatio extra. Esta guía comeza polo companion, a radio coa que envías
as mensaxes. Despois trata a antena dun repetidor, un nodo que reenvía as
mensaxes desde un tellado ou un mastro.

## O teu companion {#companion}

{{< callout type="warning" >}}
Conecta a antena antes de acender a radio. Se unha radio LoRa transmite sen
antena, pode danar o seu propio chip.
{{< /callout >}}

A antena que trae a túa placa cumpre ben. Conéctaa, mantén o nodo en vertical e
comeza a enviar mensaxes. Cunha antena mellor no companion gañas pouco; cun
repetidor ao teu alcance gañas moito.

Compra unha antena de látego á parte só se a orixinal está rota ou se non a tes.
Non todas as antenas de látego que se venden para 868 MHz están sintonizadas para
esa frecuencia. Antes de fiarte dela, [compróbaa cun
NanoVNA](#nanovna), un analizador de antenas de peto, ou pide prestada unha dunha
placa que funcione.

Un nodo preto dun transmisor forte oe menos do que debería. Un pequeno
[filtro SAW (de onda acústica superficial)](#filters) entre a radio e a antena
impide que ese transmisor entre no receptor. Mira antes a súa folla de datos:

- **Potencia máxima de entrada.** O teu propio sinal tamén pasa polo filtro. Unha
  placa que transmite 22 dBm (160 mW) a un filtro preparado para 15 dBm rompe o
  filtro.
- **Banda de paso.** Debe incluír a frecuencia da túa predefinición. Un filtro
  para 868.65 a 869.25 MHz non deixa pasar a canle EU/UK (Narrow) de
  869.618 MHz.

## Tipos de antena para un repetidor {#types}

Todas as antenas da rede están en vertical. Escolle o tipo segundo onde estean os
nodos aos que queres chegar:

- **Colineal de fibra de vidro.** Un tubo branco nun mastro, con ganancia en todo
  o horizonte. É a opción habitual para un repetidor que dá servizo a unha vila.
- **Dipolo.** É máis curto, con menos ganancia e un feixe alto. Chega mellor que
  unha colineal aos nodos que tes por debaixo e por riba, por exemplo desde un
  outeiro sobre un val.
- **Yagi.** Un brazo con elementos cruzados, apuntado a un só lugar. Chega a un
  único repetidor afastado e a pouco máis. Móntaa cos elementos en vertical,
  porque a súa polarización segue a dos elementos.

## A ganancia e o feixe {#gain}

A ganancia non engade potencia. Colle o sinal que iría cara arriba e cara abaixo
e envíao ao longo do horizonte. É como unha lanterna que enfocas: a mesma pila,
un feixe máis longo e estreito. Vese ben nun dipolo e nunha colineal do mesmo
fabricante:

| Antena | Ganancia | Ancho vertical do feixe |
|---|---|---|
| Dipolo (Sirio SO 868-915-2) | 2.2 dBi | 88 graos |
| Colineal de fibra de vidro (Sirio SPO 868-915-6) | 5.8 dBi | 23 graos |

{{< gain >}}

O diagrama corta o mastro e vese de lado. Xírao arredor do mastro e terás o feixe
completo: unha rosquilla no dipolo, un disco plano na colineal. Unha antena
vertical emite igual en todas as direccións ao seu redor. Fóra do feixe debuxado o
sinal non se detén; é máis débil, pero abonda para un nodo próximo.

Nun tellado convén un feixe plano. Nun outeiro moi por riba dos nodos, un feixe de
23 graos pásalles por riba da cabeza; un dipolo cóbreos. Unha Yagi vai aínda máis
alá: 16.6 dBi nun feixe de 23 graos de alto e 25 graos de ancho (Amphenol Procom
7176870), e nada cara aos lados.

A ganancia mídese respecto dunha referencia. O dBi compara cunha antena ideal que
emite igual en todas as direccións. O dBd compara cun dipolo de media onda, que
xa ten 2.15 dBi: mesmo a antena máis sinxela non emite nada directamente cara
arriba nin cara abaixo. Un dipolo máis longo, de 1.25 lonxitudes de onda, chega a
5.2 dBi. Unha colineal, en cambio, apila elementos de media onda uns sobre outros:
canto máis apila, maior é a ganancia. Se concentras o mesmo sinal na metade do
espazo, alí é o dobre de forte: 3 dB. Nun cuarto, 4 veces máis forte: 6 dB. Os
fabricantes indican a ganancia en dBi; o límite legal conta en dBd, consulta
[Dentro do límite legal](#legal).

### Que ganancia escoller para o teu lugar {#choose-gain}

- **Outeiros, vales ou unha cidade densa: uns 3 dBi.** O feixe alto chega aos nodos
  que tes por riba e por debaixo, e rodea as ladeiras e os edificios que hai polo
  medio. Tamén funciona ao revés: desde un val, un feixe plano pasa por debaixo
  dun repetidor situado no outeiro de arriba. A RAKwireless RAKARG12 é unha destas
  antenas: un tubo de fibra de vidro de 36 cm.
- **Arrabaldes ou unha vila de tellados baixos: de 5 a 6 dBi.** A colineal de
  fibra de vidro habitual.
- **Terreo chan e aberto: de 8 a 10 dBi.** O feixe máis plano chega máis lonxe ao
  longo do horizonte. Se a montas en alto, o feixe pasa por riba dos nodos próximos.

A ganancia que aparece no nome é a mellor cifra de toda a banda da antena. A
RAKARG12, que se vende como 3 dBi, ten 2.8 dBi entre 865 e 870 MHz. Mira a táboa de
ganancia da folla de datos na frecuencia da túa predefinición.

Por riba de 7 dBi, unha placa de 22 dBm supera o límite legal, salvo que as perdas
do cable e do filtro compensen a diferenza. Baixa a potencia de transmisión para
compensalo.

A ganancia alta só axuda se sabes onde están os nodos: ao longo do horizonte
arredor dun repetidor, ou nun repetidor afastado no caso dunha Yagi. Un companion
na man apunta a todos os lados, así que lle vai mellor a ganancia baixa que trae de
serie.

## Por que en vertical {#vertical}

As antenas óense mellor cando apuntan na mesma dirección. A perda medra co ángulo
entre elas: 45 graos custan 3 dB, a metade do teu sinal. A 90 graos, cunha antena
deitada fronte a outra vertical, en teoría non chega nada. A rede está en vertical,
así que a túa antena tamén. Isto vale igualmente para un companion nunha mesa: se o
deitas, todos os nodos ao teu redor te oen peor.

## Conectores {#connectors}

Pide a antena co conector que ten a túa placa. Cada adaptador é unha unión máis
que selar e máis sinal perdido.

- **SMA.** Un conector roscado de uns 6 mm de ancho. A toma da maioría das placas
  ten un orificio no centro; a antena leva o pin. Un conector deste tipo perde
  uns 0.03 dB a 868 MHz.
- **RP-SMA.** Ten o mesmo corpo e a mesma rosca que o SMA, co pin e o orificio
  intercambiados. Parécese ao SMA e non encaixa con el. Comproba cal ten a túa
  placa antes de facer o pedido.
- **U.FL (IPEX).** Unha toma diminuta de presión na propia placa. Un cable pigtail
  curto vai desde ela ata unha toma SMA na caixa. Está deseñada para 30 ciclos de
  conexión, así que conéctaa unha vez e déixaa así.
- **N.** O conector roscado grande das antenas de fibra de vidro e do cable groso.
  Perde como máximo 0.05 dB. Un repetidor necesita un adaptador ou un pigtail de N
  ao SMA da placa.

## Perda no cable {#cable}

O cable quítache sinal antes de que saia da antena, nos dous sentidos. 3 dB son a
metade da túa potencia. Estas son as cifras dos fabricantes por metro, de 868 a
900 MHz:

| Cable | Perda por metro | Perda en 5 m |
|---|---|---|
| RG174 | 1.02 dB | 5.1 dB |
| RG316 | 0.78 dB | 3.9 dB |
| RG58 | 0.45 dB | 2.2 dB |
| H-155 | 0.27 dB | 1.4 dB |
| LMR-240 | 0.25 dB | 1.2 dB |
| Ecoflex 10 | 0.13 dB | 0.7 dB |
| LMR-400 | 0.13 dB | 0.6 dB |

3 metros de RG174, o pigtail fino que traen moitas placas, fanche perder a metade
da potencia. Monta a placa xunto á antena cun pigtail curto, ou leva ata ela un
cable groso. Suma tamén cada adaptador e cada filtro do camiño.

## Filtros {#filters}

O filtro vai entre a radio e a antena. Deixa pasar a túa banda e bloquea o resto,
para que un transmisor forte próximo non sature o receptor. Necesítalo cando un
nodo oe menos do que debería preto doutros transmisores. Un repetidor nun mastro
con estacións base de telefonía móbil é un nodo deste tipo. O filtro quita sinal
nos dous sentidos: conta a súa perda como a do cable.

| | Filtro SAW | Filtro de cavidade |
|---|---|---|
| Tamaño | Uns poucos milímetros, nunha placa pequena | Un bloque ou tubo metálico |
| Perda dun bo filtro | menos de 2 dB | menos de 1 dB |
| Potencia máxima de entrada dun bo filtro | 500 mW | varios vatios |

O sysmocom cf866.5-kt30, por exemplo, é un filtro de cavidade para 863 a 870 MHz
que perde como máximo 1.0 dB e admite 30 W. Está feito para interiores, así que
nun mastro ponno nunha caixa selada.

Os filtros varían moito, así que mira a folla de datos antes de compralos. A súa
potencia de entrada nominal debe superar a túa potencia de transmisión, e a súa
banda de paso debe incluír a frecuencia da túa predefinición.

## Montaxe {#mounting}

- **Por riba do bordo do tellado.** A antena necesita vista despexada en todas as
  direccións que cobre. Mesmo uns poucos metros por riba dos tellados de arredor
  axudan. [Escoller un lugar](/repeater-guide/#site), na guía de repetidores,
  explica como comprobar a vista.
- **Lonxe do metal.** Os canlóns, os mastros, outras antenas e os tellados metálicos
  a carón da antena alteran o seu patrón e a súa sintonía. Móntaa enriba do mastro,
  non ao seu carón.
- **En vertical.** Usa un nivel de burbulla; consulta [Por que en vertical](#vertical).
- **Bucle de goteo.** Deixa que o cable colgue por debaixo do conector antes de
  subir ou entrar. Así a auga pinga no canto de correr ata a unión.
- **Sela todos os conectores exteriores.** A auga nun conector aumenta a perda e
  corroe o pin. Séllao contra a chuvia e revisa o selado cada ano.
- **Raios.** Unha antena nun tellado é un obxectivo. Un descargador de gas no cable
  actúa ante unha sobretensión e desvíaa a terra. Sigue
  [Hardware](/repeater-guide/#hardware), na guía de repetidores, e as normas locais
  de conexión a terra.

## Dentro do límite legal {#legal}

{{< callout type="legal" verified="2026-10-22" >}}
En Europa MeshCore usa a subbanda 869.40-869.65 MHz, cun máximo de **500 mW** de
potencia radiada efectiva (e.r.p.). O límite conta o que sae da antena: a ganancia
da antena súmase, e as perdas do cable e do filtro réstanse. A ganancia en dBi
conta 2.15 dB menos, porque o límite se mide respecto dun dipolo.
{{< /callout >}}

Unha colineal de 5.8 dBi nunha placa de 22 dBm mantense dentro do límite. A mesma
antena nunha placa con amplificador supérao, ata que baixes a potencia de
transmisión. En [Potencia: e.r.p. e a túa antena](/repeater-guide/#erp), na guía de
repetidores, tes a suma e 2 exemplos resoltos.

## Comprobar unha antena cun NanoVNA {#nanovna}

Un NanoVNA é un analizador vectorial de redes de peto. Mostra a que frecuencia está
sintonizada unha antena, así que o sabes antes de montala. O NanoVNA-H mide ata
1.5 GHz, o que cobre 868 MHz.

1. Calíbrao para 800 a 950 MHz coas pezas open, short e load do seu kit.
2. Conecta a antena co adaptador que usará no nodo. Mantena en vertical e lonxe do
   teu corpo e da mesa.
3. Le a curva de SWR (razón de onda estacionaria): mostra canto sinal devolve a
   antena. O mínimo debe estar na frecuencia da túa predefinición, 869.618 MHz para
   EU/UK (Narrow). Un mínimo a centos de MHz de distancia significa que a antena
   está feita para outra banda.

Un cuarto de onda a 868 MHz son 86 mm (a lonxitude de onda é de 345 mm). A lonxitude
por si soa non indica a banda, porque os fabricantes dobran e cargan as antenas de
látego; o NanoVNA si a indica.

## Fontes {#sources}

- Perda no cable: [Belden 8216 (RG174)](https://catalog.belden.com/techdata/en/8216_techdata.pdf),
  a folla de datos do Huber+Suhner RG316,
  [Belden 8240 (RG58)](https://catalog.belden.com/techdata/en/8240_techdata.pdf),
  [SSB H-155](https://www.ssb.de/media/h155ssb-en.pdf),
  as follas de datos do Times Microwave LMR-240 e LMR-400,
  [SSB Ecoflex 10](https://www.rigpix.com/otherusefulinfo/coax/ecoflex10.pdf).
- Antenas: [Sirio SPO 868-915-6](https://rigpix.com/antennas/sirio_spo8689156_manual.pdf),
  a folla de datos da Sirio SO 868-915-2,
  [Amphenol Procom 7176870](https://amphenolprocom.com/products/base-station-antennas/2236-7176870),
  [RAKwireless RAKARG12](https://docs.rakwireless.com/product-categories/accessories/rakarg12/datasheet/).
- A ganancia como sinal concentrado en menos espazo: [RF Cafe, introdución ás antenas](https://www.rfcafe.com/references/electrical/ew-radar-handbook/antenna-introduction-basics.htm).
- Conectores: as follas de datos de Rosenberger 32S102 (SMA) e 53S101 (N), o
  catálogo Hirose U.FL.
- Filtros: a páxina de produto do sysmocom cf866.5-kt30,
  [descargadores de gas Citel](https://citel.us/en/gas-tube-surge-arrestors-for-coaxial-line-protection).
- Perda por polarización: [Universidade de Toronto, efectos de Friis](https://www.waves.utoronto.ca/prof/svhum/ece422/notes/12-friiseffects.pdf).
- Ganancia do dipolo segundo a lonxitude: [Wikipedia, Dipole antenna](https://en.wikipedia.org/wiki/Dipole_antenna).
- Lonxitude de onda: velocidade da luz segundo o [NIST](https://physics.nist.gov/cgi-bin/cuu/Value?c).
- NanoVNA: [NanoVNA-H](https://github.com/hugen79/NanoVNA-H).
- Límite legal: [Recomendación CEPT ERC 70-03](https://docdb.cept.org/document/845),
  Anexo 1, banda h1.7; a [guía de repetidores](/repeater-guide/#legal) recolle o
  resto.
