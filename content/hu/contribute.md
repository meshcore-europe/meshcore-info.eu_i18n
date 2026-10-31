---
title: Közreműködés
lead: Ezt az útmutatót önkéntesek írják, ellenőrzik és fordítják. Itt megtudod, hogyan segíthetsz, GitHub-fiókkal vagy anélkül.
description: Vedd fel a közösségedet, egy eszközt vagy egy projektet, nézz át egy fordítást, vagy javíts egy útmutatót a meshcore-info.eu oldalon.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'f3ed6e9b'
  seeded: '2026-10-31'
  fields: {title: '97b0c61b', lead: 'e9b40d4d', description: '3bd97cd2'}
  sections: ['6e9d4b61', 'aca796d7', 'd4848d5b', '247b2601', '8a60e0d4', '645c82d3', 'c755b654']
  blocks: ['2f9dd6e8', '44167907', 'b020e1a4', 'f2c726cd', '2e9d1fdd', 'b2a902ba', 'b15ce10b', '2be86888', '3db6cb63', '2e3c2fc0', '693a5d9d', '73e33897', '96d8689d', 'c67fd14a', 'f92f7e49', '12ddca6c', 'e947e2a9', '526df4bb', 'e0d3559e']
---

Az oldal teljes tartalma egy nyilvános
[GitHub-tárolóban](https://github.com/meshcore-europe/meshcore-info.eu) található. A kisebb
változtatásokat egy GitHub-űrlapon (issue) küldheted be. A nagyobbakat pull
requestként adod be: ez egy javasolt módosítás a fájlokon, amelyet egy karbantartó átnéz.
Minden változtatást egy karbantartó ellenőriz, mielőtt élesbe kerül.

Nincs GitHub-fiókod? Írd meg nekünk a [Discordon](https://discord.meshcore-info.eu/), ha
hiányzik egy csoport, hibás egy adat, vagy furcsán hangzik egy fordítás. Onnan
egy önkéntes viszi tovább.

## Vedd fel a közösségedet {#community}

Helyi MeshCore-csoportot vezetsz, amelyhez bárki csatlakozhat? Töltsd ki a
[közösségi űrlapot](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-community.yml)
a csoport nevével, a területtel és a nyilvános linkekkel. A felvétel után a csoportod
minden nyelven megjelenik a [Helyi csoportok](/community/) oldalon.

## Javasolj egy eszközt vagy egy projektet {#device-project}

Az [eszközök oldalán](/devices/) a gyártói dokumentációból vett műszaki adatok szerepelnek,
és az oldal sosem hivatkozik webáruházakra. Hardvert az
[eszközűrlapon](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-device.yml) javasolhatsz.
Készítettél MeshCore-hoz alkalmazást, eszközt, hidat vagy hardvertervet nyilvános forráskóddal?
Vedd fel a
[projektűrlapon](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-project.yml).

## Nézz át egy fordítást {#translate}

A más nyelvű oldalak gépi fordításként indulnak, és ezt az oldal tetején jelzik is.
A fordítások külön tárolóban vannak,
[meshcore-info.eu_i18n](https://github.com/meshcore-europe/meshcore-info.eu_i18n) néven, így
sosem kell az oldal kódjához nyúlnod. Ha jól beszélsz valamelyik nyelvet,
jobbá teheted a fordítást:

1. Nyisd meg az oldalt, és kattints a „Segíts javítani ezt a fordítást” linkre. Ez
   megnyitja a fájlt a GitHubon, ahol a böngésződben szerkesztheted.
2. Javítsd a megfogalmazást. A linkeket, a kódot, a számokat és az olyan neveket, mint a MeshCore,
   hagyd pontosan úgy, ahogy vannak.
3. A fájl tetején lévő `translation` blokkban írd át a `status: ai` sort
   `status: human` értékre, majd javasold a változtatást.

Hibás szót találtál, de nincs időd kijavítani? Jelezd a
[fordítási űrlapon](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=translation-bug.yml).

## Javíts egy útmutatót {#guides}

Az útmutatók először angolul készülnek, és onnan fordítjuk őket. Javításokat
és új témákat a
[tartalmi űrlapon](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=new-content.yml)
vagy pull requestként küldhetsz. A tényekhez forrás kell: a MeshCore firmware és a dokumentációja,
egy rádiós hatóság vagy egy gyártó. A saját szavaiddal írj. Egy
rövid idézet a forrásával együtt rendben van.

A [közreműködői útmutató](https://github.com/meshcore-europe/meshcore-info.eu/blob/main/CONTRIBUTING.md)
elmagyarázza, hogyan dolgozhatsz az oldalon a saját gépeden.

## A fordítások állapota {#coverage}

A „Reviewed” azt jelenti, hogy egy ember ellenőrizte;
a „Machine” azt, hogy gépi fordítás, amelyet még senki sem nézett át;
az „Outdated” azt, hogy az angol szöveg a fordítás elkészülte után megváltozott;
a „Missing” azt, hogy az oldalnak még nincs fordítása.

{{< coverage >}}

## Köszönetnyilvánítás {#credits}

Az oldal az [Astro](https://astro.build/) keretrendszerrel készült. Az IBM Plex Sans és
az IBM Plex Mono betűtípust használja, a SIL Open Font License alatt. A fordítások
a [kiekr-i18n](https://github.com/marcelverdult/kiekr-i18n)
konvencióit követik, és annak MeshCore-szójegyzékeit használják. Magát a MeshCore-t a
[meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore) tárolóban fejlesztik.

A szövegek és a fordítások CC BY 4.0, a kód MIT
licenc alatt érhető el.
