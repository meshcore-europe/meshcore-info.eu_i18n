---
title: Wat ass MeshCore?
lead: MeshCore schéckt Textmessagen iwwer Funk, vun Node zu Node. Et funktionéiert ouni Internet an ouni Abonnement.
description: 'Wat MeshCore ass a wat net: Node-Typen, Routing, Verschlësselung an d''868-MHz-Band.'
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

MeshCore ass fräi Software fir kleng LoRa-Radioen. LoRa ass eng Funktechnik, déi wéineg Daten op grouss Distanzen iwwerdréit a ganz wéineg Stroum brauch. E Radio mat MeshCore heescht *Node*. Mat der App op dengem Telefon oder Laptop, oder mat sengem eegene Bildschierm a senger Tastatur, schécks du domat Text u Leit, déi Kilometer wäit ewech sinn. Do ass keen Tuerm, Router oder Provider dertëschent.

D'Software ass Open Source. D'Entwécklung leeft op
[meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore) ënner der MIT-Lizenz.

## Wat MeshCore net ass {#not}

Nei beim Funk? Dat hei sinn d'Saachen, déi d'Leit am dackste vu MeshCore erwaarden, an déi et net mécht.

- **Et ass keen Internet a keen Telefon.** MeshCore schéckt kuerz Textmessagen,
  ongeféier sou laang wéi eng SMS op dengem Telefon. Keng Sprooch, keng Fotoen, Videoen
  oder Websäiten, an du kanns keng normal Telefonsnummer erreechen.
- **Et ass keen Noutdéngscht.** Keen Noutdéngscht versprécht, um Mesh
  nozelauschteren, a keen versprécht, datt een deng Message liest.
- **Et ass net direkt, an net iwwerall.** Eng Message spréngt vu Radio zu
  Radio a ka e puer Sekonne brauchen, oder guer net ukommen. Ob se duerchkënnt,
  hänkt vun de Repeateren ronderëm dech of, vun der Héicht, de Gebaier an
  denger Antenn. E klenge Radio am Haus erreecht dacks keen; e Repeater op
  engem Daach kënnt Kilometer wäit.
- **Et ass keen Déngscht, deen een fir dech bedreift.** Et gëtt kee Provider,
  keen Helpdesk a kee Verspriechen iwwer d'Ofdeckung. De Mesh gëtt et do, wou
  Leit aus der Communautéit Repeateren opgestallt hunn.
