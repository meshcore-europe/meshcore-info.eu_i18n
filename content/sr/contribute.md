---
title: Doprinesi
lead: Ovaj vodič pišu, proveravaju i prevode volonteri. Evo kako možeš da pomogneš, sa GitHub nalogom ili bez njega.
description: Dodaj svoju zajednicu, uređaj ili projekat, pregledaj prevod ili poboljšaj neki vodič na meshcore-info.eu.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'f3ed6e9b'
  seeded: '2026-11-02'
  fields: {title: '97b0c61b', lead: 'e9b40d4d', description: '3bd97cd2'}
  sections: ['6e9d4b61', 'aca796d7', 'd4848d5b', '247b2601', '8a60e0d4', '645c82d3', 'c755b654']
  blocks: ['2f9dd6e8', '44167907', 'b020e1a4', 'f2c726cd', '2e9d1fdd', 'b2a902ba', 'b15ce10b', '2be86888', '3db6cb63', '2e3c2fc0', '693a5d9d', '73e33897', '96d8689d', 'c67fd14a', 'f92f7e49', '12ddca6c', 'e947e2a9', '526df4bb', 'e0d3559e']
---

Sav sadržaj ovog sajta nalazi se u javnom
[GitHub repozitorijumu](https://github.com/meshcore-europe/meshcore-info.eu). Za male izmene
popunjavaš formular na GitHub-u (issue). Veće izmene šalješ kao pull
request: to je predlog izmene fajlova koji pregleda održavalac. Održavalac proverava
svaku izmenu pre objavljivanja.

Nemaš GitHub nalog? Javi nam na [Discord-u](https://discord.meshcore-info.eu/) ako primetiš
da neka grupa nedostaje, da je neki podatak netačan ili da prevod čudno zvuči. Dalje
to preuzima volonter.

## Dodaj svoju zajednicu {#community}

Vodiš lokalnu MeshCore grupu kojoj svako može da se pridruži? Popuni
[formular za zajednicu](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-community.yml)
i navedi naziv, područje i javne linkove. Kada je dodamo, tvoja grupa će se pojaviti
na stranici [Lokalne grupe](/community/) na svim jezicima.

## Predloži uređaj ili projekat {#device-project}

Na [stranici o uređajima](/devices/) navodimo specifikacije iz dokumentacije proizvođača
i nikada ne stavljamo linkove ka prodavnicama. Hardver možeš da predložiš preko
[formulara za uređaje](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-device.yml).
Napravio si aplikaciju, alat, most ili hardverski dizajn za MeshCore s javnim izvornim
kodom? Dodaj ga preko
[formulara za projekte](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-project.yml).

## Pregledaj prevod {#translate}

Stranice na drugim jezicima u početku su mašinski prevodi, i to piše na njihovom
vrhu. Prevodi se nalaze u posebnom repozitorijumu,
[meshcore-info.eu_i18n](https://github.com/meshcore-europe/meshcore-info.eu_i18n), pa
nikada ne moraš da diraš kod sajta. Ako dobro znaš neki od tih jezika, možeš da poboljšaš prevod:

1. Otvori stranicu i klikni na „Pomozi da poboljšamo ovaj prevod”. Tako otvaraš
   fajl na GitHub-u, gde možeš da ga izmeniš u pregledaču.
2. Popravi formulacije. Linkove, kod, brojeve i nazive kao što je MeshCore
   ostavi tačno onakve kakvi jesu.
3. U bloku `translation` na vrhu promeni `status: ai` u
   `status: human`, pa predloži izmenu.

Primetio si pogrešnu reč, ali nemaš vremena da je ispraviš? Prijavi je preko
[formulara za prevode](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=translation-bug.yml).

## Poboljšaj vodič {#guides}

Vodiče prvo pišemo na engleskom, a zatim ih prevodimo s tog jezika. Ispravke
i nove teme možeš da pošalješ preko
[formulara za sadržaj](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=new-content.yml)
ili kao pull request. Za činjenice je potreban izvor: MeshCore firmver i njegova
dokumentacija, regulator za radio-komunikacije ili proizvođač. Piši svojim rečima. Kratak
citat s navedenim izvorom je u redu.

U [vodiču za saradnike](https://github.com/meshcore-europe/meshcore-info.eu/blob/main/CONTRIBUTING.md)
piše kako da radiš na sajtu na svom računaru.

## Status prevoda {#coverage}

„Pregledano” znači da je prevod proverio čovek; „Mašinski” znači da je prevod
mašinski i da ga još niko nije pregledao;
„Zastarelo” znači da se engleski tekst promenio nakon što je prevod nastao;
„Nedostaje” znači da stranica još nema prevod.

{{< coverage >}}

## Zasluge {#credits}

Sajt je napravljen pomoću alata [Astro](https://astro.build/). Koristi fontove
IBM Plex Sans i IBM Plex Mono, pod licencom SIL Open Font License. Prevodi
prate
konvencije projekta [kiekr-i18n](https://github.com/marcelverdult/kiekr-i18n) i
koriste njegove MeshCore glosare. Sam MeshCore se razvija na
[meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore).

Tekst i prevodi su objavljeni pod licencom CC BY 4.0, a kod pod licencom
MIT.
