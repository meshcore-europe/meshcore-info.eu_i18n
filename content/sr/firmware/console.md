---
title: Serijska konzola
layout: console
lead: Kucaj komande za svoj repetitor u pregledaču, preko USB-a.
description: Podesi MeshCore repetitor, room server ili senzor preko USB-a u Chrome-u, Edge-u ili Operi, pomoću serijske konzole u pregledaču, bez instaliranja.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'c33167ce'
  seeded: '2026-11-02'
  fields: {title: '4e3c41fa', lead: 'f0d52063', description: '5d53ba06'}
  sections: ['c33167ce']
  blocks: ['13e02e98', '81b697e3']
---

Repetitor (prosleđuje poruke), room server (čuva objave za grupu) ili senzor
(šalje očitavanja) nema aplikaciju, pa ga podešavaš kucanjem komandi preko USB-a.
Priključi svoj čvor na računar, otvori ovu stranicu u Chrome-u, Edge-u ili Operi na
računaru i izaberi port svog čvora. Konzola prvo šalje `get role` i `ver` da bi
saznala kakav je to čvor. Obe komande samo čitaju podatke. Zatim konzola prikazuje
šta tvoj čvor ispisuje; ukucaj komandu, na primer `get name`, i pritisni Enter.
Dok kucaš, konzola predlaže komande koje tvoj čvor razume, a taster Tab dopunjava
prvu od njih.

Companion, čvor s kog šalješ poruke, umesto toga preko USB-a komunicira s aplikacijom. Njegovu komandnu liniju naći ćeš u
aplikaciji MeshCore, u verziji 1.50 ili novijoj.