- **Net alles drop ass privat.** Direktmessage si verschlësselt, mee Public an
  d'Hashtag-Kanäl kann jiddereen liesen, an den Numm vun dengem Node an deng
  gedeelte Positioun gesäit jiddereen a Reechwäit.
  [Observeren](/network/) mellen op ëffentleche Kaarten, wat se héieren.
  D'[Sektioun iwwer d'Verschlësselung](#encryption) erkläert, wat privat bleift.
- **Et ass net onbegrenzt.** Jiddereen an engem Gebitt deelt ee Funkkanal, an
  d'Reegele fir d'[868-MHz-Band](#band) limitéieren, wéi laang all Radio
  schécken däerf. All Message hëlt deenen aneren Sendezäit ewech, dofir maache
  Bots, heefeg Adverts an Testmessagen de Mesh fir jiddereen méi lues.
- **Et ass net Meshtastic.** Meshtastic ass en anere System, deen op
  gréisstendeels deene selwechte Boards leeft. Déi zwee kënnen net matenee schwätzen.

## De Mesh an enger Minutt {#mesh}

E LoRa-Radio erreecht an enger Stad e puer Kilometer, a vun engem Hiwwel oder Daach aus vill méi wäit. Fir méi wäit ze kommen, ginn d'Radioe Message fireneen weider: dat ass e *Mesh*. Bei MeshCore maachen dat Radioen, déi *Repeateren* heeschen. E Repeater, deen e Message héiert, schéckt en nach eng Kéier, sou kann en eng ganz Regioun duerchqueren.

Kengem gehéiert de Mesh. All Node an all Repeater gehéiert engem aus der Communautéit. De Mesh geet sou wäit wéi hir Repeateren.

## Déi 3 Zorte vun Noden {#roles}

Du wiels d'Zort vun engem Node, wann s du e flashs. Däin éischten Node ass e Companion.

**Companion.** Däin eegene Radio. Du verbënns en iwwer Bluetooth oder USB mat der MeshCore-App op dengem Telefon oder Laptop; verschiddener hunn en eegene Bildschierm an eng eegen Tastatur. An der App liess a schreifs du. De Companion späichert deng Kontakter a Kanäl, an och d'Messagen, déi ukomm sinn, wärend d'App net verbonnen war. E Companion gëtt keng Message fir anerer weider.

**Repeater.** E Radio, deen héich steet a Message fir jiddereen weiderschéckt. Déi meescht lafe mat Solarenergie. Däin eegene brauchs du nëmmen do, wou de Mesh nach net hikënnt. En huet keng eegen App. Du riichts en iwwer USB an, oder du logges dech mat engem Passwuert an a verwalts en iwwer Funk. De [Repeater-Guide](/repeater-guide/) weist, wéi dat geet.

**Room Server.** E klengt Message-Board um Mesh. Wann s du dech aloggs, kriss du d'Posts, déi s du verpasst hues, wärend s du ausser Reechwäit waars, bis zu de leschten 32. En hält se nëmmen am Späicher, also läscht e Restart oder e Stroumausfall se. Eng lokal Grupp benotzt esou ee fir Ukënnegungen.

## Wéi e Message säi Wee fënnt {#routing}

All Node huet e geheime Schlëssel an en ëffentleche Schlëssel. Den ëffentleche Schlëssel ass seng Identitéit. E Node mellt sech mat engem *Advert*: engem signéierte Paket mat sengem Numm an, wann s du dat wëlls, senger Positioun. Een erschéngt an denge Kontakter, nodeems ee vu sengen Adverten dech erreecht huet, oder wann s du säi QR-Code scanns. An der App gëtt et e Knäppchen, fir däin eegenen ze schécken.

Däin éischte Message un e Kontakt geet als *Flood* eraus. All Repeater, deen en héiert, gëtt en eemol weider a setzt ënnerwee seng eege kuerz ID derbäi. D'Äntwert bréngt dës Lëscht vun IDen zeréck. Vun do u ginn deng Messagen un dee Kontakt iwwer déi opgezeechent Route, an nëmmen d'Repeateren op där Route schécken. Wann d'Route ofbrécht, schéckt d'App erëm e Flood.

Messagen un e Kanal hu keng eenzel Adress, dofir gi se ëmmer als Flood eraus. Repeateren erënnere sech drun, wat se viru Kuerzem weiderginn hunn, a geheie Kopien ewech, déi nach eng Kéier iwwer en anere Wee ukommen. E Message ka bis zu 64 Repeateren duerchqueren, oder 32, wou de Preset 2-Byte-IDe benotzt.

## Verschlësselung a Privatsphär {#encryption}

Deng Direktmessage si vun Enn zu Enn verschlësselt: nëmmen du an déi aner Persoun kënnen se liesen. Fir wien e Paket ass, gesäit e Repeater nëmmen als Hiweis vun 1 Byte.

Kanäl si mat engem gemeinsame Schlëssel verschlësselt. Wien se liese kann, hänkt also dovun of, wien dee Schlëssel huet:

- **Public** ass op all Companion agestallt. Säi Schlëssel ass publizéiert, also ka jiddereen e liesen.
- **Hashtag-Kanäl**, wéi `#utrecht`, huelen hire Schlëssel aus hirem Numm. Jiddereen, deen den Numm kennt, ka matmaachen, dofir behandel se och als ëffentlech.
- **Privat Kanäl** benotzen en zoufällege Schlëssel, deen s du selwer deels, zum Beispill als QR-Code.

Adverte si signéiert, awer net verschlësselt. Den Numm vun dengem Node, a seng Positioun, wann s du se deels, gesäit jiddereen a Reechwäit. Wiel en Numm, dee net méi verréit, wéi s du wëlls.

## De Band vun 868 MHz an Europa {#band}

An Europa benotzt MeshCore e klengen Deel vum Band vun 868 MHz, deen jiddereen ouni Lizenz benotze dierf. Säi europäesche Radio-Preset, EU/UK (Narrow), läit op 869.618 MHz op engem Kanal vu 62.5 kHz. Dat ass am Ënnerband 869.40-869.65 MHz, deen bis zu 500 mW e.r.p. erlaabt. En Apparat dierf do héchstens 10% vun der Zäit schécken. An der
[juristescher Sektioun vum Repeater-Guide](/repeater-guide/#legal) stinn d'Detailer an d'Limitte pro Land.

Jiddereen an enger Regioun benotzt de selwechte Preset, soss kënnen d'Radioe sech net héieren. Verschidde Länner a Regioune benotzen eng Variant: deng
[lokal Grupp](/community/) weess, wéi eng.

## Wofir d'Leit et benotzen {#uses}

- Kontakt halen op Wanderungen, um Mier an op Festivallen, wou de Mobilfunknetz
  iwwerlaascht ass oder feelt.
- E Reservekanal fir d'Famill oder d'Noperen, wann de Stroum oder de Mobilfunknetz
  ausfält.
- Eng Reserve fir lokal Behörden, wann hir gewéinlech Netzer ausfalen.
- Lokale Chat op Funkgeräter, déi d'Leit selwer besëtzen.
- Eng Sich- a Rettungsequipe a Kontakt halen, wou et kee Mobilfunknetz gëtt.
  MeshCore SAR, eng App vun der Communautéit op [Projeten](/projects/), bréngt
  Kaarten a gedeelte Positiounen derbäi.
- Vun doheem aus e wäiten Uert kontrolléieren. Repeateren a Sensor-Noden mellen
  hir Batteriespannung an aner Moosswäerter, wann s du se froes.
- E Sensor iwwerwaachen. Op engem Sensor-Node leeft d'MeshCore-Firmware fir
  Miessungen. En späichert de Verlaf vu senger Batteriespannung. Wann s du
  dech als Admin aloggs, warnt en dech, wann d'Batterie schwaach gëtt. Fir aner
  Moosswäerter setz du Warnunge mat dengem eegene Code derbäi.
- Eppes wäit ewech schalten, zum Beispill eng Pomp. Dat setz du mat dengem
  eegene Code an d'Sensor-Firmware derbäi.
- Experimentéiere mat Funk, Antennen, Solarenergie an Open-Source-Software.

Verschidden Autoritéite bauen oder testen e Backup op Basis vu MeshCore. Mir hunn dës
Beispiller am November 2026 nogekuckt.

- De Zyklon Gabrielle huet an Tairāwhiti, an Neiséiland, all Kommunikatioun ënnerbrach. Am
  September 2025 huet de Katastropheschutz vun der Regioun MeshCore
  [ee vu mindestens 6 Reservewee fir d'Kommunikatioun](https://www.scoop.co.nz/stories/AK2509/S00669.htm) genannt.
  Hien huet och Repeateren mat Solarenergie als Réckgrat opgebaut.
- Den däitsche Landkrees Bad Kissingen
  [baut en Textnetz op MeshCore op](https://www.landkreis-badkissingen.de/wirtschaft/digitalisierung/kommunikationsnetze/index.html)
  fir Behörden, Noutdéngschter a kritesch Standuerter. D'Pompjeescasernen
  ginn als éischt ugeschloss.
- De Gemengerot vun Hilversum, an Holland, huet
  [mat 34 géint 1 fir e Versuch gestëmmt](https://hilversum.nl/nieuwsoverzicht/gemeenteraad-buigt-zich-over-financien),
  mat engem Repeater um Tuerm vum Stadhaus. D'Gemeng
  [evaluéiert de Versuch am Hierscht 2027](https://www.spreekbuis.nl/hilversum-start-proef-met-onafhankelijk-noodcommunicatienetwerk-meshcore/).
- Zwou hollännesch Sécherheetsregiounen, déi bei enger Kris den Asaz organiséieren,
  experimentéiere mat MeshCore:
  [Süd-Limbuerg](https://nos.nl/nieuwsuur/artikel/2607176-communicatie-hulpdiensten-valt-uit-bij-lange-stroomstoring-oplossing-niet-in-zicht)
  an [Drenthe](https://www.rtvdrenthe.nl/nieuws/18438486/hackerspace-drenthe-werkt-aan-een-noodnetwerk-voor-de-provincie).
  Drenthe seet, et wier ze fréi fir ze soen, wéi oder wéini et MeshCore asetze kéint.
- Zu Dalfsen, och an Holland,
  [maache Fräiwëlleger zesumme mat de Gemengen e Pilotprojet](https://noodnetoverijssel.nl/).
  Si setzen als éischt op Sprechfunk a benotzen MeshCore als zweet Schicht fir Text.

Keen verspriécht, datt een deng Message am Mesh an denger Ëmgéigend liest.

## Wou d'Donnéeën hierkommen {#data}

D'Sich op der Säit [lokal Gruppen](/community/) fënnt eng Plaz mat enger Kopie vun de fräie Lëschte vu Plazen a Postleitzuele vu [GeoNames](https://www.geonames.org/), déi ënner der Lizenz
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) stinn. D'Kopie läit op dësem Site. Deng Sich verléisst ni däin Apparat, a keng Ufro geet u GeoNames.
