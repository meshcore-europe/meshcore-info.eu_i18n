---
title: Sériová konzola
layout: console
lead: Zadávaj príkazy svojmu repeateru cez USB priamo z prehliadača.
description: Nastav MeshCore repeater, room server alebo senzor cez USB v prehliadači Chrome, Edge alebo Opera. Sériová konzola beží v prehliadači a nič neinštaluješ.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'c33167ce'
  seeded: '2026-11-02'
  fields: {title: '4e3c41fa', lead: 'f0d52063', description: '5d53ba06'}
  sections: ['c33167ce']
  blocks: ['13e02e98', '81b697e3']
---

Repeater (preposiela správy), room server (ukladá príspevky pre skupinu) ani senzor (hlási namerané hodnoty) nemá aplikáciu, preto ho nastavuješ písaním príkazov cez USB. Pripoj uzol k počítaču, otvor túto stránku v prehliadači Chrome, Edge alebo Opera na počítači a vyber port uzla. Konzola najprv odošle `get role` a `ver`, aby zistila, o aký uzol ide. Oba príkazy údaje iba čítajú. Potom konzola zobrazí, čo uzol vypisuje. Napíš príkaz, napríklad `get name`, a stlač Enter. Počas písania ti konzola navrhuje príkazy, ktorým tvoj uzol rozumie, a klávesom Tab doplníš prvý z nich.

Companion, teda uzol, z ktorého posielaš správy, namiesto toho komunikuje cez USB s aplikáciou. Jeho príkazový riadok nájdeš v aplikácii MeshCore verzie 1.50 alebo novšej.
