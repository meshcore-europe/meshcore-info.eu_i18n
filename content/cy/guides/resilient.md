---
title: Gwna'r rhwyll yn wydn
lead: Ydy'r rhwyll yn dy ardal di yn araf neu'n llawn sothach? Darganfydda'r achos, tro ymlaen y gosodiad ailadroddydd sy'n ei atal, a dywed wrth dy grŵp lleol.
description: 'Llifogydd a sbam ar rwyll MeshCore: sut i adnabod pob math, pa osodiad ailadroddydd sy''n helpu, sut i weld llif a sut i ddod o hyd i''w ffynhonnell.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '500188ff'
  seeded: '2026-11-02'
  fields: {title: '33ec7ac8', lead: '780da19b', description: '1826e5e8'}
  sections: ['68ca5d36', '133c764a', 'a3bb5172', 'f4cc9cad', 'ace7b1ee', '89651002', 'f4dfdf59', '764c832c', 'f342b64b', 'f348e208']
  blocks: ['68ca5d36', 'c9cfbe6c', 'bcb31992', 'de7f60e4', 'e862fb9b', '0046b51f', '25f34d1d', 'c3c3ea52', '853a0f1d', '2bcea703', '871a7661', '2690aacf', 'a4aec3a1', 'd6da27c6', 'e8405458', 'f9150ee6', '8508ce40', '4b03ccd5', 'fb79c493', '695adde7', 'eba5a5b5', '836e0bac', '3497c5e8', '71c78fa1', '537d0930', '6a315252', '7c84dc56', '682e08e6', '258d7a27', '53af1400', '0dbebf97', 'ac0dca3c', '70fb4e9a', '9f055f50', 'ae90facc']
---

Ydy negeseuon yn cyrraedd yn hwyr, neu ddim o gwbl? Ydy Public yn llenwi â
sothach? Llif yw hynny: mwy o draffig nag y gall y rhwyll ei gario, wedi'i
anfon trwy gamgymeriad neu'n fwriadol. Chwilia am yr hyn rwyt ti'n ei weld
yn y tablau isod. Mae pob rhes yn enwi'r gosodiad sy'n ei atal. Tro hwnnw
ymlaen ar dy ailadroddydd, y nod sy'n trosglwyddo negeseuon ymlaen. Yna dywed
wrth dy [grŵp lleol](/community/), er mwyn i'r ailadroddwyr o dy gwmpas wneud
yr un peth. Mae pob ailadroddydd sy'n gollwng llif yn gadael amser darlledu
i bawb arall.

## Llifogydd trwy gamgymeriad {#mistake}

Daw llif trwy gamgymeriad o nod nad yw ei berchennog yn gwybod ei fod yn achosi
un. Mae'n dod i ben unwaith y bydd y perchennog yn gwybod. Hysbyseb, yn y tablau
isod, yw'r cyfarchiad y mae nod yn ei anfon er mwyn i eraill ddod o hyd iddo.

Mae'r gosodiadau yn y tablau yn seiliedig ar yr hyn y mae'r gadarnwedd yn ei
wneud. Dydy pob un ddim wedi atal llif ar rwyll go iawn eto.

