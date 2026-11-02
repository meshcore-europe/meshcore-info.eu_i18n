---
title: Kartotuvo vadovas
lead: Aukštai pastatytas kartotuvas perduoda žinutes visiems aplinkui, visame mieste ar slėnyje. Pasirink vietą, maitink jį saulės energija, sukonfigūruok ir laikykis įstatymų.
description: 'Kaip Europoje suplanuoti, maitinti, sukonfigūruoti ir teisėtai naudoti MeshCore kartotuvą: vietos parinkimas, saulės sistemos dydis, CLI nustatymai, 868 MHz galios ir darbo ciklo ribos.'
eyebrow: 868 MHz · iki 500 mW · be licencijos
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '7c7e3be3'
  seeded: '2026-11-02'
  fields: {title: '4608abcd', lead: 'bc670c65', description: '9e483ce5', eyebrow: '9fd33416'}
  sections: ['05ee477a', '938c518c', '766086be', '70faf508', '8bc641aa', '399cd683', 'e9dedb7b', '92beca03', '17634750', 'cadf6024', 'e9cc6834', '2e6e59ca', 'fb44b8db']
  blocks: ['20ac0371', 'ed2b1adf', '432543ee', '7af42c89', 'd0f7543a', '9ef3580f', '3476aef7', '1bab7bec', '6a7c4493', 'dbd9fa1f', 'aa06d32b', '9958aad3', 'd162b028', 'cca1bbdf', '64ef011d', 'e7f16724', 'd2e34ff0', 'bb195cfc', '8d080bb3', '2b1d995b', '210f1b66', 'dc7419d2', 'bdc66db0', 'b59f248c', '7184bd63', 'de5a24f9', 'f5cfb426', '48c7422f', '9d3c0836', 'da8a6af3', '240126df', '8aac2b33', '81a475b8', 'a53e42b5', '36ff1db4', 'e4ca8602', 'e4594afd', '3b24b8e9', '58330858', '68f2966e', 'd7418228', '23536e60', 'cbc5c2d1', '2ea02ba9', '92540256', '6e21f681', 'a8c12311', '3382ae7f', 'cdeafb0f', '1b1319d2']
---

Kartotuvai neša tinklą. Kompanionai (radijo įrenginiai, iš kurių rašai žinutes) žinučių toliau neperduoda, todėl be kartotuvų pasieksi tik tuos žmones, kurie yra tiesioginiame ryšio nuotolyje. Tinkamoje vietoje pastatytas kartotuvas išplečia tinklą visiems aplinkui. Šis vadovas parengtas pagal MeshCore programinę įrangą v1.18.0.

Prieš pradėdamas pasikalbėk su savo [vietine grupe](/community/). Jos nariai žino, kur trūksta aprėpties, [kokį nustatymų rinkinį naudoja tavo vietovė](/guides/settings/) ir kaip vadinti kartotuvus. [Aprėpties žemėlapiuose](/map/) patikrink, ar netoli tavęs yra kartotuvų, ir pasisveikink viešuose arba vietiniuose [kanaluose](/guides/channels/).

## Ar tau jo reikia? {#need}

Kartotuvas persiunčia kiekvieną išgirstą flood žinutę, o visi nuotolyje esantys kartotuvai dalijasi tuo pačiu eterio laiku. Jei tinklas tave jau pasiekia, dar vienas kartotuvas padidina srautą, bet ne aprėptį. Gali užtekti aukštai padėto kompaniono: palėpės lange arba balkone.

Kartotuvą statyk ten, kur trūksta aprėpties:

- [aprėpties žemėlapiuose](/map/) netoli tavęs nėra kartotuvo arba yra tik tokie, kurių tavo kompanionas negirdi;
- vietinė grupė sako, kad vietovei jo reikia.

## Pasirink vietą {#site}

Aukštis svarbesnis už galią. LoRa signalas 868 MHz dažniu geriausiai sklinda atvira tiesioginio matomumo linija. Kalvos, pastatai ir tankūs medžiai atima kur kas daugiau nuotolio, nei susigrąžintum keliais papildomais milivatais.

