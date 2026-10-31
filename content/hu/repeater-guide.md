---
title: Átjátszó-útmutató
lead: A magasra telepített átjátszó mindenkinek továbbítja az üzeneteket a környéken, akár egy egész városban vagy völgyben. Válassz helyet, tápláld napelemmel, állítsd be, és maradj a törvényes kereteken belül.
description: 'MeshCore átjátszó tervezése, táplálása, beállítása és szabályos üzemeltetése Európában: helyválasztás, napelem méretezése, CLI-beállítások, 868 MHz-es teljesítmény- és kitöltési tényező-korlátok.'
eyebrow: 868 MHz · legfeljebb 500 mW · engedély nélkül
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '7c7e3be3'
  seeded: '2026-10-31'
  fields: {title: '4608abcd', lead: 'bc670c65', description: '9e483ce5', eyebrow: '9fd33416'}
  sections: ['05ee477a', '938c518c', '766086be', '70faf508', '8bc641aa', '399cd683', 'e9dedb7b', '92beca03', '17634750', 'cadf6024', 'e9cc6834', '2e6e59ca', 'fb44b8db']
  blocks: ['20ac0371', 'ed2b1adf', '432543ee', '7af42c89', 'd0f7543a', '9ef3580f', '3476aef7', '1bab7bec', '6a7c4493', 'dbd9fa1f', 'aa06d32b', '9958aad3', 'd162b028', 'cca1bbdf', '64ef011d', 'e7f16724', 'd2e34ff0', 'bb195cfc', '8d080bb3', '2b1d995b', '210f1b66', 'dc7419d2', 'bdc66db0', 'b59f248c', '7184bd63', 'de5a24f9', 'f5cfb426', '48c7422f', '9d3c0836', 'da8a6af3', '240126df', '8aac2b33', '81a475b8', 'a53e42b5', '36ff1db4', 'e4ca8602', 'e4594afd', '3b24b8e9', '58330858', '68f2966e', 'd7418228', '23536e60', 'cbc5c2d1', '2ea02ba9', '92540256', '6e21f681', 'a8c12311', '3382ae7f', 'cdeafb0f', '1b1319d2']
---

Az átjátszók tartják össze a mesh-t. A companionök (a rádiók, amelyekről üzenetet küldesz) nem
továbbítanak üzeneteket, ezért
átjátszók nélkül csak a közvetlen hatótávolságban lévőket éred el. Egy jó helyen álló
átjátszó a környéken mindenkinek kiterjeszti a mesh-t. Ez az útmutató a MeshCore
firmware v1.18.0 verzióját követi.

Mielőtt belekezdesz, beszélj a [helyi csoportoddal](/community/). Ők tudják, hol
hiányzik a lefedettség, [melyik presetet használja a környéked](/guides/settings/), és hogyan nevezik el az átjátszókat. Nézd meg a
[lefedettségi térképeken](/map/), milyen átjátszók vannak a közeledben, és köszönj a nyilvános
vagy helyi [csatornákon](/guides/channels/).

## Kell egyáltalán? {#need}

Az átjátszó minden hallott flood üzenetet továbbküld, és a hatótávolságban lévő
összes átjátszó ugyanazon az adási időn osztozik. Ahol a mesh már elér, ott egy újabb
átjátszó forgalmat ad hozzá, lefedettséget nem. Egy magasra tett companion, például padlásablakban
vagy erkélyen, már elég lehet.

Ott állíts fel átjátszót, ahol hiányzik a lefedettség:

- a [lefedettségi térképeken](/map/) nincs átjátszó a közeledben, vagy csak olyan, amelyet a
  companionöd nem hall;
- a helyi csoportod szerint a környéknek szüksége van egyre.

## Válassz helyet {#site}

A magasság többet ér a teljesítménynél. A LoRa 868 MHz-en szabad rálátás mellett
jut a legmesszebbre. A dombok, épületek és sűrű fák sokkal több hatótávot vesznek el,
mint amennyit néhány extra milliwatt visszahoz.

