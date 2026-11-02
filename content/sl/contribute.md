---
title: Sodeluj
lead: Ta vodnik pišejo, preverjajo in prevajajo prostovoljci. Tukaj izveš, kako lahko pomagaš, z računom GitHub ali brez njega.
description: Dodaj svojo skupnost, napravo ali projekt, preglej prevod ali izboljšaj vodnik na meshcore-info.eu.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'f3ed6e9b'
  seeded: '2026-11-02'
  fields: {title: '97b0c61b', lead: 'e9b40d4d', description: '3bd97cd2'}
  sections: ['6e9d4b61', 'aca796d7', 'd4848d5b', '247b2601', '8a60e0d4', '645c82d3', 'c755b654']
  blocks: ['2f9dd6e8', '44167907', 'b020e1a4', 'f2c726cd', '2e9d1fdd', 'b2a902ba', 'b15ce10b', '2be86888', '3db6cb63', '2e3c2fc0', '693a5d9d', '73e33897', '96d8689d', 'c67fd14a', 'f92f7e49', '12ddca6c', 'e947e2a9', '526df4bb', 'e0d3559e']
---

Vsa vsebina tega spletnega mesta je v javnem
[repozitoriju GitHub](https://github.com/meshcore-europe/meshcore-info.eu). Manjše spremembe
oddaš prek obrazca na GitHubu (issue). Za večje spremembe odpreš pull
request: to je predlog sprememb datotek, ki ga pregleda vzdrževalec. Vzdrževalec
vsako spremembo preveri pred objavo.

Nimaš računa GitHub? Povej nam na [Discordu](https://discord.meshcore-info.eu/), če
manjka kakšna skupina, če je podatek napačen ali če prevod zveni čudno. Zadevo
nato prevzame prostovoljec.

## Dodaj svojo skupnost {#community}

Vodiš lokalno skupino MeshCore, ki se ji lahko pridruži vsakdo? Izpolni
[obrazec za skupnost](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-community.yml)
in vanj vpiši ime, območje in javne povezave. Ko jo dodamo, se tvoja skupina prikaže
na strani [Lokalne skupine](/community/) v vseh jezikih.

## Predlagaj napravo ali projekt {#device-project}

Na [strani z napravami](/devices/) so navedeni tehnični podatki iz dokumentacije proizvajalcev,
povezav do trgovin pa tam nikoli ne objavljamo. Strojno opremo predlagaj prek
[obrazca za napravo](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-device.yml).
Si za MeshCore izdelal aplikacijo, orodje, most ali načrt strojne opreme z javno izvorno
kodo? Projekt dodaj prek
[obrazca za projekt](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-project.yml).

## Preglej prevod {#translate}

Strani v drugih jezikih najprej nastanejo s strojnim prevajanjem, kar piše tudi na vrhu
strani. Prevodi so v ločenem repozitoriju,
[meshcore-info.eu_i18n](https://github.com/meshcore-europe/meshcore-info.eu_i18n), zato
ti kode spletnega mesta nikoli ni treba spreminjati. Če dobro govoriš enega od teh jezikov,
lahko prevod izboljšaš:

1. Odpri stran in klikni »Pomagaj izboljšati ta prevod«. Datoteka se odpre
   na GitHubu, kjer jo lahko urejaš v brskalniku.
2. Popravi besedilo. Povezave, kodo, številke in imena, kot je MeshCore, pusti
   natanko takšne, kot so.
3. V bloku `translation` na vrhu zamenjaj `status: ai` s
   `status: human` in predlagaj spremembo.

Si opazil napačno besedo, a nimaš časa za popravek? Sporoči jo prek
[obrazca za prevode](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=translation-bug.yml).

## Izboljšaj vodnik {#guides}

Vodnike najprej napišemo v angleščini in jih nato prevedemo iz nje. Popravke
in nove teme lahko predlagaš prek
[obrazca za vsebino](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=new-content.yml)
ali s pull requestom. Dejstva morajo imeti vir: vdelano programsko opremo MeshCore in njeno
dokumentacijo, regulatorja radijskih frekvenc ali proizvajalca. Piši s svojimi besedami. Kratek
navedek z virom je v redu.

V [vodniku za sodelavce](https://github.com/meshcore-europe/meshcore-info.eu/blob/main/CONTRIBUTING.md)
piše, kako spletno mesto urejaš na svojem računalniku.

## Stanje prevodov {#coverage}

»Pregledano« pomeni, da je prevod preveril
človek; »Strojno« pomeni, da je prevod strojen in še ni pregledan;
»Zastarelo« pomeni, da se je angleško besedilo spremenilo po nastanku prevoda;
»Manjka« pomeni, da stran še nima prevoda.

{{< coverage >}}

## Zasluge {#credits}

Spletno mesto je izdelano z [Astrom](https://astro.build/). Uporablja pisavi
IBM Plex Sans in IBM Plex Mono pod licenco SIL Open Font License. Prevodi
sledijo
pravilom projekta [kiekr-i18n](https://github.com/marcelverdult/kiekr-i18n) in
uporabljajo njegove glosarje za MeshCore. Sam MeshCore razvijajo na
[meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore).

Za besedilo in prevode velja licenca CC BY 4.0, za kodo pa licenca
MIT.
