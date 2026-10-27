---
title: Antennen-Ratgeber
lead: Die Antenne ist die Hälfte deines Knotens. Die richtige, gut montiert, reicht weiter als mehr Leistung. Prüfe die Antenne an deinem Companion, dann wähle, verbinde und montiere eine für einen Repeater.
description: 'Eine MeshCore-Antenne für 868 MHz wählen und montieren: Companion-Stabantenne prüfen, Antennentypen und Gewinn, Steckverbinder, Kabeldämpfung pro Meter, Filter, Montage und wie der Gewinn in die gesetzliche Grenze eingeht.'
eyebrow: Companion und Repeater · 868 MHz
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '45010ad0'
  seeded: '2026-10-26'
  fields: {title: '3a76cb0e', lead: '98430ade', description: 'ce3f3e73', eyebrow: 'd2203a35'}
  sections: ['908e2678', 'f9b96f42', '94c5bae4', 'bcfb40ec', '851afd23', '8b7a2209', 'd8832cfa', '5b70b9e8', '14a38e92', 'a5dc1e34', 'de04ca41', 'a23f19c6', '93846db4']
---

Höhe, eine abgestimmte Antenne und ein kurzes Kabel bringen mehr Reichweite
als jedes zusätzliche Milliwatt. Dieser Ratgeber beginnt beim Companion,
dem Funkgerät, von dem aus du Nachrichten schreibst. Danach geht es um die
Antenne eines Repeaters, eines Knotens, der Nachrichten von einem Dach oder
Mast aus weiterreicht.

## Dein Companion {#companion}

{{< callout type="warning" >}}
Schraube die Antenne an, bevor du das Funkgerät einschaltest. Ein LoRa-Funkgerät,
das ohne Antenne sendet, kann seinen eigenen Chip beschädigen.
{{< /callout >}}

Die Antenne, die bei deinem Board dabei war, reicht aus. Schraube sie an,
halte den Knoten aufrecht und schreibe los. Eine bessere Antenne am
Companion bringt wenig, ein Repeater in Reichweite bringt viel.

