---
title: Kartotuvo vadovas
lead: Aukštai pastatytas kartotuvas perduoda žinutes visiems aplinkui, visame mieste ar slėnyje. Pasirink vietą, maitink jį saulės energija, sukonfigūruok ir laikykis įstatymų.
description: 'Kaip Europoje suplanuoti, maitinti, sukonfigūruoti ir teisėtai naudoti MeshCore kartotuvą: vietos parinkimas, saulės sistemos dydis, CLI nustatymai, 868 MHz galios ir darbo ciklo ribos.'
eyebrow: 868 MHz · iki 500 mW · be licencijos
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'd42ee2ac'
  seeded: '2026-11-21'
  fields: {title: '4608abcd', lead: 'bc670c65', description: '9e483ce5', eyebrow: '9fd33416'}
  sections: ['05ee477a', '938c518c', '824ab38e', '662ea23c', '70faf508', 'b9991666', '69d7162f', 'bf712994', '92beca03', '17634750', 'cadf6024', 'e9cc6834', '2e6e59ca', 'cc266810']
  blocks: ['20ac0371', 'ed2b1adf', '432543ee', '7af42c89', 'd0f7543a', '9ef3580f', '3476aef7', '1bab7bec', 'bbea9a0c', '2b9fab3b', 'b13d1947', 'c2bad16f', '636edc86', 'c2d6bcd1', '957ae975', '98874949', '96d1ebad', 'dbd9fa1f', 'aa06d32b', '9958aad3', '73642ab6', 'cca1bbdf', '64ef011d', 'e7f16724', 'd2e34ff0', 'bb195cfc', '90338c64', '2b1d995b', '992bed82', '62eb1543', '210f1b66', 'e817b1f7', '63f961dc', 'bdc66db0', 'b59f248c', '7184bd63', 'de5a24f9', 'f5cfb426', '48c7422f', '9d3c0836', '50af0550', 'dd7c556b', '240126df', '8aac2b33', '81a475b8', 'a53e42b5', '36ff1db4', 'e4ca8602', 'e4594afd', '3b24b8e9', '58330858', '68f2966e', 'd7418228', '23536e60', 'cbc5c2d1', '2ea02ba9', '92540256', '6e21f681', 'a8c12311', '3382ae7f', 'cdeafb0f', '7cf2bc81']
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

