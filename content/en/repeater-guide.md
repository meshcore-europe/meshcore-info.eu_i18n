---
title: "Repeater guide"
lead: "A repeater placed high passes messages on for everyone around it, across a whole town or valley. Pick a site, power it from the sun, set it up, and stay within the law."
description: "Plan, power, configure and legally operate a MeshCore repeater in Europe: site choice, solar sizing, CLI settings, 868 MHz power and duty-cycle limits."
eyebrow: "868 MHz · up to 500 mW · licence-free"
---

Repeaters carry the mesh. Companions, the radios you message from, do not
pass messages on, so without
repeaters you only reach the people in direct range. A repeater in the right
place extends the mesh for everyone around it. This guide follows MeshCore
firmware v1.18.0.

Before you start, talk to your [local group](/community/). They know where
coverage is missing, which [preset your area uses](/guides/settings/) and how to name repeaters. Check the
[coverage maps](/map/) for repeaters near you, and say hello on the public
or local [channels](/guides/channels/).

## Do you need one? {#need}

A repeater sends on every flood message it hears, and all repeaters in
range share the same airtime. Where the mesh already reaches you, one more
repeater adds traffic, not coverage. A companion placed high, at an attic
window or on a balcony, can be all you need.

Put up a repeater where coverage is missing:

- the [coverage maps](/map/) show no repeater near you, or only ones your
  companion does not hear;
- your local group says the area needs one.

## Choose a site {#site}

Height beats power. LoRa at 868 MHz travels best along a clear line of
sight. Hills, buildings and dense trees cost far more range than a few extra
milliwatts win back.

- **Go high.** A rooftop, a mast, a tall building or a hill covers far more
  than a window sill. Even a few metres above the surrounding roofs helps.
- **Keep the antenna in the clear.** Mount it above roof edges, away from
  metal, gutters and other antennas.
