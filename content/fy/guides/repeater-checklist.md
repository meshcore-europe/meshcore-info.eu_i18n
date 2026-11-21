---
title: Kontrôlelist foar in repeater
lead: Kontrolearje dyn repeater foardat er omheech giet. Elke rigel neamt wat do kontrolearrest, it kommando dat it sjen lit en de gids dy't it útleit.
description: 'In kontrôlelist foar in MeshCore-repeater foardatsto him op in dak of mêst setst: wat do oer USB kontrolearrest, hoe''tsto him montearrest en de test foardatsto fuortgiest.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '5bbc2cbe'
  seeded: '2026-11-21'
  fields: {title: 'e982ea2f', lead: '664a2839', description: '01f56863'}
  sections: ['d512dacf', '4d357087', '75706984', '8a484df5', '33fd8c68']
  blocks: ['d512dacf', 'a7ba4c46', '6a427551', '2f0a8827', '2bda1638', '589c7b4f', '5fedefb7', 'e12f330e', 'd6d0b21c']
---

In repeater op in dak is dreech te berikken, dus kontrolearje him wylst er noch
op dyn buro stiet. De [repeaterhantlieding](/repeater-guide/) leit elke stap út.
De wearden, lykas de preset en de hoplimiten, komme út de
[ynstellings foar dyn gebiet](/guides/settings/). Typ de kommando's fia USB,
bygelyks yn de [seriële konsole](/firmware/console/). Dizze list folget
MeshCore firmware v1.18.0.

## Foardatsto begjinst {#start}

- [ ] De [dekkingskaarten](/map/) of dyn [pleatslike groep](/community/) sizze
      dat it gebiet in repeater nedich hat. Sjoch [Hasto der ien nedich?](/repeater-guide/#need)
- [ ] De eigener fan it plak hat ynstimd, en do kinst by de repeater komme
      foar ûnderhâld.
- [ ] Batterij en paniel binne berekkene op de slimste wintermoanne. Sjoch
      [Enerzjy en sinnepanielen berekkenje](/repeater-guide/#power).

## Oan dyn buro, fia USB {#usb}

- [ ] Op it board stiet de **Repeater**-firmware: `ver` lit de ferzje sjen. Sjoch
      [Ynstelle](/repeater-guide/#config).
- [ ] Op in nRF52-board stiet `OTAFIX` yn it antwurd op `get bootloader.ver`.
      Sjoch [Oer de loft bywurkje](/repeater-guide/#update).
- [ ] `get radio` lit de preset fan dyn gebiet sjen.
- [ ] `get dutycycle` lit 10 sjen. Sjoch [Duty cycle](/repeater-guide/#duty-cycle).
- [ ] `get tx` plus de winst fan dyn antenne bliuwt binnen 500 mW e.r.p. Sjoch
      [Fermogen: e.r.p. en dyn antenne](/repeater-guide/#erp).
- [ ] It adminwachtwurd is net mear `password`.
- [ ] `get guest.password` lit in wachtwurd sjen.
- [ ] `get name` lit de namme sjen dy't dyn pleatslike groep foar har repeaters brûkt.
- [ ] `get lat` en `get lon` litte de posysje fan it plak sjen.
- [ ] `get owner.info` lit sjen hoe't oare operators dy berikke.
- [ ] `region` lit de regio's fan dyn gebiet sjen. `get flood.max.advert` en
      `get flood.max.unscoped` litte de hoplimiten sjen. Sjoch
      [Hâld it ferkear leech](/guides/settings/#traffic).
- [ ] Do hast de privee kaai út `get prv.key` op in feilich plak bewarre.
- [ ] `clock` lit de tiid fan no sjen, yn UTC.
- [ ] By sinne-enerzjy lit `powersaving` `on` sjen.

## Op it dak {#roof}

- [ ] De antenne sit fêst foardat de repeater stroom krijt.
- [ ] De antenne stiet rjocht oerein boppe op de mêst, frij fan metaal. Sjoch
      [Montearje](/guides/antenna/#mounting).
- [ ] Elke ferbiner bûtendoar is ôfdichte, en de kabel hat in druplus.
- [ ] De behuzing is ticht, mei in fentilaasje- of ôfwetteringsgat. Sjoch
      [Hardware](/repeater-guide/#hardware).

## Foardatsto fuortgiest {#leave}

- [ ] Op ôfstân berikt dyn companion de repeater yn de app.
- [ ] Do hast `advert` stjoerd, sadat nodes yn de hiele mesh de repeater leare kennen.
- [ ] Dyn [pleatslike groep](/community/) wit dat er draait.
