---
title: Átjátszó-ellenőrzőlista
lead: Ellenőrizd az átjátszódat, mielőtt felszereled. Minden sor megadja, mit kell ellenőrizni, melyik parancs mutatja meg, és melyik útmutató magyarázza el.
description: 'Ellenőrzőlista egy MeshCore átjátszóhoz, mielőtt tetőre vagy árbocra kerül: mit ellenőrizz USB-n, hogyan szereld fel, és mit tesztelj, mielőtt elmész.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '5bbc2cbe'
  seeded: '2026-11-21'
  fields: {title: 'e982ea2f', lead: '664a2839', description: '01f56863'}
  sections: ['d512dacf', '4d357087', '75706984', '8a484df5', '33fd8c68']
  blocks: ['d512dacf', 'a7ba4c46', '6a427551', '2f0a8827', '2bda1638', '589c7b4f', '5fedefb7', 'e12f330e', 'd6d0b21c']
---

A tetőn lévő átjátszót nehéz elérni, ezért ellenőrizd, amíg még az asztalodon
van. Az [átjátszó-útmutató](/repeater-guide/) minden lépést elmagyaráz. Az
értékeket, például az előbeállítást és az ugráskorlátokat, a
[környéked beállításai](/guides/settings/) adják meg. A parancsokat USB-n
keresztül írd be, például a [soros konzolban](/firmware/console/). Ez a lista a
MeshCore firmware v1.18.0-s verzióját követi.

## Mielőtt belekezdesz {#start}

- [ ] A [lefedettségi térképek](/map/) vagy a [helyi csoportod](/community/)
      szerint a környéknek szüksége van egy átjátszóra. Lásd:
      [Kell egyáltalán?](/repeater-guide/#need)
- [ ] A helyszín tulajdonosa beleegyezett, és karbantartáshoz hozzáférsz az
      átjátszóhoz.
- [ ] Az akkumulátort és a napelemet a legrosszabb téli hónapra méretezted.
      Lásd: [Tápellátás és napelem méretezése](/repeater-guide/#power).

## Az asztalnál, USB-n keresztül {#usb}

- [ ] A panelen a **Repeater** firmware fut: a `ver` megmutatja a verzióját.
      Lásd: [Beállítás](/repeater-guide/#config).
- [ ] nRF52-es panelen a `get bootloader.ver` válaszában szerepel az `OTAFIX`.
      Lásd: [Frissítés rádión keresztül](/repeater-guide/#update).
- [ ] A `get radio` a környéked előbeállítását mutatja.
- [ ] A `get dutycycle` 10-et mutat. Lásd:
      [Kitöltési tényező](/repeater-guide/#duty-cycle).
- [ ] A `get tx` értéke az antennád nyereségével együtt legfeljebb 500 mW
      e.r.p. Lásd: [Teljesítmény: e.r.p. és az antennád](/repeater-guide/#erp).
- [ ] Az admin jelszó már nem `password`.
- [ ] A `get guest.password` mutat egy jelszót.
- [ ] A `get name` azt a nevet mutatja, amelyet a helyi csoportod az
      átjátszóihoz használ.
- [ ] A `get lat` és a `get lon` a helyszín pozícióját mutatja.
- [ ] A `get owner.info` megmutatja, hogyan érnek el téged más üzemeltetők.
- [ ] A `region` a környéked régióit mutatja. A `get flood.max.advert` és a
      `get flood.max.unscoped` a környék ugráskorlátait mutatja. Lásd:
      [Tartsd alacsonyan a forgalmat](/guides/settings/#traffic).
- [ ] A `get prv.key` által mutatott privát kulcsot biztonságos helyre
      mentetted.
- [ ] A `clock` az aktuális időt mutatja, UTC-ben.
- [ ] Napelemes üzemnél a `powersaving` értéke `on`.

## A tetőn {#roof}

- [ ] Az antenna már csatlakoztatva van, mielőtt az átjátszó áramot kap.
- [ ] Az antenna függőlegesen áll az árboc tetején, fémtől távol. Lásd:
      [Felszerelés](/guides/antenna/#mounting).
- [ ] Minden kültéri csatlakozó tömítve van, és a kábelen van csepegési hurok.
- [ ] A ház zárva van, és van rajta szellőző vagy vízelvezető nyílás. Lásd:
      [Hardver](/repeater-guide/#hardware).

## Mielőtt elmész {#leave}

- [ ] Távolabbról a companionöddel eléred az átjátszót az appban.
- [ ] Elküldted az `advert` parancsot, így a csomópontok az egész mesh-ben
      megismerik az átjátszót.
- [ ] A [helyi csoportod](/community/) tud róla, hogy működik.
