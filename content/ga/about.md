---
title: Cad é MeshCore?
lead: Seolann MeshCore teachtaireachtaí téacs thar raidió, ó nód go nód. Oibríonn sé gan an t-idirlíon agus gan síntiús.
description: 'Cad is MeshCore ann agus cad nach bhfuil ann: cineálacha nóid, ródú, an difríocht ó Meshtastic, criptiú agus an banda 868 MHz.'
eyebrow: MeshCore v1.18.0
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '279b56a4'
  seeded: '2026-11-02'
  fields: {title: '06eda66b', lead: 'c0174569', description: '15e6d2a7', eyebrow: '8610c822'}
  sections: ['aa768ac3', '16fde264', '0a55792c', 'c3de803d', '493b444f', 'a8b2b9b4', '429f699c', 'f8008f48', '88af2bd3', '0894fe81']
  blocks: ['c3c9c568', '55e4248c', 'c0324d05', 'b20e61c3', 'fab378a5', '68ed3005', 'cabeb32d', 'b2ca68ba', '681d55b9', 'd1df283f', '0d0e2a8b', '0596f602', 'eec63bed', '183a79e4', '47910535', 'd5a92bbf', 'b44d4637', 'fc8f3129', '8dec428a', '07cbac35', '431021a0', '83c03732', 'e908ca85', '8f79fbf9', '3323d83e', '857c37dc', '0c4d0dd2', 'bd238f09', '794792be', '95e18f18', '02f1fe2f', 'e6b5b258']
---

Bogearraí saora do raidiónna beaga LoRa is ea MeshCore. Teicníc raidió is ea LoRa a sheolann beagán sonraí i bhfad, ar fhíorbheagán cumhachta. Tugtar *nód* ar raidió a bhfuil MeshCore air. Nuair a nascann tú é leis an aip ar do ghuthán nó ar do ríomhaire glúine, nó nuair a úsáideann tú a scáileán agus a mhéarchlár féin, seolann tú téacs chuig daoine atá ciliméadair uait. Níl aon túr, ródaire ná soláthraí sa lár.

Bogearraí foinse oscailte atá iontu. Forbraítear iad ag [meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore) faoin gceadúnas MIT.

## Cad nach bhfuil i MeshCore {#not}

An bhfuil raidió nua duit? Seo na rudaí is minice a mbíonn daoine ag súil leo ó MeshCore, agus nach ndéanann sé.

