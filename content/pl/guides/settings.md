---
title: Zalecane ustawienia
layout: settings
lead: Preset radiowy używany w twojej okolicy i ustawienia, które zmienili twoi sąsiedzi. Wybierz kraj, ustaw preset i skopiuj polecenia.
description: Preset radiowy MeshCore dla każdej okolicy w Europie oraz ustawienia przekaźnika i companiona, które lokalne grupy zmieniły względem domyślnych, razem z poleceniami.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '0876215b'
  seeded: '2026-10-31'
  fields: {title: 'cfb32983', lead: 'f3f16725', description: 'cb15acd3'}
  sections: ['39848942', 'd1606fcd']
  blocks: ['8c9e88ea', '50ac6063', '85c2203d', '15f91217', 'bdf5fa4e', '69d8e70b', '28f83120', 'fe27027b']
---

Każda okolica poniżej ma własny preset radiowy albo zmienia kilka domyślnych
ustawień MeshCore. Wszystko, czego tu nie ma, zostaje domyślne. Zmieniasz więc
tylko to, co zmieniła twoja okolica. Przekaźnik przekazuje wiadomości dalej dla
wszystkich. Companion to węzeł, z którego wysyłasz wiadomości. Łączysz go z
telefonem lub laptopem przez Bluetooth albo USB, albo ma własny ekran.

W [poradniku o przekaźnikach](/repeater-guide/#config) znajdziesz opis, jak
dostać się do wiersza poleceń przekaźnika. W [konsoli szeregowej](/firmware/console/)
na tej stronie sam wpisujesz polecenia. Pod każdą okolicą możesz też wysłać jej
ustawienia przez USB. Poradnik podaje też [limity prawne](/repeater-guide/#legal)
dla pasma 868 MHz.

## Ograniczaj ruch {#traffic}

Te ustawienia obowiązują w każdej okolicy. Każdy przekaźnik przekazuje dalej
każdą wiadomość flood, którą usłyszy. Jedna twoja wiadomość to jedna transmisja
i po jednej na każdy przekaźnik, który ją usłyszy. Przy cyklu pracy 10%
przekaźnik może wysłać około 680 pakietów na godzinę. Wszyscy wokół niego
dzielą się tą liczbą. Wiadomość, która leci dalej, niż musi, zużywa jej część.

**Wysyłaj do najmniejszego regionu, który dociera do osób, do których piszesz.**
Regiony zawierają się jeden w drugim: kraj, województwo, lokalna grupa. Każdy
ma własny kod, na przykład `nl`, `nl-ov` i `nl-ov-zwo`. Wiadomość dla
`nl-ov-zwo` zostaje u przekaźników tej grupy. Przekaźnik przekazuje dalej
tylko regiony, które sam ma. Jeśli ma `nl`, nie przekaże przez to `nl-ov`.
Dodaj każdy przekaźnik do każdego regionu, który obsługuje, i tylko do nich.
Twoja [lokalna grupa](/community/) wie, które to są.

**Ogranicz to, co przekazuje twój przekaźnik.** Dwa ustawienia trzymają blisko
domu ruch, który nie musi docierać daleko:

```text
set flood.max.advert 3
set flood.max.unscoped 1
```

- `flood.max.advert 3`: ogłoszenia, którymi węzeł zgłasza się w siatce,
  przechodzą najwyżej 3 skoki.
- `flood.max.unscoped 1`: wiadomość bez regionu przechodzi najwyżej przez
  jeden przekaźnik.
