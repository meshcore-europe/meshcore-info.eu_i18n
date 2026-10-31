---
title: MQTT på din observer
lead: Lad din repeater sende det, den hører, til MeshCore Analyzer over Wi-Fi. Den videresender stadig beskeder som før.
description: Gør en ESP32-repeater til en MeshCore-observer med DMC observer-firmwaren. Flash den, indstil Wi-Fi og din lufthavnskode, vælg brokerne og tjek, at den rapporterer til MeshCore Analyzer.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '7b9a9320'
  seeded: '2026-10-31'
  fields: {title: '62626d0f', lead: 'fe9653d4', description: '739edb74'}
  sections: ['962bdbc4', '0ccd4a85', 'fc57f65c', 'ef841ae5', '77d109c5', 'b3e4f8d2', '602a1021']
  blocks: ['75461763', '0e0db0ff', '231a92ad', '49ad02ce', '19b33688', '01e79e69', '6f184c96', '75da543a', '966b1e87', '11f22f4c', '5f85ac9b', 'f74cb809', '1a70c3f5', '9cadc611', '5261e7e9', 'c998ea2d', '393339d9', '803a2dc4', 'cedf8d28', '7c222cec', '6bc50a6a', '59f2a96c', 'a8bd6037', '0d3b84ff', 'e43d5a74', '3bd6439c', '2ddd9432', 'd9df877b', '3283886d', 'f6131e02', '99dc83fb']
---

En observer er en node, der også rapporterer det, den hører, over MQTT via
Wi-Fi. Hver observer viser lidt mere af meshet på
[MeshCore Analyzer](https://meshcore-analyzer.eu/) og på
[dækningskortene](/map/). Med denne guide gør du en repeater (en node, der
videresender beskeder) til en observer. Den bliver ved med at videresende.
Rapporterne går kun én vej: intet kommer tilbage på meshet.

{{< callout type="warning" >}}
Denne guide gælder **DMC observer-firmwaren**. Det er observer-udgaven af
[Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore), baseret på
MeshCore 1.18.0. Standard-MeshCore har ikke MQTT. Alle kommandoer nedenfor er
hentet fra firmwarens kildekode ved build `32dd8ad` af 19. oktober 2026.
{{< /callout >}}

## Det skal du bruge {#need}

- Et ESP32-board med Wi-Fi, for eksempel en Heltec V3 eller V4, en LilyGo T3S3
  eller en Xiao S3. [Udgivelsen](https://github.com/Dutch-MeshCore/MeshCore/releases/tag/observer-mqtt-dev)
  viser alle boards. nRF52-boards som RAK4631 har ikke Wi-Fi.
- Et 2.4 GHz Wi-Fi-netværk der, hvor boardet står.
- Et USB-datakabel og Chrome, Edge eller Opera på din computer.
- Lufthavnskoden nærmest din node, 3 bogstaver som `AMS` eller `BRU`.
  Den fortæller brokerne (serverne, der modtager dine rapporter), hvilket
  område din observer er i.

Ingen Wi-Fi der, hvor din repeater står, men en computer ved siden af?
[Byg i stedet en bridge-konfiguration](/guides/mctomqtt/).

## Flash firmwaren {#flash}

[Flasheren](/firmware/flasher/) på dette site har kun standard-MeshCore.
Observer-firmwaren henter du med flasheren i
[DutchMeshCore Toolbox](https://toolbox.dutchmeshcore.nl/):

1. Vælg dit board og derefter **DutchMeshCore MQTT** (Repeater + Observer + MQTT).
2. Vælg **Full flash** første gang: den erstatter alt på boardet, også
   partitionstabellen. App-opdateringen beholder det, der ligger der, og er
   til senere opdateringer.
3. Sæt din repeater op som normalt: navn, radio-preset og admin-adgangskode,
   som i [repeater-guiden](/repeater-guide/#config).

Denne firmware er **dev**-udgaven. Den opdaterer sig selv fra dev-kanalen,
når du skriver `ota update`. Den stabile kanal har stadig 1.17.1, så bliv på
dev til denne guide.

## Indstillinger {#settings}

Åbn [seriel-konsollen](/firmware/console/) på dette site, og forbind dit
board. Udfyld dit eget Wi-Fi-netværk, din adgangskode og din lufthavnskode.
Indsæt derefter linjerne én ad gangen:

```text
set wifi.ssid MyNetwork
set wifi.pwd MyPassword
set mqtt.iata AMS
reboot
```

Efter genstarten går boardet på dit Wi-Fi og stiller sit ur efter internettet.
Brokerne bruger uret til at tjekke, hvem din observer er. Uden en lufthavnskode
bliver intet rapporteret.

Vil du hellere klikke end skrive? `start webconfig` åbner en side med
indstillinger på boardet, på den adresse, konsollen viser. Log ind med din
admin-adgangskode.

## Broker-pladser {#brokers}

En plads rummer én broker. Fra start er disse pladser udfyldt i firmwaren:

| Plads | Broker | Drives af |
| --- | --- | --- |
| 1 | `dutchmeshcore-1` | Dutch-MeshCore |
| 2 | `dutchmeshcore-2` | Dutch-MeshCore |
| 3 | `meshcore-analyzer-eu` | MeshCore Analyzer |

Et board uden ekstra hukommelse (PSRAM), fx Heltec V3, har 3 pladser. Det
forbinder til 2 af dem ad gangen, så Analyzer på plads 3 forbinder aldrig.
Flyt den til plads 1:

```text
set mqtt3.preset none
set mqtt1.preset meshcore-analyzer-eu
```

Et board med PSRAM, fx Heltec V4, har 6 pladser og forbinder til 5 ad gangen.
Her skal du ikke ændre noget.

Din node logger ind på hver broker med sin egen nøgle, så du behøver ingen
konto. `get mqtt.presets` viser de andre fællesskabsbrokere, firmwaren kender.

### Din egen broker {#own}

Sæt din egen broker på en ledig plads. Udfyld adresse, port, brugernavn og
adgangskode. På et board med PSRAM er plads 4 ledig:

```text
set mqtt4.preset custom
set mqtt4.server mqtt.example.org
set mqtt4.port 1883
set mqtt4.username my_username
set mqtt4.password my_password
```

På et board uden PSRAM bruger du plads 2 i stedet: skift `mqtt4` ud med `mqtt2`.
Din broker tager så pladsen fra `dutchmeshcore-2`.

Port `8883` forbinder krypteret (TLS), port `443` krypteret over en
webforbindelse (websocket), og alle andre porte ukrypteret. Du kan også angive
den fulde adresse, fx `wss://mqtt.example.org:9002/mqtt`. Så gælder
portreglen ikke.

## Tjek, at det virker {#check}

Skriv `get mqtt.status`. Hver plads viser sin status:

```text
> msgs: on, 1: meshcore-analyzer-eu (ok), 2: dutchmeshcore-2 (ok), q:0
```

- `ok`: forbundet.
- `wait`: pladsen mangler en indstilling, fx lufthavnskoden.
- `disc`: ikke forbundet endnu. Tjek dit Wi-Fi med `get wifi.status`.
- `fail`: pladsen fejlede 7 gange i træk, over cirka 20 minutter, og prøver nu
  én gang hvert 30. minut. Tjek brokerens adresse og login.
- `inactive`: boardet har ikke plads til denne plads. Se
  [Broker-pladser](#brokers).

Kig derefter efter din repeaters navn på
[Analyzers observer-side](https://meshcore-analyzer.eu/#observers).
Den dukker op inden for 5 minutter med det, den har hørt.
