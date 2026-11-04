---
title: Mapas de cobertura
layout: map
lead: Mira ata onde chega a rede mesh, onde están os nodos e como viaxan as mensaxes. Comunidades de toda Europa manteñen estes mapas.
description: Mapas de MeshCore en directo, mapas de cobertura e analizadores de paquetes para Europa e para países concretos.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '24bfdf6b'
  seeded: '2026-11-04'
  fields: {title: '4b9f20a0', lead: 'fedb89bb', description: 'b5719f82'}
  sections: ['24bfdf6b']
  blocks: ['dd5f039e', '9d4a2ad8', '763fc710', '70c417f2', '9fef7e16']
---

Un nodo aparece nestes mapas cando o seu dono o publica ou cando o escoita un
*observador*: un nodo que reenvía por MQTT o que escoita. Por iso ningún mapa
está completo. Os analizadores mostran o tráfico que reciben os seus observadores:
paquetes, rutas e actividade das canles. As mensaxes directas seguen cifradas,
así que ningún analizador mostra o que din.

Un nodo figura no mapa onde o puxo o seu dono, e esa posición pode estar errada
ou desactualizada. Unha mensaxe por inundación (flood) percorre varios camiños á vez. Unha ruta
nun mapa é o camiño da copia que chegou primeiro; os outros non quedan rexistrados.

Unha ruta nun mapa parece pouco probable? Comproba 2 dos seus nodos con Line of Sight
na app de MeshCore. A [guía de repetidores](/repeater-guide/#check-site) explica como facelo.

Estes mapas precisan internet; a rede mesh non. [Por que](/network/)

Tes un repetidor, un nodo que retransmite as mensaxes? Indica a súa posición con `set lat` e `set lon`, e os mapas
poderán situalo. A [guía do repetidor](/repeater-guide/#config) explica como facelo.
