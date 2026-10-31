---
title: Sériová konzole
layout: console
lead: Zadávej příkazy svému repeateru z prohlížeče přes USB.
description: Nastav MeshCore repeater, room server nebo senzor přes USB z Chrome, Edge nebo Opery. Sériová konzole běží v prohlížeči a nic neinstaluješ.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'c33167ce'
  seeded: '2026-10-31'
  fields: {title: '4e3c41fa', lead: 'f0d52063', description: '5d53ba06'}
  sections: ['c33167ce']
  blocks: ['13e02e98', '81b697e3']
---

Repeater (předává zprávy dál), room server (ukládá příspěvky pro skupinu) nebo
senzor (posílá naměřené hodnoty) nemá aplikaci. Nastavuješ ho proto příkazy
přes USB. Připoj uzel k počítači a otevři tuto stránku v Chrome, Edge nebo
Opeře na počítači. Pak vyber port svého uzlu. Konzole nejdřív pošle `get role`
a `ver`, aby věděla, o jaký uzel jde. Oba příkazy jen čtou. Potom konzole
zobrazuje, co tvůj uzel vypisuje. Napiš příkaz, třeba `get name`, a stiskni
Enter. Během psaní ti konzole nabízí příkazy, kterým tvůj uzel rozumí. Klávesou
Tab doplníš první z nich.

Companion je uzel, ze kterého posíláš zprávy. Ten místo toho komunikuje přes
USB s aplikací. Jeho příkazový řádek najdeš v aplikaci MeshCore od verze 1.50.
