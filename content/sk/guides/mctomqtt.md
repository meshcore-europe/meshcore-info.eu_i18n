---
title: Zostav konfiguráciu mosta
lead: 'Posielaj to, čo tvoj repeater počuje, na ľubovoľný MQTT broker: vlastný alebo Analyzer. Odosielanie má na starosti počítač vedľa repeatera.'
description: Spusti meshcoretomqtt na Raspberry Pi alebo inom počítači a posielaj to, čo repeater MeshCore počuje, cez USB na vlastný MQTT broker, na MeshCore Analyzer alebo na oba.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'e0f7daa0'
  seeded: '2026-11-02'
  fields: {title: 'fd2dd667', lead: 'fa0c29ce', description: 'ed719ece'}
  sections: ['af5761f3', 'dca6b13e', '06316a22', '61b943e5', '55d5754a']
  blocks: ['af5761f3', '231a92ad', 'b80540ea', '46961e94', '51a4e1da', 'b066c819', 'b3d5ca4d', 'fb38b5f9', '7c1f4a97', '789a975f', 'a303d7b9', '04e0dbe0', '04087e05', 'cdaee24b', '2eaf18e9', '726148ad']
---

Repeater je uzol, ktorý posúva správy ďalej. Chceš jeho prevádzku dostať na MQTT
broker: na vlastný pre dashboard alebo databázu, alebo na broker
[MeshCore Analyzera](https://meshcore-analyzer.eu/). Alebo tvoj repeater nemá
vlastnú Wi-Fi, ale vedľa neho stojí Raspberry Pi alebo server.
[meshcoretomqtt](https://github.com/Cisien/meshcoretomqtt), komunitný nástroj,
je tým mostom: prevádzku odosiela z tohto počítača. Tvoj repeater ďalej opakuje
správy, pretože most iba číta to, čo repeater loguje cez USB.

## Čo potrebuješ {#need}

- Repeater zostavený s logovaním paketov (pozri nižšie).
- Raspberry Pi Zero, 2, 3 alebo 4, alebo ľubovoľný počítač s Linuxom či macOS,
  s Pythonom 3.11 alebo novším.
- Dátový USB kábel medzi nimi.

Štandardný firmvér repeatera z flashera pakety neloguje. Firmvér repeatera si
zostav sám zo [zdrojového kódu MeshCore](https://github.com/meshcore-dev/MeshCore)
a do zostavenia pre svoju dosku pridaj tento príznak:

```text
-D MESH_PACKET_LOGGING=1
```

## Inštalácia {#install}

Zapoj repeater do počítača a potom na tomto počítači spusti inštalačný skript
meshcoretomqtt:

```text
curl -fsSL https://raw.githubusercontent.com/Cisien/meshcoretomqtt/main/install.sh | sudo bash
```

Skript nainštaluje most ako službu, ktorá sa spúšťa spolu s počítačom, a opýta sa
ťa, na ktoré brokery má posielať. Analyzer v tomto zozname nie je; pridáš ho
v konfiguračnom súbore nižšie. Tvoje vlastné nastavenia sú v súbore
`/etc/mctomqtt/config.d/99-user.toml`; aktualizácia tento súbor nikdy neprepíše.

## Brokery {#brokers}

Každý broker má vlastný blok `[[broker]]`, takže jeden repeater môže posielať
dáta viacerým brokerom naraz. Do vlastného brokera sa prihlásiš menom a heslom,
alebo sa nemusíš prihlasovať vôbec (`method = "none"`).
MeshCore Analyzer namiesto toho vyžaduje token, ktorý podpisuje kľúč tvojho repeatera:

- adresa `mqtt.meshcore-analyzer.eu`, port `443`, cez zabezpečený websocket;
- audience tokenu je tá istá adresa.

## Tvoj konfiguračný súbor {#config}

Obsah súboru `/etc/mctomqtt/config.d/99-user.toml` nahraď týmto. Doplň kód letiska,
ktoré je najbližšie k tvojmu repeateru (napríklad `AMS`), a USB port, na ktorom je
repeater pripojený. Potom pridaj vlastný broker. Blok, ktorý nepotrebuješ, vynechaj.

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

Po zmene reštartuj službu (na Linuxe `sudo systemctl restart mctomqtt`). Tvoj
repeater sa potom na Analyzeri zobrazí pod svojím menom ako observer, teda uzol,
ktorý odosiela to, čo počuje. Všetky ostatné nastavenia nájdeš
v [README nástroja meshcoretomqtt](https://github.com/Cisien/meshcoretomqtt).
