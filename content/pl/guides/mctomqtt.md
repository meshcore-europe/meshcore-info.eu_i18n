---
title: Konfiguracja mostka
lead: 'Wysyłaj to, co słyszy twój przekaźnik, do dowolnego brokera MQTT: własnego albo do Analyzera. Wysyłaniem zajmuje się komputer obok przekaźnika.'
description: Uruchom meshcoretomqtt na Raspberry Pi lub innym komputerze i wysyłaj to, co przekaźnik MeshCore słyszy przez USB, do własnego brokera MQTT, do MeshCore Analyzera albo do obu.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'e0f7daa0'
  seeded: '2026-10-31'
  fields: {title: 'fd2dd667', lead: 'fa0c29ce', description: 'ed719ece'}
  sections: ['af5761f3', 'dca6b13e', '06316a22', '61b943e5', '55d5754a']
  blocks: ['af5761f3', '231a92ad', 'b80540ea', '46961e94', '51a4e1da', 'b066c819', 'b3d5ca4d', 'fb38b5f9', '7c1f4a97', '789a975f', 'a303d7b9', '04e0dbe0', '04087e05', 'cdaee24b', '2eaf18e9', '726148ad']
---

Przekaźnik to węzeł, który przekazuje wiadomości dalej. Chcesz mieć jego ruch na brokerze MQTT: własnym, na potrzeby dashboardu lub bazy danych, albo na brokerze [MeshCore Analyzera](https://meshcore-analyzer.eu/). Może też twój przekaźnik nie ma własnego Wi-Fi, ale obok niego stoi Raspberry Pi lub serwer. [meshcoretomqtt](https://github.com/Cisien/meshcoretomqtt), narzędzie społeczności, to mostek: wysyła ruch z tego komputera. Twój przekaźnik dalej przekazuje wiadomości, bo mostek tylko odczytuje to, co przekaźnik loguje przez USB.

## Czego potrzebujesz {#need}

- Przekaźnika zbudowanego z logowaniem pakietów (opis poniżej).
- Raspberry Pi Zero, 2, 3 lub 4 albo dowolnego komputera z Linuksem lub macOS, z Pythonem 3.11 lub nowszym.
- Kabla USB do transmisji danych między nimi.

Standardowy firmware przekaźnika z flashera nie loguje pakietów. Zbuduj firmware przekaźnika samodzielnie ze [źródeł MeshCore](https://github.com/meshcore-dev/MeshCore). Do konfiguracji budowania swojej płytki dodaj tę flagę:

```text
-D MESH_PACKET_LOGGING=1
```

## Instalacja {#install}

Podłącz przekaźnik do komputera. Potem uruchom na tym komputerze skrypt instalacyjny meshcoretomqtt:

```text
curl -fsSL https://raw.githubusercontent.com/Cisien/meshcoretomqtt/main/install.sh | sudo bash
```

Skrypt instaluje mostek jako usługę, która startuje razem z komputerem. Pyta też, do których brokerów ma wysyłać dane. Analyzera nie ma na tej liście: dodasz go w pliku konfiguracyjnym poniżej. Twoje własne ustawienia są w pliku `/etc/mctomqtt/config.d/99-user.toml`. Aktualizacja nigdy go nie nadpisuje.

## Brokery {#brokers}

Każdy broker ma własny blok `[[broker]]`. Dzięki temu jeden przekaźnik może wysyłać dane do kilku brokerów jednocześnie. Własny broker wymaga nazwy użytkownika i hasła albo działa bez logowania (`method = "none"`). MeshCore Analyzer wymaga zamiast tego tokenu, który twój przekaźnik podpisuje swoim kluczem:

- adres `mqtt.meshcore-analyzer.eu`, port `443`, przez bezpieczny websocket;
- odbiorca (audience) tokenu to ten sam adres.

## Twój plik konfiguracyjny {#config}

Zastąp zawartość pliku `/etc/mctomqtt/config.d/99-user.toml` poniższym tekstem. Wpisz kod lotniska najbliższego twojemu przekaźnikowi (na przykład `AMS`). Wpisz też port USB, do którego podłączony jest przekaźnik. Potem dodaj własny broker. Pomiń blok, którego nie potrzebujesz.

```toml
[general]
iata = "AMS"

[serial]
ports = ["/dev/ttyACM0"]

# Your own broker
[[broker]]
name = "my-broker"
enabled = true
server = "mqtt.example.org"
port = 1883

[broker.auth]
method = "password"
username = "my_username"
password = "my_password"

# The MeshCore Analyzer
[[broker]]
name = "meshcore-analyzer"
enabled = true
server = "mqtt.meshcore-analyzer.eu"
port = 443
transport = "websockets"

[broker.tls]
enabled = true
verify = true

[broker.auth]
method = "token"
audience = "mqtt.meshcore-analyzer.eu"
```

Po każdej zmianie uruchom usługę ponownie (na Linuksie: `sudo systemctl restart mctomqtt`). Wtedy twój przekaźnik pojawi się w Analyzerze jako obserwator, czyli węzeł, który wysyła to, co słyszy. Zobaczysz go pod własną nazwą przekaźnika. Wszystkie pozostałe ustawienia opisuje [README meshcoretomqtt](https://github.com/Cisien/meshcoretomqtt).
