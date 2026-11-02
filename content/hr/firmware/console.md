---
title: Serijska konzola
layout: console
lead: Upisuj naredbe svom repetitoru iz preglednika, preko USB-a.
description: Postavi MeshCore repetitor, room server ili senzor preko USB-a iz Chromea, Edgea ili Opere, pomoću serijske konzole u pregledniku i bez instalacije.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'c33167ce'
  seeded: '2026-11-02'
  fields: {title: '4e3c41fa', lead: 'f0d52063', description: '5d53ba06'}
  sections: ['c33167ce']
  blocks: ['13e02e98', '81b697e3']
---

Repetitor (prosljeđuje poruke), room server (čuva objave za grupu) ili senzor
(javlja očitanja) nema aplikaciju, pa ga postavljaš tako da upisuješ naredbe preko USB-a.
Spoji svoj čvor na računalo, otvori ovu stranicu u Chromeu, Edgeu ili Operi na
računalu i odaberi port svog čvora. Konzola najprije šalje `get role` i `ver` da
sazna što je tvoj čvor. Obje naredbe samo čitaju. Zatim prikazuje što tvoj čvor
javlja; upiši naredbu poput `get name` i pritisni Enter. Dok tipkaš, konzola
predlaže naredbe koje tvoj čvor razumije, a tipkom Tab dovršavaš prvu od njih.

Companion, čvor s kojeg šalješ poruke, umjesto toga preko USB-a komunicira s aplikacijom. Njegov naredbeni redak je u aplikaciji
MeshCore, u verziji 1.50 ili novijoj.
