---
title: "Packet filter"
lead: "Keep your repeater from passing on junk: floods from far away, a bot that never stops, a noisy channel. Try a setting first, then switch it on."
description: "The packet filter of the DMC repeater firmware: what it drops, ready-made settings for a normal and a busy repeater, every filter command with its default, and how to see what it dropped."
---

A repeater (a node that passes messages on) repeats everything it hears.
On a busy mesh that includes junk. A bot posts every minute. One node sends
its advert, the hello that lets others find it, again every few minutes.
Messages arrive that travelled across half the country. Each repeat takes
airtime from everyone around you. The packet filter lets your repeater drop
that traffic instead of passing it on. To find out what floods your mesh
first, and what helps besides the filter, see
[Make the mesh resilient](/guides/resilient/).

{{< callout type="warning" >}}
The packet filter is part of the **DMC repeater firmware**, the repeater
build of [Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore). Stock
MeshCore has no packet filter; it has `region denyf *` and
`set flood.max.unscoped`, on the [CLI commands](/guides/cli/) page. This
guide follows the 1.18.0 dev build `ecfb2d4` of 19 October 2026. The stable
1.17.1 build has the hop, rate, channel, hash and malformed filters only. It
also has no dry-run.
{{< /callout >}}

## What the filter does {#what}

The filter only looks at packets your repeater passes on by flooding (sending
them to every node in range). It never touches what your repeater sends
itself, or packets that follow a known route to one node. Direct messages and
requests to and from your own contacts pass too. It can drop:

- packets that already passed as many repeaters (hops) as you allow, per
  packet type;
- more packets of one type than you allow per minute;
- an advert from a node that already advertised in the last hours;
- messages on a channel you block;
- everything that came through one repeater you block;
- group messages from one sender or with one word, or only some of them;
- group messages that are broken, or older than you allow.

