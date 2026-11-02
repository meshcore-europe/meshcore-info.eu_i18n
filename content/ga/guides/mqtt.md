---
title: MQTT ar do bhreathnóir
lead: Lig do d'athsheoltóir an méid a chloiseann sé a thuairisciú don MeshCore Analyzer thar Wi-Fi. Leanann sé air ag cur teachtaireachtaí ar aghaidh mar a rinne sé roimhe seo.
description: Déan breathnóir MeshCore d'athsheoltóir ESP32 le dochtearraí breathnóra DMC. Flaiseáil iad, socraigh Wi-Fi agus do chód aerfoirt, roghnaigh na bróicéirí agus deimhnigh go dtuairiscíonn an nód don MeshCore Analyzer.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '7b9a9320'
  seeded: '2026-11-02'
  fields: {title: '62626d0f', lead: 'fe9653d4', description: '739edb74'}
  sections: ['962bdbc4', '0ccd4a85', 'fc57f65c', 'ef841ae5', '77d109c5', 'b3e4f8d2', '602a1021']
  blocks: ['75461763', '0e0db0ff', '231a92ad', '49ad02ce', '19b33688', '01e79e69', '6f184c96', '75da543a', '966b1e87', '11f22f4c', '5f85ac9b', 'f74cb809', '1a70c3f5', '9cadc611', '5261e7e9', 'c998ea2d', '393339d9', '803a2dc4', 'cedf8d28', '7c222cec', '6bc50a6a', '59f2a96c', 'a8bd6037', '0d3b84ff', 'e43d5a74', '3bd6439c', '2ddd9432', 'd9df877b', '3283886d', 'f6131e02', '99dc83fb']
---

