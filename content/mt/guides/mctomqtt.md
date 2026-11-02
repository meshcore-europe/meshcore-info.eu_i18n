---
title: Ibni konfigurazzjoni ta' bridge
lead: 'Ibgħat dak li jisma'' r-repeater tiegħek lil kwalunkwe broker MQTT: tiegħek, jew l-Analyzer. Kompjuter ħdejn ir-repeater jieħu ħsieb il-bgħit.'
description: Ħaddem meshcoretomqtt fuq Raspberry Pi jew kompjuter ieħor biex dak li jisma' repeater ta' MeshCore jasal permezz tal-USB għand il-broker MQTT tiegħek, il-MeshCore Analyzer, jew it-tnejn.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'e0f7daa0'
  seeded: '2026-11-02'
  fields: {title: 'fd2dd667', lead: 'fa0c29ce', description: 'ed719ece'}
  sections: ['af5761f3', 'dca6b13e', '06316a22', '61b943e5', '55d5754a']
  blocks: ['af5761f3', '231a92ad', 'b80540ea', '46961e94', '51a4e1da', 'b066c819', 'b3d5ca4d', 'fb38b5f9', '7c1f4a97', '789a975f', 'a303d7b9', '04e0dbe0', '04087e05', 'cdaee24b', '2eaf18e9', '726148ad']
---

Repeater huwa node li jgħaddi l-messaġġi. Trid it-traffiku tiegħu fuq broker MQTT:
il-broker tiegħek għal dashboard jew database, jew dak tal-[MeshCore Analyzer](https://meshcore-analyzer.eu/).
Jew ir-repeater tiegħek m'għandux Wi-Fi tiegħu, imma għandek Raspberry Pi jew server ħdejh.
[meshcoretomqtt](https://github.com/Cisien/meshcoretomqtt), għodda tal-komunità,
hija l-bridge: tibgħat it-traffiku minn dak il-kompjuter. Ir-repeater tiegħek
ikompli jgħaddi l-messaġġi, għax il-bridge jaqra biss dak li r-repeater jirreġistra fuq l-USB.

## X'għandek bżonn {#need}

- Repeater mibni bil-packet logging (ara hawn taħt).
- Raspberry Pi Zero, 2, 3 jew 4, jew kwalunkwe kompjuter Linux jew macOS, b'Python
  3.11 jew verżjoni aktar ġdida.
- Kejbil USB tad-data bejn it-tnejn.

Il-firmware standard tar-repeater mill-flasher ma jirreġistrax il-pakketti. Ibni
l-firmware tar-repeater int stess mis-[sors ta' MeshCore](https://github.com/meshcore-dev/MeshCore)
u żid din il-flag mal-build tal-bord tiegħek:

```text
-D MESH_PACKET_LOGGING=1
```

## Installazzjoni {#install}

Qabbad ir-repeater mal-kompjuter, imbagħad ħaddem l-iskript tal-installazzjoni ta'
meshcoretomqtt fuq dak il-kompjuter:

```text
curl -fsSL https://raw.githubusercontent.com/Cisien/meshcoretomqtt/main/install.sh | sudo bash
```

L-iskript jinstalla l-bridge bħala servizz li jibda meta jixgħel il-kompjuter, u jistaqsik lil
liema brokers trid tibgħat. L-Analyzer mhuwiex f'dik il-lista; iżżidu fil-fajl
tal-konfigurazzjoni hawn taħt. Is-settings tiegħek jinsabu fil-fajl
`/etc/mctomqtt/config.d/99-user.toml`; l-ebda aġġornament ma jikteb fuq dak il-fajl.

## Brokers {#brokers}

Kull broker għandu l-blokka `[[broker]]` tiegħu, għalhekk repeater wieħed jista'
jibgħat lil diversi brokers fl-istess ħin. Il-broker tiegħek juża username u password, jew l-ebda login
(`method = "none"`).
Il-MeshCore Analyzer juża token minflok, u ċ-ċavetta tar-repeater tiegħek tiffirmah:

- indirizz `mqtt.meshcore-analyzer.eu`, port `443`, fuq websocket sigur;
- l-audience tat-token hija l-istess indirizz.

## Il-fajl tal-konfigurazzjoni tiegħek {#config}

Ibdel il-kontenut ta' `/etc/mctomqtt/config.d/99-user.toml` b'dan it-test. Daħħal
il-kodiċi tal-eqreb ajruport għar-repeater tiegħek (`AMS`, pereżempju) u l-port USB
li fih hu mqabbad ir-repeater. Imbagħad żid il-broker tiegħek. Ħalli barra kull blokka
li m'għandekx bżonn.

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

Erġa' ibda s-servizz wara kull bidla (`sudo systemctl restart mctomqtt` fuq
Linux). Imbagħad ir-repeater tiegħek jidher fuq l-Analyzer bħala observer, node li
jtella' dak li jisma', taħt l-isem tiegħu stess. Is-settings l-oħra kollha
tarahom fil-[README ta' meshcoretomqtt](https://github.com/Cisien/meshcoretomqtt).
