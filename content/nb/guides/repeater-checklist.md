---
title: Sjekkliste for repeater
lead: Sjekk repeateren din før den kommer opp. Hver linje sier hva du skal sjekke, hvilken kommando som viser det og hvilken veiledning som forklarer det.
description: 'En sjekkliste for en MeshCore-repeater før den monteres på tak eller mast: hva du sjekker over USB, hvordan du monterer den og hvilken test du gjør før du går.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '5bbc2cbe'
  seeded: '2026-11-21'
  fields: {title: 'e982ea2f', lead: '664a2839', description: '01f56863'}
  sections: ['d512dacf', '4d357087', '75706984', '8a484df5', '33fd8c68']
  blocks: ['d512dacf', 'a7ba4c46', '6a427551', '2f0a8827', '2bda1638', '589c7b4f', '5fedefb7', 'e12f330e', 'd6d0b21c']
---

En repeater på et tak er vanskelig å komme til, så sjekk den mens den
ennå står på pulten din. [Repeater-veiledningen](/repeater-guide/) forklarer
hvert steg. Verdiene, som forhåndsinnstillingen og hoppgrensene, finner du
i [innstillingene for området ditt](/guides/settings/). Skriv inn kommandoene
over USB, for eksempel i [seriekonsollen](/firmware/console/). Denne listen
følger MeshCore firmware v1.18.0.

## Før du begynner {#start}

- [ ] [Dekningskartene](/map/) eller [den lokale gruppen din](/community/) sier
      at området trenger en repeater. Se [Trenger du en?](/repeater-guide/#need)
- [ ] Eieren av stedet har sagt ja, og du kommer til repeateren for å
      vedlikeholde den.
- [ ] Batteri og solpanel er dimensjonert for den verste vintermåneden. Se
      [Strøm og dimensjonering av solceller](/repeater-guide/#power).

## Ved pulten, over USB {#usb}

- [ ] Kortet kjører **Repeater**-firmwaren: `ver` viser versjonen. Se
      [Sett den opp](/repeater-guide/#config).
- [ ] På et nRF52-kort inneholder svaret på `get bootloader.ver` teksten
      `OTAFIX`. Se [Oppdater den trådløst](/repeater-guide/#update).
- [ ] `get radio` viser forhåndsinnstillingen for området ditt.
- [ ] `get dutycycle` viser 10. Se [Duty cycle](/repeater-guide/#duty-cycle).
- [ ] `get tx` pluss antenneforsterkningen din holder seg innenfor 500 mW e.r.p.
      Se [Effekt: e.r.p. og antennen din](/repeater-guide/#erp).
- [ ] Administratorpassordet er ikke lenger `password`.
- [ ] `get guest.password` viser et passord.
- [ ] `get name` viser navnet den lokale gruppen din bruker på repeaterne sine.
- [ ] `get lat` og `get lon` viser posisjonen til stedet.
- [ ] `get owner.info` viser hvordan andre operatører når deg.
- [ ] `region` viser regionene i området ditt. `get flood.max.advert` og
      `get flood.max.unscoped` viser hoppgrensene der. Se
      [Hold trafikken nede](/guides/settings/#traffic).
- [ ] Du har lagret den private nøkkelen fra `get prv.key` på et trygt sted.
- [ ] `clock` viser klokkeslettet akkurat nå, i UTC.
- [ ] Ved soldrift viser `powersaving` verdien `on`.

## På taket {#roof}

- [ ] Antennen er koblet til før repeateren får strøm.
- [ ] Antennen står loddrett på toppen av masten, unna metall. Se
      [Montering](/guides/antenna/#mounting).
- [ ] Alle utendørs kontakter er tettet, og kabelen har en dryppsløyfe.
- [ ] Kapslingen er lukket og har et lufte- eller dreneringshull. Se
      [Maskinvare](/repeater-guide/#hardware).

## Før du går {#leave}

- [ ] På avstand når companion-enheten din repeateren i appen.
- [ ] Du har sendt `advert`, så noder i hele meshet får vite om repeateren.
- [ ] [Den lokale gruppen din](/community/) vet at den er i drift.
