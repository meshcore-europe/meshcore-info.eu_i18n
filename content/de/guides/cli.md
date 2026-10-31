---
title: CLI-Befehle
layout: cli
lead: Alle Befehle für deinen Repeater, Room Server, Sensor oder Companion, sortiert nach dem, was du vorhast. Lies nach, was ein Befehl tut und mit welchem Wert er startet. Trag deinen eigenen Wert ein und kopiere den Befehl.
description: 'Alle Befehle der MeshCore-Firmware 1.18.0 für Repeater, Room Server, Sensoren und Companions, sortiert nach Aufgabe: was ein Befehl tut, mit welchem Wert die Firmware startet und welche Knoten ihn kennen.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '15bdb6eb'
  seeded: '2026-10-31'
  fields: {title: 'a13cc6cb', lead: 'd051d3b4', description: '9a2dae75'}
  sections: ['15bdb6eb']
  blocks: ['8253bb3c', '66c83d82', '4f1b7c73', 'f28cf8b4']
---

Diese Befehle entsprechen der MeshCore-Firmware 1.18.0 und stammen aus ihrem
Quellcode. Kam ein Befehl erst in einer neueren Version dazu, steht die nötige
Version dabei. Ein Repeater leitet Nachrichten weiter. Ein Room Server speichert
Beiträge für eine Gruppe. Ein Sensor meldet Messwerte. Room Server, Sensoren und
Companions haben viele Befehle gemeinsam. Bei jedem Befehl steht, welche Knoten
ihn kennen. Unter „Welcher Knoten?“ siehst du nur die Befehle für deinen Knoten.

Auf einem Repeater, Room Server oder Sensor gibst du die Befehle über USB an
deinem Computer ein, zum Beispiel in der [seriellen Konsole](/firmware/console/) auf dieser Website. Die MeshCore-App schickt sie über das Mesh. Im
[Repeater-Leitfaden](/repeater-guide/#config) findest du beide Wege.

Seit 1.18 hat auch ein Companion eine Befehlszeile. Der Companion ist der
Knoten, von dem aus du Nachrichten schreibst. Er ist mit deinem Handy oder
Laptop gekoppelt oder hat einen eigenen Bildschirm. Öffne Command Line in den
Einstellungen der MeshCore-App, ab Version 1.50. Ein Kontakt mit der
Berechtigung Remote CLI kann deinem Companion dieselben Befehle über das Mesh
schicken. Dazu gehören auch die Befehle für WiFi und PIN.

Der Startwert eines Befehls ist der Wert des Repeaters. Bei einem Room Server,
Sensor oder Companion kann der Startwert anders sein. Gibt es einen Befehl nur
beim Companion, steht dort sein eigener Startwert.
