---
title: Współtwórz
lead: Ten przewodnik piszą, sprawdzają i tłumaczą wolontariusze. Oto jak możesz pomóc, z kontem na GitHub lub bez niego.
description: Dodaj swoją społeczność, urządzenie lub projekt, sprawdź tłumaczenie albo popraw przewodnik na meshcore-info.eu.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: 'f3ed6e9b'
  seeded: '2026-10-26'
  fields: {title: '97b0c61b', lead: 'e9b40d4d', description: '3bd97cd2'}
  sections: ['6e9d4b61', 'aca796d7', 'd4848d5b', '247b2601', '8a60e0d4', '645c82d3', 'c755b654']
---

Cała zawartość tej strony znajduje się w publicznym
[repozytorium na GitHub](https://github.com/meshcore-europe/meshcore-info.eu). Drobne zmiany
zgłaszasz przez formularz na GitHub (issue). Większe zmiany trafiają jako pull
request: propozycja zmiany w plikach, którą sprawdza opiekun projektu. Opiekun
sprawdza każdą zmianę, zanim trafi ona na stronę.

Nie masz konta na GitHub? Napisz nam na [Discordzie](https://discord.meshcore-info.eu/):
o brakującej grupie, błędnym fakcie lub tłumaczeniu, które brzmi dziwnie. Resztą
zajmie się wolontariusz.

## Dodaj swoją społeczność {#community}

Prowadzisz lokalną grupę MeshCore, do której każdy może dołączyć? Wypełnij
[formularz społeczności](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-community.yml),
podając nazwę, obszar i publiczne linki. Po dodaniu twoja grupa pojawi się
na stronie [Grupy lokalne](/community/) w każdej wersji językowej.

## Zaproponuj urządzenie lub projekt {#device-project}

[Strona urządzeń](/devices/) zawiera specyfikacje z dokumentacji producentów
i nigdy nie linkuje do sklepów. Sprzęt zgłaszasz przez
[formularz urządzenia](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-device.yml).
Stworzyłeś aplikację, narzędzie, most lub projekt sprzętu dla MeshCore z publicznym
kodem źródłowym? Dodaj go przez
[formularz projektu](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-project.yml).

## Sprawdź tłumaczenie {#translate}

Strony w innych językach powstają najpierw jako tłumaczenia maszynowe i informują
o tym u góry. Tłumaczenia mają własne repozytorium,
[meshcore-info.eu_i18n](https://github.com/meshcore-europe/meshcore-info.eu_i18n), więc
nie musisz dotykać kodu strony. Jeśli dobrze znasz któryś z tych języków,
możesz je poprawić:

1. Otwórz stronę i kliknij „Pomóż ulepszyć to tłumaczenie”. Otworzy się
   plik na GitHub, który możesz edytować w przeglądarce.
2. Popraw sformułowania. Linki, kod, liczby i nazwy takie jak MeshCore
   zostaw dokładnie w takiej postaci, w jakiej są.
3. W bloku `translation` u góry zmień `status: ai` na
   `status: human` i zaproponuj zmianę.

Znalazłeś błędne słowo, ale nie masz czasu go poprawić? Zgłoś je przez
[formularz tłumaczenia](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=translation-bug.yml).

## Popraw przewodnik {#guides}

Przewodniki powstają najpierw po angielsku, a potem są tłumaczone. Poprawki
i nowe tematy zgłaszasz przez
[formularz treści](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=new-content.yml)
lub pull request. Każdy fakt wymaga źródła: firmware MeshCore i jego
dokumentacji, regulatora radiowego lub producenta. Pisz własnymi słowami.
Krótki cytat z podaniem źródła jest w porządku.

[Przewodnik dla współtwórców](https://github.com/meshcore-europe/meshcore-info.eu/blob/main/CONTRIBUTING.md)
wyjaśnia, jak pracować nad stroną na własnym komputerze.

## Stan tłumaczeń {#coverage}

„Sprawdzone” oznacza, że tłumaczenie sprawdziła osoba;
„Maszynowe” oznacza tłumaczenie maszynowe, którego nikt jeszcze nie sprawdził;
„Nieaktualne” oznacza, że tekst angielski zmienił się po wykonaniu tłumaczenia;
„Brak” oznacza, że strona nie ma jeszcze tłumaczenia.

{{< coverage >}}

## Podziękowania {#credits}

Strona jest zbudowana na [Astro](https://astro.build/). Używa krojów pisma
IBM Plex Sans i IBM Plex Mono na licencji SIL Open Font License. Tłumaczenia
stosują
konwencje [kiekr-i18n](https://github.com/marcelverdult/kiekr-i18n) i
korzystają z jego słowników MeshCore. Sam MeshCore jest rozwijany w
[meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore).

Tekst i tłumaczenia są dostępne na licencji CC BY 4.0, kod na licencji
MIT.
