---
title: Repeater-Checkliste
lead: Prüf deinen Repeater, bevor er nach oben kommt. Jede Zeile nennt, was du prüfst, den Befehl, der es anzeigt, und die Anleitung, die es erklärt.
description: 'Eine Checkliste für einen MeshCore-Repeater, bevor er auf ein Dach oder einen Mast kommt: was du über USB prüfst, wie du ihn montierst und der Test, bevor du gehst.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '5bbc2cbe'
  seeded: '2026-11-21'
  fields: {title: 'e982ea2f', lead: '664a2839', description: '01f56863'}
  sections: ['d512dacf', '4d357087', '75706984', '8a484df5', '33fd8c68']
  blocks: ['d512dacf', 'a7ba4c46', '6a427551', '2f0a8827', '2bda1638', '589c7b4f', '5fedefb7', 'e12f330e', 'd6d0b21c']
---

Ein Repeater auf dem Dach ist schwer erreichbar. Prüf ihn deshalb, solange er
noch auf deinem Schreibtisch liegt. Die [Repeater-Anleitung](/repeater-guide/)
erklärt jeden Schritt. Die Werte, etwa das Preset und die Hop-Limits, findest
du in den [Einstellungen für deine Gegend](/guides/settings/). Gib die Befehle
über USB ein, zum Beispiel in der [seriellen Konsole](/firmware/console/).
Diese Liste gilt für die MeshCore-Firmware v1.18.0.

## Bevor du anfängst {#start}

- [ ] Die [Abdeckungskarten](/map/) oder deine [lokale Gruppe](/community/)
      zeigen, dass die Gegend einen Repeater braucht. Siehe
      [Brauchst du einen?](/repeater-guide/#need)
- [ ] Der Eigentümer des Standorts ist einverstanden, und du kommst für die
      Wartung an den Repeater heran.
- [ ] Akku und Solarpanel sind für den schlechtesten Wintermonat ausgelegt.
      Siehe [Strom und Solar dimensionieren](/repeater-guide/#power).

## Am Schreibtisch, über USB {#usb}

- [ ] Auf dem Board läuft die **Repeater**-Firmware: `ver` zeigt ihre Version.
      Siehe [Einrichten](/repeater-guide/#config).
- [ ] Auf einem nRF52-Board enthält die Antwort auf `get bootloader.ver` den
      Eintrag `OTAFIX`. Siehe [Over the Air aktualisieren](/repeater-guide/#update).
- [ ] `get radio` zeigt das Preset deiner Gegend.
- [ ] `get dutycycle` zeigt 10. Siehe [Duty Cycle](/repeater-guide/#duty-cycle).
- [ ] `get tx` plus dein Antennengewinn ergibt höchstens 500 mW e.r.p.
      Siehe [Leistung: e.r.p. und deine Antenne](/repeater-guide/#erp).
- [ ] Das Admin-Passwort lautet nicht mehr `password`.
- [ ] `get guest.password` zeigt ein Passwort.
- [ ] `get name` zeigt den Namen, den deine lokale Gruppe für ihre Repeater
      verwendet.
- [ ] `get lat` und `get lon` zeigen die Position des Standorts.
- [ ] `get owner.info` zeigt, wie andere Betreiber dich erreichen.
- [ ] `region` zeigt die Regionen deiner Gegend. `get flood.max.advert` und
      `get flood.max.unscoped` zeigen ihre Hop-Limits. Siehe
      [Datenverkehr gering halten](/guides/settings/#traffic).
- [ ] Du hast den privaten Schlüssel aus `get prv.key` an einem sicheren Ort
      gespeichert.
- [ ] `clock` zeigt die aktuelle Uhrzeit in UTC.
- [ ] Bei Solarbetrieb zeigt `powersaving` den Wert `on`.

## Auf dem Dach {#roof}

- [ ] Du schließt die Antenne an, bevor der Repeater Strom bekommt.
- [ ] Die Antenne steht senkrecht oben auf dem Mast, mit Abstand zu Metall.
      Siehe [Montage](/guides/antenna/#mounting).
- [ ] Jeder Steckverbinder im Freien ist abgedichtet, und das Kabel hat eine
      Tropfschlaufe.
- [ ] Das Gehäuse ist geschlossen und hat eine Belüftungs- oder Ablauföffnung.
      Siehe [Hardware](/repeater-guide/#hardware).

## Bevor du gehst {#leave}

- [ ] Aus der Entfernung erreichst du den Repeater mit deinem Companion in der
      App.
- [ ] Du hast `advert` gesendet, damit die Knoten im ganzen Mesh den Repeater
      kennenlernen.
- [ ] Deine [lokale Gruppe](/community/) weiß, dass er läuft.
