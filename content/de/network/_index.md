---
title: Das Netz
layout: network
lead: Sieh dir das Mesh in ganz Europa an und hilf mit, mehr davon sichtbar zu machen. Observer hören das Mesh und melden, was sie empfangen. Jeder neue zeigt ein Stück mehr.
description: 'So wird das MeshCore-Mesh in Europa sichtbar: Observer melden dem MeshCore Analyzer, was sie hören. Live-Zahlen und wie du deinen eigenen Observer hinzufügst.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '90bef266'
  seeded: '2026-10-31'
  fields: {title: '1b32d67c', lead: '382c041f', description: '0dcdc2ac'}
  sections: ['90bef266']
  blocks: ['535ce3c7', 'dee00f8d', '23271f25']
---

Das Mesh selbst speichert nichts: Eine Nachricht wandert von Knoten zu Knoten
und ist dann weg. Was du auf [Abdeckungskarten](/map/) und in Statistiken
siehst, stammt von Observern. Ein Observer ist ein Knoten, der zusätzlich per
MQTT meldet, was er hört. Das läuft über WiFi oder das Internet. Die Meldung
geht nur in eine Richtung: Nichts gelangt zurück ins Mesh. Ein Repeater (ein
Knoten, der Nachrichten weitergibt) mit Observer-Firmware leitet wie bisher
weiter.

Observer in ganz Europa melden an den [MeshCore Analyzer](https://meshcore-analyzer.eu/)
unter mqtt.meshcore-analyzer.eu. Der Analyzer liest auch andere Broker mit.
Ein Observer dort zählt also ebenfalls. Aus diesen Meldungen erstellt der
Analyzer die Karten, die Statistiken und die [Kanalliste](/guides/channels/)
auf dieser Website.

{{< callout type="tip" >}}
Das Mesh braucht nichts davon. Die Tools helfen dir nur, es zu sehen und zu planen. Die Meldungen der Observer, der Analyzer, diese Karten
und Tools laufen über das Internet. Bei einem Stromausfall oder ohne Internet fallen sie aus. Das
Mesh leitet Nachrichten weiterhin per Funk weiter, über jeden Repeater, der noch
Strom hat, etwa die mit Solarstrom.
{{< /callout >}}
