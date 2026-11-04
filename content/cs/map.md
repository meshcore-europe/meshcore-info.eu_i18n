---
title: Mapy pokrytí
layout: map
lead: Podívej se, kam mesh dosáhne, kde jsou uzly a jak putují zprávy. Tyto mapy provozují komunity po celé Evropě.
description: Živé mapy MeshCore, mapy pokrytí a analyzátory paketů pro Evropu i jednotlivé země.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '24bfdf6b'
  seeded: '2026-11-04'
  fields: {title: '4b9f20a0', lead: 'fedb89bb', description: 'b5719f82'}
  sections: ['24bfdf6b']
  blocks: ['dd5f039e', '9d4a2ad8', '763fc710', '70c417f2', '9fef7e16']
---

Uzel se na těchto mapách objeví, když ho jeho majitel zveřejní. Nebo když ho
zachytí *observer*: uzel, který přes MQTT přeposílá vše, co slyší. Žádná mapa
proto není úplná. Analyzátory ukazují provoz, který přijímají jejich observery:
pakety, trasy a aktivitu v kanálech. Přímé zprávy zůstávají šifrované. Jejich
obsah tedy žádný analyzátor neukáže.

Uzel je na mapě tam, kam ho umístil majitel. Tato poloha může být chybná nebo
zastaralá. Zpráva typu flood putuje několika cestami najednou. Trasa na mapě je cesta
kopie, která dorazila první. Ostatní kopie se nezaznamenávají.

Vypadá trasa na mapě nepravděpodobně? Prověř 2 její uzly funkcí Line of Sight
v aplikaci MeshCore. Postup ukazuje [návod k repeateru](/repeater-guide/#check-site).

Tyto mapy potřebují internet, mesh ho nepotřebuje. [Proč](/network/)

Provozuješ repeater, tedy uzel, který zprávy předává dál? Nastav mu polohu
pomocí `set lat` a `set lon` a mapy ho dokážou umístit. Jak na to, ukazuje
[návod k repeateru](/repeater-guide/#config).
