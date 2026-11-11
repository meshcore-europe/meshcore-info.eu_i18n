---
title: Cad é MeshCore?
lead: Seolann MeshCore teachtaireachtaí téacs thar raidió, ó nód go nód. Oibríonn sé gan an t-idirlíon agus gan síntiús.
description: 'Cad is MeshCore ann agus cad nach ea: cineálacha nód, ródú, criptiú agus an banda 868 MHz.'
eyebrow: MeshCore v1.18.0
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '70b86ac3'
  seeded: '2026-11-11'
  fields: {title: '06eda66b', lead: 'c0174569', description: 'c2255f49', eyebrow: '8610c822'}
  sections: ['aa768ac3', '9e1e2d85', '0a55792c', 'c3de803d', '493b444f', '429f699c', 'f8008f48', 'd516c212', '0894fe81']
  blocks: ['c3c9c568', '55e4248c', 'c0324d05', 'b20e61c3', 'b7b981e6', '68ed3005', 'cabeb32d', 'b2ca68ba', '681d55b9', 'd1df283f', '0d0e2a8b', '0596f602', 'eec63bed', '183a79e4', '47910535', 'd5a92bbf', 'b44d4637', '431021a0', '83c03732', 'e908ca85', '8f79fbf9', '3323d83e', '857c37dc', '0c4d0dd2', 'bd238f09', '794792be', '5d796ffb', '1a490368', 'f0dd237f', '053d85bc', '02f1fe2f', 'e6b5b258']
---

Bogearraí saora do raidiónna beaga LoRa is ea MeshCore. Teicníc raidió is ea LoRa a sheolann beagán sonraí i bhfad, ar fhíorbheagán cumhachta. Tugtar *nód* ar raidió a bhfuil MeshCore air. Nuair a nascann tú é leis an aip ar do ghuthán nó ar do ríomhaire glúine, nó nuair a úsáideann tú a scáileán agus a mhéarchlár féin, seolann tú téacs chuig daoine atá ciliméadair uait. Níl aon túr, ródaire ná soláthraí sa lár.

Bogearraí foinse oscailte atá iontu. Forbraítear iad ag [meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore) faoin gceadúnas MIT.

## Cad nach bhfuil i MeshCore {#not}

An bhfuil raidió nua duit? Seo na rudaí is minice a mbíonn daoine ag súil leo ó MeshCore, agus nach ndéanann sé.

