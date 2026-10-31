---
title: Filtro de paquetes
lead: 'Evita que tu repetidor reenvíe basura: inundaciones que llegan de lejos, un bot que nunca para, un canal ruidoso. Prueba primero un ajuste y luego actívalo.'
description: 'El filtro de paquetes del firmware de repetidor DMC: qué descarta, ajustes listos para un repetidor normal y uno con mucho tráfico, cada comando del filtro con su valor por defecto y cómo ver lo que ha descartado.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'b07d39a8'
  seeded: '2026-10-31'
  fields: {title: '20a3ef1f', lead: 'd948682d', description: 'a8c57a9f'}
  sections: ['d06c9ddd', 'b1d9a8d1', '2dd3448d', 'ee64176e', 'a3cb880e', '09b568f0', 'a1a4fb68', '95fe64ae', 'dbac19c3', '05123b18', '3fa1bb28', 'e98b2285']
  blocks: ['b6231504', 'c66e4d9a', 'c0502fb4', 'fa699506', 'f7008037', '3acbb97b', '5e55d14c', 'bd024580', '68c8a4b1', '119fc5b9', '61804e40', '2fa7ebe8', '0610128b', 'a3cb880e', '0e6268be', 'e6d77222', 'f50be141', '2a1ae00c', '095e165f', 'd96efc68', 'b8a89bea', 'a29d0e87', 'c69ba7d1', 'f553d783', '1a83fda3', 'b6f87585', '64e2bbfa', 'dc79ca3a', '6ed9acff', 'd3701ccc', 'd4a25061', '22092611', '9184f977', 'f70c9e55', 'b2f0d9cb', 'c7b214c1', 'e8da9f3e', '0742c6c4', '7f2f59ae', '2789fc6d', 'ae920329', '7dd6f173', 'e1ca9ac7', 'ac11c47b', 'ec7913ae']
---

Un repetidor (un nodo que reenvía mensajes) repite todo lo que oye.
En una malla con mucho tráfico, eso incluye basura. Un bot publica cada minuto.
Un nodo envía su anuncio, el saludo que permite a otros encontrarlo, cada pocos
minutos. Llegan mensajes que han cruzado medio país. Cada repetición quita
tiempo de emisión a todos los que te rodean. Con el filtro de paquetes, tu
repetidor descarta ese tráfico en lugar de reenviarlo. Para saber primero qué
inunda tu malla, y qué ayuda además del filtro, consulta
[Haz la malla más resistente](/guides/resilient/).

{{< callout type="warning" >}}
El filtro de paquetes forma parte del **firmware de repetidor DMC**, la versión
para repetidores de [Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore).
El MeshCore original no tiene filtro de paquetes. Tiene `region denyf *` y
`set flood.max.unscoped`, en la página de [comandos CLI](/guides/cli/). Esta
guía sigue la versión de desarrollo 1.18.0 `ecfb2d4` del 19 de octubre de 2026.
La versión estable 1.17.1 solo tiene los filtros de saltos, frecuencia, canal,
hash y mensajes dañados. Tampoco tiene modo de prueba (dry-run).
{{< /callout >}}

## Qué hace el filtro {#what}

El filtro solo revisa los paquetes que tu repetidor reenvía por inundación
(a todos los nodos a su alcance). Nunca toca lo que envía tu propio repetidor,
ni los paquetes que siguen una ruta conocida hacia un nodo. También pasan los
mensajes directos y las peticiones de y hacia tus propios contactos. Puede
descartar:

- paquetes que ya han pasado por tantos repetidores (saltos) como permites,
  según el tipo de paquete;
- más paquetes de un tipo por minuto de los que permites;
- un anuncio de un nodo que ya se anunció en las últimas horas;
- mensajes de un canal que bloqueas;
- todo lo que llegó a través de un repetidor que bloqueas;
- mensajes de grupo de un remitente o con una palabra, o solo una parte de ellos;
- mensajes de grupo dañados o más antiguos de lo que permites.

