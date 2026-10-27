---
title: "Build a bridge config"
lead: "Send what your repeater hears to any MQTT broker: your own, or the Analyzer. A computer next to the repeater does the sending."
description: "Run meshcoretomqtt on a Raspberry Pi or another computer to send what a MeshCore repeater hears over USB to your own MQTT broker, the MeshCore Analyzer, or both."
---

A repeater is a node that passes messages on. You want its traffic on an MQTT
broker: your own for a dashboard or a database, or the
[MeshCore Analyzer](https://meshcore-analyzer.eu/)'s. Or your repeater has no
Wi-Fi of its own, but a Raspberry Pi or a server stands next to it.
[meshcoretomqtt](https://github.com/Cisien/meshcoretomqtt), a community tool,
is the bridge: it sends the traffic from that computer. Your repeater keeps
repeating, because the bridge only reads what it logs over USB.

## What you need {#need}

- A repeater built with packet logging (below).
- A Raspberry Pi Zero, 2, 3 or 4, or any Linux or macOS computer, with Python
  3.11 or newer.
- A USB data cable between the two.

The standard repeater firmware from the flasher does not log packets. Build
the repeater firmware yourself from the
[MeshCore source](https://github.com/meshcore-dev/MeshCore) with this flag
added to your board's build:

```text
-D MESH_PACKET_LOGGING=1
```

## Install {#install}

Plug the repeater into the computer, then run the install script of
meshcoretomqtt on that computer:

```text
curl -fsSL https://raw.githubusercontent.com/Cisien/meshcoretomqtt/main/install.sh | sudo bash
```

It installs the bridge as a service that starts with the computer, and asks
which brokers to send to. The Analyzer is not in that list; you add it in the
config file below. Your own settings live in
`/etc/mctomqtt/config.d/99-user.toml`; an update never overwrites that file.

## Brokers {#brokers}

Each broker gets its own `[[broker]]` block, so one repeater can feed several
at the same time. Your own broker takes a username and a password, or no login at all
(`method = "none"`).
The MeshCore Analyzer takes a token instead, which your repeater's key signs:

- address `mqtt.meshcore-analyzer.eu`, port `443`, over a secure websocket;
- the token's audience is the same address.

## Your config file {#config}

Replace the contents of `/etc/mctomqtt/config.d/99-user.toml` with this. Fill
in the airport code nearest to your repeater (`AMS`, for example) and the USB
port your repeater is on. Then add your own broker. Leave out a block you do
not need.

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

Restart the service after a change (`sudo systemctl restart mctomqtt` on
Linux). Your repeater then shows up on the Analyzer as an observer, a node that
uploads what it hears, under your repeater's own name. The
[meshcoretomqtt README](https://github.com/Cisien/meshcoretomqtt) has every
other setting.
