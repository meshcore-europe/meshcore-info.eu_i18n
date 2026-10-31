---
title: Antennen-Ratgeber
lead: Die richtige Antenne, gut montiert, reicht weiter als mehr Leistung. Prüf die Antenne an deinem Companion, dann wähl eine für einen Repeater aus, schließ sie an und montier sie.
description: 'Eine MeshCore-Antenne für 868 MHz auswählen und montieren: Stabantenne am Companion prüfen, Antennentypen und Gewinn, Steckverbinder, Kabelverlust pro Meter, Filter, Montage und wie der Gewinn zur gesetzlichen Grenze zählt.'
eyebrow: Companion und Repeater · 868 MHz
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'f828c4aa'
  seeded: '2026-10-31'
  fields: {title: '3a76cb0e', lead: 'd82ec429', description: 'ce3f3e73', eyebrow: 'd2203a35'}
  sections: ['908e2678', 'f9b96f42', 'ca18da90', 'bcfb40ec', '851afd23', '8b7a2209', 'd8832cfa', '5b70b9e8', '14a38e92', 'a5dc1e34', 'de04ca41', 'a23f19c6', '93846db4']
  blocks: ['908e2678', '0868bca9', '081db416', 'ad1da217', '73844333', 'aa14f1b1', '07e4fbad', '32d64d0d', 'ef66133c', '558c115b', '5d28e314', '57d6e138', 'e9b3d055', 'dd757d4a', '2cbd0b58', '21c67ec0', '306a3ded', 'fa46c89f', '1e6ccb3a', 'a3e53320', '6ae131c0', '98f350c6', '138d049d', '3bd28746', '2fc98ff1', '5ea29ee5', 'cfbd64e1', '48833347', '56a82a5c', '4ef7e883', '711e4fee', '1f7844ed', '6b188411', '8da9aa78', '4c2d8bbc', 'a721a9d0', '69c1dc1a', 'a631dbfa', '3f9f3471', '5af4ae3b', 'fa5095fd', '65eeb436', '15aa0eca', 'a8f5b505', '57f35115', '8e5e4975', '89764d3d']
---

Höhe, eine abgestimmte Antenne und ein kurzes Kabel bringen mehr Reichweite
als jedes zusätzliche Milliwatt. Dieser Ratgeber beginnt beim Companion,
dem Funkgerät, von dem aus du Nachrichten schreibst. Danach geht es um die
Antenne an einem Repeater. Das ist ein Knoten, der Nachrichten von einem
Dach oder Mast aus weitergibt.

## Dein Companion {#companion}

{{< callout type="warning" >}}
Schraub die Antenne an, bevor du das Funkgerät einschaltest. Ein LoRa-Funkgerät,
das ohne Antenne sendet, kann seinen eigenen Chip beschädigen.
{{< /callout >}}

Die Antenne, die bei deinem Board dabei war, reicht aus. Schraub sie an, halte
den Knoten aufrecht und schreib los. Eine bessere
Antenne am Companion bringt wenig; ein Repeater in Reichweite bringt viel.

