---
title: MQTT al teu observador
lead: Fes que el teu repetidor informi per Wi-Fi al MeshCore Analyzer del que sent. Continuarà retransmetent missatges com fins ara.
description: Converteix un repetidor ESP32 en un observador de MeshCore amb el firmware d'observador DMC. Instal·la'l, configura la Wi-Fi i el codi d'aeroport, tria els brokers i comprova que informa al MeshCore Analyzer.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '7b9a9320'
  seeded: '2026-11-02'
  fields: {title: '62626d0f', lead: 'fe9653d4', description: '739edb74'}
  sections: ['962bdbc4', '0ccd4a85', 'fc57f65c', 'ef841ae5', '77d109c5', 'b3e4f8d2', '602a1021']
  blocks: ['75461763', '0e0db0ff', '231a92ad', '49ad02ce', '19b33688', '01e79e69', '6f184c96', '75da543a', '966b1e87', '11f22f4c', '5f85ac9b', 'f74cb809', '1a70c3f5', '9cadc611', '5261e7e9', 'c998ea2d', '393339d9', '803a2dc4', 'cedf8d28', '7c222cec', '6bc50a6a', '59f2a96c', 'a8bd6037', '0d3b84ff', 'e43d5a74', '3bd6439c', '2ddd9432', 'd9df877b', '3283886d', 'f6131e02', '99dc83fb']
---

