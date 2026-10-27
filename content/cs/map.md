---
title: Mapy pokrytí
layout: map
lead: Podívej se, kam mesh dosahuje, kde jsou uzly a jak zprávy putují. Tyto mapy provozují komunity po celé Evropě.
description: Živé mapy MeshCore, mapy pokrytí a analyzátory paketů pro Evropu i jednotlivé země.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '550066cc'
  seeded: '2026-10-26'
  fields: {title: '4b9f20a0', lead: 'fedb89bb', description: 'b5719f82'}
  sections: ['550066cc']
---

Uzel se na těchto mapách objeví, když ho zveřejní jeho majitel nebo když ho
zaslechne *observer*: uzel, který přeposílá vše, co slyší, přes MQTT. Žádná mapa
proto není úplná. Analyzátory zobrazují provoz, který jejich observery přijmou: pakety,
trasy a aktivitu na kanálech. Přímé zprávy zůstávají šifrované, takže žádný analyzátor
neukáže, co v nich stojí.

Tyto mapy potřebují internet, mesh ne. [Proč](/network/)

Provozuješ repeater, tedy uzel, který zprávy předává dál? Nastav jeho polohu pomocí `set lat` a `set lon` a mapy
ho pak dokážou umístit. Jak na to, ukazuje [návod k repeateru](/repeater-guide/#config).
