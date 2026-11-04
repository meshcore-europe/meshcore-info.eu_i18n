---
title: Beth yw MeshCore?
lead: Mae MeshCore yn anfon negeseuon testun dros y radio, o nod i nod. Mae'n gweithio heb y rhyngrwyd a heb danysgrifiad.
description: 'Beth yw MeshCore a beth nad yw: mathau o nod, llwybro, amgryptio a''r band 868 MHz.'
eyebrow: MeshCore v1.18.0
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '2a40da22'
  seeded: '2026-11-04'
  fields: {title: '06eda66b', lead: 'c0174569', description: 'c2255f49', eyebrow: '8610c822'}
  sections: ['aa768ac3', '92fc3ea7', '0a55792c', 'c3de803d', '493b444f', '429f699c', 'f8008f48', '203a07ef', '0894fe81']
  blocks: ['c3c9c568', '55e4248c', 'c0324d05', 'b20e61c3', 'ac039316', '68ed3005', 'cabeb32d', 'b2ca68ba', '681d55b9', 'd1df283f', '0d0e2a8b', '0596f602', 'eec63bed', '183a79e4', '47910535', 'd5a92bbf', 'b44d4637', '431021a0', '83c03732', 'e908ca85', '8f79fbf9', '3323d83e', '857c37dc', '0c4d0dd2', 'bd238f09', '794792be', '5d796ffb', '1a490368', 'f0dd237f', '3182d5c8', '02f1fe2f', 'e6b5b258']
---

Meddalwedd rydd ar gyfer radios LoRa bach yw MeshCore. Techneg radio yw LoRa sy'n anfon ychydig o ddata yn bell, ar ychydig iawn o bŵer. *Nod* yw'r enw ar radio sydd â MeshCore arno. Wedi'i baru â'r ap ar dy ffôn neu dy liniadur, neu gyda'i sgrin a'i fysellfwrdd ei hun, mae'n anfon testun at bobl sydd gilometrau i ffwrdd. Does dim mast, llwybrydd na darparwr yn y canol.

Cod agored yw'r feddalwedd. Mae'r datblygwyr yn gweithio arni yn
[meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore) dan drwydded MIT.

## Beth nad yw MeshCore {#not}

Wyt ti'n newydd i radio? Dyma'r pethau mae pobl yn eu disgwyl amlaf gan MeshCore, ond nad yw'n eu gwneud.

- **Nid y rhyngrwyd na ffôn yw MeshCore.** Mae MeshCore yn anfon negeseuon testun byr,
  tua hyd neges destun ar dy ffôn. Does dim llais, lluniau, fideo
  na gwefannau, a fedri di ddim cyrraedd rhif ffôn arferol.
- **Nid gwasanaeth brys yw e.** Does dim gwasanaeth brys yn addo
  gwrando ar y rhwyll, a does neb yn addo bod rhywun yn darllen dy neges.
- **Dyw e ddim yn syth, a dyw e ddim ym mhobman.** Mae neges yn neidio o radio i
  radio a gall gymryd ychydig eiliadau, neu beidio cyrraedd o gwbl. Mae p'un a yw hi'n cyrraedd yn dibynnu
  ar yr ailadroddyddion o dy gwmpas, ar uchder, adeiladau a dy
  antena. Yn aml, dyw radio bach dan do ddim yn cyrraedd neb; mae ailadroddydd ar do
  yn cyrraedd am gilometrau.
- **Nid gwasanaeth mae rhywun yn ei redeg i ti yw e.** Does dim darparwr, dim
  desg gymorth a dim addewid o ddarpariaeth. Mae'r rhwyll yn bodoli lle mae pobl
  yn y gymuned wedi codi ailadroddyddion.
