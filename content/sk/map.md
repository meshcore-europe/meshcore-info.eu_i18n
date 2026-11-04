---
title: Mapy pokrytia
layout: map
lead: Pozri si, kam sieť mesh siaha, kde sú uzly a ako putujú správy. Tieto mapy prevádzkujú komunity po celej Európe.
description: Živé mapy MeshCore, mapy pokrytia a analyzátory paketov pre Európu a jednotlivé krajiny.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '24bfdf6b'
  seeded: '2026-11-04'
  fields: {title: '4b9f20a0', lead: 'fedb89bb', description: 'b5719f82'}
  sections: ['24bfdf6b']
  blocks: ['dd5f039e', '9d4a2ad8', '763fc710', '70c417f2', '9fef7e16']
---

Uzol sa na týchto mapách objaví, keď ho zverejní jeho vlastník alebo keď ho
zachytí *observer*: uzol, ktorý cez MQTT preposiela to, čo zachytí. Preto
žiadna mapa nie je úplná. Analyzátory zobrazujú prevádzku, ktorú prijímajú ich
observery: pakety, trasy a aktivitu v kanáloch. Priame správy zostávajú šifrované,
takže ich obsah žiadny analyzátor nezobrazí.

Uzol je na mape tam, kam ho umiestnil jeho vlastník, a táto poloha môže byť
nesprávna alebo zastaraná. Správa typu flood putuje naraz viacerými cestami. Trasa
na mape je cesta kópie, ktorá dorazila ako prvá. Ostatné cesty sa nezaznamenávajú.

Zdá sa ti trasa na mape nepravdepodobná? Skontroluj 2 jej uzly pomocou funkcie Line of Sight
v aplikácii MeshCore. [Návod na repeater](/repeater-guide/#check-site) ukazuje, ako na to.

Tieto mapy potrebujú internet, sieť mesh ho nepotrebuje. [Prečo](/network/)

Prevádzkuješ repeater, teda uzol, ktorý posúva správy ďalej? Nastav mu polohu príkazmi `set lat` a `set lon` a mapy ho budú vedieť umiestniť. Postup nájdeš v [návode na repeater](/repeater-guide/#config).
