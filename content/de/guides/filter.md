---
title: Paketfilter
lead: 'Verhindere, dass dein Repeater Müll weiterleitet: Floods von weit her, ein Bot, der nie aufhört, einen lauten Kanal. Teste eine Einstellung zuerst und schalte sie dann ein.'
description: 'Der Paketfilter der DMC-Repeater-Firmware: was er verwirft, fertige Einstellungen für einen normalen und einen stark belasteten Repeater, jeder Filterbefehl mit seinem Standardwert, und wie du siehst, was er verworfen hat.'
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '2bf23d24'
  seeded: '2026-10-26'
  fields: {title: '20a3ef1f', lead: 'd948682d', description: 'a8c57a9f'}
  sections: ['0625daa2', 'b1d9a8d1', '2dd3448d', 'ee64176e', 'a3cb880e', '09b568f0', 'a1a4fb68', '95fe64ae', 'dbac19c3', 'ffc3f3a0', '3fa1bb28', '09511608']
---

Ein Repeater (ein Knoten, der Nachrichten weiterleitet) wiederholt alles, was er hört.
In einem belebten Mesh gehört auch Müll dazu. Ein Bot postet jede Minute. Ein Knoten
sendet sein Advert, das Hallo, mit dem andere ihn finden, alle paar Minuten erneut.
Nachrichten kommen an, die durch das halbe Land gereist sind. Jede Wiederholung kostet
alle um dich herum Sendezeit. Mit dem Paketfilter verwirft dein Repeater diesen
Verkehr, statt ihn weiterzuleiten.

{{< callout type="warning" >}}
Der Paketfilter gehört zur **DMC-Repeater-Firmware**, dem Repeater-Build von
[Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore). Das normale
MeshCore hat keinen Paketfilter; es hat `region denyf *` und
`set flood.max.unscoped`, beschrieben auf der Seite [CLI-Befehle](/guides/cli/). Diese
Anleitung folgt dem 1.18.0-Dev-Build `ecfb2d4` vom 19. Oktober 2026. Der stabile
Build 1.17.1 hat nur die Filter für Hops, Rate, Kanal, Hash und defekte Pakete. Er
hat auch keinen Testlauf.
{{< /callout >}}

## Was der Filter macht {#what}

Der Filter prüft nur Pakete, die dein Repeater per Flood weiterleitet (also an
jeden Knoten in Reichweite sendet). Was dein Repeater selbst sendet, lässt er in Ruhe,
ebenso Pakete, die einer bekannten Route zu einem Knoten folgen. Direktnachrichten und
Anfragen an und von deinen eigenen Kontakten kommen auch durch. Verwerfen kann er:

- Pakete, die schon so viele Repeater (Hops) passiert haben, wie du erlaubst, pro
  Pakettyp;
- mehr Pakete eines Typs, als du pro Minute erlaubst;
- ein Advert von einem Knoten, der in den letzten Stunden schon eines gesendet hat;
- Nachrichten auf einem Kanal, den du sperrst;
- alles, was über einen Repeater kam, den du sperrst;
- Gruppennachrichten von einem Absender oder mit einem Wort, oder nur einen Teil davon;
- Gruppennachrichten, die defekt oder älter sind, als du erlaubst.

