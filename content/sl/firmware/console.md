---
title: Serijska konzola
layout: console
lead: Ukaze za svoj ponavljalnik tipkaš v brskalniku, povezava pa teče prek USB.
description: MeshCore ponavljalnik, room server ali senzor nastaviš prek USB v brskalniku Chrome, Edge ali Opera. Serijska konzola deluje v brskalniku in ti ni treba ničesar nameščati.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'c33167ce'
  seeded: '2026-11-02'
  fields: {title: '4e3c41fa', lead: 'f0d52063', description: '5d53ba06'}
  sections: ['c33167ce']
  blocks: ['13e02e98', '81b697e3']
---

Ponavljalnik (posreduje sporočila naprej), room server (hrani objave za skupino)
in senzor (pošilja meritve) nimajo aplikacije, zato jih nastaviš z ukazi, ki jih
vtipkaš prek USB. Vozlišče priključi na računalnik, to stran odpri v brskalniku
Chrome, Edge ali Opera na računalniku in izberi vrata svojega vozlišča. Konzola
najprej pošlje `get role` in `ver`, da ugotovi, kaj je tvoje vozlišče. Oba ukaza
samo bereta. Nato konzola prikaže, kaj sporoča vozlišče; vtipkaj ukaz, na primer
`get name`, in pritisni Enter. Med tipkanjem ti konzola predlaga ukaze, ki jih
tvoje vozlišče razume, s tipko Tab pa vpišeš prvega.

Companion, vozlišče, s katerim pošiljaš sporočila, pa se prek USB povezuje z aplikacijo. Njegovo ukazno vrstico najdeš v
aplikaciji MeshCore različice 1.50 ali novejše.
