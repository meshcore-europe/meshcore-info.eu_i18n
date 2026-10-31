---
title: Begjinne
lead: Fan in nij board oant dyn earste berjocht op it mesh. Do hast in LoRa-board nedich, in kompjûter mei Chrome of Edge, en in tillefoan of laptop foar de app.
description: Set MeshCore fia dyn browser op dyn board, keppelje de app, kies de radio-preset fan dyn gebiet, stjoer dyn earste berjocht en doch mei oan dyn pleatslike kanaal.
eyebrow: 6 stappen · MeshCore v1.18.0
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'f97ca1b9'
  seeded: '2026-10-31'
  fields: {title: '61e8d44a', lead: '45b0e5c3', description: 'cf031b18', eyebrow: '4fa6fe1e'}
  sections: ['16c3728c', '203acaa5', 'df7a1665', '6da9fd7a', 'cb5fb72e', 'a1cf8b26', 'a419ce79', '66d00206']
  blocks: ['16c3728c', '2a70a7ed', '6f8e6f5f', '16c11d47', '081db416', 'd5e7fd0b', '6d28c323', 'eb2ea361', 'de50125c', 'ae20cb8e', 'abd42710', 'c08a865a', '7d1eb0b9', '263e0c96', '0903299f', 'eba20370', '5cdc20cf', '7f542f82', '802ca5a8', '1a854187', 'bc333adf', 'f25b16fa', '7c893ae2', '7f5927b4', '26e13713', '39a142cf', 'a786620c', '216897fa', '2d222782', 'a9755900', 'f081b357']
---

Dizze stappen geane út fan MeshCore-firmware v1.18.0 en de offisjele ark fan
oktober 2026. De nammen fan menu's yn de app kinne tusken ferzjes wat ferskille.

## 1. Kies in apparaat {#device}

Elk board op de [apparatenside](/devices/) dêr't companion by stiet, wurket. Kies
foar dyn earste node in *companion*: de radio dêr't do mei berjochten stjoerst.
Dy keppelsto oan dyn tillefoan of laptop fia Bluetooth of USB. Do kinst ek ien
kieze mei in eigen skerm en toetseboerd, dy't op himsels wurket.

Nim de ferzje foar 868 MHz. De antenne dy't derby sit, is goed genôch. Yn de
[antennegids](/guides/antenna/) lêst hoe'tst in antenne kontrolearrest.

{{< callout type="warning" >}}
Set de antenne derop foardatst de radio oansetst. In LoRa-radio dy't sûnder
antenne útstjoert, kin syn eigen chip skansearje.
{{< /callout >}}

## 2. Set de firmware derop {#flash}

