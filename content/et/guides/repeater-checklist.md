---
title: Repiitri kontrollnimekiri
lead: Kontrolli oma repiiter üle enne, kui see üles läheb. Igal real on kirjas, mida kontrollida, milline käsk seda näitab ja milline juhend seda selgitab.
description: 'MeshCore repiitri kontrollnimekiri enne katusele või mastile paigaldamist: mida USB kaudu kontrollida, kuidas seda kinnitada ja milline test teha enne lahkumist.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '5bbc2cbe'
  seeded: '2026-11-21'
  fields: {title: 'e982ea2f', lead: '664a2839', description: '01f56863'}
  sections: ['d512dacf', '4d357087', '75706984', '8a484df5', '33fd8c68']
  blocks: ['d512dacf', 'a7ba4c46', '6a427551', '2f0a8827', '2bda1638', '589c7b4f', '5fedefb7', 'e12f330e', 'd6d0b21c']
---

Katusel olevale repiitrile on raske ligi pääseda. Seepärast kontrolli seda, kui see
on veel sinu laual. [Repiitri juhend](/repeater-guide/) selgitab iga sammu. Väärtused,
näiteks eelseadistus ja hüpete piirangud, pärinevad
[sinu piirkonna seadetest](/guides/settings/). Sisesta käsud USB kaudu,
näiteks [jadakonsoolis](/firmware/console/). See nimekiri järgib
MeshCore püsivara versiooni v1.18.0.

## Enne alustamist {#start}

- [ ] [Leviala kaardid](/map/) või sinu [kohalik grupp](/community/) ütlevad,
      et piirkond vajab repiitrit. Vaata [Kas sul on seda vaja?](/repeater-guide/#need)
- [ ] Asukoha omanik on nõus ja sa pääsed repiitrile hoolduseks ligi.
- [ ] Aku ja paneel on dimensioneeritud kõige halvema talvekuu järgi. Vaata
      [Toide ja päikesepaneeli dimensioneerimine](/repeater-guide/#power).

## Laua taga, USB kaudu {#usb}

- [ ] Plaadil töötab **Repeater** püsivara: `ver` näitab selle versiooni. Vaata
      [Seadista see](/repeater-guide/#config).
- [ ] nRF52 plaadi puhul on käsu `get bootloader.ver` vastuses `OTAFIX`.
      Vaata [Uuenda seda üle õhu](/repeater-guide/#update).
- [ ] `get radio` näitab sinu piirkonna eelseadistust.
- [ ] `get dutycycle` näitab väärtust 10. Vaata [Töötsükkel](/repeater-guide/#duty-cycle).
- [ ] `get tx` koos sinu antenni võimendusega jääb 500 mW e.r.p. piiresse. Vaata
      [Võimsus: e.r.p. ja sinu antenn](/repeater-guide/#erp).
- [ ] Administraatori parool ei ole enam `password`.
- [ ] `get guest.password` näitab parooli.
- [ ] `get name` näitab nime, mida sinu kohalik grupp oma repiitritele kasutab.
- [ ] `get lat` ja `get lon` näitavad asukoha koordinaate.
- [ ] `get owner.info` näitab, kuidas teised operaatorid sinuga ühendust saavad.
- [ ] `region` näitab piirkondi, mis sinu kandis kehtivad. `get flood.max.advert` ja
      `get flood.max.unscoped` näitavad seal kehtivaid hüpete piiranguid. Vaata
      [Hoia liiklus väikesena](/guides/settings/#traffic).
- [ ] Oled käsu `get prv.key` antud privaatvõtme turvalisse kohta salvestanud.
- [ ] `clock` näitab praegust kellaaega UTC järgi.
- [ ] Päikesetoite puhul näitab `powersaving` väärtust `on`.

## Katusel {#roof}

- [ ] Antenn on ühendatud enne, kui repiiter toite saab.
- [ ] Antenn seisab püstiselt masti tipus, metallist eemal. Vaata
      [Paigaldamine](/guides/antenna/#mounting).
- [ ] Iga välispistik on tihendatud ja kaablil on tilgasilmus.
- [ ] Korpus on suletud ning sellel on õhutus- või äravooluava. Vaata
      [Riistvara](/repeater-guide/#hardware).

## Enne lahkumist {#leave}

- [ ] Sinu companion jõuab rakenduses eemalt repiitrini.
- [ ] Oled saatnud käsu `advert`, et sõlmed üle kogu võrgu repiitrist teada saaksid.
- [ ] Sinu [kohalik grupp](/community/) teab, et repiiter töötab.
