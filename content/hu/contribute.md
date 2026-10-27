---
title: Közreműködés
lead: Ezt az útmutatót önkéntesek írják, ellenőrzik és fordítják. Így segíthetsz, GitHub-fiókkal vagy anélkül.
description: Add hozzá a közösségedet, egy eszközt vagy egy projektet, nézz át egy fordítást, vagy javíts egy útmutatón a meshcore-info.eu oldalon.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: 'f3ed6e9b'
  seeded: '2026-10-26'
  fields: {title: '97b0c61b', lead: 'e9b40d4d', description: '3bd97cd2'}
  sections: ['6e9d4b61', 'aca796d7', 'd4848d5b', '247b2601', '8a60e0d4', '645c82d3', 'c755b654']
---

Az oldal teljes tartalma egy nyilvános
[GitHub-tárolóban](https://github.com/meshcore-europe/meshcore-info.eu) található. A kisebb
módosításokat egy GitHub-űrlapon (issue) keresztül adod be. Minden nagyobb változtatás
pull requestként érkezik: ez a fájlok módosítására tett javaslat, amelyet egy karbantartó
átnéz. Egy karbantartó minden változtatást ellenőriz, mielőtt az élesbe kerül.

Nincs GitHub-fiókod? Írd meg nekünk [Discordon](https://discord.meshcore-info.eu/): egy
hiányzó csoportot, egy téves adatot vagy egy furcsán hangzó fordítást. Onnan egy önkéntes
viszi tovább.

## Add hozzá a közösségedet {#community}

Vezetsz egy helyi MeshCore-csoportot, amelyhez bárki csatlakozhat? Töltsd ki a
[közösségi űrlapot](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-community.yml)
a névvel, a területtel és a nyilvános linkekkel. Felvétel után a csoportod minden nyelven
megjelenik a [Helyi csoportok](/community/) oldalon.

## Javasolj egy eszközt vagy egy projektet {#device-project}

Az [eszközök oldala](/devices/) a gyártói dokumentációból vett specifikációkat sorolja fel,
és soha nem hivatkozik boltokra. Hardvert az
[eszközűrlapon](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-device.yml)
javasolhatsz.
Készítettél alkalmazást, eszközt, hidat vagy hardvertervet a MeshCore-hoz nyilvános
forráskóddal? Add hozzá a
[projektűrlapon](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-project.yml).

## Nézz át egy fordítást {#translate}

A más nyelvű oldalak gépi fordításként indulnak, és ezt a tetejükön jelzik is. A
fordítások külön tárolóban élnek, a
[meshcore-info.eu_i18n](https://github.com/meshcore-europe/meshcore-info.eu_i18n) alatt, így
az oldal kódjához soha nem kell hozzányúlnod. Ha jól beszéled valamelyik nyelvet,
javíthatsz rajta:

1. Nyisd meg az oldalt, és kattints a „Segíts javítani ezt a fordítást" linkre. Ez
   megnyitja a fájlt a GitHubon, ahol a böngésződben szerkesztheted.
2. Javítsd a megfogalmazást. A linkeket, a kódot, a számokat és az olyan neveket, mint a
   MeshCore, hagyd pontosan úgy, ahogy vannak.
3. A fájl tetején lévő `translation` blokkban írd át a `status: ai` értéket
   `status: human` értékre, majd küldd be a módosítást.

Találtál egy rossz szót, de nincs időd javítani? Jelezd a
[fordítási űrlapon](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=translation-bug.yml).

## Javíts egy útmutatón {#guides}

Az útmutatók először angolul készülnek, és onnan fordítjuk őket. Javításokat és új
témákat a
[tartalmi űrlapon](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=new-content.yml)
vagy pull requestben várunk. Minden tényhez forrás kell: a MeshCore firmware és a
dokumentációja, egy rádiós hatóság vagy egy gyártó. Fogalmazz a saját szavaiddal. Egy
rövid idézet a forrásával együtt rendben van.

A [közreműködői útmutató](https://github.com/meshcore-europe/meshcore-info.eu/blob/main/CONTRIBUTING.md)
elmagyarázza, hogyan dolgozhatsz az oldalon a saját gépeden.

## A fordítások állapota {#coverage}

Az „Átnézett" azt jelenti, hogy egy ember ellenőrizte; a „Gépi" azt, hogy gépi fordítás,
amelyet még senki nem nézett át; az „Elavult" azt, hogy az angol szöveg a fordítás
elkészülte után változott; a „Hiányzik" azt, hogy az oldalnak még nincs fordítása.

{{< coverage >}}

## Köszönetnyilvánítás {#credits}

Az oldal az [Astro](https://astro.build/) keretrendszerrel készült. Az IBM Plex Sans és az
IBM Plex Mono betűtípusokat használja, a SIL Open Font License alatt. A fordítások a
[kiekr-i18n](https://github.com/marcelverdult/kiekr-i18n) szabályait követik, és annak
MeshCore-szójegyzékeit használják. Magát a MeshCore-t a
[meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore) alatt fejlesztik.

A szövegek és a fordítások CC BY 4.0 licenc alatt érhetők el, a kód pedig MIT
licenc alatt.
