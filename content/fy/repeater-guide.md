---
title: Repeaterhantlieding
lead: In repeater dy't heech stiet, stjoert berjochten troch foar elkenien yn 'e omkriten, oer in hiele stêd of delling. Kies in plak, lit him op sinneenerzjy rinne, stel him yn en bliuw binnen de wet.
description: 'In MeshCore-repeater yn Europa planne, fan stroom foarsjen, ynstelle en wetlik brûke: plakkeuze, sinnepanielen berekkenje, CLI-ynstellings, 868 MHz-fermogen en duty-cycle-grinzen.'
eyebrow: 868 MHz · oant 500 mW · sûnder fergunning
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '7c7e3be3'
  seeded: '2026-10-31'
  fields: {title: '4608abcd', lead: 'bc670c65', description: '9e483ce5', eyebrow: '9fd33416'}
  sections: ['05ee477a', '938c518c', '766086be', '70faf508', '8bc641aa', '399cd683', 'e9dedb7b', '92beca03', '17634750', 'cadf6024', 'e9cc6834', '2e6e59ca', 'fb44b8db']
  blocks: ['20ac0371', 'ed2b1adf', '432543ee', '7af42c89', 'd0f7543a', '9ef3580f', '3476aef7', '1bab7bec', '6a7c4493', 'dbd9fa1f', 'aa06d32b', '9958aad3', 'd162b028', 'cca1bbdf', '64ef011d', 'e7f16724', 'd2e34ff0', 'bb195cfc', '8d080bb3', '2b1d995b', '210f1b66', 'dc7419d2', 'bdc66db0', 'b59f248c', '7184bd63', 'de5a24f9', 'f5cfb426', '48c7422f', '9d3c0836', 'da8a6af3', '240126df', '8aac2b33', '81a475b8', 'a53e42b5', '36ff1db4', 'e4ca8602', 'e4594afd', '3b24b8e9', '58330858', '68f2966e', 'd7418228', '23536e60', 'cbc5c2d1', '2ea02ba9', '92540256', '6e21f681', 'a8c12311', '3382ae7f', 'cdeafb0f', '1b1319d2']
---

Repeaters drage de mesh. Companions, de radio's dêr't do berjochten mei stjoerst, stjoere gjin berjochten troch. Sûnder
repeaters berikst do dus allinnich de minsken yn direkt berik. In repeater op it goede
plak wreidet de mesh út foar elkenien yn 'e omkriten. Dizze hantlieding folget MeshCore-firmware
v1.18.0.

Praat foar'tsto begjinst mei dyn [pleatslike groep](/community/). Sy witte wêr't
dekking ûntbrekt, hokker [preset dyn gebiet brûkt](/guides/settings/) en hoe'tsto repeaters neamst. Sjoch op de
[dekkingskaarten](/map/) hokker repeaters by dy yn 'e buert steane, en sis goeie op de iepenbiere
of pleatslike [kanalen](/guides/channels/).

## Hasto der ien nedich? {#need}

In repeater stjoert elk floodberjocht troch dat er heart, en alle repeaters yn
berik diele deselde etertiid. Wêr't de mesh dy al berikt, jout in ekstra
repeater mear ferkear en gjin ekstra dekking. In companion dy't heech stiet, by in solderrút
of op in balkon, kin al genôch wêze.

Set in repeater del wêr't dekking ûntbrekt:

- op de [dekkingskaarten](/map/) stiet gjin repeater by dy yn 'e buert, of allinnich repeaters dy't dyn
  companion net heart;
- dyn pleatslike groep seit dat it gebiet der ien nedich hat.

## Kies in plak {#site}

Hichte wint it fan fermogen. LoRa op 868 MHz komt it fierst by frij sicht.
Heuvels, gebouwen en tichte beammen kostje folle mear berik as in pear ekstra
milliwatt weromwinne.

- **Gean heech.** In dak, in mêst, in heech gebou of in heuvel beslacht folle mear
  as in finsterbank. In pear meter boppe de omlizzende dakken helpt al.
- **Hâld de antenne frij.** Monteer him boppe de dakrâne, fuort fan
  metaal, dakgoaten en oare antennes.
