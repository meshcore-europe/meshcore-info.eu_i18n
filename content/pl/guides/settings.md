---
title: Zalecane ustawienia
layout: settings
lead: Preset radiowy używany w twojej okolicy i ustawienia, które zmienili twoi sąsiedzi. Wybierz kraj, ustaw preset i skopiuj polecenia.
description: Preset radiowy MeshCore dla poszczególnych obszarów w Europie oraz ustawienia przekaźników i companionów, które lokalne grupy zmieniły względem domyślnych, wraz z poleceniami.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '9547ba62'
  seeded: '2026-10-26'
  fields: {title: 'cfb32983', lead: 'f3f16725', description: 'cb15acd3'}
  sections: ['39848942', '43cde8b4']
---

Każdy obszar poniżej używa własnego presetu radiowego lub zmienia kilka
domyślnych ustawień MeshCore. Wszystko, czego nie wymieniono, zostaje na
wartościach domyślnych, więc zmieniasz tylko to, co zmieniła twoja okolica.
Przekaźnik przekazuje wiadomości dalej dla wszystkich. Companion to węzeł, z
którego piszesz wiadomości, sparowany z telefonem lub laptopem przez Bluetooth
albo USB, lub wyposażony we własny ekran.

W [przewodniku po przekaźnikach](/repeater-guide/#config) znajdziesz, jak
dostać się do linii poleceń swojego przekaźnika. Polecenia wpisujesz
samodzielnie w [konsoli szeregowej](/firmware/console/) na tej stronie. Pod
każdym obszarem możesz też wysłać jego ustawienia przez USB. Przewodnik podaje
również [limity prawne](/repeater-guide/#legal) dla pasma 868 MHz.

## Ogranicz ruch {#traffic}

Te ustawienia obowiązują w każdym obszarze. Każdy przekaźnik przekazuje dalej
każdą wiadomość flood, którą usłyszy. Jedna wiadomość od ciebie to jedna
transmisja, plus jedna na każdy przekaźnik, który ją usłyszy. Przy cyklu pracy
10% przekaźnik może wysłać około 680 pakietów na godzinę, a wszyscy wokół niego
dzielą tę liczbę. Wiadomość, która wędruje dalej, niż musi, zużywa część tej
puli.

**Wysyłaj do najmniejszego regionu, który obejmuje osoby, do których
piszesz.** Regiony są zagnieżdżone: kraj, województwo, lokalna grupa, każdy z
własnym kodem, na przykład `nl`, `nl-ov` i `nl-ov-zwo`. Wiadomość dla
`nl-ov-zwo` zostaje w przekaźnikach tej grupy. Dodawaj każdy przekaźnik tylko
do regionów, które obsługuje. Twoja [lokalna grupa](/community/) wie, które to
regiony.

**Ogranicz to, co przekazuje twój przekaźnik.** Dwa ustawienia trzymają blisko
domu ruch, który nie musi wędrować daleko:

```text
set flood.max.advert 3
set flood.max.unscoped 1
```

- `flood.max.advert 3`: ogłoszenia, które informują siatkę o węźle, pokonują
  najwyżej 3 skoki.
- `flood.max.unscoped 1`: wiadomość bez regionu przechodzi najwyżej przez
  jeden przekaźnik.
