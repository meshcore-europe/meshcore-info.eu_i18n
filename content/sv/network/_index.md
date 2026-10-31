---
title: Nätet
layout: network
lead: Se meshen över hela Europa och hjälp den att synas mer. Observers hör meshen och rapporterar den, och varje ny observer visar lite mer.
description: 'Så blir MeshCore-meshen i Europa synlig: observers rapporterar det de hör till MeshCore Analyzer. Siffror i realtid, och hur du lägger till en egen observer.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '90bef266'
  seeded: '2026-10-31'
  fields: {title: '1b32d67c', lead: '382c041f', description: '0dcdc2ac'}
  sections: ['90bef266']
  blocks: ['535ce3c7', 'dee00f8d', '23271f25']
---

Meshen sparar ingenting själv: ett meddelande går från nod till nod och är
sedan borta. Det du ser på [täckningskartor](/map/) och i statistiken kommer från
observers. En observer är en nod som också rapporterar det den hör via MQTT,
över WiFi eller internet. Rapporten går bara åt ett håll: ingenting går tillbaka ut i
meshen. En repeater (en nod som skickar meddelanden vidare) med observer-firmware fortsätter
att vidarebefordra som tidigare.

Observers i hela Europa rapporterar till [MeshCore Analyzer](https://meshcore-analyzer.eu/)
på mqtt.meshcore-analyzer.eu. Analyzer läser även andra brokers, så en
observer där räknas också. Utifrån rapporterna bygger Analyzer kartorna,
statistiken och [kanallistan](/guides/channels/) på den här webbplatsen.

{{< callout type="tip" >}}
Meshen behöver inget av detta. Verktygen hjälper dig bara att se och planera den. Rapporterna från observers, Analyzer, de här kartorna
och verktygen går via internet. Vid strömavbrott eller när internet ligger nere slutar de fungera. Meshen
fortsätter att skicka meddelanden via radio, genom alla repeatrar som fortfarande har
ström, till exempel de som drivs med solenergi.
{{< /callout >}}
