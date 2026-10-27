---
title: Nettverket
layout: network
lead: Se mesh-nettet over hele Europa, og hjelp det med å se mer. Observatører hører mesh-nettet og rapporterer det, og hver ny observatør viser litt mer.
description: 'Slik blir MeshCore-mesh-nettet i Europa synlig: observatører rapporterer det de hører til MeshCore Analyzer. Tall i sanntid, og hvordan du legger til din egen observatør.'
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '05fa5ea3'
  seeded: '2026-10-26'
  fields: {title: '1b32d67c', lead: '382c041f', description: '0dcdc2ac'}
  sections: ['05fa5ea3']
---

Mesh-nettet selv lagrer ingenting: en melding går fra node til node og er
borte. Det du ser på [dekningskart](/map/) og i statistikk kommer fra
observatører. En observatør er en node som også rapporterer det den hører over MQTT,
via WiFi eller internett. Rapporten går én vei: ingenting kommer tilbake inn i
mesh-nettet. En repeater (en node som sender meldinger videre) med observatør-firmware fortsetter
å repeatere som før.

Observatører over hele Europa rapporterer til [MeshCore Analyzer](https://meshcore-analyzer.eu/)
på mqtt.meshcore-analyzer.eu. Analyzer leser også andre brokere, så en
observatør der teller også. Ut fra disse rapportene bygger den kartene,
statistikken og [kanallisten](/guides/channels/) på dette nettstedet.

{{< callout type="tip" >}}
Mesh-nettet trenger ikke noe av dette. Rapportene fra observatørene, Analyzer, disse kartene
og verktøyene går over internett. Ved strømbrudd eller når internett er nede, stopper de.
Mesh-nettet fortsetter å sende meldinger videre over radio, gjennom hver repeater som fortsatt har
strøm, for eksempel dem som går på solceller. Verktøyene finnes for å se og planlegge
mesh-nettet, ikke for å drive det.
{{< /callout >}}
