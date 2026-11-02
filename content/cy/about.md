---
title: Beth yw MeshCore?
lead: Mae MeshCore yn anfon negeseuon testun dros y radio, o nod i nod. Mae'n gweithio heb y rhyngrwyd a heb danysgrifiad.
description: 'Beth yw MeshCore a beth nad ydyw: y rhwyll, cymdeithion, ailadroddyddion a gweinyddion ystafell, llwybro, amgryptio, a''r band 868 MHz yn Ewrop.'
eyebrow: MeshCore v1.18.0
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '78bc31e8'
  seeded: '2026-11-02'
  fields: {title: '06eda66b', lead: 'c0174569', description: '658f8a01', eyebrow: '8610c822'}
  sections: ['aa768ac3', 'c9b24089', '0a55792c', 'c3de803d', '493b444f', '429f699c', 'f8008f48', '655373a9', '0894fe81']
  blocks: ['c3c9c568', '55e4248c', 'c0324d05', 'b20e61c3', 'b9fc8810', '68ed3005', 'cabeb32d', 'b2ca68ba', '681d55b9', 'd1df283f', '0d0e2a8b', '0596f602', 'eec63bed', '183a79e4', '47910535', 'd5a92bbf', 'b44d4637', '431021a0', '83c03732', 'e908ca85', '8f79fbf9', '3323d83e', '857c37dc', '0c4d0dd2', 'bd238f09', '794792be', '0eb54b47', '02f1fe2f', 'e6b5b258']
---

Meddalwedd rydd ar gyfer radios LoRa bach yw MeshCore. Techneg radio yw LoRa sy'n anfon ychydig o ddata yn bell, ar ychydig iawn o bŵer. *Nod* yw'r enw ar radio sydd â MeshCore arno. Wedi'i baru â'r ap ar dy ffôn neu dy liniadur, neu gyda'i sgrin a'i fysellfwrdd ei hun, mae'n anfon testun at bobl sydd gilometrau i ffwrdd. Does dim mast, llwybrydd na darparwr yn y canol.

Cod agored yw'r feddalwedd. Mae'r datblygwyr yn gweithio arni yn
[meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore) dan drwydded MIT.

## Beth nad yw MeshCore {#not}

Wyt ti'n newydd i radio? Dyma'r pethau mae pobl yn eu disgwyl amlaf gan MeshCore, ond nad yw'n eu gwneud.

