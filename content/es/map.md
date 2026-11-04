---
title: Mapas de cobertura
layout: map
lead: Mira hasta dónde llega la malla, dónde están los nodos y por dónde viajan los mensajes. Comunidades de toda Europa mantienen estos mapas.
description: Mapas de MeshCore en directo, mapas de cobertura y analizadores de paquetes para Europa y para cada país.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '24bfdf6b'
  seeded: '2026-11-04'
  fields: {title: '4b9f20a0', lead: 'fedb89bb', description: 'b5719f82'}
  sections: ['24bfdf6b']
  blocks: ['dd5f039e', '9d4a2ad8', '763fc710', '70c417f2', '9fef7e16']
---

Un nodo aparece en estos mapas cuando su dueño lo publica o cuando lo oye un
*observador*: un nodo que reenvía por MQTT lo que oye. Por eso ningún mapa
está completo. Los analizadores muestran el tráfico que reciben sus observadores:
paquetes, rutas y actividad de los canales. Los mensajes directos siguen cifrados,
así que ningún analizador muestra su contenido.

Un nodo aparece en el mapa donde lo colocó su dueño. Esa posición puede ser
errónea o estar desactualizada. Un mensaje por inundación viaja por varias rutas a la vez.
La ruta que ves en un mapa es la de la copia que llegó primero. Las demás no
quedan registradas.

¿Te parece poco probable una ruta en un mapa? Comprueba 2 de sus nodos con Line of Sight
en la app de MeshCore. La [guía del repetidor](/repeater-guide/#check-site) explica cómo hacerlo.

Estos mapas necesitan internet, la malla no. [Por qué](/network/)

¿Tienes un repetidor, un nodo que retransmite mensajes? Fija su posición con `set lat` y `set lon`
y los mapas podrán situarlo. La [guía del repetidor](/repeater-guide/#config) explica cómo.
