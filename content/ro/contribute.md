---
title: Contribuie
lead: Acest ghid este scris, verificat și tradus de voluntari. Iată cum poți ajuta, cu sau fără cont de GitHub.
description: Adaugă comunitatea ta, un dispozitiv sau un proiect, verifică o traducere sau îmbunătățește un ghid de pe meshcore-info.eu.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'f3ed6e9b'
  seeded: '2026-10-31'
  fields: {title: '97b0c61b', lead: 'e9b40d4d', description: '3bd97cd2'}
  sections: ['6e9d4b61', 'aca796d7', 'd4848d5b', '247b2601', '8a60e0d4', '645c82d3', 'c755b654']
  blocks: ['2f9dd6e8', '44167907', 'b020e1a4', 'f2c726cd', '2e9d1fdd', 'b2a902ba', 'b15ce10b', '2be86888', '3db6cb63', '2e3c2fc0', '693a5d9d', '73e33897', '96d8689d', 'c67fd14a', 'f92f7e49', '12ddca6c', 'e947e2a9', '526df4bb', 'e0d3559e']
---

Tot conținutul acestui site se află într-un
[depozit public pe GitHub](https://github.com/meshcore-europe/meshcore-info.eu). Modificările mici
le trimiți printr-un formular pe GitHub (un issue). Pe cele mai mari le trimiți ca pull
request: o propunere de modificare a fișierelor, pe care o verifică un administrator. Un
administrator verifică fiecare modificare înainte să apară pe site.

Nu ai cont de GitHub? Scrie-ne pe [Discord](https://discord.meshcore-info.eu/): un
grup care lipsește, o informație greșită sau o traducere care sună ciudat. Un voluntar
se ocupă de rest.

## Adaugă comunitatea ta {#community}

Conduci un grup local MeshCore căruia i se poate alătura oricine? Completează
[formularul pentru comunități](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-community.yml)
cu numele, zona și linkurile publice. După ce îl adăugăm, grupul tău apare
pe pagina [Grupuri locale](/community/) în toate limbile.

## Propune un dispozitiv sau un proiect {#device-project}

Pe [pagina de dispozitive](/devices/) găsești specificații din documentația
producătorilor, fără linkuri către magazine. Propune un dispozitiv prin
[formularul pentru dispozitive](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-device.yml).
Ai construit o aplicație, un instrument, o punte sau un design hardware pentru MeshCore, cu cod sursă public?
Adaugă-l prin
[formularul pentru proiecte](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-project.yml).

## Verifică o traducere {#translate}

Paginile în alte limbi încep ca traduceri automate și o spun în partea de
sus. Traducerile stau într-un depozit separat,
[meshcore-info.eu_i18n](https://github.com/meshcore-europe/meshcore-info.eu_i18n), așa că
nu trebuie să atingi niciodată codul site-ului. Dacă vorbești bine una dintre limbi,
o poți îmbunătăți:

1. Deschide pagina și apasă pe „Ajută la îmbunătățirea acestei traduceri”. Se deschide
   fișierul pe GitHub, unde îl poți edita în browser.
2. Corectează formularea. Păstrează linkurile, codul, numerele și nume precum MeshCore
   exact așa cum sunt.
3. În blocul `translation` din partea de sus, schimbă `status: ai` în
   `status: human` și propune modificarea.

Ai găsit un cuvânt greșit, dar nu ai timp să-l corectezi? Semnalează-l prin
[formularul pentru traduceri](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=translation-bug.yml).

## Îmbunătățește un ghid {#guides}

Ghidurile se scriu întâi în engleză, apoi se traduc din engleză. Corecturile
și subiectele noi sunt binevenite prin
[formularul pentru conținut](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=new-content.yml)
sau printr-un pull request. Orice informație are nevoie de o sursă: firmware-ul MeshCore și documentația lui,
o autoritate de reglementare radio sau un producător. Scrie cu propriile tale cuvinte. Un
citat scurt, cu sursa lui, este în regulă.

[Ghidul pentru contributori](https://github.com/meshcore-europe/meshcore-info.eu/blob/main/CONTRIBUTING.md)
explică cum lucrezi la site pe propriul tău calculator.

## Starea traducerilor {#coverage}

„Reviewed” înseamnă verificat
de o persoană; „Machine” înseamnă tradus automat și încă neverificat;
„Outdated” înseamnă că textul în engleză s-a schimbat după ce s-a făcut traducerea;
„Missing” înseamnă că pagina nu are încă o traducere.

{{< coverage >}}

## Mulțumiri {#credits}

Site-ul este construit cu [Astro](https://astro.build/). Folosește fonturile
IBM Plex Sans și IBM Plex Mono, sub licența SIL Open Font License. Traducerile
respectă
convențiile din [kiekr-i18n](https://github.com/marcelverdult/kiekr-i18n) și
îi folosesc glosarele MeshCore. MeshCore însuși este dezvoltat la
[meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore).

Textele și traducerile sunt publicate sub licența CC BY 4.0, iar codul sub licența
MIT.
