---
title: Haz que la malla resista
lead: ¿La malla de tu zona va lenta o está llena de basura? Descubre qué lo provoca, activa el ajuste del repetidor que lo frena y avisa a tu grupo local.
description: 'Inundaciones y spam en una malla MeshCore: cómo reconocer cada tipo, qué ajuste del repetidor ayuda, cómo ver una inundación y cómo encontrar su origen.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '500188ff'
  seeded: '2026-10-31'
  fields: {title: '33ec7ac8', lead: '780da19b', description: '1826e5e8'}
  sections: ['68ca5d36', '133c764a', 'a3bb5172', 'f4cc9cad', 'ace7b1ee', '89651002', 'f4dfdf59', '764c832c', 'f342b64b', 'f348e208']
  blocks: ['68ca5d36', 'c9cfbe6c', 'bcb31992', 'de7f60e4', 'e862fb9b', '0046b51f', '25f34d1d', 'c3c3ea52', '853a0f1d', '2bcea703', '871a7661', '2690aacf', 'a4aec3a1', 'd6da27c6', 'e8405458', 'f9150ee6', '8508ce40', '4b03ccd5', 'fb79c493', '695adde7', 'eba5a5b5', '836e0bac', '3497c5e8', '71c78fa1', '537d0930', '6a315252', '7c84dc56', '682e08e6', '258d7a27', '53af1400', '0dbebf97', 'ac0dca3c', '70fb4e9a', '9f055f50', 'ae90facc']
---

¿Los mensajes llegan tarde o no llegan? ¿Public se llena de basura? Eso es
una inundación: más tráfico del que la malla puede llevar, enviado por
error o a propósito. Busca lo que ves en las tablas de abajo. Cada fila
indica el ajuste que lo frena. Actívalo en tu repetidor, el nodo que
reenvía los mensajes. Después avisa a tu [grupo local](/community/) para
que los repetidores de tu alrededor hagan lo mismo. Cada repetidor que
descarta una inundación deja tiempo de emisión libre para los demás.

## Inundaciones por error {#mistake}

Una inundación por error sale de un nodo cuyo dueño no sabe que la
provoca. Se acaba en cuanto lo sabe. En las tablas de abajo, un anuncio es
el saludo que envía un nodo para que los demás lo encuentren.

Los ajustes de las tablas se basan en lo que hace el firmware. No todos
han frenado ya una inundación en una malla real.

