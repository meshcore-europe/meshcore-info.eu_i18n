---
title: Canllaw ailadroddyddion
lead: Mae ailadroddydd mewn man uchel yn anfon negeseuon ymlaen i bawb o'i gwmpas, ar draws tref neu ddyffryn cyfan. Dewisa safle, rho bŵer iddo o'r haul, gosoda fe a chadwa o fewn y gyfraith.
description: 'Cynllunia, pwera, ffurfweddu a defnyddia ailadroddydd MeshCore yn gyfreithlon yn Ewrop: dewis safle, maint system solar, gosodiadau CLI, a therfynau pŵer a chylchred gwaith 868 MHz.'
eyebrow: 868 MHz · hyd at 500 mW · heb drwydded
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '3e38a8c6'
  seeded: '2026-11-04'
  fields: {title: '4608abcd', lead: 'bc670c65', description: '9e483ce5', eyebrow: '9fd33416'}
  sections: ['05ee477a', '938c518c', '824ab38e', '662ea23c', '70faf508', '8bc641aa', '399cd683', 'e9dedb7b', '92beca03', '17634750', 'cadf6024', 'e9cc6834', '2e6e59ca', 'fb44b8db']
  blocks: ['20ac0371', 'ed2b1adf', '432543ee', '7af42c89', 'd0f7543a', '9ef3580f', '3476aef7', '1bab7bec', 'bbea9a0c', '2b9fab3b', 'b13d1947', 'c2bad16f', '636edc86', 'c2d6bcd1', '957ae975', '98874949', '96d1ebad', 'dbd9fa1f', 'aa06d32b', '9958aad3', 'd162b028', 'cca1bbdf', '64ef011d', 'e7f16724', 'd2e34ff0', 'bb195cfc', '8d080bb3', '2b1d995b', '210f1b66', 'dc7419d2', 'bdc66db0', 'b59f248c', '7184bd63', 'de5a24f9', 'f5cfb426', '48c7422f', '9d3c0836', 'da8a6af3', '240126df', '8aac2b33', '81a475b8', 'a53e42b5', '36ff1db4', 'e4ca8602', 'e4594afd', '3b24b8e9', '58330858', '68f2966e', 'd7418228', '23536e60', 'cbc5c2d1', '2ea02ba9', '92540256', '6e21f681', 'a8c12311', '3382ae7f', 'cdeafb0f', '1b1319d2']
---

Ailadroddyddion sy'n cynnal y rhwydwaith mesh. Dydy cymdeithion (companions), y radios rwyt ti'n anfon negeseuon ohonyn nhw, ddim yn anfon negeseuon ymlaen. Heb ailadroddyddion, dim ond pobl o fewn amrediad uniongyrchol y gelli di eu cyrraedd. Mae ailadroddydd yn y lle iawn yn ymestyn y mesh i bawb o'i gwmpas. Mae'r canllaw hwn yn dilyn cadarnwedd MeshCore v1.18.0.

Cyn dechrau, siarada â'th [grŵp lleol](/community/). Maen nhw'n gwybod ble mae bylchau yn y ddarpariaeth, pa [ragosodiad mae dy ardal yn ei ddefnyddio](/guides/settings/) a sut i enwi ailadroddyddion. Edrycha ar y [mapiau darpariaeth](/map/) i weld ailadroddyddion yn dy ymyl, a dweda helo ar y [sianeli](/guides/channels/) cyhoeddus neu leol.

## Oes angen un arnat ti? {#need}

Mae ailadroddydd yn anfon ymlaen bob neges orlif (flood) mae'n ei chlywed, ac mae pob ailadroddydd o fewn cyrraedd yn rhannu'r un amser ar yr awyr. Lle mae'r mesh yn dy gyrraedd di'n barod, mae ailadroddydd arall yn ychwanegu traffig, nid darpariaeth. Gall cydymaith mewn man uchel, wrth ffenest atig neu ar falconi, fod yn ddigon i ti.

Gosoda ailadroddydd lle mae bwlch yn y ddarpariaeth:

- dydy'r [mapiau darpariaeth](/map/) ddim yn dangos ailadroddydd yn dy ymyl, neu dim ond rhai nad yw dy gydymaith yn eu clywed;
- mae dy grŵp lleol yn dweud bod angen un ar yr ardal.

## Dewis safle {#site}

Mae uchder yn bwysicach na phŵer. Mae LoRa ar 868 MHz yn teithio orau ar hyd llinell welediad glir. Mae bryniau, adeiladau a choed trwchus yn costio llawer mwy o gyrhaeddiad nag y mae ychydig o filiwatiau ychwanegol yn ei ennill yn ôl.

- **Dos yn uchel.** Mae to, mast, adeilad tal neu fryn yn cwmpasu llawer mwy na sil ffenest. Mae hyd yn oed ychydig fetrau uwchben y toeau o gwmpas yn helpu.
- **Cadwa'r antena yn glir.** Gosoda hi uwchben ymylon y to, i ffwrdd o fetel, cafnau ac antenâu eraill.
- **Gwiria'r olygfa.** Mae offer fel [HeyWhatsThat](https://www.heywhatsthat.com/) yn dangos beth sydd i'w weld o leoliad. Mae ap MeshCore yn [cyfrifo beth y gall ailadroddydd yno ei gyrraedd](#check-site).
- **Gad le clir.** Mae angen gofod rhydd ar lwybr radio o gwmpas y llinell uniongyrchol, nid y llinell ei hun yn unig. Ar 868 MHz, mae'r gofod hwnnw tua 20 m o amgylch canol llwybr 5 km. Dros 20 km, mae tua 40 m.
- **Gofyn am ganiatâd.** Sicrha ganiatâd y perchennog ar gyfer y to neu'r mast, a chytuna sut y byddi di'n cyrraedd yr ailadroddydd i'w gynnal a'i gadw.

### Gwirio safle yn yr ap {#check-site}

Mae gan fersiwn 1.33 neu ddiweddarach o ap MeshCore yr offer hyn o dan **Tools** yn
ei ddewislen. Maen nhw'n gweithio heb radio wedi'i gysylltu.

- Mae **Line of Sight** yn llunio'r tir rhwng 2 bwynt, a'r gofod sydd ei angen ar y
  signal uwch ei ben. Pwysa'n hir ar 2 bwynt ar y map, neu tapia ailadroddyddion.
- Mae **Antenna Coverage** yn dangos ar y map beth all antena ar 1 pwynt ei gyrraedd.
  Pwysa'n hir ar bwynt neu tapia ailadroddydd. Ychwanega ragor o bwyntiau i gymharu safleoedd.

Ar gyfrifiadur, dewisa **Add Point** yn newislen yr offeryn a theipia'r cyfesurynnau.

Mae'r ddau offeryn yn rhoi'r antena ar dy safle ar 5 m i ddechrau, felly gosod
yr uchder rwyt ti'n ei fwriadu yng ngosodiadau'r offeryn. Mae Antenna Coverage yn rhoi antena
derbyn ar 1 m i ddechrau. Heb radio wedi'i gysylltu, mae Line of Sight yn dechrau ar 915 MHz: gosod
amledd dy [ragosodiad](/guides/settings/) yn ei osodiadau.

Mae'r offer yn cyfrifo ar sail data uchder, a dydyn nhw ddim yn profi dy radio. Gwiria goed ac
adeiladau newydd dy hun, yna cer â chydymaith i'r fan a gweld pa
ailadroddyddion mae'n eu clywed.

![Line of Sight yn ap MeshCore: y tir rhwng 2 bwynt, a'r gofod sydd ei angen ar y signal uwch ei ben](/media/guides/line-of-sight.webp)

![Antenna Coverage yn ap MeshCore: yr ardal y gall antena ar fryn ei chyrraedd, ar fap](/media/guides/antenna-coverage.webp)

## Caledwedd {#hardware}

- **Bwrdd.** Dewisa fwrdd nRF52 pŵer isel fel y [Heltec T114](/devices/), RAK WisBlock neu'r SenseCAP Solar Node. Mae byrddau ESP32 yn tynnu mwy o bŵer (mae'r dudalen dyfeisiau yn eu marcio'n High), ac mae hynny'n gwneud rhedeg ar ynni solar yn anodd.
- **Antena.** Defnyddia antena wedi'i gwneud ar gyfer 868 MHz, wedi'i gosod yn fertigol. Mae'r [canllaw antenâu](/guides/antenna/) yn trafod mathau, cysylltwyr, cebl a gosod. Mae cynnydd yr antena yn cyfrif tuag at y terfyn pŵer cyfreithiol: edrycha ar [Terfynau cyfreithiol](#legal).
- **Cebl.** Cadwa'r cebl cyfechelog yn fyr, neu defnyddia gebl colled isel. Ar 868 MHz, gall ychydig fetrau o gebl tenau golli hanner dy bŵer.
- **Blwch.** Defnyddia flwch gwrth-dywydd (IP65 neu well) gyda chwarren gebl, twll awyru neu ddraenio rhag anwedd, a lliw golau neu gysgod rhag yr haul. Mae batris yn dioddef mewn gwres, ac alli di ddim eu gwefru o dan y rhewbwynt.
- **Mellt.** Mae antena ar do yn darged. Dilyna'r rheolau lleol ar ddaearu, neu gosoda hi lle na fyddai trawiad yn cyrraedd gwifrau'r adeilad.

## Pŵer a maint y system solar {#power}

Rhaid i ailadroddydd solar oroesi wythnosau tywyllaf y gaeaf. Cynllunia'r maint ar eu cyfer nhw:

1. **Mesura'r llwyth.** Rheda'r ailadroddydd wedi'i ffurfweddu drwy fesurydd pŵer USB am ddiwrnod. Darllena'r ynni a ddefnyddiwyd mewn wat-oriau (Wh). Mae traffig dy ardal yn newid y rhif, felly mesura ar y safle os gelli di.
2. **Ychwanega gronfa wrth gefn.** Cynllunia gapasiti batri ar gyfer o leiaf 5 i 7 diwrnod heb haul defnyddiol.
3. **Ffeindia haul dy aeaf.** Mae [teclyn PVGIS](https://re.jrc.ec.europa.eu/pvg_tools/en/) rhad ac am ddim yr UE yn dangos faint o ynni mae panel yn ei gynhyrchu bob mis, mewn unrhyw leoliad. Defnyddia'r mis â'r lleiaf o haul.
4. **Dewisa faint y panel.** Rhaid i'r panel ailgyflenwi defnydd pob dydd yn y mis gwaethaf hwnnw, gyda lle i golledion gwefru.

Enghraifft wedi'i chyfrifo, gyda rhifau tybiedig: mae angen batri o 7 Wh o leiaf ar ailadroddydd sy'n defnyddio 1 Wh y dydd, ar gyfer wythnos wrth gefn, tua 2 Ah o gapasiti defnyddiadwy ar 3.7 V. Os yw PVGIS yn dweud bod panel 1 W ar dy safle yn rhoi 0.5 Wh y dydd ym mis Rhagfyr, mae angen panel 2 W o leiaf arnat ti. Mae 3 i 5 W yn gadael lle ar gyfer cymylau, eira a heneiddio.

## Ei osod {#config}

**Fflachio.** Defnyddia'r [fflachiwr gwe](https://flasher.meshcore.io) a dewisa'r gadarnwedd **Repeater** ar gyfer dy fwrdd. Edrycha ar [Dechrau arni](/get-started/#flash) am y camau fflachio.

**Ffurfweddu dros USB.** Gyda'r ailadroddydd yn dal wedi'i gysylltu â'th gyfrifiadur, agor [config.meshcore.io](https://config.meshcore.io) neu gonsol y fflachiwr. Gelli di hefyd ddefnyddio unrhyw derfynell gyfresol ar 115200 baud. Y gorchmynion pwysicaf:

| Beth | Gorchymyn |
|---|---|
| Newid cyfrinair y gweinyddwr | `password <new password>` |
| Rhoi enw iddo | `set name <name>` |
| Rhagosodiad radio: amledd, lled band, SF, CR (ailgychwyn i'w roi ar waith) | `set radio 869.618,62.5,8,8` |
| Terfyn cylchred gwaith, mewn y cant | `set dutycycle 10` |
| Pŵer trawsyrru'r sglodyn radio, mewn dBm | `set tx <dBm>` |
| Safle, er mwyn iddo ymddangos ar fapiau | `set lat <degrees>` a `set lon <degrees>` |
| Manylion cyswllt i weithredwyr eraill | `set owner.info <text>` |
| Oriau rhwng hysbysiadau gorlif, y rhai mae'r mesh cyfan yn eu clywed | `set flood.advert.interval <hours>` |
| Ei gyhoeddi nawr | `advert` |
| Ailgychwyn | `reboot` |

Cyfrinair diofyn y gweinyddwr yw `password`, ac mae unrhyw un sy'n mewngofnodi ag ef yn dod yn weinyddwr. Newidia fe cyn i'r ailadroddydd fynd ar yr awyr.

Mae'r enghraifft `set radio` uchod ar gyfer EU/UK (Narrow). Defnyddia werthoedd rhagosodiad dy ardal yn lle hynny: mae [Gosodiadau a argymhellir](/guides/settings/) yn eu rhestru fesul gwlad.

**Gosod y cloc.** Heb fodiwl cloc (RTC), mae ailadroddydd yn colli'r amser bob tro mae'r pŵer yn torri, ac mae'n ailddechrau ym mis Mai 2024. Tra mae'n rhedeg, mae ei gloc hefyd yn drifftio: mae'n mynd fwyfwy ar y blaen neu ar ei hôl hi. Felly gosoda'r cloc bob hyn a hyn: mewngofnoda o bell o'r ap a defnyddia `clock sync`, neu gosoda'r amser dros USB. Gyda modiwl RTC, anaml y bydd angen i ti wneud hyn: mae'n cadw'r amser pan fydd y pŵer yn torri ac yn drifftio llawer llai.

**Ei reoli o bell.** Unwaith y bydd ar y mesh, mewngofnoda o ap MeshCore gyda chyfrinair y gweinyddwr. Yno rwyt ti'n darllen ei statws ac yn defnyddio'r un gorchmynion dros y radio. Dim ond dros USB mae rhai gorchmynion yn gweithio, fel `set freq` a'r ailosodiad ffatri `erase`.

**Cadw ei hunaniaeth.** Cyn dileu, teipia `get prv.key` dros USB a chadwa'r allwedd breifat mae'n ei dangos mewn lle diogel. Ar ôl dileu, mae `set prv.key <key>` a `reboot` yn rhoi ei hen hunaniaeth yn ôl i'r ailadroddydd, felly mae nodau sy'n ei adnabod yn dod o hyd iddo o dan yr un rhagddodiad.

Mae'r rhestr lawn o orchmynion yn y [cyfeirlyfr CLI MeshCore](https://github.com/meshcore-dev/MeshCore/blob/main/docs/cli_commands.md).

## Ei ddiweddaru dros yr awyr {#update}

Unwaith y bydd yr ailadroddydd i fyny'n uchel, rwyt ti'n ei ddiweddaru o'r ddaear. Mewngofnoda o ap MeshCore gyda chyfrinair y gweinyddwr, agor ei linell orchymyn a theipia `start ota`. Mae'r hyn sy'n dilyn yn dibynnu ar y bwrdd. Mae byrddau eraill yn ateb `Error`, ac rwyt ti'n diweddaru'r rheini dros USB.

**Byrddau nRF52**, fel RAK, Heltec T114, Seeed XIAO a SenseCAP Solar:

1. Lawrlwytha **ZIP** y gadarnwedd newydd ar gyfer dy fwrdd o'r [fflachiwr gwe](https://flasher.meshcore.io).
2. Teipia `start ota`. Mae'r ailadroddydd yn ateb `OK` ac yn ymddangos dros Bluetooth fel `<board>_OTA`, er enghraifft `RAK4631_OTA`.
3. Agor ap nRF Device Firmware Update ar dy ffôn, dewisa'r ZIP a'r ailadroddydd, ac uwchlwytha. Mae'n cymryd ychydig funudau.

Gosoda'r [cychwynnydd OTAFIX](https://github.com/oltaco/Adafruit_nRF52_Bootloader_OTAFIX) ar fwrdd nRF52 cyn iddo fynd i fyny. Gyda'r cychwynnydd gwreiddiol, dim ond dros USB y gelli di drwsio diweddariad a fethodd. Gydag OTAFIX, mae'r bwrdd yn mynd yn ôl i'r modd diweddaru, ac rwyt ti'n rhoi cynnig arall arni dros Bluetooth.

**Byrddau ESP32**, fel y Heltec V3 a V4:

1. Lawrlwytha'r `.bin` **non-merged** ar gyfer dy fwrdd o'r fflachiwr gwe: y ffeil heb "merged" yn ei henw.
2. Teipia `start ota`. Mae'r ailadroddydd yn agor rhwydwaith WiFi o'r enw `MeshCore-OTA` ac yn ateb gyda chyfeiriad ei dudalen uwchlwytho.
3. O fewn cyrraedd WiFi, cysyllta dy ffôn neu liniadur â'r rhwydwaith hwnnw, agor y cyfeiriad ac uwchlwytha'r ffeil.

## Terfynau cyfreithiol {#legal}

{{< callout type="legal" verified="2026-10-02" >}}
Mae rhagosodiadau Ewropeaidd MeshCore yn yr is-fand **869.40-869.65 MHz**. Yn yr UE, y DU, y Swistir a Norwy, mae ar agor i ddyfeisiau amrediad byr heb drwydded, o fewn y terfynau hyn:

- **500 mW e.r.p.** o bŵer pelydrol ar y mwyaf;
- **cylchred gwaith o 10%** ar y mwyaf: dim mwy na 360 eiliad o drawsyrru mewn unrhyw awr, fesul dyfais. Fel arall, caiff dyfais ddefnyddio listen-before-talk gydag adaptive frequency agility fel y'i diffinnir yn ETSI EN 300 220-2;
- rhaid i'r signal cyfan, 250 kHz o led ar y mwyaf, aros y tu mewn i'r is-fand.

Mae'r band yn cael ei rannu: chei di ddim tarfu ar wasanaethau trwyddedig, a gall eraill darfu arnat ti.
Rhaid i'r radio gael marc CE (ym Mhrydain Fawr, CE neu UKCA).
{{< /callout >}}

Ffynonellau: [Argymhelliad CEPT ERC 70-03](https://docdb.cept.org/document/845), Atodiad 1, band h1.7;
[Penderfyniad y Comisiwn 2006/771/EC](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02006D0771(01)-20250123) a'i ddiwygiadau;
[ETSI EN 300 220-2](https://www.etsi.org/deliver/etsi_en/300200_300299/30022002/03.03.01_60/en_30022002v030301p.pdf), band O.

### Pŵer: e.r.p. a'th antena {#erp}

Mae'r terfyn yn berthnasol i'r pŵer *pelydrol*, wedi'i fesur o'i gymharu ag antena deupol syml (e.r.p.). Mae cynnydd yr antena yn cyfrif, ac rwyt ti'n tynnu colled y cebl. Mae gwneuthurwyr yn nodi cynnydd antena mewn dBi, sydd 2.15 dB yn fwy na'r un cynnydd mewn dBd (o'i gymharu â deupol). Cadwa'r swm hwn ar 27 dBm (500 mW) neu'n is:

> pŵer trawsyrru (dBm) + cynnydd antena (dBi) − colled cebl (dB) − 2.15 ≤ 27

- Bwrdd sy'n trawsyrru 22 dBm i antena 5 dBi drwy 1 dB o gebl: 22 + 5 − 1 − 2.15 = 23.85 dBm, tua 240 mW e.r.p. O fewn y terfyn.
- Bwrdd gyda mwyhadur 30 dBm (1 W) i antena 3 dBi: 30 + 3 − 2.15 = 30.85 dBm, tua 1.2 W e.r.p. Dros y terfyn: gostynga'r pŵer trawsyrru.

Mae `set tx` yn gosod allbwn y sglodyn LoRa, mewn dBm. Mae'r sglodyn SX1262 ei hun yn cyrraedd 22 dBm ar y mwyaf, a dydy'r gadarnwedd ddim yn gwirio'r rhif rwyt ti'n ei roi. Mae byrddau gyda mwyhadur ychwanegol, fel y Heltec V4 neu'r Station G2, yn trawsyrru llawer mwy na'r rhif rwyt ti'n ei osod. Gwiria dabl y gwneuthurwr cyn ei osod, a dechreua'n isel.

### Cylchred gwaith {#duty-cycle}

Mae ailadroddydd yn trawsyrru ar ran pawb o'i gwmpas, felly mae'n defnyddio ei amser ar yr awyr yn gyflymach na chydymaith. Y gwerth diofyn ar gyfyngydd cylchred gwaith MeshCore yw 50%, sy'n uwch na'r hyn mae'r band hwn yn ei ganiatáu. Gosoda fe ar 10% ar bob ailadroddydd:

```text
set dutycycle 10
```

### Cywirdeb amledd {#frequency}

Mae sianel EU/UK (Narrow), 869.618 MHz gyda lled band 62.5 kHz, yn cyrraedd hyd at 869.649 MHz: llai nag 1 kHz o dan frig yr is-fand. Rhaid i'r signal aros y tu mewn i'r band ar bob tymheredd. Mae hynny'n gofyn am grisial â chydadfer tymheredd (TCXO). Mae gan bron bob bwrdd cyfredol un. Mae byrddau hŷn hebddo, fel y Heltec V2, yn drifftio gormod i weithio'n ddibynadwy ar 62.5 kHz.

### Nodiadau gwledydd {#countries}

- **Rhaid i aelod-wladwriaethau'r UE** sicrhau bod yr is-fand hwn ar gael ar yr amodau hyn (Penderfyniad 2006/771/EC, Erthygl 3).
- **Y Deyrnas Unedig:** yr un terfynau, yn [IR 2030](https://www.ofcom.org.uk/spectrum/radio-equipment/short-range-devices) Ofcom.
- **Y Swistir a Liechtenstein:** yr un terfynau, yn [RIR1008-09](https://www.ofcomnet.ch/api/rir/1008/09) OFCOM.
- **Norwy:** yr un terfynau, yn y [rheoliad ar awdurdodiadau cyffredinol](https://lovdata.no/dokument/SF/forskrift/2012-01-19-77) (fribruksforskriften).

Nid cyngor cyfreithiol yw'r nodiadau hyn. Mae rheolau'n newid. Os wyt ti'n ansicr, gwiria gyda'th reoleiddiwr cenedlaethol.

## Rhestr wirio gosod {#checklist}

- [ ] Mae perchennog y safle wedi cytuno, a gelli di gyrraedd yr ailadroddydd ar gyfer gwaith cynnal.
- [ ] Mae'r bwrdd yn rhedeg y gadarnwedd **Repeater**, ac fe gafodd yr antena ei chysylltu cyn rhoi pŵer iddo am y tro cyntaf.
- [ ] Mae cyfrinair y gweinyddwr wedi'i newid.
- [ ] Mae'r radio yn cyfateb i [ragosodiad dy ardal](/guides/settings/) (`get radio`).
- [ ] Mae `set dutycycle 10` wedi'i osod.
- [ ] Mae'r pŵer trawsyrru ynghyd â chynnydd yr antena yn aros o fewn 500 mW e.r.p.
- [ ] Mae'r enw, y safle ac `owner.info` wedi'u gosod, fel bod eraill yn gwybod pwy sy'n ei redeg.
- [ ] Mae'r cloc wedi'i osod (`clock`).
- [ ] Mae'r blwch wedi'i selio, gyda thwll draenio neu awyru, ac mae dolen ddiferu ar y cebl.
- [ ] Mae maint y batri a'r panel yn addas ar gyfer mis gwaethaf y gaeaf.
- [ ] Fe wnest ti ei brofi o bellter gyda'r ap cyn gadael y safle.
- [ ] Mae dy grŵp lleol yn gwybod ei fod ar waith.
