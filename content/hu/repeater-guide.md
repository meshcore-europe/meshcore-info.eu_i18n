---
title: Átjátszó útmutató
lead: Egy magasra telepített átjátszó mindenki üzeneteit továbbítja körülötte, egy egész városon vagy völgyön át. Válassz helyet, tápláld napenergiával, állítsd be, és maradj a törvény keretein belül.
description: 'Tervezd meg, lásd el árammal, állítsd be és üzemeltesd legálisan a MeshCore átjátszódat Európában: helyválasztás, napelem méretezése, CLI beállítások, 868 MHz teljesítmény- és kitöltési tényező korlátok.'
eyebrow: 868 MHz · legfeljebb 500 mW · engedélymentes
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '4a0fe39f'
  seeded: '2026-10-26'
  fields: {title: '4608abcd', lead: 'bc670c65', description: '9e483ce5', eyebrow: '9fd33416'}
  sections: ['1de4a4f7', '766086be', '70faf508', '8bc641aa', '2018aa04', '92beca03', '17634750', 'cadf6024', 'e9cc6834', '2e6e59ca', 'fb44b8db']
---

Az átjátszók tartják fenn a mesh-t. A companion eszközök, vagyis a rádiók, amelyekről üzenetet küldesz, nem adják tovább az üzeneteket, így átjátszók nélkül csak a közvetlen hatótávon belüli embereket éred el. Minden átjátszó, amit kihelyezel, bővíti a mesh-t mindenki számára a környéken. Ez az útmutató a MeshCore firmware v1.18.0 verzióját követi.

Mielőtt belekezdesz, beszélj a [helyi csoportoddal](/community/). Ők tudják, hol hiányzik a lefedettség, melyik [presetet használja a környéked](/guides/settings/), és hogyan nevezik el az átjátszókat. Nézd meg a [lefedettségi térképeket](/map/) a közeledben lévő átjátszókért, és köszönj be a nyilvános vagy helyi [csatornákon](/guides/channels/).

## Válassz helyszínt {#site}

A magasság többet ér, mint a teljesítmény. A LoRa 868 MHz-en tiszta rálátás mentén terjed a legjobban. A dombok, épületek és sűrű fák sokkal több hatótávot vesznek el, mint amennyit néhány extra milliwatt visszahoz.

