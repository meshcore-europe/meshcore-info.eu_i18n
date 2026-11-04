---
title: Vodnik za repetitorje
lead: Visoko postavljen repetitor posreduje sporočila vsem okoli sebe, po celem mestu ali dolini. Izberi lokacijo, zagotovi sončno napajanje, nastavi repetitor in upoštevaj zakonske omejitve.
description: 'Načrtuj, napajaj, nastavi in zakonito upravljaj repetitor MeshCore v Evropi: izbira lokacije, dimenzioniranje sončnega napajanja, nastavitve CLI ter omejitve moči in delovnega cikla pri 868 MHz.'
eyebrow: 868 MHz · do 500 mW · brez licence
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '3e38a8c6'
  seeded: '2026-11-04'
  fields: {title: '4608abcd', lead: 'bc670c65', description: '9e483ce5', eyebrow: '9fd33416'}
  sections: ['05ee477a', '938c518c', '824ab38e', '662ea23c', '70faf508', '8bc641aa', '399cd683', 'e9dedb7b', '92beca03', '17634750', 'cadf6024', 'e9cc6834', '2e6e59ca', 'fb44b8db']
  blocks: ['20ac0371', 'ed2b1adf', '432543ee', '7af42c89', 'd0f7543a', '9ef3580f', '3476aef7', '1bab7bec', 'bbea9a0c', '2b9fab3b', 'b13d1947', 'c2bad16f', '636edc86', 'c2d6bcd1', '957ae975', '98874949', '96d1ebad', 'dbd9fa1f', 'aa06d32b', '9958aad3', 'd162b028', 'cca1bbdf', '64ef011d', 'e7f16724', 'd2e34ff0', 'bb195cfc', '8d080bb3', '2b1d995b', '210f1b66', 'dc7419d2', 'bdc66db0', 'b59f248c', '7184bd63', 'de5a24f9', 'f5cfb426', '48c7422f', '9d3c0836', 'da8a6af3', '240126df', '8aac2b33', '81a475b8', 'a53e42b5', '36ff1db4', 'e4ca8602', 'e4594afd', '3b24b8e9', '58330858', '68f2966e', 'd7418228', '23536e60', 'cbc5c2d1', '2ea02ba9', '92540256', '6e21f681', 'a8c12311', '3382ae7f', 'cdeafb0f', '1b1319d2']
---

Mrežo nosijo repetitorji. Spremljevalne naprave (companion), torej radii, s katerih pošiljaš sporočila, sporočil ne posredujejo. Brez repetitorjev zato dosežeš samo ljudi v neposrednem dosegu. Repetitor na pravem mestu razširi mrežo za vse okoli sebe. Ta vodnik velja za vdelano programsko opremo MeshCore v1.18.0.

Preden začneš, se pogovori s svojo [lokalno skupino](/community/). Člani vedo, kje manjka pokritost, [katero prednastavitev uporabljajo na tvojem območju](/guides/settings/) in kako poimenovati repetitorje. Na [zemljevidih pokritosti](/map/) preveri, kateri repetitorji so blizu tebe, in se oglasi na javnih ali lokalnih [kanalih](/guides/channels/).

## Ali ga potrebuješ? {#need}

Repetitor naprej pošlje vsako poplavno sporočilo (flood), ki ga sliši, vsi repetitorji v dosegu pa si delijo isti oddajni čas. Kjer te mreža že doseže, dodaten repetitor poveča promet, pokritosti pa ne izboljša. Morda zadošča že visoko postavljena spremljevalna naprava, na primer ob strešnem oknu ali na balkonu.

Repetitor postavi tam, kjer manjka pokritost:

- na [zemljevidih pokritosti](/map/) blizu tebe ni nobenega repetitorja ali pa so tam samo takšni, ki jih tvoja spremljevalna naprava ne sliši;
- tvoja lokalna skupina pravi, da območje repetitor potrebuje.

## Izberi lokacijo {#site}

Višina šteje več kot moč. LoRa pri 868 MHz najbolje potuje po neovirani vidni črti. Hribi, stavbe in gosto drevje vzamejo veliko več dosega, kot ga povrne nekaj dodatnih milivatov.

