---
title: Nettverket
layout: network
lead: Se meshen over hele Europa, og hjelp den å se mer. Observatører hører meshen og rapporterer det de hører, og hver ny observatør viser litt mer.
description: 'Slik blir MeshCore-meshen i Europa synlig: observatører rapporterer det de hører til MeshCore Analyzer. Live tall, og slik legger du til din egen observatør.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '90bef266'
  seeded: '2026-10-31'
  fields: {title: '1b32d67c', lead: '382c041f', description: '0dcdc2ac'}
  sections: ['90bef266']
  blocks: ['535ce3c7', 'dee00f8d', '23271f25']
---

Selve meshen lagrer ingenting: en melding går fra node til node og er
borte. Det du ser på [dekningskart](/map/) og i statistikk, kommer fra
observatører. En observatør er en node som også rapporterer det den hører over MQTT,
via Wi-Fi eller internett. Rapporten går bare én vei: ingenting kommer tilbake til
meshen. En repeater (en node som sender meldinger videre) med observatør-firmware fortsetter
å videresende som før.

Observatører over hele Europa rapporterer til [MeshCore Analyzer](https://meshcore-analyzer.eu/)
på mqtt.meshcore-analyzer.eu. Analyzer leser også andre brokere, så en
observatør der teller med. Ut fra disse rapportene lager Analyzer kartene,
statistikken og [kanallisten](/guides/channels/) på dette nettstedet.

{{< callout type="tip" >}}
Meshen trenger ikke noe av dette. Verktøyene hjelper deg bare med å se og planlegge den. Rapportene fra observatørene, Analyzer, disse kartene
og verktøyene går over internett. Ved strømbrudd eller når internett er nede, stopper de. Meshen
fortsetter å sende meldinger videre over radio, gjennom alle repeatere som fortsatt har
strøm, for eksempel de som går på solenergi.
{{< /callout >}}
