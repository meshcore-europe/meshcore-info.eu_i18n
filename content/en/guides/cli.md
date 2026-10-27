---
title: "CLI commands"
layout: cli
lead: "Every command of your repeater, room server, sensor or companion, grouped by what you want to do. Read what it does and the value it starts with, fill in your own and copy it."
description: "Every command of MeshCore firmware 1.18.0 for repeaters, room servers, sensors and companions, grouped by task: what it does, the value the firmware starts with, and which nodes have it."
---

These commands follow MeshCore firmware 1.18.0, read from the firmware
source. A command added in a recent version says which version it needs. A
repeater passes messages on, a room server stores posts for a group, a sensor
reports readings. Room servers, sensors and companions share many commands.
Each command says which nodes have it. "Which node?" shows only the commands
of yours.

On a repeater, room server or sensor, you type them over USB from your
computer, for example in the [serial console](/firmware/console/) on this site. The MeshCore app sends them over the mesh. The
[repeater guide](/repeater-guide/#config) shows both.

Since 1.18, a companion (the node you message from, paired with your phone or laptop, or
with its own screen) has a command line
too. Open Command Line in the settings of the MeshCore app, version 1.50 or
later. A contact with the Remote CLI permission can send your companion the
same commands over the mesh. That includes the WiFi and PIN commands.

The value a command starts with is the repeater's. A room server, sensor or
companion can start at another value. A command that only a companion has shows its own.
