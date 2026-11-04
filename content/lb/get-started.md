---
title: Éischt Schrëtt
lead: Vun engem neie Board bis zu denger éischter Noriicht am Mesh. Du brauchs e LoRa-Board, e Computer mat Chrome oder Edge, an en Telefon oder Laptop fir d'App.
description: Flash MeshCore aus dengem Browser, verbann d'App, wiel de Radio-Preset vun denger Géigend, schéck deng éischt Noriicht a komm an däi lokale Kanal.
eyebrow: 6 Schrëtt · MeshCore v1.18.0
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '0490a311'
  seeded: '2026-11-04'
  fields: {title: '61e8d44a', lead: '45b0e5c3', description: 'cf031b18', eyebrow: '4fa6fe1e'}
  sections: ['16c3728c', '5b6d136a', 'df7a1665', '6da9fd7a', 'cb5fb72e', 'a1cf8b26', '1741ed35', '66d00206']
  blocks: ['16c3728c', '2a70a7ed', '6f8e6f5f', '16c11d47', 'e90b7859', '081db416', 'd5e7fd0b', '6d28c323', 'eb2ea361', 'de50125c', 'ae20cb8e', 'abd42710', 'c08a865a', '7d1eb0b9', '263e0c96', '0903299f', 'eba20370', '5cdc20cf', '7f542f82', '802ca5a8', '1a854187', '53276869', 'f25b16fa', '7c893ae2', '7f5927b4', '26e13713', '39a142cf', 'a786620c', '216897fa', '2d222782', 'a9755900', 'f081b357']
---

Dës Schrëtt baséieren op der MeshCore-Firmware v1.18.0 an den offiziellen Tools
vum Oktober 2026. D'Menünimm an der App kënne sech tëscht de Versiounen e bësse
ënnerscheeden.

## 1. Wiel en Apparat {#device}

All Board op der [Apparater-Säit](/devices/), bei deem companion steet, funktionéiert.
Fir däin éischten Node huel e *companion*: de Radio, vun deem aus du Noriichte
schécks. Verbann en iwwer Bluetooth oder USB mat dengem Telefon oder Laptop, oder
huel ee mat eegenem Schierm an eegener Tastatur, deen eleng funktionéiert.

Huel d'Versioun fir 868 MHz. D'Antenn, déi dobäi ass, geet duer; am
[Antennen-Guide](/guides/antenna/) gesäis du, wéi s du eng iwwerpréifs.

Leeft op dengem Board elo Meshtastic? Wann s de MeshCore flashs, ersetzt dat
Meshtastic, an déi zwee schwätze net mateneen.

{{< callout type="warning" >}}
Schléiss d'Antenn un, ier s du de Radio aschalts. E LoRa-Radio, deen ouni Antenn
sent, kann säin eegenen Chip beschiedegen.
{{< /callout >}}

## 2. Flash d'Firmware {#flash}

1. Verbann den Apparat mat engem USB-Datekabel mat dengem Computer.
2. Maach de Web-Flasher op [flasher.meshcore.io](https://flasher.meshcore.io)
   an Chrome oder Edge op. Hie benotzt Web Serial, an dat hunn aner Browser net.
3. Wiel däin Apparat, dann d'**Companion**-Firmware fir **Bluetooth** (oder
   USB, wann s du en nëmme mat engem Computerkabel benotz).
4. Flash. Verschidde Boards musse fir d'éischt an den Update-Modus; de Flasher
   seet dir, wéi dat geet.

Benotz *erase* nëmme fir en Neiufank: dat läscht d'Identitéit vum Apparat an deng
Kontakter. Bei spéideren Updates flashs du ouni ze läschen. Wann s du deng
Identitéit no engem Erase behale wëlls, exportéier virdrun de private Schlëssel
vun dengem Companion aus der App an importéier en duerno.

## 3. Installéier d'App {#app}

