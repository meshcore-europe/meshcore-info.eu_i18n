---
title: Bridge-konfiguráció összeállítása
lead: 'Küldd el, amit az átjátszód hall, bármelyik MQTT brokerre: a sajátodra vagy az Analyzerre. A küldést egy számítógép végzi az átjátszó mellett.'
description: Futtasd a meshcoretomqtt eszközt egy Raspberry Pi-on vagy más számítógépen, és küldd el, amit egy MeshCore átjátszó USB-n keresztül hall, a saját MQTT brokeredre, a MeshCore Analyzerre vagy mindkettőre.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'e0f7daa0'
  seeded: '2026-10-31'
  fields: {title: 'fd2dd667', lead: 'fa0c29ce', description: 'ed719ece'}
  sections: ['af5761f3', 'dca6b13e', '06316a22', '61b943e5', '55d5754a']
  blocks: ['af5761f3', '231a92ad', 'b80540ea', '46961e94', '51a4e1da', 'b066c819', 'b3d5ca4d', 'fb38b5f9', '7c1f4a97', '789a975f', 'a303d7b9', '04e0dbe0', '04087e05', 'cdaee24b', '2eaf18e9', '726148ad']
---

Az átjátszó olyan csomópont, amely továbbadja az üzeneteket. Szeretnéd a forgalmát
egy MQTT brokerre küldeni: a sajátodra egy dashboardhoz vagy adatbázishoz, vagy a
[MeshCore Analyzer](https://meshcore-analyzer.eu/) brokerére. Vagy az átjátszódnak
nincs saját Wi-Fi-je, de áll mellette egy Raspberry Pi vagy egy szerver.
A [meshcoretomqtt](https://github.com/Cisien/meshcoretomqtt), egy közösségi eszköz,
lesz a bridge: ez küldi a forgalmat arról a számítógépről. Az átjátszód közben tovább
ismétel, mert a bridge csak azt olvassa, amit az átjátszó USB-n naplóz.

## Amire szükséged van {#need}

- Egy átjátszó, amelyet csomagnaplózással fordítottál (lásd lent).
- Egy Raspberry Pi Zero, 2, 3 vagy 4, vagy bármilyen Linux vagy macOS
  számítógép, Python 3.11 vagy újabb verzióval.
- Egy USB-adatkábel a kettő között.

A flasherben elérhető szabványos átjátszó firmware nem naplózza a csomagokat.
Az átjátszó firmware-t magadnak kell lefordítanod a
[MeshCore forráskódból](https://github.com/meshcore-dev/MeshCore). Ehhez add hozzá
ezt a kapcsolót a kártyád buildjéhez:

```text
-D MESH_PACKET_LOGGING=1
```

## Telepítés {#install}

Csatlakoztasd az átjátszót a számítógéphez, majd futtasd azon a számítógépen a
meshcoretomqtt telepítőszkriptjét:

```text
curl -fsSL https://raw.githubusercontent.com/Cisien/meshcoretomqtt/main/install.sh | sudo bash
```

A szkript szolgáltatásként telepíti a bridge-et, amely a számítógéppel együtt
indul. Közben megkérdezi, melyik brokerekre küldjön. Az Analyzer nincs ebben a
listában, azt lent, a konfigurációs fájlban adod hozzá. A saját beállításaid a
`/etc/mctomqtt/config.d/99-user.toml` fájlban vannak. Egy frissítés ezt a fájlt
soha nem írja felül.

## Brokerek {#brokers}

Minden broker saját `[[broker]]` blokkot kap, így egy átjátszó egyszerre több
brokert is elláthat. A saját brokeredhez felhasználónév és jelszó kell, vagy
egyáltalán nem kell bejelentkezés (`method = "none"`).
A MeshCore Analyzerhez ehelyett token kell, amelyet az átjátszód kulcsa ír alá:

- a cím `mqtt.meshcore-analyzer.eu`, a port `443`, biztonságos websocketen át;
- a token audience értéke ugyanez a cím.

## A konfigurációs fájlod {#config}

Cseréld le a `/etc/mctomqtt/config.d/99-user.toml` tartalmát erre. Írd be az
átjátszódhoz legközelebbi repülőtér kódját (például `AMS`), és azt az USB-portot,
amelyen az átjátszód van. Utána add hozzá a saját brokeredet. Hagyd ki azt a
blokkot, amelyre nincs szükséged.

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

Módosítás után indítsd újra a szolgáltatást (Linuxon `sudo systemctl restart mctomqtt`).
Ezután az átjátszód observerként, vagyis a hallott forgalmat feltöltő csomópontként
jelenik meg az Analyzeren, a saját nevén. Minden további beállítást a
[meshcoretomqtt README](https://github.com/Cisien/meshcoretomqtt) fájlban találsz.
