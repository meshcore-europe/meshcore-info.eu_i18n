---
title: X'inhu MeshCore?
lead: MeshCore jibgħat messaġġi ta' test bir-radju, minn node għal node. Jaħdem mingħajr internet u mingħajr abbonament.
description: 'X''inhu MeshCore u x''mhuwiex: tipi ta'' node, routing, encryption u l-banda ta'' 868 MHz.'
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

MeshCore huwa softwer b'xejn għal radjijiet LoRa żgħar. LoRa hija teknika tar-radju li tibgħat ftit data 'l bogħod, b'ftit li xejn enerġija. Radju bi MeshCore jissejjaħ *node*. Tqabbdu mal-app fuq il-mowbajl jew il-laptop tiegħek, jew tuża l-iskrin u t-tastiera tiegħu stess, u tibgħat test lil nies li jinsabu kilometri 'l bogħod. Bejnek u bejnhom ma hemm l-ebda torri, router jew provider.

Is-softwer huwa open source, u l-iżvilupp tiegħu jsir f'[meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore) taħt il-liċenzja MIT.

## X'mhuwiex MeshCore {#not}

Ir-radju għadu ġdid għalik? Dawn huma l-affarijiet li n-nies l-aktar jistennew minn MeshCore, u li MeshCore ma jagħmilx.

- **Mhuwiex l-internet jew telefon.** MeshCore jibgħat messaġġi tat-test qosra,
  bejn wieħed u ieħor daqs messaġġ tat-test fuq il-mowbajl tiegħek. M'hemmx vuċi, ritratti, vidjo
  jew websajts, u ma tistax tilħaq numru tat-telefon normali.
- **Mhuwiex servizz ta' emerġenza.** L-ebda servizz ta' emerġenza ma jwiegħed li jisma'
  fuq il-mesh. Nafu li l-mesh jista' jaħdem. Jekk jaħdimx f'emerġenza,
  ħadd ma jaf.
- **Mhuwiex immedjat, u mhuwiex kullimkien.** Messaġġ jaqbeż minn radju għal
  radju u jista' jieħu ftit sekondi, jew ma jasal qatt. Jekk jgħaddix
  jiddependi mir-repeaters ta' madwarek, mill-għoli, mill-bini u mill-antenna tiegħek.
  Radju żgħir ġewwa d-dar spiss ma jilħaq lil ħadd. Repeater fuq bejt
  jilħaq kilometri.
- **Mhuwiex servizz li xi ħadd imexxi għalik.** M'hemmx fornitur,
  helpdesk jew wegħda ta' kopertura. Il-mesh jeżisti fejn nies mill-komunità
  tellgħu repeaters.
