---
title: Was ist MeshCore?
lead: MeshCore schickt Textnachrichten per Funk von Knoten zu Knoten. Dafür brauchst du weder Internet noch Abo.
description: 'Was MeshCore ist und was nicht: Knotenarten, Routing, Verschlüsselung und das 868-MHz-Band.'
eyebrow: MeshCore v1.18.0
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '2a40da22'
  seeded: '2026-11-04'
  fields: {title: '06eda66b', lead: 'c0174569', description: 'c2255f49', eyebrow: '8610c822'}
  sections: ['aa768ac3', '92fc3ea7', '0a55792c', 'c3de803d', '493b444f', '429f699c', 'f8008f48', '203a07ef', '0894fe81']
  blocks: ['c3c9c568', '55e4248c', 'c0324d05', 'b20e61c3', 'ac039316', '68ed3005', 'cabeb32d', 'b2ca68ba', '681d55b9', 'd1df283f', '0d0e2a8b', '0596f602', 'eec63bed', '183a79e4', '47910535', 'd5a92bbf', 'b44d4637', '431021a0', '83c03732', 'e908ca85', '8f79fbf9', '3323d83e', '857c37dc', '0c4d0dd2', 'bd238f09', '794792be', '5d796ffb', '1a490368', 'f0dd237f', '3182d5c8', '02f1fe2f', 'e6b5b258']
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

- **Es ist nicht das Internet und kein Telefon.** MeshCore schickt kurze
  Textnachrichten, etwa so lang wie eine SMS auf deinem Handy. Es gibt keine Sprachübertragung,
  keine Fotos, keine Videos und keine Webseiten. Eine normale Telefonnummer erreichst du nicht.
- **Es ist kein Notrufdienst.** Kein Notrufdienst verspricht, im Mesh
  mitzuhören. Niemand verspricht, dass jemand deine Nachricht liest.
- **Es geht nicht sofort und nicht überall.** Eine Nachricht springt von Funkgerät zu
  Funkgerät und kann ein paar Sekunden brauchen oder gar nicht ankommen. Ob sie
  durchkommt, hängt von den Repeatern um dich herum ab, von Höhe, Gebäuden und deiner
  Antenne. Ein kleines Funkgerät im Haus erreicht oft niemanden. Ein Repeater auf einem Dach
  reicht kilometerweit.
- **Es ist kein Dienst, den jemand für dich betreibt.** Es gibt keinen Anbieter, keinen
  Helpdesk und keine Zusage zur Abdeckung. Das Mesh gibt es dort, wo Leute aus der
  Community Repeater aufgestellt haben.
