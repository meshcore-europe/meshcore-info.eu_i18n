---
title: CLI komande
layout: cli
lead: Sve komande tvog repetitora, room servera, senzora ili companiona, grupisane po tome šta želiš da uradiš. Pročitaj šta komanda radi i koja joj je početna vrednost, unesi svoju i kopiraj komandu.
description: 'Sve komande MeshCore firmvera 1.18.0 za repetitore, room servere, senzore i companione, grupisane po zadatku: šta rade, koju početnu vrednost im firmver daje i koji čvorovi ih imaju.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '15bdb6eb'
  seeded: '2026-11-02'
  fields: {title: 'a13cc6cb', lead: 'd051d3b4', description: '9a2dae75'}
  sections: ['15bdb6eb']
  blocks: ['8253bb3c', '66c83d82', '4f1b7c73', 'f28cf8b4']
---

Ove komande odgovaraju MeshCore firmveru 1.18.0, a preuzete su iz izvornog koda
firmvera. Uz komandu dodatu u novijoj verziji piše koja joj verzija treba.
Repetitor prosleđuje poruke dalje, room server čuva objave za grupu, a senzor
šalje očitavanja. Room serveri, senzori i companioni imaju mnogo zajedničkih komandi.
Uz svaku komandu piše koji je čvorovi imaju. Opcija "Koji čvor?" prikazuje samo
komande tvog čvora.

Na repetitoru, room serveru ili senzoru komande kucaš preko USB veze sa računara, na primer u [serijskoj konzoli](/firmware/console/) na ovom sajtu. MeshCore aplikacija ih šalje preko mreže. U
[vodiču za repetitor](/repeater-guide/#config) naći ćeš oba načina.

Od verzije 1.18 i companion ima komandnu liniju. Companion je čvor s kojeg šalješ poruke, uparen sa telefonom ili laptopom, ili sa sopstvenim ekranom.
Otvori Command Line u podešavanjima MeshCore aplikacije, verzije 1.50 ili
novije. Kontakt sa dozvolom Remote CLI može da šalje tvom companionu
iste komande preko mreže. To važi i za WiFi i PIN komande.

Početna vrednost uz komandu je ona koju ima repetitor. Room server, senzor ili
companion mogu da krenu od druge vrednosti. Uz komandu koju ima samo companion piše njegova vrednost.
