---
title: Guía de antenas
lead: Una buena antena, bien montada, llega más lejos que más potencia. Revisa la antena de tu companion y después elige, conecta y monta una para un repetidor.
description: 'Elige y monta una antena MeshCore para 868 MHz: revisa el látigo de un companion, tipos de antena y ganancia, conectores, pérdida del cable por metro, filtros, montaje y cómo cuenta la ganancia para el límite legal.'
eyebrow: Companion y repetidor · 868 MHz
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'f828c4aa'
  seeded: '2026-10-31'
  fields: {title: '3a76cb0e', lead: 'd82ec429', description: 'ce3f3e73', eyebrow: 'd2203a35'}
  sections: ['908e2678', 'f9b96f42', 'ca18da90', 'bcfb40ec', '851afd23', '8b7a2209', 'd8832cfa', '5b70b9e8', '14a38e92', 'a5dc1e34', 'de04ca41', 'a23f19c6', '93846db4']
  blocks: ['908e2678', '0868bca9', '081db416', 'ad1da217', '73844333', 'aa14f1b1', '07e4fbad', '32d64d0d', 'ef66133c', '558c115b', '5d28e314', '57d6e138', 'e9b3d055', 'dd757d4a', '2cbd0b58', '21c67ec0', '306a3ded', 'fa46c89f', '1e6ccb3a', 'a3e53320', '6ae131c0', '98f350c6', '138d049d', '3bd28746', '2fc98ff1', '5ea29ee5', 'cfbd64e1', '48833347', '56a82a5c', '4ef7e883', '711e4fee', '1f7844ed', '6b188411', '8da9aa78', '4c2d8bbc', 'a721a9d0', '69c1dc1a', 'a631dbfa', '3f9f3471', '5af4ae3b', 'fa5095fd', '65eeb436', '15aa0eca', 'a8f5b505', '57f35115', '8e5e4975', '89764d3d']
---

La altura, una antena bien sintonizada y un cable corto dan más alcance
que cualquier milivatio extra. Esta guía empieza por el companion, la radio
desde la que envías mensajes. Después trata la antena de un repetidor, un
nodo que retransmite mensajes desde un tejado o un mástil.

## Tu companion {#companion}

{{< callout type="warning" >}}
Conecta la antena antes de encender la radio. Una radio LoRa que transmite
sin antena puede dañar su propio chip.
{{< /callout >}}

La antena que venía con tu placa cumple su función. Conéctala, sostén el
nodo en vertical y empieza a enviar mensajes. Una antena mejor en un
companion aporta poco; un repetidor a tu alcance aporta mucho.