- **Nicht alles im Mesh ist privat.** Direktnachrichten sind verschlüsselt. Public und die
  Hashtag-Kanäle kann aber jeder lesen. Den Namen deines Knotens und deine geteilte Position
  sieht jeder in Reichweite. [Observer](/network/) melden, was sie hören, an öffentliche
  Karten. Der [Abschnitt zur Verschlüsselung](#encryption) erklärt, was privat bleibt.
- **Es ist nicht unbegrenzt.** Alle in einer Gegend teilen sich einen Funkkanal. Die Regeln
  für das [868-MHz-Band](#band) begrenzen, wie lange jedes Funkgerät senden darf.
  Jede Nachricht nimmt allen anderen Sendezeit weg. Bots, häufige Adverts und
  Testnachrichten bremsen das Mesh deshalb für alle.
- **Es ist nicht Meshtastic.** Meshtastic ist ein anderes System, das auf weitgehend denselben
  Boards läuft. Die beiden können nicht miteinander kommunizieren.

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

- Mit anderen in Kontakt bleiben: beim Wandern, auf See und auf Festivals, wo das Mobilfunknetz
  überlastet ist oder fehlt.
- Ein Ersatzkanal für Familie oder Nachbarn, wenn Strom oder Mobilfunknetze
  ausfallen.
- Ein Ersatz für lokale Behörden, wenn ihre üblichen Netze ausfallen.
- Lokaler Chat auf Funkgeräten, die man selbst besitzt.
- Ein Such- und Rettungsteam in Kontakt halten, wo es kein Mobilfunknetz gibt.
  MeshCore SAR, eine Community-App unter [Projekte](/projects/), ergänzt Karten und
  geteilte Standorte.
- Einen abgelegenen Standort von zu Hause aus prüfen. Repeater und Sensorknoten melden
  ihre Batteriespannung und andere Messwerte, wenn du sie abfragst.
- Einen Sensor überwachen. Auf einem Sensorknoten läuft die MeshCore-Firmware für
  Messungen. Er speichert einen Verlauf seiner Batteriespannung. Meldest du dich als
  Admin an, warnt er dich, wenn die Batterie schwach wird. Warnungen für andere
  Messwerte ergänzt du mit eigenem Code.
- Etwas aus der Ferne schalten, etwa eine Pumpe. Das ergänzt du in der
  Sensor-Firmware mit eigenem Code.
- Mit Funk, Antennen, Solarstrom und Open-Source-Software experimentieren.

Einige Behörden bauen oder testen eine Rückfallebene auf Basis von MeshCore. Wir haben diese Beispiele im November 2026 geprüft.

- Der Zyklon Gabrielle legte in Tairāwhiti, Neuseeland, die gesamte Kommunikation lahm. Im
  September 2025 nannte der Katastrophenschutz der Region MeshCore
  [einen von mindestens 6 Ausweichwegen für die Kommunikation](https://www.scoop.co.nz/stories/AK2509/S00669.htm).
  Der Katastrophenschutz baute außerdem Solar-Repeater als Rückgrat auf.
- Der deutsche Landkreis Bad Kissingen
  [baut ein Textnetz auf Basis von MeshCore auf](https://www.landkreis-badkissingen.de/wirtschaft/digitalisierung/kommunikationsnetze/index.html).
  Es ist für Behörden, Rettungsdienste und kritische Einrichtungen gedacht. Die Feuerwehrhäuser
  kommen zuerst ans Netz.
- Der Gemeinderat von Hilversum in den Niederlanden
  [stimmte mit 34 zu 1 für einen Probebetrieb](https://hilversum.nl/nieuwsoverzicht/gemeenteraad-buigt-zich-over-financien)
  mit einem Repeater auf dem Rathausturm. Die Gemeinde
  [wertet ihn im Herbst 2027 aus](https://www.spreekbuis.nl/hilversum-start-proef-met-onafhankelijk-noodcommunicatienetwerk-meshcore/).
- Zwei niederländische Sicherheitsregionen (sie organisieren die Bewältigung von Krisen)
  experimentieren mit MeshCore:
  [Süd-Limburg](https://nos.nl/nieuwsuur/artikel/2607176-communicatie-hulpdiensten-valt-uit-bij-lange-stroomstoring-oplossing-niet-in-zicht)
  und [Drenthe](https://www.rtvdrenthe.nl/nieuws/18438486/hackerspace-drenthe-werkt-aan-een-noodnetwerk-voor-de-provincie).
  Drenthe hält es für zu früh, um zu sagen, wie oder wann die Region MeshCore nutzen könnte.
- In Dalfsen, ebenfalls in den Niederlanden,
  [betreiben Freiwillige ein Pilotprojekt gemeinsam mit den Gemeinden](https://noodnetoverijssel.nl/).
  Sie setzen zuerst auf Sprechfunk und nutzen MeshCore als zweite Ebene für Text.

Niemand verspricht, dass jemand deine Nachricht im Mesh in deiner Nähe liest.

## Woher die Daten kommen {#data}

Die Suche auf der Seite [lokale Gruppen](/community/) findet Orte mithilfe einer
Kopie der freien Orts- und Postleitzahlenlisten von [GeoNames](https://www.geonames.org/),
lizenziert unter
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Die Kopie liegt auf
dieser Website. Deine Suche verlässt dein Gerät nie, und keine Anfrage geht an
GeoNames.
