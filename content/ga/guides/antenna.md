---
title: Treoir ar aeróga
lead: Sroicheann an aeróg cheart, agus í gléasta go maith, níos faide ná cumhacht bhreise. Seiceáil an aeróg ar do chompánach, ansin roghnaigh, ceangail agus gléas ceann d'athsheoltóir.
description: 'Roghnaigh agus gléas aeróg MeshCore do 868 MHz: seiceáil aeróg fuipe ar chompánach, cineálacha aeróige agus gnóthachan, nascóirí, caillteanas cábla in aghaidh an mhéadair, scagairí, gléasadh agus an chaoi a n-áirítear gnóthachan i dtreo na teorann dlíthiúla.'
eyebrow: Compánach agus athsheoltóir · 868 MHz
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'f828c4aa'
  seeded: '2026-11-02'
  fields: {title: '3a76cb0e', lead: 'd82ec429', description: 'ce3f3e73', eyebrow: 'd2203a35'}
  sections: ['908e2678', 'f9b96f42', 'ca18da90', 'bcfb40ec', '851afd23', '8b7a2209', 'd8832cfa', '5b70b9e8', '14a38e92', 'a5dc1e34', 'de04ca41', 'a23f19c6', '93846db4']
  blocks: ['908e2678', '0868bca9', '081db416', 'ad1da217', '73844333', 'aa14f1b1', '07e4fbad', '32d64d0d', 'ef66133c', '558c115b', '5d28e314', '57d6e138', 'e9b3d055', 'dd757d4a', '2cbd0b58', '21c67ec0', '306a3ded', 'fa46c89f', '1e6ccb3a', 'a3e53320', '6ae131c0', '98f350c6', '138d049d', '3bd28746', '2fc98ff1', '5ea29ee5', 'cfbd64e1', '48833347', '56a82a5c', '4ef7e883', '711e4fee', '1f7844ed', '6b188411', '8da9aa78', '4c2d8bbc', 'a721a9d0', '69c1dc1a', 'a631dbfa', '3f9f3471', '5af4ae3b', 'fa5095fd', '65eeb436', '15aa0eca', 'a8f5b505', '57f35115', '8e5e4975', '89764d3d']
---

Tugann airde, aeróg thiúnta agus cábla gearr níos mó raoin duit ná aon mhilleavata breise. Tosaíonn an treoir seo leis an gcompánach, an raidió óna seolann tú teachtaireachtaí. Ansin pléann sí an aeróg ar athsheoltóir, nód a chuireann teachtaireachtaí ar aghaidh ó dhíon nó ó chrann.

## Do chompánach {#companion}

{{< callout type="warning" >}}
Ceangail an aeróg sula gcuireann tú an raidió ar siúl. Má tharchuireann raidió LoRa gan aeróg, féadann sé damáiste a dhéanamh dá shlis féin.
{{< /callout >}}

Déanann an aeróg a tháinig le do chlár an gnó. Ceangail í, coinnigh an nód ina sheasamh, agus tosaigh ag seoladh teachtaireachtaí. Is beag a ghnóthaíonn tú le haeróg níos fearr ar chompánach; is mór a ghnóthaíonn tú le hathsheoltóir atá laistigh de raon.

