---
title: "MQTT on your observer"
lead: "Let your repeater report what it hears to the MeshCore Analyzer over Wi-Fi. It keeps passing messages on as before."
description: "Turn an ESP32 repeater into a MeshCore observer with the DMC observer firmware. Flash it, set Wi-Fi and your airport code, pick the brokers and check it reports to the MeshCore Analyzer."
---

An observer is a node that also reports what it hears over MQTT, through
Wi-Fi. Every observer shows a bit more of the mesh on the
[MeshCore Analyzer](https://meshcore-analyzer.eu/) and on the
[coverage maps](/map/). This guide turns a repeater (a node that passes
messages on) into one. It keeps repeating, and the report goes one way:
nothing comes back onto the mesh.

{{< callout type="warning" >}}
This guide is for the **DMC observer firmware**, the observer build of
[Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore), based on
MeshCore 1.18.0. Stock MeshCore has no MQTT. Every command below is read from
the firmware source at build `32dd8ad` of 19 October 2026.
{{< /callout >}}

## What you need {#need}

- An ESP32 board with Wi-Fi, such as a Heltec V3 or V4, a LilyGo T3S3 or a
  Xiao S3. The [release](https://github.com/Dutch-MeshCore/MeshCore/releases/tag/observer-mqtt-dev)
  lists every board. nRF52 boards such as the RAK4631 have no Wi-Fi.
- A 2.4 GHz Wi-Fi network where the board stands.
- A USB data cable, and Chrome, Edge or Opera on your computer.
- The airport code nearest to your node, 3 letters such as `AMS` or `BRU`.
  It tells the brokers (the servers that receive your reports) which area
  your observer is in.

No Wi-Fi where your repeater stands, but a computer next to it?
[Build a bridge config](/guides/mctomqtt/) instead.

## Flash the firmware {#flash}

The [flasher](/firmware/flasher/) on this site carries stock MeshCore only.
The observer firmware comes from the flasher in the
[DutchMeshCore Toolbox](https://toolbox.dutchmeshcore.nl/):

1. Pick your board, then **DutchMeshCore MQTT** (Repeater + Observer + MQTT).
2. Choose **Full flash** the first time: it replaces everything on the
   board, including the partition table. The app update keeps what is there
   and is for later updates.
3. Set your repeater up as usual: name, radio preset and admin password, as
   in the [repeater guide](/repeater-guide/#config).

This firmware is the **dev** build and updates itself from the dev channel
when you type `ota update`. The stable channel still carries 1.17.1, so stay
on dev for this guide.

## Settings {#settings}

Open the [serial console](/firmware/console/) on this site and connect your
board. Fill in your own Wi-Fi network, password and airport code, then paste
these lines one at a time:

```text
set wifi.ssid MyNetwork
set wifi.pwd MyPassword
set mqtt.iata AMS
reboot
```

After the reboot, the board joins your Wi-Fi and sets its clock from the
internet. The brokers need that clock to check who your observer is. Without
an airport code, nothing gets reported.

Rather click than type? `start webconfig` opens a settings page on the
board, at the address the console shows. Log in with your admin password.

## Broker slots {#brokers}

A slot holds one broker. The firmware starts with these slots filled in:

| Slot | Broker | Run by |
| --- | --- | --- |
| 1 | `dutchmeshcore-1` | Dutch-MeshCore |
| 2 | `dutchmeshcore-2` | Dutch-MeshCore |
| 3 | `meshcore-analyzer-eu` | MeshCore Analyzer |

A board without extra memory (PSRAM), such as the Heltec V3, has 3 slots. It
connects to 2 of them at once, so the Analyzer in slot 3 never connects.
Move it to slot 1:

```text
set mqtt3.preset none
set mqtt1.preset meshcore-analyzer-eu
```

A board with PSRAM, such as the Heltec V4, has 6 slots and connects to 5 at
once. It needs no change.

Your node logs in to each broker with its own key, so you need no account.
`get mqtt.presets` lists the other community brokers the firmware knows.

### Your own broker {#own}

Put your own broker in a free slot. Fill in its address, port, username and
password. On a board with PSRAM, slot 4 is free:

```text
set mqtt4.preset custom
set mqtt4.server mqtt.example.org
set mqtt4.port 1883
set mqtt4.username my_username
set mqtt4.password my_password
```

On a board without PSRAM, use slot 2 instead: replace `mqtt4` with `mqtt2`.
Your broker then takes the place of `dutchmeshcore-2`.

Port `8883` connects encrypted (TLS), port `443` encrypted over a web
connection (websocket), and any other port unencrypted. You can also give the
full address, such as `wss://mqtt.example.org:9002/mqtt`; then the port rule
does not apply.

## Check it works {#check}

Type `get mqtt.status`. Each slot shows its state:

```text
> msgs: on, 1: meshcore-analyzer-eu (ok), 2: dutchmeshcore-2 (ok), q:0
```

- `ok`: connected.
- `wait`: the slot misses a setting, such as the airport code.
- `disc`: not connected yet. Check your Wi-Fi with `get wifi.status`.
- `fail`: the slot failed 7 times in a row, over about 20 minutes, and now
  tries once every 30 minutes. Check the broker's address and login.
- `inactive`: the board has no room for this slot. See
  [Broker slots](#brokers).

Then look for your repeater's name on the
[observers page of the Analyzer](https://meshcore-analyzer.eu/#observers).
It shows up within 5 minutes, with what it heard.
