---
title: MQTT na twoim obserwatorze
lead: Twój przekaźnik może zgłaszać przez Wi-Fi to, co słyszy, do MeshCore Analyzer. Przy tym dalej przekazuje wiadomości jak wcześniej.
description: Zamień przekaźnik ESP32 w obserwatora MeshCore dzięki firmware DMC observer. Wgraj go, ustaw Wi-Fi i kod lotniska, wybierz brokery i sprawdź, czy wysyła zgłoszenia do MeshCore Analyzer.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '7b9a9320'
  seeded: '2026-10-31'
  fields: {title: '62626d0f', lead: 'fe9653d4', description: '739edb74'}
  sections: ['962bdbc4', '0ccd4a85', 'fc57f65c', 'ef841ae5', '77d109c5', 'b3e4f8d2', '602a1021']
  blocks: ['75461763', '0e0db0ff', '231a92ad', '49ad02ce', '19b33688', '01e79e69', '6f184c96', '75da543a', '966b1e87', '11f22f4c', '5f85ac9b', 'f74cb809', '1a70c3f5', '9cadc611', '5261e7e9', 'c998ea2d', '393339d9', '803a2dc4', 'cedf8d28', '7c222cec', '6bc50a6a', '59f2a96c', 'a8bd6037', '0d3b84ff', 'e43d5a74', '3bd6439c', '2ddd9432', 'd9df877b', '3283886d', 'f6131e02', '99dc83fb']
---

