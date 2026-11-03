---
title: Was ist MeshCore?
lead: MeshCore schickt Textnachrichten per Funk von Knoten zu Knoten. Dafür brauchst du weder Internet noch Abo.
description: 'Was MeshCore ist und was nicht: Knotenarten, Routing, der Unterschied zu Meshtastic, Verschlüsselung und das 868-MHz-Band.'
eyebrow: MeshCore v1.18.0
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '279b56a4'
  seeded: '2026-11-02'
  fields: {title: '06eda66b', lead: 'c0174569', description: '15e6d2a7', eyebrow: '8610c822'}
  sections: ['aa768ac3', '16fde264', '0a55792c', 'c3de803d', '493b444f', 'a8b2b9b4', '429f699c', 'f8008f48', '88af2bd3', '0894fe81']
  blocks: ['c3c9c568', '55e4248c', 'c0324d05', 'b20e61c3', 'fab378a5', '68ed3005', 'cabeb32d', 'b2ca68ba', '681d55b9', 'd1df283f', '0d0e2a8b', '0596f602', 'eec63bed', '183a79e4', '47910535', 'd5a92bbf', 'b44d4637', 'fc8f3129', '8dec428a', '07cbac35', '431021a0', '83c03732', 'e908ca85', '8f79fbf9', '3323d83e', '857c37dc', '0c4d0dd2', 'bd238f09', '794792be', '95e18f18', '02f1fe2f', 'e6b5b258']
---

MeshCore ist freie Software für kleine LoRa-Funkgeräte. LoRa ist eine Funktechnik,
die wenige Daten mit sehr wenig Strom weit überträgt. Ein Funkgerät mit MeshCore
heißt *Knoten*. Du koppelst es mit der App auf deinem Handy oder Laptop oder nutzt
seinen eigenen Bildschirm und seine Tastatur. Dann schickst du damit Text an Menschen, die Kilometer entfernt sind. Dazwischen gibt es keinen Funkmast, keinen Router und keinen Anbieter.

Die Software ist Open Source. Sie wird unter der MIT-Lizenz bei
[meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore) entwickelt.

## Was MeshCore nicht ist {#not}

Funk ist neu für dich? Das erwarten Leute am häufigsten von MeshCore, und das
kann es nicht.

- **Es ist weder Internet noch Telefon.** MeshCore überträgt kurze Textnachrichten,
  ungefähr so lang wie eine SMS auf deinem Handy. Sprache, Fotos, Videos
  und Websites gibt es nicht, und eine normale Telefonnummer erreichst du nicht.
- **Es ist kein Notdienst.** Kein Notdienst hört im Mesh mit, und niemand
  verspricht, dass jemand deine Nachricht liest. Ruf im Notfall die 112 an.
- **Es geht nicht sofort und nicht überall.** Eine Nachricht springt von Funkgerät zu
  Funkgerät. Das kann ein paar Sekunden dauern, oder sie kommt gar nicht an. Ob sie
  durchkommt, hängt von den Repeatern in deiner Umgebung ab, von Höhe, Gebäuden und deiner
  Antenne. Ein kleines Funkgerät im Haus erreicht oft niemanden. Ein Repeater auf einem Dach
  reicht Kilometer weit.
- **Es ist kein Dienst, den jemand für dich betreibt.** Es gibt keinen Anbieter, keinen
  Helpdesk und keine Zusage zur Abdeckung. Das Mesh gibt es dort, wo Leute aus der
  Community Repeater aufgestellt haben, und sonst nirgends.
