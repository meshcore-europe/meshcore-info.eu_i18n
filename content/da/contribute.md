---
title: Bidrag
lead: Denne guide bliver skrevet, kontrolleret og oversat af frivillige. Her kan du se, hvordan du hjælper, med eller uden en GitHub-konto.
description: Tilføj dit fællesskab, en enhed eller et projekt, gennemgå en oversættelse eller forbedr en guide på meshcore-info.eu.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: 'f3ed6e9b'
  seeded: '2026-10-26'
  fields: {title: '97b0c61b', lead: 'e9b40d4d', description: '3bd97cd2'}
  sections: ['6e9d4b61', 'aca796d7', 'd4848d5b', '247b2601', '8a60e0d4', '645c82d3', 'c755b654']
---

Alt på dette site ligger i et offentligt
[GitHub-repository](https://github.com/meshcore-europe/meshcore-info.eu). Små ændringer
sender du ind via en formular på GitHub (et issue). Alt større kommer ind som en pull
request: et forslag til ændring af filerne, som en vedligeholder gennemgår. En
vedligeholder kontrollerer hver ændring, før den går live.

Har du ingen GitHub-konto? Sig til på [Discord](https://discord.meshcore-info.eu/): en
gruppe, der mangler, en forkert oplysning eller en oversættelse, der lyder underligt. En frivillig
tager den derfra.

## Tilføj dit fællesskab {#community}

Driver du en lokal MeshCore-gruppe, som alle kan være med i? Udfyld
[fællesskabsformularen](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-community.yml)
med navn, område og de offentlige links. Når gruppen er tilføjet, vises den
på siden [Lokale grupper](/community/) på alle sprog.

## Foreslå en enhed eller et projekt {#device-project}

[Enhedssiden](/devices/) viser specifikationer fra producenternes
dokumentation og linker aldrig til butikker. Foreslå hardware med
[enhedsformularen](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-device.yml).
Har du lavet en app, et værktøj, en bro eller et hardwaredesign til MeshCore med offentlig
kildekode? Tilføj det med
[projektformularen](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-project.yml).

## Gennemgå en oversættelse {#translate}

Sider på andre sprog starter som maskinoversættelser og oplyser det øverst
på siden. Oversættelserne ligger i deres eget repository,
[meshcore-info.eu_i18n](https://github.com/meshcore-europe/meshcore-info.eu_i18n), så
du behøver aldrig at røre sitets kode. Taler du et af sprogene
godt, kan du gøre oversættelsen bedre:

1. Åbn siden, og følg "Hjælp med at forbedre denne oversættelse". Linket åbner
   filen på GitHub, hvor du kan redigere den i din browser.
2. Ret formuleringerne. Lad links, kode, tal og navne som MeshCore
   stå præcis, som de er.
3. Skift `status: ai` til `status: human` i blokken `translation` øverst,
   og send ændringen som forslag.

Har du fundet et forkert ord, men ikke tid til at rette det? Meld det med
[oversættelsesformularen](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=translation-bug.yml).

## Forbedr en guide {#guides}

Guiderne bliver skrevet på engelsk først og oversat derfra. Rettelser
og nye emner er velkomne via
[indholdsformularen](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=new-content.yml)
eller en pull request. Fakta kræver en kilde: MeshCore-firmwaren og dens
dokumentation, en radiomyndighed eller en producent. Skriv med dine egne ord. Et
kort citat med kildeangivelse er i orden.

[Bidragsguiden](https://github.com/meshcore-europe/meshcore-info.eu/blob/main/CONTRIBUTING.md)
forklarer, hvordan du arbejder på sitet på din egen computer.

## Oversættelsesstatus {#coverage}

"Gennemgået" betyder kontrolleret
af en person; "Maskine" betyder maskinoversat og endnu ikke gennemgået;
"Forældet" betyder, at den engelske tekst er ændret, efter oversættelsen blev lavet;
"Mangler" betyder, at siden endnu ikke har nogen oversættelse.

{{< coverage >}}

## Tak til {#credits}

Sitet er bygget med [Astro](https://astro.build/). Det bruger skrifttyperne
IBM Plex Sans og IBM Plex Mono under SIL Open Font License. Oversættelserne
følger
konventionerne fra [kiekr-i18n](https://github.com/marcelverdult/kiekr-i18n) og
deler dets MeshCore-ordlister. MeshCore selv bliver udviklet på
[meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore).

Tekst og oversættelser er udgivet under CC BY 4.0, kode under MIT-licensen.