1. Ferbyn it apparaat mei dyn kompjûter fia in USB-datakabel.
2. Iepenje de webflasher op [flasher.meshcore.io](https://flasher.meshcore.io)
   yn Chrome of Edge. Dy brûkt Web Serial, en oare browsers hawwe dat net.
3. Kies dyn apparaat en dêrnei de **Companion**-firmware foar **Bluetooth** (of
   USB, asto it allinnich mei in kabel oan in kompjûter brûke silst).
4. Set de firmware derop. Guon boards moatte earst yn de updatemodus; de flasher
   seit dy hoe.

Brûk *erase* allinnich asto op 'e nij begjinne wolst. Mei erase wisksto de
identiteit fan it apparaat en dyn kontakten. Set by lettere updates de firmware
derop sûnder te wiskjen. Wolsto dyn identiteit hâlde by in erase? Eksportearje
dan earst de privee kaai fan dyn companion yn de app, en ymportearje him dêrnei
wer.

## 3. Ynstallearje de app {#app}

De offisjele MeshCore-app is der foar Android, iOS, Windows en macOS. Op
[meshcore.io](https://meshcore.io) fynst keppelings nei alle ferzjes. Der is ek
in webapp op [app.meshcore.nz](https://app.meshcore.nz), dy't yn Chrome of
Edge op in kompjûter draait.

## 4. Keppelje dyn node {#pair}

Set dyn node oan, iepenje de app en meitsje ferbining fia Bluetooth. As de app
om in PIN freget:

- in node **mei** skerm lit in PIN sjen; typ dy yn;
- in node **sûnder** skerm brûkt `123456`.

Slagget it keppeljen net? Helje it apparaat dan út de Bluetooth-ynstellings fan
dyn tillefoan en besykje it opnij. Jou dyn node dêrnei in namme. Oaren sjogge
dy namme, dus brûk net dyn folsleine namme of adres, útsein asto dat wolst.

## 5. Kies de radio-preset fan dyn gebiet {#preset}

Alle radio's yn in gebiet brûke deselde frekwinsje en ynstellings, oars hearre
se inoar net. Kies yn de radio-ynstellings fan de app de preset fan dyn gebiet.
Bûten de gebieten hjirûnder brûkt Europa **EU/UK (Narrow)**. Nederlân, Tsjechje,
Hongarije, Slowakije, Portugal en Switserlân hawwe in eigen preset, en Limburg
yn Nederlân hat in fariant:

{{< presets >}}

Hat dyn apparaat de preset fan dyn gebiet net? Fier dan de 4 wearden út de tabel
mei de hân yn by de radio-ynstellings fan de app: frekwinsje, bânbreedte,
spreading factor en coding rate. In node mei oare wearden heart it mesh net.

Witsto it net wis? Dyn [pleatslike groep](/community/) wit hokker preset dyn
gebiet brûkt. De app hellet dizze list op by it MeshCore-projekt. Foar in nije
preset hoechst de app dus net te aktualisearjen.

## 6. Sis goeie {#hello}

1. **Meld dysels.** Stjoer in *advert* út de app. In "flood"-advert giet troch
   de repeaters (nodes dy't berjochten trochjouwe), sadat elkenien op it mesh
   dy tafoegje kin.
   Companions melde harsels nea automatysk.
2. **Fyn oaren.** Minsken komme yn dyn kontakten sa gau't harren adverts dy
   berikke. Repeaters stjoere standert elke 47 oeren in flood-advert. It kin
   dus 2 dagen duorje oant dyn list fol rekket.
3. **Stjoer in berjocht.** Iepenje in kontakt en skriuw. It earste berjocht giet
   as flood troch it netwurk. De ûntfanger meldet werom hokker rûte it naam, en
   lettere berjochten folgje dy rûte.
4. **Doch mei oan kanalen.** It kanaal **Public** stiet al klear; alles watsto
   dêr skriuwst, berikt elkenien op it mesh. Typ de namme fan it *hashtag-kanaal*
   fan dyn regio (in namme dy't mei `#` begjint) om it ta te foegjen. Dyn
   [pleatslike groep](/community/) fertelt dy hokker kanalen aktyf binne.

## As eat net wurket {#troubleshooting}

**De app fynt myn apparaat net fia Bluetooth.**
Wierskynlik hasto de USB-companion derop set. Set de firmware opnij derop en
kies de Bluetooth-ferzje. By de Heltec V3 hat de lytse ynboude Bluetooth-antenne
in koart berik; hâld de tillefoan tichtby.

**It keppeljen mislukt hieltyd.**
Helje it apparaat út de Bluetooth-ynstellings fan dyn tillefoan, start Bluetooth
opnij en keppelje wer mei de PIN op it skerm of `123456`.

**Der komt gjinien yn myn kontakten.**
Kontrolearje oft dyn preset by dyn gebiet past. Stjoer in flood-advert. As der
gjin repeater binnen berik is, hearsto allinnich radio's tichtby. Op de
[kaartside](/map/) sjochst wêr't repeaters steane.

**By in kontakt stiet "lêst sjoen" dagen lyn, wylst er aktyf is.**
Ien fan de twa nodes hat de ferkearde tiid. In companion nimt de tiid oer fan
dyn tillefoan. By repeaters en room servers (nodes dy't berjochten foar in groep
bewarje) moat de eigener de tiid ynstelle.

**In direkt berjocht komt nea oan.**
Do en de oar moatte inoar beide as kontakt hawwe. In node smyt in berjocht fan ien
dy't er net ken fuort, en seit dat net tsjin de stjoerder. Stjoer in flood-advert
en freegje de oar om ek ien te stjoeren. Kontrolearje yn de app oft dy nije
kontakten automatysk tafoeget. De app foeget allinnich nodes ta binnen syn
hop-limyt.

**Alde kontakten wurkje, nije krije nea ferbining.**
In earste berjocht giet as flood troch it netwurk. In repeater jout it allinnich
troch as er de regio fan it berjocht hat. Lettere berjochten folgje in learde
rûte, en dêr hâldt gjin regiokontrôle se tsjin. Freegje dyn
[pleatslike groep](/community/) hokker regio's de repeaters om dy hinne hawwe, en
kontrolearje [de ynstellings foar dyn gebiet](/guides/settings/#traffic).

**De app makket gjin ferbining mear mei dyn companion.**
Guon boards hawwe in brûkersknop, lykas guon RAK-boards en de Heltec T114. Hâld
dy yn de earste 8 sekonden nei it opstarten fan it board yndrukt. De companion
iepenet dan in rescue-konsole fia USB. Yn de konsole op
[flasher.meshcore.io](https://flasher.meshcore.io) setsto mei `set pin <pin>`
in nije Bluetooth-PIN yn, en mei `erase` wisksto it apparaat.

**De flasher kin de seriële poarte op Linux net iepenje.**
Dyn brûker hat tagong ta de poarte nedich, bygelyks mei
`sudo setfacl -m u:$USER:rw /dev/ttyUSB0`, of as lid fan de groep `dialout`.

**Eat oars.** Yn de
[MeshCore FAQ](https://github.com/meshcore-dev/MeshCore/blob/main/docs/faq.md)
fynst in protte mear problemen.
