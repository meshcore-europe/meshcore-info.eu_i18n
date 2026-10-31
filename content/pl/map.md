---
title: Mapy zasięgu
layout: map
lead: Zobacz, dokąd sięga siatka, gdzie są węzły i jak wędrują wiadomości. Te mapy prowadzą społeczności z całej Europy.
description: Mapy MeshCore na żywo, mapy zasięgu i analizatory pakietów dla Europy i poszczególnych krajów.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '351071aa'
  seeded: '2026-10-31'
  fields: {title: '4b9f20a0', lead: 'fedb89bb', description: 'b5719f82'}
  sections: ['351071aa']
  blocks: ['dd5f039e', '9d4a2ad8', '70c417f2', '9fef7e16']
---

Węzeł pojawia się na tych mapach, gdy opublikuje go właściciel albo gdy usłyszy go
*obserwator*: węzeł, który przekazuje to, co słyszy, przez MQTT. Dlatego żadna mapa
nie jest kompletna. Analizatory pokazują ruch, który odbierają ich obserwatorzy: pakiety,
trasy i aktywność na kanałach. Wiadomości prywatne pozostają zaszyfrowane, więc żaden analizator
nie pokazuje ich treści.

Węzeł widnieje na mapie tam, gdzie umieścił go właściciel. To miejsce może być błędne
albo nieaktualne. Wiadomość flood wędruje naraz kilkoma ścieżkami. Trasa na mapie to ścieżka
kopii, która dotarła pierwsza. Pozostałych nikt nie zapisuje.

Te mapy wymagają internetu, siatka go nie potrzebuje. [Dlaczego](/network/)

Masz przekaźnik, czyli węzeł, który przekazuje wiadomości dalej? Ustaw jego pozycję poleceniami `set lat` i `set lon`, a mapy
będą mogły go umieścić. Jak to zrobić, pokazuje [poradnik o przekaźnikach](/repeater-guide/#config).
