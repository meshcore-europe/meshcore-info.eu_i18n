---
title: Filtro de paquetes
lead: 'Evita que tu repetidor reenvíe basura: inundaciones desde muy lejos, un bot que no para, un canal ruidoso. Prueba primero un ajuste y luego actívalo.'
description: 'El filtro de paquetes del firmware de repetidor DMC: qué descarta, ajustes listos para un repetidor normal y uno saturado, cada comando del filtro con su valor por defecto, y cómo ver lo que ha descartado.'
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '2bf23d24'
  seeded: '2026-10-26'
  fields: {title: '20a3ef1f', lead: 'd948682d', description: 'a8c57a9f'}
  sections: ['0625daa2', 'b1d9a8d1', '2dd3448d', 'ee64176e', 'a3cb880e', '09b568f0', 'a1a4fb68', '95fe64ae', 'dbac19c3', 'ffc3f3a0', '3fa1bb28', '09511608']
---

Un repetidor (un nodo que reenvía mensajes) repite todo lo que oye.
En una malla con mucho tráfico, eso incluye basura. Un bot publica cada minuto.
Un nodo envía su anuncio, el saludo que permite a otros encontrarlo, cada pocos
minutos. Llegan mensajes que han cruzado medio país. Cada repetición quita
tiempo de aire a todos los que te rodean. Con el filtro de paquetes, tu
repetidor descarta ese tráfico en lugar de reenviarlo.

{{< callout type="warning" >}}
El filtro de paquetes forma parte del **firmware de repetidor DMC**, la
versión para repetidores de [Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore).
El MeshCore estándar no tiene filtro de paquetes; tiene `region denyf *` y
`set flood.max.unscoped`, en la página de [comandos CLI](/guides/cli/). Esta
guía sigue la versión de desarrollo 1.18.0 `ecfb2d4` del 19 de octubre de
2026. La versión estable 1.17.1 solo tiene los filtros de saltos, tasa, canal,
hash y malformados. Tampoco tiene modo de prueba (dry-run).
{{< /callout >}}

## Qué hace el filtro {#what}

El filtro solo mira los paquetes que tu repetidor reenvía por inundación
(enviándolos a todos los nodos al alcance). Nunca toca lo que tu repetidor
envía por su cuenta, ni los paquetes que siguen una ruta conocida hacia un
nodo. Los mensajes directos y las peticiones hacia y desde tus propios
contactos también pasan. Puede descartar:

- paquetes que ya han pasado por tantos repetidores (saltos) como permites,
  por tipo de paquete;
- más paquetes de un tipo de los que permites por minuto;
- un anuncio de un nodo que ya se anunció en las últimas horas;
- mensajes en un canal que bloqueas;
- todo lo que llegó a través de un repetidor que bloqueas;
- mensajes de grupo de un remitente o con una palabra, o solo parte de ellos;
- mensajes de grupo rotos, o más antiguos de lo que permites.

