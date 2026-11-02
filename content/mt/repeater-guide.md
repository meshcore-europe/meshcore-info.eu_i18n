---
title: Gwida għar-ripetituri
lead: Ripetitur f'post għoli jgħaddi l-messaġġi għal kulħadd madwaru, madwar belt jew wied sħiħ. Agħżel il-post, ħaddmu bix-xemx, ikkonfigurah u ibqa' fil-limiti tal-liġi.
description: 'Ippjana, agħti l-enerġija, ikkonfigura u ħaddem ripetitur MeshCore skont il-liġi fl-Ewropa: l-għażla tal-post, id-daqs tas-sistema solari, is-settings tas-CLI, u l-limiti tal-qawwa u tad-duty cycle fuq 868 MHz.'
eyebrow: 868 MHz · sa 500 mW · mingħajr liċenzja
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '7c7e3be3'
  seeded: '2026-11-02'
  fields: {title: '4608abcd', lead: 'bc670c65', description: '9e483ce5', eyebrow: '9fd33416'}
  sections: ['05ee477a', '938c518c', '766086be', '70faf508', '8bc641aa', '399cd683', 'e9dedb7b', '92beca03', '17634750', 'cadf6024', 'e9cc6834', '2e6e59ca', 'fb44b8db']
  blocks: ['20ac0371', 'ed2b1adf', '432543ee', '7af42c89', 'd0f7543a', '9ef3580f', '3476aef7', '1bab7bec', '6a7c4493', 'dbd9fa1f', 'aa06d32b', '9958aad3', 'd162b028', 'cca1bbdf', '64ef011d', 'e7f16724', 'd2e34ff0', 'bb195cfc', '8d080bb3', '2b1d995b', '210f1b66', 'dc7419d2', 'bdc66db0', 'b59f248c', '7184bd63', 'de5a24f9', 'f5cfb426', '48c7422f', '9d3c0836', 'da8a6af3', '240126df', '8aac2b33', '81a475b8', 'a53e42b5', '36ff1db4', 'e4ca8602', 'e4594afd', '3b24b8e9', '58330858', '68f2966e', 'd7418228', '23536e60', 'cbc5c2d1', '2ea02ba9', '92540256', '6e21f681', 'a8c12311', '3382ae7f', 'cdeafb0f', '1b1319d2']
---

Ir-ripetituri huma s-sinsla tal-mesh. Il-companions, ir-radjijiet li minnhom tibgħat il-messaġġi, ma jgħaddux il-messaġġi 'l quddiem. Għalhekk, mingħajr ripetituri tilħaq biss lin-nies fil-medda diretta tiegħek. Ripetitur fil-post it-tajjeb ikabbar il-mesh għal kulħadd madwaru. Din il-gwida ssegwi l-firmware MeshCore v1.18.0.

Qabel ma tibda, kellem lill-[grupp lokali](/community/) tiegħek. Il-grupp jaf fejn hemm nuqqas ta' kopertura, liema [preset tuża ż-żona tiegħek](/guides/settings/) u kif jissemmew ir-ripetituri. Fittex ir-ripetituri qrib tiegħek fuq il-[mapep tal-kopertura](/map/), u sellem fuq il-[kanali](/guides/channels/) pubbliċi jew lokali.

## Għandek bżonn wieħed? {#need}

Ripetitur jerġa' jibgħat kull messaġġ flood li jisma', u r-ripetituri kollha fil-medda jaqsmu l-istess ħin fuq l-arja. Fejn il-mesh diġà jilħqek, ripetitur ieħor iżid it-traffiku, mhux il-kopertura. Companion f'post għoli, f'tieqa tal-attic jew fuq gallarija, jista' jkun biżżejjed.

Waħħal ripetitur fejn hemm nuqqas ta' kopertura:

- il-[mapep tal-kopertura](/map/) ma juru l-ebda ripetitur qrib tiegħek, jew juru biss ripetituri li l-companion tiegħek ma jismax;
- il-grupp lokali tiegħek jgħid li ż-żona għandha bżonn wieħed.

## Agħżel il-post {#site}

L-għoli jgħodd aktar mill-qawwa. LoRa fuq 868 MHz jasal l-aħjar f'linja tal-vista ħielsa. L-għoljiet, il-binjiet u s-siġar fitti jnaqqsu l-medda ferm aktar milli jistgħu jpattu ftit milliwatts żejda.

