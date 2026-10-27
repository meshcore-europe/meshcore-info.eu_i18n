---
title: Sériová konzole
layout: console
lead: Posílej příkazy svému repeateru z prohlížeče přes USB.
description: Nastav MeshCore repeater, room server nebo senzor přes USB z Chromu, Edge nebo Opery pomocí sériové konzole v prohlížeči. Nic neinstaluješ.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: 'c33167ce'
  seeded: '2026-10-26'
  fields: {title: '4e3c41fa', lead: 'f0d52063', description: 'a2fe0704'}
  sections: ['c33167ce']
---

Repeater (předává zprávy dál), room server (ukládá příspěvky pro skupinu) ani senzor (hlásí naměřené hodnoty) nemají aplikaci, takže je nastavíš psaním příkazů přes USB. Připoj uzel k počítači, otevři tuto stránku v Chromu, Edge nebo Opeře na počítači a vyber port svého uzlu. Konzole nejdřív pošle `get role` a `ver`, aby věděla, co je tvůj uzel zač. Oba příkazy jen čtou. Potom ukáže, co tvůj uzel odpovídá; napiš příkaz, třeba `get name`, a stiskni Enter. Během psaní ti nabízí příkazy, kterým tvůj uzel rozumí, a Tab doplní ten první.

Companion, tedy uzel, ze kterého píšeš zprávy, komunikuje přes USB s aplikací. Jeho příkazový řádek najdeš v aplikaci MeshCore od verze 1.50.
