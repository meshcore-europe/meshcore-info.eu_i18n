---
title: Współtwórz
lead: Ten przewodnik piszą, sprawdzają i tłumaczą wolontariusze. Zobacz, jak możesz pomóc, z kontem GitHub albo bez niego.
description: Dodaj swoją społeczność, urządzenie lub projekt, sprawdź tłumaczenie albo popraw przewodnik na meshcore-info.eu.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'f3ed6e9b'
  seeded: '2026-10-31'
  fields: {title: '97b0c61b', lead: 'e9b40d4d', description: '3bd97cd2'}
  sections: ['6e9d4b61', 'aca796d7', 'd4848d5b', '247b2601', '8a60e0d4', '645c82d3', 'c755b654']
  blocks: ['2f9dd6e8', '44167907', 'b020e1a4', 'f2c726cd', '2e9d1fdd', 'b2a902ba', 'b15ce10b', '2be86888', '3db6cb63', '2e3c2fc0', '693a5d9d', '73e33897', '96d8689d', 'c67fd14a', 'f92f7e49', '12ddca6c', 'e947e2a9', '526df4bb', 'e0d3559e']
---

Cała zawartość tej strony znajduje się w publicznym
[repozytorium GitHub](https://github.com/meshcore-europe/meshcore-info.eu). Drobne zmiany
zgłaszasz przez formularz na GitHub (issue). Większe zmiany przesyłasz jako pull
request: to propozycja zmian w plikach, którą sprawdza opiekun. Opiekun
sprawdza każdą zmianę, zanim pojawi się na stronie.

Nie masz konta GitHub? Napisz do nas na [Discord](https://discord.meshcore-info.eu/):
o brakującej grupie, błędnej informacji albo tłumaczeniu, które brzmi dziwnie. Dalej
zajmie się tym wolontariusz.

## Dodaj swoją społeczność {#community}

Prowadzisz lokalną grupę MeshCore, do której każdy może dołączyć? Wypełnij
[formularz społeczności](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-community.yml).
Podaj w nim nazwę, obszar i publiczne linki. Po dodaniu twoja grupa pojawi się
na stronie [Lokalne grupy](/community/) w każdym języku.

## Zaproponuj urządzenie lub projekt {#device-project}

Na [stronie urządzeń](/devices/) podajemy specyfikacje z dokumentacji producentów.
Nigdy nie linkujemy tam do sklepów. Sprzęt zaproponujesz przez
[formularz urządzenia](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-device.yml).
Zbudowałeś aplikację, narzędzie, mostek lub projekt sprzętu dla MeshCore z publicznym kodem źródłowym?
Dodaj go przez
[formularz projektu](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-project.yml).

## Sprawdź tłumaczenie {#translate}

Strony w innych językach powstają najpierw jako tłumaczenia maszynowe. Informacja o tym widnieje na
górze strony. Tłumaczenia mają własne repozytorium,
[meshcore-info.eu_i18n](https://github.com/meshcore-europe/meshcore-info.eu_i18n), więc
nie musisz dotykać kodu strony. Jeśli dobrze znasz jeden z tych języków,
możesz poprawić tłumaczenie:

1. Otwórz stronę i kliknij „Help improve this translation”. Otworzysz wtedy
   plik na GitHub i zmienisz go w przeglądarce.
2. Popraw sformułowania. Linki, kod, liczby i nazwy, takie jak MeshCore, zostaw
   dokładnie tak, jak są.
3. W bloku `translation` na górze zmień `status: ai` na
   `status: human` i zaproponuj zmianę.

Widzisz błędne słowo, ale nie masz czasu go poprawić? Zgłoś je przez
[formularz tłumaczenia](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=translation-bug.yml).

## Popraw przewodnik {#guides}

Przewodniki piszemy najpierw po angielsku i z tej wersji je tłumaczymy. Poprawki
i nowe tematy możesz zgłosić przez
[formularz treści](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=new-content.yml)
albo pull request. Fakty muszą mieć źródło: firmware MeshCore i jego
dokumentację, urząd regulacji radiowej albo producenta. Pisz własnymi słowami.
Krótki cytat ze źródłem jest w porządku.

[Przewodnik dla współtwórców](https://github.com/meshcore-europe/meshcore-info.eu/blob/main/CONTRIBUTING.md)
wyjaśnia, jak pracować nad stroną na własnym komputerze.

## Stan tłumaczeń {#coverage}

„Reviewed” oznacza tłumaczenie sprawdzone
przez człowieka. „Machine” oznacza tłumaczenie maszynowe, jeszcze niesprawdzone.
„Outdated” oznacza, że tekst angielski zmienił się po powstaniu tłumaczenia.
„Missing” oznacza, że strona nie ma jeszcze tłumaczenia.

{{< coverage >}}

## Podziękowania {#credits}

Strona powstała w [Astro](https://astro.build/). Używa krojów pisma
IBM Plex Sans i IBM Plex Mono na licencji SIL Open Font License. Tłumaczenia
stosują
zasady [kiekr-i18n](https://github.com/marcelverdult/kiekr-i18n) i
korzystają z jego glosariuszy MeshCore. Sam MeshCore powstaje w
[meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore).

Teksty i tłumaczenia są dostępne na licencji CC BY 4.0, a kod na licencji
MIT.
