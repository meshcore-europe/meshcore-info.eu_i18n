---
title: Repiiteri juhend
lead: Kõrgele paigutatud repiiter edastab sõnumeid kõigile enda ümber, üle terve linna või oru. Vali koht, toida repiitrit päikeseenergiaga, seadista see ja püsi seaduse piires.
description: 'Planeeri, toida, seadista ja käita MeshCore''i repiiterit Euroopas seaduslikult: asukoha valik, päikesepaneeli mõõdistamine, CLI seaded, 868 MHz võimsuse ja töötsükli piirangud.'
eyebrow: 868 MHz · kuni 500 mW · litsentsivaba
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '3e38a8c6'
  seeded: '2026-11-04'
  fields: {title: '4608abcd', lead: 'bc670c65', description: '9e483ce5', eyebrow: '9fd33416'}
  sections: ['05ee477a', '938c518c', '824ab38e', '662ea23c', '70faf508', '8bc641aa', '399cd683', 'e9dedb7b', '92beca03', '17634750', 'cadf6024', 'e9cc6834', '2e6e59ca', 'fb44b8db']
  blocks: ['20ac0371', 'ed2b1adf', '432543ee', '7af42c89', 'd0f7543a', '9ef3580f', '3476aef7', '1bab7bec', 'bbea9a0c', '2b9fab3b', 'b13d1947', 'c2bad16f', '636edc86', 'c2d6bcd1', '957ae975', '98874949', '96d1ebad', 'dbd9fa1f', 'aa06d32b', '9958aad3', 'd162b028', 'cca1bbdf', '64ef011d', 'e7f16724', 'd2e34ff0', 'bb195cfc', '8d080bb3', '2b1d995b', '210f1b66', 'dc7419d2', 'bdc66db0', 'b59f248c', '7184bd63', 'de5a24f9', 'f5cfb426', '48c7422f', '9d3c0836', 'da8a6af3', '240126df', '8aac2b33', '81a475b8', 'a53e42b5', '36ff1db4', 'e4ca8602', 'e4594afd', '3b24b8e9', '58330858', '68f2966e', 'd7418228', '23536e60', 'cbc5c2d1', '2ea02ba9', '92540256', '6e21f681', 'a8c12311', '3382ae7f', 'cdeafb0f', '1b1319d2']
---

Võrk püsib repiitrite peal. Kaasseadmed ehk raadiod, millega sõnumeid saadad, sõnumeid edasi ei anna. Ilma repiitriteta jõuad seega ainult nendeni, kes on otseses levis. Õiges kohas asuv repiiter laiendab võrku kõigile ümberkaudsetele. See juhend põhineb MeshCore'i püsivaral v1.18.0.

Enne alustamist räägi oma [kohaliku grupiga](/community/). Grupi liikmed teavad, kus levi puudub, [millist eelseadistust sinu piirkonnas kasutatakse](/guides/settings/) ja kuidas repiitreid nimetada. Vaata [levikaartidelt](/map/), millised repiitrid on sinu lähedal, ja tervita teisi avalikes või kohalikes [kanalites](/guides/channels/).

## Kas sul on repiitrit vaja? {#need}

Repiiter saadab edasi iga üleujutussõnumi, mida ta kuuleb, ja kõik levialas olevad repiitrid jagavad sama eetriaega. Kui võrk ulatub sinuni juba praegu, lisab veel üks repiiter liiklust, aga mitte levi. Sulle võib piisata kõrgele paigutatud kaasseadmest, näiteks pööninguaknal või rõdul.

Pane repiiter üles sinna, kus levi puudub:

- [levikaartidel](/map/) pole sinu lähedal ühtegi repiitrit või on ainult sellised, mida sinu kaasseade ei kuule;
- sinu kohalik grupp ütleb, et piirkonnas on repiitrit vaja.

## Vali asukoht {#site}

Kõrgus on tähtsam kui võimsus. LoRa levib 868 MHz sagedusel kõige paremini vaba otsenähtavuse korral. Künkad, hooned ja tihe mets võtavad levi palju rohkem, kui mõni lisamillivatt tagasi annab.

- **Mine kõrgele.** Katus, mast, kõrge hoone või küngas katab palju rohkem
  kui aknalaud. Juba mõni meeter üle ümbritsevate katuste aitab.
