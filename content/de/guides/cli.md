---
title: CLI-Befehle
layout: cli
lead: Jeder Befehl deines Repeaters, Room-Servers, Sensors oder Companions, geordnet nach dem, was du tun willst. Lies, was er tut und mit welchem Wert er startet, trag deinen eigenen ein und kopiere ihn.
description: 'Jeder Befehl der MeshCore-Firmware 1.18.0 für Repeater, Room-Server, Sensoren und Companions, geordnet nach Aufgabe: was er tut, mit welchem Wert die Firmware startet und welche Knoten ihn haben.'
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '15bdb6eb'
  seeded: '2026-10-26'
  fields: {title: 'a13cc6cb', lead: 'd051d3b4', description: '9a2dae75'}
  sections: ['15bdb6eb']
---

Diese Befehle folgen der MeshCore-Firmware 1.18.0, abgelesen aus dem
Quellcode der Firmware. Bei einem Befehl aus einer neueren Version steht, welche Version er braucht. Ein
Repeater leitet Nachrichten weiter, ein Room-Server speichert Beiträge für eine Gruppe, ein Sensor
meldet Messwerte. Room-Server, Sensoren und Companions haben viele Befehle gemeinsam.
Bei jedem Befehl steht, welche Knoten ihn haben. „Welcher Knoten?" zeigt nur die Befehle
deines Knotens.

Auf einem Repeater, Room-Server oder Sensor tippst du sie über USB von deinem
Computer ein, zum Beispiel in der [seriellen Konsole](/firmware/console/) auf dieser Seite. Die MeshCore-App schickt sie über das Mesh. Die
[Repeater-Anleitung](/repeater-guide/#config) zeigt beides.

Seit 1.18 hat auch ein Companion (der Knoten, von dem du Nachrichten schreibst, gekoppelt mit deinem Handy oder Laptop oder
mit eigenem Bildschirm) eine Befehlszeile.
Öffne dafür Command Line in den Einstellungen der MeshCore-App, Version 1.50 oder
neuer. Ein Kontakt mit der Berechtigung Remote CLI kann deinem Companion dieselben
Befehle über das Mesh schicken. Dazu gehören auch die WiFi- und PIN-Befehle.

Der Wert, mit dem ein Befehl startet, ist der des Repeaters. Ein Room-Server, Sensor oder
Companion kann mit einem anderen Wert starten. Bei einem Befehl, den nur ein Companion hat, steht dessen eigener Wert.