{{< callout type="warning" >}}
Algunos ajustes de esta página necesitan el firmware DMC. **MeshCore** 1.18.0
de serie trae regiones, los límites de saltos `flood.max.*`, la detección
de bucles y el ciclo de trabajo. El filtro de paquetes, las reglas con las
que tu repetidor descarta basura, viene con el **firmware DMC** de
[Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore). Lo mismo
pasa con el control por ciclo de trabajo y el filtro del companion. Esta
página sigue la versión de desarrollo DMC 1.18.0 `ecfb2d4` del 19 de
octubre de 2026. La página del [filtro de paquetes](/guides/filter/#firmware)
explica dónde conseguirla.
{{< /callout >}}

| Lo que ves | Qué es | Qué ayuda |
| --- | --- | --- |
| Peticiones a repetidores desde un mismo nodo, día y noche, y una malla que sigue lenta durante días | Un sistema domótico o un bot que pide su estado a los repetidores demasiado a menudo | `filter on`. Así el filtro de paquetes deja pasar 5 peticiones por minuto. Avisa al dueño. |
| El mismo tipo de mensaje en un canal, cada minuto | Un bot que publica demasiado a menudo | [Bloquea el canal](/guides/filter/#channel) o [frena al remitente](/guides/filter/#sender). Avisa al dueño. |
| Mensajes ilegibles en Public y otros canales | Un nodo con el firmware dañado o una configuración de radio errónea | `filter malformed on` los descarta en Public. Avisa al dueño. |
| El anuncio de un mismo nodo cada pocos minutos | Un nodo configurado para anunciarse demasiado a menudo | `filter advert 24` deja pasar el anuncio de cada nodo una vez al día. `set flood.max.advert 3` mantiene los anuncios dentro de 3 saltos. |
| Mensajes de muy lejos, con regiones que no son de aquí | Un puente que une mallas por internet | `set flood.max.unscoped 1`, y pon tu repetidor solo en las [regiones que cubre](/guides/settings/#traffic). |
| El mismo mensaje pasa una y otra vez, con el ID de tu repetidor más de una vez en su ruta | Un repetidor que modifica paquetes y los reenvía, así que dan vueltas en bucle | La detección de bucles funciona en `minimal` por defecto. Con `set loop.detect moderate` descartas un bucle antes. |

## Inundaciones a propósito {#purpose}

Algunas inundaciones son spam: basura enviada a propósito para atascar la
malla. El remitente cambia de nombre, de clave y de ruta, así que ninguna
regla por sí sola frena la inundación.

| Lo que ves | Qué es | Qué ayuda |
| --- | --- | --- |
| Muchos nodos nuevos con nombres aleatorios, cada uno con una clave nueva | Anuncios falsos | `filter rate 04 5 60` deja pasar 5 anuncios por minuto. `filter advert` no sirve: cada anuncio viene de una [clave nueva](#forged). |
| Mensajes con texto ilegible de remitentes inventados, a menudo con fecha de hace más de un año | Spam de canal | `filter malformed on` los descarta en Public. `filter age 60` descarta los de fecha antigua en Public y en los [canales vigilados](/guides/filter/#settings). |
| Hasta 200 mensajes directos por minuto a nodos que no existen, sin acuses de recibo de vuelta | Una inundación de mensajes directos | `filter rate 02 5 60`. Tu app no muestra estos mensajes; un observer sí. |
| Ráfagas de peticiones desde un nodo a decenas de otros | Spam de peticiones | Con `filter on`, el filtro de paquetes deja pasar 5 peticiones por minuto. |
| Un mensaje vuelve 10 a 20 minutos después, con casi la misma ruta | Replay: una copia enviada de nuevo | Un repetidor recuerda los últimos 160 paquetes que ha visto. Por eso, en una malla con mucho tráfico, una copia posterior vuelve a pasar. `filter age` descarta un mensaje de grupo más antiguo de lo que permitas. |
| Mensajes de Public reenviados con un remitente inventado, a veces con una fecha antigua | Spam de eco | `filter age 60`. `filter malformed on` también descarta una fecha con más de una semana de desfase. |
| Un mensaje cada pocos segundos en varios canales, cada uno con un nombre nuevo, con preguntas corrientes | Una oleada de bots | `filter rate 05 10 60`, y [bloquea los canales](/guides/filter/#channel) que no se usan en tu zona. Cada nombre es nuevo, así que las [reglas de remitente](#forged) no lo detectan. |

## Lo que ha funcionado {#worked}

Los grupos locales frenaron inundaciones con estos pasos:

1. **Avisa al dueño.** Una inundación por error se acaba en cuanto su
   dueño lo sabe. Mándale un mensaje amable.
2. **No reacciones en la malla.** Una respuesta le demuestra a un spammer
   que su spam funciona.
3. **Pide observers.** Un observer es un nodo que informa por MQTT de cada
   paquete que oye. Cuantos más observers haya cerca, antes ves por dónde
   entra una inundación. Convierte tu propio repetidor en uno con
   [MQTT en tu observer](/guides/mqtt/).
4. **Encuentra el origen.** Los observers sitúan al remitente en una zona.
   El último kilómetro lo recorren personas a pie con una radio. Consulta
   [Encuentra el origen](#source).
5. **Pon en marcha a tu grupo local.** Un repetidor con los ajustes
   correctos ayuda. Todos los repetidores de la zona juntos frenan una
   inundación. Tu [grupo local](/community/) consigue que cada dueño active
   el ajuste.

## Remitentes y rutas inventados {#forged}

El remitente escribe estas partes de un paquete, y nadie las comprueba:

- **El nombre del remitente.** En un mensaje de canal, el nombre forma
  parte del texto. Cualquiera con la clave del canal puede poner el nombre
  que quiera.
- **El principio de la ruta.** Cada repetidor añade su propio ID al final
  de la ruta. Nadie comprueba los ID que ya estaban, así que un remitente
  puede empezar la ruta con ID inventados. El final de la ruta es real.

{{< forged-path >}}

Por eso `filter sender` y `filter path` solo frenan a un remitente hasta
que cambia de nombre o de ruta. Un [bloqueo de ruta](/guides/filter/#path)
también descarta el tráfico real del repetidor cuyo ID contiene. Los
límites de tasa, los límites de saltos, las comprobaciones de antigüedad y
de mensajes malformados, los bloqueos de canal, las regiones y el ciclo de
trabajo siguen funcionando.

## Ajustes para cualquier inundación {#always}

Estos sirven sea cual sea la inundación:

- **Ciclo de trabajo al 10%.** Así tu repetidor nunca transmite más de lo
  que permite la ley, entre lo que entre. La
  [guía del repetidor](/repeater-guide/#duty-cycle) lo explica.
- **Regiones y límites de saltos.** Una región es la zona en la que se
  queda un mensaje. Un repetidor solo reenvía mensajes de las regiones que
  tiene, y `flood.max.*` mantiene el tráfico cerca. Los dos están en
  [Reduce el tráfico](/guides/settings/#traffic).
- **El filtro de paquetes para un repetidor con mucho tráfico.** Los
  [ajustes predefinidos](/guides/filter/#busy) reducen a la mitad los
  mensajes de grupo y los anuncios. Pruébalos antes en
  [dry-run](/guides/filter/#dryrun): en ese modo solo cuenta lo que
  descartaría.
- **El filtro del companion, en el firmware DMC.** Tu companion, el nodo
  desde el que envías mensajes, mantiene la basura fuera de tu app. Oculta
  los mensajes dañados y antiguos, y los de un repetidor, un remitente o
  una palabra que bloquees. Una regla de remitente o de palabra
  solo te oculta el mensaje a ti; los demás lo siguen recibiendo.

### Control por ciclo de trabajo {#gate}

Con el firmware DMC, tu repetidor puede dar prioridad a su propia región
cuando tiene mucho tráfico. Cuando ha transmitido más del 35% del último
minuto, deja de reenviar mensajes sin región. Si sigue saturado, descarta
después la región más amplia, nivel a nivel. Su propia región siempre
pasa. Solo funciona si has configurado regiones en tu repetidor. Actívalo
y compruébalo:

```text
set dc.gate on
get dc.gate.status
```

{{< dc-gate >}}

Lo que descarta no aparece en `filter stats`. Cuando el repetidor vuelve a
estar tranquilo, las regiones regresan, empezando por la más interior.

## Ver una inundación {#see}

Tu app solo muestra lo que te llega a ti. Una inundación de mensajes
directos a nodos que no existen solo la oye un observer. Cada observer
informa al [MeshCore Analyzer](https://meshcore-analyzer.eu/), donde
cualquiera puede verlo. Convierte tu repetidor en uno con
[MQTT en tu observer](/guides/mqtt/).

En el Analyzer, mira todas las copias de un mismo paquete. Su ruta suele
mostrar de dónde viene. Quien inunda puede empezar la ruta con
[ID inventados](#forged), así que los primeros ID no te dicen nada. Pero
todas las copias llevan el mismo principio inventado. La copia con la ruta
más corta ha pasado por menos repetidores reales, así que se oyó más cerca
del remitente.

{{< copies >}}

En tu propio repetidor, `filter stats` muestra lo que descartó el filtro
de paquetes. `filter stats top` muestra el primer byte de los ID de nodo
que causan más descartes. Muchos nodos comparten ese byte, así que acota
la búsqueda pero no identifica al remitente.

## Encuentra el origen {#source}

Cuando una inundación vuelve una y otra vez:

1. **Sigue las rutas.** Lee una ruta desde el final: los últimos ID son
   los repetidores por los que pasó la inundación. El primer ID real está
   cerca del origen; los ID anteriores pueden ser [inventados](#forged).
2. **Acota la zona.** Varios observers que oyen el mismo paquete sitúan al
   remitente en una zona. El
   [DMC Triangulator](https://triangulator.dutchmeshcore.nl/) la calcula a
   partir de los repetidores que lo oyeron.
3. **Recorre el último kilómetro a pie.** Los repetidores solo oyen el
   origen en el límite de su alcance, así que el último tramo lo hacen
   personas a pie. [Mesh-Hunter](https://mesh-hunter.eu/) se empareja con
   tu companion y registra cada paquete que oye con tu posición GPS. Si
   salen varias personas a la vez, lo encuentran antes.
4. **Avisa a tu [grupo local](/community/).** Ven una parte mayor de la
   malla, deciden qué hacer después y contactan con quien inunda a propósito.

## Cuéntanos lo que viste {#add}

¿Te ha afectado una inundación que no
está en estas tablas? ¿Algún ajuste frenó una? Cuéntanoslo en
[Discord](https://discord.meshcore-info.eu/): lo que viste y lo que
activaste. Lo añadimos a la página.
