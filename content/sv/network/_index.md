---
title: Nätverket
layout: network
lead: Se meshen över hela Europa, och hjälp den att se mer. Observatörer hör meshen och rapporterar den, och varje ny observatör visar lite mer.
description: 'Så blir MeshCore-meshen i Europa synlig: observatörer rapporterar vad de hör till MeshCore Analyzer. Siffror i realtid, och hur du lägger till en egen observatör.'
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '05fa5ea3'
  seeded: '2026-10-26'
  fields: {title: '1b32d67c', lead: '382c041f', description: '0dcdc2ac'}
  sections: ['05fa5ea3']
---

Meshen själv sparar inget: ett meddelande går från nod till nod och är
sedan borta. Det du ser på [täckningskartor](/map/) och i statistiken kommer från
observatörer. En observatör är en nod som dessutom rapporterar vad den hör över MQTT,
via WiFi eller internet. Rapporten går bara en väg: ingenting kommer tillbaka till
meshen. En repeater (en nod som skickar meddelanden vidare) med observatörsfirmware fortsätter
att repetera som förut.

Observatörer runt om i Europa rapporterar till [MeshCore Analyzer](https://meshcore-analyzer.eu/)
på mqtt.meshcore-analyzer.eu. Analyzer läser även andra brokrar, så en
observatör där räknas också. Av rapporterna bygger den kartorna,
statistiken och [kanallistan](/guides/channels/) på den här sidan.

{{< callout type="tip" >}}
Meshen behöver inget av detta. Observatörernas rapporter, Analyzer, kartorna
och verktygen går över internet. Vid ett strömavbrott eller när internet ligger nere stannar de. Meshen
fortsätter att skicka meddelanden via radio, genom varje repeater som fortfarande har
ström, till exempel de som drivs med solceller. Verktygen finns för att se och planera
meshen, inte för att driva den.
{{< /callout >}}