- **Dyw popeth arno ddim yn breifat.** Mae negeseuon uniongyrchol wedi'u hamgryptio, ond
  gall unrhyw un ddarllen Public a'r sianeli hashnod. Gall pawb o fewn cyrraedd weld
  enw dy nod a'r lleoliad rwyt ti'n ei rannu.
  Mae [arsylwyr](/network/) yn anfon yr hyn maen nhw'n ei glywed i fapiau cyhoeddus. Mae'r
  [adran amgryptio](#encryption) yn esbonio beth sy'n aros yn breifat.
- **Dyw e ddim yn ddiderfyn.** Mae pawb mewn ardal yn rhannu un sianel radio, ac
  mae rheolau'r [band 868 MHz](#band) yn cyfyngu ar ba mor hir mae pob radio'n cael anfon.
  Mae pob neges yn cymryd amser darlledu oddi wrth bawb arall. Felly mae bots, adverts aml
  a negeseuon prawf yn arafu'r rhwyll i bawb.
- **Nid Meshtastic yw e.** Mae Meshtastic yn system wahanol sy'n rhedeg ar
  fwy neu lai yr un byrddau. Fedr y ddwy ddim siarad â'i gilydd.

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

- Cadw mewn cysylltiad ar deithiau cerdded, ar y môr ac mewn gwyliau lle mae'r rhwydwaith
  symudol dan ormod o bwysau neu'n absennol.
- Sianel wrth gefn i deulu neu gymdogion pan fydd y cyflenwad pŵer neu'r rhwydweithiau
  symudol yn methu.
- Dull wrth gefn i awdurdodau lleol pan fydd eu rhwydweithiau arferol yn methu.
- Sgwrsio lleol ar radios sy'n eiddo i bobl eu hunain.
- Cadw tîm chwilio ac achub mewn cysylltiad lle nad oes rhwydwaith symudol.
  Mae MeshCore SAR, ap cymunedol ar [Prosiectau](/projects/), yn ychwanegu mapiau a
  lleoliadau wedi'u rhannu.
- Gwirio safle anghysbell o gartref. Mae ailadroddyddion a nodau synhwyrydd yn rhoi gwybod
  am foltedd eu batri a darlleniadau eraill pan fyddi di'n gofyn.
- Cadw llygad ar synhwyrydd. Mae nod synhwyrydd yn rhedeg cadarnwedd MeshCore ar gyfer
  mesur pethau. Mae'n cadw hanes o foltedd ei fatri. Mewngofnoda fel gweinyddwr ac
  mae'n dy rybuddio pan fydd y batri'n mynd yn isel. Rwyt ti'n ychwanegu rhybuddion ar gyfer
  darlleniadau eraill gyda dy god dy hun.
- Troi rhywbeth ymlaen neu i ffwrdd o bell, fel pwmp. Rwyt ti'n ychwanegu hynny at
  gadarnwedd y synhwyrydd gyda dy god dy hun.
- Arbrofi gyda radio, antenâu, pŵer solar a meddalwedd cod agored.

Mae rhai awdurdodau'n adeiladu neu'n profi system wrth gefn ar MeshCore. Fe wnaethon ni wirio'r enghreifftiau hyn ym mis Tachwedd 2026.

- Torrodd Seiclon Gabrielle bob cyfathrebu yn Tairāwhiti, Seland Newydd. Ym mis
  Medi 2025, enwodd rheolwyr argyfwng y rhanbarth MeshCore yn
  [un o o leiaf 6 ffordd wrth gefn i gyfathrebu](https://www.scoop.co.nz/stories/AK2509/S00669.htm).
  Roedden nhw hefyd yn adeiladu ailadroddyddion solar yn asgwrn cefn.
- Mae ardal Bad Kissingen yn yr Almaen
  [yn adeiladu rhwydwaith testun ar MeshCore](https://www.landkreis-badkissingen.de/wirtschaft/digitalisierung/kommunikationsnetze/index.html)
  ar gyfer awdurdodau, gwasanaethau brys a safleoedd hanfodol. Gorsafoedd tân
  sy'n cysylltu gyntaf.
- Yn yr Iseldiroedd, fe wnaeth cyngor Hilversum
  [bleidleisio 34 i 1 dros dreial](https://hilversum.nl/nieuwsoverzicht/gemeenteraad-buigt-zich-over-financien)
  gydag ailadroddydd ar dŵr neuadd y dref. Mae'r fwrdeistref
  [yn ei werthuso yn hydref 2027](https://www.spreekbuis.nl/hilversum-start-proef-met-onafhankelijk-noodcommunicatienetwerk-meshcore/).
- Mae dau ranbarth diogelwch yn yr Iseldiroedd, sy'n trefnu'r ymateb i argyfwng,
  yn arbrofi gyda MeshCore:
  [De Limburg](https://nos.nl/nieuwsuur/artikel/2607176-communicatie-hulpdiensten-valt-uit-bij-lange-stroomstoring-oplossing-niet-in-zicht)
  a [Drenthe](https://www.rtvdrenthe.nl/nieuws/18438486/hackerspace-drenthe-werkt-aan-een-noodnetwerk-voor-de-provincie).
  Yn ôl Drenthe, mae'n rhy gynnar i ddweud sut na phryd y gallai ei ddefnyddio.
- Yn Dalfsen, hefyd yn yr Iseldiroedd, mae gwirfoddolwyr
  [yn rhedeg cynllun peilot ochr yn ochr â'r bwrdeistrefi](https://noodnetoverijssel.nl/).
  Maen nhw'n defnyddio radio llais yn gyntaf, a MeshCore fel ail haen ar gyfer testun.

Does neb yn addo y bydd rhywun yn darllen dy neges ar y rhwyll o dy gwmpas.

## O ble mae'r data'n dod {#data}

Mae'r chwiliad ar y dudalen [grwpiau lleol](/community/) yn dod o hyd i le gyda chopi o restrau rhydd lleoedd a chodau post [GeoNames](https://www.geonames.org/), dan drwydded
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Mae'r copi ar y wefan hon. Dydy dy chwiliad byth yn gadael dy ddyfais, a does dim cais yn mynd i GeoNames.