Kaufe eine separate Stabantenne nur, wenn die mitgelieferte kaputt ist oder fehlt.
Nicht jede Stabantenne, die für 868 MHz verkauft wird, ist darauf abgestimmt.
[Prüfe sie mit einem NanoVNA](#nanovna), einem Antennenanalysator im Taschenformat,
bevor du ihr vertraust, oder leihe dir eine von einem Board, das funktioniert.

Ein Knoten neben einem starken Sender hört weniger, als er sollte. Ein kleines
[SAW-Filter (Surface Acoustic Wave)](#filters) zwischen Funkgerät und Antenne
hält diesen Sender vom Empfänger fern. Prüfe zuerst sein Datenblatt:

- **Maximale Eingangsleistung.** Das Filter sitzt auch im Pfad deiner eigenen
  Sendung. Ein Board, das mit 22 dBm (160 mW) in ein Filter für 15 dBm sendet,
  zerstört das Filter.
- **Durchlassbereich.** Er muss die Frequenz deines Presets enthalten. Ein Filter
  für 868.65 bis 869.25 MHz lässt den Kanal EU/UK (Narrow) auf
  869.618 MHz nicht durch.

## Antennentypen für einen Repeater {#types}

Jede Antenne im Mesh steht aufrecht. Wähle den Typ danach, wo die Knoten
stehen, die du erreichen willst:

- **Glasfaser-Kollinearantenne.** Ein weißes Rohr auf einem Mast, mit
  Gewinn rundum am Horizont. Die Standardwahl für einen Repeater, der eine
  Stadt versorgt.
- **Dipol.** Kürzer, mit weniger Gewinn und einer hohen Keule. Er erreicht
  Knoten unter und über dir besser als eine Kollinearantenne. Das zählt auf
  einem Hügel über einem Tal.
- **Yagi.** Ein Träger mit Querelementen, auf einen Ort gerichtet. Sie
  erreicht einen einzelnen fernen Repeater und sonst kaum etwas. Montiere
  sie mit den Elementen senkrecht, denn ihre Polarisation folgt den
  Elementen.

## Gewinn und Keule {#gain}

Gewinn erzeugt keine Leistung. Er nimmt das Signal, das nach oben und
unten gehen würde, und schickt es entlang des Horizonts. Wie eine
Taschenlampe, die du fokussierst: dieselbe Batterie, ein längerer und
schmalerer Strahl. Ein Dipol und eine Kollinearantenne desselben Herstellers
zeigen es:

| Antenne | Gewinn | Vertikaler Öffnungswinkel |
|---|---|---|
| Dipol (Sirio SO 868-915-2) | 2.2 dBi | 88 Grad |
| Glasfaser-Kollinearantenne (Sirio SPO 868-915-6) | 5.8 dBi | 23 Grad |

{{< gain >}}

Das Diagramm schneidet durch den Mast, von der Seite gesehen. Drehe es um
den Mast und du hast die ganze Keule: ein Ring für den Dipol, eine flache
Scheibe für die Kollinearantenne. Eine aufrechte Antenne sendet in jede
Richtung um sich herum gleich. Außerhalb der gezeichneten Keule hört das
Signal nicht auf; es ist schwächer, für einen Knoten in der Nähe aber noch
genug.

Auf einem Dach willst du eine flache Keule. Auf einem Hügel hoch über den
Knoten geht eine Keule von 23 Grad über ihre Köpfe hinweg; ein Dipol
deckt sie ab. Eine Yagi treibt das weiter: 16.6 dBi in einer Keule von
23 Grad Höhe und 25 Grad Breite (Amphenol Procom 7176870), und nichts zu
den Seiten.

Gewinn gilt gegenüber einer Referenz. dBi vergleicht mit einer idealen
Antenne, die in jede Richtung gleich sendet. dBd vergleicht mit einem
Halbwellendipol, der selbst 2.15 dBi hat: Selbst die einfachste Antenne
sendet nichts senkrecht nach oben oder unten. Ein längerer Dipol mit
1.25 Wellenlängen erreicht 5.2 dBi. Eine Kollinearantenne stapelt
stattdessen Halbwellenelemente übereinander: je mehr sie stapelt, desto
höher der Gewinn. Drücke dasselbe Signal in den halben Raum und es ist dort
doppelt so stark: 3 dB. In ein Viertel, 4-mal so stark: 6 dB. Hersteller
geben den Gewinn in dBi an; die gesetzliche Grenze rechnet in dBd, siehe
[Innerhalb der gesetzlichen Grenze](#legal).

### Welcher Gewinn für deinen Standort {#choose-gain}

- **Hügel, Täler oder eine dichte Stadt: etwa 3 dBi.** Die hohe Keule
  erreicht Knoten über und unter dir, und rund um die Hänge und Gebäude im
  Weg. Es gilt auch umgekehrt: Aus einem Tal geht eine flache Keule unter
  einem Repeater auf dem Hügel darüber hindurch. Die RAKwireless RAKARG12
  ist so eine: ein Glasfaserrohr von 36 cm.
- **Vororte oder eine Stadt mit niedrigen Dächern: 5 bis 6 dBi.** Die
  Standard-Kollinearantenne aus Glasfaser.
- **Flaches, offenes Land: 8 bis 10 dBi.** Die flachste Keule reicht am
  weitesten entlang des Horizonts. Hoch montiert geht sie über die Knoten
  in der Nähe hinweg.

Der Gewinn im Namen ist der beste Wert über das ganze Band der Antenne. Die
RAKARG12, verkauft mit 3 dBi, hat bei 865 bis 870 MHz 2.8 dBi. Lies die
Gewinntabelle im Datenblatt bei der Frequenz deines Presets.

Über 7 dBi überschreitet ein Board mit 22 dBm die gesetzliche Grenze, außer
Kabel- und Filterdämpfung gleichen die Differenz aus. Senke die
Sendeleistung entsprechend.

Hoher Gewinn hilft nur, wenn du weißt, wo die Knoten sind: entlang des
Horizonts rund um einen Repeater, oder an einem fernen Repeater bei einer
Yagi. Ein Companion in deiner Hand zeigt in alle Richtungen, deshalb passt
der geringe Gewinn, mit dem er geliefert wurde, am besten zu ihm.

## Warum senkrecht {#vertical}

Antennen hören einander am besten, wenn sie in dieselbe Richtung zeigen.
Der Verlust wächst mit dem Winkel zwischen ihnen: 45 Grad kosten 3 dB, die
Hälfte deines Signals. Bei 90 Grad, eine liegende Antenne gegen eine
aufrechte, kommt in der Theorie nichts an. Das Mesh steht aufrecht, also
steht deine Antenne auch aufrecht. Das gilt auch für einen Companion auf
dem Schreibtisch: Legst du ihn flach hin, hört jeder Knoten um dich herum
weniger.

## Steckverbinder {#connectors}

Bestelle die Antenne mit dem Steckverbinder, den dein Board hat. Jeder
Adapter ist eine weitere Verbindung, die du abdichten musst, und mehr
verlorenes Signal.

- **SMA.** Ein Schraubverbinder von etwa 6 mm Breite. Die Buchse auf den
  meisten Boards hat in der Mitte ein Loch; die Antenne hat den Stift. Ein
  Verbinder dieser Art verliert bei 868 MHz etwa 0.03 dB.
- **RP-SMA.** Dasselbe Gehäuse und Gewinde wie SMA, mit Stift und Loch
  vertauscht. Er sieht aus wie SMA und passt nicht dazu. Prüfe, welchen
  dein Board hat, bevor du bestellst.
- **U.FL (IPEX).** Eine winzige Steckbuchse direkt auf dem Board. Ein
  kurzes Pigtail-Kabel führt von ihr zu einer SMA-Buchse im Gehäuse. Sie
  ist für 30 Steckzyklen ausgelegt, also verbinde sie einmal und lass sie
  in Ruhe.
- **N.** Der große Schraubverbinder an Glasfaserantennen und dickem Kabel.
  Er verliert höchstens 0.05 dB. Ein Repeater braucht einen Adapter oder
  ein Pigtail von N auf das SMA des Boards.

## Kabeldämpfung {#cable}

Kabel kostet Signal, bevor es die Antenne verlässt, in beide Richtungen.
3 dB sind die Hälfte deiner Leistung. Die Herstellerangaben pro Meter, bei
868 bis 900 MHz:

| Kabel | Dämpfung pro Meter | Dämpfung über 5 m |
|---|---|---|
| RG174 | 1.02 dB | 5.1 dB |
| RG316 | 0.78 dB | 3.9 dB |
| RG58 | 0.45 dB | 2.2 dB |
| H-155 | 0.27 dB | 1.4 dB |
| LMR-240 | 0.25 dB | 1.2 dB |
| Ecoflex 10 | 0.13 dB | 0.7 dB |
| LMR-400 | 0.13 dB | 0.6 dB |

3 Meter RG174, das dünne Pigtail, das vielen Boards beiliegt, verlieren die
Hälfte deiner Leistung. Montiere das Board mit einem kurzen Pigtail direkt
an der Antenne, oder lege dickes Kabel zu ihr. Rechne jeden Adapter und
Filter im Pfad zur Summe dazu.

## Filter {#filters}

Ein Filter sitzt zwischen Funkgerät und Antenne. Er lässt dein Band durch
und sperrt den Rest, damit ein starker Sender in der Nähe den Empfänger
nicht überlastet. Du brauchst einen, wenn ein Knoten in der Nähe anderer
Sender weniger hört, als er sollte. Ein Repeater auf einem Mast mit
Mobilfunk-Basisstationen ist so ein Knoten. Ein Filter kostet Signal in
beide Richtungen: Rechne seine Dämpfung wie Kabel.

| | SAW-Filter | Hohlraumfilter |
|---|---|---|
| Größe | Wenige Millimeter, auf einer kleinen Platine | Ein Metallblock oder -rohr |
| Dämpfung eines guten | unter 2 dB | unter 1 dB |
| Maximale Eingangsleistung eines guten | 500 mW | mehrere Watt |

Der sysmocom cf866.5-kt30 zum Beispiel ist ein Hohlraumfilter für 863 bis
870 MHz, der höchstens 1.0 dB verliert und 30 W verträgt. Er ist für innen
gebaut, also setze ihn an einem Mast in eine abgedichtete Box.

Filter unterscheiden sich stark, also prüfe vor dem Kauf das Datenblatt.
Seine zulässige Eingangsleistung muss über deiner Sendeleistung liegen, und
sein Durchlassbereich muss die Frequenz deines Presets enthalten.

## Montage {#mounting}

- **Über der Dachkante.** Die Antenne braucht freie Sicht in jede Richtung,
  die sie versorgt. Schon ein paar Meter über den umliegenden Dächern
  helfen. [Standort wählen](/repeater-guide/#site) im Repeater-Ratgeber
  zeigt, wie du die Sicht prüfst.
- **Weg von Metall.** Dachrinnen, Masten, andere Antennen und Metalldächer
  neben der Antenne verändern ihr Strahlungsmuster und ihre Abstimmung.
  Montiere sie oben auf dem Mast, nicht daneben.
- **Senkrecht.** Nimm eine Wasserwaage; siehe [Warum senkrecht](#vertical).
- **Tropfschleife.** Lass das Kabel unter dem Verbinder durchhängen, bevor
  es nach oben oder hinein geht. Wasser tropft dann ab, statt in die
  Verbindung zu laufen.
- **Jeden Außenverbinder abdichten.** Wasser in einem Verbinder erhöht die
  Dämpfung und lässt den Stift korrodieren. Dichte ihn gegen Regen ab und
  prüfe die Dichtung jedes Jahr.
- **Blitz.** Eine Antenne auf einem Dach ist ein Ziel. Ein Gasableiter im
  Kabel zündet bei einem Überspannungsstoß und leitet ihn zur Erde. Folge
  [Hardware](/repeater-guide/#hardware) im Repeater-Ratgeber und deinen
  örtlichen Regeln für die Erdung.

## Innerhalb der gesetzlichen Grenze {#legal}

{{< callout type="legal" verified="2026-10-22" >}}
In Europa nutzt MeshCore das Teilband 869.40-869.65 MHz, mit höchstens
**500 mW** effektiver Strahlungsleistung (e.r.p.). Die Grenze zählt, was die Antenne verlässt:
Antennengewinn kommt dazu, Kabel- und Filterdämpfung gehen ab. Gewinn in dBi zählt
2.15 dB weniger, weil die Grenze gegenüber einem Dipol gemessen wird.
{{< /callout >}}

Eine Kollinearantenne mit 5.8 dBi an einem Board mit 22 dBm bleibt innerhalb der Grenze. Dieselbe
Antenne an einem Board mit Verstärker nicht, bis du die Sendeleistung
senkst. [Leistung: e.r.p. und deine Antenne](/repeater-guide/#erp) im
Repeater-Ratgeber hat die Rechnung und 2 durchgerechnete Beispiele.

## Eine Antenne mit einem NanoVNA prüfen {#nanovna}

Ein NanoVNA ist ein vektorieller Netzwerkanalysator im Taschenformat. Er zeigt,
auf welche Frequenz eine Antenne abgestimmt ist, damit du es vor der Montage
weißt. Der NanoVNA-H misst bis 1.5 GHz, das deckt 868 MHz ab.

1. Kalibriere ihn für 800 bis 950 MHz mit den Teilen Open, Short und Load
   aus seinem Set.
2. Schließe die Antenne über den Adapter an, den sie am Knoten nutzen wird.
   Halte sie aufrecht und weg von deinem Körper und dem Tisch.
3. Lies die SWR-Kurve (Stehwellenverhältnis): Sie zeigt, wie viel Signal
   die Antenne zurückschickt. Die Senke muss auf der Frequenz deines Presets
   liegen, 869.618 MHz für EU/UK (Narrow). Eine Senke Hunderte MHz entfernt
   bedeutet, dass die Antenne für ein anderes Band gebaut ist.

Eine Viertelwelle bei 868 MHz ist 86 mm lang (die Wellenlänge ist 345 mm).
Die Länge allein verrät dir das Band nicht, weil Hersteller Stabantennen
falten und verkürzen; der NanoVNA tut es.

## Quellen {#sources}

- Kabeldämpfung: [Belden 8216 (RG174)](https://catalog.belden.com/techdata/en/8216_techdata.pdf),
  das Datenblatt Huber+Suhner RG316,
  [Belden 8240 (RG58)](https://catalog.belden.com/techdata/en/8240_techdata.pdf),
  [SSB H-155](https://www.ssb.de/media/h155ssb-en.pdf),
  die Datenblätter Times Microwave LMR-240 und LMR-400,
  [SSB Ecoflex 10](https://www.rigpix.com/otherusefulinfo/coax/ecoflex10.pdf).
- Antennen: [Sirio SPO 868-915-6](https://rigpix.com/antennas/sirio_spo8689156_manual.pdf),
  das Datenblatt Sirio SO 868-915-2,
  [Amphenol Procom 7176870](https://amphenolprocom.com/products/base-station-antennas/2236-7176870),
  [RAKwireless RAKARG12](https://docs.rakwireless.com/product-categories/accessories/rakarg12/datasheet/).
- Gewinn als in weniger Raum gedrücktes Signal: [RF Cafe, Einführung in Antennen](https://www.rfcafe.com/references/electrical/ew-radar-handbook/antenna-introduction-basics.htm).
- Steckverbinder: die Datenblätter Rosenberger 32S102 (SMA) und 53S101 (N),
  der Hirose-Katalog zu U.FL.
- Filter: die Produktseite sysmocom cf866.5-kt30,
  [Citel Gasableiter](https://citel.us/en/gas-tube-surge-arrestors-for-coaxial-line-protection).
- Polarisationsverlust: [University of Toronto, Friis effects](https://www.waves.utoronto.ca/prof/svhum/ece422/notes/12-friiseffects.pdf).
- Dipolgewinn nach Länge: [Wikipedia, Dipole antenna](https://en.wikipedia.org/wiki/Dipole_antenna).
- Wellenlänge: Lichtgeschwindigkeit vom [NIST](https://physics.nist.gov/cgi-bin/cuu/Value?c).
- NanoVNA: [NanoVNA-H](https://github.com/hugen79/NanoVNA-H).
- Gesetzliche Grenze: [CEPT ERC Recommendation 70-03](https://docdb.cept.org/document/845),
  Anhang 1, Band h1.7; der [Repeater-Ratgeber](/repeater-guide/#legal)
  nennt den Rest.
