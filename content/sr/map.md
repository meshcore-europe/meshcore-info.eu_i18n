---
title: Mape pokrivenosti
layout: map
lead: Pogledaj dokle mreža dopire, gde se nalaze čvorovi i kojim putem putuju poruke. Ove mape vode zajednice širom Evrope.
description: MeshCore mape uživo, mape pokrivenosti i analizatori paketa za Evropu i pojedine zemlje.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '24bfdf6b'
  seeded: '2026-11-04'
  fields: {title: '4b9f20a0', lead: 'fedb89bb', description: 'b5719f82'}
  sections: ['24bfdf6b']
  blocks: ['dd5f039e', '9d4a2ad8', '763fc710', '70c417f2', '9fef7e16']
---

Čvor se pojavljuje na ovim mapama kada ga vlasnik objavi ili kada ga čuje
*observer*: čvor koji ono što čuje prosleđuje preko MQTT-a. Zato nijedna mapa
nije potpuna. Analizatori prikazuju saobraćaj koji primaju njihovi observeri:
pakete, rute i aktivnost na kanalima. Direktne poruke ostaju šifrovane, pa
nijedan analizator ne prikazuje njihov sadržaj.

Čvor stoji na mapi tamo gde ga je vlasnik postavio, a ta pozicija može biti
pogrešna ili zastarela. Flood poruka putuje kroz više putanja istovremeno. Ruta na
mapi je putanja kopije koja je stigla prva. Ostale putanje niko ne beleži.

Deluje li ti neka ruta na mapi malo verovatno? Proveri 2 njena čvora alatom Line of Sight
u MeshCore aplikaciji. [Vodič za repetitore](/repeater-guide/#check-site) pokazuje kako.

Ovim mapama treba internet, a mreži ne treba. [Zašto](/network/)

Imaš repeater, čvor koji prenosi poruke dalje? Podesi njegovu poziciju komandama
`set lat` i `set lon`, pa mape mogu da ga ucrtaju. U
[vodiču za repeater](/repeater-guide/#config) piše kako se to radi.
