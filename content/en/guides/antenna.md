---
title: "Antenna guide"
lead: "The antenna is half your node. The right one, mounted well, reaches further than more power. Check the antenna on your companion, then choose, connect and mount one for a repeater."
description: "Choose and mount a MeshCore antenna for 868 MHz: check a companion whip, antenna types and gain, connectors, cable loss per metre, filters, mounting and how gain counts toward the legal limit."
eyebrow: "Companion and repeater · 868 MHz"
---

Height, a tuned antenna and a short cable win more range than any extra
milliwatt. This guide starts with the companion, the radio you message
from. Then it covers the antenna on a repeater, a node that passes
messages on from a roof or mast.

## Your companion {#companion}

{{< callout type="warning" >}}
Attach the antenna before you switch the radio on. A LoRa radio that
transmits without an antenna can damage its own chip.
{{< /callout >}}

The antenna that came with your board does the job. Attach it, hold the
node upright, and start messaging. A better
antenna on a companion wins little; a repeater within reach wins a lot.

Buy a separate whip only when the supplied one is broken or missing. Not
every whip sold for 868 MHz is tuned for it. [Check it with a
NanoVNA](#nanovna), a pocket antenna analyser, before you trust it, or borrow one from a board that
works.

A node next to a strong transmitter hears less than it should. A small
[SAW (surface acoustic wave) filter](#filters) between the radio and the
antenna keeps that transmitter out of the receiver. Check its datasheet
first:

- **Maximum input power.** The filter also sits in the path of your own
  transmission. A board transmitting 22 dBm (160 mW) into a filter rated for 15 dBm
  breaks the filter.
- **Passband.** It must include your preset's frequency. A filter for
  868.65 to 869.25 MHz does not pass the EU/UK (Narrow) channel on
  869.618 MHz.

## Antenna types for a repeater {#types}

Every antenna on the mesh stands upright. Pick the type by where the nodes
are that you want to reach:

- **Fibreglass collinear.** A white tube on a mast, with gain all around
  the horizon. The standard choice for a repeater that serves a town.
- **Dipole.** Shorter, with less gain and a tall beam. It reaches nodes
  below and above you better than a collinear. That matters on a hill
  above a valley.
- **Yagi.** A boom with cross elements, aimed at one place. It reaches a
  single far repeater and little else. Mount it with the elements upright,
  because its polarisation follows the elements.

## Gain and the beam {#gain}

Gain does not add power. It takes the signal that would go up and down
and sends it along the horizon. Like a torch you focus: the same battery,
a longer and narrower beam. A dipole and a collinear of the same maker
show it:

| Antenna | Gain | Vertical beamwidth |
|---|---|---|
| Dipole (Sirio SO 868-915-2) | 2.2 dBi | 88 degrees |
| Fibreglass collinear (Sirio SPO 868-915-6) | 5.8 dBi | 23 degrees |

{{< gain >}}

The diagram cuts through the mast, seen from the side. Turn it round the
mast and you have the whole beam: a doughnut for the dipole, a flat disc
for the collinear. An upright antenna sends the same way in every direction around
it. Outside the drawn beam the signal does not stop; it is weaker, still
enough for a node close by.

On a roof, a flat beam is what you want. On a hill high above the nodes,
a 23 degree beam passes over their heads; a dipole covers them. A Yagi
takes this further: 16.6 dBi in a beam 23 degrees tall
and 25 degrees wide (Amphenol Procom
7176870), and nothing to the sides.

Gain counts against a reference. dBi compares with an ideal antenna that
sends equally in every direction. dBd compares with a half-wave dipole,
which has 2.15 dBi itself: even the simplest antenna sends nothing straight
up or down. A longer dipole, 1.25 wavelengths, reaches 5.2 dBi. A collinear
stacks half-wave elements above each other instead: the more it stacks, the
higher the gain. Squeeze the same signal into half the space and it is
twice as strong there: 3 dB. Into a quarter, 4 times as strong: 6 dB.
Makers state gain in dBi; the legal limit counts in dBd, see
[Within the legal limit](#legal).

### Which gain for your site {#choose-gain}

- **Hills, valleys or a dense city: about 3 dBi.** The tall beam reaches
  nodes above and below you, and round the slopes and buildings in the way.
  It also works the other way: from a valley, a flat beam passes under a
  repeater on the hill above. The RAKwireless RAKARG12 is one: a
  fibreglass tube of 36 cm.
- **Suburbs or a town with low roofs: 5 to 6 dBi.** The standard
  fibreglass collinear.
- **Flat, open land: 8 to 10 dBi.** The flattest beam reaches furthest
  along the horizon. Mounted high, it passes over the nodes close by.

The gain in the name is the best figure across the antenna's whole band.
The RAKARG12, sold as 3 dBi, has 2.8 dBi at 865 to 870 MHz. Read the gain
table in the datasheet at your preset's frequency.

Above 7 dBi a 22 dBm board goes over the legal limit, unless cable and filter
loss make up the difference. Lower the transmit power to match.

High gain only helps when you know where the nodes are: along the horizon
round a repeater, or at one far repeater for a Yagi. A companion in your
hand points every way, so the low gain it came with suits it best.

## Why vertical {#vertical}

Antennas hear each other best when they point the same way. The loss grows
with the angle between them: 45 degrees costs 3 dB, half your signal. At
90 degrees, a flat antenna against an upright one, in theory nothing
arrives. The mesh stands upright, so your antenna does too. This also holds
for a companion on a desk: lay it flat and every node around you hears
less.

## Connectors {#connectors}

Order the antenna with the connector
your board has. Every adapter is one more joint to seal and more signal
lost.

- **SMA.** A threaded connector about 6 mm wide. The socket on most boards
  has a hole in the centre; the antenna has the pin. A connector of this
  kind loses about 0.03 dB at 868 MHz.
- **RP-SMA.** The same body and thread as SMA, with the pin and the hole
  swapped. It looks like SMA and does not mate with it. Check which one
  your board has before you order.
- **U.FL (IPEX).** A tiny push-on socket on the board itself. A short
  pigtail cable runs from it to an SMA socket in the case. It is rated for
  30 mating cycles, so connect it once and leave it.
- **N.** The large threaded connector on fibreglass antennas and thick
  cable. It loses at most 0.05 dB. A repeater needs one
  adapter or pigtail from N to the board's SMA.

## Cable loss {#cable}

Cable costs signal before it leaves the antenna, in both directions. 3 dB
is half your power. The makers' figures per metre, at 868 to 900 MHz:

| Cable | Loss per metre | Loss over 5 m |
|---|---|---|
| RG174 | 1.02 dB | 5.1 dB |
| RG316 | 0.78 dB | 3.9 dB |
| RG58 | 0.45 dB | 2.2 dB |
| H-155 | 0.27 dB | 1.4 dB |
| LMR-240 | 0.25 dB | 1.2 dB |
| Ecoflex 10 | 0.13 dB | 0.7 dB |
| LMR-400 | 0.13 dB | 0.6 dB |

3 metres of RG174, the thin pigtail supplied with many boards, loses half
your power. Mount the board at the antenna with a short pigtail, or
run thick cable to it. Add every adapter and filter in the path to the sum.

## Filters {#filters}

A filter sits between the radio and the antenna. It passes your band and
blocks the rest, so a strong transmitter nearby does not swamp the
receiver. You need one when a node hears less than it should near other
transmitters. A repeater on a mast with mobile phone base stations is such
a node. A filter costs signal in both directions: count its loss like
cable.

| | SAW filter | Cavity filter |
|---|---|---|
| Size | A few millimetres, on a small board | A metal block or tube |
| Loss of a good one | under 2 dB | under 1 dB |
| Maximum input power of a good one | 500 mW | several watts |

The sysmocom cf866.5-kt30, for example, is a cavity filter for 863 to
870 MHz that loses 1.0 dB at most and takes 30 W. It is made for indoors,
so put it in a sealed box on a mast.

Filters differ a lot, so check the datasheet before you buy. Its rated
input power must exceed your transmit power, and its passband must include
your preset's frequency.

## Mounting {#mounting}

- **Above the roof edge.** The antenna needs a clear view in every
  direction it serves. Even a few metres above the surrounding roofs
  helps. [Choose a site](/repeater-guide/#site) in the repeater guide shows
  how to check the view.
- **Away from metal.** Gutters, masts, other antennas and metal roofs next
  to the antenna change its pattern and tuning. Mount it on top of the
  mast, not beside it.
- **Upright.** Use a spirit level; see [Why vertical](#vertical).
- **Drip loop.** Let the cable hang below the connector before it goes up
  or in. Water then drips off instead of running into the joint.
- **Seal every outdoor connector.** Water in a connector raises the loss
  and corrodes the pin. Seal it against rain and check the seal each year.
- **Lightning.** An antenna on a roof is a target. A gas discharge arrestor
  in the cable fires on a surge and sends it to ground. Follow
  [Hardware](/repeater-guide/#hardware) in the repeater guide and your local
  rules for grounding.

## Within the legal limit {#legal}

{{< callout type="legal" verified="2026-10-22" >}}
In Europe MeshCore uses the sub-band 869.40-869.65 MHz, with at most
**500 mW** effective radiated power (e.r.p.). The limit counts what leaves the antenna:
antenna gain adds, cable and filter loss subtract. Gain in dBi counts
2.15 dB less, because the limit is measured against a dipole.
{{< /callout >}}

A 5.8 dBi collinear on a 22 dBm board stays within the limit. The same
antenna on a board with an amplifier does not, until you lower the transmit
power. [Power: e.r.p. and your antenna](/repeater-guide/#erp) in the
repeater guide has the sum and 2 worked examples.

## Check an antenna with a NanoVNA {#nanovna}

A NanoVNA is a pocket-size vector network analyser. It shows at which
frequency an antenna is tuned, so you know before you mount it. The
NanoVNA-H measures up to 1.5 GHz, which covers 868 MHz.

1. Calibrate it for 800 to 950 MHz with the open, short and load pieces
   from its kit.
2. Connect the antenna through the adapter it will use on the node. Hold it
   upright and away from your body and the table.
3. Read the SWR (standing wave ratio) curve: it shows how much signal
   the antenna sends back. The dip must sit on your preset's frequency, 869.618
   MHz for EU/UK (Narrow). A dip hundreds of MHz away means the antenna is
   made for another band.

A quarter wave at 868 MHz is 86 mm (the wavelength is 345 mm). Length
alone does not tell you the band, because makers fold and load whips; the
NanoVNA does.

## Sources {#sources}

- Cable loss: [Belden 8216 (RG174)](https://catalog.belden.com/techdata/en/8216_techdata.pdf),
  the Huber+Suhner RG316 datasheet,
  [Belden 8240 (RG58)](https://catalog.belden.com/techdata/en/8240_techdata.pdf),
  [SSB H-155](https://www.ssb.de/media/h155ssb-en.pdf),
  the Times Microwave LMR-240 and LMR-400 datasheets,
  [SSB Ecoflex 10](https://www.rigpix.com/otherusefulinfo/coax/ecoflex10.pdf).
- Antennas: [Sirio SPO 868-915-6](https://rigpix.com/antennas/sirio_spo8689156_manual.pdf),
  the Sirio SO 868-915-2 datasheet,
  [Amphenol Procom 7176870](https://amphenolprocom.com/products/base-station-antennas/2236-7176870),
  [RAKwireless RAKARG12](https://docs.rakwireless.com/product-categories/accessories/rakarg12/datasheet/).
- Gain as signal squeezed into less space: [RF Cafe, antenna introduction](https://www.rfcafe.com/references/electrical/ew-radar-handbook/antenna-introduction-basics.htm).
- Connectors: the Rosenberger 32S102 (SMA) and 53S101 (N) datasheets, the
  Hirose U.FL catalogue.
- Filters: the sysmocom cf866.5-kt30 product page,
  [Citel gas discharge arrestors](https://citel.us/en/gas-tube-surge-arrestors-for-coaxial-line-protection).
- Polarisation loss: [University of Toronto, Friis effects](https://www.waves.utoronto.ca/prof/svhum/ece422/notes/12-friiseffects.pdf).
- Dipole gain by length: [Wikipedia, Dipole antenna](https://en.wikipedia.org/wiki/Dipole_antenna).
- Wavelength: speed of light from [NIST](https://physics.nist.gov/cgi-bin/cuu/Value?c).
- NanoVNA: [NanoVNA-H](https://github.com/hugen79/NanoVNA-H).
- Legal limit: [CEPT ERC Recommendation 70-03](https://docdb.cept.org/document/845),
  Annex 1, band h1.7; the [repeater guide](/repeater-guide/#legal) lists the
  rest.
