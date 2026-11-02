---
title: Karte pokrivenosti
layout: map
lead: Pogledaj dokle mreža seže, gdje su čvorovi i kako poruke putuju. Ove karte vode zajednice diljem Europe.
description: MeshCore karte uživo, karte pokrivenosti i analizatori paketa za Europu i pojedine države.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '351071aa'
  seeded: '2026-11-02'
  fields: {title: '4b9f20a0', lead: 'fedb89bb', description: 'b5719f82'}
  sections: ['351071aa']
  blocks: ['dd5f039e', '9d4a2ad8', '70c417f2', '9fef7e16']
---

Čvor se pojavljuje na ovim kartama kada ga vlasnik objavi ili kada ga čuje
*observer*: čvor koji ono što čuje prosljeđuje preko MQTT-a. Zato nijedna karta
nije potpuna. Analizatori prikazuju promet koji primaju njihovi observeri: pakete,
rute i aktivnost na kanalima. Izravne poruke ostaju šifrirane, pa nijedan analizator
ne prikazuje njihov sadržaj.

Čvor stoji na karti ondje gdje ga je vlasnik postavio, a to mjesto može biti pogrešno ili
zastarjelo. Flood poruka putuje kroz više putova odjednom. Ruta na karti put je
kopije koja je stigla prva, a ostali se putovi ne bilježe.

Ovim kartama treba internet, a mreži ne treba. [Zašto](/network/)

Imaš repeater, čvor koji prosljeđuje poruke? Postavi njegov položaj naredbama `set lat` i `set lon`, i karte će ga
moći smjestiti. U [vodiču za repeater](/repeater-guide/#config) piše kako.
