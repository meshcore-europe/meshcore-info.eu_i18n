---
title: MQTT på observeren din
lead: La repeateren din rapportere det den hører, til MeshCore Analyzer over Wi-Fi. Den videresender meldinger som før.
description: Gjør en ESP32-repeater om til en MeshCore-observer med DMC-observerfirmwaren. Flash den, sett opp Wi-Fi og flyplasskoden din, velg brokere og sjekk at den rapporterer til MeshCore Analyzer.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '7b9a9320'
  seeded: '2026-10-31'
  fields: {title: '62626d0f', lead: 'fe9653d4', description: '739edb74'}
  sections: ['962bdbc4', '0ccd4a85', 'fc57f65c', 'ef841ae5', '77d109c5', 'b3e4f8d2', '602a1021']
  blocks: ['75461763', '0e0db0ff', '231a92ad', '49ad02ce', '19b33688', '01e79e69', '6f184c96', '75da543a', '966b1e87', '11f22f4c', '5f85ac9b', 'f74cb809', '1a70c3f5', '9cadc611', '5261e7e9', 'c998ea2d', '393339d9', '803a2dc4', 'cedf8d28', '7c222cec', '6bc50a6a', '59f2a96c', 'a8bd6037', '0d3b84ff', 'e43d5a74', '3bd6439c', '2ddd9432', 'd9df877b', '3283886d', 'f6131e02', '99dc83fb']
---

