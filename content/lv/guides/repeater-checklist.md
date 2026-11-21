---
title: Retranslatora pārbaudes saraksts
lead: Pārbaudi savu retranslatoru, pirms to uzstādi. Katrā rindā ir norādīts, kas jāpārbauda, kura komanda to parāda un kura rokasgrāmata to izskaidro.
description: 'MeshCore retranslatora pārbaudes saraksts pirms uzstādīšanas uz jumta vai masta: ko pārbaudīt caur USB, kā to nostiprināt un kāds tests jāveic pirms aiziešanas.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '5bbc2cbe'
  seeded: '2026-11-21'
  fields: {title: 'e982ea2f', lead: '664a2839', description: '01f56863'}
  sections: ['d512dacf', '4d357087', '75706984', '8a484df5', '33fd8c68']
  blocks: ['d512dacf', 'a7ba4c46', '6a427551', '2f0a8827', '2bda1638', '589c7b4f', '5fedefb7', 'e12f330e', 'd6d0b21c']
---

Retranslatoram uz jumta ir grūti piekļūt, tāpēc pārbaudi to, kamēr tas vēl ir
uz tava galda. [Retranslatora rokasgrāmatā](/repeater-guide/) ir izskaidrots
katrs solis. Vērtības, piemēram, priekšiestatījumu un lēcienu ierobežojumus,
tu atradīsi [sava apgabala iestatījumos](/guides/settings/). Komandas ievadi
caur USB, piemēram, [seriālajā konsolē](/firmware/console/). Šis saraksts
atbilst MeshCore programmaparatūrai v1.18.0.

## Pirms sāc {#start}

- [ ] [Pārklājuma kartes](/map/) vai tava [vietējā grupa](/community/) rāda,
      ka apgabalam vajag retranslatoru. Skaties [Vai tev tas vajadzīgs?](/repeater-guide/#need)
- [ ] Uzstādīšanas vietas īpašnieks ir piekritis, un tu vari piekļūt
      retranslatoram apkopes darbiem.
- [ ] Akumulatora un paneļa jauda ir aprēķināta sliktākajam ziemas mēnesim.
      Skaties [Barošana un saules paneļa izmērs](/repeater-guide/#power).

## Pie galda, caur USB {#usb}

- [ ] Platē darbojas **Repeater** programmaparatūra: `ver` parāda tās versiju.
      Skaties [Iestatīšana](/repeater-guide/#config).
- [ ] nRF52 platē atbildē uz `get bootloader.ver` ir `OTAFIX`. Skaties
      [Atjaunināšana pa gaisu](/repeater-guide/#update).
- [ ] `get radio` parāda tava apgabala priekšiestatījumu.
- [ ] `get dutycycle` parāda 10. Skaties [Darba cikls](/repeater-guide/#duty-cycle).
- [ ] `get tx` kopā ar tavas antenas pastiprinājumu nepārsniedz 500 mW e.r.p.
      Skaties [Jauda: e.r.p. un tava antena](/repeater-guide/#erp).
- [ ] Administratora parole vairs nav `password`.
- [ ] `get guest.password` parāda paroli.
- [ ] `get name` parāda nosaukumu, ko tava vietējā grupa lieto saviem
      retranslatoriem.
- [ ] `get lat` un `get lon` parāda uzstādīšanas vietas koordinātas.
- [ ] `get owner.info` parāda, kā citi operatori var ar tevi sazināties.
- [ ] `region` parāda tava apgabala reģionus. `get flood.max.advert` un
      `get flood.max.unscoped` parāda tā lēcienu ierobežojumus. Skaties
      [Samazini datplūsmu](/guides/settings/#traffic).
- [ ] Tu esi saglabājis privāto atslēgu no `get prv.key` drošā vietā.
- [ ] `clock` parāda pašreizējo laiku UTC.
- [ ] Ja izmanto saules paneli, `powersaving` parāda `on`.

## Uz jumta {#roof}

- [ ] Antena ir pievienota, pirms tu pieslēdz retranslatoram barošanu.
- [ ] Antena stāv vertikāli masta galā, tālu no metāla. Skaties
      [Montāža](/guides/antenna/#mounting).
- [ ] Katrs āra savienotājs ir noblīvēts, un kabelim ir pilienu cilpa.
- [ ] Korpuss ir aizvērts, un tam ir ventilācijas vai drenāžas atvere. Skaties
      [Aparatūra](/repeater-guide/#hardware).

## Pirms aizej {#leave}

- [ ] No attāluma tu ar savu companion lietotnē sasniedz retranslatoru.
- [ ] Tu nosūtīji `advert`, lai mezgli visā mesh tīklā uzzinātu par
      retranslatoru.
- [ ] Tava [vietējā grupa](/community/) zina, ka tas darbojas.
