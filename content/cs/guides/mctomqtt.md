---
title: Sestav konfiguraci mostu
lead: 'Posílej to, co tvůj repeater slyší, do libovolného MQTT brokeru: do vlastního nebo do Analyzeru. Odesílání obstarává počítač vedle repeateru.'
description: Spusť meshcoretomqtt na Raspberry Pi nebo jiném počítači. Bude posílat to, co repeater MeshCore slyší přes USB, do tvého MQTT brokeru, do MeshCore Analyzeru, nebo do obou.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'e0f7daa0'
  seeded: '2026-10-31'
  fields: {title: 'fd2dd667', lead: 'fa0c29ce', description: 'ed719ece'}
  sections: ['af5761f3', 'dca6b13e', '06316a22', '61b943e5', '55d5754a']
  blocks: ['af5761f3', '231a92ad', 'b80540ea', '46961e94', '51a4e1da', 'b066c819', 'b3d5ca4d', 'fb38b5f9', '7c1f4a97', '789a975f', 'a303d7b9', '04e0dbe0', '04087e05', 'cdaee24b', '2eaf18e9', '726148ad']
---

Repeater je uzel, který předává zprávy dál. Chceš mít jeho provoz na MQTT
brokeru: na vlastním pro dashboard nebo databázi, nebo na brokeru
[MeshCore Analyzeru](https://meshcore-analyzer.eu/). Nebo tvůj repeater nemá
vlastní Wi-Fi, ale vedle něj stojí Raspberry Pi nebo server.
Mostem je [meshcoretomqtt](https://github.com/Cisien/meshcoretomqtt), nástroj
od komunity: provoz odesílá z toho počítače. Tvůj repeater dál opakuje zprávy,
protože most jen čte to, co repeater zapisuje do logu přes USB.

## Co potřebuješ {#need}

- Repeater sestavený s logováním paketů (viz níže).
- Raspberry Pi Zero, 2, 3 nebo 4, nebo libovolný počítač s Linuxem či macOS,
  vždy s Pythonem 3.11 nebo novějším.
- Datový USB kabel mezi nimi.

Standardní firmware repeateru z flasheru pakety neloguje. Firmware repeateru
si sestav sám ze [zdrojového kódu MeshCore](https://github.com/meshcore-dev/MeshCore).
Do sestavení pro svou desku přidej tento příznak:

```text
-D MESH_PACKET_LOGGING=1
```

## Instalace {#install}

Připoj repeater k počítači. Pak na tom počítači spusť instalační skript
meshcoretomqtt:

```text
curl -fsSL https://raw.githubusercontent.com/Cisien/meshcoretomqtt/main/install.sh | sudo bash
```

Skript nainstaluje most jako službu, která se spouští s počítačem. Zeptá se tě,
do kterých brokerů má posílat. Analyzer v tom seznamu není, přidáš ho
v konfiguračním souboru níže. Tvoje vlastní nastavení jsou v souboru
`/etc/mctomqtt/config.d/99-user.toml`. Aktualizace tento soubor nikdy nepřepíše.

## Brokery {#brokers}

Každý broker má vlastní blok `[[broker]]`, takže jeden repeater může posílat
data do několika brokerů současně. Do vlastního brokeru se přihlásíš uživatelským jménem
a heslem, nebo bez přihlášení (`method = "none"`).
MeshCore Analyzer místo toho vyžaduje token, který podepisuje klíč tvého repeateru:

- adresa `mqtt.meshcore-analyzer.eu`, port `443`, přes zabezpečený websocket;
- audience tokenu je stejná adresa.

## Tvůj konfigurační soubor {#config}

Nahraď obsah souboru `/etc/mctomqtt/config.d/99-user.toml` tímto. Doplň kód
letiště nejbližšího k tvému repeateru (třeba `AMS`) a USB port, na kterém je
repeater připojený. Pak přidej svůj vlastní broker. Blok, který nepotřebuješ,
vynech.

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

Po každé změně službu restartuj (na Linuxu `sudo systemctl restart mctomqtt`).
Tvůj repeater se pak v Analyzeru objeví jako observer, tedy uzel, který nahrává
to, co slyší. Uvidíš ho pod vlastním jménem repeateru. Všechna ostatní nastavení
najdeš v [README k meshcoretomqtt](https://github.com/Cisien/meshcoretomqtt).
