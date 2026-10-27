---
title: Comenzi CLI
layout: cli
lead: Fiecare comandă a repetorului, room server-ului, senzorului sau companion-ului tău, grupată după ce vrei să faci. Citește ce face și valoarea cu care pornește, completează valoarea ta și copiaz-o.
description: 'Fiecare comandă din firmware-ul MeshCore 1.18.0 pentru repetoare, room servere, senzori și companioni, grupată pe sarcini: ce face, valoarea cu care pornește firmware-ul și ce noduri o au.'
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '15bdb6eb'
  seeded: '2026-10-26'
  fields: {title: 'a13cc6cb', lead: 'd051d3b4', description: '9a2dae75'}
  sections: ['15bdb6eb']
---

Aceste comenzi urmează firmware-ul MeshCore 1.18.0, citite din codul sursă al firmware-ului. O comandă adăugată într-o versiune recentă spune ce versiune are nevoie. Un repetor transmite mesajele mai departe, un room server stochează postările unui grup, un senzor raportează măsurători. Room serverele, senzorii și companionii au multe comenzi în comun. Fiecare comandă spune ce noduri o au. „Ce nod?" arată doar comenzile nodului tău.

Pe un repetor, room server sau senzor, le tastezi prin USB de pe calculatorul tău, de exemplu în [consola serială](/firmware/console/) de pe acest site. Aplicația MeshCore le trimite prin mesh. [Ghidul pentru repetoare](/repeater-guide/#config) le arată pe amândouă.

De la 1.18, și un companion (nodul de pe care trimiți mesaje, asociat cu telefonul sau laptopul tău, sau cu propriul ecran) are o linie de comandă. Deschide Command Line în setările aplicației MeshCore, versiunea 1.50 sau mai nouă. Un contact cu permisiunea Remote CLI poate trimite companion-ului tău aceleași comenzi prin mesh. Asta include comenzile pentru WiFi și PIN.

Valoarea cu care pornește o comandă este cea a repetorului. Un room server, senzor sau companion poate porni de la altă valoare. O comandă pe care o are doar un companion arată valoarea proprie.
