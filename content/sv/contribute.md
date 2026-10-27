---
title: Bidra
lead: Den här guiden skrivs, granskas och översätts av frivilliga. Så här hjälper du till, med eller utan GitHub-konto.
description: Lägg till din community, en enhet eller ett projekt, granska en översättning eller förbättra en guide på meshcore-info.eu.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: 'f3ed6e9b'
  seeded: '2026-10-26'
  fields: {title: '97b0c61b', lead: 'e9b40d4d', description: '3bd97cd2'}
  sections: ['6e9d4b61', 'aca796d7', 'd4848d5b', '247b2601', '8a60e0d4', '645c82d3', 'c755b654']
---

Allt på den här webbplatsen finns i ett publikt
[GitHub-repositorium](https://github.com/meshcore-europe/meshcore-info.eu). Små ändringar
skickar du via ett formulär på GitHub (en issue). Större ändringar skickar du som en pull
request: ett ändringsförslag till filerna som en underhållare granskar. En
underhållare kontrollerar varje ändring innan den publiceras.

Har du inget GitHub-konto? Berätta för oss på [Discord](https://discord.meshcore-info.eu/): en
grupp som saknas, ett fel i texten eller en översättning som låter konstig. En frivillig
tar det vidare därifrån.

## Lägg till din community {#community}

Driver du en lokal MeshCore-grupp som vem som helst kan gå med i? Fyll i
[community-formuläret](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-community.yml)
med namn, område och publika länkar. När gruppen har lagts till visas den
på sidan [Lokala grupper](/community/) på alla språk.

## Föreslå en enhet eller ett projekt {#device-project}

[Enhetssidan](/devices/) listar specifikationer från tillverkarnas
dokumentation och länkar aldrig till butiker. Föreslå hårdvara med
[enhetsformuläret](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-device.yml).
Har du byggt en app, ett verktyg, en brygga eller en hårdvarudesign för MeshCore med öppen
källkod? Lägg till det med
[projektformuläret](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-project.yml).

## Granska en översättning {#translate}

Sidor på andra språk börjar som maskinöversättningar och säger det
överst på sidan. Översättningarna finns i ett eget repositorium,
[meshcore-info.eu_i18n](https://github.com/meshcore-europe/meshcore-info.eu_i18n), så
du behöver aldrig röra webbplatsens kod. Om du behärskar ett av språken
väl kan du förbättra översättningen:

1. Öppna sidan och följ "Hjälp till att förbättra den här översättningen". Då öppnas
   filen på GitHub, där du kan redigera den i webbläsaren.
2. Rätta formuleringarna. Låt länkar, kod, siffror och namn som MeshCore
   stå kvar exakt som de är.
3. Ändra `status: ai` till `status: human` i blocket `translation`
   överst, och föreslå ändringen.

Har du hittat ett felaktigt ord men saknar tid att rätta det? Rapportera det med
[översättningsformuläret](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=translation-bug.yml).

## Förbättra en guide {#guides}

Guiderna skrivs först på engelska och översätts därifrån. Rättelser
och nya ämnen är välkomna via
[innehållsformuläret](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=new-content.yml)
eller en pull request. Fakta behöver en källa: MeshCores firmware och dess
dokumentation, en radiomyndighet eller en tillverkare. Skriv med egna ord. Ett
kort citat med källa går bra.

[Bidragsguiden](https://github.com/meshcore-europe/meshcore-info.eu/blob/main/CONTRIBUTING.md)
förklarar hur du arbetar med webbplatsen på din egen dator.

## Översättningsstatus {#coverage}

"Granskad" betyder att en person har kontrollerat sidan;
"Maskin" betyder maskinöversatt och ännu inte granskad;
"Föråldrad" betyder att den engelska texten har ändrats efter att översättningen gjordes;
"Saknas" betyder att sidan ännu inte har någon översättning.

{{< coverage >}}

## Tack till {#credits}

Webbplatsen är byggd med [Astro](https://astro.build/). Den använder typsnitten
IBM Plex Sans och IBM Plex Mono under SIL Open Font License. Översättningarna
följer
konventionerna i [kiekr-i18n](https://github.com/marcelverdult/kiekr-i18n) och
delar dess MeshCore-ordlistor. MeshCore självt utvecklas på
[meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore).

Text och översättningar är licensierade under CC BY 4.0, koden under MIT-licensen.
