---
title: Déan an mogalra athléimneach
lead: An bhfuil an mogalra in aice leat mall nó lán le dramhaíl? Faigh amach cad is cúis leis, cas air an socrú athsheoltóra a stopann é, agus cuir do ghrúpa áitiúil ar an eolas.
description: 'Tuilte agus turscar ar mhogalra MeshCore: conas gach cineál a aithint, cén socrú athsheoltóra a chabhraíonn, conas tuile a fheiceáil agus conas a foinse a aimsiú.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '500188ff'
  seeded: '2026-11-02'
  fields: {title: '33ec7ac8', lead: '780da19b', description: '1826e5e8'}
  sections: ['68ca5d36', '133c764a', 'a3bb5172', 'f4cc9cad', 'ace7b1ee', '89651002', 'f4dfdf59', '764c832c', 'f342b64b', 'f348e208']
  blocks: ['68ca5d36', 'c9cfbe6c', 'bcb31992', 'de7f60e4', 'e862fb9b', '0046b51f', '25f34d1d', 'c3c3ea52', '853a0f1d', '2bcea703', '871a7661', '2690aacf', 'a4aec3a1', 'd6da27c6', 'e8405458', 'f9150ee6', '8508ce40', '4b03ccd5', 'fb79c493', '695adde7', 'eba5a5b5', '836e0bac', '3497c5e8', '71c78fa1', '537d0930', '6a315252', '7c84dc56', '682e08e6', '258d7a27', '53af1400', '0dbebf97', 'ac0dca3c', '70fb4e9a', '9f055f50', 'ae90facc']
---

An dtagann teachtaireachtaí go déanach, nó nach dtagann siad in aon chor? An líontar Public le dramhaíl? Sin tuile: níos mó tráchta ná mar is féidir leis an mogalra a iompar, a sheoltar trí thimpiste nó d'aon turas. Aimsigh a bhfeiceann tú sna táblaí thíos. Luann gach ró an socrú a stopann é. Cuir an socrú sin ar siúl ar d'athsheoltóir, an nód a chuireann teachtaireachtaí ar aghaidh. Ansin cuir do [ghrúpa áitiúil](/community/) ar an eolas, ionas go ndéanfaidh na hathsheoltóirí thart ort an rud céanna. Gach athsheoltóir a chaitheann tuile amach, fágann sé am craolta ag gach duine eile.

## Tuilte trí thimpiste {#mistake}

Tagann tuile thimpisteach ó nód nach eol dá úinéir go bhfuil sé ina chúis léi. Stopann sí a luaithe is eol don úinéir í. Sna táblaí thíos, is ionann fógra agus an beannú a sheolann nód ionas gur féidir le nóid eile é a aimsiú.

Tagann na socruithe sna táblaí ón méid a dhéanann na dochtearraí. Níor stop gach ceann acu tuile ar mhogalra fíor go fóill.

{{< callout type="warning" >}}
Tá na dochtearraí DMC de dhíth ar shocruithe áirithe ar an leathanach seo. Tá réigiúin, na teorainneacha léime `flood.max.*`, brath lúibe agus an timthriall dualgais i **MeshCore** caighdeánach 1.18.0. Is iad na **dochtearraí DMC** ó [Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore) a thugann an scagaire paicéad duit, na rialacha a ligeann do d'athsheoltóir dramhaíl a chaitheamh amach. Tagann geatú an timthrialla dualgais agus scagaire an chompánaigh leo freisin. Leanann an leathanach seo tógáil forbartha DMC 1.18.0 `ecfb2d4` dar dáta 19 Deireadh Fómhair 2026; insíonn an leathanach [scagaire paicéad](/guides/filter/#firmware) duit cá bhfaighidh tú í.
{{< /callout >}}

