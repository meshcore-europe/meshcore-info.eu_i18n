---
title: Sestav konfiguraci mostu
lead: 'Pošli to, co tvůj repeater slyší, na libovolný MQTT broker: na vlastní, nebo na Analyzer. Odesílání zajistí počítač vedle repeateru.'
description: Spusť meshcoretomqtt na Raspberry Pi nebo jiném počítači a posílej to, co MeshCore repeater slyší přes USB, na vlastní MQTT broker, do MeshCore Analyzeru, nebo na obojí.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: 'e0f7daa0'
  seeded: '2026-10-26'
  fields: {title: 'fd2dd667', lead: 'fa0c29ce', description: 'ed719ece'}
  sections: ['af5761f3', 'dca6b13e', '06316a22', '61b943e5', '55d5754a']
---

Repeater je uzel, který předává zprávy dál. Chceš mít jeho provoz na MQTT
brokeru: na vlastním kvůli dashboardu nebo databázi, nebo na brokeru
[MeshCore Analyzeru](https://meshcore-analyzer.eu/). Nebo tvůj repeater nemá
vlastní Wi-Fi, ale vedle něj stojí Raspberry Pi nebo server.
[meshcoretomqtt](https://github.com/Cisien/meshcoretomqtt), komunitní nástroj,
je tím mostem: posílá provoz z tohoto počítače. Tvůj repeater dál opakuje,
protože most jen čte to, co repeater zapisuje do logu přes USB.

## Co potřebuješ {#need}

- Repeater sestavený s logováním paketů (viz níže).
- Raspberry Pi Zero, 2, 3 nebo 4, nebo libovolný počítač s Linuxem či macOS a
  Pythonem 3.11 nebo novějším.
- Datový kabel USB mezi oběma zařízeními.

Standardní firmware repeateru z flasheru pakety neloguje. Sestav si firmware
repeateru sám ze
[zdrojových kódů MeshCore](https://github.com/meshcore-dev/MeshCore) a do buildu
své desky přidej tento příznak:

```text
-D MESH_PACKET_LOGGING=1
```

## Instalace {#install}

Připoj repeater k počítači a na tom počítači spusť instalační skript
meshcoretomqtt:

```text
curl -fsSL https://raw.githubusercontent.com/Cisien/meshcoretomqtt/main/install.sh | sudo bash
```

Skript nainstaluje most jako službu, která se spouští spolu s počítačem, a
zeptá se, na které brokery má posílat. Analyzer v tom seznamu není; přidáš ho
v konfiguračním souboru níže. Tvoje vlastní nastavení je v souboru
`/etc/mctomqtt/config.d/99-user.toml`; aktualizace tento soubor nikdy nepřepíše.

## Brokery {#brokers}

Každý broker má vlastní blok `[[broker]]`, takže jeden repeater může zásobovat
několik brokerů najednou. Tvůj vlastní broker přijímá uživatelské jméno a heslo,
nebo žádné přihlášení (`method = "none"`).
MeshCore Analyzer místo toho přijímá token, který podepisuje klíč tvého repeateru:

- adresa `mqtt.meshcore-analyzer.eu`, port `443`, přes zabezpečený websocket;
- audience tokenu je stejná adresa.

## Tvůj konfigurační soubor {#config}

Nahraď obsah souboru `/etc/mctomqtt/config.d/99-user.toml` tímto. Doplň kód
letiště nejblíže tvému repeateru (například `AMS`) a USB port, na kterém je tvůj
repeater připojený. Pak přidej vlastní broker. Blok, který nepotřebuješ, vynech.

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

Po změně restartuj službu (na Linuxu `sudo systemctl restart mctomqtt`). Tvůj
repeater se pak v Analyzeru objeví jako observer, tedy uzel, který nahrává to,
co slyší, pod vlastním jménem tvého repeateru. Všechna ostatní nastavení najdeš v
[README meshcoretomqtt](https://github.com/Cisien/meshcoretomqtt).