- **Ní hé an t-idirlíon é, ná guthán.** Seolann MeshCore teachtaireachtaí gearra téacs, thart ar fhad téacs ar do ghuthán. Níl guth, grianghraif, físeáin ná suíomhanna gréasáin ann, agus ní féidir leat gnáthuimhir ghutháin a bhaint amach.
- **Ní seirbhís éigeandála é.** Níl aon seirbhís éigeandála ag éisteacht ar an mesh, agus ní gheallann aon duine go léifidh duine éigin do theachtaireacht. I gcás éigeandála, glaoigh ar 112.
- **Níl sé ar an toirt, ná i ngach áit.** Léimeann teachtaireacht ó raidió go raidió agus d'fhéadfadh sí cúpla soicind a thógáil, nó gan teacht in aon chor. Cibé an dtagann sí slán nó nach dtagann, braitheann sé ar na hathsheoltóirí timpeall ort, ar airde, ar fhoirgnimh agus ar d'aeróg. Is minic nach sroicheann raidió beag istigh aon duine; tá raon ciliméadar ag athsheoltóir ar dhíon.
- **Ní seirbhís é a reáchtálann duine éigin duit.** Níl soláthraí, deasc chabhrach ná gealltanas clúdaigh ann. Tá an mesh ann áit ar chuir daoine sa phobal athsheoltóirí in airde, agus níl sé áit ar bith eile.
- **Níl gach rud air príobháideach.** Tá teachtaireachtaí díreacha criptithe, ach is féidir le duine ar bith Public agus na cainéil haischlibe a léamh, agus feiceann gach duine atá i raon ainm do nóid agus an suíomh a roinneann tú. Tuairiscíonn [breathnóirí](/network/) an méid a chloiseann siad do léarscáileanna poiblí. Míníonn [an chuid faoi chriptiú](#encryption) cad a fhanann príobháideach.
- **Níl sé gan teorainn.** Roinneann gach duine i gceantar aon chainéal raidió amháin, agus cuireann na rialacha don [bhanda 868 MHz](#band) teorainn leis an méid ama a fhéadann gach raidió a bheith ag seoladh. Baineann gach teachtaireacht am craolta de gach duine eile, mar sin cuireann róbónna, fógraí minice agus teachtaireachtaí tástála moill ar an mesh do chách.
- **Ní Meshtastic é.** Córas difriúil is ea Meshtastic a ritheann ar bhoird atá mórán mar an gcéanna. Ní féidir leis an dá chóras labhairt le chéile. Liostaíonn [Ag teacht ó Meshtastic](#meshtastic) cad a oibríonn ar bhealach difriúil.

## An mogalra i nóiméad {#mesh}

Sroicheann raidió LoRa amháin cúpla ciliméadar i mbaile, agus i bhfad níos faide ó chnoc nó ó dhíon. Le dul níos faide, cuireann raidiónna teachtaireachtaí ar aghaidh dá chéile: sin *mogalra*. In MeshCore, is iad raidiónna ar a dtugtar *athsheoltóirí* a chuireann ar aghaidh iad. Nuair a chloiseann athsheoltóir teachtaireacht, seolann sé arís í, ionas gur féidir léi réigiún iomlán a thrasnú.

Ní le haon duine an mogalra. Is le duine éigin sa phobal gach nód agus gach athsheoltóir. Sroicheann an mogalra chomh fada agus a shroicheann a gcuid athsheoltóirí.

## Na 3 chineál nóid {#roles}

Roghnaíonn tú cineál an nóid nuair a splancann tú é. Compánach a bheidh i do chéad nód.

**Compánach.** Do raidió féin. Nascann tú é leis an aip MeshCore ar do ghuthán nó ar do ríomhaire glúine trí Bluetooth nó USB; tá a scáileán agus a mhéarchlár féin ag cuid acu. San aip a léann agus a chlóscríobhann tú. Coinníonn an compánach do theagmhálaithe agus do chainéil, agus na teachtaireachtaí a tháinig nuair nach raibh an aip nasctha. Ní chuireann compánach teachtaireachtaí daoine eile ar aghaidh.

**Athsheoltóir.** Raidió in áit ard a chuireann teachtaireachtaí ar aghaidh do chách. Ritheann a bhformhór ar chumhacht na gréine. Ní theastaíonn do cheann féin uait ach san áit nach sroicheann an mogalra fós. Níl aip dá chuid féin aige. Socraíonn tú é trí USB, nó logálann tú isteach le pasfhocal agus bainistíonn tú é thar an raidió. Taispeánann an [treoir athsheoltóra](/repeater-guide/) conas é sin a dhéanamh.

**Freastalaí seomra.** Clár beag teachtaireachtaí ar an mogalra. Nuair a logálann tú isteach, faigheann tú na postálacha a chaill tú agus tú as raon, suas leis an 32 is déanaí. Ní choinníonn sé iad ach sa chuimhne, mar sin glanann atosú nó gearradh cumhachta iad. Úsáideann grúpa áitiúil ceann le haghaidh fógraí.

## Conas a aimsíonn teachtaireacht a bealach {#routing}

Tá eochair rúnda agus eochair phoiblí ag gach nód. Is í an eochair phoiblí a aitheantas. Fógraíonn nód é féin le *fógra*: paicéad sínithe lena ainm agus, más mian leat, a shuíomh. Nochtann duine i measc do theagmhálaithe tar éis d'fhógra uaidh thú a shroicheadh, nó nuair a scanálann tú a chód QR. Tá cnaipe san aip chun do cheann féin a sheoladh.

Imíonn do chéad teachtaireacht chuig teagmhálaí mar *thuile*. Cuireann gach athsheoltóir a chloiseann í ar aghaidh í uair amháin, agus cuireann sé a aitheantas gearr féin léi ar an mbealach. Tugann an freagra an liosta aitheantas sin ar ais. Uaidh sin amach, leanann do theachtaireachtaí chuig an teagmhálaí sin an bealach taifeadta, agus ní sheolann ach na hathsheoltóirí atá air. Nuair a bhriseann an bealach, seolann an aip tuile arís.

Níl aon seoladh amháin ag teachtaireachtaí chuig cainéal, mar sin is tuile i gcónaí iad. Is cuimhin le hathsheoltóirí a bhfuil curtha ar aghaidh acu le déanaí, agus caitheann siad amach cóipeanna a thagann arís ar bhealach eile. Is féidir le teachtaireacht suas le 64 athsheoltóir a thrasnú, nó 32 san áit a n-úsáideann an réamhshocrú aitheantais 2 bheart.

## Ag aistriú ó Meshtastic {#meshtastic}

Is féidir le go leor bord MeshCore nó Meshtastic a rith, agus splancann tú an ceann is mian leat. Seo iad na difríochtaí a thugann tú faoi deara ar dtús. Tá siad bunaithe ar MeshCore v1.18.0 agus ar dhoiciméadacht Meshtastic ó mhí na Samhna 2026.

- **Cé a chuireann teachtaireachtaí ar aghaidh.** In MeshCore, is iad na hathsheoltóirí amháin a dhéanann é; ní dhéanann do chompánach é choíche. In Meshtastic, cuireann an ról cliaint réamhshocraithe teachtaireachtaí ar aghaidh freisin, mura ndearna nód eile é cheana.
- **Cé chomh fada a théann teachtaireacht.** Is féidir le teachtaireacht MeshCore dul trí suas le 64 athsheoltóir. Stopann Meshtastic tar éis 3 léim de réir réamhshocraithe, agus tar éis 7 ar a mhéad.
- **Léamha ó nóid eile.** Seolann athsheoltóirí agus nóid braiteora in MeshCore léamha, mar shampla voltas ceallraí, nuair a iarrann tú orthu iad. Ní sheolann siad chuig an mogalra iomlán iad.
- **An t-idirlíon.** Níl aon nasc idir mogalraí thar an idirlíon i bhfirmware MeshCore. Tuairiscíonn [breathnóirí](/network/) an méid a chloiseann siad do léarscáileanna, i dtreo amháin. Tá modúl MQTT ionsuite ag Meshtastic atá in ann teachtaireachtaí a iompar idir mogalraí thar an idirlíon.

## Criptiú agus príobháideacht {#encryption}

Tá do theachtaireachtaí díreacha criptithe ó cheann go ceann: ní féidir ach leatsa agus leis an duine eile iad a léamh. Ní fheiceann athsheoltóir cé dó an paicéad ach mar leid 1 bheart.

Tá cainéil criptithe le heochair roinnte, mar sin is iad na daoine a bhfuil an eochair sin acu a fhéadann iad a léamh:

- **Public**: tá sé socraithe ar gach compánach. Tá a eochair foilsithe, mar sin is féidir le duine ar bith é a léamh.
- **Cainéil haischlibe**, ar nós `#utrecht`: faigheann siad a n-eochair óna n-ainm. Is féidir le duine ar bith a bhfuil an t-ainm ar eolas aige dul isteach iontu, mar sin caith leo mar chainéil phoiblí freisin.
- **Cainéil phríobháideacha**: úsáideann siad eochair randamach a roinneann tú féin, mar shampla mar chód QR.

Tá fógraí sínithe ach níl siad criptithe. Feiceann gach duine laistigh de raon ainm do nóid, agus a shuíomh má roinneann tú é. Roghnaigh ainm nach ndeir níos mó ná mar is mian leat.

## An banda 868 MHz san Eoraip {#band}

San Eoraip, úsáideann MeshCore cuid bheag den bhanda 868 MHz atá ar fáil do chách gan cheadúnas. Tá a réamhshocrú raidió Eorpach, EU/UK (Narrow), ar 869.618 MHz ar chainéal 62.5 kHz. Tá sé sin laistigh den fhobhanda 869.40-869.65 MHz, a cheadaíonn suas le 500 mW e.r.p. Ní fhéadann gléas seoladh ansin ach ar feadh 10% den am ar a mhéad. Tá na sonraí agus na teorainneacha in aghaidh na tíre sa [chuid dhlíthiúil den treoir athsheoltóra](/repeater-guide/#legal).

Úsáideann gach duine i gceantar an réamhshocrú céanna, nó ní chloiseann a gcuid raidiónna a chéile. Úsáideann roinnt tíortha agus réigiún leagan eile: tá a fhios ag do [ghrúpa áitiúil](/community/) cén ceann.

## Cad chuige a n-úsáideann daoine é {#uses}

- Fanacht i dteagmháil ar shiúlóidí, ar an bhfarraige agus ag féilte, áit a bhfuil an líonra móibíleach faoi bhrú rómhór nó nach bhfuil sé ann.
- Cainéal cúltaca do theaghlach nó do chomharsana nuair a theipeann ar an leictreachas nó ar na líonraí móibíleacha.
- Comhrá áitiúil ar raidiónna ar leis na daoine féin iad.
- Láthair iargúlta a sheiceáil ón mbaile. Tuairiscíonn athsheoltóirí agus nóid braiteora voltas a gceallraí agus léamha eile nuair a iarrann tú orthu é.
- Súil a choinneáil ar bhraiteoir. Ritheann nód braiteora firmware de chuid MeshCore chun rudaí a thomhas. Coinníonn sé stair a chuid léamha. Má liostálann tú, tugann sé foláireamh duit, mar shampla nuair a bhíonn a cheallra ag éirí lag.
- Rud éigin i bhfad uait a lasadh nó a mhúchadh, ar nós caidéil. Cuireann tú é sin leis an bhfirmware braiteora le do chód féin.
- Turgnaimh a dhéanamh le raidió, aeróga, cumhacht na gréine agus bogearraí foinse oscailte.

## Cá as a dtagann na sonraí {#data}

Aimsíonn an cuardach ar leathanach [na ngrúpaí áitiúla](/community/) áit le cóip de liostaí saora áiteanna agus cód poist [GeoNames](https://www.geonames.org/), faoi cheadúnas [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Tá an chóip ar an suíomh seo. Ní fhágann do chuardach do ghléas riamh, agus ní théann aon iarratas chuig GeoNames.
