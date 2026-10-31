---
title: "What is MeshCore?"
lead: "MeshCore sends text messages by radio, from node to node. It works without the internet or a subscription."
description: "What MeshCore is and is not: the mesh, companions, repeaters and room servers, routing, encryption, and the 868 MHz band in Europe."
eyebrow: "MeshCore v1.18.0"
---

MeshCore is free software for small LoRa radios. LoRa is a radio technique
that sends little data far, on very little power. A radio with MeshCore is
called a *node*. Paired with the app on your phone or laptop, or with its own
screen and keyboard, it sends text to people kilometres away. No tower, router or provider sits in between.

The software is open source, developed at
[meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore) under the MIT
licence.

## What MeshCore is not {#not}

New to radio? These are the things people most often expect from MeshCore,
and that it does not do.

- **It is not the internet or a phone.** MeshCore sends short text messages,
  about the length of a text message on your phone. No voice, photos, video
  or websites, and you cannot reach a normal phone number.
- **It is not an emergency service.** No emergency service listens on the
  mesh, and nobody promises that someone reads your message. In an
  emergency, call 112.
- **It is not instant, and not everywhere.** A message hops from radio to
  radio and can take a few seconds, or not arrive at all. Whether it gets
  through depends on the repeaters around you, on height, buildings and your
  antenna. A small radio indoors often reaches nobody; a repeater on a roof
  reaches kilometres.
- **It is not a service someone runs for you.** There is no provider, no
  helpdesk and no coverage promise. The mesh exists where people in the
  community have put up repeaters, and nowhere else.
- **Not everything on it is private.** Direct messages are encrypted, but
  Public and the hashtag channels can be read by anyone, and your node's
  name and shared position are visible to everyone in range.
  [Observers](/network/) report what they hear to public maps. The
  [encryption section](#encryption) explains what stays private.
- **It is not unlimited.** Everyone in an area shares one radio channel, and
  the rules for the [868 MHz band](#band) limit how long each radio may send.
  Every message takes airtime from everyone else, so bots, frequent adverts
  and test messages slow the mesh down for all.
- **It is not Meshtastic.** Meshtastic is a different system that runs on
  much the same boards. The two cannot talk to each other.

## The mesh in a minute {#mesh}

One LoRa radio reaches a few kilometres in a town, and much further from a
hill or a roof. To get further, radios pass messages on for each other: that
is a *mesh*. In MeshCore, radios called *repeaters* do the passing on. A
repeater that hears a message sends it again, so it can cross a whole region.

Nobody owns the mesh. Every node and every repeater belongs to someone in the
community. The mesh reaches as far as their repeaters do.

## The 3 kinds of node {#roles}

You choose a node's kind when you flash it. Your first node is a companion.

**Companion.** Your own radio. It pairs with the MeshCore app on your phone or
laptop over Bluetooth or USB; some have their own screen and keyboard. The app
is where you read and type. The companion keeps your contacts and channels,
and the messages that arrived while the app was not connected. A companion does not pass on messages for others.

**Repeater.** A radio placed high that passes on messages for everyone. Most
run on solar power. You only need your own where the mesh does not reach
yet. It has no app of its own. You set it up over USB, or
log in with a password and manage it over the radio. The
[repeater guide](/repeater-guide/) shows how.

**Room server.** A small message board on the mesh. When you log in, you get
the posts you missed while out of range, up to the last 32. It keeps them
in memory only, so a restart or a power cut clears them. A local group uses
one for announcements.

## How a message finds its way {#routing}

Every node has a secret key and a public key. The public key is its identity. A node
announces itself with an *advert*: a signed packet with its name and, if you
choose, its position. Someone appears in your contacts after one of their
adverts reached you, or when you scan their QR code. The app has a button to send your own.

Your first message to a contact goes out as a *flood*. Every repeater that
hears it passes it on once, and adds its own short ID on the way. The reply
carries that list of IDs back. From then on your messages to that contact
follow the recorded route, and only the repeaters on it send. When the route
breaks, the app floods again.

Messages to a channel have no single address, so they always flood.
Repeaters remember what they recently passed on and drop copies that arrive
again by another route. A message can cross up to 64 repeaters, or 32 where the preset uses 2-byte
IDs.

## Encryption and privacy {#encryption}

Your direct messages are encrypted end to end: only you and the other person
can read them. A repeater sees who a packet is for only as a 1-byte hint.

Channels are encrypted with a shared key, so who can read them depends on who
has that key:

- **Public** is set up on every companion. Its key is published, so anyone
  can read it.
- **Hashtag channels**, such as `#utrecht`, take their key from their name.
  Anyone who knows the name can join, so treat them as public too.
- **Private channels** use a random key that you share yourself, for example
  as a QR code.

Adverts are signed but not encrypted. Your node's name, and its position if
you share it, are visible to everyone in range. Pick a name that says no more
than you want.

## The 868 MHz band in Europe {#band}

In Europe, MeshCore uses a small part of the 868 MHz band that anyone may use
without a licence. Its European radio preset, EU/UK (Narrow), sits at
869.618 MHz on a 62.5 kHz channel. That is inside the 869.40-869.65 MHz
sub-band, which allows up to 500 mW e.r.p. A device may send there at most 10%
of the time. The
[legal section of the repeater guide](/repeater-guide/#legal) has the details
and the limits per country.

Everyone in an area uses the same preset, or their radios cannot hear each
other. Some countries and regions use a variant: your
[local group](/community/) knows which one.

## What people use it for {#uses}

- Staying in touch on hikes, at sea and at festivals where the mobile network
  is overloaded or absent.
- A backup channel for family or neighbours when power or mobile networks
  fail.
- Local chat on radios that people own themselves.
- Experimenting with radio, antennas, solar power and open-source software.

## Where the data comes from {#data}

The search on the [local groups](/community/) page finds a place with a copy of
the free place and postcode lists of [GeoNames](https://www.geonames.org/),
licensed under
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). The copy lives on
this site. Your search never leaves your device, and no request goes to
GeoNames.
