---
title: Col·labora
lead: Aquesta guia l'escriuen, la comproven i la tradueixen persones voluntàries. T'expliquem com pots ajudar, amb un compte de GitHub o sense.
description: Afegeix la teva comunitat, un dispositiu o un projecte, revisa una traducció o millora una guia de meshcore-info.eu.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'f3ed6e9b'
  seeded: '2026-11-02'
  fields: {title: '97b0c61b', lead: 'e9b40d4d', description: '3bd97cd2'}
  sections: ['6e9d4b61', 'aca796d7', 'd4848d5b', '247b2601', '8a60e0d4', '645c82d3', 'c755b654']
  blocks: ['2f9dd6e8', '44167907', 'b020e1a4', 'f2c726cd', '2e9d1fdd', 'b2a902ba', 'b15ce10b', '2be86888', '3db6cb63', '2e3c2fc0', '693a5d9d', '73e33897', '96d8689d', 'c67fd14a', 'f92f7e49', '12ddca6c', 'e947e2a9', '526df4bb', 'e0d3559e']
---

Tot el contingut d'aquest lloc és en un
[repositori públic de GitHub](https://github.com/meshcore-europe/meshcore-info.eu). Els canvis petits
es fan amb un formulari de GitHub (una issue). Els més grans es fan amb una pull
request: una proposta de canvi als fitxers que revisa una persona responsable del lloc. Una
persona responsable comprova cada canvi abans que es publiqui.

No tens compte de GitHub? Explica'ns-ho a [Discord](https://discord.meshcore-info.eu/): un
grup que falta, una dada errònia o una traducció que sona estranya. Una persona voluntària
se n'encarregarà.

## Afegeix la teva comunitat {#community}

Portes un grup local de MeshCore obert a tothom? Omple el
[formulari de comunitat](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-community.yml)
amb el nom, la zona i els enllaços públics. Un cop afegit, el teu grup apareixerà
a la pàgina [Grups locals](/community/) en tots els idiomes.

## Proposa un dispositiu o un projecte {#device-project}

A la [pàgina de dispositius](/devices/) hi ha especificacions tretes de la documentació dels fabricants,
i no hi ha mai enllaços a botigues. Per proposar maquinari, fes servir el
[formulari de dispositius](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-device.yml).
Has creat una aplicació, una eina, un pont o un disseny de maquinari per a MeshCore amb codi font públic? Afegeix-lo amb el
[formulari de projectes](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-project.yml).

## Revisa una traducció {#translate}

Les pàgines en altres idiomes comencen com a traduccions automàtiques i ho indiquen a dalt de tot.
Les traduccions són en un repositori propi,
[meshcore-info.eu_i18n](https://github.com/meshcore-europe/meshcore-info.eu_i18n), així que
no has de tocar mai el codi del lloc. Si domines algun d'aquests idiomes,
pots millorar-ne la traducció:

1. Obre la pàgina i segueix l'enllaç "Ajuda a millorar aquesta traducció". S'obrirà el
   fitxer a GitHub, on el pots editar des del navegador.
2. Corregeix el text. Deixa els enllaços, el codi, els números i els noms com MeshCore
   exactament tal com són.
3. Al bloc `translation` de la part superior, canvia `status: ai` per
   `status: human` i proposa el canvi.

Has trobat una paraula incorrecta però no tens temps de corregir-la? Informa'n amb el
[formulari de traducció](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=translation-bug.yml).

## Millora una guia {#guides}

Escrivim les guies primer en anglès i les traduïm a partir d'aquesta versió. Pots enviar correccions
i temes nous amb el
[formulari de contingut](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=new-content.yml)
o amb una pull request. Les dades han de tenir una font: el firmware de MeshCore i la seva
documentació, un regulador de ràdio o un fabricant. Escriu amb les teves paraules. Pots
incloure una cita breu amb la font.

La [guia per a col·laboradors](https://github.com/meshcore-europe/meshcore-info.eu/blob/main/CONTRIBUTING.md)
explica com treballar en el lloc des del teu ordinador.

## Estat de les traduccions {#coverage}

"Revisada" vol dir que l'ha comprovada
una persona; "Automàtica" vol dir que és una traducció automàtica encara sense revisar;
"Desfasada" vol dir que el text anglès ha canviat després de fer la traducció;
"Falta" vol dir que la pàgina encara no té traducció.

{{< coverage >}}

## Crèdits {#credits}

El lloc està fet amb [Astro](https://astro.build/). Fa servir les tipografies
IBM Plex Sans i IBM Plex Mono, amb la llicència SIL Open Font License. Les traduccions
segueixen les
convencions de [kiekr-i18n](https://github.com/marcelverdult/kiekr-i18n) i
en comparteixen els glossaris de MeshCore. El desenvolupament de MeshCore es fa a
[meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore).

Els textos i les traduccions tenen llicència CC BY 4.0, i el codi, llicència
MIT.
