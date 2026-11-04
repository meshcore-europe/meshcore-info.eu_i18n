---
title: Dechrau arni
lead: O fwrdd newydd i'th neges gyntaf ar y mesh. Mae angen bwrdd LoRa arnat ti, cyfrifiadur gyda Chrome neu Edge, a ffôn neu liniadur ar gyfer yr ap.
description: Fflachia MeshCore o'th borwr, para'r ap, dewisa'r rhagosodiad radio sy'n cael ei ddefnyddio yn dy ardal, anfona dy neges gyntaf ac ymuna â'th sianel leol.
eyebrow: 6 cham · MeshCore v1.18.0
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '0490a311'
  seeded: '2026-11-04'
  fields: {title: '61e8d44a', lead: '45b0e5c3', description: 'cf031b18', eyebrow: '4fa6fe1e'}
  sections: ['16c3728c', '5b6d136a', 'df7a1665', '6da9fd7a', 'cb5fb72e', 'a1cf8b26', '1741ed35', '66d00206']
  blocks: ['16c3728c', '2a70a7ed', '6f8e6f5f', '16c11d47', 'e90b7859', '081db416', 'd5e7fd0b', '6d28c323', 'eb2ea361', 'de50125c', 'ae20cb8e', 'abd42710', 'c08a865a', '7d1eb0b9', '263e0c96', '0903299f', 'eba20370', '5cdc20cf', '7f542f82', '802ca5a8', '1a854187', '53276869', 'f25b16fa', '7c893ae2', '7f5927b4', '26e13713', '39a142cf', 'a786620c', '216897fa', '2d222782', 'a9755900', 'f081b357']
---

Mae'r camau hyn yn dilyn cadarnwedd MeshCore v1.18.0 ac offer swyddogol
Hydref 2026. Gall enwau'r dewislenni yn yr ap amrywio ychydig rhwng fersiynau.

## 1. Dewis dyfais {#device}

Mae unrhyw fwrdd ar y [dudalen dyfeisiau](/devices/) sy'n rhestru companion yn
gweithio. Ar gyfer dy nod cyntaf, dewisa *companion*: y radio rwyt ti'n anfon
negeseuon ohono. Para fe â dy ffôn neu dy liniadur dros Bluetooth neu USB, neu
dewisa un â'i sgrin a'i fysellfwrdd ei hun sy'n gweithio ar ei ben ei hun.

Pryna'r fersiwn 868 MHz. Mae'r antena sy'n dod gyda'r ddyfais yn gwneud y tro;
mae'r [canllaw antenâu](/guides/antenna/) yn dangos sut i wirio un.

Ydy dy fwrdd yn rhedeg Meshtastic ar hyn o bryd? Pan fyddi di'n fflachio MeshCore, mae'n cymryd ei
le, a dydy'r ddau ddim yn siarad â'i gilydd.

{{< callout type="warning" >}}
Cysyllta'r antena cyn i ti droi'r radio ymlaen. Gall radio LoRa sy'n trawsyrru
heb antena niweidio ei sglodyn ei hun.
{{< /callout >}}

## 2. Fflachio'r gadarnwedd {#flash}