- **Nid y rhyngrwyd na ffôn mohono.** Mae MeshCore yn anfon negeseuon testun byr, tua'r un hyd â neges destun ar dy ffôn. Does dim llais, lluniau, fideo na gwefannau, ac ni elli di gyrraedd rhif ffôn arferol.
- **Nid gwasanaeth brys mohono.** Does dim gwasanaeth brys yn gwrando ar y rhwyll, a does neb yn addo y bydd rhywun yn darllen dy neges. Mewn argyfwng, ffonia 112.
- **Nid yw'n digwydd ar unwaith, ac nid yw ym mhobman.** Mae neges yn neidio o radio i radio. Gall gymryd ychydig eiliadau, neu beidio â chyrraedd o gwbl. Mae p'un a yw'n cyrraedd yn dibynnu ar yr ailadroddyddion o'th gwmpas, ar uchder, ar adeiladau ac ar dy antena. Yn aml, nid yw radio bach dan do yn cyrraedd neb. Mae ailadroddydd ar do yn cyrraedd cilometrau i ffwrdd.
- **Nid gwasanaeth mae rhywun yn ei redeg ar dy ran mohono.** Does dim darparwr, dim desg gymorth a dim addewid o ddarpariaeth. Mae'r rhwyll yn bodoli lle mae pobl yn y gymuned wedi codi ailadroddyddion, a nunlle arall.
- **Nid yw popeth arno'n breifat.** Mae negeseuon uniongyrchol wedi'u hamgryptio, ond gall unrhyw un ddarllen Public a'r sianeli hashnod. Gall pawb o fewn cyrraedd weld enw dy nod a'r lleoliad rwyt ti'n ei rannu. Mae [arsylwyr](/network/) yn anfon yr hyn maen nhw'n ei glywed at fapiau cyhoeddus. Mae'r [adran amgryptio](#encryption) yn esbonio beth sy'n aros yn breifat.
- **Nid yw'n ddiderfyn.** Mae pawb mewn ardal yn rhannu un sianel radio, ac mae rheolau'r [band 868 MHz](#band) yn cyfyngu ar ba mor hir y caiff pob radio anfon. Mae pob neges yn cymryd amser darlledu oddi wrth bawb arall, felly mae botiau, hysbysebion mynych a negeseuon prawf yn arafu'r rhwyll i bawb.
- **Nid Meshtastic mohono.** System wahanol yw Meshtastic, sy'n rhedeg ar fyrddau digon tebyg. Ni all y ddwy system siarad â'i gilydd.

## Y rhwyll mewn munud {#mesh}

Mae un radio LoRa yn cyrraedd ychydig gilometrau mewn tref, a llawer ymhellach o fryn neu do. I gyrraedd ymhellach, mae radios yn trosglwyddo negeseuon dros ei gilydd: dyna yw *rhwyll*. Yn MeshCore, radios o'r enw *ailadroddyddion* sy'n gwneud y trosglwyddo. Pan fydd ailadroddydd yn clywed neges, mae'n ei hanfon eto, felly gall y neges groesi rhanbarth cyfan.

Does neb yn berchen ar y rhwyll. Mae pob nod a phob ailadroddydd yn perthyn i rywun yn y gymuned. Mae'r rhwyll yn cyrraedd cyn belled ag y mae eu hailadroddyddion nhw'n cyrraedd.

## Y 3 math o nod {#roles}

Rwyt ti'n dewis math y nod wrth fflachio'r feddalwedd arno. Cydymaith yw dy nod cyntaf.

**Cydymaith.** Dy radio dy hun. Mae'n paru â'r ap MeshCore ar dy ffôn neu dy liniadur dros Bluetooth neu USB. Mae gan rai eu sgrin a'u bysellfwrdd eu hunain. Yn yr ap rwyt ti'n darllen ac yn teipio. Mae'r cydymaith yn cadw dy gysylltiadau a'th sianeli, a'r negeseuon a gyrhaeddodd tra nad oedd yr ap wedi'i gysylltu. Dydy cydymaith ddim yn trosglwyddo negeseuon dros bobl eraill.

**Ailadroddydd.** Radio mewn man uchel sy'n trosglwyddo negeseuon dros bawb. Mae'r rhan fwyaf yn rhedeg ar bŵer solar. Dim ond lle nad yw'r rhwyll yn cyrraedd eto mae angen dy un dy hun arnat ti. Does ganddo ddim ap ei hun. Rwyt ti'n ei osod dros USB, neu'n mewngofnodi â chyfrinair ac yn ei reoli dros y radio. Mae'r [canllaw ailadroddyddion](/repeater-guide/) yn dangos sut.

**Gweinydd ystafell.** Bwrdd negeseuon bach ar y rhwyll. Pan fyddi di'n mewngofnodi, byddi di'n cael y negeseuon a gollaist ti tra oeddet ti allan o gyrraedd, hyd at y 32 diwethaf. Dim ond yn y cof mae'n eu cadw, felly mae ailgychwyn neu doriad pŵer yn eu dileu. Mae grŵp lleol yn defnyddio un ar gyfer cyhoeddiadau.

## Sut mae neges yn canfod ei ffordd {#routing}

Mae gan bob nod allwedd gyfrinachol ac allwedd gyhoeddus. Yr allwedd gyhoeddus yw ei hunaniaeth. Mae nod yn ei gyhoeddi ei hun gyda *hysbyseb*: pecyn wedi'i lofnodi sy'n cynnwys ei enw ac, os wyt ti'n dewis, ei leoliad. Mae rhywun yn ymddangos yn dy gysylltiadau ar ôl i un o'u hysbysebion dy gyrraedd, neu pan fyddi di'n sganio eu cod QR. Mae gan yr ap fotwm i anfon dy hysbyseb dy hun.

Mae dy neges gyntaf at gyswllt yn mynd allan fel *llif*. Mae pob ailadroddydd sy'n ei chlywed yn ei throsglwyddo unwaith, ac yn ychwanegu ei ID byr ei hun ar y ffordd. Mae'r ateb yn cludo'r rhestr honno o IDs yn ôl. O hynny ymlaen, mae dy negeseuon at y cyswllt hwnnw'n dilyn y llwybr a gofnodwyd, a dim ond yr ailadroddyddion arno sy'n anfon. Pan fydd y llwybr yn torri, mae'r ap yn anfon llif eto.

Does gan negeseuon at sianel ddim un cyfeiriad penodol, felly maen nhw bob amser yn mynd fel llif. Mae ailadroddyddion yn cofio'r hyn maen nhw wedi'i drosglwyddo'n ddiweddar, ac yn gollwng copïau sy'n cyrraedd eto ar hyd llwybr arall. Gall neges groesi hyd at 64 ailadroddydd, neu 32 lle mae'r rhagosodiad yn defnyddio IDs 2 beit.

## Amgryptio a phreifatrwydd {#encryption}

Mae dy negeseuon uniongyrchol wedi'u hamgryptio o'r naill ben i'r llall: dim ond ti a'r person arall sy'n gallu eu darllen. Dim ond fel awgrym 1 beit mae ailadroddydd yn gweld i bwy mae pecyn yn mynd.

Mae sianeli wedi'u hamgryptio ag allwedd a rennir, felly mae pwy sy'n gallu eu darllen yn dibynnu ar bwy sydd â'r allwedd honno:

- **Public**: mae'r sianel hon wedi'i gosod ar bob cydymaith. Mae ei hallwedd wedi'i chyhoeddi, felly gall unrhyw un ei darllen.
- **Sianeli hashnod**, fel `#utrecht`: mae eu hallwedd yn dod o'u henw. Gall unrhyw un sy'n gwybod yr enw ymuno, felly ystyria nhw'n gyhoeddus hefyd.
- **Sianeli preifat**: maen nhw'n defnyddio allwedd ar hap rwyt ti'n ei rhannu dy hun, er enghraifft fel cod QR.

Mae hysbysebion wedi'u llofnodi ond heb eu hamgryptio. Gall pawb o fewn cyrraedd weld enw dy nod, a'i leoliad os wyt ti'n ei rannu. Dewisa enw nad yw'n dweud mwy nag rwyt ti eisiau.

## Y band 868 MHz yn Ewrop {#band}

Yn Ewrop, mae MeshCore yn defnyddio rhan fach o'r band 868 MHz y caiff unrhyw un ei defnyddio heb drwydded. Mae ei ragosodiad radio Ewropeaidd, EU/UK (Narrow), ar 869.618 MHz ar sianel 62.5 kHz. Mae hynny y tu mewn i'r is-fand 869.40-869.65 MHz, sy'n caniatáu hyd at 500 mW e.r.p. Caiff dyfais anfon yno am 10% o'r amser ar y mwyaf. Mae [adran gyfreithiol y canllaw ailadroddyddion](/repeater-guide/#legal) yn rhoi'r manylion a'r cyfyngiadau fesul gwlad.

Mae pawb mewn ardal yn defnyddio'r un rhagosodiad, neu ni all eu radios glywed ei gilydd. Mae rhai gwledydd a rhanbarthau yn defnyddio amrywiad: mae dy [grŵp lleol](/community/) yn gwybod pa un.

## I beth mae pobl yn ei ddefnyddio {#uses}

- Cadw mewn cysylltiad ar deithiau cerdded, ar y môr ac mewn gwyliau lle mae'r rhwydwaith symudol dan ormod o bwysau neu ddim ar gael.
- Sianel wrth gefn i deulu neu gymdogion pan fydd y pŵer neu'r rhwydweithiau symudol yn methu.
- Sgwrsio'n lleol ar radios mae pobl yn berchen arnyn nhw eu hunain.
- Arbrofi gyda radio, antenâu, pŵer solar a meddalwedd cod agored.

## O ble mae'r data'n dod {#data}

Mae'r chwiliad ar y dudalen [grwpiau lleol](/community/) yn dod o hyd i le gyda chopi o restrau rhydd lleoedd a chodau post [GeoNames](https://www.geonames.org/), dan drwydded
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Mae'r copi ar y wefan hon. Dydy dy chwiliad byth yn gadael dy ddyfais, a does dim cais yn mynd i GeoNames.
