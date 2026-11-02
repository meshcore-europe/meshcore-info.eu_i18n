---
title: Piedalies
lead: Šo ceļvedi raksta, pārbauda un tulko brīvprātīgie. Lūk, kā vari palīdzēt, ar GitHub kontu vai bez tā.
description: Pievieno savu kopienu, ierīci vai projektu, pārskati tulkojumu vai uzlabo kādu ceļvedi vietnē meshcore-info.eu.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'f3ed6e9b'
  seeded: '2026-11-02'
  fields: {title: '97b0c61b', lead: 'e9b40d4d', description: '3bd97cd2'}
  sections: ['6e9d4b61', 'aca796d7', 'd4848d5b', '247b2601', '8a60e0d4', '645c82d3', 'c755b654']
  blocks: ['2f9dd6e8', '44167907', 'b020e1a4', 'f2c726cd', '2e9d1fdd', 'b2a902ba', 'b15ce10b', '2be86888', '3db6cb63', '2e3c2fc0', '693a5d9d', '73e33897', '96d8689d', 'c67fd14a', 'f92f7e49', '12ddca6c', 'e947e2a9', '526df4bb', 'e0d3559e']
---

Viss šīs vietnes saturs atrodas publiskā
[GitHub repozitorijā](https://github.com/meshcore-europe/meshcore-info.eu). Nelielas izmaiņas
iesniedz ar GitHub veidlapu (issue). Lielākas izmaiņas iesniedz kā pull
request: tas ir failu izmaiņu priekšlikums, ko izskata uzturētājs. Uzturētājs
pārbauda visas izmaiņas, pirms tās parādās vietnē.

Nav GitHub konta? Pastāsti mums [Discord](https://discord.meshcore-info.eu/) par
trūkstošu grupu, kļūdainu faktu vai tulkojumu, kas skan dīvaini. Tālāk par to
parūpēsies kāds brīvprātīgais.

## Pievieno savu kopienu {#community}

Vadi vietējo MeshCore grupu, kurai var pievienoties ikviens? Aizpildi
[kopienas veidlapu](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-community.yml)
un norādi nosaukumu, apgabalu un publiskās saites. Kad grupa būs pievienota, tā parādīsies
lapā [Vietējās grupas](/community/) visās valodās.

## Iesaki ierīci vai projektu {#device-project}

[Ierīču lapā](/devices/) ir specifikācijas no ražotāju dokumentācijas, un tajā nekad nav
saišu uz veikaliem. Aparatūru iesaki ar
[ierīces veidlapu](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-device.yml).
Izveidoji MeshCore lietotni, rīku, tiltu vai aparatūras dizainu ar publisku pirmkodu?
Pievieno to ar
[projekta veidlapu](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-project.yml).

## Pārskati tulkojumu {#translate}

Lapas citās valodās sākumā ir mašīntulkojumi, un to augšdaļā tas ir norādīts.
Tulkojumi atrodas atsevišķā repozitorijā,
[meshcore-info.eu_i18n](https://github.com/meshcore-europe/meshcore-info.eu_i18n), tāpēc
vietnes kodam tev nekad nav jāpieskaras. Ja labi proti kādu no šīm valodām, vari tulkojumu
uzlabot:

1. Atver lapu un izvēlies saiti "Palīdzi uzlabot šo tulkojumu". Saite atver failu GitHub,
   kur to vari rediģēt pārlūkā.
2. Izlabo formulējumu. Saites, kodu, skaitļus un nosaukumus, piemēram, MeshCore,
   atstāj tieši tādus, kādi tie ir.
3. Augšā esošajā blokā `translation` nomaini `status: ai` uz
   `status: human` un iesniedz izmaiņu priekšlikumu.

Atradi nepareizu vārdu, bet nav laika to labot? Ziņo par to ar
[tulkojuma veidlapu](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=translation-bug.yml).

## Uzlabo ceļvedi {#guides}

Ceļvežus vispirms raksta angļu valodā un pēc tam tulko no tās. Labprāt saņemam labojumus
un jaunas tēmas ar
[satura veidlapu](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=new-content.yml)
vai pull request. Faktiem vajadzīgs avots: MeshCore programmaparatūra un tās dokumentācija,
radio regulators vai ražotājs. Raksti saviem vārdiem. Īss citāts ar avota norādi ir
pieļaujams.

[Līdzdalības ceļvedī](https://github.com/meshcore-europe/meshcore-info.eu/blob/main/CONTRIBUTING.md)
ir aprakstīts, kā strādāt pie vietnes savā datorā.

## Tulkojumu statuss {#coverage}

"Pārskatīts" nozīmē, ka tulkojumu pārbaudījis cilvēks; "Mašīntulkojums" nozīmē, ka
tulkojumu veidojusi mašīna un neviens to vēl nav pārskatījis; "Novecojis" nozīmē, ka
angļu teksts mainījies pēc tulkojuma izveides; "Trūkst" nozīmē, ka lapai vēl nav tulkojuma.

{{< coverage >}}

## Pateicības {#credits}

Vietne ir veidota ar [Astro](https://astro.build/). Tajā izmantoti burtveidoli
IBM Plex Sans un IBM Plex Mono ar SIL Open Font License licenci. Tulkojumos ievērotas
[kiekr-i18n](https://github.com/marcelverdult/kiekr-i18n) konvencijas un izmantoti
tā MeshCore glosāriji. Pašu MeshCore izstrādā repozitorijā
[meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore).

Tekstam un tulkojumiem ir CC BY 4.0 licence, kodam MIT licence.
