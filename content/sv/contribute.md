---
title: Bidra
lead: Den här guiden skrivs, granskas och översätts av frivilliga. Så här kan du hjälpa till, med eller utan GitHub-konto.
description: Lägg till din grupp, en enhet eller ett projekt, granska en översättning eller förbättra en guide på meshcore-info.eu.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'f3ed6e9b'
  seeded: '2026-10-31'
  fields: {title: '97b0c61b', lead: 'e9b40d4d', description: '3bd97cd2'}
  sections: ['6e9d4b61', 'aca796d7', 'd4848d5b', '247b2601', '8a60e0d4', '645c82d3', 'c755b654']
  blocks: ['2f9dd6e8', '44167907', 'b020e1a4', 'f2c726cd', '2e9d1fdd', 'b2a902ba', 'b15ce10b', '2be86888', '3db6cb63', '2e3c2fc0', '693a5d9d', '73e33897', '96d8689d', 'c67fd14a', 'f92f7e49', '12ddca6c', 'e947e2a9', '526df4bb', 'e0d3559e']
---

Allt på den här webbplatsen finns i ett öppet
[GitHub-repository](https://github.com/meshcore-europe/meshcore-info.eu). Mindre ändringar
skickar du in via ett formulär på GitHub (ett issue). Större ändringar skickar du som en pull
request: ett förslag på ändringar i filerna, som en ansvarig granskar. En
ansvarig kontrollerar varje ändring innan den publiceras.

Har du inget GitHub-konto? Berätta för oss på [Discord](https://discord.meshcore-info.eu/): en
grupp som saknas, en felaktig uppgift eller en översättning som låter konstig. En frivillig
tar hand om resten.

## Lägg till din grupp {#community}

Driver du en lokal MeshCore-grupp som alla kan gå med i? Fyll i
[gruppformuläret](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-community.yml)
med namn, område och offentliga länkar. När gruppen är tillagd syns den
på sidan [Lokala grupper](/community/) på alla språk.

## Föreslå en enhet eller ett projekt {#device-project}

På [enhetssidan](/devices/) står specifikationer från tillverkarnas
dokumentation. Sidan länkar aldrig till butiker. Föreslå hårdvara med
[enhetsformuläret](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-device.yml).
Har du byggt en app, ett verktyg, en brygga eller en hårdvarudesign för MeshCore med öppen källkod?
Lägg till den med
[projektformuläret](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-project.yml).

## Granska en översättning {#translate}

Sidor på andra språk börjar som maskinöversättningar, och det står högst
upp på sidan. Översättningarna finns i ett eget repository,
[meshcore-info.eu_i18n](https://github.com/meshcore-europe/meshcore-info.eu_i18n), så
du behöver aldrig röra webbplatsens kod. Om du kan något av språken
bra kan du göra översättningen bättre:

1. Öppna sidan och följ länken "Help improve this translation". Den öppnar
   filen på GitHub, där du kan redigera den i webbläsaren.
2. Rätta formuleringarna. Behåll länkar, kod, siffror och namn som MeshCore
   exakt som de är.
3. Ändra `status: ai` till `status: human` i blocket `translation` högst upp,
   och föreslå sedan ändringen.

Har du hittat ett felaktigt ord men saknar tid att rätta det? Rapportera det med
[översättningsformuläret](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=translation-bug.yml).

## Förbättra en guide {#guides}

Guiderna skrivs först på engelska och översätts sedan därifrån. Rättelser
och nya ämnen är välkomna via
[innehållsformuläret](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=new-content.yml)
eller en pull request. Fakta behöver en källa: MeshCore-firmwaren och dess
dokumentation, en radiomyndighet eller en tillverkare. Skriv med egna ord. Ett
kort citat med källa går bra.

I [bidragsguiden](https://github.com/meshcore-europe/meshcore-info.eu/blob/main/CONTRIBUTING.md)
står det hur du arbetar med webbplatsen på din egen dator.

## Översättningsstatus {#coverage}

"Granskad" betyder att en person har kontrollerat
översättningen. "Maskin" betyder maskinöversatt och ännu inte granskad.
"Inaktuell" betyder att den engelska texten har ändrats efter att översättningen gjordes.
"Saknas" betyder att sidan ännu inte har någon översättning.

{{< coverage >}}

## Tack till {#credits}

Webbplatsen är byggd med [Astro](https://astro.build/). Den använder typsnitten
IBM Plex Sans och IBM Plex Mono, under SIL Open Font License. Översättningarna
följer
konventionerna i [kiekr-i18n](https://github.com/marcelverdult/kiekr-i18n) och
delar dess MeshCore-ordlistor. Själva MeshCore utvecklas på
[meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore).

Text och översättningar är licensierade under CC BY 4.0, koden under MIT-licensen.
