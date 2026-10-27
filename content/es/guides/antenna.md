---
title: Guía de antenas
lead: La antena es la mitad de tu nodo. La adecuada, bien montada, llega más lejos que más potencia. Comprueba la antena de tu companion y luego elige, conecta y monta una para un repetidor.
description: 'Elige y monta una antena MeshCore para 868 MHz: comprueba el látigo de un companion, tipos de antena y ganancia, conectores, pérdida del cable por metro, filtros, montaje y cómo cuenta la ganancia para el límite legal.'
eyebrow: Companion y repetidor · 868 MHz
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '45010ad0'
  seeded: '2026-10-26'
  fields: {title: '3a76cb0e', lead: '98430ade', description: 'ce3f3e73', eyebrow: 'd2203a35'}
  sections: ['908e2678', 'f9b96f42', '94c5bae4', 'bcfb40ec', '851afd23', '8b7a2209', 'd8832cfa', '5b70b9e8', '14a38e92', 'a5dc1e34', 'de04ca41', 'a23f19c6', '93846db4']
---

La altura, una antena sintonizada y un cable corto ganan más alcance que cualquier milivatio extra. Esta guía empieza por el companion, la radio desde la que envías mensajes. Después trata la antena de un repetidor, un nodo que reenvía mensajes desde un tejado o un mástil.

## Tu companion {#companion}

{{< callout type="warning" >}}
Conecta la antena antes de encender la radio. Una radio LoRa que transmite sin antena puede dañar su propio chip.
{{< /callout >}}

La antena que venía con tu placa cumple. Conéctala, mantén el nodo en vertical y empieza a enviar mensajes. Una antena mejor en un companion gana poco; un repetidor al alcance gana mucho.

