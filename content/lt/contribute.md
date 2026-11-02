---
title: Prisidėk
lead: Šį vadovą rašo, tikrina ir verčia savanoriai. Štai kaip gali padėti, su GitHub paskyra ar be jos.
description: Pridėk savo bendruomenę, įrenginį ar projektą, peržiūrėk vertimą arba patobulink vadovą svetainėje meshcore-info.eu.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'f3ed6e9b'
  seeded: '2026-11-02'
  fields: {title: '97b0c61b', lead: 'e9b40d4d', description: '3bd97cd2'}
  sections: ['6e9d4b61', 'aca796d7', 'd4848d5b', '247b2601', '8a60e0d4', '645c82d3', 'c755b654']
  blocks: ['2f9dd6e8', '44167907', 'b020e1a4', 'f2c726cd', '2e9d1fdd', 'b2a902ba', 'b15ce10b', '2be86888', '3db6cb63', '2e3c2fc0', '693a5d9d', '73e33897', '96d8689d', 'c67fd14a', 'f92f7e49', '12ddca6c', 'e947e2a9', '526df4bb', 'e0d3559e']
---

Visas šios svetainės turinys yra viešoje
[GitHub saugykloje](https://github.com/meshcore-europe/meshcore-info.eu). Smulkius pakeitimus
siūlai per GitHub formą (issue). Didesnius pateiki kaip pull request: tai failų
pakeitimo pasiūlymas, kurį peržiūri prižiūrėtojas. Prižiūrėtojas patikrina kiekvieną
pakeitimą prieš jį paskelbiant.

Neturi GitHub paskyros? Parašyk mums per [Discord](https://discord.meshcore-info.eu/): trūkstama
grupė, klaidingas faktas ar keistai skambantis vertimas. Toliau tuo pasirūpins
savanoris.

## Pridėk savo bendruomenę {#community}

Vadovauji vietinei MeshCore grupei, prie kurios gali prisijungti bet kas? Užpildyk
[bendruomenės formą](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-community.yml):
nurodyk pavadinimą, vietovę ir viešas nuorodas. Kai grupę pridėsime, ji bus rodoma
[vietinių grupių](/community/) puslapyje visomis kalbomis.

## Pasiūlyk įrenginį ar projektą {#device-project}

[Įrenginių puslapyje](/devices/) pateikiame specifikacijas iš gamintojų dokumentacijos
ir niekada nededame nuorodų į parduotuves. Įrangą gali pasiūlyti per
[įrenginio formą](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-device.yml).
Sukūrei MeshCore programėlę, įrankį, tiltą ar aparatinės įrangos projektą su viešu
išeities kodu? Pridėk jį per
[projekto formą](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-project.yml).

## Peržiūrėk vertimą {#translate}

Puslapius kitomis kalbomis iš pradžių išverčia mašina, ir tai nurodyta jų viršuje.
Vertimai laikomi atskiroje saugykloje,
[meshcore-info.eu_i18n](https://github.com/meshcore-europe/meshcore-info.eu_i18n), todėl
svetainės kodo tau liesti niekada neprireiks. Jei gerai moki kurią nors iš šių kalbų,
gali vertimą patobulinti:

1. Atidaryk puslapį ir spustelėk „Padėk patobulinti šį vertimą“. Failas atsidarys
   GitHub, kur galėsi jį redaguoti naršyklėje.
2. Pataisyk formuluotes. Nuorodas, kodą, skaičius ir pavadinimus, tokius kaip MeshCore,
   palik tiksliai tokius, kokie yra.
3. Viršuje esančiame `translation` bloke pakeisk `status: ai` į
   `status: human` ir pasiūlyk pakeitimą.

Radai netinkamą žodį, bet neturi laiko jo taisyti? Apie jį gali pranešti per
[vertimo formą](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=translation-bug.yml).

## Patobulink vadovą {#guides}

Vadovus pirmiausia rašome anglų kalba, o iš jos verčiame į kitas. Pataisymų ir naujų
temų laukiame per
[turinio formą](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=new-content.yml)
arba per pull request. Faktams reikia šaltinio: MeshCore programinė aparatinė įranga
ir jos dokumentacija, radijo ryšio reguliuotojas arba gamintojas. Rašyk savais žodžiais.
Trumpą citatą su šaltiniu naudoti galima.

[Prisidedančiųjų vadove](https://github.com/meshcore-europe/meshcore-info.eu/blob/main/CONTRIBUTING.md)
paaiškinta, kaip dirbti su svetaine savo kompiuteryje.

## Vertimų būsena {#coverage}

„Peržiūrėta“ reiškia, kad vertimą patikrino žmogus; „Mašininis“ reiškia, kad puslapį
išvertė mašina ir jo dar niekas nepatikrino; „Pasenęs“ reiškia, kad angliškas tekstas
pasikeitė jau po vertimo; „Nėra“ reiškia, kad puslapis dar neišverstas.

{{< coverage >}}

## Padėkos {#credits}

Svetainė sukurta naudojant [Astro](https://astro.build/). Joje naudojami šriftai
IBM Plex Sans ir IBM Plex Mono pagal SIL Open Font License licenciją. Vertimuose
laikomasi [kiekr-i18n](https://github.com/marcelverdult/kiekr-i18n) konvencijų ir
naudojami tie patys MeshCore žodynai. Patis MeshCore kuriamas saugykloje
[meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore).

Tekstui ir vertimams taikoma CC BY 4.0 licencija, kodui taikoma MIT
licencija.
