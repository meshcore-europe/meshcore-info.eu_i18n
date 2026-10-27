---
title: MQTT na twoim obserwatorze
lead: Pozwól swojemu przekaźnikowi raportować przez Wi-Fi do MeshCore Analyzer to, co słyszy. Wiadomości przekazuje dalej tak jak dotąd.
description: Zrób z przekaźnika ESP32 obserwatora MeshCore z firmware obserwatora DMC. Wgraj firmware, ustaw Wi-Fi i kod lotniska, wybierz brokery i sprawdź, czy raportuje do MeshCore Analyzer.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '7b9a9320'
  seeded: '2026-10-26'
  fields: {title: '62626d0f', lead: 'fe9653d4', description: '739edb74'}
  sections: ['962bdbc4', '0ccd4a85', 'fc57f65c', 'ef841ae5', '77d109c5', 'b3e4f8d2', '602a1021']
---

Obserwator to węzeł, który dodatkowo raportuje przez Wi-Fi po MQTT to, co słyszy. Każdy obserwator pokazuje nieco więcej siatki w [MeshCore Analyzer](https://meshcore-analyzer.eu/) i na [mapach zasięgu](/map/). Ten poradnik zmienia w obserwatora przekaźnik (węzeł, który przekazuje wiadomości dalej). Przekaźnik dalej przekazuje, a raport idzie w jedną stronę: nic nie wraca do siatki.

{{< callout type="warning" >}}
Ten poradnik dotyczy **firmware obserwatora DMC**, czyli wersji obserwatora z [Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore), opartej na MeshCore 1.18.0. Standardowy MeshCore nie ma MQTT. Każde polecenie poniżej pochodzi ze źródeł firmware w buildzie `32dd8ad` z 19 października 2026.
{{< /callout >}}

## Czego potrzebujesz {#need}

- Płytki ESP32 z Wi-Fi, na przykład Heltec V3 lub V4, LilyGo T3S3 albo
  Xiao S3. [Wydanie](https://github.com/Dutch-MeshCore/MeshCore/releases/tag/observer-mqtt-dev)
  wymienia każdą płytkę. Płytki nRF52, takie jak RAK4631, nie mają Wi-Fi.
- Sieci Wi-Fi 2.4 GHz w miejscu, gdzie stoi płytka.
- Kabla USB do danych oraz Chrome, Edge lub Opery na twoim komputerze.
- Kodu lotniska najbliższego twojemu węzłowi, 3 litery, na przykład `AMS` lub `BRU`.
  Mówi on brokerom (serwerom, które odbierają twoje raporty), w jakim obszarze
  stoi twój obserwator.

Nie masz Wi-Fi tam, gdzie stoi twój przekaźnik, ale masz obok komputer?
Zamiast tego [zbuduj konfigurację mostka](/guides/mctomqtt/).

## Wgraj firmware {#flash}

[Flasher](/firmware/flasher/) na tej stronie ma tylko standardowy MeshCore. Firmware obserwatora wgrasz flasherem w [DutchMeshCore Toolbox](https://toolbox.dutchmeshcore.nl/):

1. Wybierz swoją płytkę, a potem **DutchMeshCore MQTT** (Repeater + Observer + MQTT).
2. Za pierwszym razem wybierz **Full flash**: zastępuje on wszystko na płytce, łącznie z tablicą partycji. Aktualizacja aplikacji zachowuje to, co już jest, i służy do późniejszych aktualizacji.
3. Skonfiguruj przekaźnik jak zwykle: nazwa, preset radia i hasło administratora, tak jak w [poradniku o przekaźniku](/repeater-guide/#config).

Ten firmware to build **dev** i aktualizuje się z kanału dev, gdy wpiszesz `ota update`. Kanał stabilny wciąż ma 1.17.1, więc na potrzeby tego poradnika zostań na dev.

## Ustawienia {#settings}

Otwórz [konsolę szeregową](/firmware/console/) na tej stronie i podłącz płytkę. Wpisz własną sieć Wi-Fi, hasło i kod lotniska, a potem wklejaj te linie po jednej:

```text
set wifi.ssid MyNetwork
set wifi.pwd MyPassword
set mqtt.iata AMS
reboot
```

Po restarcie płytka łączy się z twoim Wi-Fi i ustawia zegar z internetu. Brokery potrzebują tego zegara, aby sprawdzić, kim jest twój obserwator. Bez kodu lotniska nic nie zostanie zaraportowane.

Wolisz klikać niż pisać? `start webconfig` otwiera stronę ustawień na płytce, pod adresem, który pokazuje konsola. Zaloguj się hasłem administratora.

## Sloty brokerów {#brokers}

Jeden slot mieści jednego brokera. Firmware startuje z tymi slotami wypełnionymi:

| Slot | Broker | Prowadzi |
| --- | --- | --- |
| 1 | `dutchmeshcore-1` | Dutch-MeshCore |
| 2 | `dutchmeshcore-2` | Dutch-MeshCore |
| 3 | `meshcore-analyzer-eu` | MeshCore Analyzer |

Płytka bez dodatkowej pamięci (PSRAM), taka jak Heltec V3, ma 3 sloty. Łączy się z 2 z nich naraz, więc Analyzer w slocie 3 nigdy się nie połączy. Przenieś go do slotu 1:

```text
set mqtt3.preset none
set mqtt1.preset meshcore-analyzer-eu
```

Płytka z PSRAM, taka jak Heltec V4, ma 6 slotów i łączy się z 5 naraz. Nie wymaga żadnej zmiany.

Twój węzeł loguje się do każdego brokera własnym kluczem, więc nie potrzebujesz konta. `get mqtt.presets` wypisuje pozostałe brokery społeczności, które zna firmware.

### Twój własny broker {#own}

Wpisz własnego brokera w wolny slot. Podaj jego adres, port, nazwę użytkownika i hasło. Na płytce z PSRAM wolny jest slot 4:

```text
set mqtt4.preset custom
set mqtt4.server mqtt.example.org
set mqtt4.port 1883
set mqtt4.username my_username
set mqtt4.password my_password
```

Na płytce bez PSRAM użyj zamiast tego slotu 2: zamień `mqtt4` na `mqtt2`. Twój broker zajmie wtedy miejsce `dutchmeshcore-2`.

Port `8883` łączy się szyfrowanie (TLS), port `443` szyfrowanie przez połączenie webowe (websocket), a każdy inny port bez szyfrowania. Możesz też podać pełny adres, na przykład `wss://mqtt.example.org:9002/mqtt`; wtedy reguła portów nie obowiązuje.

## Sprawdź, czy działa {#check}

Wpisz `get mqtt.status`. Każdy slot pokazuje swój stan:

```text
> msgs: on, 1: meshcore-analyzer-eu (ok), 2: dutchmeshcore-2 (ok), q:0
```

- `ok`: połączony.
- `wait`: w slocie brakuje ustawienia, na przykład kodu lotniska.
- `disc`: jeszcze nie połączony. Sprawdź Wi-Fi poleceniem `get wifi.status`.
- `fail`: slot nie połączył się 7 razy z rzędu, w ciągu około 20 minut, i teraz próbuje raz na 30 minut. Sprawdź adres brokera i dane logowania.
- `inactive`: płytka nie ma miejsca na ten slot. Zobacz [Sloty brokerów](#brokers).

Potem poszukaj nazwy swojego przekaźnika na [stronie obserwatorów w Analyzer](https://meshcore-analyzer.eu/#observers). Pojawia się tam w ciągu 5 minut, razem z tym, co usłyszał.
