---
title: Repeater-Leitfaden
lead: Ein hoch platzierter Repeater leitet Nachrichten für alle in seiner Umgebung weiter, über eine ganze Stadt oder ein ganzes Tal. Such dir einen Standort, versorge ihn mit Solarstrom, richte ihn ein und halte dich an die gesetzlichen Vorgaben.
description: 'Einen MeshCore-Repeater in Europa planen, mit Strom versorgen, konfigurieren und legal betreiben: Standortwahl, Solarauslegung, CLI-Einstellungen, Sendeleistung und Duty-Cycle-Grenzen bei 868 MHz.'
eyebrow: 868 MHz · bis 500 mW · lizenzfrei
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '7c7e3be3'
  seeded: '2026-10-31'
  fields: {title: '4608abcd', lead: 'bc670c65', description: '9e483ce5', eyebrow: '9fd33416'}
  sections: ['05ee477a', '938c518c', '766086be', '70faf508', '8bc641aa', '399cd683', 'e9dedb7b', '92beca03', '17634750', 'cadf6024', 'e9cc6834', '2e6e59ca', 'fb44b8db']
  blocks: ['20ac0371', 'ed2b1adf', '432543ee', '7af42c89', 'd0f7543a', '9ef3580f', '3476aef7', '1bab7bec', '6a7c4493', 'dbd9fa1f', 'aa06d32b', '9958aad3', 'd162b028', 'cca1bbdf', '64ef011d', 'e7f16724', 'd2e34ff0', 'bb195cfc', '8d080bb3', '2b1d995b', '210f1b66', 'dc7419d2', 'bdc66db0', 'b59f248c', '7184bd63', 'de5a24f9', 'f5cfb426', '48c7422f', '9d3c0836', 'da8a6af3', '240126df', '8aac2b33', '81a475b8', 'a53e42b5', '36ff1db4', 'e4ca8602', 'e4594afd', '3b24b8e9', '58330858', '68f2966e', 'd7418228', '23536e60', 'cbc5c2d1', '2ea02ba9', '92540256', '6e21f681', 'a8c12311', '3382ae7f', 'cdeafb0f', '1b1319d2']
---

Repeater tragen das Mesh. Companions, also die Funkgeräte, mit denen du Nachrichten
schreibst, leiten keine Nachrichten weiter. Ohne Repeater erreichst du deshalb nur
die Leute in direkter Reichweite. Ein Repeater am richtigen Ort erweitert das Mesh
für alle in seiner Umgebung. Dieser Leitfaden bezieht sich auf die MeshCore-Firmware
v1.18.0.

Sprich vor dem Start mit deiner [lokalen Gruppe](/community/). Sie weiß, wo die
Abdeckung fehlt, welches [Preset deine Gegend nutzt](/guides/settings/) und wie man
Repeater benennt. Schau auf den [Abdeckungskarten](/map/) nach Repeatern in deiner
Nähe und sag Hallo in den öffentlichen oder lokalen [Kanälen](/guides/channels/).

## Brauchst du einen? {#need}

Ein Repeater sendet jede Flood-Nachricht weiter, die er empfängt. Alle Repeater in
Reichweite teilen sich dieselbe Sendezeit. Wo das Mesh dich schon erreicht, bringt
ein weiterer Repeater mehr Verkehr und keine zusätzliche Abdeckung. Ein hoch
platzierter Companion, etwa an einem Dachfenster oder auf dem Balkon, kann schon
reichen.

Stell einen Repeater dort auf, wo Abdeckung fehlt:

- Die [Abdeckungskarten](/map/) zeigen keinen Repeater in deiner Nähe oder nur
  solche, die dein Companion nicht empfängt.
- Deine lokale Gruppe sagt, dass die Gegend einen braucht.

## Standort wählen {#site}

Höhe schlägt Leistung. LoRa auf 868 MHz kommt bei freier Sichtlinie am weitesten.
Hügel, Gebäude und dichte Bäume kosten weit mehr Reichweite, als ein paar
zusätzliche Milliwatt zurückholen.

