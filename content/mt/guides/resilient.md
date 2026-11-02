---
title: Agħmel il-mesh aktar reżiljenti
lead: Il-mesh ta' madwarek bil-mod jew mimli żibel? Sib il-kawża, ixgħel is-setting tar-repeater li jwaqqfu, u għid lill-grupp lokali tiegħek.
description: 'Għargħar u spam fuq mesh ta'' MeshCore: kif tagħraf kull tip, liema setting tar-repeater jgħin, kif tara għargħar u kif issib is-sors tiegħu.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '500188ff'
  seeded: '2026-11-02'
  fields: {title: '33ec7ac8', lead: '780da19b', description: '1826e5e8'}
  sections: ['68ca5d36', '133c764a', 'a3bb5172', 'f4cc9cad', 'ace7b1ee', '89651002', 'f4dfdf59', '764c832c', 'f342b64b', 'f348e208']
  blocks: ['68ca5d36', 'c9cfbe6c', 'bcb31992', 'de7f60e4', 'e862fb9b', '0046b51f', '25f34d1d', 'c3c3ea52', '853a0f1d', '2bcea703', '871a7661', '2690aacf', 'a4aec3a1', 'd6da27c6', 'e8405458', 'f9150ee6', '8508ce40', '4b03ccd5', 'fb79c493', '695adde7', 'eba5a5b5', '836e0bac', '3497c5e8', '71c78fa1', '537d0930', '6a315252', '7c84dc56', '682e08e6', '258d7a27', '53af1400', '0dbebf97', 'ac0dca3c', '70fb4e9a', '9f055f50', 'ae90facc']
---

Il-messaġġi jaslu tard jew ma jaslux? Public jimtela biż-żibel? Dak huwa għargħar:
aktar traffiku milli jiflaħ il-mesh, mibgħut bi żball jew apposta. Fittex dak li
qed tara fit-tabelli t'hawn taħt. F'kull ringiela ssib is-setting li jwaqqfu.
Ixgħlu fuq ir-repeater tiegħek, in-nodu li jgħaddi l-messaġġi 'l quddiem. Imbagħad għid lill-[grupp
lokali](/community/) tiegħek, biex ir-repeaters ta' madwarek jagħmlu l-istess. Kull
repeater li jarmi għargħar iħalli airtime għal kulħadd.

## Għargħar bi żball {#mistake}

Għargħar bi żball ġej minn nodu li sidu ma jafx li qed jikkawżah. Jieqaf ladarba
s-sid isir jaf. Fit-tabelli t'hawn taħt, advert huwa s-sliem li jibgħat nodu biex
oħrajn isibuh.

Is-settings fit-tabelli ġejjin minn dak li jagħmel il-firmware. Mhux kollha waqqfu
għargħar fuq mesh reali s'issa.

{{< callout type="warning" >}}
Xi settings f'din il-paġna jeħtieġu l-firmware DMC. **MeshCore** 1.18.0 standard
għandu r-reġjuni, il-limiti tal-hops `flood.max.*`, l-iskoperta tal-loops u d-duty
cycle. Il-filtru tal-pakketti, ir-regoli li jħallu r-repeater tiegħek jarmi ż-żibel,
jiġi mal-**firmware DMC** ta'
[Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore). L-istess jgħodd għad-duty-cycle
gating u l-filtru tal-companion. Din il-paġna ssegwi d-dev build DMC 1.18.0
`ecfb2d4` tad-19 ta' Ottubru 2026. Il-paġna tal-[filtru tal-pakketti](/guides/filter/#firmware)
tgħidlek minn fejn iġġibu.
{{< /callout >}}

