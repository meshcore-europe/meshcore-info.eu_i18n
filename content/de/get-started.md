---
title: Erste Schritte
lead: Vom neuen Board bis zu deiner ersten Nachricht im Mesh. Du brauchst ein LoRa-Board, einen Computer mit Chrome oder Edge und ein Handy oder einen Laptop für die App.
description: Flashe MeshCore aus dem Browser, kopple die App, wähle das Funk-Preset deiner Gegend, schicke deine erste Nachricht und tritt deinem lokalen Kanal bei.
eyebrow: 6 Schritte · MeshCore v1.18.0
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '68c89544'
  seeded: '2026-10-26'
  fields: {title: '61e8d44a', lead: '45b0e5c3', description: 'cf031b18', eyebrow: '4fa6fe1e'}
  sections: ['16c3728c', '203acaa5', '36a3eba3', '6da9fd7a', 'cb5fb72e', '89626504', 'a419ce79', 'aa273b20']
---

Diese Schritte beziehen sich auf die MeshCore-Firmware v1.18.0 und die offiziellen Tools vom
Oktober 2026. Die Menünamen in der App können sich je nach Version etwas unterscheiden.

## 1. Gerät auswählen {#device}

Jedes Board auf der [Geräteseite](/devices/), bei dem Companion steht, eignet sich. Für
deinen ersten Knoten nimmst du am besten einen *Companion*: das Funkgerät, von dem aus du Nachrichten schreibst. Du koppelst es
per Bluetooth oder USB mit deinem Handy oder Laptop, oder du nimmst eines mit eigenem Bildschirm
und eigener Tastatur, das ohne weitere Geräte läuft.

Nimm die Version für 868 MHz. Die mitgelieferte Antenne reicht aus; im
[Antennen-Ratgeber](/guides/antenna/) steht, wie du eine Antenne prüfst.

{{< callout type="warning" >}}
Schraube die Antenne an, bevor du das Funkgerät einschaltest. Sendet ein LoRa-Funkgerät
ohne Antenne, kann es seinen eigenen Chip beschädigen.
{{< /callout >}}

## 2. Firmware flashen {#flash}

