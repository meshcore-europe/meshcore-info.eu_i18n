---
title: Híd beállítása
lead: 'Küldd el, amit az átjátszód hall, bármelyik MQTT brokerre: a sajátodra vagy az Analyzerére. A küldést az átjátszó mellett álló számítógép végzi.'
description: Futtasd a meshcoretomqtt programot egy Raspberry Pi-n vagy más számítógépen, hogy a MeshCore átjátszó által hallott forgalmat USB-n át a saját MQTT brokeredre, a MeshCore Analyzerre vagy mindkettőre továbbítsd.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: 'e0f7daa0'
  seeded: '2026-10-26'
  fields: {title: 'fd2dd667', lead: 'fa0c29ce', description: 'ed719ece'}
  sections: ['af5761f3', 'dca6b13e', '06316a22', '61b943e5', '55d5754a']
---

Az átjátszó olyan csomópont, amely továbbadja az üzeneteket. A forgalmát egy MQTT
brokeren szeretnéd látni: a sajátodon egy műszerfalhoz vagy adatbázishoz, vagy a
[MeshCore Analyzer](https://meshcore-analyzer.eu/) brokerén. Vagy az átjátszódnak nincs
saját Wi-Fi-je, de mellette áll egy Raspberry Pi vagy egy szerver.
A [meshcoretomqtt](https://github.com/Cisien/meshcoretomqtt), egy közösségi eszköz,
a híd: erről a számítógépről küldi tovább a forgalmat. Az átjátszód közben továbbra is
átjátszik, mert a híd csak azt olvassa, amit az USB-n naplóz.

## Mire van szükséged {#need}

- Egy csomagnaplózással fordított átjátszó (lásd lent).
- Egy Raspberry Pi Zero, 2, 3 vagy 4, vagy bármilyen Linux vagy macOS számítógép Python
  3.11 vagy újabb verzióval.
- Egy USB adatkábel a kettő között.

A flasherből származó szabványos átjátszó firmware nem naplózza a csomagokat. Fordítsd le
az átjátszó firmware-t magad a
[MeshCore forráskódból](https://github.com/meshcore-dev/MeshCore), és add hozzá ezt a
kapcsolót a lapod buildjéhez:

```text
-D MESH_PACKET_LOGGING=1
```

## Telepítés {#install}

Csatlakoztasd az átjátszót a számítógéphez, majd futtasd rajta a meshcoretomqtt
telepítő szkriptjét:

```text
curl -fsSL https://raw.githubusercontent.com/Cisien/meshcoretomqtt/main/install.sh | sudo bash
```

A szkript szolgáltatásként telepíti a hidat, amely a számítógéppel együtt indul, és
megkérdezi, mely brokerekre küldjön. Az Analyzer nincs ebben a listában; azt a lenti
konfigurációs fájlban adod hozzá. A saját beállításaid itt vannak:
`/etc/mctomqtt/config.d/99-user.toml`; frissítéskor ez a fájl sosem íródik felül.

## Brokerek {#brokers}

Minden broker saját `[[broker]]` blokkot kap, így egy átjátszó egyszerre többet is
elláthat. A saját brokered felhasználónevet és jelszót kér, vagy semmilyen bejelentkezést
(`method = "none"`).
A MeshCore Analyzer ehelyett tokent kér, amelyet az átjátszód kulcsa ír alá:

- cím: `mqtt.meshcore-analyzer.eu`, port: `443`, biztonságos websocketen át;
- a token célközönsége (audience) ugyanez a cím.

## A konfigurációs fájlod {#config}

Cseréld le a `/etc/mctomqtt/config.d/99-user.toml` tartalmát erre. Írd be az
átjátszódhoz legközelebbi repülőtér kódját (például `AMS`) és az USB portot, amelyen az
átjátszód van. Ezután add hozzá a saját brokeredet. Hagyd ki azt a blokkot, amelyre nincs
szükséged.

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

Módosítás után indítsd újra a szolgáltatást (Linuxon: `sudo systemctl restart mctomqtt`).
Az átjátszód ezután megfigyelőként jelenik meg az Analyzeren, vagyis olyan csomópontként,
amely feltölti, amit hall, az átjátszód saját neve alatt. Minden további beállítást a
[meshcoretomqtt README](https://github.com/Cisien/meshcoretomqtt) tartalmaz.
