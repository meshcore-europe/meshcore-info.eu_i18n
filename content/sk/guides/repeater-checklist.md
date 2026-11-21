---
title: Kontrolný zoznam pre repeater
lead: Skontroluj svoj repeater, kým ho namontuješ. Každý riadok uvádza, čo skontrolovať, ktorý príkaz to ukáže a ktorý návod to vysvetľuje.
description: 'Kontrolný zoznam pre MeshCore repeater pred montážou na strechu alebo stožiar: čo skontrolovať cez USB, ako ho namontovať a aký test urobiť pred odchodom.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '5bbc2cbe'
  seeded: '2026-11-21'
  fields: {title: 'e982ea2f', lead: '664a2839', description: '01f56863'}
  sections: ['d512dacf', '4d357087', '75706984', '8a484df5', '33fd8c68']
  blocks: ['d512dacf', 'a7ba4c46', '6a427551', '2f0a8827', '2bda1638', '589c7b4f', '5fedefb7', 'e12f330e', 'd6d0b21c']
---

K repeateru na streche sa ťažko dostaneš, preto ho skontroluj, kým ho máš ešte
na stole. [Návod na repeater](/repeater-guide/) vysvetľuje každý krok. Hodnoty,
napríklad predvoľbu a limity hopov, nájdeš v
[nastaveniach pre tvoju oblasť](/guides/settings/). Príkazy zadávaj cez USB,
napríklad v [sériovej konzole](/firmware/console/). Tento zoznam vychádza
z firmvéru MeshCore v1.18.0.

## Skôr než začneš {#start}

- [ ] Podľa [máp pokrytia](/map/) alebo tvojej [miestnej skupiny](/community/)
      oblasť potrebuje repeater. Pozri [Potrebuješ ho?](/repeater-guide/#need)
- [ ] Vlastník miesta súhlasil a k repeateru sa dostaneš kvôli údržbe.
- [ ] Batériu a panel máš dimenzované na najhorší zimný mesiac. Pozri
      [Napájanie a dimenzovanie solárneho panelu](/repeater-guide/#power).

## Na stole, cez USB {#usb}

- [ ] Na doske beží firmvér **Repeater**: `ver` ukáže jeho verziu. Pozri
      [Nastavenie](/repeater-guide/#config).
- [ ] Na doske nRF52 obsahuje odpoveď na `get bootloader.ver` reťazec `OTAFIX`.
      Pozri [Aktualizácia vzduchom](/repeater-guide/#update).
- [ ] `get radio` ukáže predvoľbu tvojej oblasti.
- [ ] `get dutycycle` ukáže 10. Pozri [Duty cycle](/repeater-guide/#duty-cycle).
- [ ] Hodnota `get tx` spolu so ziskom tvojej antény neprekročí 500 mW e.r.p.
      Pozri [Výkon: e.r.p. a tvoja anténa](/repeater-guide/#erp).
- [ ] Heslo správcu už nie je `password`.
- [ ] `get guest.password` ukáže heslo.
- [ ] `get name` ukáže názov, aký tvoja miestna skupina dáva svojim repeaterom.
- [ ] `get lat` a `get lon` ukážu polohu miesta.
- [ ] `get owner.info` ukáže, ako ťa ostatní prevádzkovatelia zastihnú.
- [ ] `region` ukáže regióny tvojej oblasti. `get flood.max.advert` a
      `get flood.max.unscoped` ukážu jej limity hopov. Pozri
      [Obmedz prevádzku](/guides/settings/#traffic).
- [ ] Súkromný kľúč z `get prv.key` máš uložený na bezpečnom mieste.
- [ ] `clock` ukáže aktuálny čas v UTC.
- [ ] Pri solárnom napájaní ukáže `powersaving` hodnotu `on`.

## Na streche {#roof}

- [ ] Anténa je pripojená skôr, než repeater dostane napájanie.
- [ ] Anténa stojí zvisle na vrchole stožiara, ďaleko od kovu. Pozri
      [Montáž](/guides/antenna/#mounting).
- [ ] Každý vonkajší konektor je utesnený a kábel má odkvapovú slučku.
- [ ] Krabička je zatvorená a má vetrací alebo odtokový otvor. Pozri
      [Hardvér](/repeater-guide/#hardware).

## Pred odchodom {#leave}

- [ ] Z diaľky sa tvoj companion v aplikácii spojí s repeaterom.
- [ ] Poslal si `advert`, aby sa uzly v celej mesh sieti dozvedeli o repeateri.
- [ ] Tvoja [miestna skupina](/community/) vie, že repeater je v prevádzke.
