---
title: Ieteicamie iestatījumi
layout: settings
lead: Radio priekšiestatījums, ko lieto tavā apgabalā, un iestatījumi, ko nomainījuši tavi kaimiņi. Izvēlies valsti, iestati priekšiestatījumu un nokopē komandas.
description: MeshCore radio priekšiestatījums katram Eiropas apgabalam, kā arī retranslatora un kompanjona iestatījumi, ko vietējās grupas nomainījušas, ar komandām.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '0876215b'
  seeded: '2026-11-02'
  fields: {title: 'cfb32983', lead: 'f3f16725', description: 'cb15acd3'}
  sections: ['39848942', 'd1606fcd']
  blocks: ['8c9e88ea', '50ac6063', '85c2203d', '15f91217', 'bdf5fa4e', '69d8e70b', '28f83120', 'fe27027b']
---

Katrs tālāk minētais apgabals lieto savu radio priekšiestatījumu vai nomaina dažas
MeshCore noklusējuma vērtības. Viss, kas nav minēts, paliek noklusējuma vērtībās, tāpēc
tu maini tikai to, ko nomainījis tavs apgabals. Retranslators pārsūta ziņas visiem.
Kompanjons ir mezgls, no kura tu raksti ziņas. Tu to savieno ar telefonu vai
klēpjdatoru pa Bluetooth vai USB, vai arī lieto tā paša ekrānu.

[Retranslatora ceļvedī](/repeater-guide/#config) vari uzzināt, kā piekļūt sava
retranslatora komandrindai. Komandas pats vari ierakstīt šīs vietnes
[seriālajā konsolē](/firmware/console/). Pie katra apgabala vari arī nosūtīt tā
iestatījumus pa USB. Retranslatora ceļvedī atradīsi arī
[juridiskos ierobežojumus](/repeater-guide/#legal) 868 MHz joslā.

## Samazini datplūsmu {#traffic}

Šie iestatījumi attiecas uz katru apgabalu. Katrs retranslators pārsūta katru flood
ziņu, ko uztver. Viena tava ziņa nozīmē vienu pārraidi un vēl vienu par katru
retranslatoru, kas to uztver. Ar 10% darba ciklu retranslators stundā var nosūtīt
apmēram 680 paketes, un šo skaitu dala visi tā apkārtnē. Ziņa, kas aizceļo tālāk,
nekā vajag, iztērē daļu no tā.

**Sūti uz mazāko reģionu, kas sasniedz cilvēkus, kuriem raksti.**
Reģioni ietilpst cits citā: valsts, province, vietējā grupa. Katram ir savs kods,
piemēram, `nl`, `nl-ov` un `nl-ov-zwo`. Ziņa, kas adresēta `nl-ov-zwo`, paliek pie
šīs grupas retranslatoriem. Retranslators pārsūta tikai to reģionu ziņas, kas tam pašam
ir iestatīti: ja tam ir `nl`, tas vēl nenozīmē, ka tas pārsūta `nl-ov`. Iekļauj katru
retranslatoru visos reģionos, ko tas apkalpo, un tikai tajos. Tava
[vietējā grupa](/community/) zina, kuri tie ir.

**Ierobežo to, ko tavs retranslators pārsūta.** Ar diviem iestatījumiem datplūsma, kurai
nav jāceļo tālu, paliek tuvu mājām:

```text
set flood.max.advert 3
set flood.max.unscoped 1
```

- `flood.max.advert 3`: paziņojumi (adverts), ar kuriem mezgls piesaka sevi tīklam,
  veic ne vairāk kā 3 lēcienus.
- `flood.max.unscoped 1`: ziņa bez reģiona iziet cauri ne vairāk kā vienam retranslatoram.
