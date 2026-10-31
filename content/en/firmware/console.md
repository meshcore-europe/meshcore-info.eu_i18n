---
title: "Serial console"
layout: console
lead: "Type commands to your repeater from your browser, over USB."
description: "Configure a MeshCore repeater, room server or sensor over USB from Chrome, Edge or Opera, with a serial console in the browser and nothing to install."
---

A repeater (it passes messages on), a room server (it stores posts for a
group) or a sensor (it reports readings) has no app, so you set it up by typing
commands over USB. Plug your node into your computer, open this page in
Chrome, Edge or Opera on a computer, and pick your node's port. The console
first sends `get role` and `ver`, so it knows what your node is. Both only
read. Then it shows what your node says; type a command such as `get name` and
press Enter. While you type, it suggests the commands your node understands,
and Tab fills in the first one.

A companion, the node you message from, talks to the app over USB instead. Its command line is in the
MeshCore app, version 1.50 or later.
