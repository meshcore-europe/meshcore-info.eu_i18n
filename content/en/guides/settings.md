---
title: "Recommended settings"
layout: settings
lead: "The radio preset your area uses, and the settings your neighbours changed. Pick your country, set the preset and copy the commands."
description: "The MeshCore radio preset per area in Europe, and the repeater and companion settings local groups changed from the defaults, with the commands."
---

Each area below uses its own radio preset, or changes a few of MeshCore's
defaults. Everything not listed stays at the default, so you only change what
your area changed. A repeater passes messages on for everyone; a companion is
the node you message from, paired with your phone or laptop over Bluetooth or
USB, or with its own screen.

The [repeater guide](/repeater-guide/#config) shows how to reach your
repeater's command line, and the [serial console](/firmware/console/) on this
site is where you type commands yourself. Under each area you can also send its
settings over USB. It also lists the [legal limits](/repeater-guide/#legal)
on 868 MHz.

## Keep traffic down {#traffic}

These settings hold for every area. Each repeater passes on every flood
message it hears. One message from you costs one transmission, plus one for
each repeater that hears it. Under the 10% duty cycle a repeater can send
about 680 packets an hour, and everyone around it shares that number. A
message that travels further than it needs to uses some of it up.

**Send to the smallest region that reaches the people you write to.**
Regions nest: a country, a province, a local group, each with its own code,
such as `nl`, `nl-ov` and `nl-ov-zwo`. A message for `nl-ov-zwo` stays with
the repeaters in that group. A repeater only passes on the regions it holds
itself: holding `nl` does not make it pass on `nl-ov`. Put each repeater in
every region it serves, and only those; your [local group](/community/) knows
which ones those are.

**Limit what your repeater passes on.** Two settings keep traffic that has
no need to travel far close to home:

```text
set flood.max.advert 3
set flood.max.unscoped 1
```

- `flood.max.advert 3`: adverts, which announce a node to the mesh, travel
  at most 3 hops.
- `flood.max.unscoped 1`: a message without a region passes through one
  repeater at most.
