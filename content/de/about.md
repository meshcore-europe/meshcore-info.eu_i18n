---
title: Was ist MeshCore?
lead: MeshCore schickt Textnachrichten per Funk, von Knoten zu Knoten. Es funktioniert ohne Internet und ohne Abo.
description: 'Was MeshCore ist und was nicht: das Mesh, Companions, Repeater und Room-Server, Routing, Verschlüsselung und das 868-MHz-Band in Europa.'
eyebrow: MeshCore v1.18.0
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '33e571f0'
  seeded: '2026-10-26'
  fields: {title: '06eda66b', lead: 'c0174569', description: '658f8a01', eyebrow: '8610c822'}
  sections: ['a3a6c1ff', '007314d2', 'f1f23981', '493b444f', '429f699c', 'f8008f48', '655373a9']
---

MeshCore ist freie Software für kleine LoRa-Funkgeräte. LoRa ist eine Funktechnik,
die wenig Daten weit überträgt, mit sehr wenig Strom. Ein Funkgerät mit MeshCore
heißt *Knoten*. Gekoppelt mit der App auf deinem Handy oder Laptop, oder mit eigenem
Bildschirm und eigener Tastatur, schickt es Text an Menschen, die Kilometer entfernt sind. Dazwischen gibt es keinen Sendemast, Router oder Anbieter.

MeshCore überträgt nur kurze Textnachrichten: keine Sprache, keine Fotos und keinen
Internetverkehr.
Eine Nachricht kann ein paar Sekunden brauchen, und ob sie ankommt, hängt von den
Repeatern in deiner Umgebung ab. MeshCore ersetzt nicht die Rettungsdienste: Im
Notfall rufst du 112.

Die Software ist Open Source und wird auf
[meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore) unter der MIT-Lizenz
entwickelt.

## Das Mesh in einer Minute {#mesh}

Ein LoRa-Funkgerät reicht in einer Stadt ein paar Kilometer weit, und von einem
Hügel oder einem Dach aus viel weiter. Um weiter zu kommen, geben Funkgeräte Nachrichten
füreinander weiter: Das ist ein *Mesh*. Bei MeshCore übernehmen Funkgeräte namens *Repeater*
das Weitergeben. Ein Repeater, der eine Nachricht hört, sendet sie erneut, so kann sie eine ganze Region durchqueren.

Das Mesh gehört niemandem. Jeder Knoten und jeder Repeater gehört jemandem aus der
Community. Das Mesh ist so gut wie die Repeater, die Leute aufstellen.

## Die 3 Arten von Knoten {#roles}

Die Art eines Knotens wählst du beim Flashen. Dein erster Knoten ist ein Companion.

**Companion.** Dein eigenes Funkgerät. Es koppelt sich über Bluetooth oder USB mit der
MeshCore-App auf deinem Handy oder Laptop; manche haben einen eigenen Bildschirm und eine eigene Tastatur. In der App
liest und tippst du. Der Companion speichert deine Kontakte und Kanäle
sowie die Nachrichten, die ankamen, während die App nicht verbunden war. Ein Companion gibt keine Nachrichten für andere weiter.

**Repeater.** Ein hoch platziertes Funkgerät, das Nachrichten für alle weitergibt. Die meisten
laufen mit Solarstrom. Einen eigenen brauchst du nur dort, wo das Mesh noch nicht
hinreicht. Er hat keine eigene App. Du richtest ihn über USB ein oder
meldest dich mit einem Passwort an und verwaltest ihn über Funk. Der
[Repeater-Leitfaden](/repeater-guide/) zeigt, wie das geht.

**Room-Server.** Ein kleines Schwarzes Brett im Mesh. Wenn du dich anmeldest, bekommst du
die Beiträge, die du außerhalb der Reichweite verpasst hast, bis zu den letzten 32. Eine lokale Gruppe
nutzt einen für Ankündigungen.

## Wie eine Nachricht ihren Weg findet {#routing}

