---
title: Prvi koraki
lead: Od nove plošče do prvega sporočila v omrežju mesh. Potrebuješ ploščo LoRa, računalnik z brskalnikom Chrome ali Edge ter telefon ali prenosnik za aplikacijo.
description: Iz brskalnika naloži MeshCore, poveži aplikacijo, izberi radijsko prednastavitev svojega območja, pošlji prvo sporočilo in se pridruži lokalnemu kanalu.
eyebrow: 6 korakov · MeshCore v1.18.0
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '0c1b08d9'
  seeded: '2026-11-03'
  fields: {title: '61e8d44a', lead: '45b0e5c3', description: 'cf031b18', eyebrow: '4fa6fe1e'}
  sections: ['16c3728c', '90f3d626', 'df7a1665', '6da9fd7a', 'cb5fb72e', 'a1cf8b26', 'a419ce79', '66d00206']
  blocks: ['16c3728c', '2a70a7ed', '6f8e6f5f', '16c11d47', '757c634a', '081db416', 'd5e7fd0b', '6d28c323', 'eb2ea361', 'de50125c', 'ae20cb8e', 'abd42710', 'c08a865a', '7d1eb0b9', '263e0c96', '0903299f', 'eba20370', '5cdc20cf', '7f542f82', '802ca5a8', '1a854187', 'bc333adf', 'f25b16fa', '7c893ae2', '7f5927b4', '26e13713', '39a142cf', 'a786620c', '216897fa', '2d222782', 'a9755900', 'f081b357']
---

Ti koraki veljajo za vdelano programsko opremo MeshCore v1.18.0 in uradna orodja
iz oktobra 2026. Imena menijev v aplikaciji se med različicami lahko nekoliko razlikujejo.

## 1. Izberi napravo {#device}

Ustreza vsaka plošča, pri kateri je na [strani z napravami](/devices/) naveden
companion. Za svoje prvo vozlišče izberi *companion*: radio, s katerega pošiljaš
sporočila. Prek Bluetootha ali USB ga poveži s telefonom ali prenosnikom. Lahko pa
izbereš model z lastnim zaslonom in tipkovnico, ki deluje samostojno.

Kupi različico za 868 MHz. Priložena antena zadostuje, v
[vodniku po antenah](/guides/antenna/) pa piše, kako anteno preveriš.

