---
title: La red
layout: network
lead: Mira la malla en toda Europa y ayuda a que se vea más. Los observadores escuchan la malla e informan de lo que oyen. Cada observador nuevo muestra un poco más.
description: 'Cómo se hace visible la malla de MeshCore en Europa: los observadores envían lo que oyen al MeshCore Analyzer. Cifras en directo y cómo añadir tu propio observador.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '90bef266'
  seeded: '2026-10-31'
  fields: {title: '1b32d67c', lead: '382c041f', description: '0dcdc2ac'}
  sections: ['90bef266']
  blocks: ['535ce3c7', 'dee00f8d', '23271f25']
---

La malla no guarda ningún registro: un mensaje pasa de nodo en nodo y
desaparece. Lo que ves en los [mapas de cobertura](/map/) y en las estadísticas viene
de los observadores. Un observador es un nodo que además informa de lo que oye por MQTT,
a través de WiFi o de internet. El informe va en un solo sentido: nada vuelve a
la malla. Un repetidor (un nodo que reenvía mensajes) con firmware de observador sigue
reenviando como antes.

Los observadores de toda Europa envían sus informes al [MeshCore Analyzer](https://meshcore-analyzer.eu/)
en mqtt.meshcore-analyzer.eu. El Analyzer también lee otros brokers, así que un
observador conectado a ellos también cuenta. Con esos informes, el Analyzer crea los mapas, las
estadísticas y la [lista de canales](/guides/channels/) de este sitio.

{{< callout type="tip" >}}
La malla no necesita nada de esto. Las herramientas solo te ayudan a verla y planificarla. Los informes de los observadores, el Analyzer, estos mapas
y estas herramientas van por internet. Si hay un apagón o se cae internet, dejan de funcionar. La
malla sigue transmitiendo mensajes por radio, a través de todos los repetidores que aún tienen
corriente, como los que funcionan con energía solar.
{{< /callout >}}
