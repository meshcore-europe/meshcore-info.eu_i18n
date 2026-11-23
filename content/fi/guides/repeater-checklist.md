---
title: Toistimen tarkistuslista
lead: Tarkista toistin ennen kuin viet sen paikalleen. Jokaisella rivillä on tarkistettava asia, komento, joka näyttää sen, ja opas, joka selittää sen.
description: 'Tarkistuslista MeshCore-toistimelle ennen kuin se nousee katolle tai mastoon: mitä tarkistat USB:n kautta, miten asennat sen ja mitä testaat ennen lähtöä.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '5bbc2cbe'
  seeded: '2026-11-21'
  fields: {title: 'e982ea2f', lead: '664a2839', description: '01f56863'}
  sections: ['d512dacf', '4d357087', '75706984', '8a484df5', '33fd8c68']
  blocks: ['d512dacf', 'a7ba4c46', '6a427551', '2f0a8827', '2bda1638', '589c7b4f', '5fedefb7', 'e12f330e', 'd6d0b21c']
---

Katolla olevan toistimen luo on vaikea päästä. Tarkista se siis, kun se on vielä pöydälläsi. [Toistinopas](/repeater-guide/) käy läpi jokaisen vaiheen. Arvot, kuten esiasetus ja hyppyrajat, löydät [alueesi asetuksista](/guides/settings/). Kirjoita komennot USB:n kautta, esimerkiksi [sarjakonsolissa](/firmware/console/). Tämä lista perustuu MeshCore-laiteohjelmiston versioon v1.18.0.

## Ennen kuin aloitat {#start}

- [ ] [Kuuluvuuskartat](/map/) tai [paikallinen ryhmäsi](/community/) kertovat, että alue tarvitsee toistimen. Katso [Tarvitsetko toistimen?](/repeater-guide/#need)
- [ ] Paikan omistaja on antanut luvan, ja pääset toistimen luo huoltamaan sitä.
- [ ] Akku ja paneeli on mitoitettu talven pahimman kuukauden mukaan. Katso [Virta ja aurinkopaneelin mitoitus](/repeater-guide/#power).

## Pöydän ääressä, USB:n kautta {#usb}

- [ ] Laitteessa on **Repeater**-laiteohjelmisto: `ver` näyttää sen version. Katso [Määritä toistin](/repeater-guide/#config).
- [ ] nRF52-laitteessa komennon `get bootloader.ver` vastauksessa lukee `OTAFIX`. Katso [Päivitä toistin langattomasti](/repeater-guide/#update).
- [ ] `get radio` näyttää alueesi esiasetuksen.
- [ ] `get dutycycle` näyttää arvon 10. Katso [Käyttösuhde](/repeater-guide/#duty-cycle).
- [ ] `get tx` -arvo ja antennisi vahvistus eivät yhteensä ylitä 500 mW e.r.p.:tä. Katso [Teho: e.r.p. ja antennisi](/repeater-guide/#erp).
- [ ] Ylläpitäjän salasana ei ole enää `password`.
- [ ] `get guest.password` näyttää salasanan.
- [ ] `get name` näyttää nimen, jota paikallinen ryhmäsi käyttää toistimistaan.
- [ ] `get lat` ja `get lon` näyttävät paikan sijainnin.
- [ ] `get owner.info` kertoo, miten muut ylläpitäjät tavoittavat sinut.
- [ ] `region` näyttää seutusi alueet. `get flood.max.advert` ja `get flood.max.unscoped` näyttävät seutusi hyppyrajat. Katso [Pidä liikenne vähäisenä](/guides/settings/#traffic).
- [ ] Olet tallentanut `get prv.key` -komennon näyttämän yksityisen avaimen turvalliseen paikkaan.
- [ ] `clock` näyttää tämänhetkisen UTC-ajan.
- [ ] Aurinkovirralla toimivassa toistimessa `powersaving` näyttää `on`.

## Katolla {#roof}

- [ ] Antenni on kiinnitetty ennen kuin toistin saa virtaa.
- [ ] Antenni on pystyssä maston huipulla, kaukana metallista. Katso [Asennus](/guides/antenna/#mounting).
- [ ] Jokainen ulkoliitin on tiivistetty, ja kaapelissa on tippalenkki.
- [ ] Kotelo on suljettu, ja siinä on tuuletus- tai valutusreikä. Katso [Laitteisto](/repeater-guide/#hardware).

## Ennen kuin lähdet {#leave}

- [ ] Etäältä companion-laitteesi tavoittaa toistimen sovelluksessa.
- [ ] Olet lähettänyt komennon `advert`, jotta solmut koko meshissä saavat tiedon toistimesta.
- [ ] [Paikallinen ryhmäsi](/community/) tietää, että toistin on toiminnassa.