- **Check the view.** Tools such as [HeyWhatsThat](https://www.heywhatsthat.com/)
  show what can be seen from a location. If you can see a spot, a repeater
  there is within reach.
- **Leave clearance.** A radio path needs some free space around the direct
  line, not only the line itself. Over long distances, the middle of the path
  should clear obstacles by several metres.
- **Ask permission.** Get the owner's consent for the roof or mast, and agree
  how you will reach the repeater for maintenance.

## Hardware {#hardware}

- **Board.** Pick a low-power nRF52 board such as the
  [Heltec T114](/devices/), RAK WisBlock or the SenseCAP Solar Node. ESP32
  boards draw more power (the devices page marks them High), which makes
  running on solar hard.
- **Antenna.** Use an antenna made for 868 MHz, mounted vertically; the
  [antenna guide](/guides/antenna/) covers types, connectors, cable and
  mounting. Antenna gain counts toward the legal power limit; see
  [Legal limits](#legal).
- **Cable.** Keep coaxial cable short, or use low-loss cable. At 868 MHz a few
  metres of thin cable can lose half your power.
- **Enclosure.** A weatherproof box (IP65 or better) with a cable gland, a
  vent or drain hole against condensation, and a light colour or sun shade.
  Batteries suffer in heat and cannot be charged below freezing.
- **Lightning.** An antenna on a roof is a target. Follow local rules for
  grounding, or mount it where a strike would not reach the building's
  wiring.

## Power and solar sizing {#power}

A solar repeater must survive the darkest weeks of winter. Size it for
them:

1. **Measure the load.** Run the configured repeater through a USB power
   meter for a day. Read the energy used in watt-hours (Wh). Traffic in
   your area changes the number, so measure on site if you can.
2. **Add reserve.** Plan battery capacity for at least 5 to 7 days
   without useful sun.
3. **Find your winter sun.** The EU's free
   [PVGIS tool](https://re.jrc.ec.europa.eu/pvg_tools/en/) shows, for any
   location, how much energy a panel produces per month. Use the month with the
   least sun.
4. **Size the panel.** The panel must replace each day's use in that worst
   month, with room for charging losses.

A worked example, with assumed numbers: a repeater that uses 1 Wh per day
needs a battery of at least 7 Wh for a week of reserve, about 2 Ah of
usable capacity at 3.7 V. If PVGIS says a 1 W panel at your site gives
0.5 Wh per day in December, you need at least a 2 W panel, and 3 to 5 W
leaves margin for clouds, snow and ageing.

## Set it up {#config}

**Flash.** Use the [web flasher](https://flasher.meshcore.io) and choose the
**Repeater** firmware for your board. See
[Get started](/get-started/#flash) for the flashing steps.

**Configure over USB.** With the repeater still connected to your computer,
open [config.meshcore.io](https://config.meshcore.io) or the flasher's
console. You can also use any serial terminal at 115200 baud. The most
important commands:

| What | Command |
|---|---|
| Change the admin password | `password <new password>` |
| Name it | `set name <name>` |
| Radio preset: frequency, bandwidth, SF, CR (reboot to apply) | `set radio 869.618,62.5,8,8` |
| Duty-cycle limit, in percent | `set dutycycle 10` |
| Transmit power of the radio chip, in dBm | `set tx <dBm>` |
| Position, so it shows on maps | `set lat <degrees>` and `set lon <degrees>` |
| Contact details for other operators | `set owner.info <text>` |
| Hours between flood adverts, the ones the whole mesh hears | `set flood.advert.interval <hours>` |
| Announce it now | `advert` |
| Restart | `reboot` |

The default admin password is `password`, and anyone who logs in with it
becomes an admin. Change it before the repeater goes on air.

The `set radio` example above is EU/UK (Narrow). Use the values of your
area's preset instead: [Recommended settings](/guides/settings/) lists them
per country.

**Set the clock.** Without a clock module (RTC), a repeater loses the time at
every power cut and restarts in May 2024. While it runs, its clock also
drifts: it runs further ahead or behind. So set the clock now and then: log
in remotely from the app and use `clock sync`, or set the time over USB. With
an RTC module you rarely need to: it keeps the time through power cuts and
drifts far less.

**Manage it remotely.** Once it is on the mesh, log in from the MeshCore app
with the admin password. You read its status there and use the same commands
over the radio. Some commands work over USB only, such as `set freq` and the
factory reset `erase`.

**Keep its identity.** Before an erase, type `get prv.key` over USB and store
the private key it shows somewhere safe. After the erase, `set prv.key <key>`
and a `reboot` give the repeater its old identity back, so nodes that know
it find it under the same prefix.

The full command list is in the
[MeshCore CLI reference](https://github.com/meshcore-dev/MeshCore/blob/main/docs/cli_commands.md).

## Update it over the air {#update}

Once the repeater is up high, you update it from the ground. Log in from the
MeshCore app with the admin password, open its command line and type
`start ota`. What follows depends on the board; other boards reply `Error`,
and you update those over USB.

**nRF52 boards**, such as RAK, Heltec T114, Seeed XIAO and SenseCAP Solar:

1. Download the **ZIP** of the new firmware for your board from the
   [web flasher](https://flasher.meshcore.io).
2. Type `start ota`. The repeater replies `OK` and shows up over Bluetooth
   as `<board>_OTA`, for example `RAK4631_OTA`.
3. Open the nRF Device Firmware Update app on your phone, pick the ZIP and
   the repeater, and upload. It takes a few minutes.

Install the [OTAFIX bootloader](https://github.com/oltaco/Adafruit_nRF52_Bootloader_OTAFIX)
on an nRF52 board before it goes up. With the stock bootloader, a failed
update can only be repaired over USB. With OTAFIX the board falls back to
update mode, and you try again over Bluetooth.

**ESP32 boards**, such as the Heltec V3 and V4:

1. Download the **non-merged** `.bin` for your board from the web flasher:
   the file without "merged" in its name.
2. Type `start ota`. The repeater opens a WiFi network named `MeshCore-OTA`
   and replies with the address of its upload page.
3. Within WiFi range, connect your phone or laptop to that network, open the
   address and upload the file.

## Legal limits {#legal}

{{< callout type="legal" verified="2026-10-02" >}}
MeshCore's European presets sit in the sub-band **869.40-869.65 MHz**. In the
EU, the UK, Switzerland and Norway it is open to short-range devices without a
licence, within these limits:

- at most **500 mW e.r.p.** radiated power;
- at most **10% duty cycle**: no more than 360 seconds of transmitting in
  any hour, per device. Alternatively a device may use listen-before-talk
  with adaptive frequency agility as defined in ETSI EN 300 220-2;
- the whole signal, at most 250 kHz wide, must stay inside the sub-band.

The band is shared: you must not disturb licensed services, and others may
disturb you.
The radio must be CE marked (in Great Britain, CE or UKCA).
{{< /callout >}}

Sources: [CEPT ERC Recommendation 70-03](https://docdb.cept.org/document/845),
Annex 1, band h1.7;
[Commission Decision 2006/771/EC](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02006D0771(01)-20250123)
and its amendments;
[ETSI EN 300 220-2](https://www.etsi.org/deliver/etsi_en/300200_300299/30022002/03.03.01_60/en_30022002v030301p.pdf),
band O.

### Power: e.r.p. and your antenna {#erp}

The limit applies to the *radiated* power, measured against a simple dipole
antenna (e.r.p.). Antenna gain counts; cable loss subtracts. Makers state
antenna gain in dBi, which is 2.15 dB more than the same gain in dBd
(relative to a dipole). Keep this sum at or below 27 dBm (500 mW):

> transmit power (dBm) + antenna gain (dBi) − cable loss (dB) − 2.15 ≤ 27

- A board transmitting 22 dBm into a 5 dBi antenna through 1 dB of cable:
  22 + 5 − 1 − 2.15 = 23.85 dBm, about 240 mW e.r.p. Within the limit.
- A board with a 30 dBm (1 W) amplifier into a 3 dBi antenna:
  30 + 3 − 2.15 = 30.85 dBm, about 1.2 W e.r.p. Over the limit; lower the
  transmit power.

`set tx` sets the output of the LoRa chip, in dBm. The SX1262 chip itself
tops out at 22 dBm; the firmware does not check the number you enter. Boards with an extra
amplifier, such as the Heltec V4 or the Station G2, transmit much more than
the number you set. Check the manufacturer's table before you set it, and
start low.

### Duty cycle {#duty-cycle}

A repeater transmits for everyone around it, so it uses up its airtime faster
than a companion. MeshCore's duty-cycle limiter defaults to 50%, which is
above what this band allows. Set it to 10% on every repeater:

```text
set dutycycle 10
```

### Frequency accuracy {#frequency}

The EU/UK (Narrow) channel, 869.618 MHz with 62.5 kHz bandwidth, reaches up
to 869.649 MHz: less than 1 kHz below the top of the sub-band. The signal
must stay inside the band at every temperature. That takes a
temperature-compensated crystal (TCXO). Nearly every current board has one;
older boards without, such as the Heltec V2, drift too far to work reliably
at 62.5 kHz.

### Country notes {#countries}

- **EU member states** must make this sub-band available on these terms
  (Decision 2006/771/EC, Article 3).
- **United Kingdom:** the same limits, in Ofcom
  [IR 2030](https://www.ofcom.org.uk/spectrum/radio-equipment/short-range-devices).
- **Switzerland and Liechtenstein:** the same limits, in OFCOM
  [RIR1008-09](https://www.ofcomnet.ch/api/rir/1008/09).
- **Norway:** the same limits, in the
  [regulation on general authorisations](https://lovdata.no/dokument/SF/forskrift/2012-01-19-77)
  (fribruksforskriften).

These notes are not legal advice. Rules change; when in doubt, check with
your national regulator.

## Deployment checklist {#checklist}

- [ ] The site owner agreed, and you can reach the repeater for maintenance.
- [ ] The board runs the **Repeater** firmware, and the antenna was attached
      before first power-on.
- [ ] The admin password is changed.
- [ ] The radio matches [your area's preset](/guides/settings/) (`get radio`).
- [ ] `set dutycycle 10` is set.
- [ ] Transmit power plus antenna gain stays within 500 mW e.r.p.
- [ ] The name, position and `owner.info` are set, so others know who runs it.
- [ ] The clock is set (`clock`).
- [ ] The enclosure is sealed, with a drain or vent hole, and the cable has a
      drip loop.
- [ ] Battery and panel are sized for the worst winter month.
- [ ] You tested it from a distance with the app before leaving the site.
- [ ] Your local group knows it is up.