Compra un látigo aparte solo si el original está roto o te falta. No todos
los látigos que se venden para 868 MHz están sintonizados para esa
frecuencia. [Compruébalo con un NanoVNA](#nanovna), un analizador de antenas
de bolsillo, antes de fiarte de él, o pide prestado uno de una placa que
funcione.

Un nodo junto a un transmisor potente oye menos de lo que debería. Un
pequeño [filtro SAW (de onda acústica superficial)](#filters) entre la radio
y la antena impide que ese transmisor llegue al receptor. Antes, revisa su
hoja de datos:

- **Potencia máxima de entrada.** El filtro también está en el camino de
  tu propia transmisión. Si una placa transmite 22 dBm (160 mW) a un filtro
  que admite 15 dBm, el filtro se rompe.
- **Banda de paso.** Debe incluir la frecuencia de tu preset. Un filtro de
  868.65 a 869.25 MHz no deja pasar el canal EU/UK (Narrow) en
  869.618 MHz.

## Tipos de antena para un repetidor {#types}

Todas las antenas de la malla están en vertical. Elige el tipo según dónde
estén los nodos a los que quieres llegar:

- **Colineal de fibra de vidrio.** Un tubo blanco en un mástil, con ganancia
  en todo el horizonte. Es la opción habitual para un repetidor que da
  servicio a una ciudad.
- **Dipolo.** Más corto, con menos ganancia y un haz alto. Llega mejor que
  una colineal a los nodos que están por debajo y por encima de ti, por
  ejemplo desde una colina sobre un valle.
- **Yagi.** Un brazo con elementos cruzados, apuntado a un solo lugar.
  Llega a un único repetidor lejano y a poco más. Móntala con los elementos
  en vertical, porque su polarización sigue a los elementos.

## La ganancia y el haz {#gain}

La ganancia no añade potencia. Toma la señal que iría hacia arriba y hacia
abajo y la envía a lo largo del horizonte. Es como enfocar una linterna: la
misma pila, un haz más largo y estrecho. Un dipolo y una colineal del mismo
fabricante lo muestran:

| Antena | Ganancia | Ancho de haz vertical |
|---|---|---|
| Dipolo (Sirio SO 868-915-2) | 2.2 dBi | 88 grados |
| Colineal de fibra de vidrio (Sirio SPO 868-915-6) | 5.8 dBi | 23 grados |

{{< gain >}}

El diagrama corta el mástil, visto de lado. Gíralo alrededor del mástil y
tendrás el haz completo: un dónut para el dipolo, un disco plano para la
colineal. Una antena vertical emite igual en todas las direcciones a su
alrededor. Fuera del haz dibujado la señal no se corta; es más débil, pero
basta para un nodo cercano.

En un tejado te conviene un haz plano. En una colina muy por encima de los
nodos, un haz de 23 grados pasa por encima de sus cabezas; un dipolo sí los
cubre. Una Yagi lleva esto más lejos: 16.6 dBi en un haz de 23 grados de
alto y 25 grados de ancho (Amphenol Procom 7176870), y nada hacia los
lados.

La ganancia se mide frente a una referencia. El dBi toma como referencia una
antena ideal que emite igual en todas las direcciones. El dBd toma como
referencia un dipolo de media onda, que ya tiene 2.15 dBi: ni siquiera la
antena más sencilla emite nada justo hacia arriba ni hacia abajo. Un dipolo
más largo, de 1.25 longitudes de onda, llega a 5.2 dBi. Una colineal, en
cambio, apila elementos de media onda uno encima de otro: cuantos más apila,
mayor es la ganancia. Si concentras la misma señal en la mitad del espacio,
allí es el doble de fuerte: 3 dB. En una cuarta parte, 4 veces más fuerte:
6 dB. Los fabricantes indican la ganancia en dBi; el límite legal se expresa
en dBd, mira [Dentro del límite legal](#legal).

### Qué ganancia para tu emplazamiento {#choose-gain}

- **Colinas, valles o una ciudad densa: unos 3 dBi.** El haz alto llega a
  los nodos por encima y por debajo de ti, y rodea las laderas y los
  edificios que se interponen. También funciona al revés: desde un valle,
  un haz plano pasa por debajo de un repetidor en la colina de arriba. La
  RAKwireless RAKARG12 es una de ellas: un tubo de fibra de vidrio de 36 cm.
- **Afueras o un pueblo con tejados bajos: de 5 a 6 dBi.** La colineal de
  fibra de vidrio habitual.
- **Terreno llano y abierto: de 8 a 10 dBi.** El haz más plano llega más
  lejos a lo largo del horizonte. Si la montas alta, pasa por encima de los
  nodos cercanos.

La ganancia del nombre es la mejor cifra en toda la banda de la antena. La
RAKARG12, que se vende como de 3 dBi, tiene 2.8 dBi de 865 a 870 MHz. Lee la
tabla de ganancia de la hoja de datos en la frecuencia de tu preset.

Por encima de 7 dBi, una placa de 22 dBm supera el límite legal, salvo que
la pérdida del cable y del filtro compense la diferencia. Baja la potencia
de transmisión en consecuencia.

La ganancia alta solo ayuda si sabes dónde están los nodos: a lo largo del
horizonte alrededor de un repetidor, o en un repetidor lejano en el caso de
una Yagi. Un companion en tu mano apunta en todas direcciones, así que la
ganancia baja con la que venía es la que mejor le va.

## Por qué en vertical {#vertical}

Las antenas se oyen mejor cuando apuntan en la misma dirección. La pérdida
crece con el ángulo entre ellas: 45 grados cuestan 3 dB, la mitad de tu
señal. A 90 grados, una antena tumbada frente a una vertical, en teoría no
llega nada. La malla está en vertical, así que tu antena también debe
estarlo. Esto vale también para un companion en una mesa: si lo tumbas,
todos los nodos a tu alrededor te oyen peor.

## Conectores {#connectors}

Pide la antena con el conector que tiene tu placa. Cada adaptador es una
unión más que sellar y más señal perdida.

- **SMA.** Un conector roscado de unos 6 mm de ancho. En la mayoría de las
  placas, el zócalo tiene un agujero en el centro; la antena lleva la
  clavija. Un conector de este tipo pierde unos 0.03 dB a 868 MHz.
- **RP-SMA.** El mismo cuerpo y la misma rosca que el SMA, con la clavija y
  el agujero intercambiados. Parece un SMA, pero no encaja con él. Antes de
  hacer el pedido, comprueba cuál tiene tu placa.
- **U.FL (IPEX).** Un zócalo diminuto a presión en la propia placa. Un
  cable pigtail corto va desde él hasta un zócalo SMA en la caja. Está
  pensado para 30 conexiones, así que conéctalo una vez y déjalo.
- **N.** El conector roscado grande de las antenas de fibra de vidrio y del
  cable grueso. Pierde como mucho 0.05 dB. Para un repetidor necesitas un
  adaptador o un pigtail de N al SMA de la placa.

## Pérdida en el cable {#cable}

El cable te cuesta señal antes de que salga por la antena, en los dos
sentidos. 3 dB son la mitad de tu potencia. Estas son las cifras de los
fabricantes por metro, de 868 a 900 MHz:

| Cable | Pérdida por metro | Pérdida en 5 m |
|---|---|---|
| RG174 | 1.02 dB | 5.1 dB |
| RG316 | 0.78 dB | 3.9 dB |
| RG58 | 0.45 dB | 2.2 dB |
| H-155 | 0.27 dB | 1.4 dB |
| LMR-240 | 0.25 dB | 1.2 dB |
| Ecoflex 10 | 0.13 dB | 0.7 dB |
| LMR-400 | 0.13 dB | 0.6 dB |

Con 3 metros de RG174, el pigtail fino que traen muchas placas, pierdes la
mitad de tu potencia. Monta la placa junto a la antena con un pigtail corto,
o lleva hasta ella un cable grueso. Suma también cada adaptador y cada
filtro que haya en el camino.

## Filtros {#filters}

Un filtro va entre la radio y la antena. Deja pasar tu banda y bloquea el
resto, para que un transmisor potente cercano no sature el receptor. Lo
necesitas cuando un nodo oye menos de lo que debería cerca de otros
transmisores. Un repetidor en un mástil con estaciones base de telefonía
móvil es un caso así. Un filtro cuesta señal en los dos sentidos: cuenta su
pérdida como la del cable.

| | Filtro SAW | Filtro de cavidad |
|---|---|---|
| Tamaño | Unos pocos milímetros, en una placa pequeña | Un bloque o tubo metálico |
| Pérdida de uno bueno | menos de 2 dB | menos de 1 dB |
| Potencia máxima de entrada de uno bueno | 500 mW | varios vatios |

El sysmocom cf866.5-kt30, por ejemplo, es un filtro de cavidad para 863 a
870 MHz que pierde como mucho 1.0 dB y aguanta 30 W. Está hecho para
interiores, así que en un mástil ponlo en una caja estanca.

Los filtros varían mucho, así que revisa la hoja de datos antes de comprar.
Su potencia de entrada nominal debe superar tu potencia de transmisión, y su
banda de paso debe incluir la frecuencia de tu preset.

## Montaje {#mounting}

- **Por encima del borde del tejado.** La antena necesita vista despejada en
  cada dirección que cubre. Incluso unos pocos metros por encima de los
  tejados de alrededor ayudan. En la guía de repetidores, [Elige un
  emplazamiento](/repeater-guide/#site) explica cómo comprobar la vista.
- **Lejos del metal.** Los canalones, mástiles, otras antenas y tejados
  metálicos junto a la antena cambian su diagrama y su sintonía. Móntala en
  lo alto del mástil, no a un lado.
- **En vertical.** Usa un nivel de burbuja; mira [Por qué en
  vertical](#vertical).
- **Bucle de goteo.** Deja que el cable cuelgue por debajo del conector
  antes de que suba o entre. Así el agua gotea en vez de correr hacia la
  unión.
- **Sella cada conector exterior.** El agua en un conector aumenta la
  pérdida y corroe la clavija. Séllalo contra la lluvia y revisa el sellado
  cada año.
- **Rayos.** Una antena en un tejado es un blanco. Un descargador de gas en
  el cable se dispara con una sobretensión y la deriva a tierra. Para la
  toma de tierra, sigue [Hardware](/repeater-guide/#hardware) en la guía de
  repetidores y la normativa local.

## Dentro del límite legal {#legal}

{{< callout type="legal" verified="2026-10-22" >}}
En Europa, MeshCore usa la subbanda 869.40-869.65 MHz, con un máximo de
**500 mW** de potencia radiada efectiva (p.r.e.). El límite cuenta lo que
sale de la antena: la ganancia de la antena suma, y la pérdida del cable y
del filtro resta. La ganancia en dBi cuenta 2.15 dB menos, porque el límite
se mide frente a un dipolo.
{{< /callout >}}

Una colineal de 5.8 dBi en una placa de 22 dBm queda dentro del límite. La
misma antena en una placa con amplificador lo supera, hasta que bajas la
potencia de transmisión. En la guía de repetidores, [Potencia: p.r.e. y tu
antena](/repeater-guide/#erp) tiene el cálculo y 2 ejemplos resueltos.

## Comprueba una antena con un NanoVNA {#nanovna}

Un NanoVNA es un analizador vectorial de redes de bolsillo. Te muestra a qué
frecuencia está sintonizada una antena, así lo sabes antes de montarla. El
NanoVNA-H mide hasta 1.5 GHz, lo que incluye 868 MHz.

1. Calíbralo para 800 a 950 MHz con las piezas open, short y load de su
   kit.
2. Conecta la antena con el adaptador que usará en el nodo. Sostenla en
   vertical, lejos de tu cuerpo y de la mesa.
3. Lee la curva de SWR (relación de onda estacionaria): muestra cuánta señal
   devuelve la antena. El mínimo debe caer en la frecuencia de tu preset,
   869.618 MHz para EU/UK (Narrow). Si el mínimo está a cientos de MHz, la
   antena está hecha para otra banda.

Un cuarto de onda a 868 MHz mide 86 mm (la longitud de onda es de 345 mm).
La longitud por sí sola no te dice la banda, porque los fabricantes pliegan
y cargan los látigos; el NanoVNA sí te la dice.

## Fuentes {#sources}

- Pérdida en el cable: [Belden 8216 (RG174)](https://catalog.belden.com/techdata/en/8216_techdata.pdf),
  la hoja de datos de Huber+Suhner RG316,
  [Belden 8240 (RG58)](https://catalog.belden.com/techdata/en/8240_techdata.pdf),
  [SSB H-155](https://www.ssb.de/media/h155ssb-en.pdf),
  las hojas de datos de Times Microwave LMR-240 y LMR-400,
  [SSB Ecoflex 10](https://www.rigpix.com/otherusefulinfo/coax/ecoflex10.pdf).
- Antenas: [Sirio SPO 868-915-6](https://rigpix.com/antennas/sirio_spo8689156_manual.pdf),
  la hoja de datos de Sirio SO 868-915-2,
  [Amphenol Procom 7176870](https://amphenolprocom.com/products/base-station-antennas/2236-7176870),
  [RAKwireless RAKARG12](https://docs.rakwireless.com/product-categories/accessories/rakarg12/datasheet/).
- La ganancia como señal concentrada en menos espacio: [RF Cafe, introducción a las antenas](https://www.rfcafe.com/references/electrical/ew-radar-handbook/antenna-introduction-basics.htm).
- Conectores: las hojas de datos de Rosenberger 32S102 (SMA) y 53S101 (N), el
  catálogo U.FL de Hirose.
- Filtros: la página de producto de sysmocom cf866.5-kt30,
  [descargadores de gas de Citel](https://citel.us/en/gas-tube-surge-arrestors-for-coaxial-line-protection).
- Pérdida por polarización: [Universidad de Toronto, efectos de Friis](https://www.waves.utoronto.ca/prof/svhum/ece422/notes/12-friiseffects.pdf).
- Ganancia del dipolo según su longitud: [Wikipedia, Antena dipolo](https://en.wikipedia.org/wiki/Dipole_antenna).
- Longitud de onda: velocidad de la luz según el [NIST](https://physics.nist.gov/cgi-bin/cuu/Value?c).
- NanoVNA: [NanoVNA-H](https://github.com/hugen79/NanoVNA-H).
- Límite legal: [Recomendación ERC 70-03 de la CEPT](https://docdb.cept.org/document/845),
  anexo 1, banda h1.7; la [guía de repetidores](/repeater-guide/#legal) recoge
  el resto.