Jeder Knoten hat einen geheimen Schlüssel und einen öffentlichen Schlüssel. Der öffentliche Schlüssel ist seine Identität. Ein Knoten
kündigt sich mit einem *Advert* an: ein signiertes Paket mit seinem Namen und, wenn du
willst, seiner Position. Jemand erscheint in deinen Kontakten, nachdem dich eines seiner
Adverts erreicht hat oder wenn du seinen QR-Code scannst. Die App hat einen Knopf, um dein eigenes zu senden.

Deine erste Nachricht an einen Kontakt geht als *Flood* raus. Jeder Repeater, der
sie hört, gibt sie einmal weiter und hängt unterwegs seine eigene kurze ID an. Die Antwort
bringt diese Liste von IDs zurück. Von da an folgen deine Nachrichten an diesen Kontakt
dem aufgezeichneten Pfad, und nur die Repeater darauf senden. Wenn der Pfad
abreißt, floodet die App erneut.

Nachrichten an einen Kanal haben keine einzelne Adresse, deshalb flooden sie immer.
Repeater merken sich, was sie kürzlich weitergegeben haben, und verwerfen Kopien, die
über einen anderen Weg noch einmal ankommen. Eine Nachricht kann bis zu 64 Repeater durchlaufen, oder 32, wo das Preset 2-Byte-IDs
verwendet.

## Verschlüsselung und Privatsphäre {#encryption}

Deine Direktnachrichten sind Ende-zu-Ende verschlüsselt: Nur du und die andere Person
können sie lesen. Ein Repeater sieht nur einen 1-Byte-Hinweis darauf, für wen ein Paket bestimmt ist.

Kanäle sind mit einem gemeinsamen Schlüssel verschlüsselt. Wer sie lesen kann, hängt also davon ab, wer
diesen Schlüssel hat:

- **Public** ist auf jedem Companion eingerichtet. Sein Schlüssel ist veröffentlicht, also
  kann jeder den Kanal lesen.
- **Hashtag-Kanäle** wie `#utrecht` leiten ihren Schlüssel aus ihrem Namen ab.
  Jeder, der den Namen kennt, kann beitreten, behandle sie also ebenfalls als öffentlich.
- **Private Kanäle** nutzen einen zufälligen Schlüssel, den du selbst weitergibst, zum Beispiel
  als QR-Code.

Adverts sind signiert, aber nicht verschlüsselt. Der Name deines Knotens, und seine Position, wenn
du sie teilst, sind für jeden in Reichweite sichtbar. Wähle einen Namen, der nicht mehr verrät,
als du willst.

## Das 868-MHz-Band in Europa {#band}

In Europa nutzt MeshCore einen kleinen Teil des 868-MHz-Bands, den jeder ohne Lizenz
nutzen darf. Sein europäisches Funk-Preset, EU/UK (Narrow), liegt bei
869.618 MHz auf einem 62.5 kHz breiten Kanal. Das liegt innerhalb des Teilbands 869.40-869.65 MHz,
das bis zu 500 mW e.r.p. erlaubt. Ein Gerät darf dort höchstens 10%
der Zeit senden. Der
[Rechtsteil des Repeater-Leitfadens](/repeater-guide/#legal) enthält die Details
und die Grenzwerte pro Land.

Alle in einem Gebiet nutzen dasselbe Preset, sonst können sich ihre Funkgeräte nicht
hören. Manche Länder und Regionen nutzen eine Variante: Deine
[lokale Gruppe](/community/) weiß, welche.

## Wofür Leute es nutzen {#uses}

- In Kontakt bleiben auf Wanderungen, auf See und auf Festivals, wo das Mobilfunknetz
  überlastet ist oder fehlt.
- Ein Ersatzkanal für Familie oder Nachbarn, wenn Strom oder Mobilfunk
  ausfallen.
- Lokaler Chat über Funkgeräte, die den Leuten selbst gehören.
- Experimentieren mit Funk, Antennen, Solarstrom und Open-Source-Software.
