---
title: Abdeckungskarten
layout: map
lead: Hier siehst du, wie weit das Mesh reicht, wo Knoten stehen und welchen Weg Nachrichten nehmen. Communitys in ganz Europa betreiben diese Karten.
description: Live-Karten, Abdeckungskarten und Paketanalysatoren für MeshCore in Europa und einzelnen Ländern.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '351071aa'
  seeded: '2026-10-31'
  fields: {title: '4b9f20a0', lead: 'fedb89bb', description: 'b5719f82'}
  sections: ['351071aa']
  blocks: ['dd5f039e', '9d4a2ad8', '70c417f2', '9fef7e16']
---

Ein Knoten erscheint auf diesen Karten, wenn sein Besitzer ihn veröffentlicht oder wenn
ein *Observer* ihn hört: ein Knoten, der alles Gehörte per MQTT weiterleitet. Deshalb ist
keine Karte vollständig. Analysatoren zeigen den Verkehr, den ihre Observer empfangen: Pakete,
Routen und Kanalaktivität. Direktnachrichten bleiben verschlüsselt. Ihren Inhalt zeigt
deshalb kein Analysator.

Ein Knoten steht dort auf der Karte, wo sein Besitzer ihn eingetragen hat. Diese Angabe kann falsch
oder veraltet sein. Eine Flood-Nachricht läuft über mehrere Pfade gleichzeitig. Die Route auf einer Karte ist der Pfad
der Kopie, die zuerst ankam. Die anderen Pfade werden nicht erfasst.

Diese Karten brauchen das Internet, das Mesh nicht. [Warum](/network/)

Betreibst du einen Repeater, also einen Knoten, der Nachrichten weitergibt? Trag seine Position mit `set lat` und `set lon` ein. Dann
können Karten ihn einzeichnen. Wie das geht, steht in der [Repeater-Anleitung](/repeater-guide/#config).
