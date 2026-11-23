---
title: Checklista för repeatern
lead: Kontrollera din repeater innan den sätts upp. Varje rad säger vad du kontrollerar, vilket kommando som visar det och vilken guide som förklarar det.
description: 'En checklista för en MeshCore-repeater innan den hamnar på ett tak eller en mast: vad du kontrollerar via USB, hur du monterar den och vilket test du gör innan du går.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '5bbc2cbe'
  seeded: '2026-11-21'
  fields: {title: 'e982ea2f', lead: '664a2839', description: '01f56863'}
  sections: ['d512dacf', '4d357087', '75706984', '8a484df5', '33fd8c68']
  blocks: ['d512dacf', 'a7ba4c46', '6a427551', '2f0a8827', '2bda1638', '589c7b4f', '5fedefb7', 'e12f330e', 'd6d0b21c']
---

En repeater på ett tak är svår att komma åt, så kontrollera den medan den
fortfarande står på skrivbordet. [Repeaterguiden](/repeater-guide/) förklarar
varje steg. Värdena, till exempel förinställningen och hoppgränserna, hittar du
i [inställningarna för ditt område](/guides/settings/). Skriv kommandona via
USB, till exempel i [seriekonsolen](/firmware/console/). Listan gäller MeshCore
firmware v1.18.0.

## Innan du börjar {#start}

- [ ] [Täckningskartorna](/map/) eller din [lokala grupp](/community/) säger
      att området behöver en repeater. Se [Behöver du en?](/repeater-guide/#need)
- [ ] Ägaren till platsen har sagt ja, och du kommer åt repeatern för
      underhåll.
- [ ] Batteri och panel är dimensionerade för den sämsta vintermånaden. Se
      [Ström och dimensionering av solceller](/repeater-guide/#power).

## Vid skrivbordet, via USB {#usb}

- [ ] Kortet kör firmwaren **Repeater**: `ver` visar versionen. Se
      [Ställ in den](/repeater-guide/#config).
- [ ] På ett nRF52-kort innehåller svaret på `get bootloader.ver` texten
      `OTAFIX`. Se [Uppdatera den trådlöst](/repeater-guide/#update).
- [ ] `get radio` visar förinställningen för ditt område.
- [ ] `get dutycycle` visar 10. Se [Duty cycle](/repeater-guide/#duty-cycle).
- [ ] `get tx` plus antennens förstärkning håller sig inom 500 mW e.r.p. Se
      [Effekt: e.r.p. och din antenn](/repeater-guide/#erp).
- [ ] Adminlösenordet är inte längre `password`.
- [ ] `get guest.password` visar ett lösenord.
- [ ] `get name` visar det namn som din lokala grupp använder för sina
      repeatrar.
- [ ] `get lat` och `get lon` visar platsens position.
- [ ] `get owner.info` visar hur andra operatörer når dig.
- [ ] `region` visar regionerna i ditt område. `get flood.max.advert` och
      `get flood.max.unscoped` visar områdets hoppgränser. Se
      [Håll nere trafiken](/guides/settings/#traffic).
- [ ] Du har sparat den privata nyckeln från `get prv.key` på ett säkert ställe.
- [ ] `clock` visar aktuell tid i UTC.
- [ ] Vid soldrift visar `powersaving` värdet `on`.

## På taket {#roof}

- [ ] Antennen är ansluten innan repeatern får ström.
- [ ] Antennen står lodrätt överst på masten, en bit från metall. Se
      [Montering](/guides/antenna/#mounting).
- [ ] Varje kontakt utomhus är tätad, och kabeln har en droppögla.
- [ ] Kapslingen är stängd och har ett ventilations- eller dräneringshål. Se
      [Hårdvara](/repeater-guide/#hardware).

## Innan du går {#leave}

- [ ] På avstånd når din companion repeatern i appen.
- [ ] Du har skickat `advert`, så att noder i hela meshen får veta om repeatern.
- [ ] Din [lokala grupp](/community/) vet att den är igång.
