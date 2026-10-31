---
title: Empfohlene Einstellungen
layout: settings
lead: Das Funk-Preset deiner Gegend und die Einstellungen, die deine Nachbarn geändert haben. Wähl dein Land, stell das Preset ein und kopier die Befehle.
description: Das MeshCore-Funk-Preset für jede Gegend in Europa und die Repeater- und Companion-Einstellungen, die lokale Gruppen gegenüber den Standardwerten geändert haben, mit den Befehlen.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '0876215b'
  seeded: '2026-10-31'
  fields: {title: 'cfb32983', lead: 'f3f16725', description: 'cb15acd3'}
  sections: ['39848942', 'd1606fcd']
  blocks: ['8c9e88ea', '50ac6063', '85c2203d', '15f91217', 'bdf5fa4e', '69d8e70b', '28f83120', 'fe27027b']
---

Jede der folgenden Gegenden nutzt ihr eigenes Funk-Preset oder ändert einige
Standardwerte von MeshCore. Alles, was nicht aufgeführt ist, bleibt beim
Standardwert. Du änderst also nur, was deine Gegend geändert hat. Ein Repeater
leitet Nachrichten für alle weiter. Ein Companion ist der Knoten, von dem aus du
schreibst. Du koppelst ihn per Bluetooth oder USB mit deinem Handy oder Laptop,
oder er hat einen eigenen Bildschirm.

Im [Repeater-Leitfaden](/repeater-guide/#config) steht, wie du auf die
Kommandozeile deines Repeaters kommst. In der [seriellen Konsole](/firmware/console/)
auf dieser Website tippst du Befehle selbst ein. Unter jeder Gegend kannst du
ihre Einstellungen auch per USB senden. Der Leitfaden nennt außerdem die
[gesetzlichen Grenzen](/repeater-guide/#legal) auf 868 MHz.

## Datenverkehr gering halten {#traffic}

Diese Einstellungen gelten für jede Gegend. Jeder Repeater leitet jede
Flood-Nachricht weiter, die er empfängt. Eine Nachricht von dir kostet eine
Aussendung, plus eine für jeden Repeater, der sie empfängt. Bei 10 % Duty Cycle
kann ein Repeater etwa 680 Pakete pro Stunde senden. Alle in seiner Umgebung
teilen sich diese Zahl. Eine Nachricht, die weiter reist als nötig, verbraucht
einen Teil davon.

**Sende an die kleinste Region, die deine Empfänger erreicht.**
Regionen sind ineinander verschachtelt: ein Land, eine Provinz, eine lokale
Gruppe. Jede hat einen eigenen Code, etwa `nl`, `nl-ov` und `nl-ov-zwo`. Eine
Nachricht für `nl-ov-zwo` bleibt bei den Repeatern dieser Gruppe. Ein Repeater
leitet nur die Regionen weiter, die er selbst führt. Führt er `nl`, leitet er
deshalb noch kein `nl-ov` weiter. Trag jeden Repeater in jede Region ein, die
er bedient, und nur in diese. Welche das sind, weiß deine
[lokale Gruppe](/community/).

**Begrenze, was dein Repeater weiterleitet.** Mit zwei Einstellungen bleibt
Datenverkehr, der nicht weit reisen muss, in der Nähe:

```text
set flood.max.advert 3
set flood.max.unscoped 1
```

- `flood.max.advert 3`: Adverts, mit denen sich ein Knoten im Mesh bekannt
  macht, reisen höchstens 3 Hops weit.
- `flood.max.unscoped 1`: Eine Nachricht ohne Region läuft höchstens durch
  einen Repeater.