- **Menj magasra.** Egy háztető, árboc, magas épület vagy domb sokkal nagyobb területet lát be,
  mint egy ablakpárkány. Már néhány méter a környező tetők fölött is segít.
- **Hagyd szabadon az antennát.** Szereld a tetőperem fölé, távol a fémtől,
  ereszcsatornáktól és más antennáktól.
- **Ellenőrizd a rálátást.** A [HeyWhatsThat](https://www.heywhatsthat.com/) és hasonló eszközök
  megmutatják, mi látszik egy adott helyről. Ha egy pontot látsz, az ottani átjátszót is eléred.
- **Hagyj szabad teret.** A rádiós útvonal körül is kell némi szabad tér,
  nem elég, ha csak a közvetlen vonal szabad. Nagy távolságon az útvonal közepének több méterrel
  kell az akadályok fölött haladnia.
- **Kérj engedélyt.** Szerezd meg a tető vagy az árboc tulajdonosának beleegyezését, és egyezzetek meg,
  hogyan férsz hozzá az átjátszóhoz karbantartáskor.

## Hardver {#hardware}

- **Panel.** Válassz alacsony fogyasztású nRF52 panelt, például a
  [Heltec T114](/devices/), a RAK WisBlock vagy a SenseCAP Solar Node típust. Az ESP32
  panelek többet fogyasztanak (az eszközoldal High jelöléssel látja el őket), így
  nehéz őket napelemről üzemeltetni.
- **Antenna.** 868 MHz-re készült antennát használj, függőlegesen felszerelve; az
  [antenna-útmutató](/guides/antenna/) bemutatja a típusokat, csatlakozókat, kábeleket és
  a rögzítést. Az antenna nyeresége beleszámít a törvényes teljesítménykorlátba; lásd:
  [Törvényes korlátok](#legal).
- **Kábel.** A koaxkábel legyen rövid, vagy használj kis veszteségű kábelt. 868 MHz-en néhány
  méter vékony kábel a teljesítményed felét is elnyelheti.
- **Doboz.** Időjárásálló doboz (IP65 vagy jobb) kábeltömszelencével, a páralecsapódás ellen
  szellőző- vagy vízelvezető nyílással, világos színben vagy napellenzővel.
  Az akkumulátorok rosszul bírják a hőséget, fagypont alatt pedig nem tölthetők.
- **Villám.** A tetőn lévő antenna célpont. Kövesd a földelésre vonatkozó helyi szabályokat,
  vagy szereld oda, ahol egy becsapódás nem érné el az épület
  vezetékeit.

## Táplálás és a napelem méretezése {#power}

A napelemes átjátszónak ki kell bírnia a tél legsötétebb heteit. Ezekre
méretezd:

1. **Mérd meg a terhelést.** Járasd a beállított átjátszót egy napig egy USB-s
   fogyasztásmérőn keresztül. Olvasd le a felhasznált energiát wattórában (Wh). A környékbeli
   forgalom befolyásolja az értéket, ezért ha lehet, a helyszínen mérj.
2. **Számolj tartalékkal.** Az akkumulátor kapacitását legalább 5-7, hasznos
   napfény nélküli napra tervezd.
3. **Nézd meg a téli napsütést.** Az EU ingyenes
   [PVGIS eszköze](https://re.jrc.ec.europa.eu/pvg_tools/en/) bármely helyre megmutatja,
   mennyi energiát termel egy napelem havonta. A legkevesebb napsütésű hónappal számolj.
4. **Méretezd a napelemet.** A napelemnek a legrosszabb hónapban is pótolnia kell a napi fogyasztást,
   és maradjon tartalék a töltési veszteségekre is.

Számpélda, feltételezett értékekkel: egy napi 1 Wh-t fogyasztó átjátszónak
egyhetes tartalékhoz legalább 7 Wh-s akkumulátor kell, ez körülbelül 2 Ah
hasznos kapacitás 3.7 V-on. Ha a PVGIS szerint a helyszíneden egy 1 W-os napelem decemberben
napi 0.5 Wh-t ad, legalább 2 W-os napelem kell, 3-5 W-tal pedig
marad tartalék a felhőkre, a hóra és az öregedésre.

## Beállítás {#config}

**Flashelés.** Nyisd meg a [webes flashert](https://flasher.meshcore.io), és válaszd a paneledhez a
**Repeater** firmware-t. A flashelés lépéseit a
[Kezdő lépések](/get-started/#flash) oldalon találod.

**Beállítás USB-n.** Amíg az átjátszó még a számítógépedhez csatlakozik,
nyisd meg a [config.meshcore.io](https://config.meshcore.io) oldalt vagy a flasher
konzolját. Bármilyen soros terminált is használhatsz 115200 baudon. A legfontosabb
parancsok:

| Mit | Parancs |
|---|---|
| Az admin jelszó módosítása | `password <new password>` |
| Elnevezés | `set name <name>` |
| Rádiós preset: frekvencia, sávszélesség, SF, CR (újraindítás után érvényes) | `set radio 869.618,62.5,8,8` |
| Kitöltési tényező korlátja, százalékban | `set dutycycle 10` |
| A rádiócsip adóteljesítménye, dBm-ben | `set tx <dBm>` |
| Pozíció, hogy megjelenjen a térképeken | `set lat <degrees>` és `set lon <degrees>` |
| Elérhetőség más üzemeltetők számára | `set owner.info <text>` |
| Órák száma a flood advertek között (ezeket az egész mesh hallja) | `set flood.advert.interval <hours>` |
| Azonnali bejelentés | `advert` |
| Újraindítás | `reboot` |

Az alapértelmezett admin jelszó `password`, és aki ezzel lép be,
admin lesz. Változtasd meg, mielőtt az átjátszó adásba kerül.

A fenti `set radio` példa az EU/UK (Narrow) presetre vonatkozik. Helyette a környéked presetjének értékeit használd:
a [Javasolt beállítások](/guides/settings/) oldal országonként felsorolja őket.

**Állítsd be az órát.** Óramodul (RTC) nélkül az átjátszó minden áramszünetnél elveszíti
az időt, és újraindulás után 2024 májusát mutatja. Működés közben az órája el is csúszik:
egyre jobban siet vagy késik. Ezért időnként állítsd be: lépj be távolról
az appból, és használd a `clock sync` parancsot, vagy állítsd be az időt USB-n. RTC modullal
ritkán kell ezt megtenned: az áramszünetek alatt is megtartja az időt, és sokkal kevésbé csúszik el.

**Kezeld távolról.** Amikor már a mesh-en van, lépj be a MeshCore appból
az admin jelszóval. Itt látod az állapotát, és ugyanazokat a parancsokat rádión keresztül is
használhatod. Néhány parancs csak USB-n működik, például a `set freq` és a gyári
visszaállítás, az `erase`.

**Őrizd meg az identitását.** Törlés előtt írd be USB-n a `get prv.key` parancsot, és tedd
biztonságos helyre a megjelenő privát kulcsot. A törlés után a `set prv.key <key>`
és egy `reboot` visszaadja az átjátszó régi identitását, így az azt ismerő csomópontok
ugyanazzal az előtaggal találják meg.

A teljes parancslistát a
[MeshCore CLI-referencia](https://github.com/meshcore-dev/MeshCore/blob/main/docs/cli_commands.md) tartalmazza.

## Frissítés vezeték nélkül {#update}

Ha az átjátszó már fent van a magasban, a földről frissíted. Lépj be a
MeshCore appból az admin jelszóval, nyisd meg a parancssorát, és írd be:
`start ota`. A folytatás a paneltől függ; más panelek `Error` választ adnak,
ezeket USB-n frissíted.

**nRF52 panelek**, például RAK, Heltec T114, Seeed XIAO és SenseCAP Solar:

1. Töltsd le a paneledhez az új firmware **ZIP** fájlját a
   [webes flasherből](https://flasher.meshcore.io).
2. Írd be: `start ota`. Az átjátszó `OK` választ ad, és Bluetooth-on
   `<board>_OTA` néven jelenik meg, például `RAK4631_OTA`.
3. Nyisd meg a telefonodon az nRF Device Firmware Update appot, válaszd ki a ZIP fájlt és
   az átjátszót, majd töltsd fel. Néhány percig tart.

Telepítsd az [OTAFIX bootloadert](https://github.com/oltaco/Adafruit_nRF52_Bootloader_OTAFIX)
az nRF52 panelre, mielőtt felszereled. A gyári bootloaderrel egy sikertelen
frissítést csak USB-n lehet helyrehozni. OTAFIX-szel a panel visszaáll
frissítési módba, és Bluetooth-on újra próbálkozhatsz.

**ESP32 panelek**, például a Heltec V3 és V4:

1. Töltsd le a webes flasherből a paneledhez a **non-merged** `.bin` fájlt:
   azt, amelynek a nevében nem szerepel a "merged" szó.
2. Írd be: `start ota`. Az átjátszó megnyit egy `MeshCore-OTA` nevű WiFi hálózatot,
   és válaszul megadja a feltöltőoldala címét.
3. A WiFi hatótávolságán belül csatlakoztasd a telefonodat vagy laptopodat ehhez a hálózathoz, nyisd meg
   a címet, és töltsd fel a fájlt.

## Törvényes korlátok {#legal}

{{< callout type="legal" verified="2026-10-02" >}}
A MeshCore európai presetjei a **869.40-869.65 MHz** alsávba esnek. Az
EU-ban, az Egyesült Királyságban, Svájcban és Norvégiában ezt rövid hatótávú eszközök engedély nélkül
használhatják, a következő korlátok között:

- legfeljebb **500 mW e.r.p.** kisugárzott teljesítmény;
- legfeljebb **10% kitöltési tényező**: eszközönként óránként legfeljebb 360 másodperc
  adás. Ehelyett egy eszköz alkalmazhat listen-before-talk eljárást
  adaptív frekvenciaváltással is, az ETSI EN 300 220-2 szerint;
- a teljes, legfeljebb 250 kHz széles jelnek az alsávon belül kell maradnia.

A sáv közös: nem zavarhatod az engedélyhez kötött szolgáltatásokat, mások viszont zavarhatnak téged.
A rádiónak CE jelöléssel kell rendelkeznie (Nagy-Britanniában CE vagy UKCA jelöléssel).
{{< /callout >}}

Források: [CEPT ERC Recommendation 70-03](https://docdb.cept.org/document/845),
1. melléklet, h1.7 sáv;
[a Bizottság 2006/771/EK határozata](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02006D0771(01)-20250123)
és módosításai;
[ETSI EN 300 220-2](https://www.etsi.org/deliver/etsi_en/300200_300299/30022002/03.03.01_60/en_30022002v030301p.pdf),
O sáv.

### Teljesítmény: az e.r.p. és az antennád {#erp}

A korlát a *kisugárzott* teljesítményre vonatkozik, egy egyszerű dipólantennához mérve
(e.r.p.). Az antenna nyeresége hozzáadódik, a kábelveszteség levonódik. A gyártók az
antennanyereséget dBi-ben adják meg, ez 2.15 dB-lel több, mint ugyanez a nyereség dBd-ben
(dipólhoz viszonyítva). Tartsd ezt az összeget legfeljebb 27 dBm-en (500 mW):

> adóteljesítmény (dBm) + antennanyereség (dBi) − kábelveszteség (dB) − 2.15 ≤ 27

- Egy panel 22 dBm-mel ad egy 5 dBi-s antennára, 1 dB veszteségű kábelen át:
  22 + 5 − 1 − 2.15 = 23.85 dBm, ez körülbelül 240 mW e.r.p. A korláton belül van.
- Egy panel 30 dBm-es (1 W) erősítővel ad egy 3 dBi-s antennára:
  30 + 3 − 2.15 = 30.85 dBm, ez körülbelül 1.2 W e.r.p. Túllépi a korlátot: csökkentsd
  az adóteljesítményt.

A `set tx` a LoRa csip kimenetét állítja be, dBm-ben. Maga az SX1262 csip legfeljebb
22 dBm-re képes; a firmware nem ellenőrzi a beírt számot. A külön
erősítővel szerelt panelek, például a Heltec V4 vagy a Station G2, sokkal többet sugároznak,
mint a beállított érték. Beállítás előtt nézd meg a gyártó táblázatát, és
alacsony értékkel kezdj.

### Kitöltési tényező {#duty-cycle}

Az átjátszó a környéken mindenkinek továbbít, ezért gyorsabban éli fel az adási idejét,
mint egy companion. A MeshCore kitöltésitényező-korlátozójának alapértéke 50%, ami
több, mint amit ez a sáv megenged. Minden átjátszón állítsd 10%-ra:

```text
set dutycycle 10
```

### Frekvenciapontosság {#frequency}

Az EU/UK (Narrow) csatorna, 869.618 MHz 62.5 kHz sávszélességgel, egészen
869.649 MHz-ig ér: kevesebb mint 1 kHz-cel az alsáv felső széle alatt. A jelnek
minden hőmérsékleten a sávon belül kell maradnia. Ehhez
hőmérséklet-kompenzált kristály (TCXO) kell. Szinte minden mai panelen van ilyen;
a régebbi, TCXO nélküli panelek, például a Heltec V2, túlságosan elcsúsznak ahhoz, hogy
62.5 kHz-en megbízhatóan működjenek.

### Országonkénti megjegyzések {#countries}

- Az **EU tagállamainak** ezen feltételekkel elérhetővé kell tenniük ezt az alsávot
  (2006/771/EK határozat, 3. cikk).
- **Egyesült Királyság:** ugyanezek a korlátok, az Ofcom
  [IR 2030](https://www.ofcom.org.uk/spectrum/radio-equipment/short-range-devices) dokumentumában.
- **Svájc és Liechtenstein:** ugyanezek a korlátok, az OFCOM
  [RIR1008-09](https://www.ofcomnet.ch/api/rir/1008/09) dokumentumában.
- **Norvégia:** ugyanezek a korlátok, az
  [általános engedélyekről szóló rendeletben](https://lovdata.no/dokument/SF/forskrift/2012-01-19-77)
  (fribruksforskriften).

Ezek a megjegyzések nem jogi tanácsok. A szabályok változnak; kétség esetén érdeklődj
a nemzeti hírközlési hatóságnál.

## Telepítési ellenőrzőlista {#checklist}

- [ ] A helyszín tulajdonosa beleegyezett, és karbantartáskor hozzáférsz az átjátszóhoz.
- [ ] A panelen a **Repeater** firmware fut, és az antennát az első bekapcsolás előtt
      csatlakoztattad.
- [ ] Az admin jelszót megváltoztattad.
- [ ] A rádió megfelel [a környéked presetjének](/guides/settings/) (`get radio`).
- [ ] A `set dutycycle 10` be van állítva.
- [ ] Az adóteljesítmény és az antennanyereség együtt nem lépi túl az 500 mW e.r.p. értéket.
- [ ] A név, a pozíció és az `owner.info` be van állítva, így mások tudják, ki üzemelteti.
- [ ] Az óra be van állítva (`clock`).
- [ ] A doboz le van zárva, van rajta vízelvezető vagy szellőzőnyílás, és a kábelen van
      csepegtető hurok.
- [ ] Az akkumulátor és a napelem a legrosszabb téli hónapra van méretezve.
- [ ] A helyszín elhagyása előtt távolról kipróbáltad az appal.
- [ ] A helyi csoportod tudja, hogy működik.