Déi offiziell MeshCore-App gëtt et fir Android, iOS, Windows a macOS; op
[meshcore.io](https://meshcore.io) fënns du Linke fir all Versioun. Et gëtt och
eng Web-App op [app.meshcore.nz](https://app.meshcore.nz), déi an Chrome oder
Edge op engem Computer leeft.

## 4. Verbann däin Node {#pair}

Schalt däin Node un, maach d'App op a verbann dech iwwer Bluetooth domat. Wann
d'App no engem PIN freet:

- en Node **mat** Schierm weist e PIN; gëff deen an;
- en Node **ouni** Schierm benotzt `123456`.

Wann d'Verbindung net klappt, läsch den Apparat an de Bluetooth-Astellunge vun
dengem Telefon a probéier et nach eng Kéier. Gëff dengem Node duerno en Numm.
Anerer gesinn dësen Numm, also benotz däi ganzen Numm oder deng Adress nëmmen,
wann s du dat wëlls.

## 5. Wiel de Radio-Preset vun denger Géigend {#preset}

All Radio an enger Géigend benotzt déi selwecht Frequenz an déi selwecht
Astellungen, soss héiere si sech net. An de Radio-Astellunge vun der App
wiels du de Preset, deen deng Géigend benotzt. Ausserhalb vun de Géigenden hei
ënnendrënner benotzt Europa **EU/UK (Narrow)**. D'Nidderlanden, Tschechien, Ungarn,
d'Slowakei, Portugal an d'Schwäiz hunn en eegene Preset, a Limburg an den
Nidderlanden huet eng Variant:

{{< presets >}}

Bitt däin Apparat de Preset vun denger Géigend net un? Da gëff déi 4 Wäerter aus
der Tabell vun Hand an de Radio-Astellunge vun der App an: Frequenz, Bandbreet,
Spreading Factor a Coding Rate. En Node mat anere Wäerter héiert de Mesh net.

Net sécher? Deng [lokal Grupp](/community/) weess, wat fir e Preset deng Géigend
benotzt. D'App lued dës Lëscht vum MeshCore-Projet erof, also brauch en neie
Preset keen App-Update.

## 6. So Moien {#hello}

1. **Mell dech.** Schéck en *Advert* aus der App. En "Flood"-Advert
   geet iwwer d'Repeateren (Noden, déi Noriichte weiderginn), sou datt jiddereen
   am Mesh dech derbäisetze kann.
   Companions mellen sech ni automatesch.
2. **Fann anerer.** Leit erschéngen an denge Kontakter, soubal hir Adverts bei
   dech ukommen. Repeateren schécken standardméisseg all 47 Stonnen e Flood-Advert,
   dofir kann et 2 Deeg daueren, bis deng Lëscht voll ass.
3. **Schéck eng Noriicht.** Maach e Kontakt op a schreif. Déi éischt Noriicht
   geet als Flood duerch d'Netz; den Empfänger mellt de Wee zréck, deen se geholl huet,
   a spéider Noriichte huelen dee Wee.
4. **Tritt Kanäl bäi.** De **Public**-Kanal ass schonn ageriicht; alles, wat s du
   do schreifs, erreecht jiddereen am Mesh. Füeg de *Hashtag-Kanal* vun denger
   Regioun (en Numm, deen mat `#` ufänkt) derbäi, andeems s du säin Numm agëss. Deng
   [lokal Grupp](/community/) seet dir, wéi eng Kanäl aktiv sinn.
   Wëlls du se perséinlech treffen? Kuck d'[Treffen](/meetings/) bei dir an der Géigend.

## Wann eppes net funktionéiert {#troubleshooting}

**D'App fënnt mäin Apparat net iwwer Bluetooth.**
Wahrscheinlech hues du de USB-Companion geflasht. Flash nach eng Kéier a wiel
d'Bluetooth-Versioun. Beim Heltec V3 huet déi kleng agebaute Bluetooth-Antenn eng
kuerz Reechwäit; halt den Telefon no derbäi.

**D'Verbindung klappt ëmmer erëm net.**
Läsch den Apparat an de Bluetooth-Astellunge vun dengem Telefon, start Bluetooth
nei a verbann dech nach eng Kéier mam PIN um Schierm oder mat `123456`.

**Et erschéngt keen a menge Kontakter.**
Kontrolléier, ob däi Preset zu denger Géigend passt. Schéck e flood-Advert. Wa
kee Repeater a Reechwäit ass, héiers du nëmme Radioen no bei dir; op der
[Kaartesäit](/map/) gesäis du, wou Repeatere sinn.

**E Kontakt weist "last seen" virun e puer Deeg, obwuel déi Persoun aktiv ass.**
Ee vun den zwee Noden huet déi falsch Zäit. E Companion hëlt d'Zäit vun dengem
Telefon; bei Repeateren a room serveren (Noden, déi Noriichte fir eng Grupp
späicheren) muss de Besëtzer d'Zäit astellen.

**Eng direkt Noriicht kënnt ni un.**
Du muss déi aner Persoun als Kontakt hunn, an déi aner Persoun dech. En Node verwerft
eng Noriicht vun engem, deen en net kennt, an de Sender erfiert dovunner näischt.
Schéck e flood-Advert a fro déi aner Persoun, ob se och ee schéckt. Kontrolléier an
der App, ob se nei Kontakter automatesch derbäisetzt; si setzt nëmmen Noden
bannent hirem Hop-Limit derbäi.

**Al Kontakter funktionéieren, nei verbanne sech ni.**
Eng éischt Noriicht geet als flood duerch d'Netz, an e Repeater gëtt se nëmme
weider, wann en d'Regioun vun der Noriicht huet. Spéider Noriichte huelen e
geléierte Wee, an deen hält keng Regiounskontroll op. Fro deng
[lokal Grupp](/community/), wéi eng Regiounen d'Repeateren ronderëm dech hunn, a
kuck [d'Astellunge fir deng Géigend](/guides/settings/#traffic).

**D'App verbënnt sech net méi mat dengem Companion.**
Verschidde Boards hunn e Benotzerknäppchen, wéi verschidde RAK-Boards an den Heltec
T114. Halt e während den éischten 8 Sekonnen nom Start vum Board gedréckt. De
Companion mécht dann eng Rettungskonsol iwwer USB op. An der Konsol op
[flasher.meshcore.io](https://flasher.meshcore.io) setz du mat `set pin <pin>` en
neie Bluetooth-PIN, a mat `erase` läschs du den Apparat.

**De Flasher kann de serielle Port op Linux net opmaachen.**
Däi Benotzer brauch Zougrëff op de Port, zum Beispill mat
`sudo setfacl -m u:$USER:rw /dev/ttyUSB0`, oder muss Member vun der Grupp `dialout`
sinn.

**Eppes anescht.** An der
[MeshCore FAQ](https://github.com/meshcore-dev/MeshCore/blob/main/docs/faq.md)
geet et ëm nach vill aner Problemer.
