---
title: "Get started"
lead: "From a new board to your first message on the mesh. You need a LoRa board, a computer with Chrome or Edge, and a phone or laptop for the app."
description: "Flash MeshCore from your browser, pair the app, pick the radio preset your area uses, send your first message and join your local channel."
eyebrow: "6 steps · MeshCore v1.18.0"
---

These steps follow MeshCore firmware v1.18.0 and the official tools of
October 2026. Menu names in the app can differ a little between versions.

## 1. Choose a device {#device}

Any board on the [devices page](/devices/) that lists companion works. For
your first node, pick a *companion*: the radio you message from. Pair it with
your phone or laptop over Bluetooth or USB, or pick one with its own screen
and keyboard that works on its own.

Get the 868 MHz version. The supplied antenna does the job; the
[antenna guide](/guides/antenna/) shows how to check one.

{{< callout type="warning" >}}
Attach the antenna before you switch the radio on. A LoRa radio that
transmits without an antenna can damage its own chip.
{{< /callout >}}

## 2. Flash the firmware {#flash}

1. Connect the device to your computer with a USB data cable.
2. Open the web flasher at [flasher.meshcore.io](https://flasher.meshcore.io)
   in Chrome or Edge. It uses Web Serial, which other browsers lack.
3. Pick your device, then the **Companion** firmware for **Bluetooth** (or
   USB, if you will only use it with a computer cable).
4. Flash. Some boards first go into update mode; the flasher tells you
   how.

Only use *erase* for a fresh start: erasing deletes the device's identity
and your contacts. For later updates, flash without erasing. To keep your
identity through an erase, export your companion's private key from the app
first and import it afterwards.

## 3. Install the app {#app}

The official MeshCore app is available for Android, iOS, Windows and macOS;
[meshcore.io](https://meshcore.io) links to every version. There is also a
web app at [app.meshcore.nz](https://app.meshcore.nz) that runs in Chrome or
Edge on a computer.

## 4. Pair your node {#pair}

Switch your node on, open the app and connect to it over Bluetooth. When
asked for a PIN:

- a node **with** a screen shows a PIN; type that one;
- a node **without** a screen uses `123456`.

If pairing fails, remove the device from your phone's Bluetooth settings and
try again. Then give your node a name. Others see this name, so do not use
your full name or address unless you want to.

## 5. Pick your area's radio preset {#preset}

Every radio in an area uses the same frequency and settings, or they cannot
hear each other. In the app's radio settings, pick the preset your area uses.
Outside the areas below, Europe uses **EU/UK (Narrow)**. The Netherlands,
Czechia, Hungary, Slovakia, Portugal and Switzerland use their own, and
Limburg in the Netherlands has a variant:

{{< presets >}}

Does your device not offer your area's preset? Enter the 4 values from the
table by hand in the app's radio settings: frequency, bandwidth, spreading
factor and coding rate. A node with other values does not hear the mesh.

Not sure? Your [local group](/community/) knows which preset your area uses.
The app downloads this list from the MeshCore project, so a new preset needs
no app update.

## 6. Say hello {#hello}

1. **Announce yourself.** Send an *advert* from the app. A "flood" advert
   travels through the repeaters (nodes that pass messages on), so everyone
   on the mesh can add you.
   Companions never announce themselves automatically.
2. **Find others.** People appear in your contacts once their adverts reach
   you. Repeaters send a flood advert every 47 hours by default, so your list
   can take 2 days to fill up.
3. **Send a message.** Open a contact and write. The first message floods
   the network; the receiver reports back the route it took, and later
   messages follow that route.
4. **Join channels.** The **Public** channel is already set up; anything you
   write there reaches everyone on the mesh. Add your region's *hashtag
   channel* (a name starting with `#`) by typing its name. Your
   [local group](/community/) will tell you which channels are active.

## When something does not work {#troubleshooting}

**The app does not find my device over Bluetooth.**
You probably flashed the USB companion. Flash again and choose the
Bluetooth version. On the Heltec V3, the small built-in Bluetooth antenna
has a short range; keep the phone close.

**Pairing keeps failing.**
Remove the device from your phone's Bluetooth settings, restart Bluetooth,
and pair again with the PIN on the screen or `123456`.

**Nobody appears in my contacts.**
Check that your preset matches your area. Send a flood advert. If there is no
repeater within reach, you will only hear radios close by; the
[map page](/map/) shows where repeaters are.

**A contact shows "last seen" days ago although they are active.**
One of the two nodes has the wrong time. A companion takes the time from
your phone; repeaters and room servers (nodes that store messages for a
group) need theirs set by their owner.

**A direct message never arrives.**
You both need the other as a contact. A node drops a message from someone
it does not know, without telling the sender. Send a flood advert and ask
the other person to send one too. Check in the app that it adds new
contacts automatically; it only adds nodes within its hop limit.

**Old contacts work, new ones never connect.**
A first message floods, and a repeater only passes it on when it holds the
message's region. Later messages follow a learned route, which no region
check stops. Ask your [local group](/community/) which regions the repeaters
around you hold, and check [the settings for your area](/guides/settings/#traffic).

**The app no longer connects to your companion.**
Some boards have a user button, such as some RAK boards and the Heltec T114.
Hold it in the first 8 seconds after the board starts. The companion opens
a rescue console over USB. In the console on
[flasher.meshcore.io](https://flasher.meshcore.io), `set pin <pin>` sets a
new Bluetooth PIN and `erase` wipes the device.

**The flasher cannot open the serial port on Linux.**
Your user needs access to the port, for example
`sudo setfacl -m u:$USER:rw /dev/ttyUSB0`, or membership of the `dialout`
group.

**Something else.** The
[MeshCore FAQ](https://github.com/meshcore-dev/MeshCore/blob/main/docs/faq.md)
covers many more problems.
