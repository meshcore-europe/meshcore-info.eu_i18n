---
title: Repeater-Leitfaden
lead: Ein hoch platzierter Repeater reicht Nachrichten für alle in seiner Umgebung weiter, über eine ganze Stadt oder ein ganzes Tal. Such einen Standort, versorge ihn mit Solarstrom, richte ihn ein und bleib im Rahmen des Gesetzes.
description: 'Einen MeshCore-Repeater in Europa planen, mit Strom versorgen, konfigurieren und legal betreiben: Standortwahl, Solardimensionierung, CLI-Einstellungen, Sendeleistung und Duty-Cycle-Grenzen bei 868 MHz.'
eyebrow: 868 MHz · bis zu 500 mW · lizenzfrei
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '4a0fe39f'
  seeded: '2026-10-26'
  fields: {title: '4608abcd', lead: 'bc670c65', description: '9e483ce5', eyebrow: '9fd33416'}
  sections: ['1de4a4f7', '766086be', '70faf508', '8bc641aa', '2018aa04', '92beca03', '17634750', 'cadf6024', 'e9cc6834', '2e6e59ca', 'fb44b8db']
---

Repeater tragen das Mesh. Companions, also die Funkgeräte, von denen aus du Nachrichten schreibst, reichen Nachrichten nicht weiter. Ohne Repeater erreichst du also nur die Leute in direkter Reichweite. Jeder Repeater, den du aufstellst, erweitert das Mesh für alle in seiner Umgebung. Dieser Leitfaden bezieht sich auf die MeshCore-Firmware v1.18.0.

Sprich zuerst mit deiner [lokalen Gruppe](/community/). Sie weiß, wo Abdeckung fehlt, welches [Preset deine Region nutzt](/guides/settings/) und wie Repeater benannt werden. Schau auf den [Abdeckungskarten](/map/) nach Repeatern in deiner Nähe und sag in den öffentlichen oder lokalen [Kanälen](/guides/channels/) hallo.

## Standort wählen {#site}

Höhe schlägt Leistung. LoRa bei 868 MHz kommt am weitesten bei freier Sichtverbindung. Hügel, Gebäude und dichte Bäume kosten weit mehr Reichweite, als ein paar zusätzliche Milliwatt zurückbringen.

