---
title: Axustes recomendados
layout: settings
lead: O preset de radio que usa a túa zona e os axustes que cambiaron os teus veciños. Escolle o teu país, configura o preset e copia os comandos.
description: O preset de radio de MeshCore por zona en Europa e os axustes de repetidor e compañeiro que os grupos locais cambiaron respecto dos valores predeterminados, cos comandos.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '0876215b'
  seeded: '2026-11-02'
  fields: {title: 'cfb32983', lead: 'f3f16725', description: 'cb15acd3'}
  sections: ['39848942', 'd1606fcd']
  blocks: ['8c9e88ea', '50ac6063', '85c2203d', '15f91217', 'bdf5fa4e', '69d8e70b', '28f83120', 'fe27027b']
---

Cada zona de abaixo usa o seu propio preset de radio ou cambia algúns valores
predeterminados de MeshCore. Todo o que non figura aquí queda co valor
predeterminado, así que só cambias o que cambiou a túa zona. Un repetidor
reenvía as mensaxes para todo o mundo; un compañeiro é o nodo desde o que
escribes, vinculado ao teu teléfono ou portátil por Bluetooth ou USB, ou coa súa
propia pantalla.

Na [guía de repetidores](/repeater-guide/#config) ves como acceder á liña de
comandos do teu repetidor, e na [consola serie](/firmware/console/) deste sitio
escribes ti os comandos. Debaixo de cada zona tamén podes enviar os seus axustes
por USB. A guía recolle ademais os [límites legais](/repeater-guide/#legal) en
868 MHz.

## Reduce o tráfico {#traffic}

Estes axustes valen para todas as zonas. Cada repetidor reenvía todas as
mensaxes flood que escoita. Unha mensaxe túa custa unha transmisión, máis outra
por cada repetidor que a escoita. Co ciclo de traballo do 10%, un repetidor pode
enviar uns 680 paquetes por hora, e todo o mundo ao seu redor comparte esa cifra.
Unha mensaxe que chega máis lonxe do necesario gasta parte dela.

**Envía á rexión máis pequena que chegue ás persoas ás que escribes.**
As rexións van unhas dentro doutras: un país, unha provincia, un grupo local,
cada un co seu código, como `nl`, `nl-ov` e `nl-ov-zwo`. Unha mensaxe para
`nl-ov-zwo` queda nos repetidores dese grupo. Un repetidor só reenvía as rexións
que ten configuradas: ter `nl` non fai que reenvíe `nl-ov`. Pon cada repetidor
en todas as rexións ás que dá servizo, e só nesas; o teu
[grupo local](/community/) sabe cales son.

**Limita o que reenvía o teu repetidor.** Con dous axustes, o tráfico que non precisa
viaxar lonxe queda preto da casa:

```text
set flood.max.advert 3
set flood.max.unscoped 1
```

- `flood.max.advert 3`: os anuncios, que presentan un nodo á rede mesh, fan
  como máximo 3 saltos.
- `flood.max.unscoped 1`: unha mensaxe sen rexión pasa como máximo por un
  repetidor.
