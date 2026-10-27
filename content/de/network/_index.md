---
title: Das Netz
layout: network
lead: Sieh das Mesh in ganz Europa, und hilf mit, dass es mehr sieht. Observer hören das Mesh und melden es, und jeder neue zeigt ein Stück mehr.
description: 'Wie das MeshCore-Mesh in Europa sichtbar wird: Observer melden dem MeshCore Analyzer, was sie hören. Live-Zahlen, und wie du deinen eigenen Observer hinzufügst.'
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '05fa5ea3'
  seeded: '2026-10-26'
  fields: {title: '1b32d67c', lead: '382c041f', description: '0dcdc2ac'}
  sections: ['05fa5ea3']
---

Das Mesh selbst führt kein Protokoll: Eine Nachricht geht von Knoten zu Knoten und ist
dann weg. Was du auf den [Abdeckungskarten](/map/) und in den Statistiken siehst, stammt von
Observern. Ein Observer ist ein Knoten, der zusätzlich per MQTT meldet, was er hört,
über WiFi oder das Internet. Die Meldung geht nur in eine Richtung: Nichts kommt zurück ins
Mesh. Ein Repeater (ein Knoten, der Nachrichten weiterreicht) mit Observer-Firmware
repeatet weiter wie zuvor.

Observer in ganz Europa melden an den [MeshCore Analyzer](https://meshcore-analyzer.eu/)
unter mqtt.meshcore-analyzer.eu. Der Analyzer liest auch andere Broker, also zählt ein
Observer dort ebenfalls. Aus diesen Meldungen baut er die Karten, die
Statistiken und die [Kanalliste](/guides/channels/) auf dieser Seite.

{{< callout type="tip" >}}
Das Mesh braucht nichts davon. Die Meldungen der Observer, der Analyzer, diese Karten
und Werkzeuge laufen über das Internet. Bei einem Stromausfall oder wenn das Internet weg ist, stehen sie still. Das
Mesh reicht Nachrichten weiter per Funk, über jeden Repeater, der noch
Strom hat, etwa die mit Solarversorgung. Die Werkzeuge sind dazu da, das Mesh zu sehen und zu planen,
nicht, um es zu betreiben.
{{< /callout >}}
