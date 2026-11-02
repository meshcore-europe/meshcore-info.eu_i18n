---
title: Treoir don athsheoltóir
lead: Cuireann athsheoltóir atá suite go hard teachtaireachtaí ar aghaidh do gach duine timpeall air, ar fud baile nó gleanna iomláin. Roghnaigh suíomh, faigh an chumhacht ón ngrian, socraigh é agus fan laistigh den dlí.
description: 'Pleanáil, cumhachtaigh, cumraigh agus oibrigh athsheoltóir MeshCore go dleathach san Eoraip: rogha suímh, méid an chórais ghréine, socruithe CLI, teorainneacha cumhachta agus timthrialla dleachta ar 868 MHz.'
eyebrow: 868 MHz · suas le 500 mW · gan cheadúnas
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '7c7e3be3'
  seeded: '2026-11-02'
  fields: {title: '4608abcd', lead: 'bc670c65', description: '9e483ce5', eyebrow: '9fd33416'}
  sections: ['05ee477a', '938c518c', '766086be', '70faf508', '8bc641aa', '399cd683', 'e9dedb7b', '92beca03', '17634750', 'cadf6024', 'e9cc6834', '2e6e59ca', 'fb44b8db']
  blocks: ['20ac0371', 'ed2b1adf', '432543ee', '7af42c89', 'd0f7543a', '9ef3580f', '3476aef7', '1bab7bec', '6a7c4493', 'dbd9fa1f', 'aa06d32b', '9958aad3', 'd162b028', 'cca1bbdf', '64ef011d', 'e7f16724', 'd2e34ff0', 'bb195cfc', '8d080bb3', '2b1d995b', '210f1b66', 'dc7419d2', 'bdc66db0', 'b59f248c', '7184bd63', 'de5a24f9', 'f5cfb426', '48c7422f', '9d3c0836', 'da8a6af3', '240126df', '8aac2b33', '81a475b8', 'a53e42b5', '36ff1db4', 'e4ca8602', 'e4594afd', '3b24b8e9', '58330858', '68f2966e', 'd7418228', '23536e60', 'cbc5c2d1', '2ea02ba9', '92540256', '6e21f681', 'a8c12311', '3382ae7f', 'cdeafb0f', '1b1319d2']
---

Is ar athsheoltóirí atá an mogalra ina sheasamh. Ní chuireann compánaigh, na raidiónna óna
seolann tú teachtaireachtaí, aon teachtaireacht ar aghaidh. Gan athsheoltóirí, ní shroicheann tú
ach na daoine atá i raon díreach. Leathnaíonn athsheoltóir san áit cheart an mogalra do gach duine
timpeall air. Tá an treoir seo bunaithe ar dhochtearraí MeshCore v1.18.0.

Sula dtosaíonn tú, labhair le do [ghrúpa áitiúil](/community/). Tá a fhios acu cá bhfuil an clúdach
in easnamh, [cén réamhshocrú a úsáideann do cheantar](/guides/settings/) agus conas athsheoltóirí a
ainmniú. Féach ar na [léarscáileanna clúdaigh](/map/) le hathsheoltóirí in aice leat a aimsiú, agus
abair heileo ar na [cainéil](/guides/channels/) phoiblí nó áitiúla.

## An bhfuil ceann de dhíth ort? {#need}

Seolann athsheoltóir ar aghaidh gach teachtaireacht tuile a chloiseann sé, agus roinneann gach
athsheoltóir sa raon an t-am craolta céanna. Má shroicheann an mogalra thú cheana féin,
cuireann athsheoltóir eile le trácht, ní le clúdach. B'fhéidir gur leor duit compánach atá suite go
hard, ag fuinneog áiléir nó ar bhalcóin.

Cuir athsheoltóir suas san áit a bhfuil clúdach in easnamh:

- ní léiríonn na [léarscáileanna clúdaigh](/map/) aon athsheoltóir in aice leat, nó ní léiríonn siad
  ach cinn nach gcloiseann do chompánach;
- deir do ghrúpa áitiúil go bhfuil ceann de dhíth ar an gceantar.

## Roghnaigh suíomh {#site}

Is tábhachtaí airde ná cumhacht. Is fearr a thaistealaíonn LoRa ar 868 MHz nuair atá líne radhairc
ghlan aige. Cailleann tú i bhfad níos mó raoin de bharr cnoc, foirgneamh agus crann dlúth ná mar a
thugann cúpla milleavata breise ar ais.