| Dak li tara | X'inhu | X'jgħin |
| --- | --- | --- |
| Talbiet lir-repeaters minn nodu wieħed, lejl u nhar, u mesh li jibqa' bil-mod għal jiem | Sistema ta' home automation jew bot li jitlob l-istatus tar-repeaters ta' spiss wisq | `filter on`. Imbagħad il-filtru tal-pakketti jħalli jgħaddu 5 talbiet kull minuta. Għid lis-sid. |
| L-istess tip ta' messaġġ fuq kanal, kull minuta | Bot li jibgħat messaġġi ta' spiss wisq | [Imblokka l-kanal](/guides/filter/#channel) jew [naqqas il-pass tal-mittent](/guides/filter/#sender). Għid lis-sid. |
| Messaġġi li ma jinqrawx fuq Public u kanali oħra | Nodu b'firmware difettuż jew b'settings tar-radju ħżiena | `filter malformed on` jarmihom fuq Public. Għid lis-sid. |
| L-advert ta' nodu wieħed kull ftit minuti | Nodu ssettjat biex jibgħat adverts ta' spiss wisq | `filter advert 24` iħalli jgħaddi advert wieħed kuljum minn kull nodu. `set flood.max.advert 3` iżomm l-adverts fi ħdan 3 hops. |
| Messaġġi minn 'il bogħod, b'reġjuni li ma jappartjenux hawn | Bridge li jgħaqqad meshes permezz tal-internet | `set flood.max.unscoped 1`, u poġġi r-repeater tiegħek biss fir-[reġjuni li jservi](/guides/settings/#traffic). |
| L-istess messaġġ jgħaddi kemm-il darba, bl-ID tar-repeater tiegħek fir-rotta aktar minn darba | Repeater li jibdel il-pakketti u jgħaddihom 'il quddiem, u għalhekk jidħlu f'loop | L-iskoperta tal-loops taħdem fuq `minimal` b'mod awtomatiku. `set loop.detect moderate` jarmi loop aktar kmieni. |

## Għargħar apposta {#purpose}

Xi għargħar huwa spam: żibel mibgħut apposta biex jintasab il-mesh. Il-mittent
ibiddel l-ismijiet, iċ-ċwievet u r-rotot, għalhekk l-ebda regola waħda ma twaqqaf
l-għargħar.

| Dak li tara | X'inhu | X'jgħin |
| --- | --- | --- |
| Ħafna nodi ġodda b'ismijiet każwali, kull wieħed b'ċavetta ġdida | Adverts foloz | `filter rate 04 5 60` iħalli jgħaddu 5 adverts kull minuta. `filter advert` ma jgħinx: kull advert ġej minn [ċavetta ġdida](#forged). |
| Messaġġi b'test li ma jinqrax minn mittenti ivvintati, ħafna drabi b'data ta' aktar minn sena ilu | Spam fuq il-kanali | `filter malformed on` jarmihom fuq Public. `filter age 60` jarmi dawk b'data qadima fuq Public u fuq il-[kanali osservati](/guides/filter/#settings). |
| Sa 200 messaġġ dirett kull minuta lil nodi li ma jeżistux, bl-ebda konferma lura | Għargħar ta' messaġġi diretti | `filter rate 02 5 60`. L-app tiegħek ma turikx dawn il-messaġġi, iżda observer jurihom. |
| Mewġat ta' talbiet minn nodu wieħed lil għexieren ta' oħrajn | Spam ta' talbiet | B'`filter on`, il-filtru tal-pakketti jħalli jgħaddu 5 talbiet kull minuta. |
| Messaġġ jerġa' lura 10 sa 20 minuta wara, bi kważi l-istess rotta | Replay: kopja mibgħuta mill-ġdid | Repeater jiftakar l-aħħar 160 pakkett li ra, għalhekk fuq mesh mgħobbi kopja aktar tard terġa' tgħaddi. `filter age` jarmi messaġġ ta' grupp eqdem milli tħalli int. |
| Messaġġi minn Public mibgħuta mill-ġdid taħt mittent ivvintat, xi drabi b'data qadima | Echo spam | `filter age 60`. `filter malformed on` jarmi wkoll data żbaljata b'aktar minn ġimgħa. |
| Messaġġ kull ftit sekondi fuq diversi kanali, kull wieħed minn isem ġdid, b'domandi ordinarji | Mewġa ta' bots | `filter rate 05 10 60`, u [imblokka l-kanali](/guides/filter/#channel) li ż-żona tiegħek ma tużax. Kull isem huwa ġdid, għalhekk ir-[regoli tal-mittent](#forged) ma jaqbduhx. |

## X'ħadem {#worked}

Il-gruppi lokali waqqfu l-għargħar b'dawn il-passi:

1. **Għid lis-sid.** Għargħar bi żball jieqaf ladarba sidu jsir jaf. Ibagħtlu messaġġ
   ħbiberuż.
2. **Tirreaġixxix fuq il-mesh.** Tweġiba turi lill-ispammer li l-ispam qed jaħdem.
3. **Itlob li jkun hemm observers.** Observer huwa nodu li jirrapporta kull pakkett li jisma'
   permezz ta' MQTT. Aktar ma jkollok observers madwarek, aktar malajr tara minn fejn
   jidħol l-għargħar. Biddel ir-repeater tiegħek f'observer b'[MQTT fuq l-observer tiegħek](/guides/mqtt/).
4. **Sib is-sors.** L-observers juru f'liema żona jinsab il-mittent. L-aħħar kilometru
   jeħtieġ nies bil-mixi b'radju. Ara [Sib is-sors](#source).
5. **Qanqal il-grupp lokali tiegħek.** Repeater wieħed bis-settings it-tajbin jgħin.
   Ir-repeaters kollha taż-żona flimkien iwaqqfu l-għargħar. Il-[grupp lokali](/community/)
   tiegħek iwassal lil kull sid biex jixgħel is-setting.

## Mittenti u rotot ivvintati {#forged}

Il-mittent jikteb dawn il-partijiet ta' pakkett, u xejn ma jiċċekkjahom:

- **L-isem tal-mittent.** F'messaġġ fuq kanal, l-isem huwa parti mit-test. Kull min
  għandu ċ-ċavetta tal-kanal jista' jikteb kwalunkwe isem.
- **Il-bidu tar-rotta.** Kull repeater iżid l-ID tiegħu fl-aħħar tar-rotta. Xejn ma
  jiċċekkja l-IDs li kienu hemm qabel, għalhekk mittent jista' jibda r-rotta b'IDs
  ivvintati. It-tmiem tar-rotta huwa reali.

{{< forged-path >}}

Għalhekk `filter sender` u `filter path` iwaqqfu mittent biss sakemm ibiddel ismu
jew ir-rotta tiegħu. [Blokk tar-rotta](/guides/filter/#path) jarmi wkoll it-traffiku
reali tar-repeater li l-ID tiegħu jinsab fih. Il-limiti tar-rata, il-limiti tal-hops,
il-kontrolli tal-età u ta' malformed, il-blokki tal-kanali, ir-reġjuni u d-duty cycle
jibqgħu jaħdmu.

## Settings għal kull għargħar {#always}

Dawn jibqgħu jgħoddu, ikun x'ikun l-għargħar fuq il-mesh:

- **Duty cycle ta' 10%.** B'hekk ir-repeater tiegħek qatt ma jittrasmetti aktar milli
  tippermetti l-liġi, ikun x'ikun li jidħol. Il-[gwida tar-repeater](/repeater-guide/#duty-cycle)
  tispjega dan.
- **Reġjuni u limiti tal-hops.** Reġjun huwa ż-żona li fiha jibqa' messaġġ. Repeater
  jgħaddi biss messaġġi fir-reġjuni li għandu, u `flood.max.*` iżomm it-traffiku qrib.
  It-tnejn tsibhom f'[Naqqas it-traffiku](/guides/settings/#traffic).
- **Il-filtru tal-pakketti għal repeater mgħobbi.** Is-[settings lesti](/guides/filter/#busy)
  inaqqsu bin-nofs il-messaġġi ta' grupp u l-adverts. Ipprovahom l-ewwel f'[dry-run](/guides/filter/#dryrun):
  dan jgħodd biss dak li kien jarmi.
- **Il-filtru tal-companion, fil-firmware DMC.** Il-companion tiegħek, in-nodu li
  minnu tibgħat il-messaġġi, iżomm iż-żibel 'il barra mill-app tiegħek. Jaħbi messaġġi
  difettużi u qodma, u messaġġi minn repeater, mittent jew kelma li timblokka. Regola
  ta' mittent jew ta' kelma taħbi l-messaġġ minnek biss. Oħrajn xorta jirċevuh.

### Duty-cycle gating {#gate}

Fil-firmware DMC, ir-repeater tiegħek jista' jagħti prijorità lir-reġjun tiegħu meta
jkun mgħobbi. Ladarba jkun ittrasmetta aktar minn 35% tal-aħħar minuta, jieqaf jgħaddi
messaġġi mingħajr reġjun. Jekk jibqa' mgħobbi, imbagħad jarmi l-usa' reġjun, livell
wieħed kull darba. Ir-reġjun tiegħu dejjem jgħaddi. Dan jaħdem biss jekk ikollok reġjuni
ssettjati fuq ir-repeater tiegħek. Ixgħlu u ċċekkjah:

```text
set dc.gate on
get dc.gate.status
```

{{< dc-gate >}}

Dak li jarmi ma jidhirx f'`filter stats`. Meta r-repeater jerġa' jikkalma, ir-reġjuni
jerġgħu lura, l-aktar ta' ġewwa l-ewwel.

## Kif tara għargħar {#see}

L-app tiegħek turi biss dak li jasal għandek. Observer biss jisma' għargħar ta' messaġġi
diretti lil nodi li ma jeżistux. Kull observer jirrapporta lill-[MeshCore Analyzer](https://meshcore-analyzer.eu/),
fejn kulħadd jista' jarah. Biddel ir-repeater tiegħek f'observer b'[MQTT fuq l-observer tiegħek](/guides/mqtt/).

Fuq l-Analyzer, ħares lejn kull kopja ta' pakkett wieħed. Ir-rotta tiegħu ġeneralment
turi minn fejn ġie. Min jibgħat l-għargħar jista' jibda r-rotta b'[IDs ivvintati](#forged),
għalhekk l-ewwel IDs ma jgħidulek xejn. Iżda kull kopja ġġorr l-istess bidu ivvintat.
Il-kopja bl-iqsar rotta għaddiet mill-inqas repeaters reali, għalhekk instemgħet l-eqreb
lejn il-mittent.

{{< copies >}}

Fuq ir-repeater tiegħek, `filter stats` juri x'rema l-filtru tal-pakketti. `filter stats top`
juri l-ewwel byte tal-IDs tan-nodi li minnhom ġejjin l-aktar pakketti mormija. Ħafna
nodi għandhom l-istess byte, għalhekk idejjaq it-tfittxija iżda ma jsemmix il-mittent.

## Sib is-sors {#source}

Meta għargħar jibqa' jerġa' lura:

1. **Segwi r-rotot.** Aqra rotta mit-tmiem: l-aħħar IDs huma r-repeaters li minnhom
   għadda l-għargħar. L-ewwel wieħed reali jinsab qrib is-sors. L-IDs ta' qablu jistgħu
   jkunu [ivvintati](#forged).
2. **Dejjaq iż-żona.** Diversi observers li jisimgħu l-istess pakkett juru f'liema żona
   jinsab il-mittent. Id-[DMC Triangulator](https://triangulator.dutchmeshcore.nl/) jikkalkulaha
   mir-repeaters li semgħuh.
3. **Imxi l-aħħar kilometru.** Ir-repeaters jisimgħu s-sors biss fit-tarf tal-firxa
   tagħhom, għalhekk għall-aħħar parti n-nies iridu jimxu. [Mesh-Hunter](https://mesh-hunter.eu/)
   jitqabbad mal-companion tiegħek u jirreġistra kull pakkett li jisma' mal-pożizzjoni
   GPS tiegħek. Diversi nies li jimxu fl-istess ħin isibuh aktar malajr.
4. **Għid lill-[grupp lokali](/community/) tiegħek.** Huma jaraw aktar mill-mesh,
   jiddeċiedu x'jiġri wara, u jikkuntattjaw lil min jibgħat għargħar apposta.

## Żid dak li rajt {#add}

Laqtek għargħar li mhux f'dawn it-tabelli? Xi setting waqqaf wieħed? Għidilna fuq
[Discord](https://discord.meshcore-info.eu/): x'rajt u x'xegħelt. Aħna nżiduh fil-paġna.