- **Ní hé an t-idirlíon ná guthán atá ann.** Seolann MeshCore teachtaireachtaí gearra téacs, thart ar fhad teachtaireachta téacs ar do ghuthán. Níl glór, grianghraif, físeáin ná suíomhanna gréasáin ann, agus ní féidir leat gnáthuimhir ghutháin a shroicheadh.
- **Ní seirbhís éigeandála atá ann.** Ní gheallann aon seirbhís éigeandála go n-éistfidh sí ar an mogalra. Tá a fhios againn gur féidir leis an mogalra oibriú. Níl a fhios ag aon duine an oibreoidh sé in éigeandáil.
- **Níl sé láithreach, agus níl sé i ngach áit.** Léimeann teachtaireacht ó raidió go raidió. D'fhéadfadh sí cúpla soicind a thógáil, nó gan teacht ar chor ar bith. Braitheann sé ar na hathsheoltóirí timpeall ort an dtéann sí tríd. Braitheann sé freisin ar airde, ar fhoirgnimh agus ar d'aeróg. Is minic nach sroicheann raidió beag istigh duine ar bith; is féidir le hathsheoltóir ar dhíon ciliméadair a shroicheadh.
- **Ní seirbhís í a chuireann duine éigin ar fáil duit.** Níl soláthraí, deasc chabhrach ná gealltanas clúdaigh ann. Tá an mogalra ann san áit ar chuir daoine ón bpobal athsheoltóirí in airde.
- **Níl gach rud air príobháideach.** Tá teachtaireachtaí díreacha criptithe. Ach is féidir le duine ar bith Public agus na cainéil haischlibe a léamh. Feiceann gach duine laistigh de raon ainm do nóid agus an suíomh a roinneann tú. Tuairiscíonn [breathnóirí](/network/) an méid a chloiseann siad do léarscáileanna poiblí. Míníonn an [chuid faoi chriptiú](#encryption) cad a fhanann príobháideach.
- **Níl sé gan teorainn.** Roinneann gach duine i gceantar cainéal raidió amháin. Cuireann na rialacha don [bhanda 868 MHz](#band) teorainn le cé chomh fada is féidir le gach raidió seoladh. Tógann gach teachtaireacht am craolta ó gach duine eile. Mar sin cuireann botanna, fógraí minice agus teachtaireachtaí tástála moill ar an mogalra do chách.
- **Ní Meshtastic atá ann.** Córas eile is ea Meshtastic a oibríonn ar na boird chéanna, nach mór. Ní féidir leis an dá chóras labhairt le chéile.

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

- Teagmháil a choinneáil ar shiúlóidí, ar muir agus ag féilte, áit a bhfuil an líonra soghluaiste
  faoi bhrú nó as láthair.
- Cainéal cúltaca do theaghlach nó do chomharsana nuair a theipeann ar an gcumhacht nó ar na
  líonraí soghluaiste.
- Cúltaca d'údaráis áitiúla nuair a theipeann ar a ngnáthlíonraí.
- Comhrá áitiúil ar raidiónna ar le daoine féin iad.
- Foireann chuardaigh agus tarrthála a choinneáil i dteagmháil áit nach bhfuil líonra soghluaiste.
  Cuireann MeshCore SAR, aip phobail ar [Thionscadail](/projects/), léarscáileanna agus
  suíomhanna roinnte leis.
- Suíomh iargúlta a sheiceáil ón mbaile. Tuairiscíonn athsheoltóirí agus nóid bhraiteora
  voltas a gceallraí agus léamha eile nuair a iarrann tú orthu.
- Faire ar bhraiteoir. Ritheann nód braiteora dochtearraí MeshCore le haghaidh tomhais.
  Coinníonn sé stair voltas a cheallraí. Logáil isteach mar riarthóir agus tugann sé
  rabhadh duit nuair a bhíonn an ceallra ag éirí íseal. Cuireann tú rabhaidh do léamha eile
  leis le do chód féin.
- Rud éigin i bhfad uait a chasadh air nó as, caidéal mar shampla. Cuireann tú é sin le
  dochtearraí an bhraiteora le do chód féin.
- Turgnamh a dhéanamh le raidió, aeróga, cumhacht na gréine agus bogearraí foinse oscailte.

Tá roinnt údarás ag tógáil nó ag tástáil cúltaca bunaithe ar MeshCore. Sheiceálamar
na samplaí seo i mí na Samhna 2026.

- Ghearr Cioclón Gabrielle gach cumarsáid in Tairāwhiti, sa Nua-Shéalainn. I
  Meán Fómhair 2025, d'ainmnigh bainistíocht éigeandála an réigiúin MeshCore mar
  [cheann de 6 bhealach cúltaca ar a laghad le cumarsáid a dhéanamh](https://www.scoop.co.nz/stories/AK2509/S00669.htm).
  Bhí sí ag tógáil athsheoltóirí gréine mar chnámh droma freisin.
- Tá ceantar Bad Kissingen sa Ghearmáin
  [ag tógáil líonra téacs ar MeshCore](https://www.landkreis-badkissingen.de/wirtschaft/digitalisierung/kommunikationsnetze/index.html)
  d'údaráis, do sheirbhísí éigeandála agus do láithreacha criticiúla. Is iad na
  stáisiúin dóiteáin a nascann ar dtús.
- Vótáil comhairle Hilversum, san Ísiltír,
  [34 in aghaidh 1 ar son trialach](https://hilversum.nl/nieuwsoverzicht/gemeenteraad-buigt-zich-over-financien)
  le hathsheoltóir ar thúr halla an bhaile. Déanfaidh an bardas
  [measúnú air i bhfómhar 2027](https://www.spreekbuis.nl/hilversum-start-proef-met-onafhankelijk-noodcommunicatienetwerk-meshcore/).
- Tá dhá réigiún sábháilteachta san Ísiltír, a eagraíonn an fhreagairt ar ghéarchéim,
  ag déanamh turgnaimh le MeshCore:
  [Limburg Theas](https://nos.nl/nieuwsuur/artikel/2607176-communicatie-hulpdiensten-valt-uit-bij-lange-stroomstoring-oplossing-niet-in-zicht)
  agus [Drenthe](https://www.rtvdrenthe.nl/nieuws/18438486/hackerspace-drenthe-werkt-aan-een-noodnetwerk-voor-de-provincie).
  Deir Drenthe go bhfuil sé ró-luath le rá conas nó cathain a d'fhéadfadh an réigiún é a úsáid.
- In Dalfsen, san Ísiltír freisin, tá oibrithe deonacha
  [ag reáchtáil píolóta in éineacht leis na bardais](https://noodnetoverijssel.nl/).
  Úsáideann siad raidió gutha ar dtús, agus MeshCore mar dhara sraith le haghaidh téacs.

Níl a fhios ag aon duine an oibreoidh an mogalra in aice leat in éigeandáil.

## Cá as a dtagann na sonraí {#data}

Aimsíonn an cuardach ar leathanach [na ngrúpaí áitiúla](/community/) áit le cóip de liostaí saora áiteanna agus cód poist [GeoNames](https://www.geonames.org/), faoi cheadúnas [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Tá an chóip ar an suíomh seo. Ní fhágann do chuardach do ghléas riamh, agus ní théann aon iarratas chuig GeoNames.