- **Rinkis aukštą vietą.** Stogas, stiebas, aukštas pastatas ar kalva aprėpia kur kas daugiau nei palangė. Padeda net keli metrai virš aplinkinių stogų.
- **Palik anteną atviroje vietoje.** Tvirtink ją aukščiau stogo kraštų, atokiau nuo metalo, latakų ir kitų antenų.
- **Patikrink matomumą.** Tokiais įrankiais kaip [HeyWhatsThat](https://www.heywhatsthat.com/) pamatysi, kas matoma iš pasirinktos vietos. Jei vietą matai, ten esantį kartotuvą pasieksi.
- **Palik laisvos erdvės.** Radijo keliui reikia šiek tiek laisvos erdvės aplink tiesioginę liniją, ne tik pačios linijos. Dideliais atstumais kelio vidurys turėtų būti keliais metrais aukščiau už kliūtis.
- **Paprašyk leidimo.** Gauk stogo ar stiebo savininko sutikimą ir susitark, kaip pateksi prie kartotuvo priežiūros darbams.

## Įranga {#hardware}

- **Plokštė.** Pasirink mažai energijos naudojančią nRF52 plokštę, pavyzdžiui, [Heltec T114](/devices/), RAK WisBlock arba SenseCAP Solar Node. ESP32 plokštės naudoja daugiau energijos (įrenginių puslapyje jos pažymėtos High), todėl jas sunku maitinti saulės energija.
- **Antena.** Naudok 868 MHz dažniui skirtą anteną ir tvirtink ją vertikaliai. [Antenų vadove](/guides/antenna/) rasi tipus, jungtis, kabelius ir tvirtinimą. Antenos stiprinimas įskaičiuojamas į leistiną galios ribą, žr. [Teisinės ribos](#legal).
- **Kabelis.** Bendraašį kabelį rinkis trumpą arba naudok mažų nuostolių kabelį. Dažniu 868 MHz keli metrai plono kabelio gali atimti pusę galios.
- **Korpusas.** Oro sąlygoms atsparus korpusas (IP65 arba geresnis) su kabelio riebokšliu ir vėdinimo ar drenažo anga nuo kondensato, šviesios spalvos arba su apsauga nuo saulės. Karštis kenkia akumuliatoriams, o esant minusinei temperatūrai jų įkrauti negalima.
- **Žaibas.** Antena ant stogo yra taikinys. Laikykis vietinių įžeminimo taisyklių arba tvirtink ją ten, kur žaibo smūgis nepasiektų pastato elektros instaliacijos.

## Maitinimas ir saulės sistemos dydis {#power}

Saulės energija maitinamas kartotuvas turi atlaikyti tamsiausias žiemos savaites. Sistemą skaičiuok pagal jas:

1. **Išmatuok apkrovą.** Vieną dieną leisk sukonfigūruotam kartotuvui veikti per USB galios matuoklį. Nuskaityk sunaudotą energiją vatvalandėmis (Wh). Skaičius priklauso nuo srauto tavo vietovėje, todėl, jei gali, matuok vietoje.
2. **Pridėk rezervą.** Akumuliatoriaus talpą planuok bent 5–7 dienoms be naudingos saulės.
3. **Sužinok, kiek saulės būna žiemą.** Nemokamas ES įrankis [PVGIS](https://re.jrc.ec.europa.eu/pvg_tools/en/) parodo, kiek energijos per mėnesį saulės modulis pagamina bet kurioje vietoje. Rinkis mėnesį, kai saulės mažiausiai.
4. **Parink modulio dydį.** Tą blogiausią mėnesį modulis turi grąžinti visą per dieną sunaudotą energiją, su atsarga įkrovimo nuostoliams.

Pavyzdys su pasirinktais skaičiais: kartotuvui, kuris naudoja 1 Wh per dieną, savaitės rezervui reikia bent 7 Wh akumuliatoriaus, tai apie 2 Ah naudingos talpos esant 3.7 V. Jei PVGIS rodo, kad 1 W modulis tavo vietoje gruodį duoda 0.5 Wh per dieną, tau reikia bent 2 W modulio. Modulis nuo 3 iki 5 W palieka atsargą debesims, sniegui ir senėjimui.

## Sukonfigūruok {#config}

**Įrašyk programinę įrangą.** Atidaryk [internetinį įrašymo įrankį](https://flasher.meshcore.io) ir pasirink savo plokštei skirtą **Repeater** programinę įrangą. Įrašymo žingsnius rasi puslapyje [Pradžia](/get-started/#flash).

**Konfigūruok per USB.** Kol kartotuvas dar prijungtas prie kompiuterio, atidaryk [config.meshcore.io](https://config.meshcore.io) arba įrašymo įrankio konsolę. Taip pat gali naudoti bet kurį nuoseklųjį terminalą 115200 bodų greičiu. Svarbiausios komandos:

| Ką daryti | Komanda |
|---|---|
| Pakeisti administratoriaus slaptažodį | `password <new password>` |
| Suteikti pavadinimą | `set name <name>` |
| Radijo nustatymų rinkinys: dažnis, juostos plotis, SF, CR (įsigalioja po paleidimo iš naujo) | `set radio 869.618,62.5,8,8` |
| Darbo ciklo riba procentais | `set dutycycle 10` |
| Radijo lusto siuntimo galia, dBm | `set tx <dBm>` |
| Padėtis, kad kartotuvas būtų matomas žemėlapiuose | `set lat <degrees>` ir `set lon <degrees>` |
| Kontaktai kitiems operatoriams | `set owner.info <text>` |
| Valandos tarp flood skelbimų, kuriuos girdi visas tinklas | `set flood.advert.interval <hours>` |
| Paskelbti apie kartotuvą dabar | `advert` |
| Paleisti iš naujo | `reboot` |

Numatytasis administratoriaus slaptažodis yra `password`, ir kiekvienas, kuris juo prisijungia, tampa administratoriumi. Pakeisk jį, kol kartotuvas dar neišėjo į eterį.

Aukščiau pateiktas `set radio` pavyzdys skirtas EU/UK (Narrow). Vietoj šių verčių naudok savo vietovės nustatymų rinkinio vertes: puslapyje [Rekomenduojami nustatymai](/guides/settings/) jos išvardytos pagal šalis.

**Nustatyk laikrodį.** Be laikrodžio modulio (RTC) kartotuvas kaskart dingus maitinimui praranda laiką ir vėl pradeda nuo 2024 m. gegužės. Veikimo metu jo laikrodis dar ir nukrypsta: vis labiau skuba arba vėluoja. Todėl retkarčiais nustatyk laikrodį: prisijunk nuotoliu iš programėlės ir naudok `clock sync` arba nustatyk laiką per USB. Su RTC moduliu to reikia retai: jis išsaugo laiką dingus maitinimui ir nukrypsta daug mažiau.

**Valdyk nuotoliu.** Kai kartotuvas jau tinkle, prisijunk prie jo iš MeshCore programėlės administratoriaus slaptažodžiu. Ten matysi jo būseną ir tas pačias komandas galėsi naudoti per radijo ryšį. Kai kurios komandos veikia tik per USB, pavyzdžiui, `set freq` ir gamyklinių nustatymų atkūrimo komanda `erase`.

**Išsaugok jo tapatybę.** Prieš ištrindamas per USB įvesk `get prv.key` ir parodytą privatųjį raktą laikyk saugioje vietoje. Po ištrynimo komandomis `set prv.key <key>` ir `reboot` grąžinsi kartotuvui senąją tapatybę, todėl jį žinantys mazgai ras jį pagal tą patį prefiksą.

Visą komandų sąrašą rasi [MeshCore CLI žinyne](https://github.com/meshcore-dev/MeshCore/blob/main/docs/cli_commands.md).

## Atnaujink belaidžiu ryšiu {#update}

Kai kartotuvas jau iškeltas aukštai, atnaujini jį nuo žemės. Prisijunk iš MeshCore programėlės administratoriaus slaptažodžiu, atidaryk komandų eilutę ir įvesk `start ota`. Kas vyks toliau, priklauso nuo plokštės. Kitos plokštės atsako `Error`, ir jas atnaujini per USB.

**nRF52 plokštės**, pavyzdžiui, RAK, Heltec T114, Seeed XIAO ir SenseCAP Solar:

1. Iš [internetinio įrašymo įrankio](https://flasher.meshcore.io) atsisiųsk savo plokštei skirtą naujos programinės įrangos **ZIP** failą.
2. Įvesk `start ota`. Kartotuvas atsako `OK` ir per Bluetooth pasirodo kaip `<board>_OTA`, pavyzdžiui, `RAK4631_OTA`.
3. Telefone atidaryk programėlę nRF Device Firmware Update, pasirink ZIP failą bei kartotuvą ir įkelk. Tai užtrunka kelias minutes.

Prieš iškeldamas nRF52 plokštę aukštai, įdiek jai [OTAFIX paleidimo programą](https://github.com/oltaco/Adafruit_nRF52_Bootloader_OTAFIX). Su gamykline paleidimo programa nepavykusį atnaujinimą galima ištaisyti tik per USB. Su OTAFIX plokštė grįžta į atnaujinimo režimą, ir bandai dar kartą per Bluetooth.

**ESP32 plokštės**, pavyzdžiui, Heltec V3 ir V4:

1. Iš internetinio įrašymo įrankio atsisiųsk savo plokštei skirtą **non-merged** `.bin` failą: tą, kurio pavadinime nėra žodžio „merged“.
2. Įvesk `start ota`. Kartotuvas sukuria WiFi tinklą `MeshCore-OTA` ir atsako savo įkėlimo puslapio adresu.
3. Būdamas WiFi nuotolyje, prijunk telefoną ar nešiojamąjį kompiuterį prie to tinklo, atidaryk adresą ir įkelk failą.

## Teisinės ribos {#legal}

{{< callout type="legal" verified="2026-10-02" >}}
MeshCore europiniai nustatymų rinkiniai patenka į **869.40-869.65 MHz** pojuostę. ES, Jungtinėje Karalystėje, Šveicarijoje ir Norvegijoje mažo nuotolio įrenginiai ją gali naudoti be licencijos, laikydamiesi šių ribų:

- ne daugiau kaip **500 mW e.r.p.** spinduliuojamosios galios;
- ne daugiau kaip **10% darbo ciklo**: vienas įrenginys per bet kurią valandą gali siųsti ne ilgiau kaip 360 sekundžių. Vietoj to įrenginys gali naudoti klausymąsi prieš siuntimą su adaptyviu dažnio keitimu, kaip apibrėžta ETSI EN 300 220-2;
- visas signalas, ne platesnis kaip 250 kHz, turi likti pojuostės viduje.

Ši juosta yra bendra: negali trikdyti licencijuotų paslaugų, o kiti gali trikdyti tave.
Radijo įrenginys turi būti paženklintas CE ženklu (Didžiojoje Britanijoje CE arba UKCA).
{{< /callout >}}

Šaltiniai: [CEPT ERC rekomendacija 70-03](https://docdb.cept.org/document/845), 1 priedas, juosta h1.7; [Komisijos sprendimas 2006/771/EB](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02006D0771(01)-20250123) ir jo pakeitimai; [ETSI EN 300 220-2](https://www.etsi.org/deliver/etsi_en/300200_300299/30022002/03.03.01_60/en_30022002v030301p.pdf), juosta O.

### Galia: e.r.p. ir tavo antena {#erp}

Riba taikoma *spinduliuojamajai* galiai, matuojamai paprasto dipolio antenos atžvilgiu (e.r.p.). Antenos stiprinimas pridedamas, kabelio nuostoliai atimami. Gamintojai antenos stiprinimą nurodo dBi, o tai yra 2.15 dB daugiau nei tas pats stiprinimas dBd (dipolio atžvilgiu). Žiūrėk, kad ši suma neviršytų 27 dBm (500 mW):

> siuntimo galia (dBm) + antenos stiprinimas (dBi) − kabelio nuostoliai (dB) − 2.15 ≤ 27

- Plokštė siunčia 22 dBm į 5 dBi anteną per kabelį su 1 dB nuostoliu: 22 + 5 − 1 − 2.15 = 23.85 dBm, apie 240 mW e.r.p. Riba neviršyta.
- Plokštė su 30 dBm (1 W) stiprintuvu siunčia į 3 dBi anteną: 30 + 3 − 2.15 = 30.85 dBm, apie 1.2 W e.r.p. Riba viršyta, sumažink siuntimo galią.

Komanda `set tx` nustato LoRa lusto išėjimo galią dBm. Pats SX1262 lustas pasiekia daugiausia 22 dBm, o programinė įranga tavo įvesto skaičiaus netikrina. Plokštės su papildomu stiprintuvu, pavyzdžiui, Heltec V4 ar Station G2, siunčia gerokai daugiau, nei nustatai. Prieš nustatydamas patikrink gamintojo lentelę ir pradėk nuo mažos vertės.

### Darbo ciklas {#duty-cycle}

Kartotuvas siunčia visiems aplinkui, todėl savo eterio laiką išnaudoja greičiau nei kompanionas. MeshCore darbo ciklo ribotuvo numatytoji vertė yra 50%, o tai viršija šioje juostoje leidžiamą ribą. Kiekviename kartotuve nustatyk 10%:

```text
set dutycycle 10
```

### Dažnio tikslumas {#frequency}

EU/UK (Narrow) kanalas, 869.618 MHz su 62.5 kHz juostos pločiu, siekia iki 869.649 MHz: mažiau nei 1 kHz iki pojuostės viršutinės ribos. Signalas turi likti juostoje bet kokioje temperatūroje. Tam reikia temperatūriškai kompensuoto kristalo (TCXO). Jį turi beveik visos dabartinės plokštės. Senesnės plokštės be jo, pavyzdžiui, Heltec V2, nukrypsta per toli, todėl 62.5 kHz juostoje patikimai neveikia.

### Pastabos apie šalis {#countries}

- **ES valstybės narės** privalo suteikti šią pojuostę tokiomis sąlygomis (Sprendimas 2006/771/EB, 3 straipsnis).
- **Jungtinė Karalystė:** tos pačios ribos, Ofcom dokumente [IR 2030](https://www.ofcom.org.uk/spectrum/radio-equipment/short-range-devices).
- **Šveicarija ir Lichtenšteinas:** tos pačios ribos, OFCOM dokumente [RIR1008-09](https://www.ofcomnet.ch/api/rir/1008/09).
- **Norvegija:** tos pačios ribos, [bendrųjų leidimų reglamente](https://lovdata.no/dokument/SF/forskrift/2012-01-19-77) (fribruksforskriften).

Šios pastabos nėra teisinė konsultacija. Taisyklės keičiasi, todėl abejodamas pasitikrink savo šalies reguliavimo institucijoje.

## Įrengimo kontrolinis sąrašas {#checklist}

- [ ] Vietos savininkas sutiko, ir gali patekti prie kartotuvo priežiūros darbams.
- [ ] Plokštėje veikia **Repeater** programinė įranga, o anteną prijungei prieš pirmą įjungimą.
- [ ] Administratoriaus slaptažodis pakeistas.
- [ ] Radijo nustatymai atitinka [tavo vietovės nustatymų rinkinį](/guides/settings/) (`get radio`).
- [ ] Nustatyta `set dutycycle 10`.
- [ ] Siuntimo galia kartu su antenos stiprinimu neviršija 500 mW e.r.p.
- [ ] Nustatyti pavadinimas, padėtis ir `owner.info`, todėl kiti žino, kas jį prižiūri.
- [ ] Laikrodis nustatytas (`clock`).
- [ ] Korpusas sandarus, su drenažo ar vėdinimo anga, o kabelis turi lašėjimo kilpą.
- [ ] Akumuliatoriaus ir saulės modulio dydis parinktas pagal blogiausią žiemos mėnesį.
- [ ] Prieš išvykdamas išbandei jį iš toliau su programėle.
- [ ] Tavo vietinė grupė žino, kad jis veikia.
