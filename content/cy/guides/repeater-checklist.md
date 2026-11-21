---
title: Rhestr wirio'r ailadroddydd
lead: Gwiria dy ailadroddydd cyn iddo fynd i fyny. Mae pob llinell yn enwi beth i'w wirio, y gorchymyn sy'n ei ddangos a'r canllaw sy'n ei esbonio.
description: 'Rhestr wirio ar gyfer ailadroddydd MeshCore cyn iddo fynd ar do neu fast: beth i''w wirio dros USB, sut i''w osod, a''r prawf cyn i ti adael.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '5bbc2cbe'
  seeded: '2026-11-21'
  fields: {title: 'e982ea2f', lead: '664a2839', description: '01f56863'}
  sections: ['d512dacf', '4d357087', '75706984', '8a484df5', '33fd8c68']
  blocks: ['d512dacf', 'a7ba4c46', '6a427551', '2f0a8827', '2bda1638', '589c7b4f', '5fedefb7', 'e12f330e', 'd6d0b21c']
---

Mae'n anodd cyrraedd ailadroddydd ar do, felly gwiria fe tra mae'n dal ar dy
ddesg. Mae'r [canllaw ailadroddydd](/repeater-guide/) yn esbonio pob cam. Mae'r
gwerthoedd, fel y rhagosodiad a'r terfynau naid, yn dod o
[osodiadau dy ardal](/guides/settings/). Teipia'r gorchmynion dros USB, er
enghraifft yn y [consol cyfresol](/firmware/console/). Mae'r rhestr hon yn
dilyn cadarnwedd MeshCore v1.18.0.

## Cyn i ti ddechrau {#start}

- [ ] Mae'r [mapiau darpariaeth](/map/) neu dy [grŵp lleol](/community/) yn
      dweud bod angen ailadroddydd ar yr ardal. Gweler
      [Oes angen un arnat ti?](/repeater-guide/#need)
- [ ] Mae perchennog y safle wedi cytuno, ac rwyt ti'n gallu cyrraedd yr
      ailadroddydd i'w gynnal.
- [ ] Mae'r batri a'r panel wedi'u maintioli ar gyfer mis gwaethaf y gaeaf.
      Gweler [Maintioli pŵer a solar](/repeater-guide/#power).

## Wrth dy ddesg, dros USB {#usb}

- [ ] Mae'r bwrdd yn rhedeg cadarnwedd **Repeater**: mae `ver` yn dangos ei
      fersiwn. Gweler [Ei sefydlu](/repeater-guide/#config).
- [ ] Ar fwrdd nRF52, mae `OTAFIX` yn yr ateb i `get bootloader.ver`. Gweler
      [Diweddara fe dros yr awyr](/repeater-guide/#update).
- [ ] Mae `get radio` yn dangos rhagosodiad dy ardal.
- [ ] Mae `get dutycycle` yn dangos 10. Gweler [Cylch dyletswydd](/repeater-guide/#duty-cycle).
- [ ] Mae `get tx` ac ennill dy antena gyda'i gilydd yn aros o fewn 500 mW
      e.r.p. Gweler [Pŵer: e.r.p. a dy antena](/repeater-guide/#erp).
- [ ] Nid `password` yw'r cyfrinair gweinyddu bellach.
- [ ] Mae `get guest.password` yn dangos cyfrinair.
- [ ] Mae `get name` yn dangos yr enw mae dy grŵp lleol yn ei roi i'w
      ailadroddyddion.
- [ ] Mae `get lat` a `get lon` yn dangos lleoliad y safle.
- [ ] Mae `get owner.info` yn dangos sut mae gweithredwyr eraill yn dy
      gyrraedd di.
- [ ] Mae `region` yn dangos rhanbarthau dy ardal. Mae `get flood.max.advert`
      a `get flood.max.unscoped` yn dangos ei therfynau naid. Gweler
      [Cadw'r traffig yn isel](/guides/settings/#traffic).
- [ ] Rwyt ti wedi cadw'r allwedd breifat o `get prv.key` yn rhywle diogel.
- [ ] Mae `clock` yn dangos yr amser ar hyn o bryd, yn UTC.
- [ ] Ar solar, mae `powersaving` yn dangos `on`.

## Ar y to {#roof}

- [ ] Mae'r antena wedi'i chysylltu cyn i'r ailadroddydd gael pŵer.
- [ ] Mae'r antena'n sefyll yn syth ar ben y mast, ymhell o fetel. Gweler
      [Mowntio](/guides/antenna/#mounting).
- [ ] Mae pob cysylltydd allanol wedi'i selio, ac mae dolen ddiferu ar y cebl.
- [ ] Mae'r cas ar gau, gyda thwll awyru neu dwll draenio. Gweler
      [Caledwedd](/repeater-guide/#hardware).

## Cyn i ti adael {#leave}

- [ ] O bellter, mae dy gydymaith yn cyrraedd yr ailadroddydd yn yr ap.
- [ ] Rwyt ti wedi anfon `advert`, felly mae nodau ar draws y rhwyll yn dysgu
      am yr ailadroddydd.
- [ ] Mae dy [grŵp lleol](/community/) yn gwybod ei fod e ar waith.
