---
title: Sortu zubi-konfigurazio bat
lead: 'Bidali zure errepikagailuak entzuten duena edozein MQTT brokerretara: zeurera edo Analyzer-era. Errepikagailuaren ondoan dagoen ordenagailu batek egiten du bidalketa.'
description: Exekutatu meshcoretomqtt Raspberry Pi batean edo beste ordenagailu batean. Horrela, MeshCore errepikagailu batek entzuten duena USB bidez jaso eta zure MQTT brokerrera, MeshCore Analyzer-era edo bietara bidaltzen duzu.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'e0f7daa0'
  seeded: '2026-11-02'
  fields: {title: 'fd2dd667', lead: 'fa0c29ce', description: 'ed719ece'}
  sections: ['af5761f3', 'dca6b13e', '06316a22', '61b943e5', '55d5754a']
  blocks: ['af5761f3', '231a92ad', 'b80540ea', '46961e94', '51a4e1da', 'b066c819', 'b3d5ca4d', 'fb38b5f9', '7c1f4a97', '789a975f', 'a303d7b9', '04e0dbe0', '04087e05', 'cdaee24b', '2eaf18e9', '726148ad']
---

Errepikagailua mezuak birbidaltzen dituen nodoa da. Haren trafikoa MQTT
broker batean nahi duzu: zeurean, panel edo datu-base baterako, edo
[MeshCore Analyzer](https://meshcore-analyzer.eu/)-enean. Edo zure
errepikagailuak ez du Wi-Fi propiorik, baina Raspberry Pi bat edo zerbitzari bat
du ondoan. [meshcoretomqtt](https://github.com/Cisien/meshcoretomqtt), komunitateko
tresna bat, da zubia: ordenagailu horretatik bidaltzen du trafikoa. Zure
errepikagailuak errepikatzen jarraitzen du, zubiak errepikagailuak USB bidez
erregistratzen duena baino ez baitu irakurtzen.

## Zer behar duzun {#need}

- Paketeen erregistroarekin konpilatutako errepikagailu bat (ikus behean).
- Raspberry Pi Zero, 2, 3 edo 4 bat, edo edozein Linux edo macOS ordenagailu,
  Python 3.11 edo berriagoarekin.
- USB datu-kable bat bien artean.

Flasher-eko errepikagailu-firmware estandarrak ez ditu paketeak erregistratzen.
Konpilatu zeuk errepikagailuaren firmwarea
[MeshCore iturburu-kodetik](https://github.com/meshcore-dev/MeshCore), eta gehitu
ikur hau zure plakaren konpilazioari:

```text
-D MESH_PACKET_LOGGING=1
```

## Instalazioa {#install}

Konektatu errepikagailua ordenagailura, eta exekutatu meshcoretomqtt-en instalazio
scripta ordenagailu horretan:

```text
curl -fsSL https://raw.githubusercontent.com/Cisien/meshcoretomqtt/main/install.sh | sudo bash
```

Scriptak zubia zerbitzu gisa instalatzen du, eta zerbitzua ordenagailuarekin batera
abiarazten da. Zein brokerretara bidali nahi duzun ere galdetzen dizu. Analyzer ez
dago zerrenda horretan: behean dagoen konfigurazio-fitxategian gehitzen duzu. Zure
ezarpenak `/etc/mctomqtt/config.d/99-user.toml` fitxategian daude. Eguneratzeek ez
dute inoiz fitxategi hori gainidazten.

## Brokerrak {#brokers}

Broker bakoitzak bere `[[broker]]` blokea du, beraz errepikagailu batek hainbat
brokerri bidal diezaieke trafikoa aldi berean. Zure brokerrak erabiltzaile-izena eta
pasahitza eskatzen ditu, edo batere saio-hasierarik ez (`method = "none"`).
MeshCore Analyzer-ek, horren ordez, token bat eskatzen du, eta zure errepikagailuaren
gakoak sinatzen du token hori:

- helbidea `mqtt.meshcore-analyzer.eu`, ataka `443`, websocket seguru baten bidez;
- tokenaren audientzia helbide bera da.

## Zure konfigurazio-fitxategia {#config}

Ordeztu `/etc/mctomqtt/config.d/99-user.toml` fitxategiaren edukia honekin. Idatzi
zure errepikagailutik hurbilen dagoen aireportuaren kodea (adibidez, `AMS`) eta
errepikagailua konektatuta dagoen USB ataka. Ondoren, gehitu zure brokerra. Kendu
behar ez duzun blokea.

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

Aldaketa bat egin ondoren, berrabiarazi zerbitzua (`sudo systemctl restart mctomqtt`
Linux-en). Orduan, zure errepikagailua behatzaile gisa agertuko da Analyzer-en, bere
izenarekin. Behatzailea entzuten duena igotzen duen nodoa da. Gainerako ezarpen guztiak
[meshcoretomqtt-en README fitxategian](https://github.com/Cisien/meshcoretomqtt)
aurkituko dituzu.
