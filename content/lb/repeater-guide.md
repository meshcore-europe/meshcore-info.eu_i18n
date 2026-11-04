---
title: Repeater-Guide
lead: E Repeater op enger héijer Plaz gëtt Messagen un all d'Leit ronderëm weider, iwwer eng ganz Stad oder en ganzen Dall. Wiel e Standuert, bedreif en mat Solarstroum, riicht en an a bleif am Kader vum Gesetz.
description: 'E MeshCore-Repeater an Europa plangen, mat Stroum versuergen, konfiguréieren a legal bedreiwen: Standuert, Solardimensioun, CLI-Astellungen, 868 MHz Leeschtung an Duty-Cycle-Limitten.'
eyebrow: 868 MHz · bis zu 500 mW · ouni Lizenz
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '3e38a8c6'
  seeded: '2026-11-04'
  fields: {title: '4608abcd', lead: 'bc670c65', description: '9e483ce5', eyebrow: '9fd33416'}
  sections: ['05ee477a', '938c518c', '824ab38e', '662ea23c', '70faf508', '8bc641aa', '399cd683', 'e9dedb7b', '92beca03', '17634750', 'cadf6024', 'e9cc6834', '2e6e59ca', 'fb44b8db']
  blocks: ['20ac0371', 'ed2b1adf', '432543ee', '7af42c89', 'd0f7543a', '9ef3580f', '3476aef7', '1bab7bec', 'bbea9a0c', '2b9fab3b', 'b13d1947', 'c2bad16f', '636edc86', 'c2d6bcd1', '957ae975', '98874949', '96d1ebad', 'dbd9fa1f', 'aa06d32b', '9958aad3', 'd162b028', 'cca1bbdf', '64ef011d', 'e7f16724', 'd2e34ff0', 'bb195cfc', '8d080bb3', '2b1d995b', '210f1b66', 'dc7419d2', 'bdc66db0', 'b59f248c', '7184bd63', 'de5a24f9', 'f5cfb426', '48c7422f', '9d3c0836', 'da8a6af3', '240126df', '8aac2b33', '81a475b8', 'a53e42b5', '36ff1db4', 'e4ca8602', 'e4594afd', '3b24b8e9', '58330858', '68f2966e', 'd7418228', '23536e60', 'cbc5c2d1', '2ea02ba9', '92540256', '6e21f681', 'a8c12311', '3382ae7f', 'cdeafb0f', '1b1319d2']
---

D'Repeatere droen d'Mesh. Companions, d'Radioen, mat deenen s du Message schécks, gi keng Message weider. Ouni Repeatere erreechs du also nëmmen d'Leit an denger direkter Reechwäit. E Repeater op der richteger Plaz vergréissert d'Mesh fir jiddereen ronderëm. Dëse Guide baséiert op der MeshCore-Firmware v1.18.0.

Schwätz virum Ufank mat denger [lokaler Grupp](/community/). Si weess, wou d'Ofdeckung feelt, [wéi ee Preset deng Regioun benotzt](/guides/settings/) a wéi s du Repeatere nenne solls. Kuck op den [Ofdeckungskaarten](/map/) no Repeateren an denger Géigend, a so Moien op den ëffentlechen oder lokale [Kanäl](/guides/channels/).

## Brauchs du een? {#need}

E Repeater schéckt all Flood-Message weider, déi en héiert, an all Repeateren a Reechwäit deelen déi selwecht Sendezäit. Wou d'Mesh dech schonn erreecht, bréngt nach e Repeater méi Traffic, keng méi grouss Ofdeckung. E Companion op enger héijer Plaz, un enger Späicherfënster oder um Balcon, ka scho genuch sinn.

Riicht e Repeater do an, wou d'Ofdeckung feelt:

- d'[Ofdeckungskaarte](/map/) weise keng Repeateren an denger Géigend, oder nëmmen där, déi däi Companion net héiert;
- deng lokal Grupp seet, datt d'Géigend ee brauch.

## Wiel e Standuert {#site}

Héicht zielt méi wéi Leeschtung. LoRa op 868 MHz geet am beschte laanscht eng fräi Siichtlinn. Hiwwelen, Gebaier an dicht Beem kaschte vill méi Reechwäit, wéi e puer Milliwatt méi erëmbréngen.

- **Géi no uewen.** En Daach, e Mast, en héicht Gebai oder en Hiwwel deckt
  vill méi of wéi eng Fënsterbänk. Schonn e puer Meter iwwer den Diecher
  ronderëm hëllefen.
