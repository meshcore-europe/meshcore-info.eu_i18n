---
title: Setări recomandate
layout: settings
lead: Presetarea radio folosită în zona ta și setările pe care le-au schimbat vecinii tăi. Alege țara, setează presetarea și copiază comenzile.
description: Presetarea radio MeshCore pentru fiecare zonă din Europa, plus setările de repetor și de companion pe care grupurile locale le-au schimbat față de valorile implicite, cu comenzile aferente.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '9547ba62'
  seeded: '2026-10-26'
  fields: {title: 'cfb32983', lead: 'f3f16725', description: 'cb15acd3'}
  sections: ['39848942', '43cde8b4']
---

Fiecare zonă de mai jos folosește propria presetare radio sau schimbă câteva
dintre valorile implicite ale MeshCore. Tot ce nu apare în listă rămâne la
valoarea implicită, așa că schimbi doar ce a schimbat zona ta. Un repetor
transmite mesajele mai departe pentru toată lumea. Un companion este nodul de
pe care trimiți mesaje, asociat cu telefonul sau laptopul tău prin Bluetooth
sau USB, ori cu propriul ecran.

În [ghidul pentru repetor](/repeater-guide/#config) vezi cum ajungi la linia
de comandă a repetorului tău. În [consola serială](/firmware/console/) de pe
acest site scrii singur comenzile. Sub fiecare zonă poți trimite setările ei
și prin USB. Ghidul listează și [limitele legale](/repeater-guide/#legal)
pentru 868 MHz.

## Ține traficul la nivel scăzut {#traffic}

Aceste setări sunt valabile pentru toate zonele. Fiecare repetor transmite
mai departe fiecare mesaj flood pe care îl aude. Un mesaj trimis de tine
costă o transmisie, plus câte una pentru fiecare repetor care îl aude. La un
ciclu de funcționare de 10%, un repetor poate trimite aproximativ 680 de
pachete pe oră, iar toți cei din jurul lui împart acest număr. Un mesaj care
călătorește mai departe decât este nevoie consumă o parte din el.

**Trimite către cea mai mică regiune care ajunge la persoanele cărora le
scrii.** Regiunile sunt imbricate: o țară, o provincie, un grup local,
fiecare cu propriul cod, de exemplu `nl`, `nl-ov` și `nl-ov-zwo`. Un mesaj
pentru `nl-ov-zwo` rămâne la repetoarele din acel grup. Pune fiecare repetor
doar în regiunile pe care le deservește. [Grupul tău local](/community/) știe
care sunt acelea.

**Limitează ce transmite mai departe repetorul tău.** Două setări țin aproape
de casă traficul care nu are nevoie să călătorească departe:

```text
set flood.max.advert 3
set flood.max.unscoped 1
```

- `flood.max.advert 3`: anunțurile, care fac cunoscut un nod în mesh,
  parcurg cel mult 3 salturi.
- `flood.max.unscoped 1`: un mesaj fără regiune trece prin cel mult un
  repetor.
