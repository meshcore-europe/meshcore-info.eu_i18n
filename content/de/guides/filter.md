---
title: Paketfilter
lead: 'Dein Repeater muss keinen Müll weitergeben: Floods von weit her, einen Bot ohne Pause, einen lauten Kanal. Probier eine Einstellung zuerst aus, dann schalte sie scharf.'
description: 'Der Paketfilter der DMC-Repeater-Firmware: was er verwirft, fertige Einstellungen für einen normalen und einen stark belasteten Repeater, jeder Filterbefehl mit seinem Standardwert und wie du siehst, was er verworfen hat.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'b07d39a8'
  seeded: '2026-10-31'
  fields: {title: '20a3ef1f', lead: 'd948682d', description: 'a8c57a9f'}
  sections: ['d06c9ddd', 'b1d9a8d1', '2dd3448d', 'ee64176e', 'a3cb880e', '09b568f0', 'a1a4fb68', '95fe64ae', 'dbac19c3', '05123b18', '3fa1bb28', 'e98b2285']
  blocks: ['b6231504', 'c66e4d9a', 'c0502fb4', 'fa699506', 'f7008037', '3acbb97b', '5e55d14c', 'bd024580', '68c8a4b1', '119fc5b9', '61804e40', '2fa7ebe8', '0610128b', 'a3cb880e', '0e6268be', 'e6d77222', 'f50be141', '2a1ae00c', '095e165f', 'd96efc68', 'b8a89bea', 'a29d0e87', 'c69ba7d1', 'f553d783', '1a83fda3', 'b6f87585', '64e2bbfa', 'dc79ca3a', '6ed9acff', 'd3701ccc', 'd4a25061', '22092611', '9184f977', 'f70c9e55', 'b2f0d9cb', 'c7b214c1', 'e8da9f3e', '0742c6c4', '7f2f59ae', '2789fc6d', 'ae920329', '7dd6f173', 'e1ca9ac7', 'ac11c47b', 'ec7913ae']
---

Ein Repeater (ein Knoten, der Nachrichten weitergibt) wiederholt alles, was er hört.
In einem belebten Mesh gehört dazu auch Müll. Ein Bot postet jede Minute. Ein Knoten
sendet alle paar Minuten erneut sein Advert, also das Hallo, über das andere ihn finden.
Es kommen Nachrichten an, die durch das halbe Land gereist sind. Jede Wiederholung
kostet alle in deiner Umgebung Sendezeit. Mit dem Paketfilter verwirft dein Repeater
diesen Verkehr, statt ihn weiterzugeben. Was dein Mesh zuerst flutet und was
außer dem Filter hilft, findest du unter
[Das Mesh widerstandsfähig machen](/guides/resilient/).

{{< callout type="warning" >}}
Der Paketfilter gehört zur **DMC-Repeater-Firmware**, dem Repeater-Build von
[Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore). Das normale
MeshCore hat keinen Paketfilter. Es hat `region denyf *` und
`set flood.max.unscoped`, beschrieben auf der Seite [CLI-Befehle](/guides/cli/).
Diese Anleitung folgt dem 1.18.0-Dev-Build `ecfb2d4` vom 19. Oktober 2026. Der
stabile Build 1.17.1 hat nur die Filter für Hops, Rate, Kanal, Hash und defekte
Pakete. Einen Dry-Run hat er auch nicht.
{{< /callout >}}

## Was der Filter macht {#what}

Der Filter prüft nur Pakete, die dein Repeater per Flood weitergibt (also an jeden
Knoten in Reichweite sendet). Was dein Repeater selbst sendet, lässt er in Ruhe,
ebenso Pakete, die einem bekannten Pfad zu einem Knoten folgen. Auch
Direktnachrichten und Anfragen von und an deine eigenen Kontakte kommen durch.
Er kann Folgendes verwerfen:

- Pakete, die schon so viele Repeater (Hops) durchlaufen haben, wie du erlaubst,
  je Pakettyp;
- mehr Pakete eines Typs pro Minute, als du erlaubst;
- ein Advert von einem Knoten, der sich in den letzten Stunden schon gemeldet hat;
- Nachrichten auf einem Kanal, den du sperrst;
- alles, was über einen Repeater kam, den du sperrst;
- Gruppennachrichten von einem Absender oder mit einem bestimmten Wort, auf Wunsch nur einen Teil davon;
- Gruppennachrichten, die defekt sind oder älter, als du erlaubst.

