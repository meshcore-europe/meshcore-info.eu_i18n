---
title: Einen Schlüssel erzeugen
layout: keygen
lead: Gib deinem Repeater ein Präfix, das kein Repeater in deiner Nähe nutzt. Such dir ein freies Präfix, erzeuge einen Schlüssel, der damit beginnt, und richte ihn ein.
description: Erzeuge in deinem Browser einen MeshCore-Schlüssel mit einem Präfix deiner Wahl. So teilt kein Repeater in deiner Nähe sein Präfix in einem Pfad mit deinem.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '009b5708'
  seeded: '2026-10-31'
  fields: {title: 'e798fa1b', lead: 'a855fdb1', description: 'e2c1d5de'}
  sections: ['009b5708']
  blocks: ['843e44ff', '2586eaae']
---

Ein Repeater leitet Nachrichten für alle in seiner Umgebung weiter. In einem Pfad
bezeichnet MeshCore jeden Repeater mit den ersten Bytes seines öffentlichen Schlüssels:
seinem Präfix. Hat ein Repeater in deiner Nähe dasselbe Präfix, zeigt ein Pfad nicht,
welcher der beiden eine Nachricht weitergeleitet hat. MeshCore wählt den Schlüssel zufällig.
Hier erzeugst du einen mit dem Präfix deiner Wahl.

Nimm 2 Bytes. Am 13. Oktober 2026 fand der [MeshCore Analyzer](https://meshcore-analyzer.eu/)
in Europa jedes 1-Byte-Präfix mehrfach vergeben. Die Pfad-Hash-Größe ist eine
Einstellung des Absenders. Sie legt fest, wie viele Bytes jedes Präfixes in einen Pfad
kommen. Mehr dazu unter [CLI-Befehle](/guides/cli/).
