---
title: Síť
layout: network
lead: Podívej se na mesh po celé Evropě a pomoz mu vidět víc. Observery mesh poslouchají a hlásí, co slyší, a každý nový ukáže o kousek víc.
description: 'Jak se mesh MeshCore v Evropě stává viditelným: observery hlásí, co slyší, do MeshCore Analyzeru. Živá čísla a návod, jak přidat vlastní observer.'
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '05fa5ea3'
  seeded: '2026-10-26'
  fields: {title: '1b32d67c', lead: '382c041f', description: '0dcdc2ac'}
  sections: ['05fa5ea3']
---

Mesh sám si nic nepamatuje: zpráva projde od uzlu k uzlu a je pryč. To, co
vidíš na [mapách pokrytí](/map/) a ve statistikách, pochází od observerů.
Observer je uzel, který navíc hlásí přes MQTT, co slyší, a to přes Wi-Fi nebo
internet. Hlášení jde jen jedním směrem: do meshe se nic nevrací. Repeater
(uzel, který zprávy předává dál) s firmwarem observeru předává zprávy dál
stejně jako předtím.

Observery po celé Evropě hlásí do [MeshCore Analyzeru](https://meshcore-analyzer.eu/)
na adrese mqtt.meshcore-analyzer.eu. Analyzer čte i jiné brokery, takže se
počítá i observer, který hlásí tam. Z těchto hlášení Analyzer sestavuje mapy,
statistiky a [seznam kanálů](/guides/channels/) na tomto webu.

{{< callout type="tip" >}}
Mesh nic z toho nepotřebuje. Hlášení observerů, Analyzer, tyto mapy
a nástroje běží přes internet. Při výpadku proudu nebo internetu se zastaví. Mesh
předává zprávy dál rádiem, přes každý repeater, který má ještě napájení,
třeba ty na solární energii. Nástroje slouží k tomu, abys mesh viděl a mohl ho
plánovat, ne k jeho provozu.
{{< /callout >}}
