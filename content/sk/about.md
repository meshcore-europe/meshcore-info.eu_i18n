---
title: Čo je MeshCore?
lead: MeshCore posiela textové správy rádiom, od uzla k uzlu. Funguje bez internetu a bez predplatného.
description: 'Čo MeshCore je a čo nie je: druhy uzlov, smerovanie, šifrovanie a pásmo 868 MHz.'
eyebrow: MeshCore v1.18.0
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '2a40da22'
  seeded: '2026-11-04'
  fields: {title: '06eda66b', lead: 'c0174569', description: 'c2255f49', eyebrow: '8610c822'}
  sections: ['aa768ac3', '92fc3ea7', '0a55792c', 'c3de803d', '493b444f', '429f699c', 'f8008f48', '203a07ef', '0894fe81']
  blocks: ['c3c9c568', '55e4248c', 'c0324d05', 'b20e61c3', 'ac039316', '68ed3005', 'cabeb32d', 'b2ca68ba', '681d55b9', 'd1df283f', '0d0e2a8b', '0596f602', 'eec63bed', '183a79e4', '47910535', 'd5a92bbf', 'b44d4637', '431021a0', '83c03732', 'e908ca85', '8f79fbf9', '3323d83e', '857c37dc', '0c4d0dd2', 'bd238f09', '794792be', '5d796ffb', '1a490368', 'f0dd237f', '3182d5c8', '02f1fe2f', 'e6b5b258']
---

MeshCore je bezplatný softvér pre malé LoRa rádiá. LoRa je rádiová technika, ktorá prenáša malé množstvo dát na veľkú vzdialenosť s veľmi nízkou spotrebou. Rádio s MeshCore sa volá *uzol*. Spáruješ ho s aplikáciou v telefóne alebo notebooku, alebo použiješ jeho vlastný displej a klávesnicu. Potom môžeš posielať text ľuďom vzdialeným celé kilometre. Medzi vami nestojí žiadny vysielač, router ani poskytovateľ.

Softvér má otvorený zdrojový kód. Vyvíja sa v repozitári
[meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore) pod licenciou MIT.

## Čo MeshCore nie je {#not}

Začínaš s rádiom? Toto ľudia od MeshCore najčastejšie očakávajú, no MeshCore to nerobí.

- **Nie je to internet ani telefón.** MeshCore posiela krátke textové správy,
  zhruba také dlhé ako SMS v tvojom telefóne. Žiadny hlas, fotky, video
  ani webové stránky a na bežné telefónne číslo sa nedovoláš.
- **Nie je to tiesňová služba.** Žiadna tiesňová služba nesľubuje, že
  bude mesh počúvať, a nikto nesľubuje, že tvoju správu niekto prečíta.
- **Nefunguje to okamžite ani všade.** Správa skáče z rádia na
  rádio a môže jej to trvať pár sekúnd, alebo nepríde vôbec. Či prejde, závisí
  od repeaterov okolo teba, od výšky, budov a tvojej antény. Malé rádio
  v interiéri často nedosiahne nikoho. Repeater na streche dosiahne kilometre ďaleko.
- **Nie je to služba, ktorú pre teba niekto prevádzkuje.** Nemá
  poskytovateľa, helpdesk ani prísľub pokrytia. Mesh existuje tam, kde ľudia
  z komunity postavili repeatery.
