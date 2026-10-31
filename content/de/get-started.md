---
title: Erste Schritte
lead: Vom neuen Board bis zu deiner ersten Nachricht im Mesh. Du brauchst ein LoRa-Board, einen Computer mit Chrome oder Edge und ein Handy oder einen Laptop für die App.
description: Flashe MeshCore im Browser, kopple die App, wähle das Funk-Preset deiner Gegend, schick deine erste Nachricht und tritt deinem lokalen Kanal bei.
eyebrow: 6 Schritte · MeshCore v1.18.0
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'f97ca1b9'
  seeded: '2026-10-31'
  fields: {title: '61e8d44a', lead: '45b0e5c3', description: 'cf031b18', eyebrow: '4fa6fe1e'}
  sections: ['16c3728c', '203acaa5', 'df7a1665', '6da9fd7a', 'cb5fb72e', 'a1cf8b26', 'a419ce79', '66d00206']
  blocks: ['16c3728c', '2a70a7ed', '6f8e6f5f', '16c11d47', '081db416', 'd5e7fd0b', '6d28c323', 'eb2ea361', 'de50125c', 'ae20cb8e', 'abd42710', 'c08a865a', '7d1eb0b9', '263e0c96', '0903299f', 'eba20370', '5cdc20cf', '7f542f82', '802ca5a8', '1a854187', 'bc333adf', 'f25b16fa', '7c893ae2', '7f5927b4', '26e13713', '39a142cf', 'a786620c', '216897fa', '2d222782', 'a9755900', 'f081b357']
---

Diese Anleitung bezieht sich auf die MeshCore-Firmware v1.18.0 und die
offiziellen Tools vom Oktober 2026. Die Menünamen in der App können je nach
Version etwas abweichen.

## 1. Gerät auswählen {#device}

Jedes Board auf der [Geräteseite](/devices/), bei dem Companion aufgeführt
ist, funktioniert. Nimm für deinen ersten Knoten einen *Companion*: das
Funkgerät, über das du Nachrichten schreibst. Du koppelst es per Bluetooth
oder USB mit deinem Handy oder Laptop. Alternativ wählst du eins mit eigenem
Display und eigener Tastatur, das allein funktioniert.

Kauf die 868-MHz-Version. Die mitgelieferte Antenne reicht aus. In der
[Antennen-Anleitung](/guides/antenna/) erfährst du, wie du eine Antenne prüfst.

{{< callout type="warning" >}}
Schraub die Antenne an, bevor du das Funkgerät einschaltest. Ein LoRa-Funkgerät,
das ohne Antenne sendet, kann seinen eigenen Chip beschädigen.
{{< /callout >}}

## 2. Firmware flashen {#flash}

