---
title: Filtru tal-pakketti
lead: 'Żomm ir-repeater tiegħek milli jgħaddi l-iskart: floods minn żoni mbiegħda, bot li ma jieqaf qatt, kanal storbjuż. L-ewwel ipprova setting, imbagħad ixgħelu.'
description: 'Il-filtru tal-pakketti tal-firmware tar-repeater DMC: x’iwaqqa’, settings lesti għal repeater normali u għal wieħed mgħobbi, kull kmand tal-filtru bil-valur default tiegħu, u kif tara x’waqqa’.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'b07d39a8'
  seeded: '2026-11-02'
  fields: {title: '20a3ef1f', lead: 'd948682d', description: 'a8c57a9f'}
  sections: ['d06c9ddd', 'b1d9a8d1', '2dd3448d', 'ee64176e', 'a3cb880e', '09b568f0', 'a1a4fb68', '95fe64ae', 'dbac19c3', '05123b18', '3fa1bb28', 'e98b2285']
  blocks: ['b6231504', 'c66e4d9a', 'c0502fb4', 'fa699506', 'f7008037', '3acbb97b', '5e55d14c', 'bd024580', '68c8a4b1', '119fc5b9', '61804e40', '2fa7ebe8', '0610128b', 'a3cb880e', '0e6268be', 'e6d77222', 'f50be141', '2a1ae00c', '095e165f', 'd96efc68', 'b8a89bea', 'a29d0e87', 'c69ba7d1', 'f553d783', '1a83fda3', 'b6f87585', '64e2bbfa', 'dc79ca3a', '6ed9acff', 'd3701ccc', 'd4a25061', '22092611', '9184f977', 'f70c9e55', 'b2f0d9cb', 'c7b214c1', 'e8da9f3e', '0742c6c4', '7f2f59ae', '2789fc6d', 'ae920329', '7dd6f173', 'e1ca9ac7', 'ac11c47b', 'ec7913ae']
---

Repeater (node li jgħaddi l-messaġġi ’l quddiem) itenni kull ma jisma’.
F’mesh mgħobbija, dan jinkludi wkoll l-iskart. Bot jibgħat messaġġ kull minuta. Node wieħed jibgħat l-advert tiegħu, it-tislima li biha l-oħrajn isibuh, mill-ġdid kull ftit minuti.
Jaslu messaġġi li qasmu nofs il-pajjiż. Kull ripetizzjoni tieħu airtime mingħand kulħadd madwarek. Bil-filtru tal-pakketti, ir-repeater tiegħek iwaqqa’ dak it-traffiku minflok jgħaddih ’il quddiem. Biex l-ewwel issir taf x’qed jgħarraq il-mesh tiegħek, u x’jgħin barra l-filtru, ara
[Agħmel il-mesh reżiljenti](/guides/resilient/).

{{< callout type="warning" >}}
Il-filtru tal-pakketti huwa parti mill-**firmware tar-repeater DMC**, il-build tar-repeater ta’ [Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore). MeshCore standard m’għandux filtru tal-pakketti; għandu `region denyf *` u
`set flood.max.unscoped`, fil-paġna [Kmandi CLI](/guides/cli/). Din il-gwida ssegwi l-build dev 1.18.0 `ecfb2d4` tad-19 ta’ Ottubru 2026. Il-build stabbli 1.17.1 għandu biss il-filtri hop, rate, channel, hash u malformed. Lanqas m’għandu dry-run.
{{< /callout >}}

## X’jagħmel il-filtru {#what}

Il-filtru jħares biss lejn il-pakketti li r-repeater tiegħek jgħaddi ’l quddiem b’flooding (billi jibgħathom lil kull node fil-medda). Qatt ma jmiss dak li jibgħat ir-repeater tiegħek stess, jew pakketti li jsegwu rotta magħrufa lejn node wieħed. Jgħaddu wkoll il-messaġġi diretti u t-talbiet lejn il-kuntatti tiegħek u mingħandhom. Il-filtru jista’ jwaqqa’:

- pakketti li diġà għaddew mill-għadd massimu ta’ repeaters (hops) li tippermetti, għal kull tip ta’ pakkett;
- aktar pakketti minn tip wieħed milli tippermetti kull minuta;
- advert minn node li diġà bagħat advert fl-aħħar sigħat;
- messaġġi fuq kanal li timblokka;
- kull ma għadda minn repeater wieħed li timblokka;
- messaġġi tal-grupp minn mittent wieħed jew b’kelma waħda, jew xi wħud minnhom biss;
- messaġġi tal-grupp bil-ħsara, jew eqdem milli tippermetti.