- **Nie všetko v meshi je súkromné.** Priame správy sú šifrované. Kanál Public
  a hashtagové kanály však môže čítať ktokoľvek. Meno tvojho uzla a zdieľanú
  polohu vidí každý v dosahu. [Observery](/network/) posielajú to, čo počujú, na
  verejné mapy. [Časť o šifrovaní](#encryption) vysvetľuje, čo zostane súkromné.
- **Nie je to neobmedzené.** Všetci v oblasti zdieľajú jeden rádiový kanál.
  Pravidlá pre [pásmo 868 MHz](#band) obmedzujú, ako dlho môže každé rádio
  vysielať. Každá správa berie vysielací čas všetkým ostatným. Boty, časté
  adverty a testovacie správy preto spomaľujú mesh pre všetkých.
- **Nie je to Meshtastic.** Meshtastic je iný systém, ktorý beží na
  takmer rovnakých doskách. Tieto dva systémy spolu nedokážu komunikovať.

## Sieť mesh za minútu {#mesh}

Jedno LoRa rádio dosiahne v meste niekoľko kilometrov, z kopca alebo strechy oveľa ďalej. Aby sa správy dostali ešte ďalej, rádiá si ich navzájom odovzdávajú: to je *mesh*, teda sieť. V MeshCore správy odovzdávajú rádiá nazývané *repeatery*. Keď repeater zachytí správu, odvysiela ju znova, takže správa môže prejsť celým regiónom.

Sieť nikto nevlastní. Každý uzol a každý repeater patrí niekomu z komunity. Sieť siaha tak ďaleko, kam dosiahnu ich repeatery.

## 3 druhy uzlov {#roles}

Druh uzla si vyberieš pri flashovaní. Tvoj prvý uzol je companion.

**Companion.** Tvoje vlastné rádio. Cez Bluetooth alebo USB ho spáruješ s aplikáciou MeshCore v telefóne alebo notebooku. Niektoré majú vlastný displej a klávesnicu. V aplikácii čítaš a píšeš. Companion uchováva tvoje kontakty a kanály a tiež správy, ktoré prišli, kým aplikácia nebola pripojená. Správy pre ostatných companion neodovzdáva.

**Repeater.** Rádio umiestnené vysoko, ktoré odovzdáva správy pre všetkých. Väčšina repeaterov beží na solárnu energiu. Vlastný potrebuješ len tam, kam sieť ešte nedosahuje. Nemá vlastnú aplikáciu. Nastavíš ho cez USB alebo sa prihlásiš heslom a spravuješ ho cez rádio. Postup nájdeš v [príručke k repeateru](/repeater-guide/).

**Room server.** Malá nástenka so správami v sieti. Po prihlásení dostaneš príspevky, ktoré ti ušli mimo dosahu, najviac posledných 32. Room server ich drží len v pamäti, takže reštart alebo výpadok napájania ich vymaže. Miestna skupina ho používa na oznamy.

## Ako si správa nájde cestu {#routing}

Každý uzol má tajný kľúč a verejný kľúč. Verejný kľúč je jeho identita. Uzol sa ohlasuje *advertom*: podpísaným paketom s názvom uzla a, ak chceš, aj s jeho polohou. Niekto sa objaví v tvojich kontaktoch, keď k tebe dorazí jeden z jeho advertov alebo keď naskenuješ jeho QR kód. V aplikácii je tlačidlo na odoslanie tvojho vlastného advertu.

Tvoja prvá správa kontaktu odchádza ako *flood*, teda záplava. Každý repeater, ktorý ju zachytí, ju raz odovzdá a cestou pridá svoje krátke ID. Odpoveď prinesie tento zoznam ID späť. Odvtedy tvoje správy tomuto kontaktu idú po zaznamenanej trase a vysielajú len repeatery na nej. Keď sa trasa preruší, aplikácia znova použije flood.

Správy do kanála nemajú jednu adresu, takže sa vždy šíria ako flood. Repeatery si pamätajú, čo nedávno odovzdali, a kópie, ktoré dorazia inou trasou, zahodia. Správa môže prejsť cez najviac 64 repeaterov, alebo cez 32, ak predvoľba používa 2-bajtové ID.

## Šifrovanie a súkromie {#encryption}

Tvoje priame správy sú šifrované end-to-end: čítať ich môžeš len ty a druhá osoba. Repeater vidí adresáta paketu len ako 1-bajtovú nápovedu.

Kanály sú šifrované zdieľaným kľúčom, takže to, kto ich môže čítať, závisí od toho, kto má tento kľúč:

- **Public** je nastavený na každom companione. Jeho kľúč je zverejnený, takže ho môže čítať ktokoľvek.
- **Hashtagové kanály**, napríklad `#utrecht`, odvodzujú svoj kľúč z názvu. Pripojiť sa môže každý, kto názov pozná, preto ich tiež ber ako verejné.
- **Súkromné kanály** používajú náhodný kľúč, ktorý zdieľaš ty, napríklad ako QR kód.

Adverty sú podpísané, ale nie šifrované. Názov tvojho uzla a jeho polohu, ak ju zdieľaš, vidí každý v dosahu. Vyber si názov, ktorý neprezradí viac, než chceš.

## Pásmo 868 MHz v Európe {#band}

V Európe MeshCore používa malú časť pásma 868 MHz, ktorú smie každý využívať bez licencie. Jeho európska rádiová predvoľba EU/UK (Narrow) leží na 869.618 MHz s kanálom 62.5 kHz. To je v podpásme 869.40-869.65 MHz, ktoré povoľuje najviac 500 mW e.r.p. Zariadenie tam smie vysielať najviac 10% času. Podrobnosti a limity pre jednotlivé krajiny nájdeš v [právnej časti príručky k repeateru](/repeater-guide/#legal).

Všetci v oblasti používajú rovnakú predvoľbu, inak sa ich rádiá navzájom nepočujú. Niektoré krajiny a regióny používajú variant: tvoja [miestna skupina](/community/) vie, ktorý.

## Na čo to ľudia používajú {#uses}

- Byť v kontakte na túrach, na mori a na festivaloch, kde je mobilná sieť
  preťažená alebo chýba.
- Záložný kanál pre rodinu alebo susedov, keď zlyhajú elektrické alebo mobilné
  siete.
- Záloha pre miestne úrady, keď zlyhajú ich bežné siete.
- Miestny chat na rádiách, ktoré ľudia sami vlastnia.
- Udržať pátrací a záchranný tím v spojení tam, kde nie je mobilná sieť.
  MeshCore SAR, komunitná aplikácia v časti [Projekty](/projects/), pridáva mapy
  a zdieľané polohy.
- Kontrola vzdialeného miesta z domu. Repeatery a senzorové uzly hlásia napätie
  batérie a ďalšie hodnoty, keď si ich vyžiadaš.
- Sledovanie senzora. Na senzorovom uzle beží firmvér MeshCore určený na
  meranie. Uzol uchováva históriu napätia svojej batérie. Prihlás sa ako admin
  a uzol ťa upozorní, keď je batéria slabá. Upozornenia na ďalšie hodnoty
  pridáš vlastným kódom.
- Spínanie niečoho na diaľku, napríklad čerpadla. To pridáš do firmvéru senzora
  vlastným kódom.
- Experimentovanie s rádiom, anténami, solárnou energiou a softvérom
  s otvoreným zdrojovým kódom.

Niektoré úrady budujú alebo testujú záložné riešenie postavené na MeshCore. Tieto príklady sme overili
v novembri 2026.

- Cyklón Gabrielle prerušil všetku komunikáciu v Tairāwhiti na Novom Zélande. V
  septembri 2025 krízový manažment regiónu označil MeshCore za
  [jeden z najmenej 6 záložných spôsobov komunikácie](https://www.scoop.co.nz/stories/AK2509/S00669.htm).
  Zároveň budoval solárne repeatery ako chrbticu siete.
- Nemecký okres Bad Kissingen
  [buduje na MeshCore textovú sieť](https://www.landkreis-badkissingen.de/wirtschaft/digitalisierung/kommunikationsnetze/index.html)
  pre úrady, záchranné zložky a kritické objekty. Ako prvé sa pripájajú hasičské
  stanice.
- Mestské zastupiteľstvo Hilversumu v Holandsku
  [odhlasovalo pomerom 34 ku 1 skúšobnú prevádzku](https://hilversum.nl/nieuwsoverzicht/gemeenteraad-buigt-zich-over-financien)
  s repeaterom na veži radnice. Mesto ju
  [vyhodnotí na jeseň 2027](https://www.spreekbuis.nl/hilversum-start-proef-met-onafhankelijk-noodcommunicatienetwerk-meshcore/).
- Dva holandské bezpečnostné regióny, ktoré organizujú reakciu na krízu,
  experimentujú s MeshCore:
  [Južný Limburg](https://nos.nl/nieuwsuur/artikel/2607176-communicatie-hulpdiensten-valt-uit-bij-lange-stroomstoring-oplossing-niet-in-zicht)
  a [Drenthe](https://www.rtvdrenthe.nl/nieuws/18438486/hackerspace-drenthe-werkt-aan-een-noodnetwerk-voor-de-provincie).
  Podľa Drenthe je priskoro povedať, ako alebo kedy by ho mohla použiť.
- V Dalfsene, tiež v Holandsku, dobrovoľníci
  [vedú pilotný projekt spolu s obcami](https://noodnetoverijssel.nl/).
  Primárne používajú hlasové rádio a MeshCore ako druhú vrstvu na text.

Nikto nesľubuje, že tvoju správu v meshi vo tvojom okolí niekto prečíta.

## Odkiaľ pochádzajú dáta {#data}

Vyhľadávanie na stránke [miestnych skupín](/community/) nájde miesto pomocou kópie voľných zoznamov miest a poštových smerovacích čísel z [GeoNames](https://www.geonames.org/) s licenciou
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Kópia je uložená na tomto webe. Tvoje vyhľadávanie nikdy neopustí tvoje zariadenie a na GeoNames neodchádza žiadna požiadavka.