1. Verbinde das Gerät mit einem USB-Datenkabel mit deinem Computer.
2. Öffne den Web-Flasher unter [flasher.meshcore.io](https://flasher.meshcore.io)
   in Chrome oder Edge. Er nutzt Web Serial, das andere Browser nicht haben.
3. Wähle dein Gerät und dann die **Companion**-Firmware für **Bluetooth** (oder
   USB, wenn du es nur per Kabel am Computer nutzt).
4. Flashe die Firmware. Manche Boards musst du vorher in den Update-Modus
   versetzen. Der Flasher zeigt dir, wie das geht.

Nutze *erase* nur für einen kompletten Neuanfang: Beim Löschen gehen die
Identität des Geräts und deine Kontakte verloren. Spätere Updates flashst du
ohne Löschen. Willst du deine Identität über ein Löschen hinweg behalten,
exportierst du vorher in der App den privaten Schlüssel deines Companions.
Danach importierst du ihn wieder.

## 3. App installieren {#app}

Die offizielle MeshCore-App gibt es für Android, iOS, Windows und macOS. Auf
[meshcore.io](https://meshcore.io) findest du Links zu allen Versionen. Außerdem
gibt es eine Web-App unter [app.meshcore.nz](https://app.meshcore.nz), die auf
dem Computer in Chrome oder Edge läuft.

## 4. Knoten koppeln {#pair}

Schalte deinen Knoten ein, öffne die App und verbinde dich per Bluetooth mit
ihm. Wenn die App nach einer PIN fragt:

- Ein Knoten **mit** Display zeigt eine PIN an. Gib diese ein.
- Ein Knoten **ohne** Display nutzt `123456`.

Klappt die Kopplung nicht, entferne das Gerät aus den Bluetooth-Einstellungen
deines Handys und versuch es noch einmal. Gib deinem Knoten danach einen Namen.
Andere sehen diesen Namen. Verwende deshalb nicht deinen vollen Namen oder
deine Adresse, außer du willst das.

## 5. Funk-Preset deiner Gegend wählen {#preset}

Alle Funkgeräte in einer Gegend nutzen dieselbe Frequenz und dieselben
Einstellungen, sonst hören sie sich nicht. Wähl in den Funkeinstellungen der
App das Preset, das in deiner Gegend gilt. Außerhalb der unten genannten
Gebiete nutzt Europa **EU/UK (Narrow)**. Die Niederlande, Tschechien, Ungarn,
die Slowakei, Portugal und die Schweiz haben ein eigenes Preset. Für Limburg
in den Niederlanden gibt es eine Variante:

{{< presets >}}

Bietet dein Gerät das Preset deiner Gegend nicht an? Dann trag die 4 Werte aus
der Tabelle von Hand in die Funkeinstellungen der App ein: Frequenz, Bandbreite,
Spreading Factor und Coding Rate. Ein Knoten mit anderen Werten hört das Mesh
nicht.

Unsicher? Deine [lokale Gruppe](/community/) weiß, welches Preset in deiner
Gegend gilt. Die App lädt diese Liste vom MeshCore-Projekt herunter. Für ein
neues Preset brauchst du deshalb kein App-Update.

## 6. Sag Hallo {#hello}

1. **Mach dich bekannt.** Schick in der App ein *Advert*. Ein „Flood“-Advert
   läuft über die Repeater (Knoten, die Nachrichten weiterreichen). So kann
   dich jeder im Mesh hinzufügen.
   Companions machen sich nie automatisch bekannt.
2. **Finde andere.** Leute tauchen in deinen Kontakten auf, sobald ihre Adverts
   bei dir ankommen. Repeater senden standardmäßig alle 47 Stunden ein
   Flood-Advert. Bis sich deine Liste füllt, können also 2 Tage vergehen.
3. **Schick eine Nachricht.** Öffne einen Kontakt und schreib los. Die erste
   Nachricht geht als Flood durchs Netz. Der Empfänger meldet den Weg zurück,
   den sie genommen hat, und spätere Nachrichten nehmen diesen Weg.
4. **Tritt Kanälen bei.** Der Kanal **Public** ist schon eingerichtet. Alles,
   was du dort schreibst, erreicht jeden im Mesh. Den *Hashtag-Kanal* deiner
   Region (ein Name, der mit `#` beginnt) fügst du hinzu, indem du seinen
   Namen eintippst. Deine [lokale Gruppe](/community/) sagt dir, welche Kanäle
   aktiv sind.

## Wenn etwas nicht klappt {#troubleshooting}

**Die App findet mein Gerät nicht per Bluetooth.**
Wahrscheinlich hast du den USB-Companion geflasht. Flashe neu und wähl die
Bluetooth-Version. Beim Heltec V3 hat die kleine eingebaute Bluetooth-Antenne
nur wenig Reichweite. Halte das Handy nah dran.

**Die Kopplung schlägt immer wieder fehl.**
Entferne das Gerät aus den Bluetooth-Einstellungen deines Handys, starte
Bluetooth neu und kopple erneut mit der PIN auf dem Display oder `123456`.

**In meinen Kontakten taucht niemand auf.**
Prüf, ob dein Preset zu deiner Gegend passt. Schick ein Flood-Advert. Ist kein
Repeater in Reichweite, hörst du nur Funkgeräte in deiner Nähe. Auf der
[Kartenseite](/map/) siehst du, wo Repeater stehen.

**Ein Kontakt zeigt „zuletzt gesehen“ vor Tagen, obwohl er aktiv ist.**
Einer der beiden Knoten hat die falsche Uhrzeit. Ein Companion übernimmt die
Uhrzeit von deinem Handy. Bei Repeatern und Room-Servern (Knoten, die
Nachrichten für eine Gruppe speichern) muss der Besitzer die Uhrzeit stellen.

**Eine Direktnachricht kommt nie an.**
Du und die andere Person braucht einander als Kontakt. Ein Knoten verwirft Nachrichten
von Unbekannten, ohne dem Absender Bescheid zu geben. Schick ein Flood-Advert
und bitte die andere Person, auch eins zu senden. Prüf in der App, ob sie neue
Kontakte automatisch hinzufügt. Sie fügt nur Knoten innerhalb ihres Hop-Limits
hinzu.

**Alte Kontakte funktionieren, neue verbinden sich nie.**
Eine erste Nachricht geht als Flood raus. Ein Repeater reicht sie nur weiter,
wenn er die Region der Nachricht führt. Spätere Nachrichten folgen einem
gelernten Weg, und den hält keine Regionsprüfung auf. Frag deine
[lokale Gruppe](/community/), welche Regionen die Repeater in deiner Umgebung
führen, und prüf [die Einstellungen für deine Gegend](/guides/settings/#traffic).

**Die App verbindet sich nicht mehr mit deinem Companion.**
Manche Boards haben eine Benutzertaste, etwa einige RAK-Boards und der
Heltec T114. Halte sie in den ersten 8 Sekunden nach dem Start gedrückt.
Der Companion öffnet dann eine Rettungskonsole über USB. In der Konsole auf
[flasher.meshcore.io](https://flasher.meshcore.io) setzt `set pin <pin>` eine
neue Bluetooth-PIN, und `erase` löscht das Gerät.

**Der Flasher kann unter Linux den seriellen Port nicht öffnen.**
Dein Benutzer braucht Zugriff auf den Port, zum Beispiel über
`sudo setfacl -m u:$USER:rw /dev/ttyUSB0` oder als Mitglied der Gruppe
`dialout`.

**Etwas anderes.** Die
[MeshCore-FAQ](https://github.com/meshcore-dev/MeshCore/blob/main/docs/faq.md)
behandelt viele weitere Probleme.
