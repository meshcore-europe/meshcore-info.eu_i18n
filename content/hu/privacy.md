---
title: Adatvédelem
lead: Nincs elemzés, nincs nyomkövető és nincs fiók. Egy süti, és az is csak akkor, ha témát választasz.
description: Mit tárol rólad a meshcore-info.eu, mit kérdez más szerverektől, és mit lát a tárhelyszolgáltatónk, amikor meglátogatod az oldalt.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '84900169'
  seeded: '2026-10-26'
  fields: {title: '54a57c31', lead: '2ed1f1fa', description: '43c66faf'}
  sections: ['e3b0c442', 'd95a599e', 'a3c22720', '0162b1a7', 'd487d7f9', 'fce0b0e5', 'ccb2e4b3']
---

## Mit nem csinál ez az oldal {#not}

- Nem futtat elemző, statisztikai vagy követő szkripteket, se sajátot, se másét.
- A betűtípusokat, stílusokat és szkripteket csak erről az oldalról tölti be. Nincsenek
  más oldalakról beágyazott videók, nincsenek közösségi média gombok és nincsenek hirdetések.
- Nincsenek fiókok és hozzászólások. Az oldal két űrlapja, a kulcsgenerátor
  és a csatornaválasztó, semmit nem küld nekünk.

## Mi marad a böngésződben {#browser}

Ha a témamenüben a rendszer követése, a sötét vagy a világos beállítást választod, a böngésződ
1 évig egy `dmc-mode` nevű sütiben őrzi ezt a választást. A süti a
meshcore-info.eu oldalon és aldomainjein érvényes, így minden oldal úgy nyílik meg, ahogy választottad.
A süti csak ezt az egy szót tartalmazza. Ha sosem választasz, az oldal nem állít be sütit.
Töröld a böngésződ oldaladatait, hogy eltávolítsd.

A kezdőlap ezen a fülön azt is megjegyzi, hogy láttad a nyitófilmjét, így
ugyanazon a fülön a második látogatás már a tartalomnál nyílik meg. Ez az információ eltűnik, amikor
bezárod a fület.

Egy ellenőrzőlistás oldalon, mint például a
[telepítési ellenőrzőlista](/repeater-guide/#checklist), a böngésződ megőrzi, mely
elemeket pipáltad ki, így visszatéréskor még mindig kipipálva vannak. Addig maradnak
az eszközödön, amíg ki nem veszed a pipát.

A kezdőlap kiolvassa a böngésződ előnyben részesített nyelveit, és az oldal
megfelelő nyelvi változatát nyitja meg. Ez az ellenőrzés a böngésződben fut;
semmit nem tárol és nem küld el.

## Mit kérdez az oldal más szerverektől {#requests}

A kezdőlap és a Hálózat oldal élő számokat mutat a
[meshcore-analyzer.eu](https://meshcore-analyzer.eu) szerverről, amelyet ugyanaz az
önkéntes csapat üzemeltet. A Csatornák keresése oldal ettől a szervertől kéri le az általad
választott ország csatornáit. Minden kérés tartalmazza az IP-címedet, a böngésződ nevét
és verzióját (a user agentet), és a Csatornák keresése oldalon a választott országot. Más
oldal nem lép kapcsolatba más szerverrel.

## Mit lát a tárhelyszolgáltatónk {#host}

Minden oldalt a Cloudflare, egy tárhelyszolgáltató cég küld el neked. Ehhez a Cloudflare szerverei
feldolgozzák a kérésedet. Ez a kérés tartalmazza az IP-címedet,
az oldal címét és a böngésződ user agentjét, mint bármely
webszerver esetén. A Cloudflare [adatvédelmi irányelvei](https://www.cloudflare.com/privacypolicy/)
leírják, hogyan kezeli ezeket az adatokat. A Cloudflare arra is kéri a böngésződet, hogy
jelentse neki a sikertelen kapcsolódást, így látja a kieséseket.

Az oldalt üzemeltető önkéntesek nem kapcsolják be a Cloudflare webes elemzését,
és nem férnek hozzá az egyes látogatók naplóihoz.

## Hivatkozások más oldalakra {#links}

Az oldal hivatkozásai helyi csoportokra, térképekre, projektekre, gyártókra és a
GitHubra mutatnak. Ha rákattintasz egyre, onnantól annak az oldalnak a saját adatvédelmi irányelvei érvényesek. Az
„Oldal szerkesztése a GitHubon" hivatkozások a GitHubra visznek.

## Kérdések {#questions}

Nyiss egy issue-t a [GitHubon](https://github.com/meshcore-europe/meshcore-info.eu/issues), ha
valami ezen az oldalon nem világos vagy már nem igaz.