- **Nicht alles im Mesh ist privat.** Direktnachrichten sind verschlüsselt, aber
  Public und die Hashtag-Kanäle kann jeder lesen. Auch der Name deines Knotens und
  deine geteilte Position sind für alle in Reichweite sichtbar.
  [Observer](/network/) melden, was sie hören, an öffentliche Karten. Der
  [Abschnitt zur Verschlüsselung](#encryption) erklärt, was privat bleibt.
- **Es ist nicht unbegrenzt.** Alle in einem Gebiet teilen sich einen Funkkanal, und
  die Regeln für das [868-MHz-Band](#band) begrenzen, wie lange jedes Funkgerät senden darf.
  Jede Nachricht nimmt allen anderen Sendezeit weg. Darum bremsen Bots, häufige Adverts
  und Testnachrichten das Mesh für alle.
- **Es ist nicht Meshtastic.** Meshtastic ist ein anderes System, das auf fast denselben
  Boards läuft. Die beiden können nicht miteinander kommunizieren.
  Unter [Umstieg von Meshtastic](#meshtastic) steht, was anders funktioniert.

## Das Mesh in einer Minute {#mesh}

Ein LoRa-Funkgerät reicht in einer Stadt ein paar Kilometer weit, von einem Hügel
oder Dach aus viel weiter. Für größere Strecken geben Funkgeräte Nachrichten
füreinander weiter: Das ist ein *Mesh*. Bei MeshCore übernehmen das Funkgeräte,
die *Repeater* heißen. Hört ein Repeater eine Nachricht, sendet er sie erneut.
So kommt sie durch eine ganze Region.

Das Mesh gehört niemandem. Jeder Knoten und jeder Repeater gehört jemandem aus
der Community. Das Mesh reicht so weit wie ihre Repeater.

## Die 3 Arten von Knoten {#roles}

Die Art eines Knotens legst du beim Flashen fest. Dein erster Knoten ist ein Companion.

**Companion.** Dein eigenes Funkgerät. Du koppelst es per Bluetooth oder USB mit
der MeshCore-App auf deinem Handy oder Laptop. Manche haben einen eigenen
Bildschirm und eine Tastatur. In der App liest und schreibst du. Der Companion
speichert deine Kontakte und Kanäle und die Nachrichten, die ankamen, während die
App nicht verbunden war. Ein Companion gibt keine Nachrichten für andere weiter.

**Repeater.** Ein hoch angebrachtes Funkgerät, das Nachrichten für alle weitergibt.
Die meisten laufen mit Solarstrom. Einen eigenen brauchst du nur dort, wo das
Mesh noch nicht hinkommt. Er hat keine eigene App. Du richtest ihn per USB ein
oder meldest dich mit einem Passwort an und verwaltest ihn über Funk. Wie das
geht, zeigt die [Repeater-Anleitung](/repeater-guide/).

**Room Server.** Ein kleines Schwarzes Brett im Mesh. Wenn du dich anmeldest,
bekommst du die Beiträge, die du außer Reichweite verpasst hast, bis zu den
letzten 32. Er hält sie nur im Arbeitsspeicher. Ein Neustart oder ein Stromausfall
löscht sie also. Eine lokale Gruppe nutzt einen Room Server für Ankündigungen.

## Wie eine Nachricht ihren Weg findet {#routing}

Jeder Knoten hat einen privaten Schlüssel und einen öffentlichen Schlüssel. Der
öffentliche Schlüssel ist seine Identität. Ein Knoten macht sich mit einem
*Advert* bekannt: einem signierten Paket mit seinem Namen und, wenn du willst,
seiner Position. Jemand erscheint in deinen Kontakten, nachdem dich eines
seiner Adverts erreicht hat oder wenn du seinen QR-Code scannst. Mit einem Button in der App sendest du dein eigenes.

Deine erste Nachricht an einen Kontakt geht als *Flood* raus. Jeder Repeater,
der sie hört, gibt sie einmal weiter und hängt unterwegs seine eigene kurze ID
an. Die Antwort bringt diese Liste von IDs zurück. Ab dann folgen deine
Nachrichten an diesen Kontakt dem aufgezeichneten Pfad, und nur die Repeater
darauf senden. Reißt der Pfad ab, schickt die App wieder eine Flood.

Nachrichten an einen Kanal haben keine einzelne Adresse. Sie gehen deshalb immer
als Flood raus. Repeater merken sich, was sie zuletzt weitergegeben haben, und
verwerfen Kopien, die über einen anderen Weg noch einmal ankommen. Eine Nachricht
kann bis zu 64 Repeater durchlaufen, oder 32, wenn das Preset 2-Byte-IDs nutzt.

## Umstieg von Meshtastic {#meshtastic}

Auf vielen Boards läuft entweder MeshCore oder Meshtastic, und du flashst das System, das du haben willst. Das sind die Unterschiede, die dir zuerst auffallen. Sie beziehen sich auf MeshCore
v1.18.0 und die Meshtastic-Dokumentation vom November 2026.

- **Wer Nachrichten weitergibt.** Bei MeshCore tun das nur Repeater, dein Companion
  nie. Bei Meshtastic gibt auch die Standardrolle Client Nachrichten weiter,
  außer ein anderer Knoten hat das schon getan.
- **Wie weit eine Nachricht kommt.** Eine MeshCore-Nachricht kann bis zu 64
  Repeater durchlaufen. Meshtastic stoppt standardmäßig nach 3 Hops, spätestens nach 7.
- **Messwerte von anderen Knoten.** Repeater und Sensorknoten senden bei MeshCore
  Messwerte wie die Batteriespannung, wenn du danach fragst. An das ganze Mesh
  senden sie diese nicht.
- **Das Internet.** Die MeshCore-Firmware verbindet Meshes nicht über das
  Internet. [Observer](/network/) melden Karten, was sie hören, und zwar
  nur in eine Richtung. Meshtastic hat ein eingebautes MQTT-Modul, das
  Nachrichten über das Internet zwischen Meshes übertragen kann.

## Verschlüsselung und Privatsphäre {#encryption}

Deine Direktnachrichten sind Ende-zu-Ende-verschlüsselt: Nur du und die andere
Person können sie lesen. Ein Repeater sieht nur einen 1-Byte-Hinweis darauf, an
wen ein Paket geht.

Kanäle sind mit einem gemeinsamen Schlüssel verschlüsselt. Wer sie lesen kann,
hängt also davon ab, wer diesen Schlüssel hat:

- **Public** ist auf jedem Companion eingerichtet. Sein Schlüssel ist
  öffentlich bekannt, deshalb kann jeder mitlesen.
- **Hashtag-Kanäle** wie `#utrecht` leiten ihren Schlüssel aus ihrem Namen ab.
  Wer den Namen kennt, kann beitreten. Behandle sie deshalb ebenfalls als öffentlich.
- **Private Kanäle** nutzen einen zufälligen Schlüssel, den du selbst teilst, zum
  Beispiel als QR-Code.

Adverts sind signiert, aber nicht verschlüsselt. Den Namen deines Knotens und
seine Position, falls du sie teilst, sieht jeder in Reichweite. Wähl einen Namen,
der nicht mehr verrät, als du willst.

## Das 868-MHz-Band in Europa {#band}

In Europa nutzt MeshCore einen kleinen Teil des 868-MHz-Bands, den jeder ohne
Lizenz nutzen darf. Das europäische Funk-Preset EU/UK (Narrow) liegt auf
869.618 MHz mit einem 62.5-kHz-Kanal. Das liegt im Teilband 869.40-869.65 MHz,
das bis zu 500 mW e.r.p. erlaubt. Ein Gerät darf dort höchstens 10% der Zeit
senden. Die Einzelheiten und die Grenzen pro Land findest du im
[rechtlichen Abschnitt der Repeater-Anleitung](/repeater-guide/#legal).

Alle in einer Gegend nutzen dasselbe Preset, sonst hören sich ihre Funkgeräte
nicht. Manche Länder und Regionen nutzen eine Variante: Deine
[lokale Gruppe](/community/) weiß, welche.

## Wofür Leute es nutzen {#uses}

- In Kontakt bleiben: beim Wandern, auf See und auf Festivals, wo das Mobilfunknetz
  überlastet ist oder fehlt.
- Ein Ersatzkanal für Familie oder Nachbarn, wenn Strom oder Mobilfunknetze
  ausfallen.
- Lokaler Chat über Funkgeräte, die den Leuten selbst gehören.
- Von zu Hause aus einen entfernten Standort prüfen. Repeater und Sensorknoten melden
  ihre Batteriespannung und andere Messwerte, wenn du danach fragst.
- Einen Sensor im Blick behalten. Auf einem Sensorknoten läuft die MeshCore-Firmware
  zum Messen. Er speichert einen Verlauf seiner Messwerte. Wenn du ihn abonnierst,
  warnt er dich, zum Beispiel bei schwacher Batterie.
- Etwas aus der Ferne schalten, etwa eine Pumpe. Das ergänzt du mit eigenem Code
  in der Sensor-Firmware.
- Mit Funk, Antennen, Solarstrom und Open-Source-Software experimentieren.

## Woher die Daten kommen {#data}

Die Suche auf der Seite [lokale Gruppen](/community/) findet Orte mithilfe einer
Kopie der freien Orts- und Postleitzahlenlisten von [GeoNames](https://www.geonames.org/),
lizenziert unter
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Die Kopie liegt auf
dieser Website. Deine Suche verlässt dein Gerät nie, und keine Anfrage geht an
GeoNames.