- **Mhux kollox fuqu huwa privat.** Il-messaġġi diretti huma kriptati, imma
  kulħadd jista' jaqra Public u l-kanali bil-hashtag. L-isem tan-node tiegħek
  u l-pożizzjoni li taqsam jidhru lil kulħadd fil-medda.
  L-[observers](/network/) jirrappurtaw dak li jisimgħu lil mapep pubbliċi.
  Is-[sezzjoni dwar il-kriptaġġ](#encryption) tispjega x'jibqa' privat.
- **Mhuwiex bla limitu.** Kulħadd f'żona jaqsam kanal tar-radju wieħed, u
  r-regoli tal-[band ta' 868 MHz](#band) jillimitaw kemm żmien jista' jibgħat kull radju.
  Kull messaġġ jieħu mill-ħin fl-arja ta' kulħadd l-ieħor, għalhekk bots, adverts frekwenti
  u messaġġi tat-test idewmu l-mesh għal kulħadd.
- **Mhuwiex Meshtastic.** Meshtastic hija sistema differenti li taħdem fuq
  kważi l-istess boards. It-tnejn ma jistgħux jitkellmu ma' xulxin.

## Il-mesh f'minuta {#mesh}

Radju LoRa wieħed jilħaq ftit kilometri f'belt, u ħafna iktar minn fuq għolja jew bejt. Biex jaslu iktar 'il bogħod, ir-radjijiet jgħaddu l-messaġġi għal xulxin: dan huwa *mesh*. F'MeshCore, dan jagħmluh radjijiet imsejħa *repeaters*. Repeater li jisma' messaġġ jibagħtu mill-ġdid, u għalhekk il-messaġġ jista' jaqsam reġjun sħiħ.

Il-mesh mhu ta' ħadd. Kull node u kull repeater huma ta' xi ħadd fil-komunità. Il-mesh jasal sa fejn jaslu r-repeaters tagħhom.

## It-3 tipi ta' node {#roles}

Tagħżel it-tip ta' node meta tagħmillu flash. L-ewwel node tiegħek huwa companion.

**Companion.** Ir-radju tiegħek stess. Tqabbdu mal-app MeshCore fuq il-mowbajl jew il-laptop tiegħek b'Bluetooth jew USB; xi wħud għandhom l-iskrin u t-tastiera tagħhom. Fl-app taqra u tikteb. Il-companion iżomm il-kuntatti u l-kanali tiegħek, u l-messaġġi li waslu meta l-app ma kinitx imqabbda. Companion ma jgħaddix messaġġi għal ħaddieħor.

**Repeater.** Radju mqiegħed f'post għoli li jgħaddi l-messaġġi għal kulħadd. Il-biċċa l-kbira jaħdmu bl-enerġija solari. Ikollok bżonn wieħed tiegħek biss fejn il-mesh għadu ma jasalx. Ma għandux app tiegħu. Tissettjah b'USB, jew tidħol b'password u timmaniġġjah permezz tar-radju. Il-[gwida tar-repeater](/repeater-guide/) turik kif.

**Room server.** Bord żgħir tal-messaġġi fuq il-mesh. Meta tidħol, tirċievi l-posts li tlift meta kont barra l-medda, sal-aħħar 32. Iżommhom fil-memorja biss, għalhekk restart jew qtugħ tad-dawl iħassarhom. Grupp lokali juża wieħed għal avviżi.

## Kif messaġġ isib triqtu {#routing}

Kull node għandu ċavetta sigrieta u ċavetta pubblika. Iċ-ċavetta pubblika hija l-identità tiegħu. Node iħabbar lilu nnifsu b'*advert*: pakkett iffirmat bl-isem tiegħu u, jekk tagħżel, bil-pożizzjoni tiegħu. Xi ħadd jidher fil-kuntatti tiegħek wara li wieħed mill-adverts tiegħu jkun wasal għandek, jew meta tiskennja l-kodiċi QR tiegħu. L-app għandha buttuna biex tibgħat tiegħek.

L-ewwel messaġġ tiegħek lil kuntatt jitlaq bħala *flood*. Kull repeater li jismgħu jgħaddih darba, u fit-triq iżid l-ID qasir tiegħu. It-tweġiba ġġib lura dik il-lista ta' IDs. Minn hemm 'il quddiem, il-messaġġi tiegħek lil dak il-kuntatt isegwu r-rotta rreġistrata, u jibagħtu biss ir-repeaters li jinsabu fuqha. Meta r-rotta tinqata', l-app terġa' tagħmel flood.

Il-messaġġi lil kanal ma għandhomx indirizz wieħed, għalhekk dejjem imorru bħala flood. Ir-repeaters jiftakru dak li għaddew dan l-aħħar u jarmu l-kopji li jerġgħu jaslu minn rotta oħra. Messaġġ jista' jaqsam sa 64 repeater, jew 32 fejn il-preset juża IDs ta' 2 bytes.

## Kriptaġġ u privatezza {#encryption}

Il-messaġġi diretti tiegħek huma kriptati minn tarf għal tarf: ħadd ħliefek u l-persuna l-oħra ma jista' jaqrahom. Repeater jara għal min hu pakkett biss bħala ħjiel ta' 1 byte.

Il-kanali huma kriptati b'ċavetta komuni, għalhekk min jista' jaqrahom jiddependi minn min għandu dik iċ-ċavetta:

- **Public** huwa ssettjat fuq kull companion. Iċ-ċavetta tiegħu hija ppubblikata, għalhekk kulħadd jista' jaqrah.
- **Il-kanali bil-hashtag**, bħal `#utrecht`, jieħdu ċ-ċavetta tagħhom mill-isem. Kull min jaf l-isem jista' jingħaqad, għalhekk ittrattahom ukoll bħala pubbliċi.
- **Il-kanali privati** jużaw ċavetta każwali li taqsamha int stess, pereżempju bħala kodiċi QR.

L-adverts huma ffirmati imma mhux kriptati. L-isem tan-node tiegħek, u l-pożizzjoni tiegħu jekk taqsamha, jidhru lil kulħadd fil-medda. Agħżel isem li ma jgħidx aktar milli trid.

## Il-banda ta' 868 MHz fl-Ewropa {#band}

Fl-Ewropa, MeshCore juża parti żgħira mill-banda ta' 868 MHz, li kulħadd jista' jużaha mingħajr liċenzja. Il-preset Ewropew tar-radju tiegħu, EU/UK (Narrow), jinsab fuq 869.618 MHz, b'kanal ta' 62.5 kHz. Dan jaqa' ġewwa s-sub-banda 869.40-869.65 MHz, li tippermetti sa 500 mW e.r.p. Apparat jista' jibgħat hemm għal mhux aktar minn 10% tal-ħin. It-[taqsima legali tal-gwida tar-repeater](/repeater-guide/#legal) fiha d-dettalji u l-limiti għal kull pajjiż.

Kulħadd f'żona juża l-istess preset, inkella r-radjijiet tagħhom ma jisimgħux lil xulxin. Xi pajjiżi u reġjuni jużaw varjant: il-[grupp lokali tiegħek](/community/) jaf liema.

## Għal xiex jużawh in-nies {#uses}

- Biex tibqa' f'kuntatt waqt il-mixi, fuq il-baħar u fil-festivals fejn in-netwerk
  tal-mowbajl ikun mgħobbi żżejjed jew ma jkunx hemm.
- Kanal ta' riżerva għall-familja jew il-ġirien meta jaqa' d-dawl jew in-netwerks
  tal-mowbajl.
- Riżerva għall-awtoritajiet lokali meta jaqgħu n-netwerks tas-soltu tagħhom.
- Chat lokali fuq radjijiet li huma tan-nies infushom.
- Biex tim tat-tiftix u s-salvataġġ jibqa' f'kuntatt fejn ma hemmx netwerk tal-mowbajl.
  MeshCore SAR, app tal-komunità fuq [Proġetti](/projects/), iżżid mapep u
  pożizzjonijiet kondiviżi.
- Biex mid-dar tiċċekkja sit imbiegħed. Ir-repeaters u s-sensor nodes jirrappurtaw
  il-vultaġġ tal-batterija tagħhom u qari ieħor meta titlobhom.
- Biex tissorvelja sensor. Sensor node iħaddem il-firmware ta' MeshCore biex ikejjel
  l-affarijiet. Iżomm storja tal-vultaġġ tal-batterija tiegħu. Idħol bħala admin u
  jwissik meta l-batterija tkun baxxa. Int iżżid twissijiet għal qari ieħor
  bil-kodiċi tiegħek.
- Biex tixgħel jew titfi xi ħaġa 'l bogħod, bħal pompa. Int iżżid dan fil-firmware
  tas-sensor bil-kodiċi tiegħek.
- Biex tesperimenta bir-radju, l-antenni, l-enerġija solari u s-softwer open source.

Xi awtoritajiet qed jibnu jew jittestjaw sistema ta' riżerva fuq MeshCore. Iċċekkjajna
dawn l-eżempji f'Novembru 2026.

- Iċ-Ċiklun Gabrielle qata' l-komunikazzjonijiet kollha f'Tairāwhiti, New Zealand. F'Settembru
  2025, il-ġestjoni tal-emerġenzi tar-reġjun semmiet lil MeshCore bħala
  [wieħed minn mill-inqas 6 modi ta' riżerva biex tikkomunika](https://www.scoop.co.nz/stories/AK2509/S00669.htm).
  Kienet qed tibni wkoll repeaters bl-enerġija solari bħala s-sinsla tan-netwerk.
- Id-distrett Ġermaniż ta' Bad Kissingen
  [qed jibni netwerk tat-test fuq MeshCore](https://www.landkreis-badkissingen.de/wirtschaft/digitalisierung/kommunikationsnetze/index.html)
  għall-awtoritajiet, is-servizzi tal-emerġenza u siti kritiċi. L-istazzjonijiet
  tat-tifi tan-nar jitqabbdu l-ewwel.
- Il-kunsill ta' Hilversum, fl-Olanda,
  [ivvota 34 kontra 1 favur prova](https://hilversum.nl/nieuwsoverzicht/gemeenteraad-buigt-zich-over-financien)
  b'repeater fuq it-torri tal-muniċipju. Il-muniċipalità
  [tevalwaha fil-ħarifa tal-2027](https://www.spreekbuis.nl/hilversum-start-proef-met-onafhankelijk-noodcommunicatienetwerk-meshcore/).
- Żewġ reġjuni tas-sigurtà Olandiżi, li jorganizzaw ir-rispons għal kriżi, qed
  jesperimentaw b'MeshCore:
  [South Limburg](https://nos.nl/nieuwsuur/artikel/2607176-communicatie-hulpdiensten-valt-uit-bij-lange-stroomstoring-oplossing-niet-in-zicht)
  u [Drenthe](https://www.rtvdrenthe.nl/nieuws/18438486/hackerspace-drenthe-werkt-aan-een-noodnetwerk-voor-de-provincie).
  Drenthe tqis li għadu kmieni wisq biex tgħid kif jew meta tista' tużah.
- F'Dalfsen, ukoll fl-Olanda, voluntiera
  [imexxu proġett pilota flimkien mal-muniċipalitajiet](https://noodnetoverijssel.nl/).
  L-ewwel jużaw ir-radju tal-vuċi, u MeshCore bħala t-tieni saff għat-test.

Jekk il-mesh ta' madwarek jaħdimx f'emerġenza, ħadd ma jaf.

## Minn fejn tiġi d-data {#data}

It-tfittxija fuq il-paġna tal-[gruppi lokali](/community/) ssib post permezz ta' kopja tal-listi b'xejn ta' postijiet u kodiċijiet postali ta' [GeoNames](https://www.geonames.org/), taħt il-liċenzja [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Il-kopja tinsab fuq dan is-sit. It-tfittxija tiegħek qatt ma titlaq mill-apparat tiegħek, u l-ebda talba ma tmur għand GeoNames.