- **Geh hoch hinaus.** Ein Dach, ein Mast, ein hohes Gebäude oder ein Hügel deckt weit mehr ab als ein Fensterbrett. Schon ein paar Meter über den umliegenden Dächern helfen.
- **Halt die Antenne frei.** Montiere sie über Dachkanten, fern von Metall, Regenrinnen und anderen Antennen.
- **Prüf die Sicht.** Werkzeuge wie [HeyWhatsThat](https://www.heywhatsthat.com/) zeigen, was man von einem Standort aus sehen kann. Wenn du einen Punkt sehen kannst, ist ein Repeater dort erreichbar.
- **Lass Abstand.** Ein Funkpfad braucht etwas freien Raum um die direkte Linie, nicht nur die Linie selbst. Über lange Strecken sollte die Mitte des Pfads Hindernisse um mehrere Meter überragen.
- **Frag um Erlaubnis.** Hol die Zustimmung des Eigentümers für Dach oder Mast ein und vereinbare, wie du für die Wartung an den Repeater kommst.

## Hardware {#hardware}

- **Board.** Nimm ein sparsames nRF52-Board wie den [Heltec T114](/devices/), RAK WisBlock oder den SenseCAP Solar Node. ESP32-Boards verbrauchen mehr Strom (die Geräteseite kennzeichnet sie mit „Hoch"), was den Solarbetrieb schwierig macht.
- **Antenne.** Verwende eine für 868 MHz gebaute Antenne und montiere sie senkrecht. Der [Antennen-Leitfaden](/guides/antenna/) behandelt Typen, Stecker, Kabel und Montage. Der Antennengewinn zählt bei der gesetzlichen Leistungsgrenze mit, siehe [Gesetzliche Grenzen](#legal).
- **Kabel.** Halt Koaxialkabel kurz oder nimm dämpfungsarmes Kabel. Bei 868 MHz können ein paar Meter dünnes Kabel die halbe Leistung schlucken.
- **Gehäuse.** Ein wetterfestes Gehäuse (IP65 oder besser) mit Kabelverschraubung, einem Lüftungs- oder Ablaufloch gegen Kondenswasser und heller Farbe oder Sonnenschutz. Akkus leiden unter Hitze und lassen sich unter dem Gefrierpunkt nicht laden.
- **Blitzschutz.** Eine Antenne auf dem Dach ist ein Ziel. Halt dich an die örtlichen Regeln für die Erdung oder montiere sie dort, wo ein Einschlag die Verkabelung des Gebäudes nicht erreicht.

## Stromversorgung und Solardimensionierung {#power}

Ein Solar-Repeater muss die dunkelsten Winterwochen überstehen. Leg ihn dafür aus:

1. **Miss die Last.** Lass den konfigurierten Repeater einen Tag lang über ein USB-Leistungsmessgerät laufen. Lies den Energieverbrauch in Wattstunden (Wh) ab. Der Funkverkehr in deiner Region verändert die Zahl, also miss wenn möglich vor Ort.
2. **Plane Reserve ein.** Leg die Akkukapazität für mindestens 5 bis 7 Tage ohne nutzbare Sonne aus.
3. **Ermittle deine Wintersonne.** Das kostenlose [PVGIS-Tool](https://re.jrc.ec.europa.eu/pvg_tools/en/) der EU zeigt für jeden Standort, wie viel Energie ein Panel pro Monat liefert. Nimm den Monat mit der wenigsten Sonne.
4. **Dimensioniere das Panel.** Das Panel muss den Tagesverbrauch in diesem schlechtesten Monat ersetzen, mit Spielraum für Ladeverluste.

Ein Rechenbeispiel mit angenommenen Zahlen: Ein Repeater, der 1 Wh pro Tag verbraucht, braucht für eine Woche Reserve einen Akku mit mindestens 7 Wh, also etwa 2 Ah nutzbare Kapazität bei 3,7 V. Wenn PVGIS für deinen Standort sagt, dass ein 1-W-Panel im Dezember 0,5 Wh pro Tag liefert, brauchst du mindestens ein 2-W-Panel. 3 bis 5 W lassen Spielraum für Wolken, Schnee und Alterung.

## Einrichten {#config}

**Flashen.** Nutze den [Web-Flasher](https://flasher.meshcore.io) und wähl die **Repeater**-Firmware für dein Board. Die Schritte zum Flashen findest du unter [Erste Schritte](/get-started/#flash).

**Über USB konfigurieren.** Öffne, solange der Repeater noch an deinem Computer hängt, [config.meshcore.io](https://config.meshcore.io) oder die Konsole des Flashers. Du kannst auch ein beliebiges serielles Terminal mit 115200 Baud nutzen. Die wichtigsten Befehle:

| Was | Befehl |
|---|---|
| Admin-Passwort ändern | `password <new password>` |
| Namen vergeben | `set name <name>` |
| Funk-Preset: Frequenz, Bandbreite, SF, CR (Neustart zum Übernehmen) | `set radio 869.618,62.5,8,8` |
| Duty-Cycle-Grenze in Prozent | `set dutycycle 10` |
| Sendeleistung des Funkchips in dBm | `set tx <dBm>` |
| Position, damit er auf Karten erscheint | `set lat <degrees>` und `set lon <degrees>` |
| Kontaktdaten für andere Betreiber | `set owner.info <text>` |
| Stunden zwischen Flood-Adverts, die das ganze Mesh hört | `set flood.advert.interval <hours>` |
| Jetzt ankündigen | `advert` |
| Neu starten | `reboot` |

Das Standard-Admin-Passwort ist `password`, und jeder, der sich damit anmeldet, wird Admin. Ändere es, bevor der Repeater auf Sendung geht.

Das `set radio`-Beispiel oben gilt für EU/UK (Narrow). Nimm stattdessen die Werte des Presets deiner Region: [Empfohlene Einstellungen](/guides/settings/) listet sie pro Land auf.

**Uhr stellen.** Ohne Uhrenmodul (RTC) verliert ein Repeater bei jedem Stromausfall die Zeit und startet im Mai 2024 neu, und im Betrieb geht seine Uhr falsch. Melde dich aus der App aus der Ferne an und nutze `clock sync`, oder stell die Zeit über USB. Ein RTC-Modul lohnt sich als Ergänzung für einen Repeater: Es behält die Zeit über Stromausfälle hinweg und weicht viel weniger ab.

**Aus der Ferne verwalten.** Sobald er im Mesh ist, meldest du dich aus der MeshCore-App mit dem Admin-Passwort an. Dort liest du seinen Status und nutzt dieselben Befehle über Funk. Manche Befehle funktionieren nur über USB, etwa `set freq` und das Zurücksetzen auf Werkseinstellungen mit `erase`.

Die vollständige Befehlsliste steht in der [MeshCore-CLI-Referenz](https://github.com/meshcore-dev/MeshCore/blob/main/docs/cli_commands.md).

## Gesetzliche Grenzen {#legal}

{{< callout type="legal" verified="2026-10-02" >}}
Die europäischen Presets von MeshCore liegen im Teilband **869.40-869.65 MHz**. In der EU, dem Vereinigten Königreich, der Schweiz und Norwegen ist es ohne Lizenz für Geräte mit geringer Reichweite offen, innerhalb dieser Grenzen:

- höchstens **500 mW e.r.p.** abgestrahlte Leistung;
- höchstens **10 % Duty Cycle**: nicht mehr als 360 Sekunden Sendezeit in jeder Stunde, pro Gerät. Alternativ darf ein Gerät Listen-before-talk mit adaptiver Frequenzwahl nach ETSI EN 300 220-2 nutzen;
- das ganze Signal, höchstens 250 kHz breit, muss innerhalb des Teilbands bleiben.

Das Band wird geteilt: Du darfst lizenzierte Dienste nicht stören, und andere dürfen dich stören.
Das Funkgerät muss eine CE-Kennzeichnung tragen (in Großbritannien CE oder UKCA).
{{< /callout >}}

Quellen: [CEPT ERC Recommendation 70-03](https://docdb.cept.org/document/845), Anhang 1, Band h1.7;
[Entscheidung 2006/771/EG der Kommission](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02006D0771(01)-20250123) und ihre Änderungen;
[ETSI EN 300 220-2](https://www.etsi.org/deliver/etsi_en/300200_300299/30022002/03.03.01_60/en_30022002v030301p.pdf), Band O.

### Leistung: e.r.p. und deine Antenne {#erp}

Die Grenze gilt für die *abgestrahlte* Leistung, gemessen gegenüber einem einfachen Dipol (e.r.p.). Der Antennengewinn zählt mit, die Kabeldämpfung geht ab. Hersteller geben den Antennengewinn in dBi an, das sind 2.15 dB mehr als derselbe Gewinn in dBd (bezogen auf einen Dipol). Halt diese Summe bei höchstens 27 dBm (500 mW):

> Sendeleistung (dBm) + Antennengewinn (dBi) − Kabeldämpfung (dB) − 2.15 ≤ 27

- Ein Board sendet mit 22 dBm in eine 5-dBi-Antenne über 1 dB Kabel: 22 + 5 − 1 − 2.15 = 23.85 dBm, etwa 240 mW e.r.p. Innerhalb der Grenze.
- Ein Board mit 30-dBm-Verstärker (1 W) in eine 3-dBi-Antenne: 30 + 3 − 2.15 = 30.85 dBm, etwa 1.2 W e.r.p. Über der Grenze, also senk die Sendeleistung.

`set tx` stellt die Ausgangsleistung des LoRa-Chips in dBm ein. Der SX1262-Chip selbst schafft höchstens 22 dBm, und die Firmware prüft die eingegebene Zahl nicht. Boards mit zusätzlichem Verstärker, etwa der Heltec V4 oder die Station G2, senden mit viel mehr als dem eingestellten Wert. Schau vor dem Einstellen in die Tabelle des Herstellers und fang niedrig an.

### Duty Cycle {#duty-cycle}

Ein Repeater sendet für alle in seiner Umgebung, darum verbraucht er seine Sendezeit schneller als ein Companion. Der Duty-Cycle-Begrenzer von MeshCore steht standardmäßig auf 50 %, mehr als dieses Band erlaubt. Stell ihn auf jedem Repeater auf 10 %:

```text
set dutycycle 10
```

### Frequenzgenauigkeit {#frequency}

Der Kanal EU/UK (Narrow), 869.618 MHz mit 62.5 kHz Bandbreite, reicht bis 869.649 MHz: weniger als 1 kHz unter der Oberkante des Teilbands. Das Signal muss bei jeder Temperatur im Band bleiben. Dafür braucht es einen temperaturkompensierten Quarz (TCXO). Fast jedes aktuelle Board hat einen; ältere Boards ohne, etwa der Heltec V2, driften zu weit, um bei 62.5 kHz zuverlässig zu arbeiten.

### Hinweise zu den Ländern {#countries}

- **EU-Mitgliedstaaten** müssen dieses Teilband zu diesen Bedingungen zur Verfügung stellen (Entscheidung 2006/771/EG, Artikel 3).
- **Vereinigtes Königreich:** dieselben Grenzen, in Ofcom [IR 2030](https://www.ofcom.org.uk/spectrum/radio-equipment/short-range-devices).
- **Schweiz und Liechtenstein:** dieselben Grenzen, in BAKOM [RIR1008-09](https://www.ofcomnet.ch/api/rir/1008/09).
- **Norwegen:** dieselben Grenzen, in der [Verordnung über allgemeine Genehmigungen](https://lovdata.no/dokument/SF/forskrift/2012-01-19-77) (fribruksforskriften).

Diese Hinweise sind keine Rechtsberatung. Regeln ändern sich; im Zweifel frag bei deiner nationalen Regulierungsbehörde nach.

## Checkliste für die Inbetriebnahme {#checklist}

- [ ] Der Eigentümer des Standorts hat zugestimmt, und du kommst für die Wartung an den Repeater.
- [ ] Das Board läuft mit der **Repeater**-Firmware, und die Antenne war vor dem ersten Einschalten angeschlossen.
- [ ] Das Admin-Passwort ist geändert.
- [ ] Die Funkeinstellungen entsprechen dem [Preset deiner Region](/guides/settings/) (`get radio`).
- [ ] `set dutycycle 10` ist gesetzt.
- [ ] Sendeleistung plus Antennengewinn bleibt innerhalb von 500 mW e.r.p.
- [ ] Name, Position und `owner.info` sind gesetzt, damit andere wissen, wer ihn betreibt.
- [ ] Die Uhr ist gestellt (`clock`).
- [ ] Das Gehäuse ist dicht, hat ein Ablauf- oder Lüftungsloch, und das Kabel hat eine Tropfschleife.
- [ ] Akku und Panel sind für den schlechtesten Wintermonat ausgelegt.
- [ ] Du hast ihn mit der App aus der Entfernung getestet, bevor du den Standort verlassen hast.
- [ ] Deine lokale Gruppe weiß, dass er läuft.
