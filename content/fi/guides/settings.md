---
title: Suositellut asetukset
layout: settings
lead: Alueesi käyttämä radioesiasetus ja asetukset, joita naapurisi ovat muuttaneet. Valitse maasi, ota esiasetus käyttöön ja kopioi komennot.
description: MeshCoren radioesiasetus alueittain Euroopassa sekä toistimen ja companion-solmun asetukset, joita paikalliset ryhmät ovat muuttaneet oletuksista, komentoineen.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '0876215b'
  seeded: '2026-10-31'
  fields: {title: 'cfb32983', lead: 'f3f16725', description: 'cb15acd3'}
  sections: ['39848942', 'd1606fcd']
  blocks: ['8c9e88ea', '50ac6063', '85c2203d', '15f91217', 'bdf5fa4e', '69d8e70b', '28f83120', 'fe27027b']
---

Jokainen alla oleva alue käyttää omaa radioesiasetustaan tai muuttaa muutamaa
MeshCoren oletusasetusta. Kaikki, mitä ei mainita, pysyy oletuksena, joten muutat vain sen, minkä
alueesi on muuttanut. Toistin välittää viestejä eteenpäin kaikille. Companion on
solmu, josta lähetät viestisi. Se on pariliitoksessa puhelimeesi tai
kannettavaasi Bluetoothin tai USB:n kautta, tai siinä on oma näyttö.

[Toistinoppaasta](/repeater-guide/#config) näet, miten pääset toistimesi
komentoriville. Tämän sivuston [sarjakonsolissa](/firmware/console/) kirjoitat
komennot itse. Jokaisen alueen kohdalla voit myös lähettää sen asetukset USB:n
kautta. Oppaassa ovat myös 868 MHz:n taajuuden [lailliset rajat](/repeater-guide/#legal).

## Pidä liikenne vähäisenä {#traffic}

Nämä asetukset koskevat kaikkia alueita. Jokainen toistin välittää eteenpäin
jokaisen kuulemansa flood-viestin. Yksi viestisi vaatii yhden lähetyksen ja
lisäksi yhden jokaista sen kuulevaa toistinta kohden. 10 %:n käyttösuhteen
rajoissa toistin voi lähettää noin 680 pakettia tunnissa. Kaikki sen
ympäristössä jakavat tämän määrän. Tarpeettoman kauas kulkeva viesti kuluttaa
siitä osan.

**Lähetä pienimmälle alueelle, joka tavoittaa ne, joille kirjoitat.**
Alueet ovat sisäkkäisiä: maa, maakunta ja paikallinen ryhmä. Jokaisella on oma
koodinsa, esimerkiksi `nl`, `nl-ov` ja `nl-ov-zwo`. Alueelle `nl-ov-zwo`
lähetetty viesti pysyy tuon ryhmän toistimissa. Toistin välittää vain alueita,
jotka sillä itsellään on. Jos toistimella on `nl`, se ei silti välitä
aluetta `nl-ov`. Lisää jokaiselle toistimelle kaikki alueet, joita se palvelee,
eikä muita. [Paikallinen ryhmäsi](/community/) tietää, mitkä ne ovat.

**Rajoita, mitä toistimesi välittää.** Kahdella asetuksella pidät lähiseudulla
liikenteen, jonka ei tarvitse kulkea kauas:

```text
set flood.max.advert 3
set flood.max.unscoped 1
```

- `flood.max.advert 3`: ilmoitukset, joilla solmu kertoo itsestään meshille,
  kulkevat enintään 3 hyppyä.
- `flood.max.unscoped 1`: viesti, jolla ei ole aluetta, kulkee enintään yhden toistimen
  kautta.
