---
title: Paràmetres recomanats
layout: settings
lead: El preset de ràdio de la teva zona i els paràmetres que han canviat els teus veïns. Tria el teu país, configura el preset i copia les ordres.
description: El preset de ràdio de MeshCore per a cada zona d'Europa i els paràmetres de repetidor i companion que els grups locals han canviat respecte dels valors per defecte, amb les ordres.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '0876215b'
  seeded: '2026-11-02'
  fields: {title: 'cfb32983', lead: 'f3f16725', description: 'cb15acd3'}
  sections: ['39848942', 'd1606fcd']
  blocks: ['8c9e88ea', '50ac6063', '85c2203d', '15f91217', 'bdf5fa4e', '69d8e70b', '28f83120', 'fe27027b']
---

Cada zona que trobaràs a continuació fa servir el seu propi preset de ràdio o canvia
alguns valors per defecte de MeshCore. Tot el que no surt a la llista es queda
amb el valor per defecte, així que només has de canviar el que ha canviat la
teva zona. Un repetidor retransmet els missatges per a tothom; un companion és
el node des del qual escrius, vinculat al mòbil o al portàtil per Bluetooth o
USB, o amb pantalla pròpia.

La [guia del repetidor](/repeater-guide/#config) explica com accedir a la
línia d'ordres del teu repetidor, i a la [consola sèrie](/firmware/console/)
d'aquest web hi pots escriure les ordres tu mateix. Sota cada zona també pots
enviar-ne els paràmetres per USB. La guia també indica els
[límits legals](/repeater-guide/#legal) a 868 MHz.

## Mantén el trànsit baix {#traffic}

Aquests paràmetres valen per a totes les zones. Cada repetidor retransmet tots
els missatges flood que capta. Un missatge teu costa una transmissió, més una per
cada repetidor que el capta. Amb el cicle de treball del 10%, un repetidor pot
enviar uns 680 paquets per hora, i tothom qui té al voltant comparteix aquesta
xifra. Un missatge que arriba més lluny del necessari en gasta una part.

**Envia a la regió més petita que arribi a les persones a qui escrius.**
Les regions van encaixades l'una dins de l'altra: un país, una província, un
grup local, cadascun amb el seu codi, com ara `nl`, `nl-ov` i `nl-ov-zwo`. Un
missatge per a `nl-ov-zwo` es queda als repetidors d'aquest grup. Un repetidor
només retransmet les regions que té configurades: tenir `nl` no fa que
retransmeti `nl-ov`. Posa cada repetidor a totes les regions on dona servei, i
només en aquestes; el teu [grup local](/community/) sap quines són.

**Limita el que retransmet el teu repetidor.** Amb dos paràmetres, el trànsit que
no necessita arribar lluny es queda a prop:

```text
set flood.max.advert 3
set flood.max.unscoped 1
```

- `flood.max.advert 3`: els adverts, que anuncien un node a la xarxa mesh, fan
  3 salts com a màxim.
- `flood.max.unscoped 1`: un missatge sense regió passa per un repetidor com a
  màxim.
