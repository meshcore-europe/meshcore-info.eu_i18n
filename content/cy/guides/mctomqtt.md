---
title: Adeiladu ffurfweddiad pont
lead: 'Anfona''r hyn mae dy ailadroddydd yn ei glywed at unrhyw frocer MQTT: dy un di, neu''r Analyzer. Cyfrifiadur wrth ymyl yr ailadroddydd sy''n gwneud yr anfon.'
description: Rheda meshcoretomqtt ar Raspberry Pi neu gyfrifiadur arall i anfon yr hyn mae ailadroddydd MeshCore yn ei glywed dros USB at dy frocer MQTT dy hun, y MeshCore Analyzer, neu'r ddau.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'e0f7daa0'
  seeded: '2026-11-02'
  fields: {title: 'fd2dd667', lead: 'fa0c29ce', description: 'ed719ece'}
  sections: ['af5761f3', 'dca6b13e', '06316a22', '61b943e5', '55d5754a']
  blocks: ['af5761f3', '231a92ad', 'b80540ea', '46961e94', '51a4e1da', 'b066c819', 'b3d5ca4d', 'fb38b5f9', '7c1f4a97', '789a975f', 'a303d7b9', '04e0dbe0', '04087e05', 'cdaee24b', '2eaf18e9', '726148ad']
---

Nod sy'n trosglwyddo negeseuon ymlaen yw ailadroddydd. Rwyt ti eisiau ei draffig ar frocer MQTT: dy frocer di ar gyfer dangosfwrdd neu gronfa ddata, neu un y
[MeshCore Analyzer](https://meshcore-analyzer.eu/). Neu does gan dy ailadroddydd ddim Wi-Fi ei hun, ond mae Raspberry Pi neu weinydd wrth ei ymyl.
Offeryn cymunedol yw [meshcoretomqtt](https://github.com/Cisien/meshcoretomqtt),
a hwnnw yw'r bont: mae'n anfon y traffig o'r cyfrifiadur hwnnw. Mae dy ailadroddydd yn dal ati i ailadrodd, oherwydd mai dim ond darllen yr hyn mae'n ei gofnodi dros USB y mae'r bont.

## Beth sydd ei angen arnat ti {#need}

- Ailadroddydd wedi'i adeiladu gyda chofnodi pecynnau (isod).
- Raspberry Pi Zero, 2, 3 neu 4, neu unrhyw gyfrifiadur Linux neu macOS, gyda Python
  3.11 neu fersiwn mwy diweddar.
- Cebl data USB rhwng y ddau.

Dydy'r cadarnwedd ailadroddydd safonol o'r flasher ddim yn cofnodi pecynnau. Adeilada'r cadarnwedd ailadroddydd dy hun o
[god ffynhonnell MeshCore](https://github.com/meshcore-dev/MeshCore), ac ychwanega'r faner hon at adeiladiad dy fwrdd:

```text
-D MESH_PACKET_LOGGING=1
```

## Gosod {#install}

Plygia'r ailadroddydd i mewn i'r cyfrifiadur, yna rheda sgript gosod meshcoretomqtt ar y cyfrifiadur hwnnw:

```text
curl -fsSL https://raw.githubusercontent.com/Cisien/meshcoretomqtt/main/install.sh | sudo bash
```

Mae'r sgript yn gosod y bont fel gwasanaeth sy'n cychwyn gyda'r cyfrifiadur, ac yn gofyn i ba frocers y dylai anfon. Dydy'r Analyzer ddim yn y rhestr honno; rwyt ti'n ei ychwanegu yn y ffeil ffurfweddu isod. Mae dy osodiadau di yn
`/etc/mctomqtt/config.d/99-user.toml`; dydy diweddariad byth yn trosysgrifo'r ffeil honno.

## Brocers {#brokers}

Mae pob brocer yn cael ei floc `[[broker]]` ei hun, felly gall un ailadroddydd fwydo sawl brocer ar yr un pryd. Mae dy frocer dy hun yn defnyddio enw defnyddiwr a chyfrinair, neu ddim mewngofnodi o gwbl
(`method = "none"`).
Mae'r MeshCore Analyzer yn defnyddio tocyn yn lle hynny, ac allwedd dy ailadroddydd sy'n ei lofnodi:

- cyfeiriad `mqtt.meshcore-analyzer.eu`, porth `443`, dros websocket diogel;
- cynulleidfa (audience) y tocyn yw'r un cyfeiriad.

## Dy ffeil ffurfweddu {#config}

Rho hyn yn lle cynnwys `/etc/mctomqtt/config.d/99-user.toml`. Nodia god y maes awyr agosaf at dy ailadroddydd (`AMS`, er enghraifft) a'r porth USB mae dy ailadroddydd arno. Yna ychwanega dy frocer dy hun. Gad allan unrhyw floc nad oes ei angen arnat ti.

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

Ailgychwyna'r gwasanaeth ar ôl newid (`sudo systemctl restart mctomqtt` ar
Linux). Wedyn mae dy ailadroddydd yn ymddangos ar yr Analyzer fel arsyllwr (observer), nod sy'n uwchlwytho'r hyn mae'n ei glywed, dan enw dy ailadroddydd ei hun. Mae pob gosodiad arall yn
[README meshcoretomqtt](https://github.com/Cisien/meshcoretomqtt).