- **Téigh in airde.** Clúdaíonn díon, crann raidió, foirgneamh ard nó cnoc i bhfad níos mó ná leac
  fuinneoige. Cabhraíonn fiú cúpla méadar os cionn na ndíonta máguaird.
- **Coinnigh an aeróg saor.** Feistigh í os cionn imill an dín, amach ó mhiotal, ó gháitéir agus ó
  aeróga eile.
- **Seiceáil an radharc.** Taispeánann uirlisí ar nós [HeyWhatsThat](https://www.heywhatsthat.com/)
  cad atá le feiceáil ó shuíomh. Más féidir leat spota a fheiceáil, tá athsheoltóir ansin i do
  raon.
- **Fág spás saor.** Teastaíonn roinnt spáis shaoir ó chonair raidió timpeall na líne dírí, ní hamháin
  an líne féin. Thar achair fhada, ba cheart roinnt méadar a bheith idir lár na conaire agus constaicí.
- **Iarr cead.** Faigh toiliú an úinéara don díon nó don chrann, agus socraigh conas a shroichfidh
  tú an t-athsheoltóir le haghaidh cothabhála.

## Crua-earraí {#hardware}

- **Bord.** Roghnaigh bord nRF52 ísealchumhachta ar nós an
  [Heltec T114](/devices/), RAK WisBlock nó an SenseCAP Solar Node. Úsáideann boird ESP32 níos mó
  cumhachta (marcálann leathanach na ngléasanna iad mar High), agus mar sin is deacair iad a rith
  ar ghrianchumhacht.
- **Aeróg.** Úsáid aeróg atá déanta do 868 MHz, agus feistigh go hingearach í; pléann an
  [treoir aeróige](/guides/antenna/) cineálacha, nascóirí, cábla agus feistiú. Áirítear gnóthachan na
  haeróige sa teorainn chumhachta dhlíthiúil; féach
  [Teorainneacha dlíthiúla](#legal).
- **Cábla.** Coinnigh an cábla comhaiseach gearr, nó úsáid cábla ísealchaillteanais. Ar 868 MHz, is
  féidir leath do chumhachta a chailleadh i gcúpla méadar de chábla tanaí.
- **Cásáil.** Bosca díonach ar an aimsir (IP65 nó níos fearr) le faisceán cábla, poll aeraithe nó
  draenála i gcoinne comhdhlúthúcháin, agus dath éadrom nó scáth gréine. Cuireann teas as do
  cheallraí, agus ní féidir iad a luchtú faoin reophointe.
- **Tintreach.** Is sprioc í aeróg ar dhíon. Lean na rialacha áitiúla maidir le talmhú, nó feistigh í
  san áit nach sroichfeadh buille tintrí sreangú an fhoirgnimh.

## Cumhacht agus méid an chórais ghréine {#power}

Caithfidh athsheoltóir gréine seachtainí is dorcha an gheimhridh a sheasamh. Roghnaigh an méid dá
réir:

1. **Tomhais an t-ualach.** Rith an t-athsheoltóir cumraithe trí mhéadar cumhachta USB ar feadh lae.
   Léigh an fuinneamh a úsáideadh in uaireanta vata (Wh). Athraíonn an trácht i do cheantar an
   uimhir, mar sin tomhais ar an láthair más féidir leat.
2. **Cuir cúlchiste leis.** Pleanáil toilleadh ceallra do 5 go 7 lá ar a laghad gan grian úsáideach.
3. **Faigh amach cé mhéad gréine a bhíonn agat sa gheimhreadh.** Taispeánann
   [uirlis PVGIS](https://re.jrc.ec.europa.eu/pvg_tools/en/) an AE, atá saor in aisce, an méid fuinnimh
   a tháirgeann painéal in aghaidh na míosa, d'aon suíomh. Úsáid an mhí is lú gréine.
4. **Roghnaigh méid an phainéil.** Caithfidh an painéal an fuinneamh a úsáidtear gach lá a athsholáthar
   sa mhí is measa sin, le corrlach do chaillteanais luchtaithe.

Sampla oibrithe, le huimhreacha toimhdithe: teastaíonn ceallra 7 Wh ar a laghad ó athsheoltóir a
úsáideann 1 Wh in aghaidh an lae le haghaidh cúlchiste seachtaine, thart ar 2 Ah de thoilleadh
inúsáidte ag 3.7 V. Má deir PVGIS go dtugann painéal 1 W ar do shuíomh 0.5 Wh in aghaidh an lae i
mí na Nollag, teastaíonn painéal 2 W ar a laghad uait, agus fágann 3 go 5 W corrlach do scamaill,
sneachta agus aosú.

## Cuir ar bun é {#config}

**Splancáil.** Úsáid an [splancálaí gréasáin](https://flasher.meshcore.io) agus roghnaigh na dochtearraí
**Repeater** do do bhord. Féach
[Tosaigh](/get-started/#flash) le haghaidh na gcéimeanna splancála.

**Cumraigh thar USB.** Agus an t-athsheoltóir fós ceangailte le do ríomhaire, oscail
[config.meshcore.io](https://config.meshcore.io) nó consól an splancálaí. Is féidir leat aon
teirminéal sraitheach ag 115200 baud a úsáid freisin. Na horduithe is tábhachtaí:

| Cad | Ordú |
|---|---|
| Athraigh pasfhocal an riarthóra | `password <new password>` |
| Tabhair ainm dó | `set name <name>` |
| Réamhshocrú raidió: minicíocht, bandaleithead, SF, CR (atosaigh lena chur i bhfeidhm) | `set radio 869.618,62.5,8,8` |
| Teorainn an timthrialla dleachta, faoin gcéad | `set dutycycle 10` |
| Cumhacht tarchuir shlis an raidió, in dBm | `set tx <dBm>` |
| Suíomh, ionas go dtaispeánfar ar léarscáileanna é | `set lat <degrees>` agus `set lon <degrees>` |
| Sonraí teagmhála d'oibreoirí eile | `set owner.info <text>` |
| Uaireanta idir fógraí tuile, na cinn a chloiseann an mogalra ar fad | `set flood.advert.interval <hours>` |
| Fógair anois é | `advert` |
| Atosaigh | `reboot` |

Is é `password` pasfhocal réamhshocraithe an riarthóra, agus déantar riarthóir d'aon duine a logálann
isteach leis. Athraigh é sula dtéann an t-athsheoltóir ar an aer.

Is é EU/UK (Narrow) an sampla `set radio` thuas. Úsáid luachanna réamhshocrú do cheantair ina áit:
tá siad liostaithe de réir tíre in [Socruithe molta](/guides/settings/).

**Socraigh an clog.** Gan modúl cloig (RTC), cailleann athsheoltóir an t-am le gach briseadh cumhachta
agus tosaíonn sé arís i mBealtaine 2024. Le linn dó a bheith ag rith, sleamhnaíonn a chlog freisin:
téann sé níos faide chun tosaigh nó ar gcúl. Mar sin, socraigh an clog ó am go ham: logáil isteach go
cianda ón aip agus úsáid `clock sync`, nó socraigh an t-am thar USB. Le modúl RTC, is annamh a
chaithfidh tú é sin a dhéanamh: coinníonn sé an t-am le linn bristeacha cumhachta agus sleamhnaíonn sé
i bhfad níos lú.

**Bainistigh go cianda é.** Nuair a bheidh sé ar an mogalra, logáil isteach ón aip MeshCore le pasfhocal
an riarthóra. Léann tú a stádas ansin agus úsáideann tú na horduithe céanna thar an raidió. Ní oibríonn
roinnt orduithe ach thar USB, ar nós `set freq` agus an athshocraithe mhonarchan `erase`.

**Coinnigh a aitheantas.** Roimh ghlanadh, clóscríobh `get prv.key` thar USB agus cuir an eochair
phríobháideach a thaispeánann sé áit éigin shábháilte. Tar éis an ghlanta, tugann `set prv.key <key>`
agus `reboot` a sheanaitheantas ar ais don athsheoltóir, ionas go n-aimseoidh nóid a bhfuil aithne acu
air é faoin réimír chéanna.

Tá an liosta iomlán orduithe sa
[tagairt CLI MeshCore](https://github.com/meshcore-dev/MeshCore/blob/main/docs/cli_commands.md).

## Nuashonraigh thar an aer é {#update}

Nuair a bhíonn an t-athsheoltóir thuas go hard, nuashonraíonn tú ón talamh é. Logáil isteach ón aip
MeshCore le pasfhocal an riarthóra, oscail a líne ordaithe agus clóscríobh `start ota`. Braitheann a
dtarlaíonn ina dhiaidh sin ar an mbord; freagraíonn boird eile `Error`, agus nuashonraíonn tú iad sin
thar USB.

**Boird nRF52**, ar nós RAK, Heltec T114, Seeed XIAO agus SenseCAP Solar:

1. Íoslódáil **ZIP** na ndochtearraí nua do do bhord ón
   [splancálaí gréasáin](https://flasher.meshcore.io).
2. Clóscríobh `start ota`. Freagraíonn an t-athsheoltóir `OK` agus feictear thar Bluetooth é mar
   `<board>_OTA`, mar shampla `RAK4631_OTA`.
3. Oscail an aip nRF Device Firmware Update ar do ghuthán, roghnaigh an ZIP agus an t-athsheoltóir,
   agus uaslódáil. Tógann sé cúpla nóiméad.

Suiteáil an [lódálaí tosaithe OTAFIX](https://github.com/oltaco/Adafruit_nRF52_Bootloader_OTAFIX)
ar bhord nRF52 sula dtéann sé in airde. Leis an lódálaí tosaithe bunaidh, ní féidir nuashonrú
teipthe a dheisiú ach thar USB. Le OTAFIX, filleann an bord ar mhód nuashonraithe, agus déanann tú
iarracht eile thar Bluetooth.

**Boird ESP32**, ar nós an Heltec V3 agus V4:

1. Íoslódáil an comhad `.bin` **neamhchumaiscthe** do do bhord ón splancálaí gréasáin: an comhad
   nach bhfuil "merged" ina ainm.
2. Clóscríobh `start ota`. Osclaíonn an t-athsheoltóir líonra WiFi darb ainm `MeshCore-OTA` agus
   freagraíonn sé le seoladh a leathanaigh uaslódála.
3. Laistigh de raon WiFi, ceangail do ghuthán nó do ríomhaire glúine leis an líonra sin, oscail an
   seoladh agus uaslódáil an comhad.

## Teorainneacha dlíthiúla {#legal}

{{< callout type="legal" verified="2026-10-02" >}}
Tá réamhshocruithe Eorpacha MeshCore san fhobhanda **869.40-869.65 MHz**. San AE, sa Ríocht Aontaithe,
san Eilvéis agus san Iorua, tá sé oscailte do ghléasanna gearr-raoin gan cheadúnas, laistigh de na
teorainneacha seo:

- **500 mW e.r.p.** ar a mhéad de chumhacht radaithe;
- **timthriall dleachta 10%** ar a mhéad: 360 soicind tarchuir ar a mhéad in aon uair an chloig, in
  aghaidh an ghléis. Mar mhalairt air sin, féadfaidh gléas éisteacht roimh labhairt a úsáid le
  haclaíocht oiriúnaitheach minicíochta mar a shainmhínítear in ETSI EN 300 220-2;
- caithfidh an comhartha iomlán, 250 kHz ar leithead ar a mhéad, fanacht laistigh den fhobhanda.

Is banda roinnte é: ní mór duit gan cur isteach ar sheirbhísí ceadúnaithe, agus féadfaidh daoine
eile cur isteach ort.
Caithfidh marc CE a bheith ar an raidió (sa Bhreatain Mhór, CE nó UKCA).
{{< /callout >}}

Foinsí: [Moladh CEPT ERC 70-03](https://docdb.cept.org/document/845),
Iarscríbhinn 1, banda h1.7;
[Cinneadh ón gCoimisiún 2006/771/EC](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02006D0771(01)-20250123)
agus a leasuithe;
[ETSI EN 300 220-2](https://www.etsi.org/deliver/etsi_en/300200_300299/30022002/03.03.01_60/en_30022002v030301p.pdf),
banda O.

### Cumhacht: e.r.p. agus d'aeróg {#erp}

Baineann an teorainn leis an gcumhacht *radaithe*, tomhaiste i gcoinne aeróige déphoil shimplí
(e.r.p.). Áirítear gnóthachan na haeróige; bainann caillteanas cábla ón iomlán. Luann déantóirí
gnóthachan aeróige in dBi, atá 2.15 dB níos mó ná an gnóthachan céanna in dBd (i gcoibhneas le
déphol). Coinnigh an tsuim seo ag 27 dBm (500 mW) nó faoina bhun:

> cumhacht tarchuir (dBm) + gnóthachan aeróige (dBi) − caillteanas cábla (dB) − 2.15 ≤ 27

- Bord a tharchuireann 22 dBm isteach in aeróg 5 dBi trí 1 dB de chábla:
  22 + 5 − 1 − 2.15 = 23.85 dBm, thart ar 240 mW e.r.p. Laistigh den teorainn.
- Bord le haimplitheoir 30 dBm (1 W) isteach in aeróg 3 dBi:
  30 + 3 − 2.15 = 30.85 dBm, thart ar 1.2 W e.r.p. Thar an teorainn; ísligh an chumhacht tarchuir.

Socraíonn `set tx` aschur na slise LoRa, in dBm. Is é 22 dBm uasmhéid na slise SX1262 féin; ní sheiceálann
na dochtearraí an uimhir a chuireann tú isteach. Tarchuireann boird le haimplitheoir breise, ar nós an
Heltec V4 nó an Station G2, i bhfad níos mó ná an uimhir a shocraíonn tú. Seiceáil tábla an déantóra
sula socraíonn tú í, agus tosaigh go híseal.

### Timthriall dleachta {#duty-cycle}

Tarchuireann athsheoltóir do gach duine timpeall air, mar sin ídíonn sé a am craolta níos tapa ná
compánach. Is é 50% an réamhshocrú ar theorannóir timthrialla dleachta MeshCore, agus tá sé sin os cionn
an mhéid a cheadaíonn an banda seo. Socraigh é ar 10% ar gach athsheoltóir:

```text
set dutycycle 10
```

### Cruinneas minicíochta {#frequency}

Sroicheann cainéal EU/UK (Narrow), 869.618 MHz le bandaleithead 62.5 kHz, suas go 869.649 MHz: níos
lú ná 1 kHz faoi bharr an fhobhanda. Caithfidh an comhartha fanacht laistigh den bhanda ag gach
teocht. Teastaíonn criostal teochtchúitithe (TCXO) chuige sin. Tá ceann ag beagnach gach bord reatha;
sleamhnaíonn boird níos sine gan é, ar nós an Heltec V2, an iomarca le hoibriú go hiontaofa ag 62.5 kHz.

### Nótaí tíre {#countries}

- **Caithfidh ballstáit an AE** an fobhanda seo a chur ar fáil ar na téarmaí seo
  (Cinneadh 2006/771/EC, Airteagal 3).
- **An Ríocht Aontaithe:** na teorainneacha céanna, in Ofcom
  [IR 2030](https://www.ofcom.org.uk/spectrum/radio-equipment/short-range-devices).
- **An Eilvéis agus Lichtinstéin:** na teorainneacha céanna, in OFCOM
  [RIR1008-09](https://www.ofcomnet.ch/api/rir/1008/09).
- **An Iorua:** na teorainneacha céanna, sa
  [rialachán ar údaruithe ginearálta](https://lovdata.no/dokument/SF/forskrift/2012-01-19-77)
  (fribruksforskriften).

Ní comhairle dhlíthiúil iad na nótaí seo. Athraíonn rialacha; má tá amhras ort, seiceáil le do
rialtóir náisiúnta.

## Seicliosta imlonnaithe {#checklist}

- [ ] D'aontaigh úinéir an tsuímh, agus is féidir leat an t-athsheoltóir a shroicheadh le haghaidh
      cothabhála.
- [ ] Ritheann an bord na dochtearraí **Repeater**, agus ceanglaíodh an aeróg roimh an gcéad chumhachtú.
- [ ] Tá pasfhocal an riarthóra athraithe.
- [ ] Tá an raidió ag teacht le [réamhshocrú do cheantair](/guides/settings/) (`get radio`).
- [ ] Tá `set dutycycle 10` socraithe.
- [ ] Fanann cumhacht tarchuir móide gnóthachan aeróige laistigh de 500 mW e.r.p.
- [ ] Tá an t-ainm, an suíomh agus `owner.info` socraithe, ionas go mbeidh a fhios ag daoine eile cé
      a oibríonn é.
- [ ] Tá an clog socraithe (`clock`).
- [ ] Tá an chásáil séalaithe, le poll draenála nó aeraithe, agus tá lúb sileáin ar an gcábla.
- [ ] Tá méid an cheallra agus an phainéil roghnaithe don mhí gheimhridh is measa.
- [ ] Thástáil tú é ó achar leis an aip sular fhág tú an suíomh.
- [ ] Tá a fhios ag do ghrúpa áitiúil go bhfuil sé ar siúl.