Compra un látigo aparte solo si el que venía está roto o falta. No todos los látigos que se venden para 868 MHz están sintonizados para esa banda. [Compruébalo con un NanoVNA](#nanovna), un analizador de antenas de bolsillo, antes de fiarte de él, o toma prestado uno de una placa que funcione.

Un nodo junto a un transmisor potente oye menos de lo que debería. Un pequeño [filtro SAW (de onda acústica superficial)](#filters) entre la radio y la antena mantiene ese transmisor fuera del receptor. Revisa antes su hoja de datos:

- **Potencia máxima de entrada.** El filtro también está en la ruta de tu propia transmisión. Una placa que transmite 22 dBm (160 mW) hacia un filtro diseñado para 15 dBm rompe el filtro.
- **Banda de paso.** Debe incluir la frecuencia de tu preset. Un filtro para 868.65 a 869.25 MHz no deja pasar el canal EU/UK (Narrow) en 869.618 MHz.

## Tipos de antena para un repetidor {#types}

Todas las antenas de la malla están en vertical. Elige el tipo según dónde estén los nodos a los que quieres llegar:

- **Colineal de fibra de vidrio.** Un tubo blanco sobre un mástil, con ganancia en todo el horizonte. La elección habitual para un repetidor que da servicio a una ciudad.
- **Dipolo.** Más corto, con menos ganancia y un haz alto. Llega mejor que un colineal a los nodos que están por debajo y por encima de ti. Eso importa en una colina sobre un valle.
- **Yagi.** Una barra con elementos cruzados, apuntada a un solo sitio. Llega a un único repetidor lejano y a poco más. Móntala con los elementos en vertical, porque su polarización sigue a los elementos.

## La ganancia y el haz {#gain}

La ganancia no añade potencia. Toma la señal que iría hacia arriba y hacia abajo y la envía a lo largo del horizonte. Como una linterna que enfocas: la misma pila, un haz más largo y más estrecho. Un dipolo y un colineal del mismo fabricante lo muestran:

| Antena | Ganancia | Ancho de haz vertical |
|---|---|---|
| Dipolo (Sirio SO 868-915-2) | 2.2 dBi | 88 grados |
| Colineal de fibra de vidrio (Sirio SPO 868-915-6) | 5.8 dBi | 23 grados |

{{< gain >}}

El diagrama corta por el mástil, visto de lado. Gíralo alrededor del mástil y tienes el haz completo: una rosquilla para el dipolo, un disco plano para el colineal. Una antena en vertical emite igual en todas las direcciones a su alrededor. Fuera del haz dibujado la señal no se detiene; es más débil, pero aún suficiente para un nodo cercano.

En un tejado, un haz plano es lo que quieres. En una colina muy por encima de los nodos, un haz de 23 grados pasa por encima de sus cabezas; un dipolo los cubre. Una Yagi lleva esto más lejos: 16.6 dBi en un haz de 23 grados de alto y 25 grados de ancho (Amphenol Procom 7176870), y nada hacia los lados.

La ganancia se mide respecto a una referencia. dBi compara con una antena ideal que emite igual en todas las direcciones. dBd compara con un dipolo de media onda, que ya tiene 2.15 dBi: hasta la antena más simple no emite nada hacia arriba ni hacia abajo. Un dipolo más largo, de 1.25 longitudes de onda, alcanza 5.2 dBi. Un colineal, en cambio, apila elementos de media onda unos sobre otros: cuantos más apila, mayor es la ganancia. Concentra la misma señal en la mitad del espacio y ahí es el doble de fuerte: 3 dB. En un cuarto, 4 veces más fuerte: 6 dB. Los fabricantes indican la ganancia en dBi; el límite legal cuenta en dBd, consulta [Dentro del límite legal](#legal).

### Qué ganancia para tu emplazamiento {#choose-gain}

- **Colinas, valles o una ciudad densa: unos 3 dBi.** El haz alto llega a los nodos por encima y por debajo de ti, y rodea las laderas y los edificios que estorban. También funciona al revés: desde un valle, un haz plano pasa por debajo de un repetidor en la colina de arriba. La RAKwireless RAKARG12 es una de ellas: un tubo de fibra de vidrio de 36 cm.
- **Afueras o una ciudad con tejados bajos: 5 a 6 dBi.** El colineal de fibra de vidrio habitual.
- **Terreno llano y abierto: 8 a 10 dBi.** El haz más plano llega más lejos a lo largo del horizonte. Montado en alto, pasa por encima de los nodos cercanos.

La ganancia del nombre es la mejor cifra en toda la banda de la antena. La RAKARG12, vendida como de 3 dBi, tiene 2.8 dBi entre 865 y 870 MHz. Lee la tabla de ganancia de la hoja de datos en la frecuencia de tu preset.

Por encima de 7 dBi, una placa de 22 dBm supera el límite legal, salvo que la pérdida del cable y del filtro compense la diferencia. Baja la potencia de transmisión para ajustarte.

Una ganancia alta solo ayuda cuando sabes dónde están los nodos: a lo largo del horizonte alrededor de un repetidor, o en un único repetidor lejano para una Yagi. Un companion en tu mano apunta a todas partes, así que la ganancia baja con la que venía es la que mejor le va.

## Por qué en vertical {#vertical}

Las antenas se oyen mejor entre sí cuando apuntan en la misma dirección. La pérdida crece con el ángulo entre ellas: 45 grados cuestan 3 dB, la mitad de tu señal. A 90 grados, una antena tumbada frente a una vertical, en teoría no llega nada. La malla está en vertical, así que tu antena también. Esto vale también para un companion sobre un escritorio: túmbalo y todos los nodos a tu alrededor oyen menos.

## Conectores {#connectors}

Pide la antena con el conector que tiene tu placa. Cada adaptador es una unión más que sellar y más señal perdida.

- **SMA.** Un conector roscado de unos 6 mm de ancho. La toma de la mayoría de las placas tiene un agujero en el centro; la antena tiene el pin. Un conector de este tipo pierde unos 0.03 dB a 868 MHz.
- **RP-SMA.** El mismo cuerpo y la misma rosca que el SMA, con el pin y el agujero intercambiados. Parece un SMA y no encaja con él. Comprueba cuál tiene tu placa antes de pedir.
- **U.FL (IPEX).** Una toma diminuta a presión en la propia placa. De ella sale un cable corto (pigtail) hasta una toma SMA en la carcasa. Está diseñada para 30 ciclos de conexión, así que conéctala una vez y déjala.
- **N.** El conector roscado grande de las antenas de fibra de vidrio y del cable grueso. Pierde como máximo 0.05 dB. Un repetidor necesita un adaptador o pigtail de N al SMA de la placa.

## Pérdida del cable {#cable}

El cable cuesta señal antes de que salga por la antena, en ambos sentidos. 3 dB es la mitad de tu potencia. Las cifras de los fabricantes por metro, entre 868 y 900 MHz:

| Cable | Pérdida por metro | Pérdida en 5 m |
|---|---|---|
| RG174 | 1.02 dB | 5.1 dB |
| RG316 | 0.78 dB | 3.9 dB |
| RG58 | 0.45 dB | 2.2 dB |
| H-155 | 0.27 dB | 1.4 dB |
| LMR-240 | 0.25 dB | 1.2 dB |
| Ecoflex 10 | 0.13 dB | 0.7 dB |
| LMR-400 | 0.13 dB | 0.6 dB |

3 metros de RG174, el pigtail fino que viene con muchas placas, pierden la mitad de tu potencia. Monta la placa junto a la antena con un pigtail corto, o lleva cable grueso hasta ella. Suma al total cada adaptador y filtro de la ruta.

## Filtros {#filters}

Un filtro va entre la radio y la antena. Deja pasar tu banda y bloquea el resto, de modo que un transmisor potente cercano no sature el receptor. Lo necesitas cuando un nodo oye menos de lo que debería cerca de otros transmisores. Un repetidor en un mástil con estaciones base de telefonía móvil es uno de esos nodos. Un filtro cuesta señal en ambos sentidos: cuenta su pérdida como la del cable.

| | Filtro SAW | Filtro de cavidad |
|---|---|---|
| Tamaño | Unos milímetros, en una placa pequeña | Un bloque o tubo metálico |
| Pérdida de uno bueno | menos de 2 dB | menos de 1 dB |
| Potencia máxima de entrada de uno bueno | 500 mW | varios vatios |

El sysmocom cf866.5-kt30, por ejemplo, es un filtro de cavidad para 863 a 870 MHz que pierde como máximo 1.0 dB y admite 30 W. Está hecho para interiores, así que ponlo en una caja estanca en el mástil.

Los filtros varían mucho, así que revisa la hoja de datos antes de comprar. Su potencia de entrada nominal debe superar tu potencia de transmisión, y su banda de paso debe incluir la frecuencia de tu preset.

## Montaje {#mounting}

- **Por encima del borde del tejado.** La antena necesita vista despejada en cada dirección a la que da servicio. Incluso unos metros por encima de los tejados vecinos ayudan. [Elige un emplazamiento](/repeater-guide/#site) en la guía del repetidor muestra cómo comprobar la vista.
- **Lejos del metal.** Los canalones, mástiles, otras antenas y tejados metálicos junto a la antena cambian su patrón y su sintonía. Móntala en lo alto del mástil, no a un lado.
- **En vertical.** Usa un nivel de burbuja; consulta [Por qué en vertical](#vertical).
- **Lazo de goteo.** Deja que el cable cuelgue por debajo del conector antes de subir o entrar. Así el agua gotea en vez de correr hacia la unión.
- **Sella cada conector exterior.** El agua en un conector aumenta la pérdida y corroe el pin. Séllalo contra la lluvia y revisa el sellado cada año.
- **Rayos.** Una antena en un tejado es un blanco. Un descargador de gas en el cable se dispara con una sobretensión y la envía a tierra. Sigue [Hardware](/repeater-guide/#hardware) en la guía del repetidor y la normativa local sobre puesta a tierra.

## Dentro del límite legal {#legal}

{{< callout type="legal" verified="2026-10-22" >}}
En Europa MeshCore usa la subbanda 869.40-869.65 MHz, con como máximo **500 mW** de potencia radiada aparente (e.r.p.). El límite cuenta lo que sale de la antena: la ganancia de la antena suma, la pérdida del cable y del filtro resta. La ganancia en dBi cuenta 2.15 dB menos, porque el límite se mide respecto a un dipolo.
{{< /callout >}}

Un colineal de 5.8 dBi en una placa de 22 dBm se mantiene dentro del límite. La misma antena en una placa con amplificador no, hasta que bajes la potencia de transmisión. [Potencia: e.r.p. y tu antena](/repeater-guide/#erp) en la guía del repetidor tiene la suma y 2 ejemplos resueltos.

## Comprueba una antena con un NanoVNA {#nanovna}

Un NanoVNA es un analizador vectorial de redes de bolsillo. Muestra en qué frecuencia está sintonizada una antena, así lo sabes antes de montarla. El NanoVNA-H mide hasta 1.5 GHz, lo que cubre 868 MHz.

1. Calíbralo para 800 a 950 MHz con las piezas de abierto, corto y carga de su kit.
2. Conecta la antena a través del adaptador que usará en el nodo. Sostenla en vertical y lejos de tu cuerpo y de la mesa.
3. Lee la curva de ROE (relación de onda estacionaria): muestra cuánta señal devuelve la antena. El valle debe caer en la frecuencia de tu preset, 869.618 MHz para EU/UK (Narrow). Un valle a cientos de MHz de distancia significa que la antena está hecha para otra banda.

Un cuarto de onda a 868 MHz mide 86 mm (la longitud de onda es 345 mm). La longitud por sí sola no te dice la banda, porque los fabricantes pliegan y cargan los látigos; el NanoVNA sí.

## Fuentes {#sources}

- Pérdida del cable: [Belden 8216 (RG174)](https://catalog.belden.com/techdata/en/8216_techdata.pdf),
  la hoja de datos del Huber+Suhner RG316,
  [Belden 8240 (RG58)](https://catalog.belden.com/techdata/en/8240_techdata.pdf),
  [SSB H-155](https://www.ssb.de/media/h155ssb-en.pdf),
  las hojas de datos de Times Microwave LMR-240 y LMR-400,
  [SSB Ecoflex 10](https://www.rigpix.com/otherusefulinfo/coax/ecoflex10.pdf).
- Antenas: [Sirio SPO 868-915-6](https://rigpix.com/antennas/sirio_spo8689156_manual.pdf),
  la hoja de datos de la Sirio SO 868-915-2,
  [Amphenol Procom 7176870](https://amphenolprocom.com/products/base-station-antennas/2236-7176870),
  [RAKwireless RAKARG12](https://docs.rakwireless.com/product-categories/accessories/rakarg12/datasheet/).
- La ganancia como señal concentrada en menos espacio: [RF Cafe, introducción a las antenas](https://www.rfcafe.com/references/electrical/ew-radar-handbook/antenna-introduction-basics.htm).
- Conectores: las hojas de datos de Rosenberger 32S102 (SMA) y 53S101 (N), el catálogo U.FL de Hirose.
- Filtros: la página de producto del sysmocom cf866.5-kt30,
  [descargadores de gas Citel](https://citel.us/en/gas-tube-surge-arrestors-for-coaxial-line-protection).
- Pérdida por polarización: [Universidad de Toronto, efectos de Friis](https://www.waves.utoronto.ca/prof/svhum/ece422/notes/12-friiseffects.pdf).
- Ganancia del dipolo según su longitud: [Wikipedia, Dipole antenna](https://en.wikipedia.org/wiki/Dipole_antenna).
- Longitud de onda: velocidad de la luz según el [NIST](https://physics.nist.gov/cgi-bin/cuu/Value?c).
- NanoVNA: [NanoVNA-H](https://github.com/hugen79/NanoVNA-H).
- Límite legal: [Recomendación ERC 70-03 de la CEPT](https://docdb.cept.org/document/845),
  Anexo 1, banda h1.7; la [guía del repetidor](/repeater-guide/#legal) enumera el resto.