- **Geh hoch hinaus.** Ein Dach, ein Mast, ein hohes Gebäude oder ein Hügel deckt
  weit mehr ab als eine Fensterbank. Schon ein paar Meter über den umliegenden
  Dächern helfen.
- **Halte die Antenne frei.** Montiere sie über der Dachkante, fern von Metall,
  Dachrinnen und anderen Antennen.
- **Prüf die Sicht.** Mit Tools wie [HeyWhatsThat](https://www.heywhatsthat.com/)
  siehst du, was von einem Standort aus sichtbar ist. Siehst du einen Ort, ist ein
  Repeater dort in Reichweite.
- **Lass Freiraum.** Eine Funkstrecke braucht etwas freien Raum um die direkte
  Linie herum, nicht nur die Linie selbst. Auf langen Strecken sollte die Mitte des
  Pfads mehrere Meter Abstand zu Hindernissen haben.
- **Frag um Erlaubnis.** Hol dir die Zustimmung des Eigentümers für Dach oder Mast.
  Vereinbare auch, wie du für die Wartung an den Repeater kommst.

## Hardware {#hardware}

- **Board.** Wähl ein sparsames nRF52-Board wie das [Heltec T114](/devices/),
  RAK WisBlock oder den SenseCAP Solar Node. ESP32-Boards brauchen mehr Strom (die
  Geräteseite kennzeichnet sie mit High). Mit Solarstrom lassen sie sich deshalb
  schwer betreiben.
- **Antenne.** Nimm eine Antenne für 868 MHz und montiere sie senkrecht. Der
  [Antennen-Leitfaden](/guides/antenna/) behandelt Typen, Stecker, Kabel und
  Montage. Der Antennengewinn zählt zur gesetzlichen Leistungsgrenze, siehe
  [Gesetzliche Grenzen](#legal).
- **Kabel.** Halte das Koaxialkabel kurz oder nimm verlustarmes Kabel. Bei
  868 MHz können ein paar Meter dünnes Kabel die Hälfte deiner Leistung schlucken.
- **Gehäuse.** Nimm eine wetterfeste Box (IP65 oder besser) mit Kabelverschraubung
  und einem Lüftungs- oder Ablaufloch gegen Kondenswasser. Sie sollte hell sein oder
  einen Sonnenschutz haben. Akkus leiden unter Hitze und lassen sich unter dem
  Gefrierpunkt nicht laden.
- **Blitz.** Eine Antenne auf dem Dach ist ein Ziel. Halte dich an die örtlichen
  Regeln zur Erdung oder montiere sie so, dass ein Einschlag die Elektrik des
  Gebäudes nicht erreicht.

## Strom und Solarauslegung {#power}

Ein Solar-Repeater muss die dunkelsten Winterwochen überstehen. Leg ihn dafür aus:

1. **Miss den Verbrauch.** Häng den konfigurierten Repeater für einen Tag an ein
   USB-Strommessgerät. Lies die verbrauchte Energie in Wattstunden (Wh) ab. Der
   Verkehr in deiner Gegend verändert den Wert, miss also möglichst vor Ort.
2. **Plan Reserve ein.** Leg die Akkukapazität für mindestens 5 bis 7 Tage ohne
   brauchbare Sonne aus.
3. **Ermittle deine Wintersonne.** Das kostenlose
   [PVGIS-Tool](https://re.jrc.ec.europa.eu/pvg_tools/en/) der EU zeigt für jeden
   Standort, wie viel Energie ein Panel pro Monat liefert. Nimm den Monat mit der
   wenigsten Sonne.
4. **Leg das Panel aus.** Das Panel muss im schlechtesten Monat den Tagesverbrauch
   ersetzen, mit Spielraum für Ladeverluste.

Ein Rechenbeispiel mit angenommenen Werten: Ein Repeater, der 1 Wh pro Tag
verbraucht, braucht für eine Woche Reserve einen Akku mit mindestens 7 Wh. Das sind
etwa 2 Ah nutzbare Kapazität bei 3,7 V. Liefert ein 1-W-Panel an deinem Standort
laut PVGIS im Dezember 0,5 Wh pro Tag, brauchst du mindestens ein 2-W-Panel. Mit
3 bis 5 W hast du Reserve für Wolken, Schnee und Alterung.

## Einrichten {#config}

**Flashen.** Öffne den [Web-Flasher](https://flasher.meshcore.io) und wähl die
**Repeater**-Firmware für dein Board. Die einzelnen Schritte findest du unter
[Erste Schritte](/get-started/#flash).

**Per USB konfigurieren.** Lass den Repeater mit deinem Computer verbunden und öffne
[config.meshcore.io](https://config.meshcore.io) oder die Konsole des Flashers. Du
kannst auch jedes serielle Terminal mit 115200 Baud nutzen. Die wichtigsten Befehle:

| Was | Befehl |
|---|---|
| Admin-Passwort ändern | `password <new password>` |
| Namen vergeben | `set name <name>` |
| Funk-Preset: Frequenz, Bandbreite, SF, CR (wirkt nach Neustart) | `set radio 869.618,62.5,8,8` |
| Duty-Cycle-Grenze in Prozent | `set dutycycle 10` |
| Sendeleistung des Funkchips in dBm | `set tx <dBm>` |
| Position, damit er auf Karten erscheint | `set lat <degrees>` und `set lon <degrees>` |
| Kontaktdaten für andere Betreiber | `set owner.info <text>` |
| Stunden zwischen Flood-Adverts, die das ganze Mesh empfängt | `set flood.advert.interval <hours>` |
| Sofort ankündigen | `advert` |
| Neu starten | `reboot` |

Das Standard-Admin-Passwort ist `password`. Wer sich damit anmeldet, wird Admin.
Ändere es, bevor der Repeater auf Sendung geht.

Das Beispiel für `set radio` oben gilt für EU/UK (Narrow). Nimm stattdessen die
Werte des Presets deiner Gegend: [Empfohlene Einstellungen](/guides/settings/)
listet sie pro Land auf.

**Uhr stellen.** Ohne Uhrmodul (RTC) verliert ein Repeater bei jedem Stromausfall
die Zeit, und seine Uhr beginnt wieder im Mai 2024. Im Betrieb driftet seine Uhr
außerdem: Sie geht immer weiter vor oder nach. Stell die Uhr deshalb ab und zu:
Melde dich in der App aus der Ferne an und nutze `clock sync`, oder stell die Zeit
per USB. Mit einem RTC-Modul musst du das selten tun: Es hält die Zeit über
Stromausfälle hinweg und driftet viel weniger.

**Aus der Ferne verwalten.** Sobald er im Mesh ist, meldest du dich in der
MeshCore-App mit dem Admin-Passwort an. Dort liest du seinen Status ab und nutzt
dieselben Befehle über Funk. Manche Befehle funktionieren nur per USB, etwa
`set freq` und der Werksreset `erase`.

**Identität behalten.** Gib vor einem Erase per USB `get prv.key` ein. Bewahr den
angezeigten privaten Schlüssel sicher auf. Nach dem Erase bekommt der Repeater mit
`set prv.key <key>` und einem `reboot` seine alte Identität zurück. Knoten, die ihn
kennen, finden ihn dann unter demselben Präfix.

Die vollständige Befehlsliste steht in der
[MeshCore-CLI-Referenz](https://github.com/meshcore-dev/MeshCore/blob/main/docs/cli_commands.md).

## Über Funk aktualisieren {#update}

Hängt der Repeater erst oben, aktualisierst du ihn vom Boden aus. Melde dich in der
MeshCore-App mit dem Admin-Passwort an, öffne seine Kommandozeile und gib
`start ota` ein. Was dann passiert, hängt vom Board ab. Andere Boards antworten mit
`Error`, die aktualisierst du per USB.

**nRF52-Boards** wie RAK, Heltec T114, Seeed XIAO und SenseCAP Solar:

1. Lade im [Web-Flasher](https://flasher.meshcore.io) die **ZIP**-Datei der neuen
   Firmware für dein Board herunter.
2. Gib `start ota` ein. Der Repeater antwortet mit `OK` und erscheint per Bluetooth
   als `<board>_OTA`, zum Beispiel `RAK4631_OTA`.
3. Öffne auf deinem Handy die App nRF Device Firmware Update, wähl die ZIP-Datei
   und den Repeater und starte den Upload. Das dauert ein paar Minuten.

Installier den [OTAFIX-Bootloader](https://github.com/oltaco/Adafruit_nRF52_Bootloader_OTAFIX)
auf einem nRF52-Board, bevor es nach oben kommt. Mit dem Standard-Bootloader lässt
sich ein fehlgeschlagenes Update nur per USB reparieren. Mit OTAFIX fällt das Board
in den Update-Modus zurück, und du versuchst es erneut per Bluetooth.

**ESP32-Boards** wie Heltec V3 und V4:

1. Lade im Web-Flasher die **nicht zusammengeführte** `.bin` für dein Board
   herunter: die Datei ohne „merged“ im Namen.
2. Gib `start ota` ein. Der Repeater öffnet ein WiFi-Netz namens `MeshCore-OTA` und
   antwortet mit der Adresse seiner Upload-Seite.
3. Verbinde dich in WiFi-Reichweite mit Handy oder Laptop mit diesem Netz, öffne
   die Adresse und lade die Datei hoch.

## Gesetzliche Grenzen {#legal}

{{< callout type="legal" verified="2026-10-02" >}}
Die europäischen Presets von MeshCore liegen im Teilband **869.40-869.65 MHz**. In
der EU, im Vereinigten Königreich, in der Schweiz und in Norwegen steht es
Funkanwendungen mit geringer Reichweite ohne Lizenz offen, innerhalb dieser Grenzen:

- höchstens **500 mW e.r.p.** Strahlungsleistung;
- höchstens **10% Duty Cycle**: höchstens 360 Sekunden Sendezeit pro Stunde und
  Gerät. Alternativ darf ein Gerät Listen-before-Talk mit adaptiver Frequenzagilität
  nach ETSI EN 300 220-2 nutzen;
- das ganze Signal, höchstens 250 kHz breit, muss im Teilband bleiben.

Das Band ist geteilt: Du darfst lizenzierte Dienste nicht stören, und andere
dürfen dich stören.
Das Funkgerät muss eine CE-Kennzeichnung tragen (in Großbritannien CE oder UKCA).
{{< /callout >}}

Quellen: [CEPT ERC Recommendation 70-03](https://docdb.cept.org/document/845),
Anhang 1, Band h1.7;
[Entscheidung 2006/771/EG der Kommission](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02006D0771(01)-20250123)
und ihre Änderungen;
[ETSI EN 300 220-2](https://www.etsi.org/deliver/etsi_en/300200_300299/30022002/03.03.01_60/en_30022002v030301p.pdf),
Band O.

### Leistung: e.r.p. und deine Antenne {#erp}

Die Grenze gilt für die *abgestrahlte* Leistung, gemessen gegen eine einfache
Dipolantenne (e.r.p.). Der Antennengewinn zählt mit, der Kabelverlust zieht ab.
Hersteller geben den Antennengewinn in dBi an. Das sind 2.15 dB mehr als derselbe
Gewinn in dBd (bezogen auf einen Dipol). Halte diese Summe bei höchstens 27 dBm
(500 mW):

> transmit power (dBm) + antenna gain (dBi) − cable loss (dB) − 2.15 ≤ 27

- Ein Board sendet 22 dBm über 1 dB Kabelverlust in eine 5-dBi-Antenne:
  22 + 5 − 1 − 2.15 = 23.85 dBm, etwa 240 mW e.r.p. Das liegt innerhalb der Grenze.
- Ein Board mit einem 30-dBm-Verstärker (1 W) an einer 3-dBi-Antenne:
  30 + 3 − 2.15 = 30.85 dBm, etwa 1.2 W e.r.p. Das liegt über der Grenze. Senk die
  Sendeleistung.

`set tx` legt die Ausgangsleistung des LoRa-Chips in dBm fest. Der SX1262-Chip
selbst schafft höchstens 22 dBm. Die Firmware prüft den eingegebenen Wert nicht.
Boards mit zusätzlichem Verstärker, etwa der Heltec V4 oder die Station G2, senden
mit viel mehr Leistung als dem eingestellten Wert. Prüf die Tabelle des Herstellers,
bevor du den Wert einstellst, und fang niedrig an.

### Duty Cycle {#duty-cycle}

Ein Repeater sendet für alle in seiner Umgebung. Deshalb verbraucht er seine
Sendezeit schneller als ein Companion. Der Duty-Cycle-Begrenzer von MeshCore steht
standardmäßig auf 50%, mehr als dieses Band erlaubt. Stell ihn auf jedem Repeater
auf 10%:

```text
set dutycycle 10
```

### Frequenzgenauigkeit {#frequency}

Der Kanal EU/UK (Narrow), 869.618 MHz mit 62.5 kHz Bandbreite, reicht bis
869.649 MHz: weniger als 1 kHz unter der Obergrenze des Teilbands. Das Signal
muss bei jeder Temperatur im Band bleiben. Dafür braucht das Board einen
temperaturkompensierten Quarz (TCXO). Fast jedes aktuelle Board hat einen;
ältere Boards ohne, etwa der Heltec V2, driften zu weit, um bei 62.5 kHz
zuverlässig zu funktionieren.

### Hinweise nach Ländern {#countries}

- **EU-Mitgliedstaaten** müssen dieses Teilband zu diesen Bedingungen bereitstellen
  (Entscheidung 2006/771/EG, Artikel 3).
- **Vereinigtes Königreich:** dieselben Grenzen, in Ofcom
  [IR 2030](https://www.ofcom.org.uk/spectrum/radio-equipment/short-range-devices).
- **Schweiz und Liechtenstein:** dieselben Grenzen, in BAKOM
  [RIR1008-09](https://www.ofcomnet.ch/api/rir/1008/09).
- **Norwegen:** dieselben Grenzen, in der
  [Verordnung über Allgemeinzuteilungen](https://lovdata.no/dokument/SF/forskrift/2012-01-19-77)
  (fribruksforskriften).

Diese Hinweise sind keine Rechtsberatung. Regeln ändern sich. Frag im Zweifel bei
deiner nationalen Regulierungsbehörde nach.

## Checkliste für die Installation {#checklist}

- [ ] Der Eigentümer des Standorts hat zugestimmt, und du kommst für die Wartung an
      den Repeater.
- [ ] Auf dem Board läuft die **Repeater**-Firmware, und die Antenne war vor dem
      ersten Einschalten angeschlossen.
- [ ] Das Admin-Passwort ist geändert.
- [ ] Die Funkeinstellungen passen zum [Preset deiner Gegend](/guides/settings/)
      (`get radio`).
- [ ] `set dutycycle 10` ist gesetzt.
- [ ] Sendeleistung plus Antennengewinn bleiben innerhalb von 500 mW e.r.p.
- [ ] Name, Position und `owner.info` sind gesetzt, damit andere wissen, wer ihn
      betreibt.
- [ ] Die Uhr ist gestellt (`clock`).
- [ ] Das Gehäuse ist dicht, mit Ablauf- oder Lüftungsloch, und das Kabel hat eine
      Tropfschlaufe.
- [ ] Akku und Panel sind für den schlechtesten Wintermonat ausgelegt.
- [ ] Du hast ihn vor dem Verlassen des Standorts mit der App aus der Entfernung
      getestet.
- [ ] Deine lokale Gruppe weiß, dass er läuft.
