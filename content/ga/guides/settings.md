---
title: Socruithe molta
layout: settings
lead: An réamhshocrú raidió a úsáideann do cheantar, agus na socruithe a d'athraigh do chomharsana. Roghnaigh do thír, socraigh an réamhshocrú agus cóipeáil na horduithe.
description: An réamhshocrú raidió MeshCore do gach ceantar san Eoraip, agus na socruithe athsheoltóra agus compánaigh a d'athraigh grúpaí áitiúla ó na luachanna caighdeánacha, mar aon leis na horduithe.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '0876215b'
  seeded: '2026-11-02'
  fields: {title: 'cfb32983', lead: 'f3f16725', description: 'cb15acd3'}
  sections: ['39848942', 'd1606fcd']
  blocks: ['8c9e88ea', '50ac6063', '85c2203d', '15f91217', 'bdf5fa4e', '69d8e70b', '28f83120', 'fe27027b']
---

Úsáideann gach ceantar thíos a réamhshocrú raidió féin, nó athraíonn sé cúpla
ceann de luachanna caighdeánacha MeshCore. Fanann gach rud nach bhfuil liostaithe
ar an luach caighdeánach, mar sin ní athraíonn tú ach an méid a d'athraigh do cheantar.
Cuireann athsheoltóir (repeater) teachtaireachtaí ar aghaidh do chách; is é an
compánach (companion) an nód a seolann tú teachtaireachtaí uaidh, péireáilte le
do ghuthán nó do ríomhaire glúine thar Bluetooth nó USB, nó lena scáileán féin.

Taispeánann an [treoir athsheoltóra](/repeater-guide/#config) conas teacht ar líne
na n-orduithe ar d'athsheoltóir, agus clóscríobhann tú na horduithe tú féin sa
[chonsól sraitheach](/firmware/console/) ar an suíomh seo. Faoi gach ceantar, is
féidir leat a shocruithe a sheoladh thar USB freisin. Liostaíonn an treoir freisin
na [teorainneacha dlíthiúla](/repeater-guide/#legal) ar 868 MHz.

## Coinnigh an trácht íseal {#traffic}

Baineann na socruithe seo le gach ceantar. Cuireann gach athsheoltóir gach
teachtaireacht thuilte (flood) a chloiseann sé ar aghaidh. Cosnaíonn teachtaireacht
amháin uait tarchur amháin, móide ceann do gach athsheoltóir a chloiseann í. Faoin
timthriall dleachta de 10% is féidir le hathsheoltóir thart ar 680 paicéad a sheoladh
in aghaidh na huaire, agus roinneann gach duine timpeall air an líon sin. Úsáideann
teachtaireacht a thaistealaíonn níos faide ná mar is gá cuid de.

**Seol chuig an réigiún is lú a shroicheann na daoine a scríobhann tú chucu.**
Luíonn réigiúin taobh istigh dá chéile: tír, cúige, grúpa áitiúil, agus a chód
féin ag gach ceann, mar shampla `nl`, `nl-ov` agus `nl-ov-zwo`. Fanann teachtaireacht
do `nl-ov-zwo` i measc na n-athsheoltóirí sa ghrúpa sin. Ní chuireann athsheoltóir
ar aghaidh ach na réigiúin atá aige féin: ní leor `nl` a bheith aige chun `nl-ov` a
chur ar aghaidh. Cuir gach athsheoltóir i ngach réigiún a bhfreastalaíonn sé air,
agus sna réigiúin sin amháin; tá a fhios ag do [ghrúpa áitiúil](/community/)
cé na cinn iad.

**Cuir teorainn leis an méid a chuireann d'athsheoltóir ar aghaidh.** Coinníonn dhá
shocrú an trácht nach gá dó taisteal i bhfad gar don bhaile:

```text
set flood.max.advert 3
set flood.max.unscoped 1
```

- `flood.max.advert 3`: taistealaíonn fógraí (adverts), a fhógraíonn nód don
  mhesh, 3 léim ar a mhéad.
- `flood.max.unscoped 1`: téann teachtaireacht gan réigiún trí athsheoltóir amháin
  ar a mhéad.