Kauf eine eigene Stabantenne nur, wenn die mitgelieferte kaputt ist oder fehlt.
Nicht jede Stabantenne, die für 868 MHz verkauft wird, ist darauf abgestimmt.
[Prüf sie mit einem NanoVNA](#nanovna), einem Antennenanalysator im Taschenformat,
bevor du ihr vertraust. Oder leih dir eine von einem Board, das funktioniert.

Ein Knoten neben einem starken Sender hört weniger, als er sollte. Ein kleiner
[SAW-Filter (Oberflächenwellenfilter)](#filters) zwischen Funkgerät und
Antenne hält diesen Sender vom Empfänger fern. Prüf vorher sein Datenblatt:

- **Maximale Eingangsleistung.** Der Filter sitzt auch im Pfad deiner eigenen
  Aussendung. Ein Board, das mit 22 dBm (160 mW) in einen Filter für 15 dBm
  sendet, zerstört den Filter.
- **Durchlassbereich.** Er muss die Frequenz deines Presets enthalten. Ein Filter
  für 868.65 bis 869.25 MHz lässt den Kanal EU/UK (Narrow) auf
  869.618 MHz nicht durch.

## Antennentypen für einen Repeater {#types}

Jede Antenne im Mesh steht aufrecht. Wähl den Typ danach, wo die Knoten
stehen, die du erreichen willst:

- **Glasfaser-Kollinearantenne.** Ein weißes Rohr auf einem Mast, mit Gewinn rund
  um den ganzen Horizont. Die übliche Wahl für einen Repeater, der eine
  Stadt versorgt.
- **Dipol.** Kürzer, mit weniger Gewinn und einer hohen Strahlungskeule.
  Er erreicht Knoten unter und über dir besser als eine Kollinear-Antenne,
  etwa von einem Hügel über einem Tal.
- **Yagi.** Ein Ausleger mit Querelementen, auf einen Ort gerichtet. Sie
  erreicht einen einzelnen fernen Repeater und sonst wenig. Montier sie mit
  senkrechten Elementen, denn ihre Polarisation folgt den Elementen.

## Gewinn und Strahlungskeule {#gain}

Gewinn erzeugt keine zusätzliche Leistung. Er nimmt das Signal, das nach oben
und unten ginge, und schickt es den Horizont entlang. Wie eine Taschenlampe,
die du bündelst: dieselbe Batterie, ein längerer und schmalerer Strahl. Ein Dipol
und eine Kollinear-Antenne desselben Herstellers zeigen das:

| Antenne | Gewinn | Vertikaler Öffnungswinkel |
|---|---|---|
| Dipol (Sirio SO 868-915-2) | 2.2 dBi | 88 Grad |
| Glasfaser-Kollinearantenne (Sirio SPO 868-915-6) | 5.8 dBi | 23 Grad |

{{< gain >}}

Das Diagramm zeigt einen Schnitt durch den Mast, von der Seite gesehen. Dreh es um den
Mast, und du hast die ganze Strahlungskeule: einen Donut beim Dipol, eine flache
Scheibe bei der Kollinear-Antenne. Eine aufrechte Antenne sendet rundum in jede
Richtung gleich. Außerhalb der gezeichneten Keule hört das Signal nicht auf.
Es ist schwächer, reicht aber noch für einen Knoten in der Nähe.

Auf einem Dach willst du eine flache Keule. Auf einem Hügel hoch über den Knoten
geht eine Keule von 23 Grad über ihre Köpfe hinweg; ein Dipol deckt sie ab. Eine
Yagi geht noch weiter: 16.6 dBi in einer Keule, 23 Grad hoch
und 25 Grad breit (Amphenol Procom
7176870), und nichts zur Seite.

Gewinn gibt man gegenüber einer Referenz an. dBi bezieht sich auf eine ideale Antenne,
die in jede Richtung gleich sendet. dBd bezieht sich auf einen Halbwellendipol,
der selbst 2.15 dBi hat: Selbst die einfachste Antenne sendet nichts senkrecht
nach oben oder unten. Ein längerer Dipol mit 1.25 Wellenlängen erreicht 5.2 dBi.
Eine Kollinear-Antenne stapelt stattdessen Halbwellenelemente übereinander. Je mehr
sie stapelt, desto höher ist der Gewinn. Drückst du dasselbe Signal in den halben Raum,
ist es dort doppelt so stark: 3 dB. In ein Viertel gedrückt, ist es 4-mal so stark: 6 dB.
Hersteller geben den Gewinn in dBi an; die gesetzliche Grenze rechnet in dBd, siehe
[Innerhalb der gesetzlichen Grenze](#legal).

### Welcher Gewinn für deinen Standort {#choose-gain}

- **Hügel, Täler oder eine dichte Stadt: etwa 3 dBi.** Die hohe Keule erreicht
  Knoten über und unter dir, und um Hänge und Gebäude im Weg herum.
  Es gilt auch umgekehrt: Aus einem Tal geht eine flache Keule unter einem
  Repeater auf dem Hügel darüber hindurch. Die RAKwireless RAKARG12 ist so eine:
  ein Glasfaserrohr von 36 cm.
- **Vororte oder eine Stadt mit niedrigen Dächern: 5 bis 6 dBi.** Die übliche
  Glasfaser-Kollinearantenne.
- **Flaches, offenes Land: 8 bis 10 dBi.** Die flachste Keule reicht am
  weitesten den Horizont entlang. Hoch montiert geht sie über die Knoten in
  der Nähe hinweg.

Der Gewinn im Namen ist der beste Wert im ganzen Band der Antenne.
Die RAKARG12, als 3 dBi verkauft, hat 2.8 dBi bei 865 bis 870 MHz. Lies in der
Gewinntabelle des Datenblatts den Wert bei der Frequenz deines Presets ab.

Über 7 dBi liegt ein Board mit 22 dBm über der gesetzlichen Grenze. Das gilt
nicht, wenn Kabel- und Filterverluste den Unterschied ausgleichen. Senk die
Sendeleistung entsprechend ab.

Hoher Gewinn hilft nur, wenn du weißt, wo die Knoten sind: entlang des Horizonts
um einen Repeater, oder bei einer Yagi ein ferner Repeater. Einen Companion
in der Hand richtest du in jede Richtung. Deshalb passt der niedrige Gewinn
seiner mitgelieferten Antenne am besten zu ihm.

## Warum senkrecht {#vertical}

Antennen hören einander am besten, wenn sie in dieselbe Richtung zeigen.
Der Verlust wächst mit dem Winkel zwischen ihnen: 45 Grad kosten 3 dB,
also die Hälfte deines Signals. Bei 90 Grad, eine liegende Antenne gegen
eine aufrechte, kommt theoretisch nichts an. Das Mesh steht aufrecht, also
stellst du auch deine Antenne aufrecht. Das gilt auch für einen Companion auf dem
Schreibtisch: Legst du ihn hin, hört jeder Knoten um dich herum weniger.

## Stecker {#connectors}

Bestell die Antenne mit dem Stecker,
den dein Board hat. Jeder Adapter ist eine weitere Verbindung, die du abdichten musst, und
kostet Signal.

- **SMA.** Ein Schraubstecker, etwa 6 mm breit. Die Buchse an den meisten Boards
  hat in der Mitte ein Loch; die Antenne hat den Stift. Ein Stecker dieser
  Art verliert etwa 0.03 dB bei 868 MHz.
- **RP-SMA.** Dasselbe Gehäuse und Gewinde wie SMA, mit vertauschtem Stift
  und Loch. Er sieht aus wie SMA und passt nicht dazu. Prüf vor der
  Bestellung, welchen dein Board hat.
- **U.FL (IPEX).** Eine winzige Steckbuchse direkt auf dem Board. Ein kurzes
  Pigtail-Kabel führt von dort zu einer SMA-Buchse im Gehäuse. Sie ist für
  30 Steckzyklen ausgelegt. Steck sie also einmal an und lass sie dann stecken.
- **N.** Der große Schraubstecker an Glasfaser-Antennen und dickem
  Kabel. Er verliert höchstens 0.05 dB. Ein Repeater braucht einen
  Adapter oder ein Pigtail von N auf die SMA-Buchse des Boards.

## Kabelverlust {#cable}

Ein Kabel kostet Signal, bevor dieses die Antenne verlässt, in beide Richtungen. 3 dB
sind die Hälfte deiner Leistung. Die Herstellerangaben pro Meter, bei 868 bis 900 MHz:

| Kabel | Verlust pro Meter | Verlust auf 5 m |
|---|---|---|
| RG174 | 1.02 dB | 5.1 dB |
| RG316 | 0.78 dB | 3.9 dB |
| RG58 | 0.45 dB | 2.2 dB |
| H-155 | 0.27 dB | 1.4 dB |
| LMR-240 | 0.25 dB | 1.2 dB |
| Ecoflex 10 | 0.13 dB | 0.7 dB |
| LMR-400 | 0.13 dB | 0.6 dB |

3 Meter RG174, das dünne Pigtail, das bei vielen Boards dabei ist, kosten die
Hälfte deiner Leistung. Montier das Board mit einem kurzen Pigtail an der Antenne,
oder führ ein dickes Kabel zu ihr. Rechne jeden Adapter und Filter im Pfad zur
Summe dazu.

## Filter {#filters}

Ein Filter sitzt zwischen Funkgerät und Antenne. Er lässt dein Band durch
und sperrt den Rest. So übersteuert ein starker Sender in der Nähe den
Empfänger nicht. Du brauchst einen, wenn ein Knoten in der Nähe anderer
Sender weniger hört, als er sollte. Ein Repeater auf einem Mast mit
Mobilfunk-Basisstationen ist so ein Knoten. Ein Filter kostet Signal in
beide Richtungen: Rechne seinen Verlust ein wie beim Kabel.

| | SAW-Filter | Hohlraumfilter |
|---|---|---|
| Größe | Ein paar Millimeter, auf einem kleinen Board | Ein Metallblock oder ein Rohr |
| Verlust eines guten Filters | unter 2 dB | unter 1 dB |
| Maximale Eingangsleistung eines guten Filters | 500 mW | mehrere Watt |

Der sysmocom cf866.5-kt30 ist zum Beispiel ein Hohlraumfilter für 863 bis
870 MHz. Er verliert höchstens 1.0 dB und verträgt 30 W. Er ist für
Innenräume gebaut. Setz ihn also am Mast in ein abgedichtetes Gehäuse.

Filter unterscheiden sich stark. Prüf also das Datenblatt, bevor du kaufst.
Die angegebene Eingangsleistung muss über deiner Sendeleistung liegen. Der
Durchlassbereich muss die Frequenz deines Presets enthalten.

## Montage {#mounting}

- **Über der Dachkante.** Die Antenne braucht freie Sicht in jede
  Richtung, die sie versorgt. Schon wenige Meter über den umliegenden
  Dächern helfen. [Standort wählen](/repeater-guide/#site) im
  Repeater-Ratgeber zeigt dir, wie du die Sicht prüfst.
- **Abstand zu Metall.** Dachrinnen, Masten, andere Antennen und Metalldächer
  direkt neben der Antenne verändern ihr Strahlungsmuster und ihre
  Abstimmung. Montier sie oben auf dem Mast, nicht daneben.
- **Senkrecht.** Nimm eine Wasserwaage, siehe [Warum senkrecht](#vertical).
- **Tropfschlaufe.** Lass das Kabel unter dem Steckverbinder durchhängen,
  bevor es nach oben oder hinein geht. Dann tropft Wasser ab, statt in die
  Verbindung zu laufen.
- **Dichte jeden Steckverbinder im Freien ab.** Wasser im Verbinder erhöht
  den Verlust und lässt den Stift korrodieren. Dichte ihn gegen Regen ab
  und prüf die Abdichtung jedes Jahr.
- **Blitz.** Eine Antenne auf dem Dach ist ein Ziel. Ein
  Gasentladungsableiter im Kabel spricht bei einer Überspannung an und
  leitet sie zur Erde ab. Halte dich bei der Erdung an
  [Hardware](/repeater-guide/#hardware) im Repeater-Ratgeber und an deine
  örtlichen Vorschriften.

## Innerhalb der gesetzlichen Grenze {#legal}

{{< callout type="legal" verified="2026-10-22" >}}
In Europa nutzt MeshCore das Teilband 869.40-869.65 MHz, mit höchstens
**500 mW** effektiver Strahlungsleistung (e.r.p.). Die Grenze gilt für das, was die Antenne verlässt:
Antennengewinn kommt hinzu, Kabel- und Filterverlust gehen ab. Gewinn in dBi zählt
2.15 dB weniger, weil die Grenze gegen einen Dipol gemessen wird.
{{< /callout >}}

Eine Kollinear-Antenne mit 5.8 dBi an einem Board mit 22 dBm bleibt innerhalb der Grenze. Dieselbe
Antenne an einem Board mit Verstärker überschreitet sie, bis du die Sendeleistung
absenkst. [Leistung: e.r.p. und deine Antenne](/repeater-guide/#erp) im
Repeater-Ratgeber zeigt die Rechnung und 2 durchgerechnete Beispiele.

## Eine Antenne mit einem NanoVNA prüfen {#nanovna}

Ein NanoVNA ist ein vektorieller Netzwerkanalysator im Taschenformat. Er zeigt,
auf welche Frequenz eine Antenne abgestimmt ist. So weißt du es vor der Montage.
Der NanoVNA-H misst bis 1.5 GHz und deckt damit 868 MHz ab.

1. Kalibrier ihn für 800 bis 950 MHz mit den Teilen Open, Short und Load
   aus seinem Set.
2. Schließ die Antenne über den Adapter an, den du auch am Knoten verwendest.
   Halte sie aufrecht und fern von deinem Körper und dem Tisch.
3. Lies die SWR-Kurve (Stehwellenverhältnis): Sie zeigt, wie viel Signal
   die Antenne zurückschickt. Der Tiefpunkt muss auf der Frequenz deines Presets
   liegen, 869.618 MHz bei EU/UK (Narrow). Liegt der Tiefpunkt Hunderte MHz
   daneben, ist die Antenne für ein anderes Band gebaut.

Eine Viertelwelle bei 868 MHz ist 86 mm lang (die Wellenlänge ist 345 mm).
Die Länge allein verrät dir das Band nicht, denn Hersteller falten und verlängern
Stabantennen elektrisch. Der NanoVNA verrät es dir.

## Quellen {#sources}

- Kabelverlust: [Belden 8216 (RG174)](https://catalog.belden.com/techdata/en/8216_techdata.pdf),
  das Datenblatt Huber+Suhner RG316,
  [Belden 8240 (RG58)](https://catalog.belden.com/techdata/en/8240_techdata.pdf),
  [SSB H-155](https://www.ssb.de/media/h155ssb-en.pdf),
  die Datenblätter Times Microwave LMR-240 und LMR-400,
  [SSB Ecoflex 10](https://www.rigpix.com/otherusefulinfo/coax/ecoflex10.pdf).
- Antennen: [Sirio SPO 868-915-6](https://rigpix.com/antennas/sirio_spo8689156_manual.pdf),
  das Datenblatt Sirio SO 868-915-2,
  [Amphenol Procom 7176870](https://amphenolprocom.com/products/base-station-antennas/2236-7176870),
  [RAKwireless RAKARG12](https://docs.rakwireless.com/product-categories/accessories/rakarg12/datasheet/).
- Gewinn als Signal, das in weniger Raum gedrückt wird: [RF Cafe, Einführung Antennen](https://www.rfcafe.com/references/electrical/ew-radar-handbook/antenna-introduction-basics.htm).
- Steckverbinder: die Datenblätter Rosenberger 32S102 (SMA) und 53S101 (N),
  der Katalog Hirose U.FL.
- Filter: die Produktseite sysmocom cf866.5-kt30,
  [Citel Gasentladungsableiter](https://citel.us/en/gas-tube-surge-arrestors-for-coaxial-line-protection).
- Polarisationsverlust: [University of Toronto, Friis effects](https://www.waves.utoronto.ca/prof/svhum/ece422/notes/12-friiseffects.pdf).
- Dipolgewinn nach Länge: [Wikipedia, Dipol (Antenne)](https://en.wikipedia.org/wiki/Dipole_antenna).
- Wellenlänge: Lichtgeschwindigkeit von [NIST](https://physics.nist.gov/cgi-bin/cuu/Value?c).
- NanoVNA: [NanoVNA-H](https://github.com/hugen79/NanoVNA-H).
- Gesetzliche Grenze: [CEPT ERC Recommendation 70-03](https://docdb.cept.org/document/845),
  Anhang 1, Band h1.7. Den Rest listet der [Repeater-Ratgeber](/repeater-guide/#legal)
  auf.