En observer er en node som også rapporterer det den hører, over MQTT via
Wi-Fi. Hver observer viser litt mer av meshet på
[MeshCore Analyzer](https://meshcore-analyzer.eu/) og på
[dekningskartene](/map/). Med denne veiledningen gjør du en repeater (en node
som videresender meldinger) om til en observer. Den fortsetter å videresende,
og rapporten går bare én vei: ingenting kommer tilbake inn i meshet.

{{< callout type="warning" >}}
Denne veiledningen gjelder **DMC-observerfirmwaren**, observerversjonen av
[Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore), basert på
MeshCore 1.18.0. Vanlig MeshCore har ikke MQTT. Alle kommandoene nedenfor er
hentet fra kildekoden til firmwaren, bygg `32dd8ad` fra 19. oktober 2026.
{{< /callout >}}

## Dette trenger du {#need}

- Et ESP32-kort med Wi-Fi, for eksempel en Heltec V3 eller V4, en LilyGo T3S3
  eller en Xiao S3. I [releasen](https://github.com/Dutch-MeshCore/MeshCore/releases/tag/observer-mqtt-dev)
  finner du alle kortene. nRF52-kort som RAK4631 har ikke Wi-Fi.
- Et Wi-Fi-nett på 2.4 GHz der kortet står.
- En USB-kabel for data, og Chrome, Edge eller Opera på datamaskinen din.
- Flyplasskoden nærmest noden din, 3 bokstaver som `AMS` eller `BRU`.
  Med den vet brokerne (serverne som tar imot rapportene dine) hvilket område
  observeren din er i.

Har du ikke Wi-Fi der repeateren står, men en datamaskin ved siden av?
[Lag en bridge-konfigurasjon](/guides/mctomqtt/) i stedet.

## Flash firmwaren {#flash}

[Flasheren](/firmware/flasher/) på dette nettstedet har bare vanlig MeshCore.
Observerfirmwaren henter du fra flasheren i
[DutchMeshCore Toolbox](https://toolbox.dutchmeshcore.nl/):

1. Velg kortet ditt, og deretter **DutchMeshCore MQTT** (Repeater + Observer + MQTT).
2. Velg **Full flash** første gang: da erstattes alt på kortet, også
   partisjonstabellen. Appoppdateringen beholder det som ligger der, og er
   for senere oppdateringer.
3. Sett opp repeateren som vanlig: navn, radioforhåndsvalg og adminpassord,
   slik som i [repeaterveiledningen](/repeater-guide/#config).

Denne firmwaren er **dev**-bygget og oppdaterer seg selv fra dev-kanalen
når du skriver `ota update`. Den stabile kanalen har fortsatt 1.17.1, så hold
deg på dev for denne veiledningen.

## Innstillinger {#settings}

Åpne [seriekonsollen](/firmware/console/) på dette nettstedet og koble til
kortet ditt. Fyll inn ditt eget Wi-Fi-nett, passord og flyplasskode. Lim
deretter inn disse linjene én om gangen:

```text
set wifi.ssid MyNetwork
set wifi.pwd MyPassword
set mqtt.iata AMS
reboot
```

Etter omstarten kobler kortet seg til Wi-Fi-nettet ditt og stiller klokken
sin etter internett. Brokerne trenger den klokken for å bekrefte hvem
observeren din er. Uten flyplasskode blir ingenting rapportert.

Vil du heller klikke enn skrive? Med `start webconfig` åpner du en
innstillingsside på kortet, på adressen konsollen viser. Logg inn med
adminpassordet ditt.

## Broker-plasser {#brokers}

En plass rommer én broker. Firmwaren starter med disse plassene
ferdig utfylt:

| Plass | Broker | Drives av |
| --- | --- | --- |
| 1 | `dutchmeshcore-1` | Dutch-MeshCore |
| 2 | `dutchmeshcore-2` | Dutch-MeshCore |
| 3 | `meshcore-analyzer-eu` | MeshCore Analyzer |

Et kort uten ekstra minne (PSRAM), som Heltec V3, har 3 plasser. Det kobler
seg til 2 av dem samtidig, så Analyzer på plass 3 blir aldri koblet til.
Flytt den til plass 1:

```text
set mqtt3.preset none
set mqtt1.preset meshcore-analyzer-eu
```

Et kort med PSRAM, som Heltec V4, har 6 plasser og kobler seg til 5 samtidig.
Der trenger du ikke endre noe.

Noden din logger inn hos hver broker med sin egen nøkkel, så du trenger ingen
konto. Med `get mqtt.presets` ser du de andre fellesskapsbrokerne firmwaren
kjenner.

### Din egen broker {#own}

Legg din egen broker på en ledig plass. Fyll inn adresse, port, brukernavn og
passord. På et kort med PSRAM er plass 4 ledig:

```text
set mqtt4.preset custom
set mqtt4.server mqtt.example.org
set mqtt4.port 1883
set mqtt4.username my_username
set mqtt4.password my_password
```

På et kort uten PSRAM bruker du plass 2 i stedet: bytt ut `mqtt4` med `mqtt2`.
Brokeren din tar da plassen til `dutchmeshcore-2`.

Port `8883` gir kryptert tilkobling (TLS), port `443` kryptert tilkobling over
en webforbindelse (websocket), og alle andre porter ukryptert tilkobling. Du
kan også oppgi hele adressen, for eksempel `wss://mqtt.example.org:9002/mqtt`.
Da gjelder ikke portregelen.

## Sjekk at det virker {#check}

Skriv `get mqtt.status`. Du ser statusen for hver plass:

```text
> msgs: on, 1: meshcore-analyzer-eu (ok), 2: dutchmeshcore-2 (ok), q:0
```

- `ok`: tilkoblet.
- `wait`: plassen mangler en innstilling, for eksempel flyplasskoden.
- `disc`: ikke tilkoblet ennå. Sjekk Wi-Fi med `get wifi.status`.
- `fail`: plassen har feilet 7 ganger på rad, over omtrent 20 minutter, og
  prøver nå én gang hvert 30. minutt. Sjekk adressen og innloggingen til
  brokeren.
- `inactive`: kortet har ikke rom for denne plassen. Se
  [Broker-plasser](#brokers).

Se deretter etter navnet på repeateren din på
[observersiden i Analyzer](https://meshcore-analyzer.eu/#observers).
Den dukker opp innen 5 minutter, med det den har hørt.
