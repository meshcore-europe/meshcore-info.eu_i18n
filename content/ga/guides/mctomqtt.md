---
title: Cruthaigh cumraíocht droichid
lead: 'Seol a gcloiseann d''athsheoltóir chuig bróicéir MQTT ar bith: do cheann féin, nó an Analyzer. Is ríomhaire in aice leis an athsheoltóir a dhéanann an seoladh.'
description: Rith meshcoretomqtt ar Raspberry Pi nó ar ríomhaire eile chun a gcloiseann athsheoltóir MeshCore a sheoladh thar USB chuig do bhróicéir MQTT féin, chuig an MeshCore Analyzer, nó chuig an dá cheann.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'e0f7daa0'
  seeded: '2026-11-02'
  fields: {title: 'fd2dd667', lead: 'fa0c29ce', description: 'ed719ece'}
  sections: ['af5761f3', 'dca6b13e', '06316a22', '61b943e5', '55d5754a']
  blocks: ['af5761f3', '231a92ad', 'b80540ea', '46961e94', '51a4e1da', 'b066c819', 'b3d5ca4d', 'fb38b5f9', '7c1f4a97', '789a975f', 'a303d7b9', '04e0dbe0', '04087e05', 'cdaee24b', '2eaf18e9', '726148ad']
---

Is nód é athsheoltóir a chuireann teachtaireachtaí ar aghaidh. Tá a thrácht uait ar bhróicéir MQTT: do cheann féin le haghaidh deais nó bunachair sonraí, nó ceann an
[MeshCore Analyzer](https://meshcore-analyzer.eu/). Nó níl Wi-Fi dá chuid féin ag d'athsheoltóir, ach tá Raspberry Pi nó freastalaí lena thaobh.
Is é [meshcoretomqtt](https://github.com/Cisien/meshcoretomqtt), uirlis phobail,
an droichead: seolann sé an trácht ón ríomhaire sin. Leanann d'athsheoltóir air ag athsheoladh, mar ní dhéanann an droichead ach an méid a logálann d'athsheoltóir thar USB a léamh.

## A bhfuil uait {#need}

- Athsheoltóir a tógadh le logáil paicéad (féach thíos).
- Raspberry Pi Zero, 2, 3 nó 4, nó ríomhaire Linux nó macOS ar bith, le Python
  3.11 nó níos nuaí.
- Cábla sonraí USB idir an dá cheann.

Ní logálann na dochtearraí caighdeánacha athsheoltóra ón splancaire paicéid. Tóg na dochtearraí athsheoltóra tú féin ó
[fhoinse MeshCore](https://github.com/meshcore-dev/MeshCore), agus cuir an bhratach seo le tógáil do bhoird:

```text
-D MESH_PACKET_LOGGING=1
```

## Suiteáil {#install}

Plugáil an t-athsheoltóir isteach sa ríomhaire, agus ansin rith script suiteála meshcoretomqtt ar an ríomhaire sin:

```text
curl -fsSL https://raw.githubusercontent.com/Cisien/meshcoretomqtt/main/install.sh | sudo bash
```

Suiteálann an script an droichead mar sheirbhís a thosaíonn leis an ríomhaire, agus fiafraíonn sí díot cé na bróicéirí ar mian leat seoladh chucu. Níl an Analyzer ar an liosta sin: cuireann tú isteach é sa chomhad cumraíochta thíos. Tá do shocruithe féin i
`/etc/mctomqtt/config.d/99-user.toml`: ní fhorscríobhann nuashonrú an comhad sin riamh.

## Bróicéirí {#brokers}

Tá a bhloc `[[broker]]` féin ag gach bróicéir, mar sin is féidir le hathsheoltóir amháin trácht a sheoladh chuig roinnt bróicéirí ag an am céanna. Úsáideann do bhróicéir féin ainm úsáideora agus pasfhocal, nó ní úsáideann sé logáil isteach ar chor ar bith
(`method = "none"`).
Úsáideann an MeshCore Analyzer comhartha (token) ina ionad sin, agus síníonn eochair d'athsheoltóra é:

- seoladh `mqtt.meshcore-analyzer.eu`, port `443`, thar websocket slán;
- is é an seoladh céanna lucht féachana (audience) an chomhartha.

## Do chomhad cumraíochta {#config}

Cuir é seo in ionad an ábhair atá i `/etc/mctomqtt/config.d/99-user.toml`. Líon isteach cód an aerfoirt is gaire do d'athsheoltóir (`AMS`, mar shampla) agus an port USB a bhfuil d'athsheoltóir ceangailte leis. Ansin cuir do bhróicéir féin leis. Fág amach bloc nach bhfuil uait.

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

Atosaigh an tseirbhís tar éis athrú a dhéanamh (`sudo systemctl restart mctomqtt` ar Linux). Ansin feicfidh tú d'athsheoltóir ar an Analyzer mar bhreathnóir, nód a uaslódálann a gcloiseann sé, faoi ainm d'athsheoltóra féin. Tá gach socrú eile sa
[README meshcoretomqtt](https://github.com/Cisien/meshcoretomqtt).