1. Verbinde das Gerät mit einem USB-Datenkabel mit deinem Computer.
2. Öffne den Web-Flasher unter [flasher.meshcore.io](https://flasher.meshcore.io)
   in Chrome oder Edge. Er nutzt Web Serial, das andere Browser nicht haben.
3. Wähle dein Gerät und dann die **Companion**-Firmware für **Bluetooth** (oder
   USB, wenn du es nur per Kabel am Computer nutzen willst).
4. Starte das Flashen. Manche Boards müssen erst in den Update-Modus; der Flasher zeigt dir,
   wie das geht.

Nutze *erase* nur für einen Neuanfang: Das Löschen entfernt die Identität des Geräts
und deine Kontakte. Bei späteren Updates flashst du ohne Löschen.

## 3. App installieren {#app}

Die offizielle MeshCore-App gibt es für Android, iOS, Windows und macOS;
auf [meshcore.io](https://meshcore.io) findest du Links zu jeder Version. Außerdem gibt es eine
Web-App unter [app.meshcore.nz](https://app.meshcore.nz), die in Chrome oder
Edge auf einem Computer läuft.

## 4. Knoten koppeln {#pair}

Schalte deinen Knoten ein, öffne die App und verbinde dich per Bluetooth mit ihm. Wenn die App
nach einer PIN fragt:

- ein Knoten **mit** Bildschirm zeigt eine PIN an; die gibst du ein;
- ein Knoten **ohne** Bildschirm nutzt `123456`.

Schlägt die Kopplung fehl, entferne das Gerät aus den Bluetooth-Einstellungen deines Handys und
versuche es noch einmal. Gib deinem Knoten dann einen Namen. Andere sehen diesen Namen, also verwende
nicht deinen vollen Namen oder deine Adresse, außer du willst das.

## 5. Funk-Preset deiner Gegend wählen {#preset}

Alle Funkgeräte in einer Gegend nutzen dieselbe Frequenz und dieselben Einstellungen, sonst können sie
sich nicht hören. Wähle in den Funkeinstellungen der App das Preset, das deine Gegend nutzt.
Außerhalb der unten genannten Gebiete nutzt Europa **EU/UK (Narrow)**. Die Niederlande,
Tschechien, Ungarn, die Slowakei, Portugal und die Schweiz haben eigene Presets, und
Limburg in den Niederlanden hat eine Variante:

{{< presets >}}

Nicht sicher? Deine [lokale Gruppe](/community/) weiß, welches Preset deine Gegend nutzt.
Die App lädt diese Liste vom MeshCore-Projekt herunter, ein neues Preset braucht also
kein App-Update.

## 6. Hallo sagen {#hello}

1. **Mach dich bekannt.** Schicke aus der App ein *Advert*. Ein "Flood"-Advert
   läuft über die Repeater (Knoten, die Nachrichten weiterreichen), sodass dich jeder
   im Mesh hinzufügen kann.
   Companions melden sich nie von selbst.
2. **Finde andere.** Leute erscheinen in deinen Kontakten, sobald ihre Adverts dich
   erreichen. Repeater schicken standardmäßig alle 47 Stunden ein Flood-Advert, deine Liste
   kann also 2 Tage brauchen, bis sie voll ist.
3. **Schick eine Nachricht.** Öffne einen Kontakt und schreib los. Die erste Nachricht geht per Flood
   durchs Netz; der Empfänger meldet den Weg zurück, den sie genommen hat, und spätere
   Nachrichten folgen diesem Weg.
4. **Tritt Kanälen bei.** Der Kanal **Public** ist schon eingerichtet; alles, was du
   dort schreibst, erreicht jeden im Mesh. Füge den *Hashtag-Kanal* deiner Region
   (ein Name, der mit `#` beginnt) hinzu, indem du seinen Namen eingibst. Deine
   [lokale Gruppe](/community/) sagt dir, welche Kanäle aktiv sind.

## Wenn etwas nicht klappt {#troubleshooting}

**Die App findet mein Gerät nicht per Bluetooth.**
Du hast wahrscheinlich den USB-Companion geflasht. Flashe noch einmal und wähle die
Bluetooth-Version. Beim Heltec V3 hat die kleine eingebaute Bluetooth-Antenne
nur eine kurze Reichweite; halte das Handy nah dran.

**Die Kopplung schlägt immer wieder fehl.**
Entferne das Gerät aus den Bluetooth-Einstellungen deines Handys, starte Bluetooth neu
und kopple erneut mit der PIN auf dem Bildschirm oder `123456`.

**In meinen Kontakten erscheint niemand.**
Prüfe, ob dein Preset zu deiner Gegend passt. Schicke ein Flood-Advert. Ist kein
Repeater in Reichweite, hörst du nur Funkgeräte in deiner Nähe; die
[Kartenseite](/map/) zeigt, wo Repeater stehen.

**Bei einem Kontakt steht "zuletzt gesehen" vor Tagen, obwohl er aktiv ist.**
Einer der beiden Knoten hat die falsche Uhrzeit. Ein Companion übernimmt die Zeit von
deinem Handy; bei Repeatern und Room-Servern (Knoten, die Nachrichten für eine
Gruppe speichern) muss der Besitzer sie einstellen.

**Der Flasher kann unter Linux den seriellen Port nicht öffnen.**
Dein Benutzer braucht Zugriff auf den Port, zum Beispiel mit
`sudo setfacl -m u:$USER:rw /dev/ttyUSB0` oder als Mitglied der Gruppe
`dialout`.

**Etwas anderes.** Die
[MeshCore-FAQ](https://github.com/meshcore-dev/MeshCore/blob/main/docs/faq.md)
behandelt noch viele weitere Probleme.
