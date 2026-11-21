---
title: Kontrolna lista za repetitor
lead: Proveri repetitor pre nego što ga postaviš. Svaka stavka navodi šta proveravaš, komandu koja to prikazuje i vodič koji to objašnjava.
description: 'Kontrolna lista za MeshCore repetitor pre postavljanja na krov ili jarbol: šta proveravaš preko USB-a, kako ga montiraš i koji test radiš pre odlaska.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '5bbc2cbe'
  seeded: '2026-11-21'
  fields: {title: 'e982ea2f', lead: '664a2839', description: '01f56863'}
  sections: ['d512dacf', '4d357087', '75706984', '8a484df5', '33fd8c68']
  blocks: ['d512dacf', 'a7ba4c46', '6a427551', '2f0a8827', '2bda1638', '589c7b4f', '5fedefb7', 'e12f330e', 'd6d0b21c']
---

Do repetitora na krovu teško se stiže, zato ga proveri dok je još na tvom
stolu. [Vodič za repetitor](/repeater-guide/) objašnjava svaki korak. Vrednosti,
kao što su preset i ograničenja hopova, nalaziš u
[podešavanjima za tvoje područje](/guides/settings/). Komande kucaš preko USB-a,
na primer u [serijskoj konzoli](/firmware/console/). Ova lista prati
MeshCore firmver v1.18.0.

## Pre nego što počneš {#start}

- [ ] Prema [mapama pokrivenosti](/map/) ili tvojoj [lokalnoj grupi](/community/),
      području treba repetitor. Pogledaj [Da li ti treba?](/repeater-guide/#need)
- [ ] Vlasnik lokacije se složio, a ti možeš da dođeš do repetitora radi
      održavanja.
- [ ] Baterija i panel su dimenzionisani za najgori zimski mesec. Pogledaj
      [Napajanje i dimenzionisanje solara](/repeater-guide/#power).

## Za stolom, preko USB-a {#usb}

- [ ] Na ploči radi firmver **Repeater**: `ver` prikazuje njegovu verziju. Pogledaj
      [Podesi ga](/repeater-guide/#config).
- [ ] Na nRF52 ploči odgovor na `get bootloader.ver` sadrži `OTAFIX`.
      Pogledaj [Ažuriraj ga bežično](/repeater-guide/#update).
- [ ] `get radio` prikazuje preset tvog područja.
- [ ] `get dutycycle` prikazuje 10. Pogledaj [Duty cycle](/repeater-guide/#duty-cycle).
- [ ] Vrednost iz `get tx` zajedno sa pojačanjem tvoje antene ostaje u okviru 500 mW e.r.p.
      Pogledaj [Snaga: e.r.p. i tvoja antena](/repeater-guide/#erp).
- [ ] Administratorska lozinka više nije `password`.
- [ ] `get guest.password` prikazuje lozinku.
- [ ] `get name` prikazuje ime koje tvoja lokalna grupa koristi za svoje repetitore.
- [ ] `get lat` i `get lon` prikazuju položaj lokacije.
- [ ] `get owner.info` prikazuje kako drugi operateri mogu da te kontaktiraju.
- [ ] `region` prikazuje regione tvog područja. `get flood.max.advert` i
      `get flood.max.unscoped` prikazuju njegova ograničenja hopova. Pogledaj
      [Smanji saobraćaj](/guides/settings/#traffic).
- [ ] Privatni ključ iz `get prv.key` sačuvao si na sigurnom mestu.
- [ ] `clock` prikazuje trenutno vreme u UTC-u.
- [ ] Na solarnom napajanju `powersaving` prikazuje `on`.

## Na krovu {#roof}

- [ ] Antena je priključena pre nego što repetitor dobije napajanje.
- [ ] Antena stoji uspravno na vrhu jarbola, podalje od metala. Pogledaj
      [Montaža](/guides/antenna/#mounting).
- [ ] Svaki spoljni konektor je zaptiven, a kabl ima petlju za oticanje vode.
- [ ] Kućište je zatvoreno i ima otvor za ventilaciju ili odvod vode. Pogledaj
      [Hardver](/repeater-guide/#hardware).

## Pre nego što odeš {#leave}

- [ ] Sa udaljenosti dolaziš do repetitora preko svog companiona u aplikaciji.
- [ ] Poslao si `advert`, pa čvorovi širom mesh mreže saznaju za repetitor.
- [ ] Tvoja [lokalna grupa](/community/) zna da repetitor radi.