- **Itla' fl-għoli.** Bejt, arblu, bini għoli jew għolja jkopru ferm aktar minn xifer it-tieqa. Anki ftit metri fuq il-bjut ta' madwarek jgħinu.
- **Żomm l-antenna fil-miftuħ.** Waħħalha ogħla mit-truf tal-bejt, 'il bogħod minn metall, kanali tal-ilma u antenni oħra.
- **Iċċekkja l-veduta.** Għodod bħal [HeyWhatsThat](https://www.heywhatsthat.com/) juruk x'jidher minn post partikolari. Jekk tista' tara post, ripetitur hemmhekk ikun fil-medda.
- **Ħalli spazju ħieles.** Mogħdija tar-radju teħtieġ ftit spazju ħieles madwar il-linja diretta, mhux il-linja biss. Fuq distanzi twal, nofs il-mogħdija għandu jgħaddi diversi metri 'l fuq mill-ostakli.
- **Itlob il-permess.** Ikseb il-kunsens tas-sid tal-bejt jew tal-arblu, u ftiehem kif se tilħaq ir-ripetitur għall-manutenzjoni.

## Hardware {#hardware}

- **Bord.** Agħżel bord nRF52 li juża ftit enerġija, bħall-[Heltec T114](/devices/), RAK WisBlock jew is-SenseCAP Solar Node. Il-bordijiet ESP32 jużaw aktar enerġija (il-paġna tal-apparati timmarkahom High), u għalhekk huwa diffiċli tħaddimhom bix-xemx.
- **Antenna.** Uża antenna magħmula għal 868 MHz u waħħalha vertikali. Il-[gwida tal-antenni](/guides/antenna/) tispjega t-tipi, il-konnetturi, il-kejbil u t-twaħħil. Il-gain tal-antenna jgħodd għal-limitu legali tal-qawwa: ara [Il-limiti legali](#legal).
- **Kejbil.** Żomm il-kejbil koassjali qasir, jew uża kejbil b'telf baxx. Fuq 868 MHz, ftit metri ta' kejbil irqiq jistgħu jitilfu nofs il-qawwa tiegħek.
- **Kaxxa.** Kaxxa li tiflaħ it-temp (IP65 jew aħjar) b'cable gland, toqba tal-arja jew tad-drenaġġ kontra l-kondensazzjoni, u kulur ċar jew dell mix-xemx. Il-batteriji jbatu fis-sħana, u ma tistax tiċċarġjahom taħt iż-żero.
- **Sajjetti.** Antenna fuq il-bejt hija mira għas-sajjetti. Imxi mar-regoli lokali dwar l-ertjar, jew waħħalha f'post fejn sajjetta ma tilħaqx il-wajers tal-bini.

## L-enerġija u d-daqs tas-sistema solari {#power}

Ripetitur solari jrid jiflaħ għall-aktar ġimgħat mudlama tax-xitwa. Ikkalkula d-daqs tas-sistema skont dawk il-ġimgħat:

1. **Kejjel il-konsum.** Ħaddem ir-ripetitur ikkonfigurat għal ġurnata permezz ta' miter tal-enerġija USB. Aqra l-enerġija użata f'watt-sigħat (Wh). It-traffiku fiż-żona tiegħek ibiddel in-numru, għalhekk kejjel fuq il-post jekk tista'.
2. **Żid riżerva.** Ippjana l-kapaċità tal-batterija għal mill-inqas 5 sa 7 ijiem mingħajr xemx utli.
3. **Sib ix-xemx tax-xitwa fiż-żona tiegħek.** L-[għodda PVGIS](https://re.jrc.ec.europa.eu/pvg_tools/en/) b'xejn tal-UE turik, għal kull post, kemm enerġija jipproduċi pannell kull xahar. Uża x-xahar bl-inqas xemx.
4. **Agħżel id-daqs tal-pannell.** Il-pannell irid jagħmel tajjeb għall-konsum ta' kull jum f'dak l-agħar xahar, b'marġni għat-telf waqt l-iċċarġjar.

Eżempju maħdum, b'numri preżunti: ripetitur li juża 1 Wh kuljum jeħtieġ batterija ta' mill-inqas 7 Wh għal ġimgħa ta' riżerva, madwar 2 Ah ta' kapaċità li tista' tintuża f'3.7 V. Jekk PVGIS jgħid li pannell ta' 1 W fil-post tiegħek jagħti 0.5 Wh kuljum f'Diċembru, għandek bżonn pannell ta' mill-inqas 2 W. Pannell ta' 3 sa 5 W iħalli marġni għas-sħab, għas-silġ u għat-tixjiħ.

## Ikkonfigurah {#config}

**Installa l-firmware.** Uża l-[web flasher](https://flasher.meshcore.io) u agħżel il-firmware **Repeater** għall-bord tiegħek. Il-passi tal-installazzjoni tal-firmware tinsabhom f'[Ibda](/get-started/#flash).

**Ikkonfigurah bl-USB.** Waqt li r-ripetitur għadu mqabbad mal-kompjuter, iftaħ [config.meshcore.io](https://config.meshcore.io) jew il-console tal-flasher. Tista' tuża wkoll kwalunkwe terminal serjali fuq 115200 baud. Dawn huma l-aktar kmandi importanti:

| X'tagħmel | Kmand |
|---|---|
| Ibdel il-password tal-admin | `password <new password>` |
| Agħtih isem | `set name <name>` |
| Preset tar-radju: frekwenza, bandwidth, SF, CR (agħmel reboot biex jidħol fis-seħħ) | `set radio 869.618,62.5,8,8` |
| Limitu tad-duty cycle, f'perċentwal | `set dutycycle 10` |
| Qawwa tat-trażmissjoni taċ-ċippa tar-radju, f'dBm | `set tx <dBm>` |
| Pożizzjoni, biex jidher fuq il-mapep | `set lat <degrees>` u `set lon <degrees>` |
| Dettalji ta' kuntatt għal operaturi oħra | `set owner.info <text>` |
| Sigħat bejn il-flood adverts, dawk li jismagħhom il-mesh kollu | `set flood.advert.interval <hours>` |
| Ħabbru issa | `advert` |
| Erġa' ibdih | `reboot` |

Il-password default tal-admin hija `password`, u kull min jidħol biha jsir admin. Ibdilha qabel ma r-ripetitur jibda jittrażmetti.

L-eżempju ta' `set radio` hawn fuq huwa EU/UK (Narrow). Minflok, uża l-valuri tal-preset taż-żona tiegħek: [Is-settings rakkomandati](/guides/settings/) jelenkawhom skont il-pajjiż.

**Issettja l-arloġġ.** Mingħajr modulu tal-arloġġ (RTC), ripetitur jitlef il-ħin f'kull qtugħ tad-dawl u jerġa' jibda minn Mejju 2024. Waqt li jkun qed jaħdem, l-arloġġ tiegħu jitbiegħed ukoll mill-ħin it-tajjeb: jimxi dejjem aktar 'il quddiem jew lura. Għalhekk, issettja l-arloġġ minn żmien għal żmien: idħol mill-bogħod mill-app u uża `clock sync`, jew issettja l-ħin bl-USB. B'modulu RTC, rari jkollok bżonn tagħmel dan: il-modulu jżomm il-ħin waqt qtugħ tad-dawl u l-ħin jitbiegħed ferm inqas.

**Immaniġġjah mill-bogħod.** Ladarba jkun fuq il-mesh, idħol mill-app MeshCore bil-password tal-admin. Hemmhekk taqra l-istatus tiegħu u tuża l-istess kmandi bir-radju. Xi kmandi jaħdmu bl-USB biss, bħal `set freq` u r-reset tal-fabbrika `erase`.

**Żomm l-identità tiegħu.** Qabel ma tagħmel erase, ikteb `get prv.key` bl-USB u żomm iċ-ċavetta privata li jurik f'post sigur. Wara l-erase, `set prv.key <key>` u `reboot` jagħtu lura lir-ripetitur l-identità l-qadima tiegħu. Hekk, in-nodi li jafuh isibuh taħt l-istess prefiss.

Il-lista sħiħa tal-kmandi tinsab fir-[referenza tas-CLI ta' MeshCore](https://github.com/meshcore-dev/MeshCore/blob/main/docs/cli_commands.md).

## Aġġornah fuq l-arja {#update}

Ladarba r-ripetitur ikun fl-għoli, taġġornah mill-art. Idħol mill-app MeshCore bil-password tal-admin, iftaħ il-linja tal-kmandi tiegħu u ikteb `start ota`. Dak li jiġri wara jiddependi mill-bord. Bordijiet oħra jwieġbu `Error`, u dawk taġġornahom bl-USB.

**Bordijiet nRF52**, bħal RAK, Heltec T114, Seeed XIAO u SenseCAP Solar:

1. Niżżel iż-**ZIP** tal-firmware il-ġdid għall-bord tiegħek mill-[web flasher](https://flasher.meshcore.io).
2. Ikteb `start ota`. Ir-ripetitur iwieġeb `OK` u jidher fuq Bluetooth bħala `<board>_OTA`, pereżempju `RAK4631_OTA`.
3. Iftaħ l-app nRF Device Firmware Update fuq it-telefon, agħżel iż-ZIP u r-ripetitur, u tella' l-fajl. Dan jieħu ftit minuti.

Installa l-[bootloader OTAFIX](https://github.com/oltaco/Adafruit_nRF52_Bootloader_OTAFIX) fuq bord nRF52 qabel ma ttellgħu fl-għoli. Bil-bootloader oriġinali, aġġornament li jfalli jista' jissewwa biss bl-USB. Bl-OTAFIX, il-bord jerġa' lura għall-modalità tal-aġġornament, u terġa' tipprova fuq Bluetooth.

**Bordijiet ESP32**, bħall-Heltec V3 u V4:

1. Niżżel il-`.bin` **non-merged** għall-bord tiegħek mill-web flasher: il-fajl li f'ismu m'hemmx "merged".
2. Ikteb `start ota`. Ir-ripetitur jiftaħ network WiFi bl-isem `MeshCore-OTA` u jwieġeb bl-indirizz tal-paġna tat-tlugħ.
3. Fil-medda tal-WiFi, qabbad it-telefon jew il-laptop ma' dak in-network, iftaħ l-indirizz u tella' l-fajl.

## Il-limiti legali {#legal}

{{< callout type="legal" verified="2026-10-02" >}}
Il-presets Ewropej ta' MeshCore jinsabu fis-sottobanda **869.40-869.65 MHz**. Fl-UE, fir-Renju Unit, fl-Isvizzera u fin-Norveġja, din is-sottobanda hija miftuħa għal apparati ta' medda qasira mingħajr liċenzja, f'dawn il-limiti:

- qawwa radjata ta' mhux aktar minn **500 mW e.r.p.**;
- **duty cycle ta' mhux aktar minn 10%**: mhux aktar minn 360 sekonda ta' trażmissjoni f'kull siegħa, għal kull apparat. Inkella, apparat jista' juża listen-before-talk b'adaptive frequency agility, kif iddefinit f'ETSI EN 300 220-2;
- is-sinjal kollu, b'wisa' ta' mhux aktar minn 250 kHz, irid jibqa' ġewwa s-sottobanda.

Il-banda hija maqsuma ma' oħrajn: ma tistax tfixkel servizzi b'liċenzja, u oħrajn jistgħu jfixklu lilek.
Ir-radju jrid ikollu l-marka CE (fil-Gran Brittanja, CE jew UKCA).
{{< /callout >}}

Sorsi: [CEPT ERC Recommendation 70-03](https://docdb.cept.org/document/845), Anness 1, banda h1.7; [Deċiżjoni tal-Kummissjoni 2006/771/KE](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02006D0771(01)-20250123) u l-emendi tagħha; [ETSI EN 300 220-2](https://www.etsi.org/deliver/etsi_en/300200_300299/30022002/03.03.01_60/en_30022002v030301p.pdf), banda O.

### Il-qawwa: e.r.p. u l-antenna tiegħek {#erp}

Il-limitu japplika għall-qawwa *radjata*, imkejla meta mqabbla ma' antenna dipol sempliċi (e.r.p.). Il-gain tal-antenna jgħodd, u t-telf fil-kejbil jitnaqqas. Il-manifatturi jagħtu l-gain tal-antenna f'dBi, li huwa 2.15 dB aktar mill-istess gain f'dBd (meta mqabbel ma' dipol). Żomm din is-somma f'27 dBm (500 mW) jew inqas:

> qawwa tat-trażmissjoni (dBm) + gain tal-antenna (dBi) − telf fil-kejbil (dB) − 2.15 ≤ 27

- Bord li jittrażmetti 22 dBm f'antenna ta' 5 dBi permezz ta' kejbil b'telf ta' 1 dB: 22 + 5 − 1 − 2.15 = 23.85 dBm, madwar 240 mW e.r.p. Fi ħdan il-limitu.
- Bord b'amplifikatur ta' 30 dBm (1 W) f'antenna ta' 3 dBi: 30 + 3 − 2.15 = 30.85 dBm, madwar 1.2 W e.r.p. Aktar mil-limitu: naqqas il-qawwa tat-trażmissjoni.

`set tx` jissettja l-output taċ-ċippa LoRa, f'dBm. Iċ-ċippa SX1262 innifisha tilħaq massimu ta' 22 dBm, u l-firmware ma jiċċekkjax in-numru li ddaħħal. Bordijiet b'amplifikatur addizzjonali, bħall-Heltec V4 jew l-Station G2, jittrażmettu ferm aktar min-numru li tissettja. Iċċekkja t-tabella tal-manifattur qabel ma tissettjah, u ibda baxx.

### Duty cycle {#duty-cycle}

Ripetitur jittrażmetti għal kulħadd madwaru, għalhekk juża l-ħin fuq l-arja tiegħu aktar malajr minn companion. Il-limitatur tad-duty cycle ta' MeshCore ikun fuq 50% b'mod default, aktar milli tippermetti din il-banda. Issettjah għal 10% fuq kull ripetitur:

```text
set dutycycle 10
```

### Il-preċiżjoni tal-frekwenza {#frequency}

Il-kanal EU/UK (Narrow), 869.618 MHz b'bandwidth ta' 62.5 kHz, jasal sa 869.649 MHz: inqas minn 1 kHz taħt il-limitu ta' fuq tas-sottobanda. Is-sinjal irid jibqa' ġewwa l-banda f'kull temperatura. Għal dan hemm bżonn kristall ikkumpensat għat-temperatura (TCXO). Kważi kull bord attwali għandu wieħed. Bordijiet eqdem mingħajru, bħall-Heltec V2, jitbiegħdu wisq mill-frekwenza biex jaħdmu b'mod affidabbli fuq 62.5 kHz.

### Noti skont il-pajjiż {#countries}

- **L-Istati Membri tal-UE** iridu jagħmlu din is-sottobanda disponibbli b'dawn il-kundizzjonijiet (Deċiżjoni 2006/771/KE, Artikolu 3).
- **Ir-Renju Unit:** l-istess limiti, f'[IR 2030](https://www.ofcom.org.uk/spectrum/radio-equipment/short-range-devices) ta' Ofcom.
- **L-Isvizzera u l-Liechtenstein:** l-istess limiti, f'[RIR1008-09](https://www.ofcomnet.ch/api/rir/1008/09) ta' OFCOM.
- **In-Norveġja:** l-istess limiti, fir-[regolament dwar l-awtorizzazzjonijiet ġenerali](https://lovdata.no/dokument/SF/forskrift/2012-01-19-77) (fribruksforskriften).

Dawn in-noti mhumiex parir legali. Ir-regoli jinbidlu. Jekk ikollok xi dubju, iċċekkja mar-regolatur nazzjonali tiegħek.

## Lista ta' kontroll għat-twaħħil {#checklist}

- [ ] Sid il-post ta l-kunsens, u tista' tilħaq ir-ripetitur għall-manutenzjoni.
- [ ] Il-bord iħaddem il-firmware **Repeater**, u qabbadt l-antenna qabel l-ewwel tixgħil.
- [ ] Biddilt il-password tal-admin.
- [ ] Ir-radju jaqbel mal-[preset taż-żona tiegħek](/guides/settings/) (`get radio`).
- [ ] Issettjajt `set dutycycle 10`.
- [ ] Il-qawwa tat-trażmissjoni flimkien mal-gain tal-antenna tibqa' fil-limitu ta' 500 mW e.r.p.
- [ ] Issettjajt l-isem, il-pożizzjoni u `owner.info`, biex oħrajn ikunu jafu min iħaddmu.
- [ ] Issettjajt l-arloġġ (`clock`).
- [ ] Il-kaxxa hija ssiġillata, b'toqba tad-drenaġġ jew tal-arja, u l-kejbil għandu drip loop.
- [ ] Id-daqs tal-batterija u tal-pannell jlaħħaq mal-agħar xahar tax-xitwa.
- [ ] Ittestjajtu mill-bogħod bl-app qabel ma tlaqt mill-post.
- [ ] Il-grupp lokali tiegħek jaf li r-ripetitur qed jaħdem.