1. Cysyllta'r ddyfais â dy gyfrifiadur gyda chebl data USB.
2. Agor y fflachiwr gwe yn [flasher.meshcore.io](https://flasher.meshcore.io)
   yn Chrome neu Edge. Mae'n defnyddio Web Serial, a does gan borwyr eraill mo hwnnw.
3. Dewisa dy ddyfais, yna'r gadarnwedd **Companion** ar gyfer **Bluetooth** (neu
   USB, os mai dim ond gyda chebl cyfrifiadur y byddi di'n ei defnyddio).
4. Fflachia. Mae rhai byrddau'n mynd i'r modd diweddaru yn gyntaf; mae'r
   fflachiwr yn dweud wrthot ti sut.

Dim ond wrth ddechrau o'r newydd y dylet ti ddefnyddio *erase*: mae dileu yn cael
gwared ar hunaniaeth y ddyfais a dy gysylltiadau. I ddiweddaru wedyn, fflachia
heb ddileu. I gadw dy hunaniaeth drwy'r dileu, allforia allwedd breifat dy
companion o'r ap yn gyntaf a'i mewnforio wedyn.

## 3. Gosod yr ap {#app}

Mae ap swyddogol MeshCore ar gael ar gyfer Android, iOS, Windows a macOS; mae
[meshcore.io](https://meshcore.io) yn cynnig dolen i bob fersiwn. Mae ap gwe
hefyd yn [app.meshcore.nz](https://app.meshcore.nz) sy'n rhedeg yn Chrome neu
Edge ar gyfrifiadur.

## 4. Paru dy nod {#pair}

Tro dy nod ymlaen, agor yr ap a chysyllta â'r nod dros Bluetooth. Pan fydd yr
ap yn gofyn am PIN:

- mae nod **gyda** sgrin yn dangos PIN; teipia hwnnw;
- mae nod **heb** sgrin yn defnyddio `123456`.

Os yw'r paru'n methu, tynna'r ddyfais o osodiadau Bluetooth dy ffôn a rho gynnig
arall arni. Yna rho enw i dy nod. Mae pobl eraill yn gweld yr enw hwn, felly
paid â defnyddio dy enw llawn na dy gyfeiriad oni bai dy fod ti eisiau.

## 5. Dewis rhagosodiad radio dy ardal {#preset}

Mae pob radio mewn ardal yn defnyddio'r un amledd a'r un gosodiadau, neu allan
nhw ddim clywed ei gilydd. Yng ngosodiadau radio'r ap, dewisa'r rhagosodiad mae
dy ardal yn ei ddefnyddio. Y tu allan i'r ardaloedd isod, mae Ewrop yn
defnyddio **EU/UK (Narrow)**. Mae gan yr Iseldiroedd, Tsiecia, Hwngari,
Slofacia, Portiwgal a'r Swistir eu rhagosodiad eu hunain, ac mae amrywiad gan
Limburg yn yr Iseldiroedd:

{{< presets >}}

Dydy dy ddyfais ddim yn cynnig rhagosodiad dy ardal? Rho'r 4 gwerth o'r tabl â
llaw yng ngosodiadau radio'r ap: amledd, lled band, ffactor taenu a chyfradd
godio. Dydy nod â gwerthoedd eraill ddim yn clywed y mesh.

Ddim yn siŵr? Mae dy [grŵp lleol](/community/) yn gwybod pa ragosodiad mae dy
ardal yn ei ddefnyddio. Mae'r ap yn lawrlwytho'r rhestr hon gan brosiect
MeshCore, felly does dim angen diweddaru'r ap ar gyfer rhagosodiad newydd.

## 6. Dweud helo {#hello}

1. **Cyhoedda dy hun.** Anfona *advert* o'r ap. Mae advert "gorlif" yn teithio
   drwy'r ailadroddyddion (nodau sy'n trosglwyddo negeseuon ymlaen), felly gall pawb
   ar y rhwyll dy ychwanegu di.
   Dydy cymdeithion byth yn cyhoeddi eu hunain yn awtomatig.
2. **Dere o hyd i eraill.** Mae pobl yn ymddangos yn dy gysylltiadau pan fydd eu
   hadverts yn dy gyrraedd. Mae ailadroddyddion yn anfon advert gorlif bob 47
   awr yn ddiofyn, felly gall dy restr gymryd 2 ddiwrnod i lenwi.
3. **Anfona neges.** Agor gyswllt ac ysgrifenna. Mae'r neges gyntaf yn gorlifo'r
   rhwydwaith. Mae'r derbynnydd yn rhoi gwybod pa lwybr a gymerodd hi, ac mae
   negeseuon diweddarach yn dilyn y llwybr hwnnw.
4. **Ymuna â sianeli.** Mae'r sianel **Public** wedi'i gosod yn barod. Mae
   unrhyw beth rwyt ti'n ei ysgrifennu yno yn cyrraedd pawb ar y rhwyll. Ychwanega
   *sianel hashnod* dy ranbarth (enw sy'n dechrau gyda `#`) drwy deipio ei
   henw. Bydd dy [grŵp lleol](/community/) yn dweud wrthot ti pa sianeli sy'n
   weithgar.
   Eisiau eu cyfarfod wyneb yn wyneb? Edrycha ar y [cyfarfodydd](/meetings/)
   yn agos atat ti.

## Pan nad yw rhywbeth yn gweithio {#troubleshooting}

**Dydy'r ap ddim yn dod o hyd i'm dyfais dros Bluetooth.**
Mae'n debyg dy fod ti wedi fflachio'r companion USB. Fflachia eto a dewisa'r
fersiwn Bluetooth. Ar yr Heltec V3, mae gan yr antena Bluetooth fach adeiledig
gyrhaeddiad byr; cadwa'r ffôn yn agos.

**Mae'r paru'n dal i fethu.**
Tynna'r ddyfais o osodiadau Bluetooth dy ffôn, ailgychwyna Bluetooth, a phara
eto gyda'r PIN ar y sgrin neu `123456`.

**Does neb yn ymddangos yn fy nghysylltiadau.**
Gwiria fod dy ragosodiad yn cyfateb i dy ardal. Anfona advert flood. Os nad oes
ailadroddydd o fewn cyrraedd, dim ond radios cyfagos fyddi di'n eu clywed; mae'r
[dudalen map](/map/) yn dangos ble mae ailadroddyddion.

**Mae cyswllt yn dangos "last seen" ddyddiau yn ôl er ei fod yn weithgar.**
Mae'r amser yn anghywir ar un o'r ddau nod. Mae companion yn cymryd yr amser o dy
ffôn; rhaid i'w perchennog osod yr amser ar ailadroddyddion a room servers (nodau
sy'n storio negeseuon i grŵp).

**Dydy neges uniongyrchol byth yn cyrraedd.**
Rhaid i ti gael y person arall yn gyswllt, ac i'r person arall dy gael di. Mae nod yn gollwng
neges gan rywun nad yw'n ei adnabod, heb ddweud wrth yr anfonwr. Anfona advert
flood a gofyn i'r person arall anfon un hefyd. Gwiria yn yr ap ei fod yn
ychwanegu cysylltiadau newydd yn awtomatig; dim ond nodau o fewn ei derfyn hopian
y mae'n eu hychwanegu.

**Mae hen gysylltiadau'n gweithio, ond dydy rhai newydd byth yn cysylltu.**
Mae neges gyntaf yn gorlifo'r rhwydwaith, a dim ond os yw'n dal rhanbarth y neges
y mae ailadroddydd yn ei throsglwyddo ymlaen. Mae negeseuon diweddarach yn dilyn
llwybr a ddysgwyd, a does dim gwiriad rhanbarth yn atal hwnnw. Gofyn i dy
[grŵp lleol](/community/) pa ranbarthau mae'r ailadroddyddion o dy gwmpas yn eu
dal, a gwiria [osodiadau dy ardal](/guides/settings/#traffic).

**Dydy'r ap ddim yn cysylltu â dy companion mwyach.**
Mae gan rai byrddau fotwm defnyddiwr, fel rhai byrddau RAK a'r Heltec T114.
Dal y botwm i lawr yn ystod yr 8 eiliad gyntaf ar ôl i'r bwrdd gychwyn. Mae'r
companion yn agor consol achub dros USB. Yn y consol ar
[flasher.meshcore.io](https://flasher.meshcore.io), mae `set pin <pin>` yn gosod
PIN Bluetooth newydd ac mae `erase` yn clirio'r ddyfais.

**Dydy'r fflachiwr ddim yn gallu agor y porth cyfresol ar Linux.**
Mae angen mynediad i'r porth ar dy ddefnyddiwr, er enghraifft
`sudo setfacl -m u:$USER:rw /dev/ttyUSB0`, neu aelodaeth o'r grŵp `dialout`.

**Rhywbeth arall.** Mae
[Cwestiynau Cyffredin MeshCore](https://github.com/meshcore-dev/MeshCore/blob/main/docs/faq.md)
yn trafod llawer mwy o broblemau.
