---
title: Doprinesi
lead: Ovaj vodič pišu, provjeravaju i prevode volonteri. Evo kako možeš pomoći, s GitHub računom ili bez njega.
description: Dodaj svoju zajednicu, uređaj ili projekt, pregledaj prijevod ili poboljšaj vodič na meshcore-info.eu.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '1a28f66a'
  seeded: '2026-11-10'
  fields: {title: '97b0c61b', lead: 'e9b40d4d', description: '3bd97cd2'}
  sections: ['6e9d4b61', 'aca796d7', 'd4848d5b', '247b2601', '4b12bb2c', '645c82d3', 'c755b654']
  blocks: ['2f9dd6e8', '44167907', 'b020e1a4', 'f2c726cd', '2e9d1fdd', 'b2a902ba', 'b15ce10b', '2be86888', '3db6cb63', '2e3c2fc0', '693a5d9d', '8aa01985', '96d8689d', 'c67fd14a', 'f92f7e49', '12ddca6c', 'e947e2a9', '526df4bb', 'e0d3559e']
---

Sav sadržaj ove stranice nalazi se u javnom
[GitHub repozitoriju](https://github.com/meshcore-europe/meshcore-info.eu). Za male izmjene
ispuni obrazac na GitHubu (issue). Veće izmjene šalješ kao pull
request: to je prijedlog izmjene datoteka koji pregledava održavatelj. Održavatelj
provjerava svaku izmjenu prije objave.

Nemaš GitHub račun? Javi nam na [Discordu](https://discord.meshcore-info.eu/) ako primijetiš
grupu koja nedostaje, netočan podatak ili prijevod koji čudno zvuči. Volonter
će se pobrinuti za ostalo.

## Dodaj svoju zajednicu {#community}

Vodiš lokalnu MeshCore grupu kojoj se svatko može pridružiti? Ispuni
[obrazac za zajednicu](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-community.yml)
i upiši naziv, područje i javne poveznice. Nakon dodavanja tvoja će se grupa prikazivati
na stranici [Lokalne grupe](/community/) na svim jezicima.

## Predloži uređaj ili projekt {#device-project}

Na [stranici o uređajima](/devices/) navodimo specifikacije iz dokumentacije proizvođača
i nikad ne stavljamo poveznice na trgovine. Hardver možeš predložiti putem
[obrasca za uređaj](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-device.yml).
Napravio si aplikaciju, alat, most ili hardverski dizajn za MeshCore s javnim izvornim
kodom? Dodaj ga putem
[obrasca za projekt](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-project.yml).

## Pregledaj prijevod {#translate}

Stranice na drugim jezicima isprva su strojni prijevodi i to piše na vrhu
stranice. Prijevodi se nalaze u zasebnom repozitoriju,
[meshcore-info.eu_i18n](https://github.com/meshcore-europe/meshcore-info.eu_i18n), pa
nikad ne moraš dirati kod stranice. Ako dobro govoriš neki od tih jezika, možeš poboljšati prijevod:

1. Otvori stranicu i klikni na "Pomozi poboljšati ovaj prijevod". Otvorit će se
   datoteka na GitHubu, gdje je možeš urediti u pregledniku.
2. Popravi tekst. Poveznice, kod, brojeve i nazive poput MeshCore ostavi
   točno onako kako jesu.
3. U bloku `translation` na vrhu promijeni `status: ai` u
   `status: human` i predloži izmjenu.

Našao si pogrešnu riječ, ali nemaš vremena za ispravak? Prijavi je putem
[obrasca za prijevod](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=translation-bug.yml).

## Poboljšaj vodič {#guides}

Vodiči se prvo pišu na engleskom, a zatim prevode s njega. Ispravke
i nove teme možeš poslati putem
[obrasca za sadržaj](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=new-content.yml)
ili kao pull request. Za činjenice trebaš navesti izvor: firmware ili dokumentaciju MeshCorea,
regulatora, proizvođača ili održavatelja. Piši svojim riječima.
Kratak citat s navedenim izvorom je u redu.

U [vodiču za suradnike](https://github.com/meshcore-europe/meshcore-info.eu/blob/main/CONTRIBUTING.md)
piše kako raditi na stranici na vlastitom računalu.

## Status prijevoda {#coverage}

"Pregledano" znači da je prijevod provjerila
osoba; "Strojno" znači da je riječ o strojnom prijevodu koji još nitko nije pregledao;
"Zastarjelo" znači da se engleski tekst promijenio nakon izrade prijevoda;
"Nedostaje" znači da stranica još nema prijevod.

{{< coverage >}}

## Zasluge {#credits}

Stranica je izrađena pomoću [Astra](https://astro.build/). Koristi fontove
IBM Plex Sans i IBM Plex Mono, pod licencom SIL Open Font License. Prijevodi
slijede
konvencije projekta [kiekr-i18n](https://github.com/marcelverdult/kiekr-i18n) i
dijele njegove MeshCore glosare. Sam MeshCore razvija se na
[meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore).

Tekst i prijevodi objavljeni su pod licencom CC BY 4.0, a kod pod licencom MIT.