- **Menj magasra.** Egy háztető, egy árboc, egy magas épület vagy egy domb sokkal többet fed le, mint egy ablakpárkány. Már néhány méter a környező tetők fölött is segít.
- **Tartsd szabadon az antennát.** Szereld a tetőszélek fölé, távol fémtől, ereszcsatornáktól és más antennáktól.
- **Ellenőrizd a kilátást.** Az olyan eszközök, mint a [HeyWhatsThat](https://www.heywhatsthat.com/), megmutatják, mi látható egy adott helyről. Ha látsz egy pontot, egy ottani átjátszó elérhető.
- **Hagyj szabad teret.** A rádiós útvonalnak szabad hely kell a közvetlen vonal körül, nem csak maga a vonal. Nagy távolságon az útvonal közepe több méterrel haladjon el az akadályok fölött.
- **Kérj engedélyt.** Szerezd meg a tulajdonos hozzájárulását a tetőhöz vagy árbochoz, és egyezzetek meg, hogyan éred el az átjátszót karbantartáshoz.

## Hardver {#hardware}

- **Panel.** Válassz egy alacsony fogyasztású nRF52 panelt, például a [Heltec T114](/devices/), a RAK WisBlock vagy a SenseCAP Solar Node eszközt. Az ESP32 panelek többet fogyasztanak (az eszközök oldala Magas jelzéssel látja el őket), ami megnehezíti a napelemes működést.
- **Antenna.** Használj 868 MHz-re készült antennát, függőlegesen felszerelve; az [antenna útmutató](/guides/antenna/) bemutatja a típusokat, csatlakozókat, kábelt és rögzítést. Az antenna nyeresége beleszámít a törvényes teljesítménykorlátba; lásd [Jogi korlátok](#legal).
- **Kábel.** Tartsd rövidre a koaxiális kábelt, vagy használj alacsony veszteségű kábelt. 868 MHz-en néhány méter vékony kábel a teljesítményed felét elnyelheti.
- **Doboz.** Időjárásálló doboz (IP65 vagy jobb) kábeltömszelencével, szellőző- vagy lefolyónyílással a páralecsapódás ellen, és világos színnel vagy napárnyékolóval. Az akkumulátorok szenvednek a hőségben, és fagypont alatt nem tölthetők.
- **Villámlás.** Egy tetőn lévő antenna célpont. Kövesd a helyi földelési szabályokat, vagy szereld oda, ahol egy villámcsapás nem érné el az épület vezetékeit.

## Áramellátás és napelem méretezése {#power}

Egy napelemes átjátszónak túl kell élnie a tél legsötétebb heteit. Ezekre méretezd:

1. **Mérd meg a fogyasztást.** Járasd a beállított átjátszót egy napig USB fogyasztásmérőn keresztül. Olvasd le a felhasznált energiát wattórában (Wh). A környéked forgalma befolyásolja az értéket, ezért ha tudod, a helyszínen mérj.
2. **Számolj tartalékkal.** Tervezz legalább 5-7 napra elegendő akkumulátor-kapacitást hasznos napsütés nélkül.
3. **Nézd meg a téli napsütést.** Az EU ingyenes [PVGIS eszköze](https://re.jrc.ec.europa.eu/pvg_tools/en/) bármely helyszínre megmutatja, mennyi energiát termel egy panel havonta. A legkevesebb napsütésű hónappal számolj.
4. **Méretezd a panelt.** A panelnek a legrosszabb hónapban is pótolnia kell minden nap fogyasztását, a töltési veszteségekre is hagyva helyet.

Egy kidolgozott példa, feltételezett számokkal: egy napi 1 Wh-t fogyasztó átjátszónak legalább 7 Wh-s akkumulátor kell egy hét tartalékhoz, ez nagyjából 2 Ah hasznos kapacitás 3.7 V-on. Ha a PVGIS szerint egy 1 W-os panel a helyszíneden decemberben napi 0.5 Wh-t ad, legalább 2 W-os panel kell, a 3-5 W pedig tartalékot hagy felhőkre, hóra és öregedésre.

## Állítsd be {#config}

**Flashelés.** Használd a [webes flashert](https://flasher.meshcore.io), és válaszd a panelodhoz a **Repeater** firmware-t. A flashelés lépéseit a [Kezdő lépések](/get-started/#flash) oldalon találod.

**Beállítás USB-n.** Amíg az átjátszó a számítógépedhez csatlakozik, nyisd meg a [config.meshcore.io](https://config.meshcore.io) oldalt vagy a flasher konzolját. Bármilyen soros terminált is használhatsz 115200 baud sebességgel. A legfontosabb parancsok:

| Mit | Parancs |
|---|---|
| Admin jelszó módosítása | `password <new password>` |
| Névadás | `set name <name>` |
| Rádió preset: frekvencia, sávszélesség, SF, CR (érvényesítéshez újraindítás kell) | `set radio 869.618,62.5,8,8` |
| Duty cycle korlát, százalékban | `set dutycycle 10` |
| A rádiócsip adóteljesítménye, dBm-ben | `set tx <dBm>` |
| Pozíció, hogy megjelenjen a térképeken | `set lat <degrees>` és `set lon <degrees>` |
| Elérhetőség más üzemeltetők számára | `set owner.info <text>` |
| Órák száma a flood advertek között, amelyeket az egész mesh hall | `set flood.advert.interval <hours>` |
| Bejelentés most | `advert` |
| Újraindítás | `reboot` |

Az alapértelmezett admin jelszó a `password`, és aki ezzel bejelentkezik, admin lesz. Változtasd meg, mielőtt az átjátszó adásba kerül.

A fenti `set radio` példa az EU/UK (Narrow) preset. Helyette a környéked presetjének értékeit használd: az [Ajánlott beállítások](/guides/settings/) országonként felsorolja őket.

**Állítsd be az órát.** Óramodul (RTC) nélkül az átjátszó minden áramszünetnél elveszti az időt, és 2024 májusában indul újra, működés közben pedig az órája elcsúszik. Jelentkezz be távolról az appból, és használd a `clock sync` parancsot, vagy állítsd be az időt USB-n. Egy RTC modul hasznos kiegészítő egy átjátszóhoz: megtartja az időt áramszünet alatt, és sokkal kevésbé csúszik el.

**Kezeld távolról.** Amint a mesh-en van, jelentkezz be a MeshCore appból az admin jelszóval. Ott olvasod le az állapotát, és ugyanezeket a parancsokat használod rádión keresztül. Néhány parancs csak USB-n működik, például a `set freq` és a gyári visszaállítás, az `erase`.

A teljes parancslista a [MeshCore CLI referenciában](https://github.com/meshcore-dev/MeshCore/blob/main/docs/cli_commands.md) található.

## Jogi korlátok {#legal}

{{< callout type="legal" verified="2026-10-02" >}}
A MeshCore európai presetjei a **869.40-869.65 MHz** alsávban helyezkednek el. Az EU-ban, az Egyesült Királyságban, Svájcban és Norvégiában ez engedély nélkül nyitva áll a rövid hatótávú eszközök előtt, ezekkel a korlátokkal:

- legfeljebb **500 mW e.r.p.** kisugárzott teljesítmény;
- legfeljebb **10% duty cycle**: eszközönként legfeljebb 360 másodperc adás bármely órában. Alternatívaként egy eszköz használhat adás előtti figyelést adaptív frekvenciaválasztással, ahogy az ETSI EN 300 220-2 meghatározza;
- a teljes jelnek, amely legfeljebb 250 kHz széles lehet, az alsávon belül kell maradnia.

A sáv megosztott: nem zavarhatod az engedélyköteles szolgáltatásokat, és mások zavarhatnak téged.
A rádiónak CE jelöléssel kell rendelkeznie (Nagy-Britanniában CE vagy UKCA).
{{< /callout >}}

Források: [CEPT ERC 70-03 ajánlás](https://docdb.cept.org/document/845),
1. melléklet, h1.7 sáv;
[2006/771/EK bizottsági határozat](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02006D0771(01)-20250123)
és módosításai;
[ETSI EN 300 220-2](https://www.etsi.org/deliver/etsi_en/300200_300299/30022002/03.03.01_60/en_30022002v030301p.pdf),
O sáv.

### Teljesítmény: e.r.p. és az antennád {#erp}

A korlát a *kisugárzott* teljesítményre vonatkozik, egy egyszerű dipólantennához mérve (e.r.p.). Az antenna nyeresége beleszámít; a kábelveszteség levonódik. A gyártók az antenna nyereségét dBi-ben adják meg, ami 2.15 dB-lel több, mint ugyanaz a nyereség dBd-ben (dipólhoz viszonyítva). Tartsd ezt az összeget 27 dBm-en (500 mW) vagy alatta:

> adóteljesítmény (dBm) + antenna nyeresége (dBi) − kábelveszteség (dB) − 2.15 ≤ 27

- Egy panel, amely 22 dBm-mel ad egy 5 dBi antennába 1 dB veszteségű kábelen át: 22 + 5 − 1 − 2.15 = 23.85 dBm, körülbelül 240 mW e.r.p. A korláton belül van.
- Egy panel 30 dBm (1 W) erősítővel egy 3 dBi antennába: 30 + 3 − 2.15 = 30.85 dBm, körülbelül 1.2 W e.r.p. A korlát felett van; csökkentsd az adóteljesítményt.

A `set tx` a LoRa csip kimenetét állítja be dBm-ben. Maga az SX1262 csip 22 dBm-nél tetőzik; a firmware nem ellenőrzi a beírt számot. A külön erősítővel szerelt panelek, mint a Heltec V4 vagy a Station G2, sokkal többet adnak, mint a beállított szám. Nézd meg a gyártó táblázatát, mielőtt beállítod, és kezdd alacsonyan.

### Duty cycle {#duty-cycle}

Az átjátszó mindenki helyett ad a környéken, így gyorsabban használja el az adásidejét, mint egy companion eszköz. A MeshCore duty cycle korlátozója alapértelmezés szerint 50%, ami több, mint amennyit ez a sáv megenged. Állítsd 10%-ra minden átjátszón:

```text
set dutycycle 10
```

### Frekvenciapontosság {#frequency}

Az EU/UK (Narrow) csatorna, 869.618 MHz 62.5 kHz sávszélességgel, 869.649 MHz-ig ér fel: kevesebb mint 1 kHz-cel az alsáv teteje alatt. A jelnek minden hőmérsékleten a sávon belül kell maradnia. Ehhez hőmérséklet-kompenzált kristály (TCXO) kell. Szinte minden jelenlegi panelben van ilyen; a régebbi panelek nélküle, például a Heltec V2, túl messzire csúsznak el, hogy 62.5 kHz-en megbízhatóan működjenek.

### Országonkénti megjegyzések {#countries}

- **Az EU-tagállamoknak** ezekkel a feltételekkel kell elérhetővé tenniük ezt az alsávot
  (2006/771/EK határozat, 3. cikk).
- **Egyesült Királyság:** ugyanezek a korlátok, az Ofcom
  [IR 2030](https://www.ofcom.org.uk/spectrum/radio-equipment/short-range-devices) dokumentumában.
- **Svájc és Liechtenstein:** ugyanezek a korlátok, az OFCOM
  [RIR1008-09](https://www.ofcomnet.ch/api/rir/1008/09) dokumentumában.
- **Norvégia:** ugyanezek a korlátok, az
  [általános engedélyekről szóló rendeletben](https://lovdata.no/dokument/SF/forskrift/2012-01-19-77)
  (fribruksforskriften).

Ezek a megjegyzések nem jogi tanácsok. A szabályok változnak; ha kétséged van, kérdezd meg
a nemzeti szabályozó hatóságodat.

## Telepítési ellenőrzőlista {#checklist}

- [ ] A helyszín tulajdonosa beleegyezett, és karbantartáshoz eléred az átjátszót.
- [ ] A panelen a **Repeater** firmware fut, és az antennát az első bekapcsolás
      előtt csatlakoztattad.
- [ ] Az admin jelszó meg van változtatva.
- [ ] A rádió megfelel [a környéked presetjének](/guides/settings/) (`get radio`).
- [ ] A `set dutycycle 10` be van állítva.
- [ ] Az adóteljesítmény plusz az antenna nyeresége 500 mW e.r.p. alatt marad.
- [ ] A név, a pozíció és az `owner.info` be van állítva, hogy mások tudják, ki üzemelteti.
- [ ] Az óra be van állítva (`clock`).
- [ ] A doboz le van zárva, van lefolyó- vagy szellőzőnyílása, és a kábelen van
      csepegtetőhurok.
- [ ] Az akkumulátor és a panel a legrosszabb téli hónapra van méretezve.
- [ ] Távolról kipróbáltad az appból, mielőtt elhagytad a helyszínt.
- [ ] A helyi csoportod tudja, hogy üzemel.
