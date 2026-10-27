---
title: Bygg en bryggkonfiguration
lead: 'Skicka det din repeater hör till valfri MQTT-broker: din egen eller Analyzerns. En dator bredvid repeatern sköter sändningen.'
description: Kör meshcoretomqtt på en Raspberry Pi eller en annan dator för att skicka det en MeshCore-repeater hör över USB till din egen MQTT-broker, MeshCore Analyzer eller båda.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: 'e0f7daa0'
  seeded: '2026-10-26'
  fields: {title: 'fd2dd667', lead: 'fa0c29ce', description: 'ed719ece'}
  sections: ['af5761f3', 'dca6b13e', '06316a22', '61b943e5', '55d5754a']
---

En repeater är en nod som skickar meddelanden vidare. Du vill ha dess trafik på en MQTT-broker: din egen för en dashboard eller en databas, eller den som [MeshCore Analyzer](https://meshcore-analyzer.eu/) har. Eller så saknar din repeater egen Wi-Fi, men en Raspberry Pi eller en server står bredvid den. [meshcoretomqtt](https://github.com/Cisien/meshcoretomqtt), ett verktyg från communityn, är bryggan: det skickar trafiken från den datorn. Din repeater fortsätter att repetera, eftersom bryggan bara läser det den loggar över USB.

## Det här behöver du {#need}

- En repeater byggd med paketloggning (se nedan).
- En Raspberry Pi Zero, 2, 3 eller 4, eller valfri dator med Linux eller macOS, med Python 3.11 eller nyare.
- En USB-datakabel mellan de två.

Standardfirmwaren för repeatern från flashern loggar inga paket. Bygg repeaterfirmwaren själv från [MeshCore-källkoden](https://github.com/meshcore-dev/MeshCore) med den här flaggan tillagd i bygget för ditt kort:

```text
-D MESH_PACKET_LOGGING=1
```

## Installera {#install}

Anslut repeatern till datorn och kör sedan installationsskriptet för meshcoretomqtt på den datorn:

```text
curl -fsSL https://raw.githubusercontent.com/Cisien/meshcoretomqtt/main/install.sh | sudo bash
```

Skriptet installerar bryggan som en tjänst som startar med datorn och frågar vilka brokers den ska skicka till. Analyzern finns inte med i den listan; du lägger till den i konfigurationsfilen nedan. Dina egna inställningar ligger i `/etc/mctomqtt/config.d/99-user.toml`; en uppdatering skriver aldrig över den filen.

## Brokers {#brokers}

Varje broker får sitt eget `[[broker]]`-block, så en repeater kan mata flera samtidigt. Din egen broker tar ett användarnamn och ett lösenord, eller ingen inloggning alls (`method = "none"`). MeshCore Analyzer tar i stället en token, som din repeaters nyckel signerar:

- adress `mqtt.meshcore-analyzer.eu`, port `443`, över en säker websocket;
- tokenens audience är samma adress.

## Din konfigurationsfil {#config}

Ersätt innehållet i `/etc/mctomqtt/config.d/99-user.toml` med det här. Fyll i flygplatskoden närmast din repeater (till exempel `AMS`) och USB-porten som din repeater sitter på. Lägg sedan till din egen broker. Utelämna ett block du inte behöver.

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

Starta om tjänsten efter en ändring (`sudo systemctl restart mctomqtt` på Linux). Din repeater dyker då upp på Analyzern som en observer, en nod som laddar upp det den hör, under din repeaters eget namn. I [README-filen för meshcoretomqtt](https://github.com/Cisien/meshcoretomqtt) hittar du alla övriga inställningar.