{{< callout type="warning" >}}
Mae angen y gadarnwedd DMC ar rai gosodiadau ar y dudalen hon. Mae gan **MeshCore**
safonol 1.18.0 ranbarthau, y terfynau neidiau `flood.max.*`, canfod dolenni a'r
cylch dyletswydd. Daw'r hidlydd pecynnau, y rheolau sy'n gadael i dy ailadroddydd
ollwng sothach, gyda'r **gadarnwedd DMC** gan
[Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore). Felly hefyd gatio'r
cylch dyletswydd a hidlydd y cydymaith. Mae'r dudalen hon yn dilyn fersiwn
datblygu DMC 1.18.0 `ecfb2d4` o 19 Hydref 2026; mae tudalen yr
[hidlydd pecynnau](/guides/filter/#firmware) yn dweud ble i'w chael.
{{< /callout >}}

| Beth rwyt ti'n ei weld | Beth yw e | Beth sy'n helpu |
| --- | --- | --- |
| Ceisiadau i ailadroddwyr gan un nod, ddydd a nos, a rhwyll sy'n aros yn araf am ddyddiau | System awtomeiddio cartref neu fot sy'n gofyn i ailadroddwyr am eu statws yn rhy aml | `filter on`. Wedyn mae'r hidlydd pecynnau yn gadael 5 cais y funud drwodd. Dywed wrth y perchennog. |
| Yr un math o neges ar sianel, bob munud | Bot sy'n postio'n rhy aml | [Rhwystra'r sianel](/guides/filter/#channel) neu [arafa'r anfonwr](/guides/filter/#sender). Dywed wrth y perchennog. |
| Negeseuon annarllenadwy ar Public a sianeli eraill | Nod â chadarnwedd wedi torri neu osodiadau radio anghywir | Mae `filter malformed on` yn eu gollwng ar Public. Dywed wrth y perchennog. |
| Hysbyseb un nod bob ychydig funudau | Nod sydd wedi'i osod i hysbysebu'n rhy aml | Mae `filter advert 24` yn gadael hysbyseb pob nod drwodd unwaith y dydd. Mae `set flood.max.advert 3` yn cadw hysbysebion o fewn 3 naid. |
| Negeseuon o bell, gyda rhanbarthau nad ydyn nhw'n perthyn yma | Pont sy'n cysylltu rhwyllau dros y rhyngrwyd | `set flood.max.unscoped 1`, a rho dy ailadroddydd yn y [rhanbarthau y mae'n eu gwasanaethu](/guides/settings/#traffic) yn unig. |
| Mae'r un neges yn pasio dro ar ôl tro, gydag ID dy ailadroddydd yn ei llwybr fwy nag unwaith | Ailadroddydd sy'n newid pecynnau ac yn eu trosglwyddo ymlaen, felly maen nhw'n mynd mewn dolen | Mae canfod dolenni yn rhedeg ar `minimal` yn ddiofyn. Mae `set loop.detect moderate` yn gollwng dolen yn gynt. |

## Llifogydd bwriadol {#purpose}

Sbam yw rhai llifogydd: sothach sy'n cael ei anfon yn fwriadol i dagu'r rhwyll.
Mae'r anfonwr yn newid enwau, allweddi a llwybrau, felly does dim un rheol yn
atal y llif.

| Beth rwyt ti'n ei weld | Beth yw e | Beth sy'n helpu |
| --- | --- | --- |
| Llawer o nodau newydd ag enwau ar hap, pob un ag allwedd newydd | Hysbysebion ffug | Mae `filter rate 04 5 60` yn gadael 5 hysbyseb y funud drwodd. Dydy `filter advert` ddim yn helpu: daw pob hysbyseb o [allwedd newydd](#forged). |
| Negeseuon â thestun annarllenadwy gan anfonwyr ffug, yn aml â dyddiad fwy na blwyddyn yn ôl | Sbam sianel | Mae `filter malformed on` yn eu gollwng ar Public. Mae `filter age 60` yn gollwng y rhai â hen ddyddiad ar Public ac ar [sianeli dan wyliadwriaeth](/guides/filter/#settings). |
| Hyd at 200 o negeseuon uniongyrchol y funud i nodau nad ydyn nhw'n bodoli, a dim cydnabyddiaethau'n ôl | Llif o negeseuon uniongyrchol | `filter rate 02 5 60`. Dydy dy ap ddim yn dangos y negeseuon hyn; mae arsylwr yn eu dangos. |
| Pyliau o geisiadau gan un nod i ddwsinau o rai eraill | Sbam ceisiadau | Gyda `filter on`, mae'r hidlydd pecynnau yn gadael 5 cais y funud drwodd. |
| Mae neges yn dod yn ôl 10 i 20 munud yn ddiweddarach, gyda bron yr un llwybr | Ailchwarae: copi sy'n cael ei anfon eto | Mae ailadroddydd yn cofio'r 160 pecyn diwethaf a welodd, felly ar rwyll brysur mae copi diweddarach yn pasio eto. Mae `filter age` yn gollwng neges grŵp sy'n hŷn nag rwyt ti'n ei ganiatáu. |
| Negeseuon o Public yn cael eu hanfon eto dan anfonwr ffug, weithiau gyda hen ddyddiad | Sbam atsain | `filter age 60`. Mae `filter malformed on` hefyd yn gollwng dyddiad sydd fwy nag wythnos o'i le. |
| Neges bob ychydig eiliadau ar sawl sianel, pob un gan enw newydd, yn gofyn cwestiynau cyffredin | Ton o fotiau | `filter rate 05 10 60`, a [rhwystra'r sianeli](/guides/filter/#channel) nad yw dy ardal yn eu defnyddio. Mae pob enw'n newydd, felly dydy'r [rheolau anfonwr](#forged) ddim yn ei dal. |

## Beth sydd wedi gweithio {#worked}

Ataliodd grwpiau lleol lifogydd gyda'r camau hyn:

1. **Dywed wrth y perchennog.** Mae llif trwy gamgymeriad yn dod i ben unwaith
   y bydd ei berchennog yn gwybod. Anfona neges gyfeillgar ato.
2. **Paid ag ymateb ar y rhwyll.** Mae ateb yn dangos i sbamiwr fod y sbam yn gweithio.
3. **Gofynna am arsylwyr.** Nod sy'n adrodd am bob pecyn y mae'n ei glywed dros MQTT
   yw arsylwr. Po fwyaf o arsylwyr sydd o dy gwmpas, cynharaf y gweli di ble mae
   llif yn dod i mewn. Tro dy ailadroddydd dy hun yn un gydag
   [MQTT ar dy arsylwr](/guides/mqtt/).
4. **Darganfydda'r ffynhonnell.** Mae arsylwyr yn lleoli'r anfonwr mewn ardal.
   Ar gyfer y cilometr olaf, rhaid i bobl gerdded gyda radio. Edrycha ar
   [Dod o hyd i'r ffynhonnell](#source).
5. **Rho dy grŵp lleol ar waith.** Mae un ailadroddydd â'r gosodiadau cywir yn
   helpu. Gyda'i gilydd, mae holl ailadroddwyr yr ardal yn atal llif. Mae dy
   [grŵp lleol](/community/) yn cael pob perchennog i droi'r gosodiad ymlaen.

## Anfonwyr a llwybrau ffug {#forged}

Mae anfonwr yn ysgrifennu'r rhannau hyn o becyn, a does dim byd yn eu gwirio:

- **Enw'r anfonwr.** Mewn neges sianel, mae'r enw yn rhan o'r testun. Gall
  unrhyw un sydd ag allwedd y sianel ysgrifennu unrhyw enw.
- **Dechrau'r llwybr.** Mae pob ailadroddydd yn ychwanegu ei ID ei hun at ddiwedd
  y llwybr. Does dim byd yn gwirio'r IDs a oedd yno o'r blaen, felly gall anfonwr
  ddechrau'r llwybr ag IDs ffug. Mae diwedd y llwybr yn real.

{{< forged-path >}}

Felly dim ond nes bod anfonwr yn newid ei enw neu ei lwybr y mae `filter sender`
a `filter path` yn ei atal. Mae [rhwystr llwybr](/guides/filter/#path) hefyd yn
gollwng traffig go iawn yr ailadroddydd y mae ei ID ynddo. Mae terfynau cyfradd,
terfynau neidiau, y gwiriadau oedran a malformed, rhwystrau sianel, rhanbarthau
a'r cylch dyletswydd yn dal i weithio.

## Gosodiadau ar gyfer pob llif {#always}

Mae'r rhain yn dal i weithio, beth bynnag sy'n boddi'r rhwyll:

- **Cylch dyletswydd ar 10%.** Wedyn dydy dy ailadroddydd byth yn trosglwyddo mwy
  nag y mae'r gyfraith yn ei ganiatáu, beth bynnag sy'n dod i mewn. Mae'r
  [canllaw ailadroddwyr](/repeater-guide/#duty-cycle) yn ymdrin â hyn.
- **Rhanbarthau a therfynau neidiau.** Rhanbarth yw'r ardal y mae neges yn aros
  ynddi. Dim ond negeseuon yn y rhanbarthau sydd ganddo y mae ailadroddydd yn eu
  trosglwyddo ymlaen, ac mae `flood.max.*` yn cadw traffig yn agos. Mae'r ddau yn
  [Cadw traffig i lawr](/guides/settings/#traffic).
- **Yr hidlydd pecynnau ar gyfer ailadroddydd prysur.** Mae'r
  [gosodiadau parod](/guides/filter/#busy) yn haneru negeseuon grŵp a hysbysebion.
  Rho gynnig arnyn nhw yn y modd [dry-run](/guides/filter/#dryrun) yn gyntaf: dim
  ond cyfrif yr hyn y byddai'n ei ollwng y mae'r modd hwnnw.
- **Hidlydd y cydymaith, yn y gadarnwedd DMC.** Mae dy gydymaith, y nod rwyt ti'n
  anfon negeseuon ohono, yn cadw sothach allan o dy ap. Mae'n cuddio negeseuon
  wedi torri a hen negeseuon, a negeseuon gan ailadroddydd, anfonwr neu air rwyt
  ti'n ei rwystro. Dim ond oddi wrthyt ti y mae rheol anfonwr neu air yn cuddio'r
  neges; mae eraill yn dal i'w derbyn.

### Gatio'r cylch dyletswydd {#gate}

Yn y gadarnwedd DMC, gall dy ailadroddydd roi blaenoriaeth i'w ranbarth ei hun pan
fydd yn brysur. Unwaith y bydd wedi trosglwyddo am fwy na 35% o'r funud ddiwethaf,
mae'n peidio â throsglwyddo negeseuon heb ranbarth. Os yw'n aros yn brysur, mae'n
gollwng y rhanbarth lletaf nesaf, un lefel ar y tro. Mae ei ranbarth ei hun bob
amser yn pasio. Dim ond gyda rhanbarthau wedi'u gosod ar dy ailadroddydd y mae'n
gweithio. Tro fe ymlaen a'i wirio:

```text
set dc.gate on
get dc.gate.status
```

{{< dc-gate >}}

Dydy'r hyn y mae'n ei ollwng ddim yn ymddangos yn `filter stats`. Pan fydd yr
ailadroddydd yn dawel eto, mae'r rhanbarthau'n dod yn ôl, yr un mwyaf mewnol yn gyntaf.

## Gweld llif {#see}

Dim ond yr hyn sy'n dy gyrraedd di y mae dy ap yn ei ddangos. Dim ond arsylwr sy'n
clywed llif o negeseuon uniongyrchol i nodau nad ydyn nhw'n bodoli. Mae pob arsylwr
yn adrodd i'r [MeshCore Analyzer](https://meshcore-analyzer.eu/), lle gall pawb ei
weld. Tro dy ailadroddydd yn un gydag [MQTT ar dy arsylwr](/guides/mqtt/).

Ar yr Analyzer, edrycha ar bob copi o un pecyn. Mae ei lwybr fel arfer yn dangos
o ble y daeth. Gall anfonwr llif ddechrau'r llwybr ag [IDs ffug](#forged), felly
dydy'r IDs cyntaf yn dweud dim wrthyt ti. Ond mae pob copi yn cario'r un dechrau
ffug. Pasiodd y copi â'r llwybr byrraf y nifer lleiaf o ailadroddwyr go iawn, felly
cafodd ei glywed agosaf at yr anfonwr.

{{< copies >}}

Ar dy ailadroddydd dy hun, mae `filter stats` yn dangos yr hyn a ollyngodd yr
hidlydd pecynnau. Mae `filter stats top` yn dangos beit cyntaf IDs y nodau sydd
y tu ôl i'r rhan fwyaf o'r hyn a ollyngodd. Mae llawer o nodau'n rhannu'r beit hwnnw,
felly mae'n culhau'r chwilio ond dydy e ddim yn enwi'r anfonwr.

## Dod o hyd i'r ffynhonnell {#source}

Pan fydd llif yn dal i ddod yn ôl:

1. **Dilyna'r llwybrau.** Darllena lwybr o'r diwedd: yr IDs olaf yw'r ailadroddwyr
   y pasiodd y llif drwyddyn nhw. Mae'r un go iawn cynharaf ger y ffynhonnell; gall
   yr IDs cyn hwnnw fod yn [ffug](#forged).
2. **Culha'r ardal.** Mae sawl arsylwr sy'n clywed yr un pecyn yn lleoli'r anfonwr
   mewn ardal. Mae'r [DMC Triangulator](https://triangulator.dutchmeshcore.nl/)
   yn cyfrifo hyn o'r ailadroddwyr a'i clywodd.
3. **Cerdda'r cilometr olaf.** Dim ond ar ymyl eu cyrhaeddiad y mae'r ailadroddwyr
   yn clywed y ffynhonnell, felly rhaid i bobl gerdded y darn olaf.
   Mae [Mesh-Hunter](https://mesh-hunter.eu/) yn paru â dy gydymaith ac yn cofnodi
   pob pecyn y mae'n ei glywed gyda dy safle GPS. Mae sawl person sy'n cerdded ar
   yr un pryd yn dod o hyd iddi'n gynt.
4. **Dywed wrth dy [grŵp lleol](/community/).** Maen nhw'n gweld mwy o'r rhwyll,
   nhw sy'n penderfynu beth sy'n digwydd nesaf, a nhw sy'n cysylltu â phwy bynnag
   sy'n anfon llif yn fwriadol.

## Ychwanega'r hyn a welaist ti {#add}

A gest ti dy daro gan lif nad yw yn y tablau hyn? A wnaeth gosodiad atal un? Dywed
wrthon ni ar [Discord](https://discord.meshcore-info.eu/): beth welaist ti a beth
wnest ti ei droi ymlaen. Rydyn ni'n ei ychwanegu at y dudalen.
