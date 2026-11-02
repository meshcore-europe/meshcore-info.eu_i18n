---
title: Consola sèrie
layout: console
lead: Escriu ordres al teu repetidor des del navegador, per USB.
description: Configura un repetidor, un room server o un sensor MeshCore per USB des de Chrome, Edge o Opera, amb una consola sèrie al navegador i sense instal·lar res.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'c33167ce'
  seeded: '2026-11-02'
  fields: {title: '4e3c41fa', lead: 'f0d52063', description: '5d53ba06'}
  sections: ['c33167ce']
  blocks: ['13e02e98', '81b697e3']
---

Un repetidor (retransmet els missatges), un room server (guarda les publicacions d'un
grup) o un sensor (envia lectures) no té aplicació, així que el configures escrivint
ordres per USB. Connecta el node a l'ordinador, obre aquesta pàgina amb
Chrome, Edge o Opera en un ordinador i tria el port del node. Primer, la consola
envia `get role` i `ver` per saber quin node tens. Totes dues ordres només
llegeixen dades. Després, la consola mostra el que diu el node. Escriu una ordre com ara `get name` i
prem Enter. Mentre escrius, la consola et suggereix les ordres que el node entén,
i la tecla Tab completa la primera.

Un companion, el node des del qual envies missatges, es comunica en canvi amb l'aplicació per USB. La línia d'ordres és a
l'aplicació MeshCore, versió 1.50 o posterior.
