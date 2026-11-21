---
title: Lista ta' kontroll għar-repeater
lead: Iċċekkja r-repeater tiegħek qabel ma ttellgħu. Kull linja tgħidlek x'għandek tiċċekkja, liema kmand juri dan u liema gwida tispjegah.
description: 'Lista ta'' kontroll għal repeater ta'' MeshCore qabel ma jitla'' fuq bejt jew arblu: x''tiċċekkja permezz tal-USB, kif twaħħlu, u t-test qabel ma titlaq.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '5bbc2cbe'
  seeded: '2026-11-21'
  fields: {title: 'e982ea2f', lead: '664a2839', description: '01f56863'}
  sections: ['d512dacf', '4d357087', '75706984', '8a484df5', '33fd8c68']
  blocks: ['d512dacf', 'a7ba4c46', '6a427551', '2f0a8827', '2bda1638', '589c7b4f', '5fedefb7', 'e12f330e', 'd6d0b21c']
---

Repeater fuq bejt diffiċli tilħqu, għalhekk iċċekkjah waqt li għadu
fuq il-mejda tiegħek. Il-[gwida tar-repeater](/repeater-guide/) tispjega kull
pass. Il-valuri, bħall-preset u l-limiti tal-hop, jiġu
mill-[issettjar taż-żona tiegħek](/guides/settings/). Ikteb il-kmandi permezz tal-USB,
pereżempju fil-[konsol serjali](/firmware/console/). Din il-lista hija skont
il-firmware ta' MeshCore v1.18.0.

## Qabel ma tibda {#start}

- [ ] Il-[mapep tal-kopertura](/map/) jew il-[grupp lokali tiegħek](/community/)
      jgħidu li ż-żona għandha bżonn repeater. Ara [Għandek bżonn wieħed?](/repeater-guide/#need)
- [ ] Is-sid tas-sit aċċetta, u tista' tilħaq ir-repeater għall-manutenzjoni.
- [ ] Il-batterija u l-pannell huma kbar biżżejjed għall-agħar xahar tax-xitwa.
      Ara [Daqs tal-enerġija u tal-pannell solari](/repeater-guide/#power).

## Fuq il-mejda, permezz tal-USB {#usb}

- [ ] Il-bord iħaddem il-firmware **Repeater**: `ver` juri l-verżjoni tiegħu.
      Ara [Issettjah](/repeater-guide/#config).
- [ ] Fuq bord nRF52, it-tweġiba għal `get bootloader.ver` fiha `OTAFIX`.
      Ara [Aġġornah bla wajers](/repeater-guide/#update).
- [ ] `get radio` juri l-preset taż-żona tiegħek.
- [ ] `get dutycycle` juri 10. Ara [Duty cycle](/repeater-guide/#duty-cycle).
- [ ] `get tx` flimkien mal-gain tal-antenna tiegħek ma jaqbiżx 500 mW e.r.p.
      Ara [Qawwa: e.r.p. u l-antenna tiegħek](/repeater-guide/#erp).
- [ ] Il-password tal-admin m'għadhiex `password`.
- [ ] `get guest.password` juri password.
- [ ] `get name` juri l-isem li juża l-grupp lokali tiegħek għar-repeaters tiegħu.
- [ ] `get lat` u `get lon` juru l-pożizzjoni tas-sit.
- [ ] `get owner.info` juri kif l-operaturi l-oħra jilħquk.
- [ ] `region` juri r-reġjuni taż-żona tiegħek. `get flood.max.advert` u
      `get flood.max.unscoped` juru l-limiti tal-hop tagħha. Ara
      [Naqqas it-traffiku](/guides/settings/#traffic).
- [ ] Ħżint iċ-ċavetta privata minn `get prv.key` f'post sigur.
- [ ] `clock` juri l-ħin ta' dan il-mument, f'UTC.
- [ ] Jekk jaħdem bl-enerġija solari, `powersaving` juri `on`.

## Fuq il-bejt {#roof}

- [ ] L-antenna hija mwaħħla qabel ma r-repeater jieħu l-enerġija.
- [ ] L-antenna toqgħod wieqfa fil-quċċata tal-arblu, 'il bogħod mill-metall.
      Ara [Twaħħil](/guides/antenna/#mounting).
- [ ] Kull konnettur ta' barra huwa ssiġillat, u l-kejbil għandu drip loop.
- [ ] Il-kaxxa hija magħluqa, b'toqba għall-arja jew għall-ilma. Ara
      [Hardware](/repeater-guide/#hardware).

## Qabel ma titlaq {#leave}

- [ ] Mill-bogħod, il-companion tiegħek jilħaq ir-repeater fl-app.
- [ ] Bgħatt `advert`, biex in-nodes madwar il-mesh isiru jafu bir-repeater.
- [ ] Il-[grupp lokali tiegħek](/community/) jaf li r-repeater qed jaħdem.
