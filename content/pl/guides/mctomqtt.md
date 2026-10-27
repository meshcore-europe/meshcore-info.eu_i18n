---
title: Przygotuj konfigurację mostka
lead: 'Wysyłaj to, co słyszy twój przekaźnik, do dowolnego brokera MQTT: własnego albo Analyzera. Wysyłaniem zajmuje się komputer stojący obok przekaźnika.'
description: Uruchom meshcoretomqtt na Raspberry Pi lub innym komputerze, aby to, co przekaźnik MeshCore słyszy, trafiało przez USB do twojego brokera MQTT, do MeshCore Analyzera albo do obu naraz.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: 'e0f7daa0'
  seeded: '2026-10-26'
  fields: {title: 'fd2dd667', lead: 'fa0c29ce', description: 'ed719ece'}
  sections: ['af5761f3', 'dca6b13e', '06316a22', '61b943e5', '55d5754a']
---

Przekaźnik to węzeł, który przekazuje wiadomości dalej. Chcesz mieć jego ruch na
brokerze MQTT: własnym, pod dashboard albo bazę danych, lub na brokerze
[MeshCore Analyzera](https://meshcore-analyzer.eu/). Albo twój przekaźnik nie ma
własnego Wi-Fi, ale obok stoi Raspberry Pi lub serwer.
[meshcoretomqtt](https://github.com/Cisien/meshcoretomqtt), narzędzie społeczności,
jest tym mostkiem: wysyła ruch z tego komputera. Przekaźnik nadal przekazuje,
bo mostek tylko odczytuje to, co przekaźnik loguje przez USB.

## Czego potrzebujesz {#need}

- Przekaźnika zbudowanego z logowaniem pakietów (poniżej).
- Raspberry Pi Zero, 2, 3 lub 4 albo dowolnego komputera z Linuksem lub macOS,
  z Pythonem 3.11 lub nowszym.
- Kabla USB do transmisji danych łączącego oba urządzenia.

Standardowy firmware przekaźnika z flashera nie loguje pakietów. Zbuduj
firmware przekaźnika samodzielnie ze
[źródeł MeshCore](https://github.com/meshcore-dev/MeshCore), dodając tę flagę
do builda swojej płytki:

```text
-D MESH_PACKET_LOGGING=1
```

## Instalacja {#install}

Podłącz przekaźnik do komputera, a potem uruchom na tym komputerze skrypt
instalacyjny meshcoretomqtt:

```text
curl -fsSL https://raw.githubusercontent.com/Cisien/meshcoretomqtt/main/install.sh | sudo bash
```

Skrypt instaluje mostek jako usługę startującą razem z komputerem i pyta,
do których brokerów wysyłać. Analyzera nie ma na tej liście; dodasz go w pliku
konfiguracyjnym poniżej. Twoje własne ustawienia są w pliku
`/etc/mctomqtt/config.d/99-user.toml`; aktualizacja nigdy go nie nadpisuje.

## Brokery {#brokers}

Każdy broker dostaje własny blok `[[broker]]`, więc jeden przekaźnik może zasilać
kilka naraz. Twój własny broker przyjmuje nazwę użytkownika i hasło albo
działa bez logowania (`method = "none"`).
MeshCore Analyzer przyjmuje zamiast tego token, który podpisuje klucz twojego przekaźnika:

- adres `mqtt.meshcore-analyzer.eu`, port `443`, przez bezpieczny websocket;
- audience tokenu to ten sam adres.

## Twój plik konfiguracyjny {#config}

Zastąp zawartość pliku `/etc/mctomqtt/config.d/99-user.toml` poniższym. Wpisz
kod lotniska najbliższego twojemu przekaźnikowi (na przykład `AMS`) oraz port USB,
do którego podłączony jest przekaźnik. Potem dodaj własny broker. Blok, którego
nie potrzebujesz, pomiń.

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

Po zmianie zrestartuj usługę (`sudo systemctl restart mctomqtt` na Linuksie).
Twój przekaźnik pojawi się wtedy w Analyzerze jako obserwator, czyli węzeł,
który przesyła to, co słyszy, pod własną nazwą przekaźnika. Wszystkie pozostałe
ustawienia opisuje
[README meshcoretomqtt](https://github.com/Cisien/meshcoretomqtt).
