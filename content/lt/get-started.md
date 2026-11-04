---
title: Kaip pradėti
lead: Nuo naujos plokštės iki pirmos žinutės tinkle. Tau reikės LoRa plokštės, kompiuterio su Chrome arba Edge ir telefono ar nešiojamojo kompiuterio programėlei.
description: Įrašyk MeshCore per naršyklę, susiek programėlę, pasirink savo vietovėje naudojamą radijo profilį, išsiųsk pirmą žinutę ir prisijunk prie vietinio kanalo.
eyebrow: 6 žingsniai · MeshCore v1.18.0
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '0490a311'
  seeded: '2026-11-04'
  fields: {title: '61e8d44a', lead: '45b0e5c3', description: 'cf031b18', eyebrow: '4fa6fe1e'}
  sections: ['16c3728c', '5b6d136a', 'df7a1665', '6da9fd7a', 'cb5fb72e', 'a1cf8b26', '1741ed35', '66d00206']
  blocks: ['16c3728c', '2a70a7ed', '6f8e6f5f', '16c11d47', 'e90b7859', '081db416', 'd5e7fd0b', '6d28c323', 'eb2ea361', 'de50125c', 'ae20cb8e', 'abd42710', 'c08a865a', '7d1eb0b9', '263e0c96', '0903299f', 'eba20370', '5cdc20cf', '7f542f82', '802ca5a8', '1a854187', '53276869', 'f25b16fa', '7c893ae2', '7f5927b4', '26e13713', '39a142cf', 'a786620c', '216897fa', '2d222782', 'a9755900', 'f081b357']
---

Šie žingsniai parašyti pagal MeshCore programinę įrangą v1.18.0 ir 2026 m. spalio mėnesio oficialius įrankius. Skirtingose versijose programėlės meniu pavadinimai gali šiek tiek skirtis.

## 1. Pasirink įrenginį {#device}

Tinka bet kuri [įrenginių puslapyje](/devices/) esanti plokštė, prie kurios nurodytas companion. Pirmam mazgui pasirink *companion*: radiją, iš kurio rašysi žinutes. Susiek jį su telefonu ar nešiojamuoju kompiuteriu per Bluetooth arba USB. Taip pat gali pasirinkti savarankiškai veikiantį įrenginį su savo ekranu ir klaviatūra.

Įsigyk 868 MHz versiją. Komplekte esančios antenos pakanka, o [antenų vadove](/guides/antenna/) rasi, kaip ją patikrinti.

Tavo plokštėje dabar veikia Meshtastic? Įrašęs MeshCore, pakeisi Meshtastic, o šios dvi sistemos tarpusavyje nesusikalba.

{{< callout type="warning" >}}
Prijunk anteną prieš įjungdamas radiją. LoRa radijas, siųsdamas be antenos, gali sugadinti savo lustą.
{{< /callout >}}

## 2. Įrašyk programinę įrangą {#flash}