- **Kontrolearje it útsicht.** Mei ark lykas [HeyWhatsThat](https://www.heywhatsthat.com/)
  sjochsto wat fan in plak út te sjen is. Kinsto in plak sjen, dan is in repeater
  dêr binnen berik.
- **Lit romte frij.** In radiopaad hat wat frije romte om de direkte
  line hinne nedich, net allinnich de line sels. Oer lange ôfstannen moat it midden fan it paad
  ferskate meters boppe obstakels bliuwe.
- **Freegje tastimming.** Regelje tastimming fan de eigner foar it dak of de mêst, en sprek ôf
  hoe'tsto by de repeater komst foar ûnderhâld.

## Hardware {#hardware}

- **Board.** Kies in nRF52-board mei leech ferbrûk, lykas de
  [Heltec T114](/devices/), RAK WisBlock of de SenseCAP Solar Node. ESP32-boards
  brûke mear stroom (de apparatenside markearret se as High). Dêrtroch is
  rinnen op sinneenerzjy dreech.
- **Antenne.** Brûk in antenne makke foar 868 MHz, fertikaal monteard. De
  [antennehantlieding](/guides/antenna/) behannelet soarten, ferbiningen, kabel en
  montaazje. Antennewinst telt mei foar de wetlike fermogensgrins; sjoch
  [Wetlike grinzen](#legal).
- **Kabel.** Hâld de koaksiale kabel koart, of brûk kabel mei leech ferlies. Op 868 MHz kinne in pear
  meter tinne kabel de helte fan dyn fermogen kostje.
- **Kast.** In waarbestindige kast (IP65 of better) mei in kabelwartel, in
  luchtgat of ôfwettergat tsjin kondens, en in ljochte kleur of sinnekap.
  Batterijen hawwe te lijen fan waarmte en kinne net laden wurde ûnder it friespunt.
- **Wjerljocht.** In antenne op in dak is in doelwyt. Folgje de pleatslike regels foar
  ierding, of monteer him dêr't in ynslach de bedrading fan it gebou net
  berikke kin.

## Stroom en sinnepanielen berekkenje {#power}

In repeater op sinneenerzjy moat de tsjusterste wiken fan 'e winter trochkomme. Berekkenje him
dêrop:

1. **Mjit it ferbrûk.** Lit de ynstelde repeater in dei lang troch in USB-stroommeter
   rinne. Lês it ferbrûk ôf yn wattoere (Wh). It ferkear yn
   dyn gebiet feroaret it getal, dus mjit op it plak sels as it kin.
2. **Tel reserve derby.** Plan batterijkapasiteit foar op syn minst 5 oant 7 dagen
   sûnder brûkbere sinne.
3. **Sykje dyn wintersinne op.** Mei it fergese
   [PVGIS-ark](https://re.jrc.ec.europa.eu/pvg_tools/en/) fan de EU sjochsto foar elk
   plak hoefolle enerzjy in paniel per moanne opwekt. Nim de moanne mei de
   minste sinne.
4. **Bepaal de grutte fan it paniel.** It paniel moat yn dy minste moanne it ferbrûk fan elke dei goedmeitsje,
   mei romte foar laadferlies.

In útwurke foarbyld, mei oannommen getallen: in repeater dy't 1 Wh per dei brûkt,
hat foar in wike reserve in batterij fan op syn minst 7 Wh nedich, sa'n 2 Ah
brûkbere kapasiteit by 3.7 V. Seit PVGIS dat in paniel fan 1 W op dyn plak
0.5 Wh per dei jout yn desimber, dan hasto op syn minst in paniel fan 2 W nedich. Mei 3 oant 5 W
hasto marzje foar wolken, snie en âlderdom.

## Ynstelle {#config}

**Flashe.** Brûk de [webflasher](https://flasher.meshcore.io) en kies de
**Repeater**-firmware foar dyn board. Sjoch
[Begjinne](/get-started/#flash) foar de stappen fan it flashen.

**Ynstelle oer USB.** Iepenje, wylst de repeater noch oan dyn kompjûter sit,
[config.meshcore.io](https://config.meshcore.io) of de konsole fan de flasher. Do kinst ek
elke seriële terminal brûke op 115200 baud. De wichtichste
kommando's:

| Wat | Kommando |
|---|---|
| It adminwachtwurd feroarje | `password <new password>` |
| In namme jaan | `set name <name>` |
| Radiopreset: frekwinsje, bânbreedte, SF, CR (opnij starte om ta te passen) | `set radio 869.618,62.5,8,8` |
| Duty-cycle-grins, yn persint | `set dutycycle 10` |
| Stjoerfermogen fan de radiochip, yn dBm | `set tx <dBm>` |
| Posysje, sadat er op kaarten stiet | `set lat <degrees>` en `set lon <degrees>` |
| Kontaktgegevens foar oare behearders | `set owner.info <text>` |
| Oeren tusken flood-adverts, dy't de hiele mesh heart | `set flood.advert.interval <hours>` |
| Him no oankundigje | `advert` |
| Opnij starte | `reboot` |

It standert adminwachtwurd is `password`, en elkenien dy't dêrmei ynlogt,
wurdt admin. Feroarje it foar't de repeater de loft yn giet.

It `set radio`-foarbyld hjirboppe is EU/UK (Narrow). Brûk ynstee de wearden fan de preset fan
dyn gebiet: [Oanrekommandearre ynstellings](/guides/settings/) jout se
per lân.

**Set de klok.** Sûnder klokmodule (RTC) ferliest in repeater de tiid by
elke stroomûnderbrekking en begjint er wer yn maaie 2024. Wylst er rint, driuwt syn klok ek
ôf: dy rint fierder foar of efter. Set de klok dus geregeld gelyk: log
op ôfstân yn fanút de app en brûk `clock sync`, of set de tiid oer USB. Mei
in RTC-module hoechsto dat selden: dy hâldt de tiid by stroomûnderbrekkings fêst en
driuwt folle minder ôf.

**Op ôfstân beheare.** As er op 'e mesh is, logsto yn fanút de MeshCore-app
mei it adminwachtwurd. Dêr lêsto syn status en brûkst deselde kommando's
oer de radio. Guon kommando's wurkje allinnich oer USB, lykas `set freq` en de
fabrykreset `erase`.

**Bewarje syn identiteit.** Typ foar in erase `get prv.key` oer USB en bewarje
de privee kaai dy't er toant op in feilich plak. Nei de erase jouwe `set prv.key <key>`
en in `reboot` de repeater syn âlde identiteit werom. Nodes dy't him kenne,
fine him dan ûnder deselde prefix.

De folsleine kommandolist stiet yn de
[MeshCore CLI-referinsje](https://github.com/meshcore-dev/MeshCore/blob/main/docs/cli_commands.md).

## Bywurkje oer de loft {#update}

As de repeater ienris heech hinget, wurksto him by fanôf de grûn. Log yn fanút de
MeshCore-app mei it adminwachtwurd, iepenje syn kommandorigel en typ
`start ota`. Wat dêrnei komt, hinget ôf fan it board. Oare boards antwurdzje `Error`,
en dy wurksto by oer USB.

**nRF52-boards**, lykas RAK, Heltec T114, Seeed XIAO en SenseCAP Solar:

1. Download de **ZIP** fan de nije firmware foar dyn board fan de
   [webflasher](https://flasher.meshcore.io).
2. Typ `start ota`. De repeater antwurdet `OK` en ferskynt oer Bluetooth
   as `<board>_OTA`, bygelyks `RAK4631_OTA`.
3. Iepenje de app nRF Device Firmware Update op dyn tillefoan, kies de ZIP en
   de repeater, en laad op. Dat duorret in pear minuten.

Ynstallearje de [OTAFIX-bootloader](https://github.com/oltaco/Adafruit_nRF52_Bootloader_OTAFIX)
op in nRF52-board foar'tst it omheech hingest. Mei de standert bootloader kinsto in mislearre
fernijing allinnich oer USB reparearje. Mei OTAFIX falt it board werom op
fernijingsmodus, en besykjesto it opnij oer Bluetooth.

**ESP32-boards**, lykas de Heltec V3 en V4:

1. Download de **net-gearfoege** `.bin` foar dyn board fan de webflasher:
   it bestân sûnder "merged" yn de namme.
2. Typ `start ota`. De repeater iepenet in WiFi-netwurk mei de namme `MeshCore-OTA`
   en antwurdet mei it adres fan syn opladside.
3. Ferbyn binnen WiFi-berik dyn tillefoan of laptop mei dat netwurk, iepenje it
   adres en laad it bestân op.

## Wetlike grinzen {#legal}

{{< callout type="legal" verified="2026-10-02" >}}
De Europeeske presets fan MeshCore lizze yn de subbân **869.40-869.65 MHz**. Yn de
EU, it Feriene Keninkryk, Switserlân en Noarwegen meie apparaten mei koart berik dizze subbân sûnder
fergunning brûke, binnen dizze grinzen:

- op syn heechst **500 mW e.r.p.** útstrielle fermogen;
- op syn heechst **10% duty cycle**: net mear as 360 sekonden stjoere yn
  elk oere, per apparaat. As alternatyf mei in apparaat listen-before-talk
  mei adaptive frequency agility brûke, sa't ETSI EN 300 220-2 dat definiearret;
- it hiele sinjaal, op syn heechst 250 kHz breed, moat binnen de subbân bliuwe.

De bân is dield: do meist tsjinsten mei fergunning net steure, en oaren meie
dy steure.
De radio moat in CE-markearring hawwe (yn Grut-Brittanje CE of UKCA).
{{< /callout >}}

Boarnen: [CEPT ERC Recommendation 70-03](https://docdb.cept.org/document/845),
Annex 1, bân h1.7;
[Kommisjebeslút 2006/771/EG](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02006D0771(01)-20250123)
en de wizigings dêrfan;
[ETSI EN 300 220-2](https://www.etsi.org/deliver/etsi_en/300200_300299/30022002/03.03.01_60/en_30022002v030301p.pdf),
bân O.

### Fermogen: e.r.p. en dyn antenne {#erp}

De grins jildt foar it *útstrielle* fermogen, mjitten tsjin in ienfâldige dipoalantenne
(e.r.p.). Antennewinst telt mei; kabelferlies giet derôf. Fabrikanten jouwe
antennewinst yn dBi. Dat is 2.15 dB mear as deselde winst yn dBd
(relatyf oan in dipoal). Hâld dizze som op of ûnder 27 dBm (500 mW):

> stjoerfermogen (dBm) + antennewinst (dBi) − kabelferlies (dB) − 2.15 ≤ 27

- In board dat 22 dBm stjoert nei in antenne fan 5 dBi troch 1 dB kabel:
  22 + 5 − 1 − 2.15 = 23.85 dBm, sa'n 240 mW e.r.p. Binnen de grins.
- In board mei in fersterker fan 30 dBm (1 W) nei in antenne fan 3 dBi:
  30 + 3 − 2.15 = 30.85 dBm, sa'n 1.2 W e.r.p. Oer de grins; set it
  stjoerfermogen leger.

Mei `set tx` stelsto it útgongsfermogen fan de LoRa-chip yn, yn dBm. De SX1262-chip sels
giet net heger as 22 dBm. De firmware kontrolearret it getal dat do ynfierst net. Boards mei in ekstra
fersterker, lykas de Heltec V4 of de Station G2, stjoere folle mear út as
it getal datsto ynstelst. Sjoch de tabel fan de fabrikant nei foar'tsto it ynstelst, en
begjin leech.

### Duty cycle {#duty-cycle}

In repeater stjoert foar elkenien yn 'e omkriten. Dêrom brûkt er syn etertiid flugger op
as in companion. De duty-cycle-begrinzer fan MeshCore stiet standert op 50%. Dat is
mear as dizze bân talit. Set him op elke repeater op 10%:

```text
set dutycycle 10
```

### Frekwinsjekrektens {#frequency}

It EU/UK (Narrow)-kanaal, 869.618 MHz mei 62.5 kHz bânbreedte, rint oant
869.649 MHz: minder as 1 kHz ûnder de boppekant fan de subbân. It sinjaal
moat by elke temperatuer binnen de bân bliuwe. Dêr is in
temperatuerkompensearre kristal (TCXO) foar nedich. Hast elk hjoeddeisk board hat der ien; âldere
boards sûnder, lykas de Heltec V2, driuwe te fier ôf om betrouber te wurkjen
op 62.5 kHz.

### Notysjes per lân {#countries}

- **EU-lidsteaten** moatte dizze subbân op dizze betingsten beskikber stelle
  (Beslút 2006/771/EG, Artikel 3).
- **Feriene Keninkryk:** deselde grinzen, yn Ofcom
  [IR 2030](https://www.ofcom.org.uk/spectrum/radio-equipment/short-range-devices).
- **Switserlân en Lychtenstein:** deselde grinzen, yn OFCOM
  [RIR1008-09](https://www.ofcomnet.ch/api/rir/1008/09).
- **Noarwegen:** deselde grinzen, yn de
  [regeling foar algemiene fergunningen](https://lovdata.no/dokument/SF/forskrift/2012-01-19-77)
  (fribruksforskriften).

Dizze notysjes binne gjin juridysk advys. Regels feroarje; by twifel, freegje it nei by
dyn nasjonale tafersjochhâlder.

## Kontrolelist foar it pleatsen {#checklist}

- [ ] De eigner fan it plak hat tastimming jûn, en do kinst by de repeater foar ûnderhâld.
- [ ] It board draait de **Repeater**-firmware, en de antenne siet der oan
      foar'tst it board de earste kear oansetst.
- [ ] It adminwachtwurd is feroare.
- [ ] De radio komt oerien mei [de preset fan dyn gebiet](/guides/settings/) (`get radio`).
- [ ] `set dutycycle 10` is ynsteld.
- [ ] Stjoerfermogen plus antennewinst bliuwt binnen 500 mW e.r.p.
- [ ] Namme, posysje en `owner.info` binne ynsteld, sadat oaren witte wa't him beheart.
- [ ] De klok is ynsteld (`clock`).
- [ ] De kast is ôfsletten, mei in ôfwetter- of luchtgat, en de kabel hat in
      drippellus.
- [ ] Batterij en paniel binne berekkene op de minste wintermoanne.
- [ ] Do hast him fan in ôfstân hifke mei de app foar'tsto it plak ferlitten hast.
- [ ] Dyn pleatslike groep wit dat er draait.
