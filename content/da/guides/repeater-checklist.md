---
title: Tjekliste til repeateren
lead: Tjek din repeater, før den kommer op. Hver linje nævner, hvad du skal tjekke, hvilken kommando der viser det, og hvilken guide der forklarer det.
description: 'En tjekliste til en MeshCore-repeater, før den kommer op på et tag eller en mast: hvad du tjekker over USB, hvordan du monterer den, og testen, før du går.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '5bbc2cbe'
  seeded: '2026-11-21'
  fields: {title: 'e982ea2f', lead: '664a2839', description: '01f56863'}
  sections: ['d512dacf', '4d357087', '75706984', '8a484df5', '33fd8c68']
  blocks: ['d512dacf', 'a7ba4c46', '6a427551', '2f0a8827', '2bda1638', '589c7b4f', '5fedefb7', 'e12f330e', 'd6d0b21c']
---

En repeater på et tag er svær at komme til. Tjek den derfor, mens den stadig
står på dit skrivebord. [Repeater-guiden](/repeater-guide/) forklarer hvert
trin. Værdierne, fx forudindstillingen og hop-grænserne, finder du i
[indstillingerne for dit område](/guides/settings/). Skriv kommandoerne over
USB, fx i [den serielle konsol](/firmware/console/). Listen følger MeshCore
firmware v1.18.0.

## Før du går i gang {#start}

- [ ] [Dækningskortene](/map/) eller din [lokale gruppe](/community/) viser,
      at området har brug for en repeater. Se [Har du brug for en?](/repeater-guide/#need)
- [ ] Ejeren af stedet har sagt ja, og du kan komme til repeateren for at
      vedligeholde den.
- [ ] Batteri og solpanel er dimensioneret til den værste vintermåned. Se
      [Strøm og dimensionering af solceller](/repeater-guide/#power).

## Ved skrivebordet, over USB {#usb}

- [ ] Boardet kører **Repeater**-firmwaren: `ver` viser versionen. Se
      [Sæt den op](/repeater-guide/#config).
- [ ] På et nRF52-board indeholder svaret på `get bootloader.ver` ordet
      `OTAFIX`. Se [Opdatér den trådløst](/repeater-guide/#update).
- [ ] `get radio` viser forudindstillingen for dit område.
- [ ] `get dutycycle` viser 10. Se [Duty cycle](/repeater-guide/#duty-cycle).
- [ ] `get tx` plus din antennes forstærkning holder sig inden for 500 mW
      e.r.p. Se [Effekt: e.r.p. og din antenne](/repeater-guide/#erp).
- [ ] Admin-adgangskoden er ikke længere `password`.
- [ ] `get guest.password` viser en adgangskode.
- [ ] `get name` viser det navn, din lokale gruppe bruger til sine repeatere.
- [ ] `get lat` og `get lon` viser stedets position.
- [ ] `get owner.info` viser, hvordan andre operatører kan kontakte dig.
- [ ] `region` viser regionerne i dit område. `get flood.max.advert` og
      `get flood.max.unscoped` viser områdets hop-grænser. Se
      [Hold trafikken nede](/guides/settings/#traffic).
- [ ] Du har gemt den private nøgle fra `get prv.key` et sikkert sted.
- [ ] `clock` viser det aktuelle tidspunkt i UTC.
- [ ] Kører repeateren på solceller, viser `powersaving` værdien `on`.

## På taget {#roof}

- [ ] Antennen er tilsluttet, før repeateren får strøm.
- [ ] Antennen står lodret øverst på masten, væk fra metal. Se
      [Montering](/guides/antenna/#mounting).
- [ ] Alle udendørs stik er tætnet, og kablet har en drypsløjfe.
- [ ] Kabinettet er lukket og har et ventilations- eller drænhul. Se
      [Hardware](/repeater-guide/#hardware).

## Før du går {#leave}

- [ ] På afstand når din companion repeateren i appen.
- [ ] Du har sendt `advert`, så noder i hele meshet lærer repeateren at kende.
- [ ] Din [lokale gruppe](/community/) ved, at repeateren kører.