1. Prijunk įrenginį prie kompiuterio USB duomenų kabeliu.
2. Chrome arba Edge naršyklėje atidaryk internetinį įrašymo įrankį [flasher.meshcore.io](https://flasher.meshcore.io). Jis naudoja Web Serial, o kitos naršyklės šios funkcijos neturi.
3. Pasirink savo įrenginį, tada **Companion** programinę įrangą, skirtą **Bluetooth** (arba USB, jei naudosi jį tik su kompiuteriu per kabelį).
4. Paleisk įrašymą. Kai kurias plokštes pirmiausia reikia perjungti į atnaujinimo režimą, o įrašymo įrankis parodo, kaip tai padaryti.

*Erase* naudok tik tada, kai nori pradėti nuo nulio: ištrynimas panaikina įrenginio tapatybę ir tavo kontaktus. Vėlesnius atnaujinimus įrašyk netrindamas. Jei nori, kad tapatybė išliktų po ištrynimo, pirmiausia programėlėje eksportuok companion įrenginio privatų raktą, o po ištrynimo jį importuok.

## 3. Įdiek programėlę {#app}

Oficiali MeshCore programėlė skirta Android, iOS, Windows ir macOS sistemoms. Nuorodas į visas versijas rasi svetainėje [meshcore.io](https://meshcore.io). Yra ir internetinė programėlė [app.meshcore.nz](https://app.meshcore.nz), kuri veikia kompiuteryje Chrome arba Edge naršyklėje.

## 4. Susiek savo mazgą {#pair}

Įjunk mazgą, atidaryk programėlę ir prisijunk prie jo per Bluetooth. Kai paprašys PIN kodo:

- mazgas **su** ekranu parodo PIN kodą, tad įvesk jį;
- mazgas **be** ekrano naudoja `123456`.

Jei susieti nepavyksta, pašalink įrenginį iš telefono Bluetooth nustatymų ir bandyk dar kartą. Tada suteik mazgui pavadinimą. Šį pavadinimą mato kiti, tad nenaudok savo vardo ir pavardės ar adreso, nebent to nori.

## 5. Pasirink savo vietovės radijo profilį {#preset}

Visi radijai vienoje vietovėje naudoja tą patį dažnį ir tuos pačius nustatymus, kitaip jie vienas kito negirdi. Programėlės radijo nustatymuose pasirink profilį, kurį naudoja tavo vietovė. Už toliau nurodytų vietovių ribų Europa naudoja **EU/UK (Narrow)**. Nyderlandai, Čekija, Vengrija, Slovakija, Portugalija ir Šveicarija naudoja savo profilius, o Nyderlandų Limburgas turi atskirą variantą:

{{< presets >}}

Įrenginys nesiūlo tavo vietovės profilio? Programėlės radijo nustatymuose ranka įvesk 4 reikšmes iš lentelės: dažnį, juostos plotį, sklaidos koeficientą (spreading factor) ir kodavimo spartą (coding rate). Mazgas su kitomis reikšmėmis tinklo negirdi.

Abejoji? Tavo [vietinė grupė](/community/) žino, kurį profilį naudoja tavo vietovė. Programėlė šį sąrašą atsisiunčia iš MeshCore projekto, tad naujam profiliui programėlės atnaujinimo nereikia.

## 6. Pasisveikink {#hello}

1. **Prisistatyk.** Programėlėje išsiųsk *skelbimą*. „Flood“ skelbimas keliauja per retransliatorius (mazgus, kurie perduoda žinutes toliau), tad visi mesh tinkle gali tave pridėti.
   Kompanionai patys savęs niekada neskelbia.
2. **Rask kitus.** Žmonės atsiranda tavo kontaktuose, kai jų skelbimai tave pasiekia. Retransliatoriai pagal numatytuosius nustatymus siunčia flood skelbimą kas 47 valandas, tad gali prireikti 2 dienų, kol tavo sąrašas užsipildys.
3. **Išsiųsk žinutę.** Atidaryk kontaktą ir rašyk. Pirmoji žinutė pasklinda tinkle flood būdu. Gavėjas atsiunčia atgal maršrutą, kuriuo ji atėjo, o vėlesnės žinutės keliauja juo.
4. **Prisijunk prie kanalų.** Kanalas **Public** jau nustatytas: viskas, ką ten parašai, pasiekia visus mesh tinkle. Pridėk savo regiono *grotažymės kanalą* (kanalą, kurio pavadinimas prasideda `#`), įvesdamas jo pavadinimą. Tavo [vietinė grupė](/community/) pasakys, kurie kanalai aktyvūs.
   Nori susitikti su jais gyvai? Pažiūrėk [susitikimus](/meetings/) savo apylinkėse.

## Kai kas nors neveikia {#troubleshooting}

**Programėlė neranda mano įrenginio per Bluetooth.**
Tikriausiai įrašei USB companion versiją. Įrašyk iš naujo ir pasirink Bluetooth versiją. Heltec V3 plokštės maža įmontuota Bluetooth antena veikia nedideliu atstumu, tad laikyk telefoną arti.

**Susieti vis nepavyksta.**
Pašalink įrenginį iš telefono Bluetooth nustatymų, paleisk Bluetooth iš naujo ir vėl susiek naudodamas PIN kodą iš ekrano arba `123456`.

**Mano kontaktuose nieko nėra.**
Patikrink, ar profilis atitinka tavo vietovę. Išsiųsk „flood“ skelbimą. Jei pasiekiamame atstume nėra kartotuvo, girdėsi tik netoliese esančius radijus. Kartotuvų vietas rasi [žemėlapio puslapyje](/map/).

**Prie kontakto rodoma „last seen“ prieš kelias dienas, nors jis aktyvus.**
Viename iš dviejų mazgų nustatytas neteisingas laikas. Companion įrenginys laiką gauna iš tavo telefono. Kartotuvams ir room server įrenginiams (mazgams, kurie saugo žinutes grupei) laiką turi nustatyti jų savininkas.

**Tiesioginė žinutė niekada neatkeliauja.**
Abu turite būti vienas kito kontaktuose. Mazgas išmeta nepažįstamo siuntėjo žinutę ir siuntėjui apie tai nepraneša. Išsiųsk „flood“ skelbimą ir paprašyk kito žmogaus išsiųsti savąjį. Programėlėje patikrink, ar ji automatiškai prideda naujus kontaktus. Ji prideda tik tuos mazgus, kurie neviršija jos šuolių ribos.

**Seni kontaktai veikia, o nauji niekada neprisijungia.**
Pirmoji žinutė sklinda po visą tinklą, o kartotuvas ją perduoda toliau tik tada, kai turi tos žinutės regioną. Vėlesnės žinutės keliauja išmoktu maršrutu, ir regiono patikra jų nestabdo. Paklausk savo [vietinės grupės](/community/), kokius regionus turi aplink tave esantys kartotuvai, ir patikrink [savo vietovės nustatymus](/guides/settings/#traffic).

**Programėlė nebeprisijungia prie tavo companion įrenginio.**
Kai kurios plokštės turi naudotojo mygtuką, pavyzdžiui, kai kurios RAK plokštės ir Heltec T114. Laikyk jį nuspaustą per pirmas 8 sekundes po plokštės paleidimo. Companion įrenginys per USB atveria gelbėjimo konsolę. Svetainės [flasher.meshcore.io](https://flasher.meshcore.io) konsolėje komanda `set pin <pin>` nustato naują Bluetooth PIN kodą, o `erase` išvalo įrenginį.

**Įrašymo įrankis Linux sistemoje negali atidaryti nuosekliojo prievado.**
Tavo naudotojui reikia prieigos prie prievado, pavyzdžiui, `sudo setfacl -m u:$USER:rw /dev/ttyUSB0`, arba narystės `dialout` grupėje.

**Kitos problemos.** [MeshCore FAQ](https://github.com/meshcore-dev/MeshCore/blob/main/docs/faq.md) aprašo dar daug kitų problemų.
