---
title: Mapas de cobertura
layout: map
lead: Mira hasta dónde llega la malla, dónde están los nodos y cómo viajan los mensajes. Comunidades de toda Europa mantienen estos mapas.
description: Mapas MeshCore en directo, mapas de cobertura y analizadores de paquetes para Europa y países concretos.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '550066cc'
  seeded: '2026-10-26'
  fields: {title: '4b9f20a0', lead: 'fedb89bb', description: 'b5719f82'}
  sections: ['550066cc']
---

Un nodo aparece en estos mapas cuando su dueño lo publica, o cuando un
*observador* lo escucha: un nodo que reenvía por MQTT lo que oye. Por eso
ningún mapa está completo. Los analizadores muestran el tráfico que reciben sus
observadores: paquetes, rutas y actividad de los canales. Los mensajes directos
siguen cifrados, así que ningún analizador muestra lo que dicen.

Estos mapas necesitan internet; la malla no. [Por qué](/network/)

¿Tienes un repetidor, un nodo que reenvía los mensajes? Fija su posición con `set lat` y `set lon`, y los mapas
podrán situarlo. La [guía del repetidor](/repeater-guide/#config) explica cómo hacerlo.
