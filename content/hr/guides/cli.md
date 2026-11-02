---
title: CLI naredbe
layout: cli
lead: Sve naredbe za tvoj repetitor, room server, senzor ili companion, grupirane prema onome što želiš napraviti. Pročitaj što naredba radi i s kojom vrijednošću počinje, upiši svoju vrijednost i kopiraj naredbu.
description: 'Sve naredbe firmvera MeshCore 1.18.0 za repetitore, room servere, senzore i companione, grupirane prema zadatku: što naredba radi, s kojom vrijednošću firmver počinje i koji je čvorovi imaju.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '15bdb6eb'
  seeded: '2026-11-02'
  fields: {title: 'a13cc6cb', lead: 'd051d3b4', description: '9a2dae75'}
  sections: ['15bdb6eb']
  blocks: ['8253bb3c', '66c83d82', '4f1b7c73', 'f28cf8b4']
---

Ove naredbe odgovaraju firmveru MeshCore 1.18.0, a preuzete su iz njegova izvornog koda. Kod naredbe dodane u novijoj verziji piše koja joj verzija treba. Repetitor prosljeđuje poruke, room server čuva objave za grupu, a senzor šalje očitanja. Room serveri, senzori i companioni dijele mnoge naredbe. Kod svake naredbe piše koji je čvorovi imaju. "Koji čvor?" prikazuje samo naredbe tvojeg čvora.

Na repetitoru, room serveru ili senzoru naredbe upisuješ s računala preko USB-a, na primjer u [serijskoj konzoli](/firmware/console/) na ovoj stranici. Aplikacija MeshCore šalje ih preko mreže. U [vodiču za repetitor](/repeater-guide/#config) naći ćeš oba načina.

Od verzije 1.18 i companion (čvor s kojeg šalješ poruke, uparen s mobitelom ili laptopom, ili s vlastitim zaslonom) ima naredbeni redak. Otvori Command Line u postavkama aplikacije MeshCore, verzije 1.50 ili novije. Kontakt s dozvolom Remote CLI može tvojem companionu poslati iste naredbe preko mreže. To vrijedi i za naredbe za WiFi i PIN.

Navedena početna vrijednost naredbe odnosi se na repetitor. Room server, senzor ili companion mogu imati drugu početnu vrijednost. Naredba koju ima samo companion prikazuje vlastitu početnu vrijednost.
