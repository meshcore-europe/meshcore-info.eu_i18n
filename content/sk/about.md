---
title: Čo je MeshCore?
lead: MeshCore posiela textové správy rádiom, od uzla k uzlu. Funguje bez internetu a bez predplatného.
description: 'Čo MeshCore je a čo nie je: sieť mesh, companiony, repeatery a room servery, smerovanie, šifrovanie a pásmo 868 MHz v Európe.'
eyebrow: MeshCore v1.18.0
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '78bc31e8'
  seeded: '2026-11-02'
  fields: {title: '06eda66b', lead: 'c0174569', description: '658f8a01', eyebrow: '8610c822'}
  sections: ['aa768ac3', 'c9b24089', '0a55792c', 'c3de803d', '493b444f', '429f699c', 'f8008f48', '655373a9', '0894fe81']
  blocks: ['c3c9c568', '55e4248c', 'c0324d05', 'b20e61c3', 'b9fc8810', '68ed3005', 'cabeb32d', 'b2ca68ba', '681d55b9', 'd1df283f', '0d0e2a8b', '0596f602', 'eec63bed', '183a79e4', '47910535', 'd5a92bbf', 'b44d4637', '431021a0', '83c03732', 'e908ca85', '8f79fbf9', '3323d83e', '857c37dc', '0c4d0dd2', 'bd238f09', '794792be', '0eb54b47', '02f1fe2f', 'e6b5b258']
---

MeshCore je bezplatný softvér pre malé LoRa rádiá. LoRa je rádiová technika, ktorá prenáša malé množstvo dát na veľkú vzdialenosť s veľmi nízkou spotrebou. Rádio s MeshCore sa volá *uzol*. Spáruješ ho s aplikáciou v telefóne alebo notebooku, alebo použiješ jeho vlastný displej a klávesnicu. Potom môžeš posielať text ľuďom vzdialeným celé kilometre. Medzi vami nestojí žiadny vysielač, router ani poskytovateľ.

Softvér má otvorený zdrojový kód. Vyvíja sa v repozitári
[meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore) pod licenciou MIT.

## Čo MeshCore nie je {#not}

Začínaš s rádiom? Toto ľudia od MeshCore najčastejšie očakávajú, no MeshCore to nerobí.

- **Nie je to internet ani telefón.** MeshCore posiela krátke textové správy, približne také dlhé ako SMS v telefóne. Hlas, fotky, video ani webové stránky neprenesieš a bežné telefónne číslo ním nezastihneš.
- **Nie je to tiesňová služba.** Žiadna tiesňová služba sieť nepočúva a nikto nesľubuje, že si tvoju správu niekto prečíta. V núdzi volaj 112.
- **Nie je to okamžité ani dostupné všade.** Správa preskakuje z rádia na rádio. Môže to trvať niekoľko sekúnd, alebo správa nedorazí vôbec. Doručenie závisí od repeaterov okolo teba, od výšky, budov a tvojej antény. Malé rádio v interiéri často nikoho nedosiahne, repeater na streche dosiahne na kilometre.
- **Nie je to služba, ktorú pre teba niekto prevádzkuje.** Nie je tu žiadny poskytovateľ, zákaznícka podpora ani prísľub pokrytia. Sieť existuje tam, kde ľudia z komunity postavili repeatery, a nikde inde.
- **Nie všetko v sieti je súkromné.** Priame správy sú šifrované, no Public a hashtagové kanály si môže prečítať ktokoľvek. Názov tvojho uzla a zdieľanú polohu vidí každý v dosahu. [Observery](/network/) posielajú na verejné mapy to, čo počujú. V [časti o šifrovaní](#encryption) sa dozvieš, čo zostáva súkromné.
- **Nie je to neobmedzené.** Všetci v oblasti zdieľajú jeden rádiový kanál a pravidlá [pásma 868 MHz](#band) obmedzujú, ako dlho smie každé rádio vysielať. Každá správa berie vysielací čas všetkým ostatným. Boty, časté adverty a testovacie správy preto spomaľujú sieť pre všetkých.
- **Nie je to Meshtastic.** Meshtastic je iný systém, ktorý beží na veľmi podobných doskách. Tieto dva systémy sa spolu nedohovoria.

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

- Na udržiavanie kontaktu na túrach, na mori a na festivaloch, kde je mobilná sieť preťažená alebo chýba.
- Ako záložný kanál pre rodinu alebo susedov, keď vypadne elektrina alebo mobilné siete.
- Na miestny chat cez rádiá, ktoré ľudia sami vlastnia.
- Na experimenty s rádiom, anténami, solárnou energiou a softvérom s otvoreným zdrojovým kódom.

## Odkiaľ pochádzajú dáta {#data}

Vyhľadávanie na stránke [miestnych skupín](/community/) nájde miesto pomocou kópie voľných zoznamov miest a poštových smerovacích čísel z [GeoNames](https://www.geonames.org/) s licenciou
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Kópia je uložená na tomto webe. Tvoje vyhľadávanie nikdy neopustí tvoje zariadenie a na GeoNames neodchádza žiadna požiadavka.
