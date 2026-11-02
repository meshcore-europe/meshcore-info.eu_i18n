---
title: Wat ass MeshCore?
lead: MeshCore schéckt Textmessagen iwwer Funk, vun Node zu Node. Et funktionéiert ouni Internet an ouni Abonnement.
description: 'Wat MeshCore ass a wat net: de Mesh, Companions, Repeateren a Room Serveren, Routing, Verschlësselung an de Band vun 868 MHz an Europa.'
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

MeshCore ass fräi Software fir kleng LoRa-Radioen. LoRa ass eng Funktechnik, déi wéineg Daten op grouss Distanzen iwwerdréit a ganz wéineg Stroum brauch. E Radio mat MeshCore heescht *Node*. Mat der App op dengem Telefon oder Laptop, oder mat sengem eegene Bildschierm a senger Tastatur, schécks du domat Text u Leit, déi Kilometer wäit ewech sinn. Do ass keen Tuerm, Router oder Provider dertëschent.

D'Software ass Open Source. D'Entwécklung leeft op
[meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore) ënner der MIT-Lizenz.

## Wat MeshCore net ass {#not}

Nei beim Funk? Dat hei sinn d'Saachen, déi d'Leit am dackste vu MeshCore erwaarden, an déi et net mécht.

- **Et ass keen Internet an och keen Telefon.** MeshCore schéckt kuerz Textmessagen, ongeféier sou laang wéi eng SMS op dengem Telefon. Keng Stëmm, keng Fotoen, kee Video a keng Websäiten, an du kanns keng normal Telefonsnummer erreechen.
- **Et ass keen Noutdéngscht.** Keen Noutdéngscht lauschtert um Mesh, a kee verspriecht, datt een däi Message liest. Am Noutfall ruffs du 112 un.
- **Et geet net direkt an net iwwerall.** E Message spréngt vu Radio zu Radio a kann e puer Sekonnen daueren oder guer net ukommen. Ob e duerchkënnt, hänkt vun de Repeateren ronderëm dech of, vun der Héicht, vu Gebaier a vun denger Antenn. E klenge Radio dobannen erreecht dacks keen; e Repeater op engem Daach kënnt Kilometer wäit.
- **Et ass kee Service, deen een fir dech bedreift.** Et gëtt kee Provider, keen Helpdesk a keng Garantie op Ofdeckung. De Mesh gëtt et do, wou Leit aus der Communautéit Repeateren opgestallt hunn, an néierens soss.
- **Net alles dorop ass privat.** Direktmessage si verschlësselt, awer Public an d'Hashtag-Kanäl ka jidderee liesen, an den Numm vun dengem Node a seng gedeelte Positioun gesäit jiddereen a Reechwäit. [Observers](/network/) mellen dat, wat se héieren, un ëffentlech Kaarten. D'[Sektioun iwwer d'Verschlësselung](#encryption) erkläert, wat privat bleift.
- **Et ass net onlimitéiert.** Jiddereen an enger Regioun deelt ee Funkkanal, an d'Reegele fir de [Band vun 868 MHz](#band) limitéieren, wéi laang all Radio schécke dierf. All Message hëlt deenen aneren Sendezäit ewech, dofir maachen Bots, heefeg Adverten an Testmessagen de Mesh fir jiddereen méi lues.
- **Et ass net Meshtastic.** Meshtastic ass en anere System, deen op bal deene selwechte Boards leeft. Déi zwee kënnen net matenee schwätzen.

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

- A Kontakt bleiwen op Trëppelturen, um Mier an op Festivalen, wou d'Mobilnetz iwwerlaascht ass oder feelt.
- E Backup-Kanal fir Famill oder Noperen, wann de Stroum oder d'Mobilnetz ausfalen.
- Lokale Chat op Radioen, déi d'Leit selwer besëtzen.
- Experimentéiere mat Funk, Antennen, Solarenergie an Open-Source-Software.

## Wou d'Donnéeën hierkommen {#data}

D'Sich op der Säit [lokal Gruppen](/community/) fënnt eng Plaz mat enger Kopie vun de fräie Lëschte vu Plazen a Postleitzuele vu [GeoNames](https://www.geonames.org/), déi ënner der Lizenz
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) stinn. D'Kopie läit op dësem Site. Deng Sich verléisst ni däin Apparat, a keng Ufro geet u GeoNames.
