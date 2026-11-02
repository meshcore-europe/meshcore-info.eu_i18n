---
title: Is-settings irrakkomandati
layout: settings
lead: Il-preset tar-radju li tuża ż-żona tiegħek, u s-settings li bidlu l-ġirien tiegħek. Agħżel il-pajjiż tiegħek, issettja l-preset u kkopja l-kmandi.
description: Il-preset tar-radju ta' MeshCore għal kull żona fl-Ewropa, u s-settings tar-repeater u tal-companion li l-gruppi lokali bidlu mid-default, flimkien mal-kmandi.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '0876215b'
  seeded: '2026-11-02'
  fields: {title: 'cfb32983', lead: 'f3f16725', description: 'cb15acd3'}
  sections: ['39848942', 'd1606fcd']
  blocks: ['8c9e88ea', '50ac6063', '85c2203d', '15f91217', 'bdf5fa4e', '69d8e70b', '28f83120', 'fe27027b']
---

Kull żona hawn taħt tuża l-preset tar-radju tagħha, jew tibdel ftit mid-defaults
ta' MeshCore. Dak kollu li mhuwiex imniżżel jibqa' fuq id-default, għalhekk
tibdel biss dak li biddlet iż-żona tiegħek. Repeater jgħaddi l-messaġġi għal
kulħadd; companion huwa n-node li minnu tibgħat il-messaġġi, imqabbad mat-telefon
jew mal-laptop tiegħek bil-Bluetooth jew bl-USB, jew bl-iskrin tiegħu stess.

Fil-[gwida tar-repeater](/repeater-guide/#config) issib kif tasal għall-command
line tar-repeater tiegħek, u fuq il-[console serjali](/firmware/console/) ta' dan
is-sit tikteb il-kmandi int stess. Taħt kull żona tista' wkoll tibgħat is-settings
tagħha bl-USB. Il-gwida telenka wkoll il-[limiti legali](/repeater-guide/#legal)
fuq 868 MHz.

## Żomm it-traffiku baxx {#traffic}

Dawn is-settings japplikaw għal kull żona. Kull repeater jgħaddi kull messaġġ
flood li jisma'. Messaġġ wieħed mingħandek jiswa trażmissjoni waħda, u oħra għal
kull repeater li jismgħu. Taħt id-duty cycle ta' 10%, repeater jista' jibgħat
madwar 680 pakkett fis-siegħa, u kulħadd madwaru jaqsam dak in-numru. Messaġġ li
jasal aktar 'il bogħod milli għandu bżonn juża parti minnu.

**Ibgħat lill-iżgħar reġjun li jilħaq lin-nies li tikteb lilhom.**
Ir-reġjuni jidħlu wieħed ġewwa l-ieħor: pajjiż, provinċja, grupp lokali, kull
wieħed bil-kodiċi tiegħu, bħal `nl`, `nl-ov` u `nl-ov-zwo`. Messaġġ għal
`nl-ov-zwo` jibqa' mar-repeaters ta' dak il-grupp. Repeater jgħaddi biss
ir-reġjuni li għandu hu stess: jekk għandu `nl`, xorta ma jgħaddix `nl-ov`. Poġġi
kull repeater f'kull reġjun li jservi, u f'dawk biss; il-[grupp lokali
tiegħek](/community/) jaf liema huma.

**Illimita dak li jgħaddi r-repeater tiegħek.** Żewġ settings iżommu qrib id-dar
it-traffiku li m'għandux għalfejn jasal 'il bogħod:

```text
set flood.max.advert 3
set flood.max.unscoped 1
```

- `flood.max.advert 3`: l-adverts, li jħabbru node lill-mesh, jagħmlu l-aktar
  3 hops.
- `flood.max.unscoped 1`: messaġġ mingħajr reġjun jgħaddi minn repeater wieħed
  l-aktar.
