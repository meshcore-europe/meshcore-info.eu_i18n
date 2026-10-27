---
title: Mitmachen
lead: Freiwillige schreiben, prüfen und übersetzen diese Anleitung. So kannst du helfen, mit oder ohne GitHub-Konto.
description: Trage deine Community, ein Gerät oder ein Projekt ein, prüfe eine Übersetzung oder verbessere eine Anleitung auf meshcore-info.eu.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: 'f3ed6e9b'
  seeded: '2026-10-26'
  fields: {title: '97b0c61b', lead: 'e9b40d4d', description: '3bd97cd2'}
  sections: ['6e9d4b61', 'aca796d7', 'd4848d5b', '247b2601', '8a60e0d4', '645c82d3', 'c755b654']
---

Alles auf dieser Website liegt in einem öffentlichen
[GitHub-Repository](https://github.com/meshcore-europe/meshcore-info.eu). Kleine Änderungen
laufen über ein Formular auf GitHub (ein Issue). Alles Größere kommt als Pull
Request herein: ein Änderungsvorschlag für die Dateien, den ein Maintainer prüft. Ein
Maintainer prüft jede Änderung, bevor sie online geht.

Kein GitHub-Konto? Sag uns auf [Discord](https://discord.meshcore-info.eu/) Bescheid: eine
fehlende Gruppe, ein falscher Fakt oder eine Übersetzung, die sich seltsam liest. Ein Freiwilliger
kümmert sich dann darum.

## Trage deine Community ein {#community}

Du betreibst eine lokale MeshCore-Gruppe, der jeder beitreten kann? Fülle das
[Community-Formular](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-community.yml)
mit Name, Gebiet und den öffentlichen Links aus. Nach der Aufnahme erscheint deine Gruppe
auf der Seite [Lokale Gruppen](/community/) in jeder Sprache.

## Schlage ein Gerät oder ein Projekt vor {#device-project}

Die [Geräteseite](/devices/) listet technische Daten aus der Dokumentation der
Hersteller und verlinkt nie auf Shops. Hardware schlägst du mit dem
[Geräteformular](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-device.yml) vor.
Du hast eine App, ein Tool, eine Bridge oder ein Hardware-Design für MeshCore mit öffentlichem
Quellcode gebaut? Trage es mit dem
[Projektformular](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-project.yml) ein.

## Prüfe eine Übersetzung {#translate}

Seiten in anderen Sprachen beginnen als maschinelle Übersetzungen und sagen das oben
auch. Übersetzungen liegen in einem eigenen Repository,
[meshcore-info.eu_i18n](https://github.com/meshcore-europe/meshcore-info.eu_i18n), du musst
also nie den Code der Website anfassen. Wenn du eine der Sprachen gut
sprichst, kannst du sie verbessern:

1. Öffne die Seite und folge „Hilf mit, diese Übersetzung zu verbessern“. Das öffnet die
   Datei auf GitHub, wo du sie im Browser bearbeiten kannst.
2. Verbessere die Formulierung. Lass Links, Code, Zahlen und Namen wie MeshCore
   genau so, wie sie sind.
3. Ändere im Block `translation` oben `status: ai` zu
   `status: human` und schlage die Änderung vor.

Ein falsches Wort gefunden, aber keine Zeit, es zu beheben? Melde es mit dem
[Übersetzungsformular](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=translation-bug.yml).

## Verbessere eine Anleitung {#guides}

Anleitungen entstehen zuerst auf Englisch und werden von dort übersetzt. Korrekturen
und neue Themen sind willkommen, über das
[Inhaltsformular](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=new-content.yml)
oder einen Pull Request. Fakten brauchen eine Quelle: die MeshCore-Firmware und ihre
Dokumentation, eine Funkregulierungsbehörde oder einen Hersteller. Schreib in deinen eigenen Worten. Ein
kurzes Zitat mit Quellenangabe ist in Ordnung.

Der [Leitfaden für Mitwirkende](https://github.com/meshcore-europe/meshcore-info.eu/blob/main/CONTRIBUTING.md)
erklärt, wie du auf deinem eigenen Rechner an der Website arbeitest.

## Stand der Übersetzungen {#coverage}

„Geprüft“ heißt: von einer Person
kontrolliert; „Maschinell“ heißt: maschinell übersetzt und noch nicht geprüft;
„Veraltet“ heißt: der englische Text hat sich nach der Übersetzung geändert;
„Fehlt“ heißt: die Seite hat noch keine Übersetzung.

{{< coverage >}}

## Danksagung {#credits}

Die Website ist mit [Astro](https://astro.build/) gebaut. Sie nutzt die Schriften
IBM Plex Sans und IBM Plex Mono unter der SIL Open Font License. Übersetzungen
folgen den
Konventionen von [kiekr-i18n](https://github.com/marcelverdult/kiekr-i18n) und
teilen dessen MeshCore-Glossare. MeshCore selbst wird bei
[meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore) entwickelt.

Text und Übersetzungen stehen unter CC BY 4.0, Code unter der MIT-Lizenz.
