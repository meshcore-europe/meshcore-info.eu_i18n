---
title: Ajustes recomendados
layout: settings
lead: El preset de radio que usa tu zona y los ajustes que cambiaron tus vecinos. Elige tu país, configura el preset y copia los comandos.
description: El preset de radio de MeshCore para cada zona de Europa, y los ajustes de repetidor y companion que los grupos locales cambiaron respecto a los valores por defecto, con sus comandos.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '0876215b'
  seeded: '2026-10-31'
  fields: {title: 'cfb32983', lead: 'f3f16725', description: 'cb15acd3'}
  sections: ['39848942', 'd1606fcd']
  blocks: ['8c9e88ea', '50ac6063', '85c2203d', '15f91217', 'bdf5fa4e', '69d8e70b', '28f83120', 'fe27027b']
---

Cada zona que aparece abajo usa su propio preset de radio o cambia algunos valores
por defecto de MeshCore. Todo lo que no aparece se queda con el valor por defecto.
Así solo cambias lo que cambió tu zona. Un repetidor reenvía los mensajes de
todos. Un companion es el nodo desde el que escribes: lo emparejas con tu móvil
o tu portátil por Bluetooth o USB, o lo usas con su propia pantalla.

En la [guía del repetidor](/repeater-guide/#config) ves cómo acceder a la línea
de comandos de tu repetidor. En la [consola serie](/firmware/console/) de este
sitio escribes tú mismo los comandos. En cada zona también puedes enviar sus
ajustes por USB. La guía recoge además los [límites legales](/repeater-guide/#legal)
en 868 MHz.

## Reduce el tráfico {#traffic}

Estos ajustes valen para todas las zonas. Cada repetidor reenvía todos los
mensajes de inundación que oye. Un mensaje tuyo cuesta una transmisión, más una
por cada repetidor que lo oye. Con el ciclo de trabajo del 10%, un repetidor
puede enviar unos 680 paquetes por hora. Todos los que están a su alrededor
comparten esa cifra. Un mensaje que llega más lejos de lo necesario gasta parte
de ella.

**Envía a la región más pequeña que llegue a las personas a las que escribes.**
Las regiones van unas dentro de otras: un país, una provincia, un grupo local.
Cada una tiene su propio código, como `nl`, `nl-ov` y `nl-ov-zwo`. Un mensaje
para `nl-ov-zwo` se queda en los repetidores de ese grupo. Un repetidor solo
reenvía las regiones que tiene asignadas: si tiene `nl`, no reenvía por ello
`nl-ov`. Pon cada repetidor en todas las regiones a las que da servicio, y solo
en esas. Tu [grupo local](/community/) sabe cuáles son.

**Limita lo que reenvía tu repetidor.** Con dos ajustes, el tráfico que no
necesita ir lejos se queda cerca de casa:

```text
set flood.max.advert 3
set flood.max.unscoped 1
```

- `flood.max.advert 3`: los anuncios, que dan a conocer un nodo en la malla,
  viajan como máximo 3 saltos.
- `flood.max.unscoped 1`: un mensaje sin región pasa como máximo por un
  repetidor.