Nód is ea breathnóir a thuairiscíonn freisin an méid a chloiseann sé thar MQTT, trí Wi-Fi. Taispeánann gach breathnóir beagán níos mó den mhogalra ar an
[MeshCore Analyzer](https://meshcore-analyzer.eu/) agus ar na
[léarscáileanna clúdaigh](/map/). Leis an treoir seo, déanfaidh tú breathnóir d'athsheoltóir (nód a chuireann teachtaireachtaí ar aghaidh). Leanann sé air ag athsheoladh, agus téann an tuairisc i dtreo amháin: ní thagann aon rud ar ais ar an mogalra.

{{< callout type="warning" >}}
Is do **dhochtearraí breathnóra DMC** an treoir seo, is é sin leagan breathnóra
[Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore), atá bunaithe ar
MeshCore 1.18.0. Níl MQTT i MeshCore caighdeánach. Tagann gach ordú thíos ó chód foinseach na ndochtearraí, leagan `32dd8ad` ón 19 Deireadh Fómhair 2026.
{{< /callout >}}

## An méid a theastaíonn uait {#need}

- Clár ESP32 le Wi-Fi, mar shampla Heltec V3 nó V4, LilyGo T3S3 nó Xiao S3. Tá liosta de gach clár san
  [eisiúint](https://github.com/Dutch-MeshCore/MeshCore/releases/tag/observer-mqtt-dev).
  Níl Wi-Fi ar chláir nRF52 ar nós an RAK4631.
- Líonra Wi-Fi 2.4 GHz san áit a bhfuil an clár.
- Cábla sonraí USB, agus Chrome, Edge nó Opera ar do ríomhaire.
- Cód an aerfoirt is gaire do do nód, 3 litir ar nós `AMS` nó `BRU`.
  Insíonn sé do na bróicéirí (na freastalaithe a fhaigheann do thuairiscí) cén ceantar ina bhfuil do bhreathnóir.

Níl Wi-Fi san áit a bhfuil d'athsheoltóir, ach tá ríomhaire in aice leis?
[Cruthaigh cumraíocht droichid](/guides/mctomqtt/) ina ionad sin.

## Flaiseáil na dochtearraí {#flash}

Níl ach MeshCore caighdeánach ar an [bhflaiseálaí](/firmware/flasher/) atá ar an suíomh seo.
Faigheann tú dochtearraí an bhreathnóra ón bhflaiseálaí sa
[DutchMeshCore Toolbox](https://toolbox.dutchmeshcore.nl/):

1. Roghnaigh do chlár, agus ansin **DutchMeshCore MQTT** (Repeater + Observer + MQTT).
2. Roghnaigh **Full flash** an chéad uair: cuireann sé rud nua in áit gach ruda ar an gclár, tábla na ndeighiltí san áireamh. Coinníonn nuashonrú na haipe a bhfuil ann cheana, agus is do nuashonruithe níos déanaí é.
3. Socraigh d'athsheoltóir mar is gnách: ainm, réamhshocrú raidió agus pasfhocal riaracháin, mar atá sa
   [treoir athsheoltóra](/repeater-guide/#config).

Is é seo an leagan **dev** de na dochtearraí, agus nuashonraíonn sé é féin ón gcainéal dev nuair a chlóscríobhann tú `ota update`. Tá 1.17.1 fós ar an gcainéal cobhsaí, mar sin fan ar dev don treoir seo.

## Socruithe {#settings}

Oscail an [consól sraitheach](/firmware/console/) ar an suíomh seo agus ceangail do chlár. Cuir isteach do líonra Wi-Fi, do phasfhocal agus do chód aerfoirt féin, agus ansin greamaigh na línte seo ceann ar cheann:

```text
set wifi.ssid MyNetwork
set wifi.pwd MyPassword
set mqtt.iata AMS
reboot
```

Tar éis an atosaithe, ceanglaíonn an clár le do Wi-Fi agus socraíonn sé a chlog ón idirlíon. Teastaíonn an clog sin ó na bróicéirí chun céannacht do bhreathnóra a sheiceáil. Gan cód aerfoirt, ní thuairiscítear aon rud.

Arbh fhearr leat cliceáil ná clóscríobh? Osclaíonn `start webconfig` leathanach socruithe ar an gclár, ag an seoladh a thaispeánann an consól. Logáil isteach le do phasfhocal riaracháin.

## Sliotáin bróicéara {#brokers}

Tá bróicéir amháin i ngach sliotán. Ar dtús, tá na sliotáin seo líonta sna dochtearraí:

| Sliotán | Bróicéir | Á reáchtáil ag |
| --- | --- | --- |
| 1 | `dutchmeshcore-1` | Dutch-MeshCore |
| 2 | `dutchmeshcore-2` | Dutch-MeshCore |
| 3 | `meshcore-analyzer-eu` | MeshCore Analyzer |

Tá 3 shliotán ag clár gan chuimhne bhreise (PSRAM), ar nós an Heltec V3. Ceanglaíonn sé le 2 acu ag an am céanna, mar sin ní cheanglaíonn an Analyzer i sliotán 3 choíche.
Bog go sliotán 1 é:

```text
set mqtt3.preset none
set mqtt1.preset meshcore-analyzer-eu
```

Tá 6 shliotán ag clár le PSRAM, ar nós an Heltec V4, agus ceanglaíonn sé le 5 acu ag an am céanna. Ní theastaíonn aon athrú uaidh.

Logálann do nód isteach i ngach bróicéir lena eochair féin, mar sin ní theastaíonn cuntas uait.
Liostaíonn `get mqtt.presets` na bróicéirí pobail eile a bhfuil eolas ag na dochtearraí orthu.

### Do bhróicéir féin {#own}

Cuir do bhróicéir féin i sliotán saor. Cuir isteach a sheoladh, a phort, an t-ainm úsáideora agus an pasfhocal. Ar chlár le PSRAM, tá sliotán 4 saor:

```text
set mqtt4.preset custom
set mqtt4.server mqtt.example.org
set mqtt4.port 1883
set mqtt4.username my_username
set mqtt4.password my_password
```

Ar chlár gan PSRAM, úsáid sliotán 2 ina ionad: cuir `mqtt2` in áit `mqtt4`.
Beidh do bhróicéir ansin in áit `dutchmeshcore-2`.

Ceanglaíonn port `8883` go criptithe (TLS), port `443` go criptithe thar cheangal gréasáin (websocket), agus aon phort eile gan chriptiú. Is féidir leat an seoladh iomlán a thabhairt freisin, mar shampla `wss://mqtt.example.org:9002/mqtt`; sa chás sin, ní bhaineann riail an phoirt leis.

## Seiceáil go n-oibríonn sé {#check}

Clóscríobh `get mqtt.status`. Taispeánann gach sliotán a staid:

```text
> msgs: on, 1: meshcore-analyzer-eu (ok), 2: dutchmeshcore-2 (ok), q:0
```

- `ok`: ceangailte.
- `wait`: tá socrú in easnamh ar an sliotán, ar nós an chóid aerfoirt.
- `disc`: gan cheangal fós. Seiceáil do Wi-Fi le `get wifi.status`.
- `fail`: theip ar an sliotán 7 n-uaire as a chéile, thar thart ar 20 nóiméad, agus anois déanann sé iarracht uair amháin gach 30 nóiméad. Seiceáil seoladh an bhróicéara agus na sonraí logála isteach.
- `inactive`: níl spás ar an gclár don sliotán seo. Féach
  [Sliotáin bróicéara](#brokers).

Ansin, lorg ainm d'athsheoltóra ar
[leathanach breathnóirí an Analyzer](https://meshcore-analyzer.eu/#observers).
Beidh sé le feiceáil laistigh de 5 nóiméad, mar aon leis an méid a chuala sé.