Ná ceannaigh aeróg fuipe ar leith ach amháin má tá an ceann a tháinig leis an gclár briste nó ar iarraidh. Níl gach aeróg fuipe a dhíoltar do 868 MHz tiúnta don mhinicíocht sin. [Seiceáil í le NanoVNA](#nanovna), anailíseoir aeróige póca, sula gcuireann tú muinín inti, nó faigh ceann ar iasacht ó chlár a oibríonn.

Cloiseann nód in aice le tarchuradóir láidir níos lú ná mar ba chóir dó. Coinníonn [scagaire beag SAW (tonn fuaime dromchla)](#filters) idir an raidió agus an aeróg an tarchuradóir sin amach as an nglacadóir. Seiceáil a bhileog sonraí ar dtús:

- **Uaschumhacht ionchuir.** Tá an scagaire ar chonair do tharchurtha féin freisin. Má tharchuireann clár 22 dBm (160 mW) isteach i scagaire atá rátaithe do 15 dBm, briseann sé an scagaire.
- **Pasbhanda.** Caithfidh minicíocht do réamhshocraithe a bheith ann. Ní ligeann scagaire do 868.65 go 869.25 MHz an cainéal EU/UK (Narrow) ar 869.618 MHz tríd.

## Cineálacha aeróige d'athsheoltóir {#types}

Tá gach aeróg ar an mesh ina seasamh. Roghnaigh an cineál de réir na háite ina bhfuil na nóid is mian leat a shroicheadh:

- **Aeróg chomhlíneach snáithín gloine.** Feadán bán ar chrann, le gnóthachan timpeall na léaslíne go léir. Is í an rogha chaighdeánach í d'athsheoltóir a fhreastalaíonn ar bhaile.
- **Dépholl.** Níos giorra, le níos lú gnóthachain agus bíoma ard. Sroicheann sé nóid fút agus os do chionn níos fearr ná aeróg chomhlíneach, mar shampla ó chnoc os cionn gleanna.
- **Yagi.** Búm le heilimintí trasna, dírithe ar áit amháin. Sroicheann sé athsheoltóir amháin i bhfad uait agus is beag eile. Feistigh é leis na heilimintí ina seasamh, mar leanann a pholarú na heilimintí.

## Gnóthachan agus an bíoma {#gain}

Ní thugann gnóthachan cumhacht bhreise. Tógann sé an comhartha a rachadh suas agus síos agus seolann sé feadh na léaslíne é. Is cosúil é le tóirse a dhíríonn tú: an ceallra céanna, bíoma níos faide agus níos cúinge. Léiríonn dépholl agus aeróg chomhlíneach ón déantóir céanna é seo:

| Aeróg | Gnóthachan | Leithead ingearach an bhíoma |
|---|---|---|
| Dépholl (Sirio SO 868-915-2) | 2.2 dBi | 88 céim |
| Aeróg chomhlíneach snáithín gloine (Sirio SPO 868-915-6) | 5.8 dBi | 23 céim |

{{< gain >}}

Gearrann an léaráid tríd an gcrann, agus é le feiceáil ón taobh. Cas í timpeall an chrainn agus tá an bíoma iomlán agat: taoschnó don dépholl, diosca cothrom don aeróg chomhlíneach. Seolann aeróg ina seasamh ar an mbealach céanna i ngach treo thart uirthi. Lasmuigh den bhíoma sa léaráid, ní stopann an comhartha; tá sé níos laige, ach is leor é do nód gar di.

Ar dhíon, is bíoma cothrom atá uait. Ar chnoc i bhfad os cionn na nód, téann bíoma 23 céim thar a gcinn; clúdaíonn dépholl iad. Téann Yagi níos faide leis seo: 16.6 dBi i mbíoma atá 23 céim ar airde agus 25 céim ar leithead (Amphenol Procom 7176870), agus dada ar na taobhanna.

Tomhaistear gnóthachan i gcomparáid le tagairt. Déanann dBi comparáid le haeróg idéalach a sheolann go cothrom i ngach treo. Déanann dBd comparáid le dépholl leathtoinne, a bhfuil 2.15 dBi aige féin: ní sheolann fiú an aeróg is simplí dada díreach suas ná síos. Sroicheann dépholl níos faide, 1.25 tonnfhad, 5.2 dBi. Ina ionad sin, cruachann aeróg chomhlíneach eilimintí leathtoinne os cionn a chéile: dá mhéad a chruachann sí, is ea is airde an gnóthachan. Brúigh an comhartha céanna isteach i leath an spáis agus tá sé dhá oiread chomh láidir ansin: 3 dB. Isteach i gceathrú den spás, 4 huaire chomh láidir: 6 dB. Luann déantóirí gnóthachan in dBi; tomhaistear an teorainn dhlíthiúil in dBd, féach [Laistigh den teorainn dhlíthiúil](#legal).

### An gnóthachan a oireann do do shuíomh {#choose-gain}

- **Cnoic, gleannta nó cathair dhlúth: thart ar 3 dBi.** Sroicheann an bíoma ard nóid os do chionn agus fút, agus timpeall ar na fánaí agus na foirgnimh atá sa bhealach. Oibríonn sé sa treo eile freisin: ó ghleann, téann bíoma cothrom faoi athsheoltóir ar an gcnoc thuas. Sampla is ea an RAKwireless RAKARG12: feadán snáithín gloine 36 cm.
- **Bruachbhailte nó baile le díonta ísle: 5 go 6 dBi.** An aeróg chomhlíneach snáithín gloine chaighdeánach.
- **Talamh cothrom oscailte: 8 go 10 dBi.** Sroicheann an bíoma is cothroime is faide feadh na léaslíne. Nuair a fheistíonn tú go hard é, téann sé thar na nóid in aice láimhe.

Is é an gnóthachan san ainm an figiúr is fearr thar bhanda iomlán na haeróige. Tá 2.8 dBi ag an RAKARG12, a dhíoltar mar 3 dBi, ó 865 go 870 MHz. Léigh an tábla gnóthachain sa bhileog sonraí ag minicíocht do réamhshocraithe.

Os cionn 7 dBi, téann clár 22 dBm thar an teorainn dhlíthiúil, mura gcúitíonn caillteanas cábla agus scagaire an difríocht. Laghdaigh an chumhacht tarchuir dá réir.

Ní chabhraíonn gnóthachan ard ach nuair is eol duit cá bhfuil na nóid: feadh na léaslíne timpeall ar athsheoltóir, nó ag athsheoltóir amháin i bhfad uait do Yagi. Díríonn compánach i do lámh i ngach treo, mar sin is é an gnóthachan íseal a tháinig leis is fearr dó.

## Cén fáth ingearach {#vertical}

Is fearr a chloiseann aeróga a chéile nuair a dhíríonn siad sa treo céanna. Méadaíonn an caillteanas leis an uillinn eatarthu: cailleann tú 3 dB ag 45 céim, leath do chomhartha. Ag 90 céim, aeróg chothrom i gcoinne aeróige ina seasamh, go teoiriciúil ní thagann dada tríd. Tá an mesh ina seasamh, mar sin bíodh d'aeróg ina seasamh freisin. Baineann sé seo le compánach ar dheasc freisin: leag ar a chothrom é agus is lú a chloiseann gach nód timpeall ort.

## Nascóirí {#connectors}

Ordaigh an aeróg leis an nascóir atá ar do chlár. Is cumasc amháin eile le séalú gach cuibheoir, agus cailleann tú tuilleadh comhartha.

- **SMA.** Nascóir snáithithe thart ar 6 mm ar leithead. Tá poll i lár an tsoicéid ar fhormhór na gclár; tá an biorán ar an aeróg. Cailleann nascóir den chineál seo thart ar 0.03 dB ag 868 MHz.
- **RP-SMA.** An corp agus an snáithe céanna le SMA, ach tá an biorán agus an poll malartaithe. Tá cuma SMA air ach ní nascann sé leis. Seiceáil cén ceann atá ar do chlár sula n-ordaíonn tú.
- **U.FL (IPEX).** Soicéad bídeach brú-air ar an gclár féin. Ritheann cábla gearr pigtail uaidh go soicéad SMA sa chás. Tá sé rátaithe do 30 timthriall nasctha, mar sin ceangail é uair amháin agus fág é.
- **N.** An nascóir mór snáithithe ar aeróga snáithín gloine agus ar chábla tiubh. Cailleann sé 0.05 dB ar a mhéad. Teastaíonn ó athsheoltóir cuibheoir nó pigtail amháin ó N go SMA an chláir.

## Caillteanas cábla {#cable}

Cailleann tú comhartha sa chábla sula bhfágann sé an aeróg, sa dá threo. Is ionann 3 dB agus leath do chumhachta. Figiúirí na ndéantóirí in aghaidh an mhéadair, ag 868 go 900 MHz:

| Cábla | Caillteanas in aghaidh an mhéadair | Caillteanas thar 5 m |
|---|---|---|
| RG174 | 1.02 dB | 5.1 dB |
| RG316 | 0.78 dB | 3.9 dB |
| RG58 | 0.45 dB | 2.2 dB |
| H-155 | 0.27 dB | 1.4 dB |
| LMR-240 | 0.25 dB | 1.2 dB |
| Ecoflex 10 | 0.13 dB | 0.7 dB |
| LMR-400 | 0.13 dB | 0.6 dB |

Cailleann 3 mhéadar de RG174, an pigtail tanaí a thagann le go leor clár, leath do chumhachta. Feistigh an clár ag an aeróg le pigtail gearr, nó rith cábla tiubh chuici. Cuir gach cuibheoir agus scagaire ar an gconair san áireamh sa tsuim.

## Scagairí {#filters}

Suíonn scagaire idir an raidió agus an aeróg. Ligeann sé do bhanda tríd agus cuireann sé bac ar an gcuid eile, ionas nach mbáfaidh tarchuradóir láidir in aice láimhe an glacadóir. Teastaíonn ceann uait nuair a chloiseann nód níos lú ná mar ba chóir dó in aice le tarchuradóirí eile. Is nód den sórt sin é athsheoltóir ar chrann a bhfuil stáisiúin bhonn fón póca air. Cailleann tú comhartha i scagaire sa dá threo: áirigh a chaillteanas mar a áiríonn tú caillteanas cábla.

| | Scagaire SAW | Scagaire cuais |
|---|---|---|
| Méid | Roinnt milliméadar, ar chlár beag | Bloc nó feadán miotail |
| Caillteanas scagaire mhaith | faoi 2 dB | faoi 1 dB |
| Uaschumhacht ionchuir scagaire mhaith | 500 mW | roinnt vatanna |

Mar shampla, is scagaire cuais do 863 go 870 MHz é an sysmocom cf866.5-kt30. Cailleann sé 1.0 dB ar a mhéad agus glacann sé le 30 W. Tá sé déanta le húsáid laistigh, mar sin cuir i mbosca séalaithe ar chrann é.

Tá difríochtaí móra idir scagairí, mar sin seiceáil an bhileog sonraí sula gceannaíonn tú. Caithfidh a chumhacht ionchuir rátaithe a bheith níos airde ná do chumhacht tarchuir, agus caithfidh minicíocht do réamhshocraithe a bheith sa phasbhanda.

## Feistiú {#mounting}

- **Os cionn imeall an dín.** Teastaíonn radharc glan ón aeróg i ngach treo a bhfreastalaíonn sí air. Cabhraíonn fiú cúpla méadar os cionn na ndíonta máguaird. Taispeánann [Roghnaigh suíomh](/repeater-guide/#site) i dtreoir an athsheoltóra conas an radharc a sheiceáil.
- **Amach ó mhiotal.** Athraíonn gáitéir, crainn, aeróga eile agus díonta miotail in aice na haeróige a patrún agus a tiúnadh. Feistigh í ar bharr an chrainn, seachas lena thaobh.
- **Ina seasamh.** Úsáid leibhéal uisce; féach [Cén fáth ingearach](#vertical).
- **Lúb sileála.** Lig don chábla crochadh faoin nascóir sula dtéann sé suas nó isteach. Ansin sileann uisce de in ionad rith isteach sa chumasc.
- **Séalaigh gach nascóir atá lasmuigh.** Ardaíonn uisce i nascóir an caillteanas agus creimeann sé an biorán. Séalaigh é i gcoinne na báistí agus seiceáil an séala gach bliain.
- **Tintreach.** Is sprioc í aeróg ar dhíon. Lasann gabhálaí sceite gáis sa chábla le linn borrtha agus seolann sé an borradh chun talún. Lean [Crua-earraí](/repeater-guide/#hardware) i dtreoir an athsheoltóra agus do rialacha áitiúla maidir le talmhú.

## Laistigh den teorainn dhlíthiúil {#legal}

{{< callout type="legal" verified="2026-10-22" >}}
San Eoraip, úsáideann MeshCore an fo-bhanda 869.40-869.65 MHz, le **500 mW** de chumhacht éifeachtach radaithe (e.r.p.) ar a mhéad. Áiríonn an teorainn an méid a fhágann an aeróg: cuireann gnóthachan aeróige leis, agus baineann caillteanas cábla agus scagaire de. Áirítear gnóthachan in dBi 2.15 dB níos ísle, mar tomhaistear an teorainn i gcomparáid le dépholl.
{{< /callout >}}

Fanann aeróg chomhlíneach 5.8 dBi ar chlár 22 dBm laistigh den teorainn. Ní fhanann an aeróg chéanna laistigh di ar chlár le haimplitheoir, go dtí go laghdóidh tú an chumhacht tarchuir. Tá an tsuim agus 2 shampla oibrithe in [Cumhacht: e.r.p. agus d'aeróg](/repeater-guide/#erp) i dtreoir an athsheoltóra.

## Seiceáil aeróg le NanoVNA {#nanovna}

Is anailíseoir líonra veicteoirí méid póca é NanoVNA. Taispeánann sé an mhinicíocht ar a bhfuil aeróg tiúnta, ionas go mbeidh a fhios agat sula bhfeistíonn tú í. Tomhaiseann an NanoVNA-H suas go 1.5 GHz, rud a chlúdaíonn 868 MHz.

1. Calabraigh é do 800 go 950 MHz leis na píosaí open, short agus load óna thacar.
2. Ceangail an aeróg tríd an gcuibheoir a úsáidfidh sí ar an nód. Coinnigh ina seasamh í, amach ó do chorp agus ón mbord.
3. Léigh cuar SWR (cóimheas tonnta seasta): taispeánann sé an méid comhartha a sheolann an aeróg ar ais. Caithfidh an t-ísliú a bheith ar mhinicíocht do réamhshocraithe, 869.618 MHz do EU/UK (Narrow). Má tá an t-ísliú na céadta MHz ar shiúl, tá an aeróg déanta do bhanda eile.

Is ionann ceathrú toinne ag 868 MHz agus 86 mm (is é 345 mm an tonnfhad). Ní insíonn fad amháin an banda duit, mar fillann agus lódálann déantóirí aeróga fuipe; insíonn an NanoVNA duit é.

## Foinsí {#sources}

- Caillteanas cábla: [Belden 8216 (RG174)](https://catalog.belden.com/techdata/en/8216_techdata.pdf),
  bileog sonraí Huber+Suhner RG316,
  [Belden 8240 (RG58)](https://catalog.belden.com/techdata/en/8240_techdata.pdf),
  [SSB H-155](https://www.ssb.de/media/h155ssb-en.pdf),
  bileoga sonraí Times Microwave LMR-240 agus LMR-400,
  [SSB Ecoflex 10](https://www.rigpix.com/otherusefulinfo/coax/ecoflex10.pdf).
- Aeróga: [Sirio SPO 868-915-6](https://rigpix.com/antennas/sirio_spo8689156_manual.pdf),
  bileog sonraí Sirio SO 868-915-2,
  [Amphenol Procom 7176870](https://amphenolprocom.com/products/base-station-antennas/2236-7176870),
  [RAKwireless RAKARG12](https://docs.rakwireless.com/product-categories/accessories/rakarg12/datasheet/).
- Gnóthachan mar chomhartha brúite isteach i spás níos lú: [RF Cafe, réamhrá ar aeróga](https://www.rfcafe.com/references/electrical/ew-radar-handbook/antenna-introduction-basics.htm).
- Nascóirí: bileoga sonraí Rosenberger 32S102 (SMA) agus 53S101 (N), catalóg Hirose U.FL.
- Scagairí: leathanach táirge sysmocom cf866.5-kt30,
  [gabhálaithe sceite gáis Citel](https://citel.us/en/gas-tube-surge-arrestors-for-coaxial-line-protection).
- Caillteanas polaraithe: [Ollscoil Toronto, éifeachtaí Friis](https://www.waves.utoronto.ca/prof/svhum/ece422/notes/12-friiseffects.pdf).
- Gnóthachan dépholl de réir faid: [Wikipedia, Dipole antenna](https://en.wikipedia.org/wiki/Dipole_antenna).
- Tonnfhad: luas an tsolais ó [NIST](https://physics.nist.gov/cgi-bin/cuu/Value?c).
- NanoVNA: [NanoVNA-H](https://github.com/hugen79/NanoVNA-H).
- Teorainn dhlíthiúil: [CEPT ERC Recommendation 70-03](https://docdb.cept.org/document/845),
  Iarscríbhinn 1, banda h1.7; liostaíonn [treoir an athsheoltóra](/repeater-guide/#legal) an chuid eile.
