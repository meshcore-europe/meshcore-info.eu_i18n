---
title: Abdeckungskarten
layout: map
lead: Sieh, wie weit das Mesh reicht, wo Knoten stehen und wie Nachrichten unterwegs sind. Communities in ganz Europa betreiben diese Karten.
description: Live-Karten, Abdeckungskarten und Paketanalysen für MeshCore in Europa und einzelnen Ländern.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '550066cc'
  seeded: '2026-10-26'
  fields: {title: '4b9f20a0', lead: 'fedb89bb', description: 'b5719f82'}
  sections: ['550066cc']
---

Ein Knoten erscheint auf diesen Karten, wenn sein Besitzer ihn veröffentlicht oder wenn ein *Observer* ihn hört: ein Knoten, der alles Gehörte per MQTT weiterleitet. Keine Karte ist deshalb vollständig. Analysen zeigen den Verkehr, den ihre Observer empfangen: Pakete, Routen und Aktivität auf Kanälen. Direktnachrichten bleiben verschlüsselt, keine Analyse zeigt also ihren Inhalt.

Diese Karten brauchen das Internet, das Mesh nicht. [Warum](/network/)

Betreibst du einen Repeater, einen Knoten, der Nachrichten weitergibt? Lege seine Position mit `set lat` und `set lon` fest, dann können Karten ihn einzeichnen. Wie das geht, zeigt der [Repeater-Leitfaden](/repeater-guide/#config).
