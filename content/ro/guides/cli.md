---
title: Comenzi CLI
layout: cli
lead: Toate comenzile pentru repetorul, room serverul, senzorul sau companionul tău, grupate după ce vrei să faci. Citește ce face fiecare și valoarea de la care pornește, completează-ți propria valoare și copiaz-o.
description: 'Toate comenzile din firmware-ul MeshCore 1.18.0 pentru repetoare, room servere, senzori și companioane, grupate după sarcină: ce face fiecare, valoarea de la care pornește firmware-ul și ce noduri o au.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '15bdb6eb'
  seeded: '2026-10-31'
  fields: {title: 'a13cc6cb', lead: 'd051d3b4', description: '9a2dae75'}
  sections: ['15bdb6eb']
  blocks: ['8253bb3c', '66c83d82', '4f1b7c73', 'f28cf8b4']
---

Comenzile de aici urmează firmware-ul MeshCore 1.18.0 și sunt luate din codul sursă al firmware-ului. La o comandă adăugată într-o versiune recentă scrie de ce versiune ai nevoie. Un repetor transmite mesajele mai departe. Un room server păstrează postările pentru un grup. Un senzor raportează valorile măsurate. Room serverele, senzorii și companionii au multe comenzi în comun. La fiecare comandă scrie ce noduri o au. Cu „Ce nod?” vezi doar comenzile nodului tău.

Pe un repetor, room server sau senzor, tastezi comenzile prin USB de pe computer, de exemplu în [consola serială](/firmware/console/) de pe acest site. Aplicația MeshCore le trimite prin mesh. În [ghidul pentru repetoare](/repeater-guide/#config) găsești ambele variante.

Din versiunea 1.18, și un companion (nodul de pe care trimiți mesaje, asociat cu telefonul sau laptopul tău ori cu propriul ecran) are linie de comandă. Deschide Command Line în setările aplicației MeshCore, versiunea 1.50 sau mai nouă. Un contact cu permisiunea Remote CLI îi poate trimite companionului tău aceleași comenzi prin mesh. Aici intră și comenzile pentru WiFi și PIN.

Valoarea de pornire a unei comenzi este cea a repetorului. Un room server, un senzor sau un companion poate porni de la altă valoare. O comandă pe care o are doar companionul își arată propria valoare.
