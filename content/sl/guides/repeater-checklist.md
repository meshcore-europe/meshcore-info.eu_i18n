---
title: Kontrolni seznam za repetitor
lead: Preveri repetitor, preden ga namestiš. Vsaka vrstica pove, kaj preveriš, kateri ukaz to pokaže in kateri vodnik to razloži.
description: 'Kontrolni seznam za repetitor MeshCore, preden gre na streho ali drog: kaj preveriš prek USB, kako ga pritrdiš in kaj preizkusiš, preden odideš.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '5bbc2cbe'
  seeded: '2026-11-21'
  fields: {title: 'e982ea2f', lead: '664a2839', description: '01f56863'}
  sections: ['d512dacf', '4d357087', '75706984', '8a484df5', '33fd8c68']
  blocks: ['d512dacf', 'a7ba4c46', '6a427551', '2f0a8827', '2bda1638', '589c7b4f', '5fedefb7', 'e12f330e', 'd6d0b21c']
---

Do repetitorja na strehi težko prideš, zato ga preveri, dokler je še na tvoji
mizi. [Vodnik za repetitor](/repeater-guide/) razloži vsak korak. Vrednosti,
na primer prednastavitev in omejitve skokov, najdeš v
[nastavitvah za tvoje območje](/guides/settings/). Ukaze vpiši prek USB, na
primer v [serijski konzoli](/firmware/console/). Seznam velja za vdelano
programsko opremo MeshCore v1.18.0.

## Preden začneš {#start}

- [ ] [Zemljevidi pokritosti](/map/) ali tvoja [lokalna skupina](/community/)
      kažejo, da območje potrebuje repetitor. Glej [Ga potrebuješ?](/repeater-guide/#need)
- [ ] Lastnik lokacije je privolil, ti pa imaš dostop do repetitorja za
      vzdrževanje.
- [ ] Baterija in sončni panel sta dimenzionirana za najslabši zimski mesec. Glej
      [Napajanje in dimenzioniranje sončnega sistema](/repeater-guide/#power).

## Za mizo, prek USB {#usb}

- [ ] Na plošči teče vdelana programska oprema **Repeater**: `ver` pokaže
      njeno različico. Glej [Nastavi ga](/repeater-guide/#config).
- [ ] Na plošči nRF52 odgovor na `get bootloader.ver` vsebuje `OTAFIX`. Glej
      [Posodobi ga brezžično](/repeater-guide/#update).
- [ ] `get radio` pokaže prednastavitev tvojega območja.
- [ ] `get dutycycle` pokaže 10. Glej [Delovni cikel](/repeater-guide/#duty-cycle).
- [ ] `get tx` skupaj z ojačanjem tvoje antene ne preseže 500 mW e.r.p. Glej
      [Moč: e.r.p. in tvoja antena](/repeater-guide/#erp).
- [ ] Skrbniško geslo ni več `password`.
- [ ] `get guest.password` pokaže geslo.
- [ ] `get name` pokaže ime, ki ga tvoja lokalna skupina uporablja za svoje
      repetitorje.
- [ ] `get lat` in `get lon` pokažeta položaj lokacije.
- [ ] `get owner.info` pokaže, kako te drugi upravljavci lahko dosežejo.
- [ ] `region` pokaže regije tvojega območja. `get flood.max.advert` in
      `get flood.max.unscoped` pokažeta njegove omejitve skokov. Glej
      [Zmanjšaj promet](/guides/settings/#traffic).
- [ ] Zasebni ključ iz `get prv.key` si shranil na varno mesto.
- [ ] `clock` pokaže trenutni čas v UTC.
- [ ] Pri sončnem napajanju `powersaving` pokaže `on`.

## Na strehi {#roof}

- [ ] Antena je priključena, preden repetitor dobi napajanje.
- [ ] Antena stoji pokončno na vrhu droga, stran od kovine. Glej
      [Pritrditev](/guides/antenna/#mounting).
- [ ] Vsak zunanji konektor je zatesnjen, kabel pa ima odkapno zanko.
- [ ] Ohišje je zaprto in ima odprtino za zračenje ali odtok. Glej
      [Strojna oprema](/repeater-guide/#hardware).

## Preden odideš {#leave}

- [ ] Tvoj companion v aplikaciji od daleč doseže repetitor.
- [ ] Poslal si `advert`, da vozlišča po vsej mreži izvejo za repetitor.
- [ ] Tvoja [lokalna skupina](/community/) ve, da repetitor deluje.
