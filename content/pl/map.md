---
title: Mapy zasięgu
layout: map
lead: Zobacz, dokąd sięga siatka, gdzie stoją węzły i jak wędrują wiadomości. Te mapy prowadzą społeczności z całej Europy.
description: Mapy MeshCore na żywo, mapy zasięgu i analizatory pakietów dla Europy i poszczególnych krajów.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '550066cc'
  seeded: '2026-10-26'
  fields: {title: '4b9f20a0', lead: 'fedb89bb', description: 'b5719f82'}
  sections: ['550066cc']
---

Węzeł pojawia się na tych mapach, gdy jego właściciel go opublikuje albo gdy
usłyszy go *obserwator*: węzeł, który przekazuje przez MQTT to, co odbiera.
Dlatego żadna mapa nie jest kompletna. Analizatory pokazują ruch, który odbierają
ich obserwatorzy: pakiety, trasy i aktywność na kanałach. Wiadomości prywatne
pozostają zaszyfrowane, więc żaden analizator nie pokazuje ich treści.

Te mapy potrzebują internetu, siatka nie. [Dlaczego](/network/)

Prowadzisz przekaźnik, czyli węzeł, który przekazuje wiadomości dalej? Ustaw jego pozycję poleceniami `set lat` i `set lon`, a mapy
będą mogły go umieścić. Jak to zrobić, pokazuje [poradnik o przekaźnikach](/repeater-guide/#config).
