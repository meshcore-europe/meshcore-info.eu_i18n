---
title: Mitmachen
lead: Freiwillige schreiben, prüfen und übersetzen diesen Leitfaden. Hier erfährst du, wie du helfen kannst, mit oder ohne GitHub-Konto.
description: Trag deine Community, ein Gerät oder ein Projekt ein, prüf eine Übersetzung oder verbessere einen Leitfaden auf meshcore-info.eu.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'f3ed6e9b'
  seeded: '2026-10-31'
  fields: {title: '97b0c61b', lead: 'e9b40d4d', description: '3bd97cd2'}
  sections: ['6e9d4b61', 'aca796d7', 'd4848d5b', '247b2601', '8a60e0d4', '645c82d3', 'c755b654']
  blocks: ['2f9dd6e8', '44167907', 'b020e1a4', 'f2c726cd', '2e9d1fdd', 'b2a902ba', 'b15ce10b', '2be86888', '3db6cb63', '2e3c2fc0', '693a5d9d', '73e33897', '96d8689d', 'c67fd14a', 'f92f7e49', '12ddca6c', 'e947e2a9', '526df4bb', 'e0d3559e']
---

Alles auf dieser Website liegt in einem öffentlichen
[GitHub-Repository](https://github.com/meshcore-europe/meshcore-info.eu). Kleine Änderungen
reichst du über ein Formular auf GitHub ein (ein Issue). Größere Änderungen reichst du als Pull
Request ein: ein Änderungsvorschlag für die Dateien, den ein Maintainer prüft. Ein
Maintainer prüft jede Änderung, bevor sie online geht.

Du hast kein GitHub-Konto? Sag uns auf [Discord](https://discord.meshcore-info.eu/) Bescheid: eine
fehlende Gruppe, eine falsche Angabe oder eine Übersetzung, die seltsam klingt. Ein Freiwilliger
kümmert sich dann darum.

## Deine Community eintragen {#community}

Du leitest eine lokale MeshCore-Gruppe, der jeder beitreten kann? Füll das
[Community-Formular](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-community.yml)
mit dem Namen, dem Gebiet und den öffentlichen Links aus. Nach der Aufnahme erscheint deine Gruppe
in jeder Sprache auf der Seite [Lokale Gruppen](/community/).

## Ein Gerät oder ein Projekt vorschlagen {#device-project}

Die [Geräteseite](/devices/) listet technische Daten aus den Unterlagen der Hersteller
und verlinkt nie auf Shops. Hardware schlägst du über das
[Geräteformular](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-device.yml) vor.
Du hast eine App, ein Tool, eine Bridge oder ein Hardware-Design für MeshCore mit öffentlichem Quellcode gebaut?
Trag es über das
[Projektformular](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-project.yml) ein.

## Eine Übersetzung prüfen {#translate}

Seiten in anderen Sprachen sind zuerst maschinell übersetzt und weisen oben darauf hin.
Die Übersetzungen liegen in einem eigenen Repository,
[meshcore-info.eu_i18n](https://github.com/meshcore-europe/meshcore-info.eu_i18n). So
musst du den Code der Website nie anfassen. Sprichst du eine der Sprachen
gut, kannst du sie verbessern:

1. Öffne die Seite und klick auf „Help improve this translation“. Damit öffnest du
   die Datei auf GitHub, wo du sie im Browser bearbeiten kannst.
2. Verbessere die Formulierungen. Lass Links, Code, Zahlen und Namen wie MeshCore
   genau so, wie sie sind.
3. Ändere im Block `translation` oben `status: ai` in
   `status: human` und schlag die Änderung vor.

Du hast ein falsches Wort gefunden, aber keine Zeit zum Korrigieren? Melde es über das
[Übersetzungsformular](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=translation-bug.yml).

## Einen Leitfaden verbessern {#guides}

Wir schreiben die Leitfäden zuerst auf Englisch und übersetzen sie von dort aus. Korrekturen
und neue Themen nehmen wir gern über das
[Inhaltsformular](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=new-content.yml)
oder per Pull Request entgegen. Jede Angabe braucht eine Quelle: die MeshCore-Firmware und ihre
Dokumentation, eine Funk-Regulierungsbehörde oder einen Hersteller. Schreib in eigenen Worten. Ein
kurzes Zitat mit Quellenangabe ist in Ordnung.

Im [Leitfaden für Mitwirkende](https://github.com/meshcore-europe/meshcore-info.eu/blob/main/CONTRIBUTING.md)
steht, wie du auf deinem eigenen Computer an der Website arbeitest.

## Stand der Übersetzungen {#coverage}

„Reviewed“ heißt: Ein Mensch hat die Übersetzung geprüft. „Machine“ heißt: maschinell übersetzt
und noch nicht geprüft. „Outdated“ heißt: Der englische Text hat sich nach der Übersetzung geändert.
„Missing“ heißt: Für die Seite gibt es noch keine Übersetzung.

{{< coverage >}}

## Danksagung {#credits}

Die Website ist mit [Astro](https://astro.build/) gebaut. Sie nutzt die Schriften
IBM Plex Sans und IBM Plex Mono unter der SIL Open Font License. Die Übersetzungen
folgen den
Konventionen von [kiekr-i18n](https://github.com/marcelverdult/kiekr-i18n) und
nutzen dessen MeshCore-Glossare. MeshCore selbst wird unter
[meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore) entwickelt.

Texte und Übersetzungen stehen unter der Lizenz CC BY 4.0, der Code unter der MIT-Lizenz.
