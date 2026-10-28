---
title: "Make the mesh resilient"
lead: "Is the mesh near you slow or full of junk? Find out what causes it, switch on the repeater setting that stops it, and tell your local group."
description: "Floods and spam on a MeshCore mesh: how to recognise each kind, which repeater setting helps, how to see a flood and how to find its source."
---

Do messages arrive late or not at all? Does Public fill with junk? That is
a flood: more traffic than the mesh can carry, sent by mistake or on
purpose. Find what you see in the tables below. Each row names the setting
that stops it. Switch that on at your repeater, the node that passes
messages on. Then tell your [local group](/community/), so the repeaters
around you do the same. Every repeater that drops a flood leaves airtime
for everyone else.

## Floods by mistake {#mistake}

A flood by mistake comes from a node whose owner does not know it causes
one. It stops once they do. An advert, in the tables below, is the hello a
node sends so others can find it.

The settings in the tables come from what the firmware does. Not every one
has stopped a flood on a real mesh yet.

{{< callout type="warning" >}}
Some settings on this page need the DMC firmware. Stock **MeshCore** 1.18.0
has regions, the hop limits `flood.max.*`, loop detection and the duty
cycle. The packet filter, the rules that let your repeater drop junk, comes
with the **DMC firmware** from
[Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore). So do
duty-cycle gating and the companion filter. This page follows the DMC
1.18.0 dev build `ecfb2d4` of 19 October 2026; the
[packet filter](/guides/filter/#firmware) page says where to get it.
{{< /callout >}}

| What you see | What it is | What helps |
| --- | --- | --- |
| Requests to repeaters from one node, day and night, and a mesh that stays slow for days | A home automation or a bot that asks repeaters for their status too often | `filter on`. The packet filter then passes 5 requests a minute. Tell the owner. |
| The same kind of message on a channel, every minute | A bot that posts too often | [Block the channel](/guides/filter/#channel) or [slow the sender down](/guides/filter/#sender). Tell the owner. |
| Unreadable messages on Public and other channels | A node with broken firmware or wrong radio settings | `filter malformed on` drops them on Public. Tell the owner. |
| One node's advert every few minutes | A node set to advert too often | `filter advert 24` passes each node's advert once a day. `set flood.max.advert 3` keeps adverts within 3 hops. |
| Messages from far away, with regions that do not belong here | A bridge that links meshes over the internet | `set flood.max.unscoped 1`, and put your repeater only in the [regions it serves](/guides/settings/#traffic). |
| The same message passes again and again, with your repeater's ID in its path more than once | A repeater that changes packets and passes them on, so they loop | Loop detection runs at `minimal` by default. `set loop.detect moderate` drops a loop sooner. |

## Floods on purpose {#purpose}

Some floods are spam: junk sent on purpose to clog the mesh. The sender
changes names, keys and paths, so no single rule stops the flood.

| What you see | What it is | What helps |
| --- | --- | --- |
| Many new nodes with random names, each with a new key | Fake adverts | `filter rate 04 5 60` passes 5 adverts a minute. `filter advert` does not help: every advert comes from a [new key](#forged). |
| Messages with unreadable text from made-up senders, often dated more than a year ago | Channel spam | `filter malformed on` drops them on Public. `filter age 60` drops the old-dated ones on Public and on [watched channels](/guides/filter/#settings). |
| Up to 200 direct messages a minute to nodes that do not exist, and no acknowledgements back | A flood of direct messages | `filter rate 02 5 60`. Your app does not show these messages; an observer does. |
| Bursts of requests from one node to dozens of others | Request spam | With `filter on`, the packet filter passes 5 requests a minute. |
| A message comes back 10 to 20 minutes later, with nearly the same path | Replay: a copy sent again | A repeater remembers the last 160 packets it saw, so on a busy mesh a later copy passes again. `filter age` drops a group message older than you allow. |
| Messages from Public sent again under a made-up sender, sometimes with an old date | Echo spam | `filter age 60`. `filter malformed on` also drops a date more than a week off. |
| A message every few seconds on several channels, each from a new name, asking ordinary questions | A bot wave | `filter rate 05 10 60`, and [block the channels](/guides/filter/#channel) your area does not use. Every name is new, so the [sender rules](#forged) miss it. |

## What has worked {#worked}

Local groups stopped floods with these steps:

1. **Tell the owner.** A flood by mistake stops once its owner knows. Send
   them a friendly message.
2. **Do not react on the mesh.** A reply shows a spammer that the spam works.
3. **Ask for observers.** An observer is a node that reports every packet
   it hears over MQTT. The more observers around you, the sooner you see
   where a flood comes in. Turn your own repeater into one with
   [MQTT on your observer](/guides/mqtt/).
4. **Find the source.** Observers place the sender in an area. The last
   kilometre takes people on foot with a radio. See
   [Find the source](#source).
5. **Get your local group moving.** One repeater with the right settings
   helps. All the repeaters in the area together stop a flood. Your
   [local group](/community/) gets every owner to switch the setting on.

## Made-up senders and paths {#forged}

A sender writes these parts of a packet, and nothing checks them:

- **The sender's name.** In a channel message, the name is part of the
  text. Anyone with the channel key can write any name.
- **The start of the path.** Each repeater adds its own ID to the end of
  the path. Nothing checks the IDs that were there before, so a sender can
  start the path with made-up ones. The end of the path is real.

{{< forged-path >}}

So `filter sender` and `filter path` only stop a sender until they change
their name or path. A [path block](/guides/filter/#path) also drops the
real traffic of the repeater whose ID is in it. Rate limits, hop limits, the
age and malformed checks, channel blocks, regions and the duty cycle keep
working.

## Settings for every flood {#always}

These hold whatever floods the mesh:

- **Duty cycle at 10%.** Your repeater then never transmits more than the
  law allows, whatever comes in. The
  [repeater guide](/repeater-guide/#duty-cycle) covers it.
- **Regions and hop limits.** A region is the area a message stays in. A
  repeater only passes on messages in the regions it holds, and
  `flood.max.*` keeps traffic close. Both are in
  [Keep traffic down](/guides/settings/#traffic).
- **The packet filter for a busy repeater.** The
  [ready-made settings](/guides/filter/#busy) halve group messages and
  adverts. Try them in [dry-run](/guides/filter/#dryrun) first: it only
  counts what it would drop.
- **The companion filter, in the DMC firmware.** Your companion, the node
  you message from, keeps junk out of your app. It hides broken and old
  messages, and messages from a repeater, a sender or a word you block. A
  sender or word rule
  only hides the message from you; others still receive it.

### Duty-cycle gating {#gate}

In the DMC firmware, your repeater can give its own region priority when
it gets busy. Once it has transmitted more than 35% of the last minute, it
stops passing on messages without a region. If it stays busy, it drops the
widest region next, one level at a time. Its own region always passes. It
only works with regions set on your repeater. Switch it on and check it:

```text
set dc.gate on
get dc.gate.status
```

{{< dc-gate >}}

What it drops does not show in `filter stats`. When the repeater is quiet
again, the regions come back, innermost first.

## See a flood {#see}

Your app shows only what reaches you. Only an observer hears a flood of
direct messages to nodes that do not exist. Every observer reports
to the [MeshCore Analyzer](https://meshcore-analyzer.eu/), where everyone
can see it. Turn your repeater into one with
[MQTT on your observer](/guides/mqtt/).

On the Analyzer, look at every copy of one packet. Its path usually shows
where it came from. A flooder can start the path with
[made-up IDs](#forged), so its first IDs tell you nothing. But every copy
carries the same made-up start. The copy with the shortest path passed the
fewest real repeaters, so it was heard closest to the sender.

{{< copies >}}

On your own repeater, `filter stats` shows what the packet filter dropped.
`filter stats top` shows the first byte of the node IDs behind most drops.
That is a lead, not proof.

## Find the source {#source}

When a flood keeps coming back:

1. **Follow the paths.** Read a path from the end: the last IDs are the
   repeaters the flood passed. The earliest real one is near the source;
   the IDs before it can be [made up](#forged).
2. **Narrow down the area.** Several observers that hear the same packet
   place the sender in an area. The
   [DMC Triangulator](https://triangulator.dutchmeshcore.nl/) works it out
   from the repeaters that heard it.
3. **Walk the last kilometre.** The repeaters hear the source only at the
   edge of their range, so the last part takes people on foot.
   [Mesh-Hunter](https://mesh-hunter.eu/) pairs with your companion and
   logs every packet it hears with your GPS position. Several people
   walking at once find it sooner.
4. **Tell your [local group](/community/).** They see more of the mesh,
   they decide what happens next, and they contact whoever floods on
   purpose.

## Add what you saw {#add}

This page grows with what local groups see. Did a flood hit you that is not
in these tables? Did a setting stop one? Tell us on
[Discord](https://discord.meshcore-info.eu/): what you saw and what you
switched on. We add it to the page.