Der Filter ist **aus**, bis du ihn einschaltest. Du stellst ihn mit Befehlen ein.
Die tippst du über USB in die [serielle Konsole](/firmware/console/) auf dieser Seite.
Oder du schickst sie aus der MeshCore-App, wie in der
[Repeater-Anleitung](/repeater-guide/#config) beschrieben.

## Firmware besorgen {#firmware}

Flashe **DutchMeshCore Repeater** mit dem Flasher in der
[DutchMeshCore Toolbox](https://toolbox.dutchmeshcore.nl/). Die Observer-Firmware
aus [MQTT auf deinem Observer](/guides/mqtt/) hat denselben Filter.

## Zuerst ausprobieren {#dryrun}

Im Dry-Run zählt der Filter jedes Paket, das er verwerfen würde, gibt es aber
trotzdem weiter. So stimmst du eine Einstellung ab, bevor sie etwas verwirft:

```text
filter on
filter dryrun on
```

Solange der Dry-Run läuft, endet die Statuszeile von `filter` mit `(dry-run)`. Die
Zähler zeigen, was er verworfen hätte. Lass ihn einen Tag laufen und sieh dir dann
die Zahlen an (siehe [Was er verworfen hat](#stats)). Wenn sie stimmen, schaltest
du den Filter scharf:

```text
filter dryrun off
```

## Empfohlene Konfigurationen {#configs}

### Ein normaler Repeater {#typical}

```text
filter on
filter malformed on
filter rate 05 20 60
filter rate 02 5 60
filter hops 05 32
```

Gruppennachrichten kommen mit bis zu 20 pro Minute durch, Direktnachrichten mit bis
zu 5 pro Minute. Defekte Gruppennachrichten verwirft der Filter. Die eigene
Normalkonfiguration der Firmware erlaubt 20 Direktnachrichten pro Minute. Diese
Seite übernimmt die 5, die die Firmware seit einer Flut von Direktnachrichten im
Juli 2026 empfiehlt.

### Ein stark belasteter Repeater {#busy}

Für einen Repeater an einem hohen Standort, der eine ganze Region hört, oder einen,
der geflutet wird:

```text
filter on
filter malformed on
filter rate 05 10 60
filter rate 02 5 60
filter rate 04 5 60
filter advert 24
filter hops 05 16
filter hops 02 16
filter hops 04 8
```

Das halbiert die Gruppennachrichten und die Adverts und lässt das Advert jedes
Knotens einmal am Tag durch. Nachrichten, die schon 16 Repeater durchlaufen haben,
verwirft der Filter. Nach einem Neustart kommt von jedem Knoten ein Advert durch. Die
Dokumentation der Firmware setzt hier auch `filter hash 2`. Diese Seite lässt das
weg (warum, steht unter [Alle Einstellungen](#settings)).

### Einen lauten Kanal sperren {#channel}

```text
filter channel add #bot
```

Dein Repeater hört den Kanal weiterhin. Er gibt ihn aber nicht mehr an andere
Repeater und Companions weiter (die Knoten, von denen aus Leute Nachrichten
schreiben). Bis zu 16 Kanäle.

### Einen Absender bremsen {#sender}

Ein Bot postet zu oft auf einem Kanal, den du behalten willst:

```text
filter watch add #test
filter sender add Bob 60
```

Bobs Nachrichten im Public-Kanal und in `#test` kommen jetzt einmal pro Minute
durch. Den Rest verwirft der Filter. Er vergleicht den Namen in der Nachricht.
Ein Absender, der sich umbenennt, kommt also an ihm vorbei.

### Einen vorgelagerten Repeater sperren {#path}

Kommt der Müll über einen bestimmten Repeater herein, sperrst du dessen Präfix:
den ersten Teil seiner ID in Hexadezimal (Hex). Dafür brauchst du den 1.18-Dev-Build.
1.17.1 hat keinen Pfadfilter.

```text
filter path add a1b2
filter path list
filter stats path
```

`filter path list` zeigt die Präfixe, die du sperrst, `filter stats path`, wie viel
jedes davon verworfen hat. Mit `filter path remove a1b2` lässt du den Repeater wieder durch.
Ein kurzes Präfix wie `a1` sperrt auch jeden anderen Repeater, dessen ID mit `a1`
beginnt. Nimm ein möglichst langes Präfix. Bis zu 8 Präfixe.

## Alle Einstellungen {#settings}

Pakettypen haben Nummern. Auf dem Repeater zeigt `filter types` dieselben Nummern
mit den Namen aus der Firmware, etwa `TXT_MSG` und `GRP_TXT`:

| Nummer | Typ | Nummer | Typ |
| --- | --- | --- | --- |
| `00` | Anfrage | `06` | Gruppendaten |
| `01` | Antwort | `07` | anonyme Anfrage |
| `02` | Direktnachricht | `08` | Pfad |
| `03` | Bestätigung | `09` | Trace |
| `04` | Advert | `10` | mehrteilig |
| `05` | Gruppennachricht | `11` | Steuerung |

| Befehl | Was er tut | Startwert |
| --- | --- | --- |
| `filter on` / `filter off` | Schaltet den Filter ein oder aus. | aus |
| `filter dryrun on` / `off` | Zählt Verwerfungen, gibt aber alles weiter. | aus |
| `filter hops <type> <max>` | Verwirft einen Typ, der schon so viele Repeater durchlaufen hat, 0 bis 64. | 32 für Gruppennachrichten, 8 für den Rest |
| `filter rate <type> <limit> <secs> [soft]` | Lässt höchstens `limit` Pakete eines Typs pro `secs` durch. Mit `soft` nimmt der Durchlass von `soft` bis `limit` allmählich ab. `0` schaltet das Limit aus. | 20 pro 60 s für Direkt- und Gruppennachrichten, 10 für Adverts, 5 für den Rest |
| `filter advert <hours>` | Lässt das Advert jedes Knotens einmal pro so vielen Stunden durch, bis 720. | 0 (aus) |
| `filter channel add <#name>` | Gibt einen Kanal nicht mehr weiter. | keine |
| `filter path add <hex>` | Verwirft alles, was über einen Repeater mit diesem Präfix kam, 2 bis 8 Hex-Ziffern. | keine |
| `filter sender add <name> [secs] [prob]` | Verwirft Gruppennachrichten eines Absenders auf Public und beobachteten Kanälen. `Bot*` passt auf jeden Namen, der mit Bot beginnt. | keine |
| `filter text add <word> [secs] [prob]` | Verwirft Gruppennachrichten mit einem bestimmten Wort auf Public und beobachteten Kanälen. `^word` passt nur am Anfang. | keine |
| `filter watch add <#name>` | Lässt die Absender- und Textregeln auch diesen Kanal lesen, bis zu 4. Public lesen sie immer. | Public |
| `filter malformed on` / `off` | Verwirft Public-Nachrichten, die leer oder defekt sind oder deren Datum mehr als eine Woche abweicht (die Datumsprüfung wartet, bis die Uhr gestellt ist). | aus |
| `filter age <minutes>` / `off` | Verwirft Gruppennachrichten, die älter als dieser Wert sind, auf Public und beobachteten Kanälen, 1 bis 10080. | aus |
| `filter hash <bytes>` | Verwirft Pakete mit einer kürzeren Pfad-ID als diesem Wert, 1 bis 3. | 1 |
| `filter reset` | Setzt jede Einstellung auf ihren Standardwert zurück. | |

Zu jedem `add` gibt es ein `remove` und ein `list`, etwa `filter channel remove #bot`.
In Absender- und Textregeln lässt `secs` eine Nachricht pro so vielen Sekunden durch.
`prob` wendet die Regel nur auf diesen Anteil der Treffer an, 1 bis 100. Möglich sind
bis zu 8 Absender- und 8 Textregeln. Namen und Wörter unterscheiden Groß- und
Kleinschreibung. Ein Name hat bis zu 15 Zeichen, ein Wort bis zu 23.

Zwei Einstellungen verwerfen mehr, als du vielleicht erwartest:

- `filter hash 2` verwirft fast den gesamten Verkehr. Knoten senden standardmäßig
  Pfad-IDs mit 1 Byte.
- `filter age` verlässt sich auf die Uhr deines Repeaters. Stell sie mit `clock sync`
  aus der App, prüf sie mit `clock` und fang großzügig an: `filter age 60`.

Jede Einstellung bleibt nach einem Neustart erhalten.

## Was er verworfen hat {#stats}

`filter` zeigt die Summen je Grund:

```text
> Filter on: Blocked [ Hops: 3 | Rate: 12 | Channel: 1 | Hash: 0 | Malformed: 2 ]
```

`filter stats <topic>` zeigt die Details zu einer Einstellung. Die Themen sind
`hops`, `rate`, `channel`, `hash`, `malformed`, `advert`, `path`, `sender`,
`text` und `age`. `filter stats top` zeigt das erste Byte der Knoten-IDs hinter den
meisten Verwerfungen. Viele Knoten teilen sich dieses Byte.
`filter stats air` zeigt die Sendezeit, die dein Repeater gespart hat, weil er diese
Pakete nicht weitergegeben hat.

Die Zähler beginnen nach einem Neustart und nach `clear stats` wieder bei 0.