- **Pojdi visoko.** Streha, drog, visoka stavba ali hrib pokrijejo veliko več
  kot okenska polica. Pomaga že nekaj metrov nad okoliškimi strehami.
- **Anteno postavi na prosto.** Namesti jo nad robove streh, stran od kovine,
  žlebov in drugih anten.
- **Preveri razgled.** Orodja, kot je [HeyWhatsThat](https://www.heywhatsthat.com/),
  pokažejo, kaj se vidi z neke lokacije. Aplikacija MeshCore
  [izračuna, kaj tam doseže repetitor](#check-site).
- **Pusti prosti prostor.** Radijska pot potrebuje prostor okoli neposredne črte,
  ne samo črto samo. Pri 868 MHz je ta prostor okoli 20 m na sredini
  5 km dolge poti. Pri 20 km je okoli 40 m.
- **Vprašaj za dovoljenje.** Pridobi lastnikovo soglasje za streho ali drog in
  se dogovori, kako boš prišel do repetitorja za vzdrževanje.

### Preveri lokacijo v aplikaciji {#check-site}

Aplikacija MeshCore ima od različice 1.33 naprej ta orodja v meniju pod
**Tools**. Delujejo tudi brez povezanega radia.

- **Line of Sight** nariše teren med 2 točkama in prostor, ki ga signal
  potrebuje nad njim. Dolgo pritisni na 2 točki na zemljevidu ali tapni repetitorje.
- **Antenna Coverage** na zemljevidu pokaže, kaj doseže antena na 1 točki.
  Dolgo pritisni na točko ali tapni repetitor. Dodaj več točk in primerjaj lokacije.

Na računalniku v meniju orodja izberi **Add Point** in vpiši koordinate.

Obe orodji privzeto postavita anteno na tvoji lokaciji na višino 5 m, zato v nastavitvah orodja vnesi višino, ki jo načrtuješ. Antenna Coverage privzeto računa s sprejemno anteno na višini 1 m. Če radio ni priključen, Line of Sight privzeto uporablja 915 MHz: v njegovih nastavitvah nastavi frekvenco svoje [prednastavitve](/guides/settings/).

Orodja računajo na podlagi podatkov o višini in tvojega radia ne preizkusijo. Drevesa in
nove stavbe preveri sam, nato vzemi companion na to mesto in poglej, katere
repetitorje sliši.

![Line of Sight v aplikaciji MeshCore: teren med 2 točkama in prostor, ki ga signal potrebuje nad njim](/media/guides/line-of-sight.webp)

![Antenna Coverage v aplikaciji MeshCore: na zemljevidu prikazano območje, ki ga doseže antena na hribu](/media/guides/antenna-coverage.webp)

## Strojna oprema {#hardware}

- **Plošča.** Izberi varčno ploščo nRF52, na primer [Heltec T114](/devices/), RAK WisBlock ali SenseCAP Solar Node. Plošče ESP32 porabijo več energije (na strani z napravami imajo oznako High), zato jih je težko napajati s sončno energijo.
- **Antena.** Uporabi anteno za 868 MHz in jo namesti navpično. [Vodnik za antene](/guides/antenna/) opisuje vrste, priključke, kable in montažo. Dobitek antene se šteje v zakonsko omejitev moči; glej [Zakonske omejitve](#legal).
- **Kabel.** Koaksialni kabel naj bo kratek ali pa uporabi kabel z nizkimi izgubami. Pri 868 MHz lahko v nekaj metrih tankega kabla izgubiš polovico moči.
- **Ohišje.** Vremensko odporna omarica (IP65 ali boljša) s kabelsko uvodnico, z odprtino za zračenje ali odtok proti kondenzaciji ter svetle barve ali s senčilom. Baterijam vročina škodi, pod lediščem pa jih ni mogoče polniti.
- **Strela.** Antena na strehi je tarča. Upoštevaj lokalna pravila za ozemljitev ali anteno namesti tako, da udar ne bi dosegel napeljave v stavbi.

## Napajanje in izračun sončne napeljave {#power}

Repetitor na sončno napajanje mora zdržati najtemnejše tedne zime. Napeljavo načrtuj zanje:

1. **Izmeri porabo.** Nastavljeni repetitor za en dan priključi prek merilnika moči USB. Odčitaj porabljeno energijo v vatnih urah (Wh). Promet na tvojem območju to številko spreminja, zato po možnosti meri na lokaciji.
2. **Dodaj rezervo.** Kapaciteto baterije načrtuj za vsaj 5 do 7 dni brez uporabnega sonca.
3. **Ugotovi, koliko sonca imaš pozimi.** Brezplačno orodje EU [PVGIS](https://re.jrc.ec.europa.eu/pvg_tools/en/) za vsako lokacijo pokaže, koliko energije panel proizvede na mesec. Upoštevaj mesec z najmanj sonca.
4. **Določi velikost panela.** Panel mora v tem najslabšem mesecu nadomestiti dnevno porabo in pokriti še izgube pri polnjenju.

Računski primer s predpostavljenimi številkami: repetitor, ki porabi 1 Wh na dan, potrebuje za teden dni rezerve baterijo z vsaj 7 Wh. To je približno 2 Ah uporabne kapacitete pri 3.7 V. Če PVGIS pokaže, da panel z močjo 1 W na tvoji lokaciji decembra da 0.5 Wh na dan, potrebuješ panel z vsaj 2 W. S 3 do 5 W imaš rezervo za oblake, sneg in staranje.

## Nastavitev {#config}

**Naloži vdelano programsko opremo.** Uporabi [spletni flasher](https://flasher.meshcore.io) in za svojo ploščo izberi vdelano programsko opremo **Repeater**. Postopek nalaganja je opisan v razdelku [Prvi koraki](/get-started/#flash).

**Nastavi prek USB.** Dokler je repetitor še povezan z računalnikom, odpri [config.meshcore.io](https://config.meshcore.io) ali konzolo flasherja. Uporabiš lahko tudi katerikoli serijski terminal s hitrostjo 115200 baud. Najpomembnejši ukazi:

| Kaj | Ukaz |
|---|---|
| Spremeni skrbniško geslo | `password <new password>` |
| Poimenuj repetitor | `set name <name>` |
| Radijska prednastavitev: frekvenca, pasovna širina, SF, CR (velja po ponovnem zagonu) | `set radio 869.618,62.5,8,8` |
| Omejitev delovnega cikla v odstotkih | `set dutycycle 10` |
| Oddajna moč radijskega čipa v dBm | `set tx <dBm>` |
| Položaj, da je repetitor viden na zemljevidih | `set lat <degrees>` in `set lon <degrees>` |
| Kontaktni podatki za druge upravljavce | `set owner.info <text>` |
| Število ur med poplavnimi objavami (flood adverts), ki jih sliši vsa mreža | `set flood.advert.interval <hours>` |
| Objavi repetitor takoj | `advert` |
| Ponovni zagon | `reboot` |

Privzeto skrbniško geslo je `password` in kdor se prijavi z njim, postane skrbnik. Spremeni ga, preden repetitor začne oddajati.

Zgornji primer `set radio` velja za EU/UK (Narrow). Namesto njega uporabi vrednosti prednastavitve za svoje območje: [Priporočene nastavitve](/guides/settings/) jih navajajo po državah.

**Nastavi uro.** Brez modula ure (RTC) repetitor ob vsakem izpadu napajanja izgubi čas in znova začne z majem 2024. Med delovanjem njegova ura tudi odstopa: vedno bolj prehiteva ali zaostaja. Zato uro občasno nastavi: prijavi se na daljavo iz aplikacije in uporabi `clock sync` ali pa nastavi čas prek USB. Z modulom RTC je to redko potrebno: čas ohrani tudi ob izpadih napajanja in veliko manj odstopa.

**Upravljaj na daljavo.** Ko je repetitor v mreži, se nanj prijavi iz aplikacije MeshCore s skrbniškim geslom. Tam odčitaš njegovo stanje in iste ukaze uporabljaš prek radia. Nekateri ukazi delujejo samo prek USB, na primer `set freq` in ponastavitev na tovarniške nastavitve `erase`.

**Ohrani identiteto.** Pred brisanjem prek USB vpiši `get prv.key` in prikazani zasebni ključ shrani na varno. Po brisanju vpiši `set prv.key <key>` in `reboot`, pa repetitor dobi staro identiteto nazaj. Vozlišča, ki ga poznajo, ga tako najdejo pod isto predpono.

Celoten seznam ukazov je v [referenci MeshCore CLI](https://github.com/meshcore-dev/MeshCore/blob/main/docs/cli_commands.md).

## Posodobitev po zraku {#update}

Ko je repetitor že visoko, ga posodobiš s tal. Prijavi se iz aplikacije MeshCore s skrbniškim geslom, odpri njegovo ukazno vrstico in vpiši `start ota`. Nadaljevanje je odvisno od plošče: druge plošče odgovorijo `Error`, zato jih posodobi prek USB.

**Plošče nRF52**, na primer RAK, Heltec T114, Seeed XIAO in SenseCAP Solar:

1. S [spletnega flasherja](https://flasher.meshcore.io) prenesi datoteko **ZIP** z novo vdelano programsko opremo za svojo ploščo.
2. Vpiši `start ota`. Repetitor odgovori `OK` in se prek povezave Bluetooth prikaže kot `<board>_OTA`, na primer `RAK4631_OTA`.
3. Na telefonu odpri aplikacijo nRF Device Firmware Update, izberi ZIP in repetitor ter začni nalaganje. Traja nekaj minut.

Na ploščo nRF52 namesti [zagonski nalagalnik OTAFIX](https://github.com/oltaco/Adafruit_nRF52_Bootloader_OTAFIX), preden jo namestiš na višino. S tovarniškim zagonskim nalagalnikom lahko neuspelo posodobitev popraviš samo prek USB. Z OTAFIX se plošča vrne v način posodabljanja, ti pa poskusiš znova prek povezave Bluetooth.

**Plošče ESP32**, na primer Heltec V3 in V4:

1. S spletnega flasherja za svojo ploščo prenesi **nezdruženo** datoteko `.bin`: tisto, ki v imenu nima besede „merged“.
2. Vpiši `start ota`. Repetitor odpre omrežje WiFi z imenom `MeshCore-OTA` in odgovori z naslovom svoje strani za nalaganje.
3. V dosegu omrežja WiFi poveži telefon ali prenosnik s tem omrežjem, odpri naslov in naloži datoteko.

## Zakonske omejitve {#legal}

{{< callout type="legal" verified="2026-10-02" >}}
Evropske prednastavitve MeshCore so v podpasu **869.40-869.65 MHz**. V EU, Združenem kraljestvu, Švici in na Norveškem ga lahko naprave kratkega dosega uporabljajo brez licence, v teh mejah:

- sevana moč največ **500 mW e.r.p.**;
- **delovni cikel največ 10%**: posamezna naprava lahko v eni uri oddaja največ 360 sekund. Namesto tega lahko naprava uporablja poslušanje pred oddajo (listen-before-talk) s prilagodljivo frekvenčno agilnostjo, kot ju določa ETSI EN 300 220-2;
- celoten signal, širok največ 250 kHz, mora ostati znotraj podpasa.

Pas je v skupni rabi: licenciranih storitev ne smeš motiti, drugi pa lahko motijo tebe.
Radio mora imeti oznako CE (v Veliki Britaniji CE ali UKCA).
{{< /callout >}}

Viri: [Priporočilo CEPT ERC 70-03](https://docdb.cept.org/document/845), Priloga 1, pas h1.7; [Sklep Komisije 2006/771/ES](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02006D0771(01)-20250123) in njegove spremembe; [ETSI EN 300 220-2](https://www.etsi.org/deliver/etsi_en/300200_300299/30022002/03.03.01_60/en_30022002v030301p.pdf), pas O.

### Moč: e.r.p. in tvoja antena {#erp}

Omejitev velja za *sevano* moč, merjeno glede na preprosto dipolno anteno (e.r.p.). Dobitek antene se prišteje, izguba v kablu se odšteje. Proizvajalci navajajo dobitek antene v dBi, kar je 2.15 dB več od istega dobitka v dBd (glede na dipol). Ta vsota naj ne preseže 27 dBm (500 mW):

> oddajna moč (dBm) + dobitek antene (dBi) − izguba v kablu (dB) − 2.15 ≤ 27

- Plošča oddaja 22 dBm v anteno s 5 dBi prek kabla z izgubo 1 dB: 22 + 5 − 1 − 2.15 = 23.85 dBm, približno 240 mW e.r.p. To je znotraj omejitve.
- Plošča z ojačevalnikom 30 dBm (1 W) oddaja v anteno s 3 dBi: 30 + 3 − 2.15 = 30.85 dBm, približno 1.2 W e.r.p. To presega omejitev, zato znižaj oddajno moč.

`set tx` nastavi izhodno moč čipa LoRa v dBm. Sam čip SX1262 doseže največ 22 dBm, vdelana programska oprema pa vpisane številke ne preverja. Plošče z dodatnim ojačevalnikom, na primer Heltec V4 ali Station G2, oddajajo veliko več od nastavljene številke. Preden jo nastaviš, preveri proizvajalčevo tabelo in začni z nizko vrednostjo.

### Delovni cikel {#duty-cycle}

Repetitor oddaja za vse okoli sebe, zato svoj oddajni čas porabi hitreje kot spremljevalna naprava. Omejevalnik delovnega cikla v MeshCore je privzeto nastavljen na 50%, kar je več, kot ta pas dovoljuje. Na vsakem repetitorju ga nastavi na 10%:

```text
set dutycycle 10
```

### Natančnost frekvence {#frequency}

Kanal EU/UK (Narrow), 869.618 MHz s pasovno širino 62.5 kHz, sega do 869.649 MHz: manj kot 1 kHz pod zgornjo mejo podpasa. Signal mora ostati znotraj pasu pri vsaki temperaturi. Za to je potreben temperaturno kompenziran kristal (TCXO). Ima ga skoraj vsaka današnja plošča. Starejše plošče brez njega, na primer Heltec V2, preveč odstopajo za zanesljivo delovanje pri 62.5 kHz.

### Opombe po državah {#countries}

- **Države članice EU** morajo ta podpas omogočiti pod temi pogoji (Sklep 2006/771/ES, člen 3).
- **Združeno kraljestvo:** enake omejitve, v dokumentu Ofcom [IR 2030](https://www.ofcom.org.uk/spectrum/radio-equipment/short-range-devices).
- **Švica in Lihtenštajn:** enake omejitve, v dokumentu OFCOM [RIR1008-09](https://www.ofcomnet.ch/api/rir/1008/09).
- **Norveška:** enake omejitve, v [predpisu o splošnih dovoljenjih](https://lovdata.no/dokument/SF/forskrift/2012-01-19-77) (fribruksforskriften).

Te opombe niso pravni nasvet. Pravila se spreminjajo: če nisi prepričan, se posvetuj s svojim nacionalnim regulatorjem.

## Kontrolni seznam za postavitev {#checklist}

- [ ] Lastnik lokacije se strinja, ti pa lahko za vzdrževanje prideš do repetitorja.
- [ ] Na plošči teče vdelana programska oprema **Repeater**, anteno pa si priključil pred prvim vklopom.
- [ ] Skrbniško geslo je spremenjeno.
- [ ] Radio se ujema s [prednastavitvijo za tvoje območje](/guides/settings/) (`get radio`).
- [ ] Nastavljeno je `set dutycycle 10`.
- [ ] Oddajna moč skupaj z dobitkom antene ostaja znotraj 500 mW e.r.p.
- [ ] Ime, položaj in `owner.info` so nastavljeni, da drugi vedo, kdo upravlja repetitor.
- [ ] Ura je nastavljena (`clock`).
- [ ] Ohišje je zatesnjeno in ima odprtino za odtok ali zračenje, kabel pa ima odkapno zanko.
- [ ] Baterija in panel sta dimenzionirana za najslabši zimski mesec.
- [ ] Pred odhodom z lokacije si repetitor z aplikacijo preizkusil z razdalje.
- [ ] Tvoja lokalna skupina ve, da repetitor deluje.
