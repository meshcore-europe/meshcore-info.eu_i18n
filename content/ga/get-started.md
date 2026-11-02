---
title: Cuir tús leis
lead: Ó chlár nua go dtí do chéad teachtaireacht ar an mogalra. Tá clár LoRa, ríomhaire le Chrome nó Edge, agus fón nó ríomhaire glúine don aip de dhíth ort.
description: Lódáil MeshCore ó do bhrabhsálaí, péireáil an aip, roghnaigh an réamhshocrú raidió a úsáidtear i do cheantar, seol do chéad teachtaireacht agus téigh isteach i do chainéal áitiúil.
eyebrow: 6 chéim · MeshCore v1.18.0
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'f97ca1b9'
  seeded: '2026-11-02'
  fields: {title: '61e8d44a', lead: '45b0e5c3', description: 'cf031b18', eyebrow: '4fa6fe1e'}
  sections: ['16c3728c', '203acaa5', 'df7a1665', '6da9fd7a', 'cb5fb72e', 'a1cf8b26', 'a419ce79', '66d00206']
  blocks: ['16c3728c', '2a70a7ed', '6f8e6f5f', '16c11d47', '081db416', 'd5e7fd0b', '6d28c323', 'eb2ea361', 'de50125c', 'ae20cb8e', 'abd42710', 'c08a865a', '7d1eb0b9', '263e0c96', '0903299f', 'eba20370', '5cdc20cf', '7f542f82', '802ca5a8', '1a854187', 'bc333adf', 'f25b16fa', '7c893ae2', '7f5927b4', '26e13713', '39a142cf', 'a786620c', '216897fa', '2d222782', 'a9755900', 'f081b357']
---

Tá na céimeanna seo bunaithe ar fhirmware MeshCore v1.18.0 agus ar uirlisí oifigiúla
Dheireadh Fómhair 2026. D'fhéadfadh ainmneacha na roghchlár san aip a bheith beagán difriúil ó leagan go leagan.

## 1. Roghnaigh gléas {#device}

Oibreoidh aon chlár ar [leathanach na ngléasanna](/devices/) a bhfuil compánach luaite leis. Do do
chéad nód, roghnaigh *compánach*: an raidió óna seolann tú teachtaireachtaí. Péireáil é le
d'fhón nó le do ríomhaire glúine trí Bluetooth nó USB, nó roghnaigh ceann a bhfuil a scáileán
agus a mhéarchlár féin aige agus a oibríonn as féin.

Faigh an leagan 868 MHz. Déanann an aeróg a thagann leis an gnó; taispeánann an
[treoir aeróige](/guides/antenna/) duit conas ceann a sheiceáil.

{{< callout type="warning" >}}
Ceangail an aeróg sula gcuireann tú an raidió ar siúl. Má tharchuireann raidió LoRa gan aeróg,
féadfaidh sé damáiste a dhéanamh dá shlis féin.
{{< /callout >}}

## 2. Lódáil an firmware {#flash}