Obserwator to węzeł, który dodatkowo zgłasza przez MQTT i Wi-Fi to, co słyszy. Każdy obserwator pokazuje trochę więcej siatki w
[MeshCore Analyzer](https://meshcore-analyzer.eu/) i na
[mapach zasięgu](/map/). Z tego poradnika dowiesz się, jak zrobić obserwatora z przekaźnika (węzła, który przekazuje wiadomości dalej). Węzeł nadal działa jako przekaźnik. Zgłoszenia płyną w jedną stronę: nic nie wraca do siatki.

{{< callout type="warning" >}}
Ten poradnik dotyczy **firmware DMC observer**, czyli wersji obserwatora z
[Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore), opartej na
MeshCore 1.18.0. Standardowy MeshCore nie obsługuje MQTT. Wszystkie polecenia poniżej pochodzą z kodu źródłowego firmware w wersji `32dd8ad` z 19 października 2026.
{{< /callout >}}

## Czego potrzebujesz {#need}

- Płytki ESP32 z Wi-Fi, na przykład Heltec V3 lub V4, LilyGo T3S3 albo
  Xiao S3. Pełną listę płytek znajdziesz w [wydaniu](https://github.com/Dutch-MeshCore/MeshCore/releases/tag/observer-mqtt-dev).
  Płytki nRF52, na przykład RAK4631, nie mają Wi-Fi.
- Sieci Wi-Fi 2.4 GHz w miejscu, gdzie stoi płytka.
- Kabla USB do przesyłu danych oraz Chrome, Edge lub Opery na komputerze.
- Kodu lotniska najbliższego twojemu węzłowi. To 3 litery, na przykład `AMS` lub `BRU`.
  Dzięki niemu brokery (serwery, które odbierają twoje zgłoszenia) wiedzą, w jakim rejonie działa twój obserwator.

Nie masz Wi-Fi przy przekaźniku, ale obok stoi komputer?
W takim razie [przygotuj konfigurację mostka](/guides/mctomqtt/).

## Wgraj firmware {#flash}

[Flasher](/firmware/flasher/) na tej stronie ma tylko standardowy MeshCore.
Firmware obserwatora pobierzesz z flashera w
[DutchMeshCore Toolbox](https://toolbox.dutchmeshcore.nl/):

1. Wybierz swoją płytkę, a potem **DutchMeshCore MQTT** (Repeater + Observer + MQTT).
2. Za pierwszym razem wybierz **Full flash**: ta opcja zastępuje całą zawartość
   płytki, łącznie z tablicą partycji. Aktualizacja aplikacji zachowuje obecną zawartość. Używaj jej przy kolejnych aktualizacjach.
3. Skonfiguruj przekaźnik jak zwykle: nazwę, ustawienia radia i hasło administratora. Opis znajdziesz w [poradniku o przekaźniku](/repeater-guide/#config).

Ten firmware to wersja **dev**. Po wpisaniu `ota update` aktualizuje się z kanału dev.
Kanał stable ma wciąż wersję 1.17.1, więc na potrzeby tego poradnika zostań przy dev.

## Ustawienia {#settings}

Otwórz [konsolę szeregową](/firmware/console/) na tej stronie i podłącz płytkę. Wstaw w poleceniach nazwę swojej sieci Wi-Fi, hasło i kod lotniska. Potem wklejaj te linie pojedynczo:

```text
set wifi.ssid MyNetwork
set wifi.pwd MyPassword
set mqtt.iata AMS
reboot
```

Po restarcie płytka łączy się z twoją siecią Wi-Fi i ustawia zegar przez internet. Brokery potrzebują tego zegara, żeby sprawdzić tożsamość twojego obserwatora. Bez kodu lotniska płytka niczego nie zgłasza.

Wolisz klikać niż pisać? Polecenie `start webconfig` uruchamia na płytce stronę ustawień. Jej adres pokaże konsola. Zaloguj się hasłem administratora.

## Sloty brokerów {#brokers}

Jeden slot mieści jednego brokera. Firmware ma od początku wypełnione te sloty:

| Slot | Broker | Prowadzi |
| --- | --- | --- |
| 1 | `dutchmeshcore-1` | Dutch-MeshCore |
| 2 | `dutchmeshcore-2` | Dutch-MeshCore |
| 3 | `meshcore-analyzer-eu` | MeshCore Analyzer |

Płytka bez dodatkowej pamięci (PSRAM), na przykład Heltec V3, ma 3 sloty. Łączy się jednocześnie z 2 z nich, więc Analyzer w slocie 3 nigdy się nie połączy.
Przenieś go do slotu 1:

```text
set mqtt3.preset none
set mqtt1.preset meshcore-analyzer-eu
```

Płytka z PSRAM, na przykład Heltec V4, ma 6 slotów i łączy się jednocześnie z 5. Tu nic nie musisz zmieniać.

Twój węzeł loguje się do każdego brokera własnym kluczem, więc nie potrzebujesz konta.
Polecenie `get mqtt.presets` wyświetla pozostałe brokery społeczności, które zna firmware.

### Własny broker {#own}

Wpisz swojego brokera do wolnego slotu. Podaj jego adres, port, nazwę użytkownika i hasło. Na płytce z PSRAM wolny jest slot 4:

```text
set mqtt4.preset custom
set mqtt4.server mqtt.example.org
set mqtt4.port 1883
set mqtt4.username my_username
set mqtt4.password my_password
```

Na płytce bez PSRAM użyj slotu 2: zamień `mqtt4` na `mqtt2`.
Twój broker zajmie wtedy miejsce `dutchmeshcore-2`.

Port `8883` łączy z szyfrowaniem (TLS). Port `443` też szyfruje, ale przez połączenie webowe (websocket). Każdy inny port łączy bez szyfrowania. Możesz też podać pełny adres, na przykład `wss://mqtt.example.org:9002/mqtt`. Wtedy reguła portów nie obowiązuje.

## Sprawdź, czy działa {#check}

Wpisz `get mqtt.status`. Przy każdym slocie zobaczysz jego stan:

```text
> msgs: on, 1: meshcore-analyzer-eu (ok), 2: dutchmeshcore-2 (ok), q:0
```

- `ok`: połączony.
- `wait`: w slocie brakuje ustawienia, na przykład kodu lotniska.
- `disc`: jeszcze bez połączenia. Sprawdź Wi-Fi poleceniem `get wifi.status`.
- `fail`: slot 7 razy z rzędu nie zdołał się połączyć, w ciągu około 20 minut. Teraz próbuje raz na 30 minut. Sprawdź adres brokera i dane logowania.
- `inactive`: płytka nie ma miejsca na ten slot. Zobacz
  [Sloty brokerów](#brokers).

Potem poszukaj nazwy swojego przekaźnika na
[stronie obserwatorów w Analyzerze](https://meshcore-analyzer.eu/#observers).
Pojawi się tam w ciągu 5 minut razem z tym, co usłyszał.
