---
title: Retransliatoriaus kontrolinis sąrašas
lead: Patikrink retransliatorių, kol dar jo neiškėlei. Kiekvienoje eilutėje rasi, ką tikrinti, kokia komanda tai parodo ir kuris vadovas tai paaiškina.
description: 'MeshCore retransliatoriaus kontrolinis sąrašas prieš keliant jį ant stogo ar stiebo: ką patikrinti per USB, kaip jį pritvirtinti ir kaip išbandyti prieš išeinant.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '5bbc2cbe'
  seeded: '2026-11-21'
  fields: {title: 'e982ea2f', lead: '664a2839', description: '01f56863'}
  sections: ['d512dacf', '4d357087', '75706984', '8a484df5', '33fd8c68']
  blocks: ['d512dacf', 'a7ba4c46', '6a427551', '2f0a8827', '2bda1638', '589c7b4f', '5fedefb7', 'e12f330e', 'd6d0b21c']
---

Ant stogo retransliatorių sunku pasiekti, todėl patikrink jį, kol jis dar guli ant
tavo stalo. [Retransliatoriaus vadove](/repeater-guide/) paaiškintas kiekvienas
žingsnis. Reikšmes, pavyzdžiui, profilį ir šuolių ribas, rasi
[tavo vietovės nustatymuose](/guides/settings/). Komandas įvesk per USB,
pavyzdžiui, [nuosekliojoje konsolėje](/firmware/console/). Šis sąrašas atitinka
MeshCore programinės įrangos versiją v1.18.0.

## Prieš pradėdamas {#start}

- [ ] [Aprėpties žemėlapiai](/map/) arba tavo [vietinė grupė](/community/)
      rodo, kad vietovei reikia retransliatoriaus. Žr. [Ar jo tau reikia?](/repeater-guide/#need)
- [ ] Vietos savininkas sutiko ir tu gali prieiti prie retransliatoriaus
      techninei priežiūrai.
- [ ] Baterija ir saulės modulis parinkti pagal blogiausią žiemos mėnesį. Žr.
      [Maitinimas ir saulės sistemos dydis](/repeater-guide/#power).

## Prie stalo, per USB {#usb}

- [ ] Plokštėje veikia **Repeater** programinė įranga: `ver` parodo jos
      versiją. Žr. [Nustatyk jį](/repeater-guide/#config).
- [ ] nRF52 plokštėje atsakyme į `get bootloader.ver` yra `OTAFIX`. Žr.
      [Atnaujink jį belaidžiu ryšiu](/repeater-guide/#update).
- [ ] `get radio` parodo tavo vietovės profilį.
- [ ] `get dutycycle` parodo 10. Žr. [Darbo ciklas](/repeater-guide/#duty-cycle).
- [ ] `get tx` kartu su tavo antenos stiprinimu neviršija 500 mW e.r.p. Žr.
      [Galia: e.r.p. ir tavo antena](/repeater-guide/#erp).
- [ ] Administratoriaus slaptažodis nebėra `password`.
- [ ] `get guest.password` parodo slaptažodį.
- [ ] `get name` parodo pavadinimą, kurį tavo vietinė grupė naudoja savo
      retransliatoriams.
- [ ] `get lat` ir `get lon` parodo vietos koordinates.
- [ ] `get owner.info` parodo, kaip kiti operatoriai gali su tavimi susisiekti.
- [ ] `region` parodo tavo vietovės regionus. `get flood.max.advert` ir
      `get flood.max.unscoped` parodo jos šuolių ribas. Žr.
      [Mažink srautą](/guides/settings/#traffic).
- [ ] Privatųjį raktą iš `get prv.key` išsaugojai saugioje vietoje.
- [ ] `clock` parodo dabartinį laiką pagal UTC.
- [ ] Jei naudoji saulės energiją, `powersaving` parodo `on`.

## Ant stogo {#roof}

- [ ] Anteną prijungei prieš įjungdamas retransliatoriaus maitinimą.
- [ ] Antena stovi vertikaliai stiebo viršuje, atokiau nuo metalo. Žr.
      [Montavimas](/guides/antenna/#mounting).
- [ ] Kiekviena lauko jungtis užsandarinta, o kabelis turi lašų kilpą.
- [ ] Korpusas uždarytas ir turi ventiliacijos arba drenažo angą. Žr.
      [Aparatinė įranga](/repeater-guide/#hardware).

## Prieš išeidamas {#leave}

- [ ] Iš toliau tavo kompanionas programėlėje pasiekia retransliatorių.
- [ ] Išsiuntei `advert`, kad mazgai visame mesh tinkle sužinotų apie retransliatorių.
- [ ] Tavo [vietinė grupė](/community/) žino, kad jis veikia.
