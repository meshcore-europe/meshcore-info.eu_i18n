---
title: MQTT på din observer
lead: Lad din repeater rapportere, hvad den hører, til MeshCore Analyzer over Wi-Fi. Den sender beskeder videre som før.
description: Gør en ESP32-repeater til en MeshCore-observer med DMC observer-firmwaren. Flash den, sæt Wi-Fi og din lufthavnskode, vælg brokerne og tjek, at den rapporterer til MeshCore Analyzer.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '7b9a9320'
  seeded: '2026-10-26'
  fields: {title: '62626d0f', lead: 'fe9653d4', description: '739edb74'}
  sections: ['962bdbc4', '0ccd4a85', 'fc57f65c', 'ef841ae5', '77d109c5', 'b3e4f8d2', '602a1021']
---

En observer er en node, der også rapporterer, hvad den hører, over MQTT via
Wi-Fi. Hver observer viser lidt mere af meshet på
[MeshCore Analyzer](https://meshcore-analyzer.eu/) og på
[dækningskortene](/map/). Denne guide gør en repeater (en node, der sender
beskeder videre) til en observer. Den bliver ved med at repeate, og rapporten
går kun én vej: intet kommer tilbage på meshet.

{{< callout type="warning" >}}
Denne guide gælder **DMC observer-firmwaren**, observer-udgaven af
[Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore), baseret på
MeshCore 1.18.0. Standard-MeshCore har ingen MQTT. Hver kommando herunder er
læst i firmwarens kildekode ved build `32dd8ad` fra 19. oktober 2026.
{{< /callout >}}

## Det skal du bruge {#need}

- Et ESP32-board med Wi-Fi, for eksempel et Heltec V3 eller V4, et LilyGo T3S3
  eller et Xiao S3. [Udgivelsen](https://github.com/Dutch-MeshCore/MeshCore/releases/tag/observer-mqtt-dev)
  nævner alle boards. nRF52-boards som RAK4631 har ingen Wi-Fi.
- Et 2.4 GHz Wi-Fi-netværk der, hvor boardet står.
- Et USB-datakabel og Chrome, Edge eller Opera på din computer.
- Lufthavnskoden nærmest din node, 3 bogstaver som `AMS` eller `BRU`. Den
  fortæller brokerne (serverne, der modtager dine rapporter), hvilket område
  din observer står i.

Ingen Wi-Fi der, hvor din repeater står, men en computer ved siden af?
[Byg en bridge-konfiguration](/guides/mctomqtt/) i stedet.

## Flash firmwaren {#flash}

[Flasheren](/firmware/flasher/) her på sitet har kun standard-MeshCore.
Observer-firmwaren får du fra flasheren i
[DutchMeshCore Toolbox](https://toolbox.dutchmeshcore.nl/):

1. Vælg dit board og derefter **DutchMeshCore MQTT** (Repeater + Observer + MQTT).
2. Vælg **Full flash** første gang: den erstatter alt på boardet, også
   partitionstabellen. App-opdateringen bevarer det, der ligger der, og er til
   senere opdateringer.
3. Sæt din repeater op som sædvanligt: navn, radio-preset og admin-adgangskode,
   som i [repeater-guiden](/repeater-guide/#config).

Denne firmware er **dev**-udgaven og opdaterer sig selv fra dev-kanalen, når du
skriver `ota update`. Den stabile kanal har stadig 1.17.1, så bliv på dev i
denne guide.

## Indstillinger {#settings}

Åbn [seriel-konsollen](/firmware/console/) her på sitet og tilslut dit board.
Udfyld dit eget Wi-Fi-netværk, adgangskode og lufthavnskode, og indsæt så
disse linjer én ad gangen:

```text
set wifi.ssid MyNetwork
set wifi.pwd MyPassword
set mqtt.iata AMS
reboot
```

Efter genstarten går boardet på dit Wi-Fi og stiller sit ur efter internettet.
Brokerne skal bruge det ur til at tjekke, hvem din observer er. Uden en
lufthavnskode bliver intet rapporteret.

Vil du hellere klikke end skrive? `start webconfig` åbner en indstillingsside
på boardet, på den adresse konsollen viser. Log ind med din admin-adgangskode.

## Broker-pladser {#brokers}

En plads rummer én broker. Firmwaren starter med disse pladser udfyldt:

| Plads | Broker | Drives af |
| --- | --- | --- |
| 1 | `dutchmeshcore-1` | Dutch-MeshCore |
| 2 | `dutchmeshcore-2` | Dutch-MeshCore |
| 3 | `meshcore-analyzer-eu` | MeshCore Analyzer |

Et board uden ekstra hukommelse (PSRAM), som Heltec V3, har 3 pladser. Det
forbinder til 2 af dem ad gangen, så Analyzer på plads 3 forbinder aldrig.
Flyt den til plads 1:

```text
set mqtt3.preset none
set mqtt1.preset meshcore-analyzer-eu
```

Et board med PSRAM, som Heltec V4, har 6 pladser og forbinder til 5 ad
gangen. Det kræver ingen ændring.

Din node logger ind hos hver broker med sin egen nøgle, så du behøver ingen
konto. `get mqtt.presets` viser de andre community-brokere, firmwaren kender.

### Din egen broker {#own}

Sæt din egen broker på en ledig plads. Udfyld dens adresse, port, brugernavn
og adgangskode. På et board med PSRAM er plads 4 ledig:

```text
set mqtt4.preset custom
set mqtt4.server mqtt.example.org
set mqtt4.port 1883
set mqtt4.username my_username
set mqtt4.password my_password
```

På et board uden PSRAM bruger du plads 2 i stedet: erstat `mqtt4` med `mqtt2`.
Din broker overtager så pladsen fra `dutchmeshcore-2`.

Port `8883` forbinder krypteret (TLS), port `443` krypteret over en
webforbindelse (websocket), og enhver anden port ukrypteret. Du kan også
angive den fulde adresse, som `wss://mqtt.example.org:9002/mqtt`; så gælder
portreglen ikke.

## Tjek at det virker {#check}

Skriv `get mqtt.status`. Hver plads viser sin tilstand:

```text
> msgs: on, 1: meshcore-analyzer-eu (ok), 2: dutchmeshcore-2 (ok), q:0
```

- `ok`: forbundet.
- `wait`: pladsen mangler en indstilling, for eksempel lufthavnskoden.
- `disc`: ikke forbundet endnu. Tjek dit Wi-Fi med `get wifi.status`.
- `fail`: pladsen fejlede 7 gange i træk, over cirka 20 minutter, og prøver
  nu én gang hvert 30. minut. Tjek brokerens adresse og login.
- `inactive`: boardet har ikke plads til denne plads. Se
  [Broker-pladser](#brokers).

Kig derefter efter din repeaters navn på
[observer-siden i Analyzer](https://meshcore-analyzer.eu/#observers).
Den dukker op inden for 5 minutter, med det, den har hørt.
