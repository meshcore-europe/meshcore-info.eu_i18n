---
title: Serielle Konsole
layout: console
lead: Gib deinem Repeater Befehle über USB, direkt im Browser.
description: Richte einen MeshCore Repeater, Room-Server oder Sensor über USB ein, in Chrome, Edge oder Opera, mit einer seriellen Konsole im Browser und ohne Installation.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'c33167ce'
  seeded: '2026-10-31'
  fields: {title: '4e3c41fa', lead: 'f0d52063', description: '5d53ba06'}
  sections: ['c33167ce']
  blocks: ['13e02e98', '81b697e3']
---

Ein Repeater (er leitet Nachrichten weiter), ein Room-Server (er speichert Beiträge
für eine Gruppe) oder ein Sensor (er meldet Messwerte) hat keine App. Du richtest ihn
deshalb mit Befehlen über USB ein. Schließ deinen Knoten an deinen Computer an. Öffne
diese Seite auf dem Computer in Chrome, Edge oder Opera und wähle den Port deines
Knotens. Die Konsole sendet zuerst `get role` und `ver`, damit sie weiß, was dein
Knoten ist. Beide Befehle lesen nur. Danach siehst du, was dein Knoten ausgibt. Tipp
einen Befehl wie `get name` ein und drück Enter. Beim Tippen schlägt die Konsole die
Befehle vor, die dein Knoten versteht. Mit Tab übernimmst du den ersten Vorschlag.

Ein Companion, also der Knoten, von dem aus du Nachrichten schreibst, spricht stattdessen über USB mit der App. Seine Befehlszeile findest du in der
MeshCore-App ab Version 1.50.
