---
title: Bidra
lead: Frivillige skriver, sjekker og oversetter denne guiden. Slik kan du hjelpe til, med eller uten GitHub-konto.
description: Legg til gruppen din, en enhet eller et prosjekt, gå gjennom en oversettelse eller forbedre en guide på meshcore-info.eu.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'f3ed6e9b'
  seeded: '2026-10-31'
  fields: {title: '97b0c61b', lead: 'e9b40d4d', description: '3bd97cd2'}
  sections: ['6e9d4b61', 'aca796d7', 'd4848d5b', '247b2601', '8a60e0d4', '645c82d3', 'c755b654']
  blocks: ['2f9dd6e8', '44167907', 'b020e1a4', 'f2c726cd', '2e9d1fdd', 'b2a902ba', 'b15ce10b', '2be86888', '3db6cb63', '2e3c2fc0', '693a5d9d', '73e33897', '96d8689d', 'c67fd14a', 'f92f7e49', '12ddca6c', 'e947e2a9', '526df4bb', 'e0d3559e']
---

Alt på dette nettstedet ligger i et offentlig
[GitHub-repository](https://github.com/meshcore-europe/meshcore-info.eu). Små endringer
sender du inn via et skjema på GitHub (en issue). Større endringer sender du inn som en pull
request: et forslag til endring i filene, som en vedlikeholder går gjennom. En
vedlikeholder sjekker hver endring før den blir publisert.

Har du ikke GitHub-konto? Si fra på [Discord](https://discord.meshcore-info.eu/): en
gruppe som mangler, en opplysning som er feil eller en oversettelse som høres rar ut. En frivillig
tar det derfra.

## Legg til gruppen din {#community}

Driver du en lokal MeshCore-gruppe som alle kan bli med i? Fyll ut
[gruppeskjemaet](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-community.yml)
med navn, område og offentlige lenker. Når gruppen er lagt til, vises den
på siden [Lokale grupper](/community/) på alle språk.

## Foreslå en enhet eller et prosjekt {#device-project}

[Enhetssiden](/devices/) viser spesifikasjoner fra produsentenes
dokumentasjon og lenker aldri til butikker. Foreslå maskinvare med
[enhetsskjemaet](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-device.yml).
Har du laget en app, et verktøy, en bro eller et maskinvaredesign for MeshCore med åpen kildekode?
Legg det til med
[prosjektskjemaet](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-project.yml).

## Gå gjennom en oversettelse {#translate}

Sider på andre språk starter som maskinoversettelser, og det står øverst på siden.
Oversettelsene ligger i et eget repository,
[meshcore-info.eu_i18n](https://github.com/meshcore-europe/meshcore-info.eu_i18n), så
du trenger aldri å røre koden til nettstedet. Snakker du et av språkene
godt, kan du gjøre oversettelsen bedre:

1. Åpne siden og klikk på «Hjelp til å forbedre denne oversettelsen». Da åpnes
   filen på GitHub, og du kan redigere den i nettleseren.
2. Rett opp formuleringene. Behold lenker, kode, tall og navn som MeshCore
   nøyaktig som de er.
3. I `translation`-blokken øverst endrer du `status: ai` til
   `status: human`. Deretter foreslår du endringen.

Har du funnet et feil ord, men ikke tid til å rette det? Meld fra med
[oversettelsesskjemaet](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=translation-bug.yml).

## Forbedre en guide {#guides}

Vi skriver guidene på engelsk først og oversetter dem derfra. Rettelser
og nye temaer tar vi gjerne imot via
[innholdsskjemaet](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=new-content.yml)
eller en pull request. Fakta trenger en kilde: MeshCore-firmwaren og dokumentasjonen til den,
en radiomyndighet eller en produsent. Skriv med egne ord. Et
kort sitat med kilde er greit.

[Bidragsguiden](https://github.com/meshcore-europe/meshcore-info.eu/blob/main/CONTRIBUTING.md)
forklarer hvordan du jobber med nettstedet på din egen datamaskin.

## Status for oversettelser {#coverage}

«Gjennomgått» betyr at en person har sjekket siden. «Maskin» betyr maskinoversatt og ikke gjennomgått ennå.
«Utdatert» betyr at den engelske teksten er endret etter at oversettelsen ble laget.
«Mangler» betyr at siden ikke har noen oversettelse ennå.

{{< coverage >}}

## Takk til {#credits}

Nettstedet er bygget med [Astro](https://astro.build/). Det bruker skrifttypene
IBM Plex Sans og IBM Plex Mono, under SIL Open Font License. Oversettelsene
følger
konvensjonene til [kiekr-i18n](https://github.com/marcelverdult/kiekr-i18n) og
bruker de samme MeshCore-ordlistene. Selve MeshCore utvikles i
[meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore).

Tekst og oversettelser er lisensiert under CC BY 4.0, koden under MIT-lisensen.