| A bhfeiceann tú | Cad atá ann | Cad a chabhraíonn |
| --- | --- | --- |
| Iarratais chuig athsheoltóirí ó nód amháin, de lá is d'oíche, agus mogalra a fhanann mall ar feadh laethanta | Córas uathoibrithe tí nó bot a iarrann a stádas ar athsheoltóirí rómhinic | `filter on`. Ansin ligeann an scagaire paicéad 5 iarratas in aghaidh an nóiméid tríd. Cuir an t-úinéir ar an eolas. |
| An cineál céanna teachtaireachta ar chainéal, gach nóiméad | Bot a phostálann rómhinic | [Cuir bac ar an gcainéal](/guides/filter/#channel) nó [cuir moill ar an tseoltóir](/guides/filter/#sender). Cuir an t-úinéir ar an eolas. |
| Teachtaireachtaí doléite ar Public agus ar chainéil eile | Nód a bhfuil dochtearraí briste nó socruithe raidió míchearta aige | Caitheann `filter malformed on` amach iad ar Public. Cuir an t-úinéir ar an eolas. |
| Fógra nóid amháin gach cúpla nóiméad | Nód atá socraithe chun fógraí a sheoladh rómhinic | Ligeann `filter advert 24` fógra gach nóid tríd uair sa lá. Coinníonn `set flood.max.advert 3` fógraí laistigh de 3 léim. |
| Teachtaireachtaí ó chian, le réigiúin nach mbaineann leis an áit seo | Droichead a nascann mogalraí thar an idirlíon | `set flood.max.unscoped 1`, agus ná cuir d'athsheoltóir ach sna [réigiúin a bhfreastalaíonn sé orthu](/guides/settings/#traffic). |
| Téann an teachtaireacht chéanna thart arís is arís, agus tá aitheantas d'athsheoltóra ina conair níos mó ná uair amháin | Athsheoltóir a athraíonn paicéid agus a chuireann ar aghaidh iad, ionas go dtéann siad i lúb | Bíonn brath lúibe ar `minimal` de réir réamhshocraithe. Caitheann `set loop.detect moderate` lúb amach níos túisce. |

## Tuilte d'aon turas {#purpose}

Turscar atá i roinnt tuilte: dramhaíl a sheoltar d'aon turas chun an mogalra a thachtadh. Athraíonn an seoltóir ainmneacha, eochracha agus conairí, mar sin ní stopann aon riail amháin an tuile.

| A bhfeiceann tú | Cad atá ann | Cad a chabhraíonn |
| --- | --- | --- |
| Go leor nód nua le hainmneacha randamacha, gach ceann acu le heochair nua | Fógraí bréige | Ligeann `filter rate 04 5 60` 5 fhógra in aghaidh an nóiméid tríd. Ní chabhraíonn `filter advert`: tagann gach fógra ó [eochair nua](#forged). |
| Teachtaireachtaí le téacs doléite ó sheoltóirí bréige, go minic le dáta níos mó ná bliain ó shin | Turscar cainéil | Caitheann `filter malformed on` amach iad ar Public. Caitheann `filter age 60` amach na cinn le seandáta ar Public agus ar [chainéil faoi fhaire](/guides/filter/#settings). |
| Suas le 200 teachtaireacht dhíreach in aghaidh an nóiméid chuig nóid nach ann dóibh, gan aon admháil ar ais | Tuile teachtaireachtaí díreacha | `filter rate 02 5 60`. Ní thaispeánann d'aip na teachtaireachtaí seo; taispeánann breathnóir iad. |
| Ráigeanna iarratas ó nód amháin chuig dosaein nód eile | Turscar iarratas | Le `filter on`, ligeann an scagaire paicéad 5 iarratas in aghaidh an nóiméid tríd. |
| Tagann teachtaireacht ar ais 10 go 20 nóiméad níos déanaí, leis an gconair beagnach mar an gcéanna | Athsheinm: cóip a seoltar arís | Cuimhníonn athsheoltóir ar na 160 paicéad deireanacha a chonaic sé, mar sin téann cóip níos déanaí tríd arís ar mhogalra gnóthach. Caitheann `filter age` amach teachtaireacht ghrúpa atá níos sine ná mar a cheadaíonn tú. |
| Teachtaireachtaí ó Public a seoltar arís faoi sheoltóir bréige, uaireanta le seandáta | Turscar macalla | `filter age 60`. Caitheann `filter malformed on` amach freisin dáta atá mícheart faoi níos mó ná seachtain. |
| Teachtaireacht gach cúpla soicind ar roinnt cainéal, gach ceann ó ainm nua, le gnáthcheisteanna | Tonn botanna | `filter rate 05 10 60`, agus [cuir bac ar na cainéil](/guides/filter/#channel) nach n-úsáideann do cheantar. Tá gach ainm nua, mar sin ní bheireann na [rialacha seoltóra](#forged) air. |

## Cad a d'oibrigh {#worked}

Stop grúpaí áitiúla tuilte leis na céimeanna seo:

1. **Cuir an t-úinéir ar an eolas.** Stopann tuile thimpisteach a luaithe is eol dá húinéir í. Seol teachtaireacht chairdiúil chuige.
2. **Ná freagair ar an mogalra.** Taispeánann freagra do sheoltóir turscair go n-oibríonn an turscar.
3. **Iarr breathnóirí.** Is nód é breathnóir a thuairiscíonn gach paicéad a chloiseann sé thar MQTT. Dá mhéad breathnóirí atá thart ort, is ea is túisce a fheicfidh tú cá dtagann tuile isteach. Déan breathnóir de d'athsheoltóir féin le [MQTT ar do bhreathnóir](/guides/mqtt/).
4. **Aimsigh an fhoinse.** Aimsíonn breathnóirí an ceantar ina bhfuil an seoltóir. Don chiliméadar deireanach, caithfidh daoine siúl le raidió. Féach [Aimsigh an fhoinse](#source).
5. **Spreag do ghrúpa áitiúil.** Cabhraíonn athsheoltóir amháin leis na socruithe cearta. Stopann na hathsheoltóirí uile sa cheantar tuile le chéile. Cinntíonn do [ghrúpa áitiúil](/community/) go gcuireann gach úinéir an socrú ar siúl.

## Seoltóirí agus conairí bréige {#forged}

Scríobhann seoltóir na codanna seo de phaicéad, agus ní sheiceálann aon rud iad:

- **Ainm an tseoltóra.** I dteachtaireacht chainéil, is cuid den téacs an t-ainm. Is féidir le duine ar bith a bhfuil eochair an chainéil aige ainm ar bith a scríobh.
- **Tús na conaire.** Cuireann gach athsheoltóir a aitheantas féin le deireadh na conaire. Ní sheiceálann aon rud na haitheantais a bhí ann roimhe, mar sin is féidir le seoltóir an chonair a thosú le haitheantais bhréige. Tá deireadh na conaire fíor.

{{< forged-path >}}

Mar sin, ní stopann `filter sender` agus `filter path` seoltóir ach go dtí go n-athraíonn sé a ainm nó a chonair. Caitheann [bac conaire](/guides/filter/#path) amach freisin fíorthrácht an athsheoltóra a bhfuil a aitheantas sa bhac. Leanann teorainneacha ráta, teorainneacha léime, na seiceálacha aoise agus míchumtha, bacanna cainéil, réigiúin agus an timthriall dualgais ag obair.

## Socruithe do gach tuile {#always}

Oibríonn na socruithe seo cibé tuile a bhuaileann an mogalra:

- **Timthriall dualgais ag 10%.** Ansin ní tharchuireann d'athsheoltóir riamh níos mó ná mar a cheadaíonn an dlí, cibé rud a thagann isteach. Pléann an [treoir athsheoltóra](/repeater-guide/#duty-cycle) é.
- **Réigiúin agus teorainneacha léime.** Is ionann réigiún agus an limistéar ina bhfanann teachtaireacht. Ní chuireann athsheoltóir ar aghaidh ach teachtaireachtaí sna réigiúin atá aige, agus coinníonn `flood.max.*` an trácht gar. Tá an dá rud in [Coinnigh trácht íseal](/guides/settings/#traffic).
- **An scagaire paicéad d'athsheoltóir gnóthach.** Laghdaíonn na [socruithe réamhdhéanta](/guides/filter/#busy) teachtaireachtaí grúpa agus fógraí faoi leath. Bain triail astu i mód [dry-run](/guides/filter/#dryrun) ar dtús: ní dhéanann sé ach an méid a chaithfeadh sé amach a chomhaireamh.
- **Scagaire an chompánaigh, sna dochtearraí DMC.** Coinníonn do chompánach, an nód óna seolann tú teachtaireachtaí, dramhaíl as d'aip. Folaíonn sé teachtaireachtaí briste agus seanteachtaireachtaí, agus teachtaireachtaí ó athsheoltóir, ó sheoltóir nó le focal a gcuireann tú bac orthu. Ní fholaíonn riail seoltóra nó focail an teachtaireacht ach uaitse; faigheann daoine eile í fós.

### Geatú an timthrialla dualgais {#gate}

Sna dochtearraí DMC, is féidir le d'athsheoltóir tosaíocht a thabhairt dá réigiún féin nuair a éiríonn sé gnóthach. A luaithe a tharchuir sé ar feadh níos mó ná 35% den nóiméad deireanach, stopann sé de theachtaireachtaí gan réigiún a chur ar aghaidh. Má fhanann sé gnóthach, caitheann sé amach an réigiún is leithne ina dhiaidh sin, leibhéal amháin ag an am. Téann a réigiún féin tríd i gcónaí. Ní oibríonn sé ach nuair atá réigiúin socraithe ar d'athsheoltóir. Cuir ar siúl é agus seiceáil é:

```text
set dc.gate on
get dc.gate.status
```

{{< dc-gate >}}

Ní thaispeánann `filter stats` a gcaitheann sé amach. Nuair a bhíonn an t-athsheoltóir ciúin arís, tagann na réigiúin ar ais, an ceann is faide istigh ar dtús.

## Tuile a fheiceáil {#see}

Ní thaispeánann d'aip ach a shroicheann thú. Ní chloiseann ach breathnóir tuile teachtaireachtaí díreacha chuig nóid nach ann dóibh. Tuairiscíonn gach breathnóir don [MeshCore Analyzer](https://meshcore-analyzer.eu/), áit ar féidir le gach duine é a fheiceáil. Déan breathnóir de d'athsheoltóir le [MQTT ar do bhreathnóir](/guides/mqtt/).

Ar an Analyzer, féach ar gach cóip de phaicéad amháin. De ghnáth, léiríonn a chonair cé as ar tháinig sé. Is féidir le seoltóir tuile an chonair a thosú le [haitheantais bhréige](#forged), mar sin ní insíonn na chéad aitheantais aon rud duit. Ach bíonn an tús bréige céanna ar gach cóip. Chuaigh an chóip leis an gconair is giorra tríd an líon is lú fíor-athsheoltóirí, mar sin is gaire don tseoltóir a chualathas í.

{{< copies >}}

Ar d'athsheoltóir féin, taispeánann `filter stats` a chaith an scagaire paicéad amach. Taispeánann `filter stats top` an chéad bheart d'aitheantais na nód is cúis leis an gcuid is mó den mhéid a caitheadh amach. Tá an beart sin ag go leor nód, mar sin caolaíonn sé an cuardach ach ní ainmníonn sé an seoltóir.

## Aimsigh an fhoinse {#source}

Nuair a thagann tuile ar ais arís is arís:

1. **Lean na conairí.** Léigh conair ón deireadh: is iad na haitheantais dheireanacha na hathsheoltóirí a ndeachaigh an tuile tríothu. Tá an ceann fíor is túisce gar don fhoinse; d'fhéadfadh na haitheantais roimhe a bheith [bréagach](#forged).
2. **Caolaigh an ceantar.** Nuair a chloiseann roinnt breathnóirí an paicéad céanna, aimsíonn siad an ceantar ina bhfuil an seoltóir. Oibríonn an [DMC Triangulator](https://triangulator.dutchmeshcore.nl/) amach é ó na hathsheoltóirí a chuala é.
3. **Siúil an ciliméadar deireanach.** Ní chloiseann na hathsheoltóirí an fhoinse ach ag imeall a raoin, mar sin caithfidh daoine an chuid dheireanach a shiúl. Péireálann [Mesh-Hunter](https://mesh-hunter.eu/) le do chompánach agus logálann sé gach paicéad a chloiseann sé le do shuíomh GPS. Aimsíonn roinnt daoine atá ag siúl ag an am céanna í níos túisce.
4. **Cuir do [ghrúpa áitiúil](/community/) ar an eolas.** Feiceann siad níos mó den mhogalra, socraíonn siad cad a tharlóidh ina dhiaidh sin, agus déanann siad teagmháil le duine ar bith a chruthaíonn tuile d'aon turas.

## Cuir leis a chonaic tú {#add}

Ar bhuail tuile thú nach bhfuil sna táblaí seo? Ar stop socrú ceann acu? Inis dúinn ar [Discord](https://discord.meshcore-info.eu/): a chonaic tú agus a chuir tú ar siúl. Cuirfimid leis an leathanach é.
