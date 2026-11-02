---
title: Recommandéiert Astellungen
layout: settings
lead: De Radio-Preset vun denger Géigend an d'Astellungen, déi deng Noperen geännert hunn. Wiel däi Land, setz de Preset a kopéier d'Kommandoen.
description: De MeshCore-Radio-Preset fir all Géigend an Europa, an d'Repeater- a Companion-Astellungen, déi lokal Gruppen am Verglach mat de Standardwäerter geännert hunn, mat de Kommandoen.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '0876215b'
  seeded: '2026-11-02'
  fields: {title: 'cfb32983', lead: 'f3f16725', description: 'cb15acd3'}
  sections: ['39848942', 'd1606fcd']
  blocks: ['8c9e88ea', '50ac6063', '85c2203d', '15f91217', 'bdf5fa4e', '69d8e70b', '28f83120', 'fe27027b']
---

All Géigend hei ënnendrënner benotzt hiren eegene Radio-Preset oder ännert e puer
Standardwäerter vu MeshCore. Alles, wat net opgelëscht ass, bleift um Standardwäert. Du
ännerst also nëmmen dat, wat deng Géigend geännert huet. E Repeater gëtt Messagë fir
jidderee weider. E Companion ass den Node, vun deem aus s du Messagë schécks: du
verbënns en iwwer Bluetooth oder USB mat dengem Handy oder Laptop, oder du benotzt säin
eegene Schierm.

Am [Repeater-Guide](/repeater-guide/#config) gesäis du, wéi s du op d'Kommandozeil vun
dengem Repeater kënns, an an der [serieller Konsol](/firmware/console/) op dëser Säit
tipps du d'Kommandoe selwer an. Ënner all Géigend kanns du hir Astellungen och iwwer USB
schécken. De Guide lëscht och d'[gesetzlech Limitten](/repeater-guide/#legal) op 868 MHz op.

## Haal den Trafic niddreg {#traffic}

Dës Astellunge gëlle fir all Géigend. All Repeater gëtt all Flood-Message weider, déi en
héiert. Eng Message vun dir kascht eng Iwwerdroung, plus eng fir all Repeater, deen se héiert.
Mat engem Duty Cycle vun 10% kann e Repeater ongeféier 680 Paketen an der Stonn
schécken, an all d'Leit ronderëm hien deele sech dës Zuel. Eng Message, déi méi wäit reest
wéi néideg, verbraucht en Deel dovun.

**Schéck un déi klengst Regioun, déi d'Leit erreecht, deene s du schreifs.**
Regioune leien anenee: e Land, eng Provënz, eng lokal Grupp, all mat hirem eegene Code,
wéi `nl`, `nl-ov` an `nl-ov-zwo`. Eng Message fir `nl-ov-zwo` bleift bei de Repeateren
an där Grupp. E Repeater gëtt nëmmen d'Regioune weider, déi e selwer huet: mat `nl`
gëtt en `nl-ov` nach net weider. Setz all Repeater an all Regioun, déi e bedéngt, an
nëmmen an déi. Deng [lokal Grupp](/community/) weess, wéi eng dat sinn.

**Limitéier, wat däi Repeater weidergëtt.** Mat zwou Astellunge bleift Trafic, deen net wäit
muss reesen, an der Géigend:

```text
set flood.max.advert 3
set flood.max.unscoped 1
```

- `flood.max.advert 3`: Adverts, déi en Node am Mesh ukënnegen, reese maximal 3 Hops.
- `flood.max.unscoped 1`: eng Message ouni Regioun geet duerch maximal ee Repeater.