Na tvoji plošči zdaj teče Meshtastic? Ko naložiš MeshCore, ga s tem zamenjaš, sistema pa med seboj ne komunicirata.
V razdelku [Prehod z Meshtastica](/about/#meshtastic) piše, kaj deluje drugače.

{{< callout type="warning" >}}
Anteno priklopi, preden vklopiš radio. Radio LoRa, ki oddaja brez antene,
si lahko poškoduje čip.
{{< /callout >}}

## 2. Naloži vdelano programsko opremo {#flash}

1. Napravo poveži z računalnikom s podatkovnim kablom USB.
2. V brskalniku Chrome ali Edge odpri spletno orodje za nalaganje na
   [flasher.meshcore.io](https://flasher.meshcore.io). Orodje potrebuje Web Serial, tega pa drugi brskalniki nimajo.
3. Izberi svojo napravo, nato vdelano programsko opremo **Companion** za **Bluetooth**
   (ali za USB, če jo boš uporabljal samo prek kabla z računalnikom).
4. Zaženi nalaganje. Nekatere plošče morajo najprej preklopiti v način za posodobitev.
   Orodje ti pove, kako to narediš.

Možnost *erase* uporabi samo za čisti začetek: brisanje odstrani identiteto naprave
in tvoje stike. Pri poznejših posodobitvah naloži brez brisanja. Če želiš identiteto
ohraniti tudi po brisanju, prej v aplikaciji izvozi zasebni ključ svojega companiona
in ga pozneje uvozi.

## 3. Namesti aplikacijo {#app}

Uradna aplikacija MeshCore je na voljo za Android, iOS, Windows in macOS.
Povezave do vseh različic najdeš na [meshcore.io](https://meshcore.io). Na voljo je
tudi spletna aplikacija na [app.meshcore.nz](https://app.meshcore.nz), ki na računalniku
deluje v brskalniku Chrome ali Edge.

## 4. Poveži svoje vozlišče {#pair}

Vklopi vozlišče, odpri aplikacijo in se z njim poveži prek Bluetootha. Ko aplikacija
zahteva PIN:

- vozlišče **z** zaslonom prikaže PIN, ti pa ga vtipkaj;
- vozlišče **brez** zaslona uporablja `123456`.

Če povezovanje ne uspe, odstrani napravo iz nastavitev Bluetootha na telefonu in
poskusi znova. Nato vozlišču daj ime. To ime vidijo drugi, zato ne uporabi
polnega imena ali naslova, razen če to želiš.

## 5. Izberi radijsko prednastavitev svojega območja {#preset}

Vsi radii na območju uporabljajo isto frekvenco in iste nastavitve, sicer se med seboj
ne slišijo. V radijskih nastavitvah aplikacije izberi prednastavitev svojega območja.
Zunaj spodnjih območij Evropa uporablja **EU/UK (Narrow)**. Nizozemska, Češka,
Madžarska, Slovaška, Portugalska in Švica uporabljajo svoje, Limburg na Nizozemskem
pa ima posebno različico:

{{< presets >}}

Tvoja naprava ne ponuja prednastavitve za tvoje območje? V radijskih nastavitvah
aplikacije ročno vnesi 4 vrednosti iz tabele: frekvenco, pasovno širino, faktor
razširjanja in kodno razmerje. Vozlišče z drugačnimi vrednostmi omrežja mesh ne sliši.

Ne veš zagotovo? Tvoja [lokalna skupina](/community/) ve, katero prednastavitev
uporablja tvoje območje. Aplikacija ta seznam prenese od projekta MeshCore, zato nova
prednastavitev ne zahteva posodobitve aplikacije.

## 6. Pozdravi {#hello}

1. **Predstavi se.** V aplikaciji pošlji *advert* (objavo svojega vozlišča). Advert tipa
   „flood“ potuje prek repetitorjev (vozlišč, ki posredujejo sporočila), zato te lahko
   doda vsak v omrežju mesh.
   Companioni se nikoli ne predstavijo samodejno.
2. **Poišči druge.** Ljudje se prikažejo med tvojimi stiki, ko te dosežejo njihovi
   adverti. Repetitorji privzeto pošljejo advert flood vsakih 47 ur, zato se lahko
   seznam polni 2 dni.
3. **Pošlji sporočilo.** Odpri stik in piši. Prvo sporočilo preplavi omrežje. Prejemnik
   nato sporoči pot, po kateri je prišlo, in naslednja sporočila gredo po tej poti.
4. **Pridruži se kanalom.** Kanal **Public** je že nastavljen, kar napišeš vanj, pa
   doseže vse v omrežju mesh. Dodaj *kanal s ključnikom* svoje regije (ime se začne
   z `#`), tako da vtipkaš njegovo ime. Tvoja [lokalna skupina](/community/) ti bo
   povedala, kateri kanali so aktivni.

## Ko kaj ne deluje {#troubleshooting}

**Aplikacija prek Bluetootha ne najde moje naprave.**
Verjetno si naložil companion za USB. Nalaganje ponovi in izberi različico za
Bluetooth. Na plošči Heltec V3 ima majhna vgrajena antena za Bluetooth kratek doseg,
zato drži telefon blizu.

**Povezovanje vedno znova spodleti.**
Odstrani napravo iz nastavitev Bluetootha na telefonu, znova zaženi Bluetooth in se
ponovno poveži s PIN-om z zaslona ali s `123456`.

**Med mojimi stiki ni nikogar.**
Preveri, ali se tvoja prednastavitev ujema z območjem. Pošlji advert flood. Če v dosegu
ni repetitorja, boš slišal samo bližnje radie. Lokacije repetitorjev najdeš na
[strani z zemljevidom](/map/).

**Pri stiku piše „last seen“ pred več dnevi, čeprav je aktiven.**
Eno od obeh vozlišč ima napačen čas. Companion dobi čas s tvojega telefona. Pri
repetitorjih in strežnikih sob (vozliščih, ki hranijo sporočila za skupino) mora čas
nastaviti lastnik.

**Neposredno sporočilo nikoli ne prispe.**
Oba morata imeti drug drugega med stiki. Vozlišče zavrže sporočilo nekoga, ki ga ne
pozna, pošiljatelju pa tega ne sporoči. Pošlji advert flood in prosi drugo osebo, naj
ga pošlje tudi sama. V aplikaciji preveri, ali samodejno dodaja nove stike. Dodaja samo
vozlišča znotraj svoje omejitve skokov.

**Stari stiki delujejo, novi se nikoli ne povežejo.**
Prvo sporočilo preplavi omrežje, repetitor pa ga posreduje samo, če ima nastavljeno
regijo tega sporočila. Naslednja sporočila gredo po naučeni poti, ki je preverjanje
regije ne ustavi. Svojo [lokalno skupino](/community/) vprašaj, katere regije imajo
repetitorji v tvoji bližini, in preveri [nastavitve za svoje območje](/guides/settings/#traffic).

**Aplikacija se ne poveže več s tvojim companionom.**
Nekatere plošče imajo uporabniški gumb, na primer nekatere plošče RAK in Heltec T114.
Drži ga pritisnjenega v prvih 8 sekundah po zagonu plošče. Companion nato prek USB odpre
reševalno konzolo. V konzoli na [flasher.meshcore.io](https://flasher.meshcore.io) z ukazom
`set pin <pin>` nastaviš nov PIN za Bluetooth, z `erase` pa izbrišeš napravo.

**Orodje za nalaganje v Linuxu ne more odpreti serijskih vrat.**
Tvoj uporabnik potrebuje dostop do vrat, na primer
`sudo setfacl -m u:$USER:rw /dev/ttyUSB0`, ali članstvo v skupini `dialout`.

**Nekaj drugega.** V
[MeshCore FAQ](https://github.com/meshcore-dev/MeshCore/blob/main/docs/faq.md)
je opisanih še veliko drugih težav.
