---
title: Errepikagailuaren egiaztapen-zerrenda
lead: Egiaztatu errepikagailua instalatu aurretik. Lerro bakoitzak zer egiaztatu, hori erakusten duen komandoa eta azaltzen duen gida adierazten ditu.
description: 'MeshCore errepikagailu baterako egiaztapen-zerrenda, teilatuan edo mastan jarri aurretik: USB bidez zer egiaztatu, nola muntatu eta joan aurreko proba.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '5bbc2cbe'
  seeded: '2026-11-21'
  fields: {title: 'e982ea2f', lead: '664a2839', description: '01f56863'}
  sections: ['d512dacf', '4d357087', '75706984', '8a484df5', '33fd8c68']
  blocks: ['d512dacf', 'a7ba4c46', '6a427551', '2f0a8827', '2bda1638', '589c7b4f', '5fedefb7', 'e12f330e', 'd6d0b21c']
---

Teilatuko errepikagailu batera iristea zaila da. Beraz, egiaztatu oraindik mahai gainean duzunean. [Errepikagailuaren gidak](/repeater-guide/) urrats guztiak azaltzen ditu. Balioak, adibidez preseta eta jauzi-mugak, [zure inguruko ezarpenetatik](/guides/settings/) datoz. Idatzi komandoak USB bidez, adibidez [serie-kontsolan](/firmware/console/). Zerrenda hau MeshCore firmwarearen v1.18.0 bertsioan oinarritzen da.

## Hasi aurretik {#start}

- [ ] [Estaldura-mapek](/map/) edo zure [tokiko taldeak](/community/) diote
      inguruak errepikagailu bat behar duela. Ikus [Behar al duzu?](/repeater-guide/#need)
- [ ] Lekuaren jabeak baimena eman du, eta errepikagailura irits zaitezke
      mantentze-lanetarako.
- [ ] Bateria eta panela neguko hilabete txarrenerako neurtuta daude. Ikus
      [Elikadura eta eguzki-panelen neurketa](/repeater-guide/#power).

## Mahaian, USB bidez {#usb}

- [ ] Plakak **Repeater** firmwarea darabil: `ver` komandoak haren bertsioa
      erakusten du. Ikus [Konfiguratu](/repeater-guide/#config).
- [ ] nRF52 plaka batean, `get bootloader.ver` komandoaren erantzunean `OTAFIX`
      agertzen da. Ikus [Eguneratu airez](/repeater-guide/#update).
- [ ] `get radio` komandoak zure inguruko preseta erakusten du.
- [ ] `get dutycycle` komandoak 10 erakusten du. Ikus [Duty cycle](/repeater-guide/#duty-cycle).
- [ ] `get tx` balioa gehi zure antenaren irabazia 500 mW e.r.p. muga barruan geratzen da.
      Ikus [Potentzia: e.r.p. eta zure antena](/repeater-guide/#erp).
- [ ] Administratzailearen pasahitza ez da jada `password`.
- [ ] `get guest.password` komandoak pasahitz bat erakusten du.
- [ ] `get name` komandoak zure tokiko taldeak bere errepikagailuetarako
      erabiltzen duen izena erakusten du.
- [ ] `get lat` eta `get lon` komandoek lekuaren kokapena erakusten dute.
- [ ] `get owner.info` komandoak beste operadoreek zurekin nola harremanetan
      jar daitezkeen erakusten du.
- [ ] `region` komandoak zure inguruko eskualdeak erakusten ditu.
      `get flood.max.advert` eta `get flood.max.unscoped` komandoek inguruko
      jauzi-mugak erakusten dituzte. Ikus [Murriztu trafikoa](/guides/settings/#traffic).
- [ ] `get prv.key` komandoak erakusten duen gako pribatua leku seguru batean gorde duzu.
- [ ] `clock` komandoak uneko ordua erakusten du, UTC-n.
- [ ] Eguzki-energiaz dabilenean, `powersaving` komandoak `on` erakusten du.

## Teilatuan {#roof}

- [ ] Antena konektatuta dago errepikagailuak elikadura jaso aurretik.
- [ ] Antena zutik dago mastaren goialdean, metaletik urrun. Ikus
      [Muntatzea](/guides/antenna/#mounting).
- [ ] Kanpoko konektore guztiak zigilatuta daude, eta kableak tanta-begizta du.
- [ ] Kaxa itxita dago, aireztapen- edo drainatze-zulo batekin. Ikus
      [Hardwarea](/repeater-guide/#hardware).

## Joan aurretik {#leave}

- [ ] Urrutitik, zure companion-a errepikagailura iristen da aplikazioan.
- [ ] `advert` bidali duzu, mesh sare osoko nodoek errepikagailuaren berri izan dezaten.
- [ ] Zure [tokiko taldeak](/community/) badaki martxan dagoela.
