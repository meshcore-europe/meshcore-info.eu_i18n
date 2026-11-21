---
title: Checklist voor je repeater
lead: Controleer je repeater voordat hij de hoogte in gaat. Elke regel noemt wat je controleert, met welk commando je het ziet en welke gids het uitlegt.
description: 'Een checklist voor een MeshCore-repeater voordat hij op een dak of mast komt: wat je via USB controleert, hoe je hem monteert en wat je test voordat je vertrekt.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '5bbc2cbe'
  seeded: '2026-11-21'
  fields: {title: 'e982ea2f', lead: '664a2839', description: '01f56863'}
  sections: ['d512dacf', '4d357087', '75706984', '8a484df5', '33fd8c68']
  blocks: ['d512dacf', 'a7ba4c46', '6a427551', '2f0a8827', '2bda1638', '589c7b4f', '5fedefb7', 'e12f330e', 'd6d0b21c']
---

Een repeater op een dak is lastig te bereiken. Controleer hem dus zolang hij nog
op je bureau ligt. De [repeatergids](/repeater-guide/) legt elke stap uit. De
waarden, zoals de preset en de hoplimieten, haal je uit de
[instellingen voor jouw omgeving](/guides/settings/). Typ de commando's via USB,
bijvoorbeeld in de [seriële console](/firmware/console/). Deze lijst volgt
MeshCore-firmware v1.18.0.

## Voordat je begint {#start}

- [ ] Volgens de [dekkingskaarten](/map/) of je [lokale groep](/community/)
      heeft de omgeving een repeater nodig. Zie [Heb je er een nodig?](/repeater-guide/#need)
- [ ] De eigenaar van de locatie heeft toestemming gegeven, en je kunt bij de
      repeater komen voor onderhoud.
- [ ] Je hebt accu en zonnepaneel berekend op de slechtste wintermaand. Zie
      [Voeding en zonnepaneel berekenen](/repeater-guide/#power).

## Op je bureau, via USB {#usb}

- [ ] Op het board draait de **Repeater**-firmware: `ver` toont de versie. Zie
      [Instellen](/repeater-guide/#config).
- [ ] Op een nRF52-board staat `OTAFIX` in het antwoord op
      `get bootloader.ver`. Zie [Draadloos bijwerken](/repeater-guide/#update).
- [ ] `get radio` toont de preset van jouw omgeving.
- [ ] `get dutycycle` toont 10. Zie [Duty cycle](/repeater-guide/#duty-cycle).
- [ ] `get tx` plus je antenneversterking blijft binnen 500 mW e.r.p.
      Zie [Vermogen: e.r.p. en je antenne](/repeater-guide/#erp).
- [ ] Het beheerderswachtwoord is niet meer `password`.
- [ ] `get guest.password` toont een wachtwoord.
- [ ] `get name` toont de naam die je lokale groep voor zijn repeaters gebruikt.
- [ ] `get lat` en `get lon` tonen de positie van de locatie.
- [ ] `get owner.info` toont hoe andere beheerders je bereiken.
- [ ] `region` toont de regio's van jouw omgeving. `get flood.max.advert` en
      `get flood.max.unscoped` tonen de hoplimieten ervan. Zie
      [Houd het verkeer laag](/guides/settings/#traffic).
- [ ] Je hebt de privésleutel uit `get prv.key` op een veilige plek bewaard.
- [ ] `clock` toont de huidige tijd, in UTC.
- [ ] Bij zonne-energie toont `powersaving` de waarde `on`.

## Op het dak {#roof}

- [ ] De antenne zit eraan voordat de repeater stroom krijgt.
- [ ] De antenne staat rechtop boven op de mast, uit de buurt van metaal. Zie
      [Montage](/guides/antenna/#mounting).
- [ ] Elke buitenconnector is afgedicht, en de kabel heeft een druiplus.
- [ ] De behuizing is dicht, met een ventilatie- of afvoergaatje. Zie
      [Hardware](/repeater-guide/#hardware).

## Voordat je vertrekt {#leave}

- [ ] Je companion bereikt de repeater op afstand in de app.
- [ ] Je hebt `advert` verstuurd, zodat nodes in de hele mesh de repeater leren kennen.
- [ ] Je [lokale groep](/community/) weet dat hij in de lucht is.