El filtro está **desactivado** hasta que lo activas. Lo configuras con comandos.
Escríbelos por USB en la [consola serie](/firmware/console/) de este sitio. O
envíalos desde la app de MeshCore, como en la
[guía del repetidor](/repeater-guide/#config).

## Consigue el firmware {#firmware}

Flashea **DutchMeshCore Repeater** con el flasheador de la
[DutchMeshCore Toolbox](https://toolbox.dutchmeshcore.nl/). El firmware de
observador de [MQTT en tu observador](/guides/mqtt/) tiene el mismo filtro.

## Pruébalo primero {#dryrun}

En modo de prueba, el filtro cuenta cada paquete que descartaría, pero lo sigue
reenviando. Así ajustas una configuración antes de que descarte nada:

```text
filter on
filter dryrun on
```

Mientras el modo de prueba está activo, la línea de estado de `filter` termina
en `(dry-run)`. Los contadores muestran lo que habría descartado. Déjalo
funcionando un día y luego revísalos (consulta [Lo que ha descartado](#stats)).
Cuando las cifras te parezcan correctas, aplícalo:

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

Pasan hasta 20 mensajes de grupo por minuto y hasta 5 mensajes directos por
minuto. Los mensajes de grupo dañados se descartan. La configuración normal del
propio firmware permite 20 mensajes directos por minuto. Esta página usa los 5
que el firmware recomienda desde una inundación de mensajes directos en julio de 2026.

### Un repetidor con mucho tráfico {#busy}

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
documentación del propio firmware también pone `filter hash 2` aquí. Esta
página lo omite (consulta [Todos los ajustes](#settings) para saber por qué).

### Bloquea un canal ruidoso {#channel}

```text
filter channel add #bot
```

Tu repetidor sigue oyendo el canal. Ya no lo reenvía a otros repetidores ni a
los companions (los nodos desde los que la gente envía mensajes). Hasta 16 canales.

### Frena a un remitente {#sender}

Un bot que publica demasiado en un canal que quieres conservar:

```text
filter watch add #test
filter sender add Bob 60
```

Ahora los mensajes de Bob en el canal Public y en `#test` pasan una vez por
minuto. El resto se descarta. El filtro compara el nombre que aparece en el
mensaje, así que un remitente que cambia de nombre lo esquiva.

### Bloquea un repetidor anterior {#path}

Si la basura entra a través de un repetidor, bloquea su prefijo: la primera
parte de su ID, en hexadecimal (hex). Necesitas la versión de desarrollo 1.18.
La 1.17.1 no tiene filtro de ruta.

```text
filter path add a1b2
filter path list
filter stats path
```

`filter path list` muestra los prefijos que bloqueas, y `filter stats path`
cuánto ha descartado cada uno. Con `filter path remove a1b2` vuelve a pasar.
Un prefijo corto como `a1` bloquea también cualquier otro repetidor cuyo ID
empiece por `a1`. Usa el prefijo más largo que puedas. Hasta 8 prefijos.

## Todos los ajustes {#settings}

Los tipos de paquete se indican por número. En el repetidor, `filter types`
muestra los mismos números con los nombres del firmware, como `TXT_MSG` y `GRP_TXT`:

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
| `filter on` / `filter off` | Activa o desactiva el filtro. | desactivado |
| `filter dryrun on` / `off` | Cuenta los descartes, pero lo sigue reenviando todo. | desactivado |
| `filter hops <type> <max>` | Descarta un tipo que ya ha pasado por este número de repetidores, de 0 a 64. | 32 para mensajes de grupo, 8 para el resto |
| `filter rate <type> <limit> <secs> [soft]` | Deja pasar como máximo `limit` de un tipo cada `secs`. Con `soft`, el paso se reduce poco a poco de `soft` a `limit`. `0` desactiva el límite. | 20 cada 60 s para mensajes directos y de grupo, 10 para anuncios, 5 para el resto |
| `filter advert <hours>` | Deja pasar el anuncio de cada nodo una vez cada este número de horas, hasta 720. | 0 (desactivado) |
| `filter channel add <#name>` | Deja de reenviar un canal. | ninguno |
| `filter path add <hex>` | Descarta todo lo que llegó a través de un repetidor con este prefijo, de 2 a 8 dígitos hex. | ninguno |
| `filter sender add <name> [secs] [prob]` | Descarta mensajes de grupo de un remitente, en Public y en los canales vigilados. `Bot*` coincide con cualquier nombre que empiece por Bot. | ninguno |
| `filter text add <word> [secs] [prob]` | Descarta mensajes de grupo que contienen una palabra, en Public y en los canales vigilados. `^word` solo coincide al principio. | ninguno |
| `filter watch add <#name>` | Hace que las reglas de remitente y de texto lean también este canal, hasta 4. Public se lee siempre. | Public |
| `filter malformed on` / `off` | Descarta los mensajes de Public vacíos, dañados o con una fecha desviada más de una semana (la comprobación de fecha espera a que el reloj esté en hora). | desactivado |
| `filter age <minutes>` / `off` | Descarta los mensajes de grupo más antiguos que esto, en Public y en los canales vigilados, de 1 a 10080. | desactivado |
| `filter hash <bytes>` | Descarta los paquetes con un ID de ruta más corto que esto, de 1 a 3. | 1 |
| `filter reset` | Devuelve todos los ajustes a su valor por defecto. | |

Cada `add` tiene su `remove` y su `list`, como `filter channel remove #bot`.
En las reglas de remitente y de texto, `secs` deja pasar un mensaje cada ese
número de segundos. `prob` aplica la regla solo a esa proporción de las
coincidencias, de 1 a 100. Hasta 8 reglas de remitente y 8 de texto. Los nombres
y las palabras distinguen mayúsculas y minúsculas. Un nombre tiene hasta 15
caracteres, y una palabra hasta 23.

Dos ajustes descartan más de lo que quizá esperas:

- `filter hash 2` descarta casi todo el tráfico. Por defecto, los nodos envían
  IDs de ruta de 1 byte.
- `filter age` se fía del reloj de tu repetidor. Ponlo en hora con `clock sync`
  desde la app, compruébalo con `clock` y empieza con un margen amplio: `filter age 60`.

Todos los ajustes se conservan tras un reinicio.

## Lo que ha descartado {#stats}

`filter` muestra los totales por motivo:

```text
> Filter on: Blocked [ Hops: 3 | Rate: 12 | Channel: 1 | Hash: 0 | Malformed: 2 ]
```

`filter stats <topic>` muestra el detalle de un ajuste. Los temas son
`hops`, `rate`, `channel`, `hash`, `malformed`, `advert`, `path`, `sender`,
`text` y `age`. `filter stats top` muestra el primer byte de los IDs de nodo
que causan más descartes. Muchos nodos comparten ese byte.
`filter stats air` muestra el tiempo de emisión que ha ahorrado tu repetidor
al no reenviar estos paquetes.

Los contadores vuelven a 0 tras un reinicio y tras `clear stats`.
