---
title: Gosodiadau a argymhellir
layout: settings
lead: Y rhagosodiad radio mae dy ardal yn ei ddefnyddio, a'r gosodiadau a newidiodd dy gymdogion. Dewisa dy wlad, gosoda'r rhagosodiad a chopïa'r gorchmynion.
description: Y rhagosodiad radio MeshCore fesul ardal yn Ewrop, a'r gosodiadau ailadroddydd a companion a newidiodd grwpiau lleol o'r gwerthoedd diofyn, gyda'r gorchmynion.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '0876215b'
  seeded: '2026-11-02'
  fields: {title: 'cfb32983', lead: 'f3f16725', description: 'cb15acd3'}
  sections: ['39848942', 'd1606fcd']
  blocks: ['8c9e88ea', '50ac6063', '85c2203d', '15f91217', 'bdf5fa4e', '69d8e70b', '28f83120', 'fe27027b']
---

Mae pob ardal isod yn defnyddio ei rhagosodiad radio ei hun, neu'n newid rhai o
werthoedd diofyn MeshCore. Mae popeth sydd heb ei restru yn aros ar y gwerth
diofyn, felly dim ond yr hyn a newidiodd dy ardal di sydd angen i ti ei newid.
Mae ailadroddydd (repeater) yn anfon negeseuon ymlaen i bawb; companion yw'r nod
rwyt ti'n anfon negeseuon ohono, wedi'i baru â dy ffôn neu dy liniadur dros
Bluetooth neu USB, neu gyda'i sgrin ei hun.

Mae'r [canllaw ailadroddydd](/repeater-guide/#config) yn dangos sut i gyrraedd
llinell orchymyn dy ailadroddydd, ac yn y [consol cyfresol](/firmware/console/)
ar y wefan hon rwyt ti'n teipio gorchmynion dy hun. O dan bob ardal, gelli di
hefyd anfon ei gosodiadau dros USB. Mae'r canllaw hefyd yn rhestru'r
[terfynau cyfreithiol](/repeater-guide/#legal) ar 868 MHz.

## Cadw'r traffig yn isel {#traffic}

Mae'r gosodiadau hyn yn berthnasol i bob ardal. Mae pob ailadroddydd yn anfon
pob neges flood mae'n ei chlywed ymlaen. Mae un neges gen ti yn costio un
trosglwyddiad, ac un arall am bob ailadroddydd sy'n ei chlywed. Dan y cylch
dyletswydd o 10%, gall ailadroddydd anfon tua 680 pecyn yr awr, ac mae pawb o'i
gwmpas yn rhannu'r nifer hwnnw. Mae neges sy'n teithio'n bellach nag sydd angen
yn defnyddio rhan ohono.

**Anfona at y rhanbarth lleiaf sy'n cyrraedd y bobl rwyt ti'n ysgrifennu atyn nhw.**
Mae rhanbarthau'n ffitio o fewn ei gilydd: gwlad, talaith, grŵp lleol, pob un â'i
god ei hun, fel `nl`, `nl-ov` a `nl-ov-zwo`. Mae neges i `nl-ov-zwo` yn aros gyda'r
ailadroddyddion yn y grŵp hwnnw. Dim ond y rhanbarthau sydd ganddo ei hun mae
ailadroddydd yn eu hanfon ymlaen: dydy cael `nl` ddim yn golygu ei fod yn anfon
`nl-ov` ymlaen. Rho bob ailadroddydd ym mhob rhanbarth mae'n ei wasanaethu, a
dim ond y rheini; mae dy [grŵp lleol](/community/) yn gwybod pa rai ydyn nhw.

**Cyfynga ar yr hyn mae dy ailadroddydd yn ei anfon ymlaen.** Mae dau osodiad yn
cadw traffig nad oes angen iddo deithio'n bell yn agos i adref:

```text
set flood.max.advert 3
set flood.max.unscoped 1
```

- `flood.max.advert 3`: mae hysbysiadau (adverts), sy'n cyhoeddi nod i'r rhwyll,
  yn teithio 3 naid ar y mwyaf.
- `flood.max.unscoped 1`: mae neges heb ranbarth yn mynd drwy un ailadroddydd ar
  y mwyaf.