- **Hoia antenn vabas kohas.** Paigalda see katuseservadest kõrgemale, eemale
  metallist, vihmaveerennidest ja teistest antennidest.
- **Kontrolli nähtavust.** Sellised tööriistad nagu [HeyWhatsThat](https://www.heywhatsthat.com/)
  näitavad, mida mingist kohast näha on. MeshCore'i rakendus
  [arvutab, kuhu sinna paigutatud repiiter ulatub](#check-site).
- **Jäta vaba ruumi.** Raadioteekonnal peab vaba olema ka ruum otsejoone ümber,
  mitte ainult joon ise. 868 MHz sagedusel on see ruum 5 km teekonna
  keskel umbes 20 m. 20 km teekonnal on see umbes 40 m.
- **Küsi luba.** Hangi katuse või masti omaniku nõusolek ja lepi kokku,
  kuidas sa hoolduseks repiitrini pääsed.

### Kontrolli asukohta rakenduses {#check-site}

MeshCore'i rakenduse versioonis 1.33 ja uuemates leiad need tööriistad
menüü jaotisest **Tools**. Need töötavad ka ilma ühendatud raadiota.

- **Line of Sight** joonistab 2 punkti vahelise maapinna ja ruumi, mida signaal
  selle kohal vajab. Vajuta kaardil pikalt 2 punktile või puuduta repiitreid.
- **Antenna Coverage** näitab kaardil, kuhu 1 punktis asuv antenn ulatub.
  Vajuta pikalt punktile või puuduta repiitrit. Asukohtade võrdlemiseks lisa veel punkte.

Arvutis vali tööriista menüüst **Add Point** ja sisesta koordinaadid.

Mõlemas tööriistas on sinu asukoha antenn algul 5 m kõrgusel, seega määra
tööriista seadetes kõrgus, mida plaanid. Antenna Coverage'is on vastuvõttev
antenn algul 1 m kõrgusel. Kui raadio pole ühendatud, kasutab Line of Sight algul
sagedust 915 MHz: määra selle seadetes oma [eelseadistuse](/guides/settings/) sagedus.

Tööriistad arvutavad kõrgusandmete põhjal ega testi sinu raadiot. Kontrolli puid ja
uusi hooneid ise, seejärel vii companion kohale ja vaata, milliseid
repiitreid see kuuleb.

![Line of Sight MeshCore'i rakenduses: maapind 2 punkti vahel ja ruum, mida signaal selle kohal vajab](/media/guides/line-of-sight.webp)

![Antenna Coverage MeshCore'i rakenduses: ala kaardil, kuhu künkal asuv antenn ulatub](/media/guides/antenna-coverage.webp)

## Riistvara {#hardware}

- **Plaat.** Vali väikese voolutarbega nRF52-plaat, näiteks [Heltec T114](/devices/), RAK WisBlock või SenseCAP Solar Node. ESP32-plaadid tarbivad rohkem voolu (seadmete lehel on neil märge High), seega on neid päikeseenergiaga raske toita.
- **Antenn.** Kasuta 868 MHz jaoks tehtud antenni ja paigalda see vertikaalselt. [Antennijuhend](/guides/antenna/) käsitleb antennitüüpe, liitmikke, kaableid ja paigaldamist. Antenni võimendus läheb seadusliku võimsuspiirangu arvestusse: vaata jaotist [Seaduslikud piirangud](#legal).
- **Kaabel.** Hoia koaksiaalkaabel lühike või kasuta väikese kaoga kaablit. 868 MHz juures võib mõni meeter peenikest kaablit neelata poole sinu võimsusest.
- **Korpus.** Sobib ilmastikukindel karp (IP65 või parem), millel on kaabliläbiviik, kondensaadi vastu õhutus- või äravooluava ning hele värv või päikesevari. Akud kannatavad kuumuse käes ja miinuskraadidega ei saa neid laadida.
- **Pikne.** Katusel olev antenn on pikse sihtmärk. Järgi kohalikke maandusnõudeid või paigalda antenn nii, et pikselöök ei jõuaks hoone juhtmestikuni.

## Toide ja päikesesüsteemi arvutamine {#power}

Päikeseenergial töötav repiiter peab üle elama talve kõige pimedamad nädalad. Arvuta süsteem nende järgi:

1. **Mõõda tarbimist.** Lase seadistatud repiitril üks päev USB-võimsusmõõturi kaudu töötada. Loe kulunud energia välja vatt-tundides (Wh). Sinu piirkonna liiklus muudab seda arvu, seega mõõda võimaluse korral kohapeal.
2. **Lisa varu.** Arvuta aku mahutavus nii, et see kestaks vähemalt 5 kuni 7 päeva ilma kasuliku päikeseta.
3. **Leia oma talvine päikesekogus.** ELi tasuta [PVGIS-i tööriist](https://re.jrc.ec.europa.eu/pvg_tools/en/) näitab iga asukoha kohta, kui palju energiat paneel kuus toodab. Võta aluseks kuu, kus päikest on kõige vähem.
4. **Arvuta paneeli suurus.** Paneel peab sel halvimal kuul iga päeva tarbimise tagasi tootma, varuga laadimiskadude jaoks.

Arvutusnäide eeldatud arvudega: kui repiiter kasutab 1 Wh päevas, vajab ta nädalase varu jaoks vähemalt 7 Wh akut. See on 3.7 V juures umbes 2 Ah kasutatavat mahtu. Kui PVGIS näitab, et 1 W paneel annab sinu asukohas detsembris 0.5 Wh päevas, vajad vähemalt 2 W paneeli. 3 kuni 5 W paneel jätab varu pilvede, lume ja vananemise jaoks.

## Seadista repiiter {#config}

**Püsivara paigaldamine.** Kasuta [veebipõhist paigaldajat](https://flasher.meshcore.io) ja vali oma plaadile **Repeater**-püsivara. Paigaldamise sammud leiad lehelt [Alustamine](/get-started/#flash).

**Seadistamine USB kaudu.** Kui repiiter on veel arvutiga ühendatud, ava [config.meshcore.io](https://config.meshcore.io) või paigaldaja konsool. Võid kasutada ka mis tahes jadaterminali kiirusel 115200 baudi. Kõige tähtsamad käsud:

| Mida teha | Käsk |
|---|---|
| Muuda administraatori parooli | `password <new password>` |
| Pane nimi | `set name <name>` |
| Raadio eelseadistus: sagedus, ribalaius, SF, CR (rakendamiseks taaskäivita) | `set radio 869.618,62.5,8,8` |
| Töötsükli piirang protsentides | `set dutycycle 10` |
| Raadiokiibi saatevõimsus dBm-ides | `set tx <dBm>` |
| Asukoht, et repiiter kaartidel paistaks | `set lat <degrees>` ja `set lon <degrees>` |
| Kontaktandmed teistele käitajatele | `set owner.info <text>` |
| Tunnid üleujutusteadete vahel (neid kuuleb kogu võrk) | `set flood.advert.interval <hours>` |
| Anna repiitrist kohe teada | `advert` |
| Taaskäivita | `reboot` |

Administraatori vaikeparool on `password` ja igaüks, kes sellega sisse logib, saab administraatoriks. Muuda parool enne, kui repiiter eetrisse läheb.

Ülal olev `set radio` näide on eelseadistuse EU/UK (Narrow) jaoks. Kasuta selle asemel oma piirkonna eelseadistuse väärtusi: lehel [Soovitatud seaded](/guides/settings/) on need riikide kaupa kirjas.

**Kella seadmine.** Ilma kellamoodulita (RTC) kaotab repiiter iga voolukatkestusega kellaaja ja alustab uuesti 2024. aasta maist. Töö ajal kell ka triivib: see läheb järjest rohkem ette või taha. Seepärast sea kell aeg-ajalt õigeks: logi rakendusest kaugühendusega sisse ja kasuta käsku `clock sync` või sea aeg USB kaudu. RTC-mooduliga on seda harva vaja: moodul hoiab aega ka voolukatkestuste ajal ja triivib palju vähem.

**Kaughaldus.** Kui repiiter on võrgus, logi MeshCore'i rakendusest administraatori parooliga sisse. Seal näed selle olekut ja saad samu käske raadio kaudu kasutada. Mõni käsk töötab ainult USB kaudu, näiteks `set freq` ja tehaseseadete taastamise käsk `erase`.

**Identiteedi säilitamine.** Enne kustutamist sisesta USB kaudu `get prv.key` ja hoia kuvatud privaatvõti kindlas kohas. Pärast kustutamist annavad `set prv.key <key>` ja `reboot` repiitrile vana identiteedi tagasi. Nii leiavad seda tundvad sõlmed repiitri üles sama prefiksi alt.

Käskude täieliku loendi leiad [MeshCore'i CLI juhendist](https://github.com/meshcore-dev/MeshCore/blob/main/docs/cli_commands.md).

## Uuenda repiitrit üle õhu {#update}

Kui repiiter on kõrgel, uuendad seda maa pealt. Logi MeshCore'i rakendusest administraatori parooliga sisse, ava repiitri käsurida ja sisesta `start ota`. Edasine sõltub plaadist. Teised plaadid vastavad `Error` ja neid uuendad USB kaudu.

**nRF52-plaadid**, näiteks RAK, Heltec T114, Seeed XIAO ja SenseCAP Solar:

1. Laadi [veebipõhisest paigaldajast](https://flasher.meshcore.io) alla oma plaadi uue püsivara **ZIP**.
2. Sisesta `start ota`. Repiiter vastab `OK` ja on Bluetoothis nähtav nimega `<board>_OTA`, näiteks `RAK4631_OTA`.
3. Ava telefonis rakendus nRF Device Firmware Update, vali ZIP ja repiiter ning laadi fail üles. See võtab mõne minuti.

Paigalda nRF52-plaadile [OTAFIX-i alglaadur](https://github.com/oltaco/Adafruit_nRF52_Bootloader_OTAFIX) enne, kui selle üles viid. Tehase alglaaduriga saad ebaõnnestunud uuenduse parandada ainult USB kaudu. OTAFIX-iga läheb plaat tagasi uuendusrežiimi ja saad Bluetoothi kaudu uuesti proovida.

**ESP32-plaadid**, näiteks Heltec V3 ja V4:

1. Laadi veebipõhisest paigaldajast alla oma plaadi **non-merged** `.bin`: fail, mille nimes pole sõna "merged".
2. Sisesta `start ota`. Repiiter avab WiFi-võrgu nimega `MeshCore-OTA` ja saadab vastuseks oma üleslaadimislehe aadressi.
3. Ühenda WiFi levialas telefon või sülearvuti selle võrguga, ava aadress ja laadi fail üles.

## Seaduslikud piirangud {#legal}

{{< callout type="legal" verified="2026-10-02" >}}
MeshCore'i Euroopa eelseadistused asuvad alamribas **869.40-869.65 MHz**. ELis, Ühendkuningriigis, Šveitsis ja Norras tohivad lähitoimeseadmed seda ilma litsentsita kasutada järgmistes piirides:

- kiirgusvõimsus on kuni **500 mW e.r.p.**;
- töötsükkel on kuni **10%**: ühe seadme kohta kuni 360 sekundit saatmist mis tahes tunni jooksul. Teise võimalusena võib seade kasutada standardis ETSI EN 300 220-2 määratletud meetodit listen-before-talk koos kohanduva sagedusvahetusega;
- kogu signaal, laiusega kuni 250 kHz, peab jääma alamriba sisse.

Riba on jagatud: sa ei tohi segada litsentsitud teenuseid ja teised võivad segada sind.
Raadiol peab olema CE-märgis (Suurbritannias CE või UKCA).
{{< /callout >}}

Allikad: [CEPT ERC soovitus 70-03](https://docdb.cept.org/document/845), lisa 1, riba h1.7; [komisjoni otsus 2006/771/EÜ](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02006D0771(01)-20250123) ja selle muudatused; [ETSI EN 300 220-2](https://www.etsi.org/deliver/etsi_en/300200_300299/30022002/03.03.01_60/en_30022002v030301p.pdf), riba O.

### Võimsus: e.r.p. ja sinu antenn {#erp}

Piirang kehtib *kiiratud* võimsuse kohta, mida mõõdetakse lihtsa dipoolantenni suhtes (e.r.p.). Antenni võimendus liidetakse, kaabli kadu lahutatakse. Tootjad annavad antenni võimenduse dBi-des, mis on 2.15 dB rohkem kui sama võimendus dBd-des (dipooli suhtes). Hoia selle tehte tulemus kuni 27 dBm (500 mW) piires:

> saatevõimsus (dBm) + antenni võimendus (dBi) − kaabli kadu (dB) − 2.15 ≤ 27

- Plaat saadab 22 dBm 1 dB kaoga kaabli kaudu 5 dBi antenni: 22 + 5 − 1 − 2.15 = 23.85 dBm, umbes 240 mW e.r.p. See jääb lubatud piiresse.
- 30 dBm (1 W) võimendiga plaat saadab signaali 3 dBi antenni: 30 + 3 − 2.15 = 30.85 dBm, umbes 1.2 W e.r.p. See ületab piirangu, seega vähenda saatevõimsust.

`set tx` määrab LoRa kiibi väljundi dBm-ides. Kiibi SX1262 enda ülempiir on 22 dBm ja püsivara sisestatud arvu ei kontrolli. Lisavõimendiga plaadid, näiteks Heltec V4 või Station G2, saadavad palju suurema võimsusega, kui määratud arv näitab. Vaata enne seadistamist tootja tabelit ja alusta väikesest väärtusest.

### Töötsükkel {#duty-cycle}

Repiiter saadab kõigile enda ümber, seega kulutab ta oma eetriaega kiiremini kui kaasseade. MeshCore'i töötsükli piiraja vaikeväärtus on 50%, mis ületab selles ribas lubatu. Sea igal repiitril väärtuseks 10%:

```text
set dutycycle 10
```

### Sageduse täpsus {#frequency}

Kanal EU/UK (Narrow), 869.618 MHz ribalaiusega 62.5 kHz, ulatub kuni 869.649 MHz-ni: vähem kui 1 kHz alamriba ülemisest piirist allpool. Signaal peab igal temperatuuril ribasse jääma. Selleks on vaja temperatuurikompenseeritud kristalli (TCXO). See on peaaegu igal praegusel plaadil. Vanemad plaadid, millel seda pole, näiteks Heltec V2, triivivad 62.5 kHz juures usaldusväärseks tööks liiga palju.

### Märkused riikide kohta {#countries}

- **ELi liikmesriigid** peavad selle alamriba nendel tingimustel kättesaadavaks tegema (otsus 2006/771/EÜ, artikkel 3).
- **Ühendkuningriik:** samad piirangud on Ofcomi dokumendis [IR 2030](https://www.ofcom.org.uk/spectrum/radio-equipment/short-range-devices).
- **Šveits ja Liechtenstein:** samad piirangud on OFCOM-i dokumendis [RIR1008-09](https://www.ofcomnet.ch/api/rir/1008/09).
- **Norra:** samad piirangud on [üldlubade määruses](https://lovdata.no/dokument/SF/forskrift/2012-01-19-77) (fribruksforskriften).

Need märkused ei ole õigusnõu. Reeglid muutuvad. Kahtluse korral küsi oma riigi reguleerivalt asutuselt.

## Paigalduse kontrollnimekiri {#checklist}

- [ ] Asukoha omanik on nõus ja sa pääsed hoolduseks repiitrini.
- [ ] Plaadil töötab **Repeater**-püsivara ja antenn ühendati enne esimest sisselülitamist.
- [ ] Administraatori parool on muudetud.
- [ ] Raadio vastab [sinu piirkonna eelseadistusele](/guides/settings/) (`get radio`).
- [ ] Käsk `set dutycycle 10` on antud.
- [ ] Saatevõimsus koos antenni võimendusega jääb 500 mW e.r.p. piiresse.
- [ ] Nimi, asukoht ja `owner.info` on seatud, et teised teaksid, kes repiitrit käitab.
- [ ] Kell on seatud (`clock`).
- [ ] Korpus on suletud ning sellel on äravoolu- või õhutusava, kaablil on tilgasilmus.
- [ ] Aku ja paneel on arvutatud talve halvima kuu järgi.
- [ ] Testisid repiitrit enne asukohast lahkumist rakendusega eemalt.
- [ ] Sinu kohalik grupp teab, et repiiter töötab.
