---
title: Bidrag
lead: Frivillige skriver, kontrollerer og oversætter denne guide. Her kan du se, hvordan du hjælper, med eller uden en GitHub-konto.
description: Tilføj dit fællesskab, en enhed eller et projekt, gennemgå en oversættelse, eller forbedr en guide på meshcore-info.eu.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'f3ed6e9b'
  seeded: '2026-10-31'
  fields: {title: '97b0c61b', lead: 'e9b40d4d', description: '3bd97cd2'}
  sections: ['6e9d4b61', 'aca796d7', 'd4848d5b', '247b2601', '8a60e0d4', '645c82d3', 'c755b654']
  blocks: ['2f9dd6e8', '44167907', 'b020e1a4', 'f2c726cd', '2e9d1fdd', 'b2a902ba', 'b15ce10b', '2be86888', '3db6cb63', '2e3c2fc0', '693a5d9d', '73e33897', '96d8689d', 'c67fd14a', 'f92f7e49', '12ddca6c', 'e947e2a9', '526df4bb', 'e0d3559e']
---

Alt på dette site ligger i et offentligt
[GitHub-repository](https://github.com/meshcore-europe/meshcore-info.eu). Små ændringer
sender du via en formular på GitHub (et issue). Større ændringer sender du som en pull
request: et forslag til ændring af filerne, som en maintainer gennemgår. En
maintainer kontrollerer hver ændring, før den går live.

Har du ingen GitHub-konto? Fortæl os det på [Discord](https://discord.meshcore-info.eu/): en
manglende gruppe, en forkert oplysning eller en oversættelse, der lyder mærkelig. En frivillig
tager sig af resten.

## Tilføj dit fællesskab {#community}

Driver du en lokal MeshCore-gruppe, som alle kan blive en del af? Udfyld
[fællesskabsformularen](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-community.yml)
med navn, område og de offentlige links. Når vi har tilføjet din gruppe, vises den
på siden [Lokale grupper](/community/) på alle sprog.

## Foreslå en enhed eller et projekt {#device-project}

[Enhedssiden](/devices/) viser specifikationer fra producenternes
dokumentation og linker aldrig til butikker. Foreslå hardware med
[enhedsformularen](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-device.yml).
Har du bygget en app, et værktøj, en bridge eller et hardwaredesign til MeshCore med offentlig kildekode?
Tilføj det med
[projektformularen](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-project.yml).

## Gennemgå en oversættelse {#translate}

Sider på andre sprog starter som maskinoversættelser, og det står øverst på
siden. Oversættelserne ligger i deres eget repository,
[meshcore-info.eu_i18n](https://github.com/meshcore-europe/meshcore-info.eu_i18n), så
du aldrig behøver at røre sitets kode. Taler du et af sprogene
godt, kan du gøre oversættelsen bedre:

1. Åbn siden, og klik på "Help improve this translation". Linket åbner filen
   på GitHub, hvor du kan redigere den i din browser.
2. Ret formuleringerne. Lad links, kode, tal og navne som MeshCore
   stå præcis, som de er.
3. I blokken `translation` øverst ændrer du `status: ai` til
   `status: human`, og så foreslår du ændringen.

Har du fundet et forkert ord, men ingen tid til at rette det? Meld det via
[oversættelsesformularen](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=translation-bug.yml).

## Forbedr en guide {#guides}

Vi skriver guiderne på engelsk først og oversætter dem derfra. Rettelser
og nye emner er velkomne via
[indholdsformularen](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=new-content.yml)
eller en pull request. Oplysninger skal have en kilde: MeshCore-firmwaren og dens
dokumentation, en radiomyndighed eller en producent. Skriv med dine egne ord. Et
kort citat med kilde er i orden.

[Bidragyderguiden](https://github.com/meshcore-europe/meshcore-info.eu/blob/main/CONTRIBUTING.md)
forklarer, hvordan du arbejder på sitet på din egen computer.

## Oversættelsesstatus {#coverage}

"Reviewed" betyder, at en person har kontrolleret
siden; "Machine" betyder maskinoversat og endnu ikke gennemgået;
"Outdated" betyder, at den engelske tekst er ændret, efter oversættelsen blev lavet;
"Missing" betyder, at siden endnu ikke har nogen oversættelse.

{{< coverage >}}

## Tak {#credits}

Sitet er bygget med [Astro](https://astro.build/). Det bruger skrifttyperne
IBM Plex Sans og IBM Plex Mono under SIL Open Font License. Oversættelserne
følger
konventionerne fra [kiekr-i18n](https://github.com/marcelverdult/kiekr-i18n) og
deler dens MeshCore-ordlister. Selve MeshCore udvikles på
[meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore).

Tekst og oversættelser er licenseret under CC BY 4.0, kode under MIT-licensen.
