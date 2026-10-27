---
title: Empfohlene Einstellungen
layout: settings
lead: Das Funk-Preset deiner Gegend und die Einstellungen, die deine Nachbarn geändert haben. Wähle dein Land, stelle das Preset ein und kopiere die Befehle.
description: Das MeshCore-Funk-Preset pro Gegend in Europa sowie die Repeater- und Companion-Einstellungen, die lokale Gruppen gegenüber den Standardwerten geändert haben, mit den Befehlen.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '9547ba62'
  seeded: '2026-10-26'
  fields: {title: 'cfb32983', lead: 'f3f16725', description: 'cb15acd3'}
  sections: ['39848942', '43cde8b4']
---

Jede Gegend unten nutzt ihr eigenes Funk-Preset oder ändert einige Standardwerte von MeshCore. Alles, was nicht aufgeführt ist, bleibt auf dem Standardwert. Du änderst also nur das, was deine Gegend geändert hat. Ein Repeater leitet Nachrichten für alle weiter. Ein Companion ist der Knoten, von dem aus du schreibst: gekoppelt mit deinem Handy oder Laptop über Bluetooth oder USB, oder mit eigenem Bildschirm.

Die [Repeater-Anleitung](/repeater-guide/#config) zeigt, wie du an die Befehlszeile deines Repeaters kommst. In der [seriellen Konsole](/firmware/console/) auf dieser Seite tippst du Befehle selbst ein. Unter jeder Gegend kannst du ihre Einstellungen außerdem über USB senden. Die Anleitung nennt auch die [gesetzlichen Grenzen](/repeater-guide/#legal) auf 868 MHz.

## Funkverkehr gering halten {#traffic}

Diese Einstellungen gelten für jede Gegend. Jeder Repeater leitet jede Flood-Nachricht weiter, die er hört. Eine Nachricht von dir kostet eine Sendung, plus eine für jeden Repeater, der sie hört. Unter dem Duty Cycle von 10% kann ein Repeater etwa 680 Pakete pro Stunde senden. Alle in seiner Umgebung teilen sich diese Zahl. Eine Nachricht, die weiter reist als nötig, verbraucht einen Teil davon.

**Sende an die kleinste Region, die die Leute erreicht, denen du schreibst.** Regionen sind verschachtelt: ein Land, eine Provinz, eine lokale Gruppe, jede mit eigenem Code, etwa `nl`, `nl-ov` und `nl-ov-zwo`. Eine Nachricht für `nl-ov-zwo` bleibt bei den Repeatern dieser Gruppe. Trage jeden Repeater nur in die Regionen ein, die er versorgt. Deine [lokale Gruppe](/community/) weiß, welche das sind.

**Begrenze, was dein Repeater weiterleitet.** Zwei Einstellungen halten Verkehr, der nicht weit reisen muss, in der Nähe:

```text
set flood.max.advert 3
set flood.max.unscoped 1
```

- `flood.max.advert 3`: Adverts, die einen Knoten im Mesh bekannt machen, reisen höchstens 3 Hops.
- `flood.max.unscoped 1`: Eine Nachricht ohne Region läuft durch höchstens einen Repeater.
