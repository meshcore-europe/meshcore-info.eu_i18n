---
title: Meedoen
lead: Vrijwilligers schrijven, controleren en vertalen deze gids. Zo help je mee, met of zonder GitHub-account.
description: Voeg je community, een apparaat of een project toe, controleer een vertaling of verbeter een gids op meshcore-info.eu.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'f3ed6e9b'
  seeded: '2026-10-31'
  fields: {title: '97b0c61b', lead: 'e9b40d4d', description: '3bd97cd2'}
  sections: ['6e9d4b61', 'aca796d7', 'd4848d5b', '247b2601', '8a60e0d4', '645c82d3', 'c755b654']
  blocks: ['2f9dd6e8', '44167907', 'b020e1a4', 'f2c726cd', '2e9d1fdd', 'b2a902ba', 'b15ce10b', '2be86888', '3db6cb63', '2e3c2fc0', '693a5d9d', '73e33897', '96d8689d', 'c67fd14a', 'f92f7e49', '12ddca6c', 'e947e2a9', '526df4bb', 'e0d3559e']
---

Alles op deze site staat in een openbare
[GitHub-repository](https://github.com/meshcore-europe/meshcore-info.eu). Kleine wijzigingen
gaan via een formulier op GitHub (een issue). Grotere wijzigingen dien je in als pull
request: een voorstel voor een wijziging in de bestanden, dat een beheerder beoordeelt. Een
beheerder controleert elke wijziging voordat die online komt.

Geen GitHub-account? Laat het ons weten op [Discord](https://discord.meshcore-info.eu/): een
ontbrekende groep, een onjuist feit of een vertaling die raar klinkt. Een vrijwilliger
pakt het daarna op.

## Voeg je community toe {#community}

Heb je een lokale MeshCore-groep waar iedereen lid van kan worden? Vul dan het
[communityformulier](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-community.yml)
in met de naam, het gebied en de openbare links. Zodra je groep is toegevoegd, staat die
in elke taal op de pagina [Lokale groepen](/community/).

## Stel een apparaat of een project voor {#device-project}

Op de [apparatenpagina](/devices/) staan specificaties uit de documentatie van fabrikanten. Die pagina linkt nooit naar winkels. Stel hardware voor met het
[apparaatformulier](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-device.yml).
Heb je voor MeshCore een app, tool, bridge of hardwareontwerp met openbare broncode gemaakt? Voeg het toe met het
[projectformulier](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-project.yml).

## Controleer een vertaling {#translate}

Pagina's in andere talen beginnen als machinevertaling en dat staat er bovenaan bij. De vertalingen staan in een eigen repository,
[meshcore-info.eu_i18n](https://github.com/meshcore-europe/meshcore-info.eu_i18n). Je hoeft de code van de site dus nooit aan te raken. Spreek je een van de talen goed? Dan kun je de vertaling verbeteren:

1. Open de pagina en klik op "Help improve this translation". Je komt dan bij
   het bestand op GitHub, waar je het in je browser kunt bewerken.
2. Verbeter de tekst. Laat links, code, getallen en namen als MeshCore
   precies staan zoals ze zijn.
3. Verander in het `translation`-blok bovenaan `status: ai` in
   `status: human` en stel de wijziging voor.

Zie je een verkeerd woord maar heb je geen tijd om het te verbeteren? Meld het met het
[vertaalformulier](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=translation-bug.yml).

## Verbeter een gids {#guides}

De gidsen schrijven we eerst in het Engels en vertalen we daarna. Correcties
en nieuwe onderwerpen zijn welkom via het
[inhoudsformulier](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=new-content.yml)
of een pull request. Bij feiten hoort een bron: de MeshCore-firmware en de documentatie daarvan, een radiotoezichthouder of een fabrikant. Schrijf in je eigen woorden. Een
kort citaat met bron mag.

In de [handleiding voor bijdragers](https://github.com/meshcore-europe/meshcore-info.eu/blob/main/CONTRIBUTING.md)
lees je hoe je op je eigen computer aan de site werkt.

## Status van de vertalingen {#coverage}

"Reviewed" betekent dat een persoon de pagina heeft gecontroleerd. "Machine" betekent machinaal vertaald en nog niet gecontroleerd.
"Outdated" betekent dat de Engelse tekst is veranderd nadat de vertaling is gemaakt.
"Missing" betekent dat de pagina nog geen vertaling heeft.

{{< coverage >}}

## Met dank aan {#credits}

De site is gebouwd met [Astro](https://astro.build/). Hij gebruikt de lettertypen
IBM Plex Sans en IBM Plex Mono, onder de SIL Open Font License. De vertalingen
volgen de
afspraken van [kiekr-i18n](https://github.com/marcelverdult/kiekr-i18n) en
gebruiken dezelfde MeshCore-woordenlijsten. MeshCore zelf wordt ontwikkeld op
[meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore).

Tekst en vertalingen vallen onder de licentie CC BY 4.0, code onder de MIT-licentie.
