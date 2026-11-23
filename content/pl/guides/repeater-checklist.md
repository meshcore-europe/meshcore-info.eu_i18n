---
title: Lista kontrolna przekaźnika
lead: Sprawdź przekaźnik, zanim trafi na górę. Przy każdym punkcie znajdziesz, co sprawdzić, jakim poleceniem to zobaczysz i który poradnik to wyjaśnia.
description: 'Lista kontrolna dla przekaźnika MeshCore, zanim trafi na dach lub maszt: co sprawdzić przez USB, jak go zamontować i jaki test zrobić przed odejściem.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '5bbc2cbe'
  seeded: '2026-11-21'
  fields: {title: 'e982ea2f', lead: '664a2839', description: '01f56863'}
  sections: ['d512dacf', '4d357087', '75706984', '8a484df5', '33fd8c68']
  blocks: ['d512dacf', 'a7ba4c46', '6a427551', '2f0a8827', '2bda1638', '589c7b4f', '5fedefb7', 'e12f330e', 'd6d0b21c']
---

Do przekaźnika na dachu trudno się dostać, więc sprawdź go jeszcze na biurku.
[Poradnik o przekaźnikach](/repeater-guide/) wyjaśnia każdy krok. Wartości,
takie jak preset i limity skoków, znajdziesz w
[ustawieniach dla twojej okolicy](/guides/settings/). Polecenia wpisujesz
przez USB, na przykład w [konsoli szeregowej](/firmware/console/). Ta lista
dotyczy firmware MeshCore v1.18.0.

## Zanim zaczniesz {#start}

- [ ] [Mapy zasięgu](/map/) lub twoja [lokalna grupa](/community/) wskazują,
      że okolica potrzebuje przekaźnika. Zobacz [Czy go potrzebujesz?](/repeater-guide/#need)
- [ ] Właściciel miejsca montażu się zgodził, a ty masz dostęp do przekaźnika
      na potrzeby konserwacji.
- [ ] Akumulator i panel są dobrane do najgorszego zimowego miesiąca. Zobacz
      [Zasilanie i dobór paneli](/repeater-guide/#power).

## Na biurku, przez USB {#usb}

- [ ] Na płytce działa firmware **Repeater**: `ver` pokazuje jego wersję.
      Zobacz [Konfiguracja](/repeater-guide/#config).
- [ ] Na płytce nRF52 odpowiedź na `get bootloader.ver` zawiera `OTAFIX`.
      Zobacz [Aktualizacja przez radio](/repeater-guide/#update).
- [ ] `get radio` pokazuje preset twojej okolicy.
- [ ] `get dutycycle` pokazuje 10. Zobacz [Duty cycle](/repeater-guide/#duty-cycle).
- [ ] `get tx` razem z zyskiem anteny nie przekracza 500 mW e.r.p. Zobacz
      [Moc: e.r.p. i twoja antena](/repeater-guide/#erp).
- [ ] Hasło administratora nie brzmi już `password`.
- [ ] `get guest.password` pokazuje hasło.
- [ ] `get name` pokazuje nazwę, jakiej twoja lokalna grupa używa dla
      swoich przekaźników.
- [ ] `get lat` i `get lon` pokazują położenie miejsca montażu.
- [ ] `get owner.info` pokazuje, jak inni operatorzy mogą się z tobą
      skontaktować.
- [ ] `region` pokazuje regiony twojej okolicy. `get flood.max.advert` i
      `get flood.max.unscoped` pokazują jej limity skoków. Zobacz
      [Ogranicz ruch](/guides/settings/#traffic).
- [ ] Klucz prywatny z `get prv.key` zapisałeś w bezpiecznym miejscu.
- [ ] `clock` pokazuje bieżący czas w UTC.
- [ ] Przy zasilaniu solarnym `powersaving` pokazuje `on`.

## Na dachu {#roof}

- [ ] Antena jest podłączona, zanim przekaźnik dostanie zasilanie.
- [ ] Antena stoi pionowo na szczycie masztu, z dala od metalu. Zobacz
      [Montaż](/guides/antenna/#mounting).
- [ ] Każde złącze zewnętrzne jest uszczelnione, a kabel ma pętlę
      okapową.
- [ ] Obudowa jest zamknięta i ma otwór wentylacyjny lub odpływowy. Zobacz
      [Sprzęt](/repeater-guide/#hardware).

## Zanim odejdziesz {#leave}

- [ ] Z daleka twój companion łączy się z przekaźnikiem w aplikacji.
- [ ] Wysłałeś `advert`, więc węzły w całej siatce dowiadują się o
      przekaźniku.
- [ ] Twoja [lokalna grupa](/community/) wie, że przekaźnik działa.
