---
title: Mach das Mesh widerstandsfähig
lead: Ist das Mesh bei dir langsam oder voller Müll? Finde heraus, woran es liegt, schalte am Repeater die passende Einstellung ein und sag deiner lokalen Gruppe Bescheid.
description: 'Floods und Spam in einem MeshCore-Mesh: wie du jede Art erkennst, welche Repeater-Einstellung hilft, wie du einen Flood siehst und wie du seine Quelle findest.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '500188ff'
  seeded: '2026-10-31'
  fields: {title: '33ec7ac8', lead: '780da19b', description: '1826e5e8'}
  sections: ['68ca5d36', '133c764a', 'a3bb5172', 'f4cc9cad', 'ace7b1ee', '89651002', 'f4dfdf59', '764c832c', 'f342b64b', 'f348e208']
  blocks: ['68ca5d36', 'c9cfbe6c', 'bcb31992', 'de7f60e4', 'e862fb9b', '0046b51f', '25f34d1d', 'c3c3ea52', '853a0f1d', '2bcea703', '871a7661', '2690aacf', 'a4aec3a1', 'd6da27c6', 'e8405458', 'f9150ee6', '8508ce40', '4b03ccd5', 'fb79c493', '695adde7', 'eba5a5b5', '836e0bac', '3497c5e8', '71c78fa1', '537d0930', '6a315252', '7c84dc56', '682e08e6', '258d7a27', '53af1400', '0dbebf97', 'ac0dca3c', '70fb4e9a', '9f055f50', 'ae90facc']
---

Kommen Nachrichten spät oder gar nicht an? Füllt sich Public mit Müll? Das
ist ein Flood: mehr Verkehr, als das Mesh tragen kann. Jemand sendet ihn aus
Versehen oder mit Absicht. Such in den Tabellen unten, was du siehst. Jede
Zeile nennt die Einstellung, die es stoppt. Schalte sie an deinem Repeater
ein, dem Knoten, der Nachrichten weitergibt. Sag dann deiner
[lokalen Gruppe](/community/) Bescheid, damit die Repeater um dich herum
dasselbe tun. Jeder Repeater, der einen Flood verwirft, lässt Sendezeit für
alle anderen frei.

## Floods aus Versehen {#mistake}

Ein Flood aus Versehen kommt von einem Knoten, dessen Besitzer nichts davon
weiß. Er hört auf, sobald der Besitzer es erfährt. Ein Advert (in den
Tabellen unten) ist das Hallo, das ein Knoten sendet, damit andere ihn
finden.

Die Einstellungen in den Tabellen leiten sich aus dem ab, was die Firmware
tut. Nicht jede hat schon einen Flood in einem echten Mesh gestoppt.