- **Statyk aukštai.** Stogas, stiebas, aukštas pastatas ar kalva aprėpia kur kas daugiau nei palangė. Padeda net keli metrai virš aplinkinių stogų.
- **Antenai palik laisvą erdvę.** Tvirtink ją aukščiau stogo kraštų, atokiau nuo metalo, latakų ir kitų antenų.
- **Patikrink matomumą.** Tokie įrankiai kaip [HeyWhatsThat](https://www.heywhatsthat.com/) parodo, kas matyti iš tam tikros vietos. MeshCore programėlė [apskaičiuoja, ką pasiektų ten pastatytas retransliatorius](#check-site).
- **Palik laisvą tarpą.** Radijo ryšiui reikia laisvos erdvės aplink tiesioginę liniją, ne tik pačios linijos. Esant 868 MHz dažniui, ta erdvė siekia apie 20 m aplink 5 km ryšio linijos vidurį. Kai atstumas 20 km, ji siekia apie 40 m.
- **Paprašyk leidimo.** Gauk stogo ar stiebo savininko sutikimą ir susitark, kaip pateksi prie retransliatoriaus jį prižiūrėti.

### Patikrink vietą programėlėje {#check-site}

MeshCore programėlės 1.33 ir naujesnės versijos meniu šiuos įrankius rasi skiltyje **Tools**. Jie veikia ir be prijungto radijo.

- **Line of Sight** nubraižo žemės paviršių tarp 2 taškų ir erdvę, kurios signalui reikia virš jo. Ilgai paspausk 2 taškus žemėlapyje arba bakstelėk retransliatorius.
- **Antenna Coverage** žemėlapyje parodo, ką pasiektų antena 1 taške. Ilgai paspausk tašką arba bakstelėk retransliatorių. Pridėk daugiau taškų, kad palygintum vietas.

Kompiuteryje įrankio meniu pasirink **Add Point** ir įvesk koordinates.

Abu įrankiai iš pradžių nustato, kad antena tavo vietoje yra 5 m aukštyje, todėl įrankio nustatymuose nurodyk planuojamą aukštį. Antenna Coverage iš pradžių naudoja priimančiąją anteną 1 m aukštyje. Jei radijas neprijungtas, Line of Sight iš pradžių naudoja 915 MHz dažnį: jo nustatymuose nurodyk savo [profilio](/guides/settings/) dažnį.

Įrankiai skaičiuoja pagal aukščio duomenis ir tavo radijo netikrina. Medžius ir
naujus pastatus patikrink pats, tada nusinešk kompanioną į tą vietą ir pažiūrėk,
kuriuos retransliatorius jis girdi.

![Line of Sight MeshCore programėlėje: žemės paviršius tarp 2 taškų ir erdvė, kurios signalui reikia virš jo](/media/guides/line-of-sight.webp)

![Antenna Coverage MeshCore programėlėje: žemėlapyje pažymėta sritis, kurią gali pasiekti antena ant kalvos](/media/guides/antenna-coverage.webp)

## Įranga {#hardware}

- **Plokštė.** Pasirink mažai energijos naudojančią nRF52 plokštę, pavyzdžiui, [Heltec T114](/devices/), RAK WisBlock arba SenseCAP Solar Node. ESP32 plokštės naudoja daugiau energijos (įrenginių puslapyje jos pažymėtos High), todėl jas sunku maitinti saulės energija.
- **Antena.** Naudok 868 MHz dažniui skirtą anteną ir tvirtink ją vertikaliai. [Antenų vadove](/guides/antenna/) rasi tipus, jungtis, kabelius ir tvirtinimą. Antenos stiprinimas įskaičiuojamas į leistiną galios ribą, žr. [Teisinės ribos](#legal).
- **Kabelis.** Bendraašį kabelį rinkis trumpą arba naudok mažų nuostolių kabelį. Dažniu 868 MHz keli metrai plono kabelio gali atimti pusę galios.
- **Korpusas.** Oro sąlygoms atsparus korpusas (IP65 arba geresnis) su kabelio riebokšliu ir vėdinimo ar drenažo anga nuo kondensato, šviesios spalvos arba su apsauga nuo saulės. Karštis kenkia akumuliatoriams, o esant minusinei temperatūrai jų įkrauti negalima.
- **Žaibas.** Antena ant stogo yra taikinys. Laikykis vietinių įžeminimo taisyklių arba tvirtink ją ten, kur žaibo smūgis nepasiektų pastato elektros instaliacijos.

## Maitinimas ir saulės sistemos dydis {#power}

Saulės energija maitinamas retransliatorius turi atlaikyti tamsiausias žiemos savaites. Pirmiausia
įjunk energijos taupymą: po `powersaving on` retransliatorius tarp paketų miega. Tai
veikia nRF52 plokštėse ir ESP32 plokštėse, kurių programinėje įrangoje nėra tilto. Tada
apskaičiuok akumuliatoriaus ir saulės skydelio dydį:

1. **Išmatuok apkrovą.** Vieną dieną leisk sukonfigūruotam kartotuvui veikti per USB galios matuoklį. Nuskaityk sunaudotą energiją vatvalandėmis (Wh). Skaičius priklauso nuo srauto tavo vietovėje, todėl, jei gali, matuok vietoje.
2. **Pridėk rezervą.** Akumuliatoriaus talpą planuok bent 5–7 dienoms be naudingos saulės.
3. **Sužinok, kiek saulės būna žiemą.** Nemokamas ES įrankis [PVGIS](https://re.jrc.ec.europa.eu/pvg_tools/en/) parodo, kiek energijos per mėnesį saulės modulis pagamina bet kurioje vietoje. Rinkis mėnesį, kai saulės mažiausiai.
4. **Parink modulio dydį.** Tą blogiausią mėnesį modulis turi grąžinti visą per dieną sunaudotą energiją, su atsarga įkrovimo nuostoliams.

Pavyzdys su pasirinktais skaičiais: kartotuvui, kuris naudoja 1 Wh per dieną, savaitės rezervui reikia bent 7 Wh akumuliatoriaus, tai apie 2 Ah naudingos talpos esant 3.7 V. Jei PVGIS rodo, kad 1 W modulis tavo vietoje gruodį duoda 0.5 Wh per dieną, tau reikia bent 2 W modulio. Modulis nuo 3 iki 5 W palieka atsargą debesims, sniegui ir senėjimui.

## Sukonfigūruok {#config}

**Įrašyk programinę įrangą.** Atidaryk [internetinį įrašymo įrankį](https://flasher.meshcore.io) ir pasirink savo plokštei skirtą **Repeater** programinę įrangą. Įrašymo žingsnius rasi puslapyje [Pradžia](/get-started/#flash).

**Konfigūruok per USB.** Kol kartotuvas dar prijungtas prie kompiuterio, atidaryk [config.meshcore.io](https://config.meshcore.io) arba įrašymo įrankio konsolę. Taip pat gali naudoti bet kurį nuoseklųjį terminalą 115200 bodų greičiu. Svarbiausios komandos:

| Kas | Komanda |
|---|---|
| Pakeisk administratoriaus slaptažodį | `password <new password>` |
| Slaptažodis svečiams, kurie gali matyti jo būseną | `set guest.password <password>` |
| Suteik jam pavadinimą | `set name <name>` |
| Radijo profilis: dažnis, pralaidumas, SF, CR (įsigalioja paleidus iš naujo) | `set radio 869.618,62.5,8,8` |
| Darbo ciklo riba procentais | `set dutycycle 10` |
| Radijo lusto siuntimo galia, dBm | `set tx <dBm>` |
| Padėtis, kad jis būtų rodomas žemėlapiuose | `set lat <degrees>` ir `set lon <degrees>` |
| Kontaktiniai duomenys kitiems operatoriams | `set owner.info <text>` |
| Laikas valandomis tarp flood skelbimų, kuriuos girdi visas mesh tinklas | `set flood.advert.interval <hours>` |
| Paskelbk jį dabar | `advert` |
| Paleisk iš naujo | `reboot` |

Numatytasis administratoriaus slaptažodis yra `password`, ir kiekvienas, kuris juo prisijungia, tampa administratoriumi. Pakeisk jį, kol kartotuvas dar neišėjo į eterį.

Iš pradžių svečio slaptažodis tuščias. Tada bet kas gali prisijungti kaip svečias be slaptažodžio ir matyti retransliatoriaus būseną bei jo kaimynus. Kiekviena užklausa yra srautas mesh tinkle. Nustatyk svečio slaptažodį ir duok jį tiems, kam jo reikia.

**Pasirink pavadinimą.** Pavadink jį taip, kaip savo retransliatorius vadina tavo vietinė grupė.
Jei grupės nėra, įrašyk šalį, vietovę ir trumpą pavadinimą, pavyzdžiui,
`DE-63477-MUF1`. Taip kiti operatoriai matys, kur yra retransliatorius. Pavadinime
telpa iki 31 baito, o skelbime, kuriame yra ir padėtis, telpa 23.

Aukščiau pateiktas `set radio` pavyzdys skirtas EU/UK (Narrow). Vietoj šių verčių naudok savo vietovės nustatymų rinkinio vertes: puslapyje [Rekomenduojami nustatymai](/guides/settings/) jos išvardytos pagal šalis.

**Nustatyk laikrodį.** Be laikrodžio modulio (RTC) retransliatorius kaskart dingus
elektrai praranda laiką ir grįžta į 2024 m. gegužę. Kol jis veikia, jo laikrodis
dar ir nukrypsta: vis labiau skuba arba vėluoja. Todėl laikas nuo laiko nustatyk
laikrodį: prisijunk nuotoliniu būdu per programėlę ir įvesk `clock sync` arba
nustatyk laiką per USB. Su RTC moduliu to reikia retai: jis išlaiko laiką dingus
elektrai ir nukrypsta kur kas mažiau. Programinė įranga pati aptinka DS3231,
RV3028, PCF8563 arba RX8130 modulį.

**Plokštė su GPS** abu dalykus nustato už tave. Po `gps on` retransliatorius kas 30 minučių
gauna laiką iš GPS, o `gps setloc` įrašo savo padėtį į `lat` ir `lon`.
Kol GPS įjungtas, jis visą laiką naudoja energiją. Jei retransliatorius maitinamas
saulės energija, vietoje vieną kartą paleisk `gps setloc` ir išjunk GPS komanda
`gps off`. Tada laikrodžiui vėl reikės `clock sync`.

**Valdyk nuotoliu.** Kai kartotuvas jau tinkle, prisijunk prie jo iš MeshCore programėlės administratoriaus slaptažodžiu. Ten matysi jo būseną ir tas pačias komandas galėsi naudoti per radijo ryšį. Kai kurios komandos veikia tik per USB, pavyzdžiui, `set freq` ir gamyklinių nustatymų atkūrimo komanda `erase`.

**Išsaugok jo tapatybę.** Prieš ištrindamas per USB įvesk `get prv.key` ir parodytą privatųjį raktą laikyk saugioje vietoje. Po ištrynimo komandomis `set prv.key <key>` ir `reboot` grąžinsi kartotuvui senąją tapatybę, todėl jį žinantys mazgai ras jį pagal tą patį prefiksą.

Visą komandų sąrašą rasi [MeshCore CLI žinyne](https://github.com/meshcore-dev/MeshCore/blob/main/docs/cli_commands.md).

## Atnaujink belaidžiu ryšiu {#update}

Kai kartotuvas jau iškeltas aukštai, atnaujini jį nuo žemės. Prisijunk iš MeshCore programėlės administratoriaus slaptažodžiu, atidaryk komandų eilutę ir įvesk `start ota`. Kas vyks toliau, priklauso nuo plokštės. Kitos plokštės atsako `Error`, ir jas atnaujini per USB.

**nRF52 plokštės**, pavyzdžiui, RAK, Heltec T114, Seeed XIAO ir SenseCAP Solar:

1. Iš [internetinio įrašymo įrankio](https://flasher.meshcore.io) atsisiųsk savo plokštei skirtą naujos programinės įrangos **ZIP** failą.
2. Įvesk `start ota`. Kartotuvas atsako `OK` ir per Bluetooth pasirodo kaip `<board>_OTA`, pavyzdžiui, `RAK4631_OTA`.
3. Telefone atidaryk programėlę nRF Device Firmware Update, pasirink ZIP failą bei kartotuvą ir įkelk. Tai užtrunka kelias minutes.

Prieš iškeldamas nRF52 plokštę aukštai, įdiek jai [OTAFIX paleidyklę](https://github.com/oltaco/Adafruit_nRF52_Bootloader_OTAFIX).
Su standartine paleidykle nepavykusį atnaujinimą pataisysi tik per USB.
Su OTAFIX plokštė grįžta į atnaujinimo režimą, ir tu bandai dar kartą per Bluetooth.
`get bootloader.ver` parodo, kokia paleidyklė yra plokštėje: jei įdiegta OTAFIX, atsakyme yra `OTAFIX`.

Po atnaujinimo `ver` parodo dabar veikiančios programinės įrangos versiją.

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

Prieš iškeldamas retransliatorių aukštai, peržiūrėk
[retransliatoriaus kontrolinį sąrašą](/guides/repeater-checklist/). Jame nurodytas
kiekvienas dalykas, kurį reikia patikrinti, ir komanda, kuri jį parodo.
