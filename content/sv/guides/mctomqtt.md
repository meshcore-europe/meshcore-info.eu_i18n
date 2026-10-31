---
title: Bygg en bryggkonfiguration
lead: 'Skicka det din repeater hör till valfri MQTT-broker: din egen eller Analyzer. En dator bredvid repeatern sköter sändningen.'
description: Kör meshcoretomqtt på en Raspberry Pi eller en annan dator och skicka det en MeshCore-repeater hör via USB till din egen MQTT-broker, MeshCore Analyzer eller båda.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'e0f7daa0'
  seeded: '2026-10-31'
  fields: {title: 'fd2dd667', lead: 'fa0c29ce', description: 'ed719ece'}
  sections: ['af5761f3', 'dca6b13e', '06316a22', '61b943e5', '55d5754a']
  blocks: ['af5761f3', '231a92ad', 'b80540ea', '46961e94', '51a4e1da', 'b066c819', 'b3d5ca4d', 'fb38b5f9', '7c1f4a97', '789a975f', 'a303d7b9', '04e0dbe0', '04087e05', 'cdaee24b', '2eaf18e9', '726148ad']
---

En repeater är en nod som skickar meddelanden vidare. Du vill ha dess trafik på
en MQTT-broker: din egen för en dashboard eller en databas, eller den som
[MeshCore Analyzer](https://meshcore-analyzer.eu/) har. Eller så saknar din
repeater eget WiFi, men en Raspberry Pi eller en server står bredvid den.
[meshcoretomqtt](https://github.com/Cisien/meshcoretomqtt), ett verktyg från
communityn, är bryggan: det skickar trafiken från den datorn. Din
repeater fortsätter att vidarebefordra, eftersom bryggan bara läser det som
repeatern loggar via USB.

## Det här behöver du {#need}

- En repeater som är byggd med paketloggning (se nedan).
- En Raspberry Pi Zero, 2, 3 eller 4, eller valfri dator med Linux eller
  macOS, med Python 3.11 eller nyare.
- En USB-kabel för data mellan dem.

Den vanliga repeater-firmwaren från flashverktyget loggar inte paket. Du får
bygga repeater-firmwaren själv från
[MeshCores källkod](https://github.com/meshcore-dev/MeshCore). Lägg då till
den här flaggan i bygget för ditt kort:

```text
-D MESH_PACKET_LOGGING=1
```

## Installera {#install}

Anslut repeatern till datorn. Kör sedan installationsskriptet för
meshcoretomqtt på den datorn:

```text
curl -fsSL https://raw.githubusercontent.com/Cisien/meshcoretomqtt/main/install.sh | sudo bash
```

Skriptet installerar bryggan som en tjänst som startar med datorn. Det frågar
också vilka brokers du vill skicka till. Analyzer finns inte i den listan; du
lägger till den i konfigurationsfilen nedan. Dina egna inställningar ligger i
`/etc/mctomqtt/config.d/99-user.toml`. En uppdatering skriver aldrig över den
filen.

## Brokers {#brokers}

Varje broker får ett eget `[[broker]]`-block. Därför kan en repeater mata
flera samtidigt. Till din egen broker loggar du in med användarnamn och
lösenord, eller helt utan inloggning (`method = "none"`).
MeshCore Analyzer kräver i stället en token, som din repeaters nyckel
signerar:

- adress `mqtt.meshcore-analyzer.eu`, port `443`, via en säker websocket;
- tokenens audience är samma adress.

## Din konfigurationsfil {#config}

Ersätt innehållet i `/etc/mctomqtt/config.d/99-user.toml` med det här. Fyll
i flygplatskoden närmast din repeater (till exempel `AMS`) och USB-porten som
repeatern sitter i. Lägg sedan till din egen broker. Ta bort ett block som du
inte behöver.

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

Starta om tjänsten efter en ändring (`sudo systemctl restart mctomqtt` på
Linux). Då dyker din repeater upp i Analyzer som observer, alltså en nod som
laddar upp det den hör. Den visas under repeaterns eget namn. I
[README för meshcoretomqtt](https://github.com/Cisien/meshcoretomqtt) hittar
du alla andra inställningar.
