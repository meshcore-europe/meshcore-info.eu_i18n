---
title: Meedoen
lead: Vrijwilligers schrijven, controleren en vertalen deze gids. Zo help je mee, met of zonder GitHub-account.
description: Voeg je community, een apparaat of een project toe, controleer een vertaling of verbeter een gids op meshcore-info.eu.
translation:
  status: human
  source_hash: 'f3ed6e9b'
  seeded: '2026-10-26'
---

Alles op deze site staat in een openbare
[GitHub-repository](https://github.com/meshcore-europe/meshcore-info.eu). Kleine wijzigingen
dien je in via een formulier op GitHub (een issue). Grotere wijzigingen gaan als pull
request: een voorgestelde wijziging in de bestanden die een beheerder beoordeelt. Een
beheerder controleert elke wijziging voordat die online gaat.

Geen GitHub-account? Laat het ons weten op [Discord](https://discord.meshcore-info.eu/): een
ontbrekende groep, een fout feit of een vertaling die vreemd leest. Een vrijwilliger
pakt het daarna op.

## Voeg je community toe {#community}

Beheer je een lokale MeshCore-groep waar iedereen bij kan? Vul het
[communityformulier](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-community.yml)
in met de naam, het gebied en de openbare links. Na toevoeging verschijnt je groep
op de pagina [Lokale groepen](/community/) in elke taal.

## Stel een apparaat of een project voor {#device-project}

De [apparatenpagina](/devices/) toont specificaties uit de documentatie van fabrikanten
en linkt nooit naar winkels. Stel hardware voor met het
[apparaatformulier](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-device.yml).
Heb je een app, tool, bridge of hardwareontwerp voor MeshCore gemaakt met openbare broncode?
Voeg het toe met het
[projectformulier](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-project.yml).

## Controleer een vertaling {#translate}

Pagina's in andere talen beginnen als machinevertaling en vermelden dat bovenaan.
Vertalingen staan in een eigen repository,
[meshcore-info.eu_i18n](https://github.com/meshcore-europe/meshcore-info.eu_i18n), dus
je hoeft nooit aan de code van de site te komen. Spreek je een van die talen
goed, dan kun je de vertaling verbeteren:

1. Open de pagina en volg "Help deze vertaling te verbeteren". Daarmee open je het
   bestand op GitHub, waar je het in je browser kunt bewerken.
2. Verbeter de formulering. Laat links, code, getallen en namen zoals MeshCore
   precies zoals ze zijn.
3. Wijzig in het blok `translation` bovenaan `status: ai` in
   `status: human` en stel de wijziging voor.

Een fout woord gevonden, maar geen tijd om het te verbeteren? Meld het met het
[vertaalformulier](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=translation-bug.yml).

## Verbeter een gids {#guides}

Gidsen schrijven we eerst in het Engels en vertalen we daarna. Correcties
en nieuwe onderwerpen zijn welkom via het
[inhoudformulier](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=new-content.yml)
of een pull request. Feiten hebben een bron nodig: de MeshCore-firmware en de
documentatie ervan, een radiotoezichthouder of een fabrikant. Schrijf in je eigen woorden. Een
kort citaat met bronvermelding mag.

De [bijdragegids](https://github.com/meshcore-europe/meshcore-info.eu/blob/main/CONTRIBUTING.md)
legt uit hoe je op je eigen computer aan de site werkt.

## Vertaalstatus {#coverage}

"Gecontroleerd" betekent nagekeken
door een persoon; "Machine" betekent machinaal vertaald en nog niet nagekeken;
"Verouderd" betekent dat de Engelse tekst is gewijzigd nadat de vertaling is gemaakt;
"Ontbreekt" betekent dat de pagina nog geen vertaling heeft.

{{< coverage >}}

## Credits {#credits}

De site is gebouwd met [Astro](https://astro.build/). Hij gebruikt de lettertypen
IBM Plex Sans en IBM Plex Mono, onder de SIL Open Font License. Vertalingen
volgen de
conventies van [kiekr-i18n](https://github.com/marcelverdult/kiekr-i18n) en
delen de MeshCore-woordenlijsten daarvan. MeshCore zelf wordt ontwikkeld op
[meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore).

Tekst en vertalingen vallen onder de licentie CC BY 4.0, code onder de MIT-licentie.