The filter is **off** until you switch it on. You set it with commands. Type
them over USB in the [serial console](/firmware/console/) on this site. Or
send them from the MeshCore app, as in the
[repeater guide](/repeater-guide/#config).

## Get the firmware {#firmware}

Flash **DutchMeshCore Repeater** from the flasher in the
[DutchMeshCore Toolbox](https://toolbox.dutchmeshcore.nl/). The observer
firmware from [MQTT on your observer](/guides/mqtt/) has the same filter.

## Try it first {#dryrun}

In dry-run, the filter counts every packet it would drop, but still passes
it on. Size a setting this way before it drops anything:

```text
filter on
filter dryrun on
```

While dry-run is on, the status line of `filter` ends in `(dry-run)`. The
counts are what it would have dropped. Leave it running for a day, then look
at them (see [What it dropped](#stats)). When the numbers look right, enforce
it:

```text
filter dryrun off
```

## Recommended configurations {#configs}

### A normal repeater {#typical}

```text
filter on
filter malformed on
filter rate 05 20 60
filter rate 02 5 60
filter hops 05 32
```

Group messages pass up to 20 a minute, direct messages up to 5 a minute,
and broken group messages are dropped. The firmware's own normal
configuration allows 20 direct messages a minute. This page takes the 5 it
advises since a flood of direct messages in July 2026.

### A busy repeater {#busy}

For a repeater on a high site that hears a whole region, or one that is
flooded:

```text
filter on
filter malformed on
filter rate 05 10 60
filter rate 02 5 60
filter rate 04 5 60
filter advert 24
filter hops 05 16
filter hops 02 16
filter hops 04 8
```

This halves the group messages and the adverts, and passes each node's
advert once a day. It drops messages that already passed 16 repeaters. After a
reboot, every node gets one advert through. The firmware's own docs also set
`filter hash 2` here; this page leaves it out (see
[Every setting](#settings) for why).

### Block a noisy channel {#channel}

```text
filter channel add #bot
```

Your repeater still hears the channel. It no longer passes it on to other
repeaters and companions (the nodes people message from). Up to 16 channels.

### Slow one sender down {#sender}

A bot that posts too often on a channel you want to keep:

```text
filter watch add #test
filter sender add Bob 60
```

Bob's messages on the Public channel and `#test` now pass once a minute; the
rest is dropped. The filter matches the name in the message, so a sender who
renames gets past it.

### Block one repeater upstream {#path}

When the junk comes in through one repeater, block its prefix: the first
part of its ID, in hexadecimal (hex). This needs the 1.18 dev build; 1.17.1
has no path filter.

```text
filter path add a1b2
filter path list
filter stats path
```

`filter path list` shows the prefixes you block, `filter stats path` how
much each one dropped. `filter path remove a1b2` lets it through again.
A short prefix such as `a1` also blocks every other repeater whose ID starts
with `a1`. Use the longest prefix you can. Up to 8 prefixes.

## Every setting {#settings}

Packet types go by number. On the repeater, `filter types` shows the same
numbers with the firmware's names, such as `TXT_MSG` and `GRP_TXT`:

| Number | Type | Number | Type |
| --- | --- | --- | --- |
| `00` | request | `06` | group data |
| `01` | response | `07` | anonymous request |
| `02` | direct message | `08` | path |
| `03` | acknowledgement | `09` | trace |
| `04` | advert | `10` | multipart |
| `05` | group message | `11` | control |

| Command | What it does | Starts at |
| --- | --- | --- |
| `filter on` / `filter off` | Switch the filter on or off. | off |
| `filter dryrun on` / `off` | Count drops but still pass everything on. | off |
| `filter hops <type> <max>` | Drop a type that already passed this many repeaters, 0 to 64. | 32 for group messages, 8 for the rest |
| `filter rate <type> <limit> <secs> [soft]` | Pass at most `limit` of a type per `secs`. With `soft`, passing tapers off from `soft` to `limit`. `0` turns the limit off. | 20 per 60 s for direct and group messages, 10 for adverts, 5 for the rest |
| `filter advert <hours>` | Pass each node's advert once per this many hours, up to 720. | 0 (off) |
| `filter channel add <#name>` | Stop passing on a channel. | none |
| `filter path add <hex>` | Drop everything that came through a repeater with this prefix, 2 to 8 hex digits. | none |
| `filter sender add <name> [secs] [prob]` | Drop group messages from a sender, on Public and watched channels. `Bot*` matches every name that starts with Bot. | none |
| `filter text add <word> [secs] [prob]` | Drop group messages that contain a word, on Public and watched channels. `^word` matches only at the start. | none |
| `filter watch add <#name>` | Let the sender and text rules read this channel too, up to 4. Public is always read. | Public |
| `filter malformed on` / `off` | Drop Public messages that are empty, broken or dated more than a week off (the date check waits until the clock is set). | off |
| `filter age <minutes>` / `off` | Drop group messages older than this, on Public and watched channels, 1 to 10080. | off |
| `filter hash <bytes>` | Drop packets with a shorter path ID than this, 1 to 3. | 1 |
| `filter reset` | Put every setting back to its default. | |

Each `add` has a `remove` and a `list`, such as `filter channel remove #bot`.
In sender and text rules, `secs` lets one message per that many seconds pass.
`prob` applies the rule to only that share of the matches, 1 to 100. Up to 8
sender and 8 text rules. Names and words are case-sensitive; a name is up to
15 characters, a word up to 23.

Two settings drop more than you may expect:

- `filter hash 2` drops nearly all traffic. Nodes send 1-byte path IDs by
  default.
- `filter age` trusts your repeater's clock. Set it with `clock sync` from the
  app, check it with `clock`, and start generous: `filter age 60`.

Every setting is kept after a reboot.

## What it dropped {#stats}

`filter` shows the totals per reason:

```text
> Filter on: Blocked [ Hops: 3 | Rate: 12 | Channel: 1 | Hash: 0 | Malformed: 2 ]
```

`filter stats <topic>` shows the detail for one setting. The topics are
`hops`, `rate`, `channel`, `hash`, `malformed`, `advert`, `path`, `sender`,
`text` and `age`. `filter stats top` shows the first byte of the node IDs
behind the most drops, a lead rather than proof.
`filter stats air` shows the airtime your repeater saved by not passing these
packets on.

The counters start again at 0 after a reboot and after `clear stats`.
