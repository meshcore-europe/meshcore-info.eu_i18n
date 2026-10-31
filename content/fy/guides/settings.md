---
title: Oanrikkemandearre ynstellingen
layout: settings
lead: It radiopreset dat dyn gebiet brûkt, en de ynstellingen dy't dyn buorlju feroare hawwe. Kies dyn lân, stel it preset yn en kopiearje de kommando's.
description: It MeshCore-radiopreset per gebiet yn Europa, en de repeater- en companionynstellingen dy't pleatslike groepen oanpast hawwe, mei de kommando's.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '0876215b'
  seeded: '2026-10-31'
  fields: {title: 'cfb32983', lead: 'f3f16725', description: 'cb15acd3'}
  sections: ['39848942', 'd1606fcd']
  blocks: ['8c9e88ea', '50ac6063', '85c2203d', '15f91217', 'bdf5fa4e', '69d8e70b', '28f83120', 'fe27027b']
---

Elk gebiet hjirûnder hat in eigen radiopreset, of feroaret in pear standertynstellingen fan MeshCore.
Alles wat hjir net stiet, bliuwt op de standertwearde. Do feroarest dus allinnich wat
dyn gebiet feroare hat. In repeater stjoert berjochten troch foar elkenien. In companion is
de node dêr'tst dyn berjochten mei ferstjoerst. Do keppelest him oer Bluetooth of USB oan dyn tillefoan of laptop,
of hy hat in eigen skerm.

Yn de [repeaterhantlieding](/repeater-guide/#config) lêst do hoe'tst by de kommandorigel fan dyn
repeater komst. Yn de [seriële konsole](/firmware/console/) op dizze side typest do sels kommando's.
Under elk gebiet kinst do de ynstellingen ek oer USB ferstjoere. De hantlieding neamt ek de [wetlike grinzen](/repeater-guide/#legal)
foar 868 MHz.

## Hâld it ferkear leech {#traffic}

Dizze ynstellingen jilde foar elk gebiet. Elke repeater stjoert elk floodberjocht troch dat er heart.
Ien berjocht fan dy kostet ien útstjoering, plus ien foar
elke repeater dy't it heart. Mei de 10% duty cycle kin in repeater
sa'n 680 pakketten yn it oere stjoere. Elkenien om him hinne dielt dat oantal.
In berjocht dat fierder giet as nedich, brûkt dêr in part fan op.

**Stjoer nei de lytste regio dy't de minsken berikt dêr'tst nei skriuwst.**
Regio's sitte yn inoar: in lân, in provinsje, in pleatslike groep, elk mei in eigen koade,
lykas `nl`, `nl-ov` en `nl-ov-zwo`. In berjocht foar `nl-ov-zwo` bliuwt by
de repeaters yn dy groep. In repeater stjoert allinnich de regio's troch dy't er sels hat.
Hat er `nl`, dan stjoert er `nl-ov` noch net troch. Set elke repeater yn elke regio dy't er betsjinnet, en allinnich yn dy regio's.
Dyn [pleatslike groep](/community/) wit hokker regio's dat binne.

**Beheine wat dyn repeater trochstjoert.** Mei twa ynstellingen hâldst do ferkear dat net fier hoecht
tichtby hûs:

```text
set flood.max.advert 3
set flood.max.unscoped 1
```

- `flood.max.advert 3`: adverts, dy't in node oan it mesh bekend meitsje, geane
  maksimaal 3 hops.
- `flood.max.unscoped 1`: in berjocht sûnder regio komt by maksimaal ien
  repeater lâns.
