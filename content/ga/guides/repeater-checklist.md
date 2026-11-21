---
title: Seicliosta athsheoltóra
lead: Seiceáil d'athsheoltóir sula gcuireann tú suas é. Ainmníonn gach líne an rud le seiceáil, an t-ordú a thaispeánann é agus an treoir a mhíníonn é.
description: 'Liosta seiceála d''athsheoltóir MeshCore sula dtéann sé ar dhíon nó ar chrann: cad atá le seiceáil thar USB, conas é a fheistiú, agus an tástáil sula bhfágann tú.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '5bbc2cbe'
  seeded: '2026-11-21'
  fields: {title: 'e982ea2f', lead: '664a2839', description: '01f56863'}
  sections: ['d512dacf', '4d357087', '75706984', '8a484df5', '33fd8c68']
  blocks: ['d512dacf', 'a7ba4c46', '6a427551', '2f0a8827', '2bda1638', '589c7b4f', '5fedefb7', 'e12f330e', 'd6d0b21c']
---

Is deacair teacht ar athsheoltóir ar dhíon, mar sin seiceáil é fad atá sé ar do
dheasc fós. Míníonn an [treoir athsheoltóra](/repeater-guide/) gach céim. Tagann
na luachanna, mar an réamhshocrú agus na teorainneacha léime, ó
[shocruithe do cheantair](/guides/settings/). Clóscríobh na horduithe trí USB,
mar shampla sa [chonsól sraitheach](/firmware/console/). Tá an liosta seo
bunaithe ar dhochtearraí MeshCore v1.18.0.

## Sula dtosaíonn tú {#start}

- [ ] Deir na [léarscáileanna clúdaigh](/map/) nó do [ghrúpa áitiúil](/community/)
      go bhfuil athsheoltóir de dhíth ar an gceantar. Féach
      [An bhfuil ceann de dhíth ort?](/repeater-guide/#need)
- [ ] D'aontaigh úinéir an tsuímh, agus is féidir leat teacht ar an
      athsheoltóir le haghaidh cothabhála.
- [ ] Tá an ceallra agus an painéal toisithe don mhí gheimhridh is measa. Féach
      [Toisiú cumhachta agus gréine](/repeater-guide/#power).

## Ag do dheasc, trí USB {#usb}

- [ ] Tá na dochtearraí **Repeater** ar an mbord: taispeánann `ver` a leagan. Féach
      [Socraigh é](/repeater-guide/#config).
- [ ] Ar bhord nRF52, tá `OTAFIX` san fhreagra ar `get bootloader.ver`.
      Féach [Nuashonraigh é thar an aer](/repeater-guide/#update).
- [ ] Taispeánann `get radio` réamhshocrú do cheantair.
- [ ] Taispeánann `get dutycycle` 10. Féach [Timthriall oibre](/repeater-guide/#duty-cycle).
- [ ] Ní théann `get tx` móide gnóthachan d'aeróige thar 500 mW e.r.p. Féach
      [Cumhacht: e.r.p. agus d'aeróg](/repeater-guide/#erp).
- [ ] Ní hé `password` an focal faire riaracháin a thuilleadh.
- [ ] Taispeánann `get guest.password` focal faire.
- [ ] Taispeánann `get name` an t-ainm a úsáideann do ghrúpa áitiúil dá chuid
      athsheoltóirí.
- [ ] Taispeánann `get lat` agus `get lon` suíomh an láithreáin.
- [ ] Taispeánann `get owner.info` conas a dhéanann oibreoirí eile teagmháil leat.
- [ ] Taispeánann `region` réigiúin do cheantair. Taispeánann `get flood.max.advert`
      agus `get flood.max.unscoped` teorainneacha léime an cheantair. Féach
      [Coinnigh an trácht íseal](/guides/settings/#traffic).
- [ ] Chuir tú an eochair phríobháideach ó `get prv.key` i dtaisce in áit shábháilte.
- [ ] Taispeánann `clock` an t-am atá ann anois, in UTC.
- [ ] Ar chumhacht gréine, taispeánann `powersaving` `on`.

## Ar an díon {#roof}

- [ ] Tá an aeróg ceangailte sula bhfaigheann an t-athsheoltóir cumhacht.
- [ ] Tá an aeróg ina seasamh díreach ar bharr an chrainn, i bhfad ó mhiotal. Féach
      [Feistiú](/guides/antenna/#mounting).
- [ ] Tá gach nascóir amuigh faoin aer séalaithe, agus tá lúb silte ar an gcábla.
- [ ] Tá an t-imfhálú dúnta, le poll aeraithe nó draenála. Féach
      [Crua-earraí](/repeater-guide/#hardware).

## Sula n-imíonn tú {#leave}

- [ ] Ó chian, sroicheann do chompánach an t-athsheoltóir san aip.
- [ ] Sheol tú `advert`, ionas go bhfaigheann nóid ar fud an mhogalra eolas faoin
      athsheoltóir.
- [ ] Tá a fhios ag do [ghrúpa áitiúil](/community/) go bhfuil sé ar siúl.
