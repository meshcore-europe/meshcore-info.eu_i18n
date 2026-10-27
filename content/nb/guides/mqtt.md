---
title: MQTT på observeren din
lead: La repeateren din rapportere det den hører til MeshCore Analyzer over Wi-Fi. Den sender meldinger videre som før.
description: Gjør en ESP32-repeater om til en MeshCore-observer med DMC-observer-firmwaren. Flash den, sett opp Wi-Fi og flyplasskoden din, velg brokere og sjekk at den rapporterer til MeshCore Analyzer.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '7b9a9320'
  seeded: '2026-10-26'
  fields: {title: '62626d0f', lead: 'fe9653d4', description: '739edb74'}
  sections: ['962bdbc4', '0ccd4a85', 'fc57f65c', 'ef841ae5', '77d109c5', 'b3e4f8d2', '602a1021']
---

En observer er en node som også rapporterer det den hører over MQTT, via
Wi-Fi. Hver observer viser litt mer av meshen på
[MeshCore Analyzer](https://meshcore-analyzer.eu/) og på
[dekningskartene](/map/). Denne veiledningen gjør en repeater (en node som
sender meldinger videre) om til en observer. Den fortsetter å repetere, og
rapporten går bare én vei: ingenting kommer tilbake inn i meshen.

{{< callout type="warning" >}}
Denne veiledningen gjelder **DMC-observer-firmwaren**, observer-varianten av
[Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore), basert på
MeshCore 1.18.0. Standard MeshCore har ikke MQTT. Alle kommandoene nedenfor er
hentet fra firmware-kildekoden i bygg `32dd8ad` fra 19. oktober 2026.
{{< /callout >}}

## Det du trenger {#need}

- Et ESP32-kort med Wi-Fi, som en Heltec V3 eller V4, en LilyGo T3S3 eller en
  Xiao S3. [Utgivelsen](https://github.com/Dutch-MeshCore/MeshCore/releases/tag/observer-mqtt-dev)
  lister opp alle kortene. nRF52-kort som RAK4631 har ikke Wi-Fi.
- Et 2.4 GHz Wi-Fi-nett der kortet står.
- En USB-datakabel, og Chrome, Edge eller Opera på datamaskinen din.
- Flyplasskoden nærmest noden din, 3 bokstaver som `AMS` eller `BRU`.
  Den forteller brokerne (serverne som mottar rapportene dine) hvilket område
  observeren din står i.

Ingen Wi-Fi der repeateren din står, men en datamaskin ved siden av?
[Sett opp en bridge-konfigurasjon](/guides/mctomqtt/) i stedet.

## Flash firmwaren {#flash}

[Flasheren](/firmware/flasher/) på dette nettstedet har bare standard MeshCore.
Observer-firmwaren får du fra flasheren i
[DutchMeshCore Toolbox](https://toolbox.dutchmeshcore.nl/):

1. Velg kortet ditt, deretter **DutchMeshCore MQTT** (Repeater + Observer + MQTT).
2. Velg **Full flash** første gang: det erstatter alt på kortet, også
   partisjonstabellen. App-oppdateringen beholder det som ligger der og er
   ment for senere oppdateringer.
3. Sett opp repeateren som vanlig: navn, radioforvalg og admin-passord, slik
   det står i [repeater-veiledningen](/repeater-guide/#config).

Denne firmwaren er **dev**-bygget og oppdaterer seg selv fra dev-kanalen når
du skriver `ota update`. Den stabile kanalen ligger fortsatt på 1.17.1, så bli
på dev for denne veiledningen.

## Innstillinger {#settings}

Åpne [seriekonsollen](/firmware/console/) på dette nettstedet og koble til
kortet ditt. Fyll inn ditt eget Wi-Fi-nett, passord og flyplasskode, og lim
inn disse linjene én om gangen:

```text
set wifi.ssid MyNetwork
set wifi.pwd MyPassword
set mqtt.iata AMS
reboot
```

Etter omstarten kobler kortet seg til Wi-Fi og stiller klokka fra internett.
Brokerne trenger den klokka for å sjekke hvem observeren din er. Uten
flyplasskode blir ingenting rapportert.

Vil du heller klikke enn å skrive? `start webconfig` åpner en innstillingsside
på kortet, på adressen konsollen viser. Logg inn med admin-passordet ditt.

## Broker-plasser {#brokers}

En plass holder én broker. Firmwaren starter med disse plassene fylt ut:

| Plass | Broker | Drives av |
| --- | --- | --- |
| 1 | `dutchmeshcore-1` | Dutch-MeshCore |
| 2 | `dutchmeshcore-2` | Dutch-MeshCore |
| 3 | `meshcore-analyzer-eu` | MeshCore Analyzer |

Et kort uten ekstra minne (PSRAM), som Heltec V3, har 3 plasser. Det kobler
til 2 av dem samtidig, så Analyzer på plass 3 kobler aldri til. Flytt den til
plass 1:

```text
set mqtt3.preset none
set mqtt1.preset meshcore-analyzer-eu
```

Et kort med PSRAM, som Heltec V4, har 6 plasser og kobler til 5 samtidig. Det
trenger ingen endring.

Noden din logger inn hos hver broker med sin egen nøkkel, så du trenger ingen
konto. `get mqtt.presets` lister opp de andre fellesskapsbrokerne firmwaren
kjenner til.

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

Port `8883` kobler til kryptert (TLS), port `443` kryptert over en
nettforbindelse (websocket), og alle andre porter ukryptert. Du kan også oppgi
hele adressen, som `wss://mqtt.example.org:9002/mqtt`; da gjelder ikke
portregelen.

## Sjekk at det virker {#check}

Skriv `get mqtt.status`. Hver plass viser tilstanden sin:

```text
> msgs: on, 1: meshcore-analyzer-eu (ok), 2: dutchmeshcore-2 (ok), q:0
```

- `ok`: tilkoblet.
- `wait`: plassen mangler en innstilling, for eksempel flyplasskoden.
- `disc`: ikke tilkoblet ennå. Sjekk Wi-Fi med `get wifi.status`.
- `fail`: plassen feilet 7 ganger på rad, over omtrent 20 minutter, og prøver
  nå én gang hvert 30. minutt. Sjekk adressen og innloggingen til brokeren.
- `inactive`: kortet har ikke plass til denne plassen. Se
  [Broker-plasser](#brokers).

Se deretter etter navnet på repeateren din på
[observer-siden i Analyzer](https://meshcore-analyzer.eu/#observers).
Den dukker opp innen 5 minutter, med det den har hørt.
