---
title: Ajustes recomendados
layout: settings
lead: El preajuste de radio que usa tu zona y los ajustes que tus vecinos han cambiado. Elige tu país, configura el preajuste y copia los comandos.
description: El preajuste de radio de MeshCore por zona en Europa, y los ajustes de repetidor y companion que los grupos locales han cambiado respecto a los valores por defecto, con los comandos.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '9547ba62'
  seeded: '2026-10-26'
  fields: {title: 'cfb32983', lead: 'f3f16725', description: 'cb15acd3'}
  sections: ['39848942', '43cde8b4']
---

Cada zona de abajo usa su propio preajuste de radio, o cambia algunos valores por defecto de MeshCore. Todo lo que no aparece sigue en su valor por defecto, así que solo cambias lo que cambió tu zona. Un repetidor reenvía los mensajes para todos; un companion es el nodo desde el que escribes, emparejado con tu teléfono o portátil por Bluetooth o USB, o con su propia pantalla.

En la [guía del repetidor](/repeater-guide/#config) ves cómo llegar a la línea de comandos de tu repetidor, y en la [consola serie](/firmware/console/) de este sitio escribes los comandos tú mismo. Debajo de cada zona también puedes enviar sus ajustes por USB. La guía recoge además los [límites legales](/repeater-guide/#legal) en 868 MHz.

## Reduce el tráfico {#traffic}

Estos ajustes valen para todas las zonas. Cada repetidor reenvía todo mensaje de inundación que oye. Un mensaje tuyo cuesta una transmisión, más una por cada repetidor que lo oye. Con el ciclo de trabajo del 10% un repetidor puede enviar unos 680 paquetes por hora, y todos los que están a su alrededor comparten esa cifra. Un mensaje que viaja más lejos de lo necesario gasta parte de ella.

**Envía a la región más pequeña que alcance a las personas a las que escribes.** Las regiones se anidan: un país, una provincia, un grupo local, cada uno con su propio código, como `nl`, `nl-ov` y `nl-ov-zwo`. Un mensaje para `nl-ov-zwo` se queda en los repetidores de ese grupo. Pon cada repetidor solo en las regiones a las que sirve; tu [grupo local](/community/) sabe cuáles son.

**Limita lo que reenvía tu repetidor.** Dos ajustes mantienen cerca de casa el tráfico que no necesita viajar lejos:

```text
set flood.max.advert 3
set flood.max.unscoped 1
```

- `flood.max.advert 3`: los anuncios, que dan a conocer un nodo a la malla, viajan como máximo 3 saltos.
- `flood.max.unscoped 1`: un mensaje sin región pasa como máximo por un repetidor.
