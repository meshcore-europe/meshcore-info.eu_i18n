---
title: A rede
layout: network
lead: Contempla a malla en toda Europa e axuda a que se vexa mellor. Os observadores escoitan a malla e informan do que oen, e cada observador novo amosa un pouco máis.
description: 'Como se fai visible a malla de MeshCore en Europa: os observadores envían o que oen ao MeshCore Analyzer. Cifras en directo e como engadir o teu propio observador.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '90bef266'
  seeded: '2026-11-02'
  fields: {title: '1b32d67c', lead: '382c041f', description: '0dcdc2ac'}
  sections: ['90bef266']
  blocks: ['535ce3c7', 'dee00f8d', '23271f25']
---

A propia malla non garda ningún rexistro: unha mensaxe pasa de nodo en nodo e
desaparece. O que ves nos [mapas de cobertura](/map/) e nas estatísticas procede
dos observadores. Un observador é un nodo que tamén informa do que oe por MQTT,
a través da Wi-Fi ou de internet. O informe vai nun só sentido: nada volve á
malla. Un repetidor (un nodo que reenvía mensaxes) con firmware de observador
segue repetindo coma antes.

Observadores de toda Europa envían os informes ao [MeshCore Analyzer](https://meshcore-analyzer.eu/)
en mqtt.meshcore-analyzer.eu. O Analyzer tamén le outros brókers, así que un
observador conectado a eles tamén conta. Con eses informes, o Analyzer crea os mapas, as
estatísticas e a [lista de canles](/guides/channels/) deste sitio.

{{< callout type="tip" >}}
A malla non necesita nada disto: as ferramentas só che axudan a vela e a planificala. Os informes dos observadores, o Analyzer, estes mapas
e estas ferramentas funcionan por internet. Se hai un corte de luz ou cae internet, deixan de funcionar. A
malla segue transmitindo mensaxes por radio, a través de todos os repetidores que aínda teñen
enerxía, como os que funcionan con placas solares.
{{< /callout >}}
