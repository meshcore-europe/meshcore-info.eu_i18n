---
title: Setări recomandate
layout: settings
lead: Presetarea radio folosită în zona ta și setările pe care le-au schimbat vecinii tăi. Alege-ți țara, setează presetarea și copiază comenzile.
description: Presetarea radio MeshCore pentru fiecare zonă din Europa și setările de repetor și companion pe care grupurile locale le-au schimbat față de valorile implicite, cu comenzile.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '0876215b'
  seeded: '2026-10-31'
  fields: {title: 'cfb32983', lead: 'f3f16725', description: 'cb15acd3'}
  sections: ['39848942', 'd1606fcd']
  blocks: ['8c9e88ea', '50ac6063', '85c2203d', '15f91217', 'bdf5fa4e', '69d8e70b', '28f83120', 'fe27027b']
---

Fiecare zonă de mai jos folosește propria presetare radio sau schimbă câteva
dintre valorile implicite ale MeshCore. Tot ce nu apare aici rămâne la valoarea
implicită, așa că schimbi doar ce a schimbat zona ta. Un repetor transmite mai
departe mesajele tuturor. Un companion este nodul de pe care trimiți mesaje:
îl asociezi cu telefonul sau laptopul prin Bluetooth sau USB, ori are propriul ecran.

În [ghidul pentru repetoare](/repeater-guide/#config) afli cum ajungi la linia
de comandă a repetorului tău. În [consola serială](/firmware/console/) de pe
acest site tastezi singur comenzile. Sub fiecare zonă poți trimite și setările
ei prin USB. Ghidul prezintă și [limitele legale](/repeater-guide/#legal)
pe 868 MHz.

## Limitează traficul {#traffic}

Aceste setări sunt valabile în orice zonă. Fiecare repetor transmite mai departe
orice mesaj flood pe care îl aude. Un mesaj de la tine costă o transmisie, plus
câte una pentru fiecare repetor care îl aude. Cu un ciclu de funcționare de 10%,
un repetor poate trimite circa 680 de pachete pe oră. Toți cei din jurul lui
împart acest număr. Un mesaj care ajunge mai departe decât e nevoie consumă o
parte din el.

**Trimite în cea mai mică regiune care ajunge la cei cărora le scrii.**
Regiunile sunt incluse unele în altele: o țară, o provincie, un grup local,
fiecare cu propriul cod, de exemplu `nl`, `nl-ov` și `nl-ov-zwo`. Un mesaj
pentru `nl-ov-zwo` rămâne la repetoarele din acel grup. Un repetor transmite
mai departe doar regiunile pe care le are el însuși: dacă are `nl`, nu transmite
și `nl-ov`. Pune fiecare repetor în toate regiunile pe care le deservește, și doar
în acelea. [Grupul tău local](/community/) știe care sunt acestea.

**Limitează ce transmite mai departe repetorul tău.** Două setări țin aproape de
casă traficul care nu are nevoie să ajungă departe:

```text
set flood.max.advert 3
set flood.max.unscoped 1
```

- `flood.max.advert 3`: anunțurile, prin care un nod se face cunoscut în mesh,
  parcurg cel mult 3 salturi.
- `flood.max.unscoped 1`: un mesaj fără regiune trece prin cel mult un repetor.
