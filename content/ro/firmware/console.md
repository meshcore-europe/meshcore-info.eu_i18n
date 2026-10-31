---
title: Consolă serială
layout: console
lead: Trimite comenzi repetorului tău prin USB, direct din browser.
description: Configurează un repetor, un room server sau un senzor MeshCore prin USB din Chrome, Edge sau Opera, cu o consolă serială în browser, fără să instalezi nimic.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'c33167ce'
  seeded: '2026-10-31'
  fields: {title: '4e3c41fa', lead: 'f0d52063', description: '5d53ba06'}
  sections: ['c33167ce']
  blocks: ['13e02e98', '81b697e3']
---

Un repetor (transmite mai departe mesajele), un room server (păstrează postările
unui grup) sau un senzor (raportează măsurători) nu are aplicație. Așa că îl
configurezi tastând comenzi prin USB. Conectează nodul la calculator, deschide
pagina aceasta în Chrome, Edge sau Opera pe un calculator și alege portul
nodului tău. Consola trimite întâi `get role` și `ver`, ca să afle ce fel de nod
ai. Ambele comenzi doar citesc. Apoi consola îți arată ce răspunde nodul; scrie
o comandă precum `get name` și apasă Enter. În timp ce scrii, consola îți
sugerează comenzile pe care nodul tău le înțelege, iar Tab o completează pe
prima.

Un companion, nodul de pe care trimiți mesaje, comunică în schimb prin USB cu aplicația. Linia lui de comandă se află în
aplicația MeshCore, versiunea 1.50 sau mai nouă.