Il-filtru jibqa’ **mitfi** sakemm tixgħelu. Tissettjah bil-kmandi. Ittajpjahom permezz ta’ USB fil-[console serjali](/firmware/console/) fuq dan is-sit. Jew ibgħathom mill-app ta’ MeshCore, kif tispjega l-[gwida tar-repeater](/repeater-guide/#config).

## Ikseb il-firmware {#firmware}

Ifflaxxja **DutchMeshCore Repeater** mill-flasher fid-[DutchMeshCore Toolbox](https://toolbox.dutchmeshcore.nl/). Il-firmware tal-observer minn [MQTT fuq l-observer tiegħek](/guides/mqtt/) għandu l-istess filtru.

## L-ewwel ipprovah {#dryrun}

Fid-dry-run, il-filtru jgħodd kull pakkett li kien iwaqqa’, imma xorta jgħaddih ’il quddiem. B’hekk taġġusta setting qabel ma jwaqqa’ xejn:

```text
filter on
filter dryrun on
```

Waqt li d-dry-run ikun mixgħul, il-linja tal-istatus ta’ `filter` tispiċċa b’`(dry-run)`. L-għadd juri x’kien iwaqqa’ l-filtru. Ħallih jaħdem għal ġurnata, imbagħad iċċekkja n-numri (ara [X’waqqa’](#stats)). Meta n-numri jidhrulek tajbin, applika l-filtru:

```text
filter dryrun off
```

## Konfigurazzjonijiet rakkomandati {#configs}

### Repeater normali {#typical}

```text
filter on
filter malformed on
filter rate 05 20 60
filter rate 02 5 60
filter hops 05 32
```

Jgħaddu sa 20 messaġġ tal-grupp kull minuta u sa 5 messaġġi diretti kull minuta, u r-repeater iwaqqa’ l-messaġġi tal-grupp bil-ħsara. Il-konfigurazzjoni normali tal-firmware stess tippermetti 20 messaġġ dirett kull minuta. Din il-paġna tuża l-5 li jirrakkomanda l-firmware minn wara flood ta’ messaġġi diretti f’Lulju 2026.

### Repeater mgħobbi {#busy}

Għal repeater f’post għoli li jisma’ reġjun sħiħ, jew għal wieħed li qed jiġi mgħarraq:

```text
filter on
filter malformed on
filter rate 05 10 60
filter rate 02 5 60
filter rate 04 5 60
filter advert 24
filter hops 05 16
filter hops 02 16
filter hops 04 8
```

Din il-konfigurazzjoni tnaqqas bin-nofs il-messaġġi tal-grupp u l-adverts, u tgħaddi l-advert ta’ kull node darba kuljum. Twaqqa’ l-messaġġi li diġà għaddew minn 16-il repeater. Wara reboot, kull node jgħaddilu advert wieħed. Id-dokumentazzjoni tal-firmware stess tissettja wkoll `filter hash 2` hawn; din il-paġna tħallih barra (ara [Is-settings kollha](#settings) għar-raġuni).

### Imblokka kanal storbjuż {#channel}

```text
filter channel add #bot
```

Ir-repeater tiegħek xorta jisma’ l-kanal. Ma jibqax jgħaddih ’il quddiem lil repeaters oħra u lill-companions (in-nodes li minnhom in-nies jibagħtu l-messaġġi). Sa 16-il kanal.

### Naqqas il-pass ta’ mittent wieħed {#sender}

Bot li jibgħat messaġġi spiss wisq fuq kanal li trid iżżomm:

```text
filter watch add #test
filter sender add Bob 60
```

Issa l-messaġġi ta’ Bob fuq il-kanal Public u fuq `#test` jgħaddu darba kull minuta; il-bqija jaqgħu. Il-filtru jqabbel l-isem li jidher fil-messaġġ, għalhekk mittent li jibdel ismu jgħaddi minnu.

### Imblokka repeater wieħed upstream {#path}

Meta l-iskart jidħol minn repeater wieħed, imblokka l-prefiss tiegħu: l-ewwel parti tal-ID tiegħu, f’eżadeċimali (hex). Għal dan għandek bżonn il-build dev 1.18; 1.17.1 m’għandux filtru tal-path.

```text
filter path add a1b2
filter path list
filter stats path
```

`filter path list` juri l-prefissi li timblokka, u `filter stats path` juri kemm waqqa’ kull wieħed. `filter path remove a1b2` jerġa’ jħallih jgħaddi.
Prefiss qasir bħal `a1` jimblokka wkoll kull repeater ieħor li l-ID tiegħu jibda b’`a1`. Uża l-itwal prefiss li tista’. Sa 8 prefissi.

## Is-settings kollha {#settings}

Kull tip ta’ pakkett għandu numru. Fuq ir-repeater, `filter types` juri l-istess numri bl-ismijiet tal-firmware, bħal `TXT_MSG` u `GRP_TXT`:

| Numru | Tip | Numru | Tip |
| --- | --- | --- | --- |
| `00` | talba | `06` | data tal-grupp |
| `01` | tweġiba | `07` | talba anonima |
| `02` | messaġġ dirett | `08` | path |
| `03` | konferma ta’ riċevuta | `09` | trace |
| `04` | advert | `10` | multipart |
| `05` | messaġġ tal-grupp | `11` | kontroll |

| Kmand | X’jagħmel | Valur tal-bidu |
| --- | --- | --- |
| `filter on` / `filter off` | Jixgħel jew jitfi l-filtru. | mitfi |
| `filter dryrun on` / `off` | Jgħodd dak li kien iwaqqa’ imma xorta jgħaddi kollox ’il quddiem. | mitfi |
| `filter hops <type> <max>` | Iwaqqa’ tip li diġà għadda minn dan l-għadd ta’ repeaters, minn 0 sa 64. | 32 għall-messaġġi tal-grupp, 8 għall-bqija |
| `filter rate <type> <limit> <secs> [soft]` | Ma jgħaddix aktar minn `limit` minn tip f’kull `secs`. B’`soft`, il-pakketti li jgħaddu jonqsu gradwalment minn `soft` sa `limit`. `0` jitfi l-limitu. | 20 kull 60 s għall-messaġġi diretti u tal-grupp, 10 għall-adverts, 5 għall-bqija |
| `filter advert <hours>` | Jgħaddi l-advert ta’ kull node darba f’dan l-għadd ta’ sigħat, sa 720. | 0 (mitfi) |
| `filter channel add <#name>` | Ma jibqax jgħaddi kanal ’il quddiem. | xejn |
| `filter path add <hex>` | Iwaqqa’ kull ma għadda minn repeater b’dan il-prefiss, minn 2 sa 8 ċifri hex. | xejn |
| `filter sender add <name> [secs] [prob]` | Iwaqqa’ messaġġi tal-grupp minn mittent, fuq Public u fuq il-kanali osservati. `Bot*` jaqbel ma’ kull isem li jibda b’Bot. | xejn |
| `filter text add <word> [secs] [prob]` | Iwaqqa’ messaġġi tal-grupp li fihom kelma, fuq Public u fuq il-kanali osservati. `^word` jaqbel biss fil-bidu. | xejn |
| `filter watch add <#name>` | Iħalli r-regoli tal-mittent u tat-test jaqraw ukoll dan il-kanal, sa 4. Public jinqara dejjem. | Public |
| `filter malformed on` / `off` | Iwaqqa’ messaġġi Public vojta, bil-ħsara jew b’data żbaljata b’aktar minn ġimgħa (il-kontroll tad-data jistenna sakemm l-arloġġ ikun issettjat). | mitfi |
| `filter age <minutes>` / `off` | Iwaqqa’ messaġġi tal-grupp eqdem minn dan iż-żmien, fuq Public u fuq il-kanali osservati, minn 1 sa 10080. | mitfi |
| `filter hash <bytes>` | Iwaqqa’ pakketti b’ID tal-path iqsar minn dan, minn 1 sa 3. | 1 |
| `filter reset` | Iġib kull setting lura għall-valur default tiegħu. | |

Kull `add` għandu `remove` u `list`, bħal `filter channel remove #bot`.
Fir-regoli tal-mittent u tat-test, `secs` iħalli jgħaddi messaġġ wieħed f’dak l-għadd ta’ sekondi. `prob` japplika r-regola għal dak is-sehem biss mill-messaġġi li jaqblu, minn 1 sa 100. Sa 8 regoli tal-mittent u 8 regoli tat-test. L-ismijiet u l-kliem jagħmlu differenza bejn ittri kbar u żgħar; isem jista’ jkun sa 15-il karattru, kelma sa 23 karattru.

Żewġ settings iwaqqgħu aktar milli tista’ tistenna:

- `filter hash 2` iwaqqa’ kważi t-traffiku kollu. In-nodes jibagħtu IDs tal-path ta’ 1 byte b’mod default.
- `filter age` jafda l-arloġġ tar-repeater tiegħek. Issettjah b’`clock sync` mill-app, iċċekkjah b’`clock`, u ibda b’valur ġeneruż: `filter age 60`.

Kull setting jinżamm wara reboot.

## X’waqqa’ {#stats}

`filter` juri t-totali għal kull raġuni:

```text
> Filter on: Blocked [ Hops: 3 | Rate: 12 | Channel: 1 | Hash: 0 | Malformed: 2 ]
```

`filter stats <topic>` juri d-dettalji ta’ setting wieħed. It-topics huma `hops`, `rate`, `channel`, `hash`, `malformed`, `advert`, `path`, `sender`, `text` u `age`. `filter stats top` juri l-ewwel byte tal-IDs tan-nodes li kkawżaw l-aktar pakketti mwaqqgħin. Ħafna nodes għandhom l-istess byte.
`filter stats air` juri l-airtime li r-repeater tiegħek iffranka billi ma għaddiex dawn il-pakketti ’l quddiem.

Il-counters jerġgħu jibdew minn 0 wara reboot u wara `clear stats`.
