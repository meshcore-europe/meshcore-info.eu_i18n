---
title: Sestavi konfiguracijo mostu
lead: 'Kar sliši tvoj repetitor, pošlji poljubnemu posredniku MQTT: svojemu ali orodju Analyzer. Pošiljanje opravi računalnik ob repetitorju.'
description: Na Raspberry Pi ali drugem računalniku zaženi meshcoretomqtt in pošlji, kar repetitor MeshCore sliši prek USB, svojemu posredniku MQTT, orodju MeshCore Analyzer ali obema.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'e0f7daa0'
  seeded: '2026-11-02'
  fields: {title: 'fd2dd667', lead: 'fa0c29ce', description: 'ed719ece'}
  sections: ['af5761f3', 'dca6b13e', '06316a22', '61b943e5', '55d5754a']
  blocks: ['af5761f3', '231a92ad', 'b80540ea', '46961e94', '51a4e1da', 'b066c819', 'b3d5ca4d', 'fb38b5f9', '7c1f4a97', '789a975f', 'a303d7b9', '04e0dbe0', '04087e05', 'cdaee24b', '2eaf18e9', '726148ad']
---

Repetitor je vozlišče, ki sporočila posreduje naprej. Njegov promet želiš imeti na posredniku MQTT: na svojem za nadzorno ploščo ali podatkovno bazo ali na posredniku orodja [MeshCore Analyzer](https://meshcore-analyzer.eu/). Ali pa tvoj repetitor nima svojega Wi-Fi-ja, ob njem pa stoji Raspberry Pi ali strežnik. [meshcoretomqtt](https://github.com/Cisien/meshcoretomqtt), orodje skupnosti, je most: promet pošilja s tega računalnika. Repetitor še naprej posreduje sporočila, ker most samo bere, kar repetitor beleži prek USB.

## Kaj potrebuješ {#need}

- Repetitor z vgrajenim beleženjem paketov (spodaj).
- Raspberry Pi Zero, 2, 3 ali 4 ali kateri koli računalnik z Linuxom ali macOS-om, s Pythonom 3.11 ali novejšim.
- Podatkovni kabel USB med obema napravama.

Standardna programska oprema repetitorja iz flasherja ne beleži paketov. Programsko opremo repetitorja zgradi sam iz [izvorne kode MeshCore](https://github.com/meshcore-dev/MeshCore) in gradnji za svojo ploščo dodaj to zastavico:

```text
-D MESH_PACKET_LOGGING=1
```

## Namestitev {#install}

Repetitor priključi na računalnik, nato na tem računalniku zaženi namestitveni skript orodja meshcoretomqtt:

```text
curl -fsSL https://raw.githubusercontent.com/Cisien/meshcoretomqtt/main/install.sh | sudo bash
```

Skript namesti most kot storitev, ki se zažene skupaj z računalnikom, in te vpraša, katerim posrednikom naj pošilja. Orodja Analyzer na tem seznamu ni: dodaš ga v spodnji konfiguracijski datoteki. Tvoje nastavitve so v datoteki `/etc/mctomqtt/config.d/99-user.toml`. Posodobitev te datoteke nikoli ne prepiše.

## Posredniki {#brokers}

Vsak posrednik dobi svoj blok `[[broker]]`, zato lahko en repetitor hkrati pošilja več posrednikom. Pri svojem posredniku uporabiš uporabniško ime in geslo ali pa prijave sploh ni (`method = "none"`). MeshCore Analyzer namesto tega zahteva žeton, ki ga podpiše ključ tvojega repetitorja:

- naslov `mqtt.meshcore-analyzer.eu`, vrata `443`, prek varnega websocketa;
- občinstvo žetona je isti naslov.

## Tvoja konfiguracijska datoteka {#config}

Vsebino datoteke `/etc/mctomqtt/config.d/99-user.toml` zamenjaj s spodnjo. Vpiši kodo letališča, ki je najbližje tvojemu repetitorju (na primer `AMS`), in vrata USB, na katera je priključen repetitor. Nato dodaj svojega posrednika. Bloka, ki ga ne potrebuješ, izpusti.

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

Po vsaki spremembi znova zaženi storitev (v Linuxu `sudo systemctl restart mctomqtt`). Tvoj repetitor se nato v orodju Analyzer prikaže pod svojim imenom kot opazovalec, torej vozlišče, ki nalaga, kar sliši. Vse druge nastavitve najdeš v [README orodja meshcoretomqtt](https://github.com/Cisien/meshcoretomqtt).
