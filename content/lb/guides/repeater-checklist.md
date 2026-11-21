---
title: Checklëscht fir de Repeater
lead: Kontrolléier däi Repeater, ier en eropgeet. All Linn seet, wat s du kontrolléiers, wéi e Kommando et weist a wéi e Guide et erkläert.
description: 'Eng Checklëscht fir e MeshCore-Repeater, ier en op en Daach oder e Mast kënnt: wat s du iwwer USB kontrolléiers, wéi s du en montéiers an den Test, ier s du fortgees.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '5bbc2cbe'
  seeded: '2026-11-21'
  fields: {title: 'e982ea2f', lead: '664a2839', description: '01f56863'}
  sections: ['d512dacf', '4d357087', '75706984', '8a484df5', '33fd8c68']
  blocks: ['d512dacf', 'a7ba4c46', '6a427551', '2f0a8827', '2bda1638', '589c7b4f', '5fedefb7', 'e12f330e', 'd6d0b21c']
---

Op engem Daach kënns du schwéier un e Repeater. Kontrolléier en dofir, soulaang
en nach op dengem Schreifdësch läit. De [Repeater-Guide](/repeater-guide/)
erkläert all Schrëtt. D'Wäerter, wéi de Preset an d'Hop-Limitten, fënns du an
den [Astellunge fir deng Géigend](/guides/settings/). Tipp d'Kommandoen iwwer
USB an, zum Beispill an der [serieller Konsol](/firmware/console/). Dës Lëscht
baséiert op der MeshCore-Firmware v1.18.0.

## Ier s de ufänks {#start}

- [ ] D'[Ofdeckungskaarten](/map/) oder deng [lokal Grupp](/community/) soen,
      datt d'Géigend e Repeater brauch. Kuck [Brauchs du een?](/repeater-guide/#need)
- [ ] De Besëtzer vum Standuert ass d'accord, an du kënns fir d'Wartung un de
      Repeater.
- [ ] Batterie a Solarpanneau si fir de schlëmmste Wantermount dimensionéiert.
      Kuck [Stroum a Solar dimensionéieren](/repeater-guide/#power).

## Um Schreifdësch, iwwer USB {#usb}

- [ ] Um Board leeft d'**Repeater**-Firmware: `ver` weist hir Versioun.
      Kuck [Ariichten](/repeater-guide/#config).
- [ ] Op engem nRF52-Board steet `OTAFIX` an der Äntwert op
      `get bootloader.ver`. Kuck [Iwwer d'Loft updaten](/repeater-guide/#update).
- [ ] `get radio` weist de Preset vun denger Géigend.
- [ ] `get dutycycle` weist 10. Kuck [Duty cycle](/repeater-guide/#duty-cycle).
- [ ] `get tx` plus de Gewënn vun denger Antenn bleift bannent 500 mW e.r.p.
      Kuck [Leeschtung: e.r.p. an deng Antenn](/repeater-guide/#erp).
- [ ] D'Admin-Passwuert ass net méi `password`.
- [ ] `get guest.password` weist e Passwuert.
- [ ] `get name` weist den Numm, deen deng lokal Grupp fir hir Repeater benotzt.
- [ ] `get lat` a `get lon` weisen d'Positioun vum Standuert.
- [ ] `get owner.info` weist, wéi aner Operateuren dech erreechen.
- [ ] `region` weist d'Regioune vun denger Géigend. `get flood.max.advert` an
      `get flood.max.unscoped` weisen hir Hop-Limitten. Kuck
      [Den Traffic niddreg halen](/guides/settings/#traffic).
- [ ] Du hues de private Schlëssel aus `get prv.key` op enger sécherer Plaz
      gespäichert.
- [ ] `clock` weist déi aktuell Zäit, an UTC.
- [ ] Bei Solarbetrib weist `powersaving` de Wäert `on`.

## Um Daach {#roof}

- [ ] D'Antenn ass ugeschloss, ier de Repeater Stroum kritt.
- [ ] D'Antenn steet riicht uewen um Mast, wäit vu Metall. Kuck
      [Montage](/guides/antenna/#mounting).
- [ ] All Stecker dobaussen ass ofgedicht, an de Kabel huet eng Drëpsschleif.
- [ ] D'Gehäis ass zou, mat engem Lëftungs- oder Oflafslach. Kuck
      [Hardware](/repeater-guide/#hardware).

## Ier s de fortgees {#leave}

- [ ] Vu wäitem erreechs du de Repeater mat dengem Companion an der App.
- [ ] Du hues `advert` geschéckt, sou datt Noden am ganze Mesh de Repeater
      kennen léieren.
- [ ] Deng [lokal Grupp](/community/) weess, datt en a Betrib ass.