{{< callout type="warning" >}}
Manche Einstellungen auf dieser Seite brauchen die DMC-Firmware. Die
Standard-Firmware **MeshCore** 1.18.0 hat Regionen, die Hop-Limits
`flood.max.*`, die Schleifenerkennung und den Duty Cycle. Den Paketfilter
bringt die **DMC-Firmware** von
[Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore) mit. Mit seinen
Regeln verwirft dein Repeater Müll. Auch Duty-Cycle-Gating und der
Companion-Filter kommen mit der DMC-Firmware. Diese Seite bezieht sich auf
den DMC-Dev-Build 1.18.0 `ecfb2d4` vom 19. Oktober 2026. Auf der Seite zum
[Paketfilter](/guides/filter/#firmware) steht, wo du ihn bekommst.
{{< /callout >}}

| Was du siehst | Was es ist | Was hilft |
| --- | --- | --- |
| Anfragen an Repeater von einem Knoten, Tag und Nacht, und ein Mesh, das tagelang langsam bleibt | Eine Hausautomation oder ein Bot fragt Repeater zu oft nach ihrem Status | `filter on`. Der Paketfilter lässt dann 5 Anfragen pro Minute durch. Sag dem Besitzer Bescheid. |
| Dieselbe Art Nachricht in einem Kanal, jede Minute | Ein Bot postet zu oft | [Sperr den Kanal](/guides/filter/#channel) oder [brems den Absender aus](/guides/filter/#sender). Sag dem Besitzer Bescheid. |
| Unlesbare Nachrichten in Public und anderen Kanälen | Ein Knoten mit defekter Firmware oder falschen Funkeinstellungen | `filter malformed on` verwirft sie in Public. Sag dem Besitzer Bescheid. |
| Der Advert eines Knotens alle paar Minuten | Ein Knoten sendet zu oft Adverts | `filter advert 24` lässt den Advert jedes Knotens einmal am Tag durch. `set flood.max.advert 3` begrenzt Adverts auf 3 Hops. |
| Nachrichten von weit weg, mit Regionen, die nicht hierher gehören | Eine Brücke verbindet Meshes über das Internet | `set flood.max.unscoped 1`. Trag für deinen Repeater außerdem nur die [Regionen, die er versorgt](/guides/settings/#traffic), ein. |
| Dieselbe Nachricht kommt immer wieder durch, mit der ID deines Repeaters mehr als einmal im Pfad | Ein Repeater verändert Pakete und gibt sie weiter, sodass sie kreisen | Die Schleifenerkennung läuft standardmäßig auf `minimal`. Mit `set loop.detect moderate` verwirft dein Repeater eine Schleife früher. |

## Floods mit Absicht {#purpose}

Manche Floods sind Spam: Müll, den jemand absichtlich sendet, um das Mesh zu
verstopfen. Der Absender wechselt Namen, Schlüssel und Pfade. Deshalb stoppt
keine einzelne Regel den Flood.

| Was du siehst | Was es ist | Was hilft |
| --- | --- | --- |
| Viele neue Knoten mit zufälligen Namen, jeder mit einem neuen Schlüssel | Gefälschte Adverts | `filter rate 04 5 60` lässt 5 Adverts pro Minute durch. `filter advert` hilft nicht: Jeder Advert kommt von einem [neuen Schlüssel](#forged). |
| Nachrichten mit unlesbarem Text von erfundenen Absendern, oft mehr als ein Jahr zurückdatiert | Kanal-Spam | `filter malformed on` verwirft sie in Public. `filter age 60` verwirft die alt datierten in Public und in [überwachten Kanälen](/guides/filter/#settings). |
| Bis zu 200 Direktnachrichten pro Minute an Knoten, die es nicht gibt, und keine Bestätigungen zurück | Ein Flood aus Direktnachrichten | `filter rate 02 5 60`. Deine App zeigt diese Nachrichten nicht an, ein Observer schon. |
| Schübe von Anfragen von einem Knoten an Dutzende andere | Anfrage-Spam | Mit `filter on` lässt der Paketfilter 5 Anfragen pro Minute durch. |
| Eine Nachricht kommt 10 bis 20 Minuten später zurück, mit fast demselben Pfad | Replay: eine erneut gesendete Kopie | Ein Repeater merkt sich die letzten 160 Pakete, die er gesehen hat. In einem ausgelasteten Mesh kommt eine spätere Kopie deshalb wieder durch. `filter age` verwirft eine Gruppennachricht, die älter ist, als du erlaubst. |
| Nachrichten aus Public, erneut gesendet unter einem erfundenen Absender, manchmal mit altem Datum | Echo-Spam | `filter age 60`. `filter malformed on` verwirft auch ein Datum, das mehr als eine Woche abweicht. |
| Alle paar Sekunden eine Nachricht in mehreren Kanälen, jede von einem neuen Namen, mit Alltagsfragen | Eine Bot-Welle | `filter rate 05 10 60`. [Sperr außerdem die Kanäle](/guides/filter/#channel), die in deiner Gegend niemand nutzt. Jeder Name ist neu, daher greifen die [Absender-Regeln](#forged) nicht. |

## Was funktioniert hat {#worked}

Lokale Gruppen haben Floods mit diesen Schritten gestoppt:

1. **Sag dem Besitzer Bescheid.** Ein Flood aus Versehen hört auf, sobald
   der Besitzer davon weiß. Schreib ihm eine freundliche Nachricht.
2. **Reagier nicht im Mesh.** Eine Antwort zeigt dem Spammer, dass der Spam
   wirkt.
3. **Bitte um Observer.** Ein Observer ist ein Knoten, der jedes Paket, das
   er hört, über MQTT meldet. Je mehr Observer um dich herum, desto früher
   siehst du, wo ein Flood hereinkommt. Mit
   [MQTT auf deinem Observer](/guides/mqtt/) machst du deinen eigenen
   Repeater zu einem.
4. **Finde die Quelle.** Observer grenzen den Absender auf ein Gebiet ein.
   Für den letzten Kilometer müssen Leute mit einem Funkgerät zu Fuß los.
   Siehe [Die Quelle finden](#source).
5. **Bring deine lokale Gruppe in Bewegung.** Ein Repeater mit den richtigen
   Einstellungen hilft. Alle Repeater der Gegend zusammen stoppen einen
   Flood. Deine [lokale Gruppe](/community/) bringt jeden Besitzer dazu, die
   Einstellung einzuschalten.

## Erfundene Absender und Pfade {#forged}

Diese Teile eines Pakets schreibt der Absender, und niemand prüft sie:

- **Der Name des Absenders.** In einer Kanalnachricht ist der Name Teil des
  Textes. Wer den Kanalschlüssel hat, kann jeden Namen hineinschreiben.
- **Der Anfang des Pfads.** Jeder Repeater hängt seine eigene ID ans Ende
  des Pfads an. Die IDs, die schon davor standen, prüft niemand. Ein
  Absender kann den Pfad also mit erfundenen IDs beginnen. Das Ende des
  Pfads ist echt.

{{< forged-path >}}

Deshalb stoppen `filter sender` und `filter path` einen Absender nur, bis er
seinen Namen oder Pfad ändert. Eine [Pfadsperre](/guides/filter/#path)
verwirft außerdem den echten Verkehr des Repeaters, dessen ID darin steht.
Raten- und Hop-Limits, die Alters- und Formatprüfungen, Kanalsperren,
Regionen und der Duty Cycle wirken weiter.

## Einstellungen für jeden Flood {#always}

Diese greifen, egal womit jemand das Mesh flutet:

- **Duty Cycle auf 10%.** Dein Repeater sendet dann nie mehr, als das Gesetz
  erlaubt, egal was hereinkommt. Mehr dazu im
  [Repeater-Leitfaden](/repeater-guide/#duty-cycle).
- **Regionen und Hop-Limits.** Eine Region ist das Gebiet, in dem eine
  Nachricht bleibt. Ein Repeater gibt nur Nachrichten aus seinen Regionen
  weiter, und `flood.max.*` hält den Verkehr in der Nähe. Beides steht in
  [Verkehr gering halten](/guides/settings/#traffic).
- **Der Paketfilter für einen stark ausgelasteten Repeater.** Die
  [fertigen Einstellungen](/guides/filter/#busy) halbieren Gruppennachrichten
  und Adverts. Probier sie zuerst im [Dry-Run](/guides/filter/#dryrun) aus:
  Dort zählt der Filter nur, was er verwerfen würde.
- **Der Companion-Filter, in der DMC-Firmware.** Dein Companion ist der
  Knoten, von dem aus du Nachrichten schreibst. Er hält Müll aus deiner App
  fern. Er blendet defekte und alte Nachrichten aus, außerdem Nachrichten
  von einem Repeater, einem Absender oder mit einem Wort, das du sperrst.
  Eine Absender- oder Wortregel blendet die Nachricht nur für dich aus.
  Andere empfangen sie weiterhin.

### Duty-Cycle-Gating {#gate}

In der DMC-Firmware kann dein Repeater seiner eigenen Region Vorrang geben,
wenn viel los ist. Hat er in der letzten Minute mehr als 35% der Zeit
gesendet, gibt er keine Nachrichten ohne Region mehr weiter. Bleibt viel los,
verwirft er als Nächstes die weiteste Region, eine Ebene nach der anderen.
Seine eigene Region kommt immer durch. Das funktioniert nur, wenn du auf
deinem Repeater Regionen eingestellt hast. Schalte es ein und prüf es:

```text
set dc.gate on
get dc.gate.status
```

{{< dc-gate >}}

Was dabei verworfen wird, erscheint nicht in `filter stats`. Wird es auf dem
Repeater wieder ruhig, kommen die Regionen zurück, die innerste zuerst.

## Einen Flood sehen {#see}

Deine App zeigt nur, was bei dir ankommt. Einen Flood aus Direktnachrichten
an Knoten, die es nicht gibt, hört nur ein Observer. Jeder Observer meldet
an den [MeshCore Analyzer](https://meshcore-analyzer.eu/), wo alle es sehen
können. Mit [MQTT auf deinem Observer](/guides/mqtt/) machst du deinen
Repeater zu einem.

Sieh dir im Analyzer jede Kopie eines Pakets an. Meist zeigt ihr Pfad, woher
sie kam. Ein Flooder kann den Pfad mit [erfundenen IDs](#forged) beginnen.
Die ersten IDs sagen dir dann nichts. Jede Kopie trägt aber denselben
erfundenen Anfang. Die Kopie mit dem kürzesten Pfad ging durch die wenigsten
echten Repeater. Sie wurde also am nächsten am Absender gehört.

{{< copies >}}

Auf deinem eigenen Repeater zeigt `filter stats`, was der Paketfilter
verworfen hat. `filter stats top` zeigt das erste Byte der Knoten-IDs, von
denen die meisten verworfenen Pakete stammen. Viele Knoten teilen sich
dieses Byte. Es grenzt die Suche also ein, nennt aber nicht den Absender.

## Die Quelle finden {#source}

Wenn ein Flood immer wiederkommt:

1. **Folge den Pfaden.** Lies einen Pfad vom Ende her: Die letzten IDs sind
   die Repeater, durch die der Flood ging. Der früheste echte liegt nahe an
   der Quelle. Die IDs davor können [erfunden](#forged) sein.
2. **Grenz das Gebiet ein.** Hören mehrere Observer dasselbe Paket, grenzen
   sie den Absender auf ein Gebiet ein. Der
   [DMC Triangulator](https://triangulator.dutchmeshcore.nl/) berechnet es
   aus den Repeatern, die das Paket gehört haben.
3. **Geh den letzten Kilometer zu Fuß.** Die Repeater hören die Quelle nur
   am Rand ihrer Reichweite. Für das letzte Stück müssen deshalb Leute zu
   Fuß los. [Mesh-Hunter](https://mesh-hunter.eu/) koppelt sich mit deinem
   Companion und speichert jedes Paket, das er hört, mit deiner
   GPS-Position. Gehen mehrere Leute gleichzeitig los, finden sie die
   Quelle schneller.
4. **Sag deiner [lokalen Gruppe](/community/) Bescheid.** Sie sieht mehr vom
   Mesh, entscheidet über die nächsten Schritte und nimmt Kontakt zu dem
   auf, der absichtlich flutet.

## Ergänze, was du gesehen hast {#add}

Hat dich ein Flood getroffen, der nicht in diesen Tabellen steht? Hat eine
Einstellung einen gestoppt? Erzähl es uns auf
[Discord](https://discord.meshcore-info.eu/): was du gesehen und was du
eingeschaltet hast. Wir nehmen es in die Seite auf.
