---
title: La red
layout: network
lead: Mira la malla en toda Europa y ayúdala a ver más. Los observadores escuchan la malla y la reportan, y cada observador nuevo muestra un poco más.
description: 'Cómo se hace visible la malla MeshCore en Europa: los observadores reportan lo que escuchan al MeshCore Analyzer. Cifras en vivo y cómo añadir tu propio observador.'
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '05fa5ea3'
  seeded: '2026-10-26'
  fields: {title: '1b32d67c', lead: '382c041f', description: '0dcdc2ac'}
  sections: ['05fa5ea3']
---

La malla no guarda ningún registro: un mensaje pasa de nodo a nodo y
desaparece. Lo que ves en los [mapas de cobertura](/map/) y en las estadísticas
viene de los observadores. Un observador es un nodo que además reporta lo que
escucha por MQTT, a través de Wi-Fi o de internet. El reporte va en un solo
sentido: nada vuelve a la malla. Un repetidor (un nodo que reenvía mensajes) con
firmware de observador sigue repitiendo como antes.

Los observadores de toda Europa reportan al [MeshCore Analyzer](https://meshcore-analyzer.eu/)
en mqtt.meshcore-analyzer.eu. El Analyzer también lee otros brokers, así que un
observador conectado a ellos cuenta igual. Con esos reportes construye los mapas, las
estadísticas y la [lista de canales](/guides/channels/) de este sitio.

{{< callout type="tip" >}}
La malla no necesita nada de esto. Los reportes de los observadores, el Analyzer, estos mapas
y herramientas funcionan por internet. En un apagón o cuando internet se cae, se detienen. La
malla sigue pasando mensajes por radio, a través de cada repetidor que aún tiene
energía, como los que funcionan con energía solar. Las herramientas sirven para ver y planificar la
malla, no para hacerla funcionar.
{{< /callout >}}
