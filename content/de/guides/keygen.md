---
title: Schlüssel erzeugen
layout: keygen
lead: Gib deinem Repeater ein Präfix, das kein Repeater in deiner Nähe nutzt. Finde ein freies Präfix, erzeuge einen Schlüssel, der damit beginnt, und stelle ihn ein.
description: Erzeuge im Browser einen MeshCore-Schlüssel mit einem Präfix deiner Wahl, damit kein Repeater in deiner Nähe im Pfad dasselbe Präfix hat.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '009b5708'
  seeded: '2026-10-26'
  fields: {title: 'e798fa1b', lead: 'a855fdb1', description: 'e2c1d5de'}
  sections: ['009b5708']
---

Ein Repeater leitet Nachrichten für alle in seiner Umgebung weiter. Im Pfad
benennt MeshCore jeden Repeater mit den ersten Bytes seines öffentlichen Schlüssels:
seinem Präfix. Hat ein Repeater in deiner Nähe dasselbe Präfix, zeigt der Pfad nicht,
welcher der beiden eine Nachricht weitergeleitet hat. MeshCore wählt den Schlüssel
zufällig. Hier erzeugst du einen mit dem Präfix, das du willst.

Nimm 2 Bytes. Am 13. Oktober 2026 sah der [MeshCore Analyzer](https://meshcore-analyzer.eu/)
in Europa jedes 1-Byte-Präfix mehrfach vergeben. Wie viele Bytes jedes Präfixes in einen Pfad
eingehen, bestimmt die Path-Hash-Größe, eine Einstellung des Senders; siehe [CLI-Befehle](/guides/cli/).
