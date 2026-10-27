---
title: Consolă serială
layout: console
lead: Trimite comenzi repetorului tău din browser, prin USB.
description: Configurează un repetor, un room server sau un senzor MeshCore prin USB din Chrome, Edge sau Opera, cu o consolă serială în browser. Fără niciun program de instalat.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: 'c33167ce'
  seeded: '2026-10-26'
  fields: {title: '4e3c41fa', lead: 'f0d52063', description: 'a2fe0704'}
  sections: ['c33167ce']
---

Un repetor (transmite mesajele mai departe), un room server (păstrează mesajele unui grup) sau un senzor (raportează măsurători) nu are aplicație. De aceea îl configurezi prin comenzi tastate prin USB. Conectează nodul la calculator, deschide această pagină în Chrome, Edge sau Opera pe un calculator și alege portul nodului tău. Consola trimite mai întâi `get role` și `ver`, ca să afle ce fel de nod ai. Ambele doar citesc. Apoi îți arată ce răspunde nodul; tastează o comandă precum `get name` și apasă Enter. În timp ce scrii, consola îți sugerează comenzile pe care nodul le înțelege, iar Tab o completează pe prima.

Un companion, nodul de pe care trimiți mesaje, comunică în schimb cu aplicația prin USB. Linia lui de comandă se află în aplicația MeshCore, versiunea 1.50 sau mai nouă.
