---
title: Prispej
lead: Túto príručku píšu, kontrolujú a prekladajú dobrovoľníci. Tu zistíš, ako môžeš pomôcť, s účtom GitHub aj bez neho.
description: Pridaj svoju komunitu, zariadenie alebo projekt, skontroluj preklad alebo vylepši návod na meshcore-info.eu.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'f3ed6e9b'
  seeded: '2026-11-02'
  fields: {title: '97b0c61b', lead: 'e9b40d4d', description: '3bd97cd2'}
  sections: ['6e9d4b61', 'aca796d7', 'd4848d5b', '247b2601', '8a60e0d4', '645c82d3', 'c755b654']
  blocks: ['2f9dd6e8', '44167907', 'b020e1a4', 'f2c726cd', '2e9d1fdd', 'b2a902ba', 'b15ce10b', '2be86888', '3db6cb63', '2e3c2fc0', '693a5d9d', '73e33897', '96d8689d', 'c67fd14a', 'f92f7e49', '12ddca6c', 'e947e2a9', '526df4bb', 'e0d3559e']
---

Celý obsah tohto webu je vo verejnom
[repozitári na GitHube](https://github.com/meshcore-europe/meshcore-info.eu). Malé zmeny
navrhneš cez formulár na GitHube (issue). Väčšie zmeny pošleš ako pull
request: je to návrh úpravy súborov, ktorý posúdi správca. Správca skontroluje
každú zmenu pred zverejnením.

Nemáš účet na GitHube? Napíš nám na [Discord](https://discord.meshcore-info.eu/), ak chýba
nejaká skupina, nesedí nejaký fakt alebo preklad znie zvláštne. Ďalej sa o to
postará dobrovoľník.

## Pridaj svoju komunitu {#community}

Vedieš miestnu skupinu MeshCore, do ktorej sa môže pridať ktokoľvek? Vyplň
[formulár pre komunity](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-community.yml)
a uveď názov, oblasť a verejné odkazy. Po pridaní sa tvoja skupina zobrazí
na stránke [Miestne skupiny](/community/) vo všetkých jazykoch.

## Navrhni zariadenie alebo projekt {#device-project}

Na [stránke zariadení](/devices/) uvádzame špecifikácie z dokumentácie výrobcov
a nikdy neodkazujeme na obchody. Hardvér navrhneš cez
[formulár pre zariadenia](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-device.yml).
Vytvoril si pre MeshCore aplikáciu, nástroj, most alebo hardvérový návrh s verejným
zdrojovým kódom? Pridaj projekt cez
[formulár pre projekty](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-project.yml).

## Skontroluj preklad {#translate}

Stránky v iných jazykoch vznikajú najprv strojovým prekladom a na ich začiatku
je o tom upozornenie. Preklady majú vlastný repozitár,
[meshcore-info.eu_i18n](https://github.com/meshcore-europe/meshcore-info.eu_i18n), takže
kód webu nikdy nemusíš upravovať. Ak dobre ovládaš niektorý z jazykov,
môžeš preklad vylepšiť:

1. Otvor stránku a klikni na „Pomôž vylepšiť tento preklad“. Súbor sa otvorí
   na GitHube, kde ho môžeš upraviť v prehliadači.
2. Oprav znenie. Odkazy, kód, čísla a názvy ako MeshCore ponechaj
   presne tak, ako sú.
3. V bloku `translation` na začiatku súboru zmeň `status: ai` na
   `status: human` a navrhni zmenu.

Našiel si nesprávne slovo, ale nemáš čas ho opraviť? Nahlás ho cez
[formulár pre preklady](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=translation-bug.yml).

## Vylepši návod {#guides}

Návody najprv píšeme po anglicky a z angličtiny ich prekladáme. Opravy
a nové témy môžeš poslať cez
[formulár pre obsah](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=new-content.yml)
alebo ako pull request. Fakty musia mať zdroj: firmvér MeshCore a jeho
dokumentáciu, úrad pre reguláciu rádiových frekvencií alebo výrobcu. Píš vlastnými slovami.
Krátky citát s uvedením zdroja je v poriadku.

[Príručka pre prispievateľov](https://github.com/meshcore-europe/meshcore-info.eu/blob/main/CONTRIBUTING.md)
vysvetľuje, ako môžeš na webe pracovať na vlastnom počítači.

## Stav prekladov {#coverage}

„Skontrolované“ znamená, že preklad skontroloval človek. „Strojové“ znamená,
že ide o strojový preklad, ktorý ešte nikto neskontroloval. „Zastarané“ znamená,
že sa anglický text po vzniku prekladu zmenil. „Chýba“ znamená,
že stránka ešte nemá preklad.

{{< coverage >}}

## Poďakovanie {#credits}

Web je postavený na [Astro](https://astro.build/). Používa písma
IBM Plex Sans a IBM Plex Mono pod licenciou SIL Open Font License. Preklady
sa riadia konvenciami projektu [kiekr-i18n](https://github.com/marcelverdult/kiekr-i18n)
a používajú jeho glosáre MeshCore. Samotný MeshCore sa vyvíja v repozitári
[meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore).

Na text a preklady sa vzťahuje licencia CC BY 4.0, na kód licencia MIT.
