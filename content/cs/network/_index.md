---
title: Síť
layout: network
lead: Podívej se na mesh po celé Evropě a pomoz mu ukázat víc. Observery mesh poslouchají a hlásí, co slyší. Každý nový observer ukáže zase o kousek víc.
description: 'Jak se mesh MeshCore v Evropě stává viditelným: observery hlásí, co slyší, do MeshCore Analyzeru. Živá čísla a postup, jak přidat vlastní observer.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '90bef266'
  seeded: '2026-10-31'
  fields: {title: '1b32d67c', lead: '382c041f', description: '0dcdc2ac'}
  sections: ['90bef266']
  blocks: ['535ce3c7', 'dee00f8d', '23271f25']
---

Mesh sám nic nezaznamenává: zpráva projde od uzlu k uzlu a zmizí. To, co
vidíš na [mapách pokrytí](/map/) a ve statistikách, pochází z observerů.
Observer je uzel, který navíc přes MQTT hlásí, co slyší, a to přes Wi-Fi nebo
internet. Hlášení jde jen jedním směrem: do meshe se nic nevrací. Repeater
(uzel, který předává zprávy dál) i s firmwarem observeru opakuje zprávy
stejně jako dřív.

Observery z celé Evropy posílají hlášení do [MeshCore Analyzeru](https://meshcore-analyzer.eu/)
na adrese mqtt.meshcore-analyzer.eu. Analyzer čte i jiné brokery, takže
observer připojený tam se také počítá. Z těchto hlášení Analyzer sestavuje
mapy, statistiky a [seznam kanálů](/guides/channels/) na tomto webu.

{{< callout type="tip" >}}
Mesh nic z toho nepotřebuje. Nástroje ti jen pomáhají ho vidět a plánovat. Hlášení observerů, Analyzer, tyto mapy
a nástroje fungují přes internet. Při výpadku proudu nebo internetu přestanou fungovat. Mesh
dál předává zprávy rádiem přes každý repeater, který má stále napájení,
třeba ty na solární energii.
{{< /callout >}}
