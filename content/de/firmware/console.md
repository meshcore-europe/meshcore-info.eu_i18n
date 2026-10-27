---
title: Serielle Konsole
layout: console
lead: Gib deinem Repeater Befehle aus dem Browser, über USB.
description: Richte einen MeshCore-Repeater, Room-Server oder Sensor über USB aus Chrome, Edge oder Opera ein, mit einer seriellen Konsole im Browser. Kein Programm zu installieren.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: 'c33167ce'
  seeded: '2026-10-26'
  fields: {title: '4e3c41fa', lead: 'f0d52063', description: 'a2fe0704'}
  sections: ['c33167ce']
---

Ein Repeater (er leitet Nachrichten weiter), ein Room-Server (er speichert Beiträge für eine Gruppe) oder ein Sensor (er meldet Messwerte) hat keine App. Du richtest ihn deshalb ein, indem du Befehle über USB eingibst. Schließ deinen Knoten an deinen Computer an, öffne diese Seite in Chrome, Edge oder Opera auf einem Computer und wähl den Port deines Knotens. Die Konsole sendet zuerst `get role` und `ver`, damit sie weiß, was dein Knoten ist. Beide lesen nur. Danach zeigt sie, was dein Knoten antwortet. Gib einen Befehl wie `get name` ein und drück Enter. Während du tippst, schlägt sie die Befehle vor, die dein Knoten versteht, und mit Tab übernimmst du den ersten.

Ein Companion, der Knoten, von dem aus du Nachrichten schreibst, spricht stattdessen über USB mit der App. Seine Befehlszeile findest du in der MeshCore-App ab Version 1.50.