- **Hal d'Antenne fräi.** Montéier se iwwer d'Daachkanten, ewech vu
  Metall, Kéngelen an aneren Antennen.
- **Préif d'Siicht.** Tools wéi [HeyWhatsThat](https://www.heywhatsthat.com/)
  weisen, wat ee vun enger Plaz aus gesäit. D'MeshCore-App
  [rechent aus, wat e Repeater do erreeche kann](#check-site).
- **Looss Plaz fräi.** E Funkwee brauch fräie Raum ronderëm déi direkt Linn,
  net nëmmen d'Linn selwer. Bei 868 MHz sinn dat ongeféier 20 m ronderëm
  d'Mëtt vun engem Wee vu 5 km. Iwwer 20 km sinn et ongeféier 40 m.
- **Fro no Erlaabnes.** Hol dir d'Zoustëmmung vum Besëtzer fir den Daach oder
  de Mast, a maach aus, wéi s du fir d'Wartung bei de Repeater kënns.

### Préif e Standuert an der App {#check-site}

D'MeshCore-App huet vun der Versioun 1.33 un dës Tools am Menü ënner **Tools**.
Si funktionéieren och, wann kee Radio ugeschloss ass.

- **Line of Sight** zeechent de Buedem tëscht 2 Punkten, an de Raum, deen
  d'Signal driwwer brauch. Dréck laang op 2 Punkten op der Kaart, oder tipp op Repeateren.
- **Antenna Coverage** weist op der Kaart, wat eng Antenn op 1 Punkt erreeche kann.
  Dréck laang op e Punkt oder tipp op e Repeater. Setz méi Punkten derbäi, fir Standuerter ze vergläichen.

Um Computer wiels du am Menü vum Tool **Add Point** a gëss d'Koordinaten an.

Béid Tools fänke mat der Antenn op dengem Standuert op 5 m un. Stell dofir
d'Héicht, déi s du plangs, an den Astellunge vum Tool an. Antenna Coverage
fänkt mat enger Empfangsantenn op 1 m un. Ouni ugeschlossene Radio fänkt Line
of Sight op 915 MHz un: stell d'Frequenz vun dengem [Preset](/guides/settings/)
a sengen Astellungen an.

D'Tools rechne mat Héichtdaten a testen net däi Radio. Préif Beem an nei Gebaier selwer, huel dann e Companion mat op d'Plaz a kuck, wéi eng Repeateren en héiert.

![Line of Sight an der MeshCore-App: de Buedem tëscht 2 Punkten, an de Raum, deen d'Signal driwwer brauch](/media/guides/line-of-sight.webp)

![Antenna Coverage an der MeshCore-App: d'Géigend, déi eng Antenn op engem Hiwwel erreeche kann, op enger Kaart](/media/guides/antenna-coverage.webp)

## Hardware {#hardware}

- **Board.** Wiel en nRF52-Board mat nidderegem Verbrauch, wéi den [Heltec T114](/devices/), RAK WisBlock oder de SenseCAP Solar Node. ESP32-Boards brauche méi Stroum (d'Apparater-Säit markéiert se mat High), an dat mécht de Solarbetrib schwéier.
- **Antenn.** Benotz eng Antenn, déi fir 868 MHz gemaach ass, a montéier se vertikal; den [Antennen-Guide](/guides/antenna/) erkläert Typen, Stecker, Kabel a Montage. Den Antennegain zielt bei der gesetzlecher Leeschtungslimitt mat; kuck [Gesetzlech Limitten](#legal).
- **Kabel.** Hal d'Koaxialkabel kuerz, oder benotz Kabel mat nidderegem Verloscht. Op 868 MHz kënnen e puer Meter dënne Kabel d'Halschent vun denger Leeschtung kaschten.
- **Gehäis.** Eng wiederfest Këscht (IP65 oder besser) mat enger Kabeldurchféierung, engem Lëftungs- oder Oflafslach géint Kondensatioun, an enger heller Faarf oder engem Sonneschutz. Batterië leiden ënner Hëtzt, an ënnert dem Gefréierpunkt kanns du se net lueden.
- **Blëtz.** Eng Antenn um Daach ass en Zil. Hal dech un déi lokal Regele fir d'Äerdung, oder montéier se do, wou e Blëtz net un d'Stroumleitunge vum Gebai kënnt.

## Stroum a Solaranlag dimensionéieren {#power}

E Solar-Repeater muss déi däischterst Woche vum Wanter iwwerstoen. Dimensionéier en dofir:

1. **Moos de Verbrauch.** Looss de konfiguréierte Repeater een Dag laang un engem USB-Leeschtungsmesser lafen. Lies déi verbraucht Energie a Wattstonnen (Wh) of. Den Traffic an denger Géigend verännert d'Zuel, moos also wa méiglech op der Plaz.
2. **Plang Reserv an.** Plang d'Batteriekapazitéit fir op d'mannst 5 bis 7 Deeg ouni notzbar Sonn.
3. **Fann deng Wantersonn.** Dat gratis [PVGIS-Tool](https://re.jrc.ec.europa.eu/pvg_tools/en/) vun der EU weist fir all Standuert, wéi vill Energie e Panneau pro Mount produzéiert. Huel de Mount mat der wéinegster Sonn.
4. **Dimensionéier de Panneau.** De Panneau muss an deem schlechtste Mount den Dagesverbrauch ersetzen, mat Spillraum fir Ladeverloschter.

E Rechebeispill mat ugehollenen Zuelen: e Repeater, deen 1 Wh pro Dag verbraucht, brauch eng Batterie vun op d'mannst 7 Wh fir eng Woch Reserv, ongeféier 2 Ah notzbar Kapazitéit bei 3.7 V. Wann PVGIS seet, datt e 1 W-Panneau op dengem Standuert am Dezember 0.5 Wh pro Dag liwwert, brauchs du op d'mannst e 2 W-Panneau. Mat 3 bis 5 W hues du Spillraum fir Wolleken, Schnéi an Alterung.

## Riicht en an {#config}

**Flashen.** Benotz de [Web-Flasher](https://flasher.meshcore.io) a wiel d'**Repeater**-Firmware fir däi Board. D'Schrëtt fir ze flashe fënns du ënner [Éischt Schrëtt](/get-started/#flash).

**Iwwer USB konfiguréieren.** Looss de Repeater un dengem Computer ugeschloss a maach [config.meshcore.io](https://config.meshcore.io) oder d'Konsol vum Flasher op. Du kanns och all seriellen Terminal mat 115200 Baud benotzen. Déi wichtegst Befeeler:

| Wat | Befehl |
|---|---|
| Admin-Passwuert änneren | `password <new password>` |
| Numm ginn | `set name <name>` |
| Radio-Preset: Frequenz, Bandbreet, SF, CR (gëllt no engem Restart) | `set radio 869.618,62.5,8,8` |
| Duty-Cycle-Limitt, a Prozent | `set dutycycle 10` |
| Sendeleeschtung vum Radio-Chip, an dBm | `set tx <dBm>` |
| Positioun, fir datt en op de Kaarte steet | `set lat <degrees>` an `set lon <degrees>` |
| Kontaktinformatioune fir aner Bedreiwer | `set owner.info <text>` |
| Stonnen tëscht Flood-Adverts, déi déi ganz Mesh héiert | `set flood.advert.interval <hours>` |
| Elo ukënnegen | `advert` |
| Nei starten | `reboot` |

D'Standard-Admin-Passwuert ass `password`, a jiddereen, deen sech domat aloggt, gëtt Admin. Änner et, ier de Repeater ufänkt ze senden.

D'Beispill `set radio` uewen ass EU/UK (Narrow). Benotz amplaz d'Wäerter vum Preset vun denger Regioun: [Recommandéiert Astellungen](/guides/settings/) lëscht se pro Land op.

**D'Auer astellen.** Ouni Auermodul (RTC) verléiert e Repeater bei all Stroumausfall d'Zäit a fänkt nees am Mee 2024 un. Wärend e leeft, verrutscht seng Auer och: si geet ëmmer méi vir oder no. Stell d'Auer also vun Zäit zu Zäit: logg dech vun der App aus op Distanz an a benotz `clock sync`, oder stell d'Zäit iwwer USB an. Mat engem RTC-Modul muss du dat seele maachen: en hält d'Zäit bei Stroumausfäll a verrutscht vill manner.

**Op Distanz verwalten.** Soubal en an der Mesh ass, logg dech mam Admin-Passwuert aus der MeshCore-App an. Do liess du säi Status a benotz déi selwecht Befeeler iwwer Radio. Verschidde Befeeler funktionéieren nëmmen iwwer USB, wéi `set freq` an de Factory-Reset `erase`.

**Seng Identitéit behalen.** Tipp virun engem Erase `get prv.key` iwwer USB a späicher de private Schlëssel, deen e weist, op enger sécherer Plaz. Nom Erase ginn `set prv.key <key>` an e `reboot` dem Repeater seng al Identitéit zréck. Esou fannen d'Noden, déi e kennen, hien ënner deem selwechte Prefix.

Déi komplett Lëscht vun de Befeeler fënns du an der [MeshCore CLI-Referenz](https://github.com/meshcore-dev/MeshCore/blob/main/docs/cli_commands.md).

## Aktualiséier en iwwer Funk {#update}

Wann de Repeater eemol uewen ass, aktualiséiers du en vum Buedem aus. Logg dech mam Admin-Passwuert aus der MeshCore-App an, maach seng Kommandozeil op an tipp `start ota`. Wat duerno kënnt, hänkt vum Board of; aner Boards äntweren `Error`, an déi aktualiséiers du iwwer USB.

**nRF52-Boards**, wéi RAK, Heltec T114, Seeed XIAO a SenseCAP Solar:

1. Lued den **ZIP** vun der neier Firmware fir däi Board vum [Web-Flasher](https://flasher.meshcore.io) erof.
2. Tipp `start ota`. De Repeater äntwert `OK` a weist sech iwwer Bluetooth als `<board>_OTA`, zum Beispill `RAK4631_OTA`.
3. Maach d'App nRF Device Firmware Update op dengem Telefon op, wiel den ZIP an de Repeater a lued en erop. Dat dauert e puer Minutten.

Installéier den [OTAFIX-Bootloader](https://github.com/oltaco/Adafruit_nRF52_Bootloader_OTAFIX) op engem nRF52-Board, ier et eropgeet. Mam Standard-Bootloader kanns du e feelgeschloenen Update nëmmen iwwer USB flécken. Mat OTAFIX geet d'Board zréck an den Update-Modus, an du probéiers et nach eng Kéier iwwer Bluetooth.

**ESP32-Boards**, wéi den Heltec V3 a V4:

1. Lued déi **net-gemergte** `.bin` fir däi Board vum Web-Flasher erof: de Fichier ouni "merged" am Numm.
2. Tipp `start ota`. De Repeater mécht e WiFi-Netz mam Numm `MeshCore-OTA` op an äntwert mat der Adress vu senger Upload-Säit.
3. Verbann däin Telefon oder Laptop a WiFi-Reechwäit mat deem Netz, maach d'Adress op a lued de Fichier erop.

## Gesetzlech Limitten {#legal}

{{< callout type="legal" verified="2026-10-02" >}}
Déi europäesch Presets vu MeshCore leien am Subband **869.40-869.65 MHz**. An der EU, am Vereenegte Kinnekräich, an der Schwäiz an an Norwegen ass et fir Apparater mat kuerzer Reechwäit ouni Lizenz op, bannent dëse Limitten:

- héchstens **500 mW e.r.p.** ofgestraalt Leeschtung;
- héchstens **10% duty cycle**: net méi wéi 360 Sekonnen Senden an all Stonn, pro Apparat. Alternativ däerf en Apparat Listen-before-talk mat adaptiver Frequenzagilitéit benotzen, wéi ETSI EN 300 220-2 et definéiert;
- dat ganzt Signal, héchstens 250 kHz breet, muss am Subband bleiwen.

D'Band ass gedeelt: du däerfs lizenzéiert Déngschter net stéieren, an anerer däerfen dech stéieren.
De Radio muss eng CE-Markéierung hunn (a Groussbritannien CE oder UKCA).
{{< /callout >}}

Quellen: [CEPT ERC Recommendation 70-03](https://docdb.cept.org/document/845), Annexe 1, Band h1.7; [Commission Decision 2006/771/EC](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02006D0771(01)-20250123) a seng Ännerungen; [ETSI EN 300 220-2](https://www.etsi.org/deliver/etsi_en/300200_300299/30022002/03.03.01_60/en_30022002v030301p.pdf), Band O.

### Leeschtung: e.r.p. an deng Antenn {#erp}

D'Limitt gëllt fir déi *ofgestraalt* Leeschtung, gemooss am Verglach mat enger einfacher Dipolantenn (e.r.p.). Den Antennegain zielt derbäi, de Kabelverloscht geet of. D'Hiersteller ginn den Antennegain an dBi un, an dat ass 2.15 dB méi wéi dee selwechte Gain an dBd (relativ zu engem Dipol). Hal dës Rechnung bei 27 dBm (500 mW) oder drënner:

> Sendeleeschtung (dBm) + Antennegain (dBi) − Kabelverloscht (dB) − 2.15 ≤ 27

- E Board sent 22 dBm an eng 5 dBi-Antenn iwwer 1 dB Kabelverloscht: 22 + 5 − 1 − 2.15 = 23.85 dBm, ongeféier 240 mW e.r.p. Dat ass bannent der Limitt.
- E Board mat engem 30 dBm (1 W) Verstäerker sent an eng 3 dBi-Antenn: 30 + 3 − 2.15 = 30.85 dBm, ongeféier 1.2 W e.r.p. Dat ass iwwer der Limitt; setz d'Sendeleeschtung erof.

`set tx` stellt d'Ausgangsleeschtung vum LoRa-Chip an, an dBm. De SX1262-Chip selwer geet bis maximal 22 dBm; d'Firmware kontrolléiert d'Zuel net, déi s du agëss. Boards mat engem zousätzleche Verstäerker, wéi den Heltec V4 oder d'Station G2, schécke vill méi eraus wéi d'Zuel, déi s du astells. Kuck an d'Tabell vum Hiersteller, ier s du se astells, a fänk niddereg un.

### Duty cycle {#duty-cycle}

E Repeater sent fir jidderee ronderëm, dofir verbraucht e seng Sendezäit méi séier wéi e Companion. De Duty-Cycle-Limiter vu MeshCore steet standardméisseg op 50%, an dat ass méi, wéi dëst Band erlaabt. Stell en op all Repeater op 10%:

```text
set dutycycle 10
```

### Frequenzgenauegkeet {#frequency}

De Kanal EU/UK (Narrow), 869.618 MHz mat 62.5 kHz Bandbreet, geet bis 869.649 MHz: manner wéi 1 kHz ënner dem ieweschten Enn vum Subband. D'Signal muss bei all Temperatur am Band bleiwen. Dofir brauchs du e temperaturkompenséierte Quarz (TCXO). Bal all aktuellt Board huet een; méi al Boards ouni een, wéi den Heltec V2, verrutschen ze wäit, fir bei 62.5 kHz zouverlässeg ze schaffen.

### Hiweiser pro Land {#countries}

- **EU-Memberstaaten** mussen dëst Subband zu dëse Konditiounen zur Verfügung stellen (Decision 2006/771/EC, Artikel 3).
- **Vereenegt Kinnekräich:** déi selwecht Limitten, an Ofcom [IR 2030](https://www.ofcom.org.uk/spectrum/radio-equipment/short-range-devices).
- **Schwäiz a Liechtenstein:** déi selwecht Limitten, an OFCOM [RIR1008-09](https://www.ofcomnet.ch/api/rir/1008/09).
- **Norwegen:** déi selwecht Limitten, an der [Reglementatioun iwwer allgemeng Autorisatiounen](https://lovdata.no/dokument/SF/forskrift/2012-01-19-77) (fribruksforskriften).

Dës Hiweiser si keng Rechtsberodung. D'Regelen änneren sech; am Zweiwel fro bei denger nationaler Reguléierungsautoritéit no.

## Checklëscht fir den Opbau {#checklist}

- [ ] De Proprietär vum Standuert ass d'accord, an du kënns fir d'Maintenance bei de Repeater.
- [ ] D'Board leeft mat der **Repeater**-Firmware, an d'Antenn war virum éischten Aschalten ugeschloss.
- [ ] D'Admin-Passwuert ass geännert.
- [ ] De Radio passt zum [Preset vun denger Regioun](/guides/settings/) (`get radio`).
- [ ] `set dutycycle 10` ass agestallt.
- [ ] Sendeleeschtung plus Antennegain bleiwe bannent 500 mW e.r.p.
- [ ] Numm, Positioun an `owner.info` si agestallt, fir datt anerer wëssen, wien en bedreift.
- [ ] D'Auer ass agestallt (`clock`).
- [ ] D'Gehäis ass dicht, mat engem Oflafs- oder Lëftungslach, an de Kabel huet eng Drëpsschleif.
- [ ] Batterie a Panneau si fir de schlëmmste Wantermount dimensionéiert.
- [ ] Du hues en op Distanz mat der App getest, ier s du d'Plaz verlooss hues.
- [ ] Deng lokal Grupp weess, datt e leeft.
