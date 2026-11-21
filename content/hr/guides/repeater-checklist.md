---
title: Kontrolni popis za repetitor
lead: Provjeri svoj repetitor prije nego što ga postaviš. Svaka stavka navodi što provjeravaš, naredbu koja to prikazuje i vodič koji to objašnjava.
description: 'Kontrolni popis za MeshCore repetitor prije postavljanja na krov ili jarbol: što provjeriti preko USB-a, kako ga montirati i koji test napraviti prije odlaska.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '5bbc2cbe'
  seeded: '2026-11-21'
  fields: {title: 'e982ea2f', lead: '664a2839', description: '01f56863'}
  sections: ['d512dacf', '4d357087', '75706984', '8a484df5', '33fd8c68']
  blocks: ['d512dacf', 'a7ba4c46', '6a427551', '2f0a8827', '2bda1638', '589c7b4f', '5fedefb7', 'e12f330e', 'd6d0b21c']
---

Do repetitora na krovu teško se dolazi, zato ga provjeri dok je još na tvom
stolu. [Vodič za repetitor](/repeater-guide/) objašnjava svaki korak.
Vrijednosti poput preseta i ograničenja skokova uzmi iz
[postavki za tvoje područje](/guides/settings/). Naredbe upisuj preko USB-a,
na primjer u [serijskoj konzoli](/firmware/console/). Ovaj popis prati
MeshCore firmware v1.18.0.

## Prije nego što počneš {#start}

- [ ] [Karte pokrivenosti](/map/) ili tvoja [lokalna grupa](/community/)
      pokazuju da području treba repetitor. Vidi [Treba li ti?](/repeater-guide/#need)
- [ ] Vlasnik lokacije je pristao, a ti možeš doći do repetitora radi
      održavanja.
- [ ] Baterija i panel dimenzionirani su za najgori zimski mjesec. Vidi
      [Napajanje i dimenzioniranje solara](/repeater-guide/#power).

## Za stolom, preko USB-a {#usb}

- [ ] Na pločici je **Repeater** firmware: `ver` prikazuje njegovu verziju. Vidi
      [Postavljanje](/repeater-guide/#config).
- [ ] Na nRF52 pločici odgovor na `get bootloader.ver` sadrži `OTAFIX`.
      Vidi [Ažuriranje bežičnim putem](/repeater-guide/#update).
- [ ] `get radio` prikazuje preset tvojeg područja.
- [ ] `get dutycycle` prikazuje 10. Vidi [Duty cycle](/repeater-guide/#duty-cycle).
- [ ] `get tx` zajedno s pojačanjem tvoje antene ne prelazi 500 mW e.r.p. Vidi
      [Snaga: e.r.p. i tvoja antena](/repeater-guide/#erp).
- [ ] Administratorska lozinka više nije `password`.
- [ ] `get guest.password` prikazuje lozinku.
- [ ] `get name` prikazuje ime koje tvoja lokalna grupa daje svojim repetitorima.
- [ ] `get lat` i `get lon` prikazuju položaj lokacije.
- [ ] `get owner.info` prikazuje kako te drugi operateri mogu kontaktirati.
- [ ] `region` prikazuje regije tvojeg područja. `get flood.max.advert` i
      `get flood.max.unscoped` prikazuju ograničenja skokova tog područja. Vidi
      [Smanji promet](/guides/settings/#traffic).
- [ ] Privatni ključ iz `get prv.key` spremio si na sigurno mjesto.
- [ ] `clock` prikazuje trenutačno vrijeme u UTC-u.
- [ ] Kod solarnog napajanja `powersaving` prikazuje `on`.

## Na krovu {#roof}

- [ ] Antena je spojena prije nego što repetitor dobije napajanje.
- [ ] Antena stoji uspravno na vrhu jarbola, podalje od metala. Vidi
      [Montaža](/guides/antenna/#mounting).
- [ ] Svaki vanjski konektor je zabrtvljen, a kabel ima petlju za otjecanje vode.
- [ ] Kućište je zatvoreno, s otvorom za ventilaciju ili odvod vode. Vidi
      [Hardver](/repeater-guide/#hardware).

## Prije nego što odeš {#leave}

- [ ] Tvoj companion iz daljine u aplikaciji doseže repetitor.
- [ ] Poslao si `advert`, pa čvorovi diljem mesha saznaju za repetitor.
- [ ] Tvoja [lokalna grupa](/community/) zna da repetitor radi.
