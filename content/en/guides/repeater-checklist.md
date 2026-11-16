---
title: "Repeater checklist"
lead: "Check your repeater before it goes up. Each line names what to check, the command that shows it and the guide that explains it."
description: "A checklist for a MeshCore repeater before it goes on a roof or mast: what to check over USB, how to mount it, and the test before you leave."
---

A repeater on a roof is hard to reach, so check it while it is still on your
desk. The [repeater guide](/repeater-guide/) explains every step. The values,
such as the preset and the hop limits, come from the
[settings of your area](/guides/settings/). Type the commands over USB, for
example in the [serial console](/firmware/console/). This list follows
MeshCore firmware v1.18.0.

## Before you start {#start}

- [ ] The [coverage maps](/map/) or your [local group](/community/) say the
      area needs a repeater. See [Do you need one?](/repeater-guide/#need)
- [ ] The owner of the site agreed, and you can reach the repeater for
      maintenance.
- [ ] Battery and panel are sized for the worst winter month. See
      [Power and solar sizing](/repeater-guide/#power).

## At your desk, over USB {#usb}

- [ ] The board runs the **Repeater** firmware: `ver` shows its version. See
      [Set it up](/repeater-guide/#config).
- [ ] On an nRF52 board, the reply to `get bootloader.ver` has `OTAFIX` in
      it. See [Update it over the air](/repeater-guide/#update).
- [ ] `get radio` shows the preset of your area.
- [ ] `get dutycycle` shows 10. See [Duty cycle](/repeater-guide/#duty-cycle).
- [ ] `get tx` plus your antenna gain stays within 500 mW e.r.p. See
      [Power: e.r.p. and your antenna](/repeater-guide/#erp).
- [ ] The admin password is no longer `password`.
- [ ] `get guest.password` shows a password.
- [ ] `get name` shows the name your local group uses for its repeaters.
- [ ] `get lat` and `get lon` show the position of the site.
- [ ] `get owner.info` shows how other operators reach you.
- [ ] `region` shows the regions of your area. `get flood.max.advert` and
      `get flood.max.unscoped` show its hop limits. See
      [Keep traffic down](/guides/settings/#traffic).
- [ ] You stored the private key from `get prv.key` somewhere safe.
- [ ] `clock` shows the time of this moment, in UTC.
- [ ] On solar, `powersaving` shows `on`.

## On the roof {#roof}

- [ ] The antenna is attached before the repeater gets power.
- [ ] The antenna stands upright on top of the mast, away from metal. See
      [Mounting](/guides/antenna/#mounting).
- [ ] Every outdoor connector is sealed, and the cable has a drip loop.
- [ ] The enclosure is closed, with a vent or drain hole. See
      [Hardware](/repeater-guide/#hardware).

## Before you leave {#leave}

- [ ] From a distance, your companion reaches the repeater in the app.
- [ ] You sent `advert`, so nodes across the mesh learn about the repeater.
- [ ] Your [local group](/community/) knows it is up.
