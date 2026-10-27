---
title: Suositellut asetukset
layout: settings
lead: Alueesi käyttämä radioesiasetus ja asetukset, joita naapurisi ovat muuttaneet. Valitse maasi, aseta esiasetus ja kopioi komennot.
description: MeshCoren radioesiasetus Euroopan eri alueilla sekä toistimen ja companionin asetukset, jotka paikalliset ryhmät ovat muuttaneet oletuksista, komentoineen.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '9547ba62'
  seeded: '2026-10-26'
  fields: {title: 'cfb32983', lead: 'f3f16725', description: 'cb15acd3'}
  sections: ['39848942', '43cde8b4']
---

Jokainen alla oleva alue käyttää omaa radioesiasetustaan tai muuttaa muutamaa
MeshCoren oletusasetusta. Kaikki, mitä ei mainita, pysyy oletusarvossa, joten
muutat vain sen, minkä alueesi on muuttanut. Toistin välittää viestit eteenpäin
kaikille. Companion on solmu, josta lähetät viestejä. Se on yhdistetty
puhelimeesi tai tietokoneeseesi Bluetoothilla tai USB:llä, tai siinä on oma näyttö.

[Toistinopas](/repeater-guide/#config) näyttää, miten pääset toistimesi
komentoriville. Tämän sivuston [sarjakonsolissa](/firmware/console/) kirjoitat
komennot itse. Jokaisen alueen kohdalla voit myös lähettää sen asetukset USB:n
kautta. Opas kertoo lisäksi 868 MHz:n [lailliset rajat](/repeater-guide/#legal).

## Pidä liikenne vähäisenä {#traffic}

Nämä asetukset pätevät jokaisella alueella. Jokainen toistin välittää eteenpäin
kaikki kuulemansa flood-viestit. Yksi lähettämäsi viesti maksaa yhden
lähetyksen, ja lisäksi yhden jokaista sen kuulevaa toistinta kohden. 10 %:n
toimintasuhteella toistin voi lähettää noin 680 pakettia tunnissa, ja kaikki
sen ympärillä jakavat tuon määrän. Tarpeettoman pitkälle kulkeva viesti syö
siitä osan.

**Lähetä pienimmälle alueelle, joka tavoittaa ne, joille kirjoitat.**
Alueet ovat sisäkkäisiä: maa, maakunta ja paikallinen ryhmä, kullakin oma
koodinsa, kuten `nl`, `nl-ov` ja `nl-ov-zwo`. Alueelle `nl-ov-zwo` tarkoitettu
viesti pysyy sen ryhmän toistimissa. Lisää jokainen toistin vain niille
alueille, joita se palvelee. [Paikallinen ryhmäsi](/community/) tietää, mitkä
ne ovat.

**Rajoita sitä, mitä toistimesi välittää eteenpäin.** Kaksi asetusta pitävät
lähellä kotia liikenteen, jonka ei tarvitse kulkea kaukaa:

```text
set flood.max.advert 3
set flood.max.unscoped 1
```

- `flood.max.advert 3`: ilmoitukset, jotka kertovat solmusta meshille, kulkevat
  enintään 3 hyppyä.
- `flood.max.unscoped 1`: viesti ilman aluetta kulkee enintään yhden toistimen
  läpi.