1. Ceangail an gléas le do ríomhaire le cábla sonraí USB.
2. Oscail an uirlis lódála gréasáin ag [flasher.meshcore.io](https://flasher.meshcore.io)
   i Chrome nó Edge. Úsáideann sí Web Serial, rud nach bhfuil ag brabhsálaithe eile.
3. Roghnaigh do ghléas, ansin an firmware **Companion** le haghaidh **Bluetooth** (nó
   USB, mura n-úsáidfidh tú é ach le cábla ríomhaire).
4. Lódáil é. Téann roinnt clár isteach i mód nuashonraithe ar dtús; insíonn an uirlis lódála duit
   conas é sin a dhéanamh.

Ná húsáid *erase* ach le tosú as an nua: scriosann sé céannacht an ghléis agus do
theagmhálaithe. Le haghaidh nuashonruithe níos déanaí, lódáil gan scriosadh. Chun do chéannacht a
choinneáil tar éis scriosta, easpórtáil eochair phríobháideach do chompánaigh ón aip ar dtús
agus iompórtáil í ina dhiaidh sin.

## 3. Suiteáil an aip {#app}

Tá aip oifigiúil MeshCore ar fáil do Android, iOS, Windows agus macOS;
tá nasc chuig gach leagan ar [meshcore.io](https://meshcore.io). Tá aip ghréasáin ann freisin ag
[app.meshcore.nz](https://app.meshcore.nz) a ritheann i Chrome nó Edge ar ríomhaire.

## 4. Péireáil do nód {#pair}

Cuir do nód ar siúl, oscail an aip agus ceangail leis trí Bluetooth. Nuair a iarrtar
PIN ort:

- taispeánann nód **le** scáileán PIN; clóscríobh an ceann sin;
- úsáideann nód **gan** scáileán `123456`.

Má theipeann ar an bpéireáil, bain an gléas as socruithe Bluetooth d'fhóin agus bain triail eile
as. Ansin tabhair ainm do do nód. Feiceann daoine eile an t-ainm seo, mar sin ná húsáid d'ainm
iomlán ná do sheoladh mura dteastaíonn sin uait.

## 5. Roghnaigh réamhshocrú raidió do cheantair {#preset}

Úsáideann gach raidió i gceantar an mhinicíocht agus na socruithe céanna, nó ní chloiseann siad
a chéile. I socruithe raidió na haipe, roghnaigh an réamhshocrú a úsáidtear i do cheantar.
Lasmuigh de na ceantair thíos, úsáidtear **EU/UK (Narrow)** san Eoraip. Tá a réamhshocrú féin ag an
Ísiltír, ag an tSeicia, ag an Ungáir, ag an tSlóvaic, ag an bPortaingéil agus ag an Eilvéis, agus
tá leagan eile ag Limburg san Ísiltír:

{{< presets >}}

Nach bhfuil réamhshocrú do cheantair ar fáil ar do ghléas? Cuir na 4 luach ón tábla isteach de láimh
i socruithe raidió na haipe: minicíocht, bandaleithead, fachtóir scaipthe agus ráta códaithe.
Ní chloiseann nód le luachanna eile an mogalra.

Níl tú cinnte? Tá a fhios ag do [ghrúpa áitiúil](/community/) cén réamhshocrú a úsáidtear i do cheantar.
Íoslódálann an aip an liosta seo ó thionscadal MeshCore, mar sin ní gá an aip a nuashonrú
do réamhshocrú nua.

## 6. Abair heileo {#hello}

1. **Fógair thú féin.** Seol *fógra* ón aip. Taistealaíonn fógra "flood" trí na hathsheoltóirí
   (nóid a chuireann teachtaireachtaí ar aghaidh), ionas gur féidir le gach duine ar an mogalra tú a chur leis.
   Ní fhógraíonn compánaigh iad féin go huathoibríoch riamh.
2. **Aimsigh daoine eile.** Nochtann daoine i do theagmhálaithe chomh luath agus a shroicheann a
   bhfógraí thú. Seolann athsheoltóirí fógra "flood" gach 47 uair an chloig de réir réamhshocraithe,
   mar sin d'fhéadfadh sé 2 lá a thógáil ar do liosta líonadh.
3. **Seol teachtaireacht.** Oscail teagmhálaí agus scríobh. Scaipeann an chéad teachtaireacht ar
   fud an líonra; cuireann an faighteoir in iúl ar ais cén bealach a ghlac sí, agus leanann
   teachtaireachtaí níos déanaí an bealach sin.
4. **Téigh isteach i gcainéil.** Tá an cainéal **Public** socraithe cheana; sroicheann gach rud a
   scríobhann tú ansin gach duine ar an mogalra. Cuir *cainéal haischlibe* do réigiúin leis (ainm a
   thosaíonn le `#`) trína ainm a chlóscríobh. Inseoidh do [ghrúpa áitiúil](/community/) duit cé
   na cainéil atá gníomhach.

## Nuair nach n-oibríonn rud éigin {#troubleshooting}

**Ní aimsíonn an aip mo ghléas trí Bluetooth.**
Is dócha gur lódáil tú an compánach USB. Lódáil arís agus roghnaigh an leagan Bluetooth.
Ar an Heltec V3, tá raon gearr ag an aeróg bheag Bluetooth ionsuite; coinnigh an fón gar dó.

**Teipeann ar an bpéireáil i gcónaí.**
Bain an gléas as socruithe Bluetooth d'fhóin, atosaigh Bluetooth, agus péireáil arís leis an
PIN ar an scáileán nó le `123456`.

**Níl aon duine i mo theagmhálaithe.**
Seiceáil go bhfuil do réamhshocrú ag teacht le do cheantar. Seol fógra "flood". Mura bhfuil
athsheoltóir ar bith laistigh de raon, ní chloisfidh tú ach raidiónna atá gar duit; taispeánann
[leathanach na léarscáile](/map/) cá bhfuil athsheoltóirí.

**Taispeánann teagmhálaí "last seen" laethanta ó shin cé go bhfuil sé gníomhach.**
Tá an t-am mícheart ar cheann den dá nód. Faigheann compánach an t-am ó d'fhón; caithfidh a
n-úinéir an t-am a shocrú ar athsheoltóirí agus ar fhreastalaithe seomra (nóid a stórálann
teachtaireachtaí do ghrúpa).

**Ní thagann teachtaireacht dhíreach riamh.**
Caithfidh an duine eile a bheith agat mar theagmhálaí, agus tusa ag an duine sin. Caitheann nód
amach teachtaireacht ó dhuine nach n-aithníonn sé, gan é sin a insint don seoltóir. Seol fógra
"flood" agus iarr ar an duine eile ceann a sheoladh freisin. Seiceáil san aip go gcuireann sí
teagmhálaithe nua leis go huathoibríoch; ní chuireann sí leis ach nóid laistigh dá teorainn léimeanna.

**Oibríonn seanteagmhálaithe, ach ní cheanglaíonn cinn nua riamh.**
Scaipeann an chéad teachtaireacht ar fud an líonra, agus ní chuireann athsheoltóir ar aghaidh í
ach amháin má tá réigiún na teachtaireachta aige. Leanann teachtaireachtaí níos déanaí bealach
foghlamtha, agus ní chuireann seiceáil réigiúin stop leis sin. Fiafraigh de do
[ghrúpa áitiúil](/community/) cé na réigiúin atá ag na hathsheoltóirí timpeall ort, agus seiceáil
[na socruithe do do cheantar](/guides/settings/#traffic).

**Ní cheanglaíonn an aip le do chompánach a thuilleadh.**
Tá cnaipe úsáideora ar roinnt clár, mar shampla roinnt clár RAK agus an Heltec T114.
Coinnigh brúite é sna chéad 8 soicind tar éis don chlár tosú. Osclaíonn an compánach consól
tarrthála trí USB. Sa chonsól ar [flasher.meshcore.io](https://flasher.meshcore.io), socraíonn
`set pin <pin>` PIN Bluetooth nua agus glanann `erase` an gléas.

**Ní féidir leis an uirlis lódála an port sraitheach a oscailt ar Linux.**
Teastaíonn rochtain ar an bport ó d'úsáideoir, mar shampla
`sudo setfacl -m u:$USER:rw /dev/ttyUSB0`, nó ballraíocht sa ghrúpa `dialout`.

**Rud éigin eile.** Clúdaíonn
[MeshCore FAQ](https://github.com/meshcore-dev/MeshCore/blob/main/docs/faq.md)
go leor fadhbanna eile.
