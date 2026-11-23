---
title: Kontrolní seznam pro repeater
lead: Zkontroluj svůj repeater, než ho umístíš nahoru. U každé položky najdeš, co zkontrolovat, jaký příkaz to ukáže a který návod to vysvětluje.
description: 'Kontrolní seznam pro MeshCore repeater před montáží na střechu nebo stožár: co zkontrolovat přes USB, jak ho namontovat a jaký test udělat před odchodem.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '5bbc2cbe'
  seeded: '2026-11-21'
  fields: {title: 'e982ea2f', lead: '664a2839', description: '01f56863'}
  sections: ['d512dacf', '4d357087', '75706984', '8a484df5', '33fd8c68']
  blocks: ['d512dacf', 'a7ba4c46', '6a427551', '2f0a8827', '2bda1638', '589c7b4f', '5fedefb7', 'e12f330e', 'd6d0b21c']
---

Na repeater na střeše se špatně dostaneš, takže ho zkontroluj, dokud ještě leží na
stole. Každý krok vysvětluje [návod k repeateru](/repeater-guide/). Hodnoty,
jako jsou předvolba a limity skoků, najdeš v [nastavení pro tvou
oblast](/guides/settings/). Příkazy zadávej přes USB, třeba v [sériové
konzoli](/firmware/console/). Seznam odpovídá firmwaru MeshCore v1.18.0.

## Než začneš {#start}

- [ ] Podle [map pokrytí](/map/) nebo tvé [místní skupiny](/community/)
      oblast repeater potřebuje. Viz [Potřebuješ ho?](/repeater-guide/#need)
- [ ] Vlastník místa souhlasil a k repeateru se dostaneš kvůli údržbě.
- [ ] Baterii a panel máš dimenzované na nejhorší zimní měsíc. Viz
      [Dimenzování napájení a solárního panelu](/repeater-guide/#power).

## U stolu, přes USB {#usb}

- [ ] Na desce běží firmware **Repeater**: `ver` ukáže jeho verzi. Viz
      [Nastavení](/repeater-guide/#config).
- [ ] Na desce nRF52 obsahuje odpověď na `get bootloader.ver` text `OTAFIX`.
      Viz [Aktualizace vzduchem](/repeater-guide/#update).
- [ ] `get radio` ukáže předvolbu tvé oblasti.
- [ ] `get dutycycle` ukáže 10. Viz [Střída vysílání](/repeater-guide/#duty-cycle).
- [ ] `get tx` spolu se ziskem tvé antény nepřekročí 500 mW e.r.p. Viz
      [Výkon: e.r.p. a tvoje anténa](/repeater-guide/#erp).
- [ ] Heslo správce už není `password`.
- [ ] `get guest.password` ukáže heslo.
- [ ] `get name` ukáže jméno, které tvoje místní skupina používá pro své
      repeatery.
- [ ] `get lat` a `get lon` ukážou polohu místa.
- [ ] `get owner.info` ukáže, jak se s tebou ostatní provozovatelé spojí.
- [ ] `region` ukáže regiony tvé oblasti. `get flood.max.advert` a
      `get flood.max.unscoped` ukážou její limity skoků. Viz
      [Omez provoz](/guides/settings/#traffic).
- [ ] Soukromý klíč z `get prv.key` máš uložený na bezpečném místě.
- [ ] `clock` ukáže aktuální čas v UTC.
- [ ] Při solárním napájení ukáže `powersaving` hodnotu `on`.

## Na střeše {#roof}

- [ ] Anténa je připojená dřív, než repeater dostane napájení.
- [ ] Anténa stojí svisle na vrcholu stožáru, daleko od kovu. Viz
      [Montáž](/guides/antenna/#mounting).
- [ ] Každý venkovní konektor je utěsněný a kabel má odkapávací smyčku.
- [ ] Krabička je zavřená a má větrací nebo odtokový otvor. Viz
      [Hardware](/repeater-guide/#hardware).

## Než odejdeš {#leave}

- [ ] Z dálky se tvůj companion v aplikaci spojí s repeaterem.
- [ ] Poslal jsi `advert`, aby se o repeateru dozvěděly uzly v celé mesh síti.
- [ ] Tvoje [místní skupina](/community/) ví, že repeater běží.