Un observador és un node que, a més, informa per MQTT, a través de la Wi-Fi, del que sent. Cada observador mostra una mica més de la xarxa mesh al [MeshCore Analyzer](https://meshcore-analyzer.eu/) i als [mapes de cobertura](/map/). Amb aquesta guia convertiràs un repetidor (un node que retransmet missatges) en un observador. El node continua repetint, i els informes van en un sol sentit: res no torna a la xarxa mesh.

{{< callout type="warning" >}}
Aquesta guia és per al **firmware d'observador DMC**, la versió per a observadors de [Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore), basada en MeshCore 1.18.0. El MeshCore estàndard no té MQTT. Totes les ordres d'aquesta guia surten del codi font del firmware, a la compilació `32dd8ad` del 19 d'octubre de 2026.
{{< /callout >}}

## Què necessites {#need}

- Una placa ESP32 amb Wi-Fi, com ara una Heltec V3 o V4, una LilyGo T3S3 o una Xiao S3. A la [versió publicada](https://github.com/Dutch-MeshCore/MeshCore/releases/tag/observer-mqtt-dev) hi trobaràs totes les plaques. Les plaques nRF52, com la RAK4631, no tenen Wi-Fi.
- Una xarxa Wi-Fi de 2.4 GHz al lloc on tens la placa.
- Un cable USB de dades i Chrome, Edge o Opera a l'ordinador.
- El codi de l'aeroport més proper al teu node, de 3 lletres, com ara `AMS` o `BRU`. Amb aquest codi, els brokers (els servidors que reben els teus informes) saben en quina zona és el teu observador.

No tens Wi-Fi on és el repetidor, però sí un ordinador al costat? [Crea una configuració de pont](/guides/mctomqtt/) en lloc d'això.

## Instal·la el firmware {#flash}

El [flasher](/firmware/flasher/) d'aquest lloc només porta el MeshCore estàndard. El firmware d'observador l'has d'instal·lar amb el flasher de la [DutchMeshCore Toolbox](https://toolbox.dutchmeshcore.nl/):

1. Tria la teva placa i després **DutchMeshCore MQTT** (Repeater + Observer + MQTT).
2. La primera vegada, tria **Full flash**: substitueix tot el que hi ha a la placa, inclosa la taula de particions. L'actualització de l'aplicació conserva el que hi ha i serveix per a les actualitzacions posteriors.
3. Configura el repetidor com sempre: nom, preajust de ràdio i contrasenya d'administrador, tal com explica la [guia del repetidor](/repeater-guide/#config).

Aquest firmware és la versió **dev** i s'actualitza des del canal dev quan escrius `ota update`. El canal estable encara porta la 1.17.1, així que queda't al canal dev per seguir aquesta guia.

## Configuració {#settings}

Obre la [consola sèrie](/firmware/console/) d'aquest lloc i connecta-hi la placa. Posa la teva xarxa Wi-Fi, la contrasenya i el codi d'aeroport, i després enganxa aquestes línies d'una en una:

```text
set wifi.ssid MyNetwork
set wifi.pwd MyPassword
set mqtt.iata AMS
reboot
```

Després de reiniciar-se, la placa es connecta a la teva Wi-Fi i posa el rellotge en hora des d'internet. Els brokers necessiten aquest rellotge per comprovar qui és el teu observador. Sense codi d'aeroport, la placa no envia cap informe.

Prefereixes clicar abans que escriure? Amb `start webconfig` obres una pàgina de configuració a la placa, a l'adreça que mostra la consola. Entra-hi amb la contrasenya d'administrador.

## Ranures de broker {#brokers}

Cada ranura conté un broker. El firmware arrenca amb aquestes ranures ja plenes:

| Ranura | Broker | Gestionat per |
| --- | --- | --- |
| 1 | `dutchmeshcore-1` | Dutch-MeshCore |
| 2 | `dutchmeshcore-2` | Dutch-MeshCore |
| 3 | `meshcore-analyzer-eu` | MeshCore Analyzer |

Una placa sense memòria addicional (PSRAM), com la Heltec V3, té 3 ranures. Es connecta a 2 alhora, de manera que l'Analyzer de la ranura 3 no es connecta mai. Mou-lo a la ranura 1:

```text
set mqtt3.preset none
set mqtt1.preset meshcore-analyzer-eu
```

Una placa amb PSRAM, com la Heltec V4, té 6 ranures i es connecta a 5 alhora. No cal que hi canviïs res.

El teu node entra a cada broker amb la seva pròpia clau, així que no necessites cap compte. Amb `get mqtt.presets` veuràs la llista dels altres brokers de la comunitat que coneix el firmware.

### El teu propi broker {#own}

Posa el teu propi broker en una ranura lliure. Indica'n l'adreça, el port, el nom d'usuari i la contrasenya. En una placa amb PSRAM, la ranura 4 és lliure:

```text
set mqtt4.preset custom
set mqtt4.server mqtt.example.org
set mqtt4.port 1883
set mqtt4.username my_username
set mqtt4.password my_password
```

En una placa sense PSRAM, fes servir la ranura 2: substitueix `mqtt4` per `mqtt2`. Aleshores el teu broker ocupa el lloc de `dutchmeshcore-2`.

El port `8883` connecta amb xifratge (TLS), el port `443` connecta amb xifratge sobre una connexió web (websocket) i qualsevol altre port connecta sense xifratge. També pots indicar l'adreça completa, com ara `wss://mqtt.example.org:9002/mqtt`; en aquest cas, la regla dels ports no s'aplica.

## Comprova que funciona {#check}

Escriu `get mqtt.status`. Veuràs l'estat de cada ranura:

```text
> msgs: on, 1: meshcore-analyzer-eu (ok), 2: dutchmeshcore-2 (ok), q:0
```

- `ok`: connectada.
- `wait`: a la ranura li falta un paràmetre, com ara el codi d'aeroport.
- `disc`: encara no està connectada. Comprova la Wi-Fi amb `get wifi.status`.
- `fail`: la ranura ha fallat 7 vegades seguides, durant uns 20 minuts, i ara ho prova una vegada cada 30 minuts. Comprova l'adreça i les dades d'accés del broker.
- `inactive`: la placa no té lloc per a aquesta ranura. Consulta [Ranures de broker](#brokers).

Després busca el nom del teu repetidor a la [pàgina d'observadors de l'Analyzer](https://meshcore-analyzer.eu/#observers). Hi apareixerà en un màxim de 5 minuts, amb el que ha sentit.