Der Filter ist **aus**, bis du ihn einschaltest. Du stellst ihn mit Befehlen ein. Tippe
sie über USB in die [serielle Konsole](/firmware/console/) auf dieser Seite. Oder
schicke sie aus der MeshCore-App, wie in der
[Repeater-Anleitung](/repeater-guide/#config) beschrieben.

## Die Firmware holen {#firmware}

Flashe **DutchMeshCore Repeater** mit dem Flasher in der
[DutchMeshCore Toolbox](https://toolbox.dutchmeshcore.nl/). Die Observer-Firmware
aus [MQTT auf deinem Observer](/guides/mqtt/) hat denselben Filter.

## Zuerst testen {#dryrun}

Im Testlauf zählt der Filter jedes Paket, das er verwerfen würde, leitet es aber
trotzdem weiter. So bemisst du eine Einstellung, bevor sie etwas verwirft:

```text
filter on
filter dryrun on
```

Solange der Testlauf läuft, endet die Statuszeile von `filter` mit `(dry-run)`. Die
Zähler zeigen, was er verworfen hätte. Lass ihn einen Tag laufen und sieh sie dir dann
an (siehe [Was er verworfen hat](#stats)). Wenn die Zahlen passen, schaltest du scharf:

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

Gruppennachrichten kommen bis zu 20 pro Minute durch, Direktnachrichten bis zu 5 pro
Minute, und defekte Gruppennachrichten werden verworfen. Die normale Konfiguration der
Firmware selbst erlaubt 20 Direktnachrichten pro Minute. Diese Seite nimmt die 5, die
sie seit einem Flood von Direktnachrichten im Juli 2026 empfiehlt.

### Ein stark belasteter Repeater {#busy}

Für einen Repeater auf einem hohen Standort, der eine ganze Region hört, oder einen,
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

Das halbiert die Gruppennachrichten und die Adverts und lässt das Advert jedes Knotens
einmal am Tag durch. Nachrichten, die schon 16 Repeater passiert haben, verwirft es.
Nach einem Neustart kommt von jedem Knoten ein Advert durch. Die Dokumentation der
Firmware setzt hier zusätzlich `filter hash 2`; diese Seite lässt das weg (warum, steht
unter [Jede Einstellung](#settings)).

### Einen lauten Kanal sperren {#channel}

```text
filter channel add #bot
```

Dein Repeater hört den Kanal weiterhin. Er leitet ihn aber nicht mehr an andere
Repeater und Companions (die Knoten, von denen Leute Nachrichten schreiben) weiter. Bis
zu 16 Kanäle.

### Einen Absender ausbremsen {#sender}

Ein Bot, der zu oft auf einem Kanal postet, den du behalten willst:

```text
filter watch add #test
filter sender add Bob 60
```

Bobs Nachrichten auf dem Kanal Public und auf `#test` kommen jetzt einmal pro Minute
durch; der Rest wird verworfen. Der Filter vergleicht den Namen in der Nachricht, ein
Absender, der sich umbenennt, kommt also an ihm vorbei.

### Einen Repeater vor dir sperren {#path}

Wenn der Müll über einen bestimmten Repeater hereinkommt, sperrst du sein Präfix: den
ersten Teil seiner ID, hexadezimal (hex).

```text
filter path add a1b2
```

Ein kurzes Präfix wie `a1` sperrt auch jeden anderen Repeater, dessen ID mit `a1`
beginnt. Nimm das längste Präfix, das du kennst. Bis zu 8 Präfixe.

## Jede Einstellung {#settings}

Pakettypen haben Nummern. Auf dem Repeater zeigt `filter types` dieselben Nummern mit
den Namen der Firmware, etwa `TXT_MSG` und `GRP_TXT`:

| Nummer | Typ | Nummer | Typ |
| --- | --- | --- | --- |
| `00` | Anfrage | `06` | Gruppendaten |
| `01` | Antwort | `07` | anonyme Anfrage |
| `02` | Direktnachricht | `08` | Pfad |
| `03` | Bestätigung | `09` | Trace |
| `04` | Advert | `10` | mehrteilig |
| `05` | Gruppennachricht | `11` | Steuerung |

| Befehl | Was er macht | Standardwert |
| --- | --- | --- |
| `filter on` / `filter off` | Schaltet den Filter ein oder aus. | aus |
| `filter dryrun on` / `off` | Zählt Verwürfe, leitet aber alles weiter. | aus |
| `filter hops <type> <max>` | Verwirft einen Typ, der schon so viele Repeater passiert hat, 0 bis 64. | 32 für Gruppennachrichten, 8 für den Rest |
| `filter rate <type> <limit> <secs> [soft]` | Lässt höchstens `limit` eines Typs pro `secs` durch. Mit `soft` nimmt die Durchlassrate von `soft` bis `limit` ab. `0` schaltet das Limit aus. | 20 pro 60 s für Direkt- und Gruppennachrichten, 10 für Adverts, 5 für den Rest |
| `filter advert <hours>` | Lässt das Advert jedes Knotens einmal pro so viele Stunden durch, bis 720. | 0 (aus) |
| `filter channel add <#name>` | Leitet einen Kanal nicht mehr weiter. | keine |
| `filter path add <hex>` | Verwirft alles, was über einen Repeater mit diesem Präfix kam, 2 bis 8 Hex-Ziffern. | keine |
| `filter sender add <name> [secs] [prob]` | Verwirft Gruppennachrichten eines Absenders auf Public und beobachteten Kanälen. `Bot*` trifft jeden Namen, der mit Bot beginnt. | keine |
| `filter text add <word> [secs] [prob]` | Verwirft Gruppennachrichten mit einem Wort auf Public und beobachteten Kanälen. `^word` trifft nur am Anfang. | keine |
| `filter watch add <#name>` | Lässt die Absender- und Textregeln auch diesen Kanal lesen, bis zu 4. Public wird immer gelesen. | Public |
| `filter malformed on` / `off` | Verwirft Public-Nachrichten, die leer, defekt oder mehr als eine Woche falsch datiert sind (die Datumsprüfung wartet, bis die Uhr gestellt ist). | aus |
| `filter age <minutes>` / `off` | Verwirft Gruppennachrichten, die älter sind, auf Public und beobachteten Kanälen, 1 bis 10080. | aus |
| `filter hash <bytes>` | Verwirft Pakete mit einer kürzeren Pfad-ID als dieser, 1 bis 3. | 1 |
| `filter reset` | Setzt jede Einstellung auf ihren Standardwert zurück. | |

Zu jedem `add` gibt es ein `remove` und ein `list`, etwa `filter channel remove #bot`.
In Absender- und Textregeln lässt `secs` eine Nachricht pro so viele Sekunden durch.
`prob` wendet die Regel nur auf diesen Anteil der Treffer an, 1 bis 100. Bis zu 8
Absender- und 8 Textregeln. Namen und Wörter unterscheiden Groß- und Kleinschreibung;
ein Name hat bis zu 15 Zeichen, ein Wort bis zu 23.

Zwei Einstellungen verwerfen mehr, als du vielleicht erwartest:

- `filter hash 2` verwirft fast den gesamten Verkehr. Knoten senden standardmäßig
  Pfad-IDs von 1 Byte.
- `filter age` vertraut der Uhr deines Repeaters. Stelle sie mit `clock sync` aus der
  App, prüfe sie mit `clock` und fange großzügig an: `filter age 60`.

Jede Einstellung bleibt nach einem Neustart erhalten.

## Was er verworfen hat {#stats}

`filter` zeigt die Summen pro Grund:

```text
> Filter on: Blocked [ Hops: 3 | Rate: 12 | Channel: 1 | Hash: 0 | Malformed: 2 ]
```

`filter stats <topic>` zeigt die Details zu einer Einstellung. Die Themen sind
`hops`, `rate`, `channel`, `hash`, `malformed`, `advert`, `path`, `sender`,
`text` und `age`. `filter stats top` zeigt das erste Byte der Knoten-IDs
hinter den meisten Verwürfen, ein Hinweis, kein Beweis.
`filter stats air` zeigt die Sendezeit, die dein Repeater gespart hat, weil er diese
Pakete nicht weitergeleitet hat.

Die Zähler fangen nach einem Neustart und nach `clear stats` wieder bei 0 an.