El filtro está **desactivado** hasta que lo activas. Lo configuras con
comandos. Escríbelos por USB en la [consola serie](/firmware/console/) de este
sitio. O envíalos desde la app de MeshCore, como en la
[guía del repetidor](/repeater-guide/#config).

## Consigue el firmware {#firmware}

Flashea **DutchMeshCore Repeater** desde el flasher de la
[DutchMeshCore Toolbox](https://toolbox.dutchmeshcore.nl/). El firmware de
observador de [MQTT en tu observador](/guides/mqtt/) tiene el mismo filtro.

## Pruébalo primero {#dryrun}

En modo de prueba, el filtro cuenta cada paquete que descartaría, pero lo
reenvía igualmente. Así puedes ajustar un valor antes de que descarte nada:

```text
filter on
filter dryrun on
```

Mientras el modo de prueba está activo, la línea de estado de `filter`
termina en `(dry-run)`. Los contadores muestran lo que habría descartado.
Déjalo funcionar un día y luego míralos (consulta [Qué ha descartado](#stats)).
Cuando los números te parezcan correctos, aplícalo:

```text
filter dryrun off
```

## Configuraciones recomendadas {#configs}

### Un repetidor normal {#typical}

```text
filter on
filter malformed on
filter rate 05 20 60
filter rate 02 5 60
filter hops 05 32
```

Los mensajes de grupo pasan hasta 20 por minuto, los mensajes directos hasta
5 por minuto, y los mensajes de grupo rotos se descartan. La configuración
normal del propio firmware permite 20 mensajes directos por minuto. Esta
página toma los 5 que recomienda desde una inundación de mensajes directos en
julio de 2026.

### Un repetidor saturado {#busy}

Para un repetidor en un sitio alto que oye toda una región, o uno que sufre
una inundación:

```text
filter on
filter malformed on
filter rate 05 10 60
filter rate 02 5 60
filter rate 04 5 60
filter advert 24
filter hops 05 16
filter hops 02 16
filter hops 04 8
```

Esto reduce a la mitad los mensajes de grupo y los anuncios, y deja pasar el
anuncio de cada nodo una vez al día. Descarta los mensajes que ya han pasado
por 16 repetidores. Tras un reinicio, cada nodo consigue pasar un anuncio. La
documentación del propio firmware añade aquí `filter hash 2`; esta página lo
deja fuera (en [Cada ajuste](#settings) explicamos por qué).

### Bloquea un canal ruidoso {#channel}

```text
filter channel add #bot
```

Tu repetidor sigue oyendo el canal. Ya no lo reenvía a otros repetidores ni a
los companions (los nodos desde los que la gente escribe). Hasta 16 canales.

### Frena a un remitente {#sender}

Un bot que publica demasiado a menudo en un canal que quieres conservar:

```text
filter watch add #test
filter sender add Bob 60
```

Los mensajes de Bob en el canal Public y en `#test` ahora pasan una vez por
minuto; el resto se descarta. El filtro compara el nombre que va en el
mensaje, así que un remitente que se cambia el nombre se lo salta.

### Bloquea un repetidor aguas arriba {#path}

Cuando la basura entra por un repetidor concreto, bloquea su prefijo: la
primera parte de su ID, en hexadecimal (hex).

```text
filter path add a1b2
```

Un prefijo corto como `a1` también bloquea a cualquier otro repetidor cuyo ID
empiece por `a1`. Usa el prefijo más largo que puedas. Hasta 8 prefijos.

## Cada ajuste {#settings}

Los tipos de paquete se indican con un número. En el repetidor, `filter types`
muestra los mismos números con los nombres del firmware, como `TXT_MSG` y
`GRP_TXT`:

| Número | Tipo | Número | Tipo |
| --- | --- | --- | --- |
| `00` | petición | `06` | datos de grupo |
| `01` | respuesta | `07` | petición anónima |
| `02` | mensaje directo | `08` | ruta |
| `03` | confirmación | `09` | traza |
| `04` | anuncio | `10` | multiparte |
| `05` | mensaje de grupo | `11` | control |

| Comando | Qué hace | Valor inicial |
| --- | --- | --- |
| `filter on` / `filter off` | Activa o desactiva el filtro. | off |
| `filter dryrun on` / `off` | Cuenta los descartes pero reenvía todo igualmente. | off |
| `filter hops <type> <max>` | Descarta un tipo que ya ha pasado por este número de repetidores, de 0 a 64. | 32 para mensajes de grupo, 8 para el resto |
| `filter rate <type> <limit> <secs> [soft]` | Deja pasar como máximo `limit` de un tipo por cada `secs`. Con `soft`, el paso se reduce gradualmente desde `soft` hasta `limit`. `0` desactiva el límite. | 20 por 60 s para mensajes directos y de grupo, 10 para anuncios, 5 para el resto |
| `filter advert <hours>` | Deja pasar el anuncio de cada nodo una vez por este número de horas, hasta 720. | 0 (off) |
| `filter channel add <#name>` | Deja de reenviar un canal. | ninguno |
| `filter path add <hex>` | Descarta todo lo que llegó a través de un repetidor con este prefijo, de 2 a 8 dígitos hex. | ninguno |
| `filter sender add <name> [secs] [prob]` | Descarta mensajes de grupo de un remitente, en Public y en los canales vigilados. `Bot*` coincide con cualquier nombre que empiece por Bot. | ninguno |
| `filter text add <word> [secs] [prob]` | Descarta mensajes de grupo que contienen una palabra, en Public y en los canales vigilados. `^word` solo coincide al principio. | ninguno |
| `filter watch add <#name>` | Hace que las reglas de remitente y texto lean también este canal, hasta 4. Public siempre se lee. | Public |
| `filter malformed on` / `off` | Descarta mensajes de Public vacíos, rotos o con una fecha que se desvía más de una semana (la comprobación de fecha espera hasta que el reloj está ajustado). | off |
| `filter age <minutes>` / `off` | Descarta mensajes de grupo más antiguos que esto, en Public y en los canales vigilados, de 1 a 10080. | off |
| `filter hash <bytes>` | Descarta paquetes con un ID de ruta más corto que esto, de 1 a 3. | 1 |
| `filter reset` | Devuelve cada ajuste a su valor por defecto. | |

Cada `add` tiene su `remove` y su `list`, como `filter channel remove #bot`.
En las reglas de remitente y texto, `secs` deja pasar un mensaje por cada
tantos segundos. `prob` aplica la regla solo a esa proporción de las
coincidencias, de 1 a 100. Hasta 8 reglas de remitente y 8 de texto. Los
nombres y las palabras distinguen mayúsculas y minúsculas; un nombre tiene
hasta 15 caracteres, una palabra hasta 23.

Dos ajustes descartan más de lo que quizá esperas:

- `filter hash 2` descarta casi todo el tráfico. Los nodos envían IDs de ruta
  de 1 byte por defecto.
- `filter age` confía en el reloj de tu repetidor. Ajústalo con `clock sync`
  desde la app, compruébalo con `clock` y empieza con margen: `filter age 60`.

Cada ajuste se conserva tras un reinicio.

## Qué ha descartado {#stats}

`filter` muestra los totales por motivo:

```text
> Filter on: Blocked [ Hops: 3 | Rate: 12 | Channel: 1 | Hash: 0 | Malformed: 2 ]
```

`filter stats <topic>` muestra el detalle de un ajuste. Los temas son
`hops`, `rate`, `channel`, `hash`, `malformed`, `advert`, `path`, `sender`,
`text` y `age`. `filter stats top` muestra el primer byte de los IDs de nodo
que acumulan más descartes, una pista más que una prueba.
`filter stats air` muestra el tiempo de aire que tu repetidor ahorró al no
reenviar estos paquetes.

Los contadores vuelven a 0 tras un reinicio y tras `clear stats`.
