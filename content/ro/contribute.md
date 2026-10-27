---
title: Contribuie
lead: Acest ghid este scris, verificat și tradus de voluntari. Iată cum poți ajuta, cu sau fără cont GitHub.
description: Adaugă comunitatea ta, un dispozitiv sau un proiect, revizuiește o traducere sau îmbunătățește un ghid pe meshcore-info.eu.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: 'f3ed6e9b'
  seeded: '2026-10-26'
  fields: {title: '97b0c61b', lead: 'e9b40d4d', description: '3bd97cd2'}
  sections: ['6e9d4b61', 'aca796d7', 'd4848d5b', '247b2601', '8a60e0d4', '645c82d3', 'c755b654']
---

Tot ce vezi pe acest site se află într-un
[depozit public pe GitHub](https://github.com/meshcore-europe/meshcore-info.eu). Modificările mici
trec printr-un formular pe GitHub (un issue). Orice schimbare mai mare intră ca pull
request: o propunere de modificare a fișierelor, pe care o revizuiește un întreținător. Un
întreținător verifică fiecare modificare înainte ca ea să apară pe site.

Nu ai cont GitHub? Spune-ne pe [Discord](https://discord.meshcore-info.eu/): un
grup care lipsește, o informație greșită sau o traducere care sună ciudat. Un voluntar
preia lucrurile de acolo.

## Adaugă comunitatea ta {#community}

Coordonezi un grup local MeshCore în care poate intra oricine? Completează
[formularul pentru comunități](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-community.yml)
cu numele, zona și linkurile publice. După adăugare, grupul tău apare
pe pagina [Grupuri locale](/community/) în toate limbile.

## Propune un dispozitiv sau un proiect {#device-project}

[Pagina de dispozitive](/devices/) prezintă specificații din documentația
producătorilor și nu trimite niciodată către magazine. Propune hardware prin
[formularul pentru dispozitive](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-device.yml).
Ai creat o aplicație, un instrument, o punte sau un proiect hardware pentru MeshCore cu codul sursă
public? Adaugă-l prin
[formularul pentru proiecte](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-project.yml).

## Revizuiește o traducere {#translate}

Paginile în alte limbi pornesc ca traduceri automate și menționează acest lucru în
partea de sus. Traducerile stau într-un depozit propriu,
[meshcore-info.eu_i18n](https://github.com/meshcore-europe/meshcore-info.eu_i18n), așa că
nu trebuie să atingi niciodată codul site-ului. Dacă vorbești bine una dintre limbi,
o poți face mai bună:

1. Deschide pagina și urmează „Ajută la îmbunătățirea acestei traduceri”. Astfel se deschide
   fișierul pe GitHub, unde îl poți edita direct în browser.
2. Corectează formulările. Păstrează linkurile, codul, numerele și numele precum MeshCore
   exact așa cum sunt.
3. În blocul `translation` din partea de sus, schimbă `status: ai` în
   `status: human` și propune modificarea.

Ai găsit un cuvânt greșit, dar nu ai timp să-l corectezi? Raportează-l prin
[formularul pentru traduceri](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=translation-bug.yml).

## Îmbunătățește un ghid {#guides}

Ghidurile se scriu mai întâi în engleză și se traduc de acolo. Corecturile
și subiectele noi sunt binevenite prin
[formularul pentru conținut](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=new-content.yml)
sau printr-un pull request. Faptele au nevoie de o sursă: firmware-ul MeshCore și documentația
lui, o autoritate de reglementare radio sau un producător. Scrie cu propriile tale cuvinte. Un
citat scurt, cu sursa lui, este în regulă.

[Ghidul pentru contribuitori](https://github.com/meshcore-europe/meshcore-info.eu/blob/main/CONTRIBUTING.md)
explică cum lucrezi la site pe propriul tău calculator.

## Starea traducerilor {#coverage}

„Revizuită” înseamnă verificată
de o persoană; „Automată” înseamnă tradusă automat și încă nerevizuită;
„Învechită” înseamnă că textul în engleză s-a schimbat după ce s-a făcut traducerea;
„Lipsă” înseamnă că pagina nu are încă nicio traducere.

{{< coverage >}}

## Mulțumiri {#credits}

Site-ul este construit cu [Astro](https://astro.build/). Folosește fonturile
IBM Plex Sans și IBM Plex Mono, sub licența SIL Open Font License. Traducerile
urmează
convențiile din [kiekr-i18n](https://github.com/marcelverdult/kiekr-i18n) și
folosesc aceleași glosare MeshCore. MeshCore însuși este dezvoltat la
[meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore).

Textul și traducerile sunt publicate sub licența CC BY 4.0, iar codul sub licența
MIT.
