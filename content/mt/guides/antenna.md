---
title: Gwida għall-antenni
lead: L-antenna t-tajba, immuntata sew, tasal iktar 'il bogħod milli tasal b'iktar qawwa. Iċċekkja l-antenna fuq il-companion tiegħek, imbagħad agħżel, qabbad u immonta waħda għal repeater.
description: 'Agħżel u immonta antenna ta'' MeshCore għal 868 MHz: iċċekkja whip ta'' companion, tipi ta'' antenni u gain, konnetturi, telf tal-kejbil kull metru, filtri, immuntar u kif il-gain jgħodd għal-limitu legali.'
eyebrow: Companion u repeater · 868 MHz
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'f828c4aa'
  seeded: '2026-11-02'
  fields: {title: '3a76cb0e', lead: 'd82ec429', description: 'ce3f3e73', eyebrow: 'd2203a35'}
  sections: ['908e2678', 'f9b96f42', 'ca18da90', 'bcfb40ec', '851afd23', '8b7a2209', 'd8832cfa', '5b70b9e8', '14a38e92', 'a5dc1e34', 'de04ca41', 'a23f19c6', '93846db4']
  blocks: ['908e2678', '0868bca9', '081db416', 'ad1da217', '73844333', 'aa14f1b1', '07e4fbad', '32d64d0d', 'ef66133c', '558c115b', '5d28e314', '57d6e138', 'e9b3d055', 'dd757d4a', '2cbd0b58', '21c67ec0', '306a3ded', 'fa46c89f', '1e6ccb3a', 'a3e53320', '6ae131c0', '98f350c6', '138d049d', '3bd28746', '2fc98ff1', '5ea29ee5', 'cfbd64e1', '48833347', '56a82a5c', '4ef7e883', '711e4fee', '1f7844ed', '6b188411', '8da9aa78', '4c2d8bbc', 'a721a9d0', '69c1dc1a', 'a631dbfa', '3f9f3471', '5af4ae3b', 'fa5095fd', '65eeb436', '15aa0eca', 'a8f5b505', '57f35115', '8e5e4975', '89764d3d']
---

L-għoli, antenna sintonizzata u kejbil qasir iżidulek il-firxa iktar minn kull milliwatt żejjed. Din il-gwida tibda bil-companion, ir-radju li minnu tibgħat il-messaġġi. Imbagħad titkellem dwar l-antenna fuq repeater, node li jgħaddi l-messaġġi minn fuq bejt jew arblu.

## Il-companion tiegħek {#companion}

{{< callout type="warning" >}}
Waħħal l-antenna qabel ma tixgħel ir-radju. Radju LoRa li jittrasmetti mingħajr antenna jista' jagħmel ħsara liċ-ċippa tiegħu.
{{< /callout >}}

L-antenna li ġiet mal-bord tiegħek hija biżżejjed. Waħħalha, żomm in-node wieqaf u ibda ibgħat il-messaġġi. Antenna aħjar fuq companion ftit iżżidlek; repeater fil-firxa tiegħek iżidlek ħafna.

Ixtri whip separat biss meta dak li ġie mal-bord ikun imkisser jew nieqes. Mhux kull whip li jinbiegħ għal 868 MHz huwa sintonizzat għal din il-frekwenza. [Iċċekkjah b'NanoVNA](#nanovna), analizzatur tal-antenni daqs il-but, qabel ma tafdah, jew issellef wieħed minn bord li jaħdem.

Node ħdejn trasmettitur qawwi jisma' inqas milli suppost. [Filtru SAW (surface acoustic wave)](#filters) żgħir bejn ir-radju u l-antenna jżomm lil dak it-trasmettitur barra mir-riċevitur. L-ewwel iċċekkja d-datasheet tiegħu:

- **Qawwa massima fid-dħul.** It-trasmissjoni tiegħek stess ukoll tgħaddi mill-filtru. Bord li jittrasmetti 22 dBm (160 mW) f'filtru klassifikat għal 15 dBm jkisser il-filtru.
- **Passband.** Irid jinkludi l-frekwenza tal-preset tiegħek. Filtru għal 868.65 sa 869.25 MHz ma jgħaddix il-kanal EU/UK (Narrow) fuq 869.618 MHz.

## Tipi ta' antenni għal repeater {#types}

Kull antenna fuq il-mesh tkun wieqfa. Agħżel it-tip skont fejn jinsabu n-nodes li trid tilħaq:

- **Collinear tal-fibreglass.** Tubu abjad fuq arblu, b'gain fuq l-orizzont kollu madwaru. Din hija l-għażla standard għal repeater li jservi belt.
- **Dipole.** Iqsar, b'inqas gain u raġġ għoli. Jilħaq nodes taħtek u fuqek aħjar minn collinear, pereżempju minn fuq għolja li tagħti għal wied.
- **Yagi.** Virga b'elementi trasversali, immirata lejn post wieħed. Tilħaq repeater wieħed 'il bogħod u ftit li xejn iktar. Immuntaha bl-elementi weqfin, għax il-polarizzazzjoni tagħha ssegwi l-elementi.

## Il-gain u r-raġġ {#gain}

Il-gain ma jżidx il-qawwa. Jieħu s-sinjal li kien imur 'il fuq u 'l isfel u jibagħtu tul l-orizzont. Bħal torċ li tiffoka: l-istess batterija, raġġ itwal u idjaq. Dipole u collinear tal-istess manifattur juru dan:

| Antenna | Gain | Wisa' vertikali tar-raġġ |
|---|---|---|
| Dipole (Sirio SO 868-915-2) | 2.2 dBi | 88 grad |
| Collinear tal-fibreglass (Sirio SPO 868-915-6) | 5.8 dBi | 23 grad |

{{< gain >}}

Id-dijagramma taqta' mill-arblu, kif jidher mill-ġenb. Dawwarha madwar l-arblu u jkollok ir-raġġ kollu: doughnut għad-dipole, diska ċatta għall-collinear. Antenna wieqfa tibgħat bl-istess mod f'kull direzzjoni madwarha. Barra mir-raġġ imfassal is-sinjal ma jieqafx; ikun iktar dgħajjef, imma xorta biżżejjed għal node fil-qrib.

Fuq bejt, trid raġġ ċatt. Fuq għolja ferm 'il fuq min-nodes, raġġ ta' 23 grad jgħaddi minn fuq rashom; dipole jkoprihom. Yagi tmur iktar 'il bogħod minn hekk: 16.6 dBi f'raġġ għoli 23 grad u wiesa' 25 grad (Amphenol Procom 7176870), u xejn lejn il-ġnub.

Il-gain jitkejjel meta mqabbel ma' referenza. dBi jqabbel ma' antenna ideali li tibgħat indaqs f'kull direzzjoni. dBd iqabbel ma' dipole ta' nofs mewġa, li għandu 2.15 dBi hu stess: anki l-iktar antenna sempliċi ma tibgħat xejn dritt 'il fuq jew 'l isfel. Dipole itwal, ta' 1.25 tul ta' mewġa, jilħaq 5.2 dBi. Collinear minflok ipoġġi elementi ta' nofs mewġa wieħed fuq l-ieħor: iktar ma jpoġġi, iktar jogħla l-gain. Agħfas l-istess sinjal f'nofs l-ispazju u hemmhekk ikun darbtejn iktar qawwi: 3 dB. Agħfsu f'kwart, u jkun 4 darbi iktar qawwi: 6 dB. Il-manifatturi jagħtu l-gain f'dBi; il-limitu legali jgħodd f'dBd, ara [Fi ħdan il-limitu legali](#legal).

### Liema gain għall-post tiegħek {#choose-gain}

- **Għoljiet, widien jew belt iffullata: madwar 3 dBi.** Ir-raġġ għoli jilħaq nodes fuqek u taħtek, u jdur max-xaqlibiet u l-binjiet li jkunu fit-triq. Jaħdem ukoll bil-maqlub: minn wied, raġġ ċatt jgħaddi minn taħt repeater fuq l-għolja ta' fuqek. Eżempju huwa r-RAKwireless RAKARG12: tubu tal-fibreglass ta' 36 cm.
- **Subborgi jew belt bi btieħi baxxi: 5 sa 6 dBi.** Il-collinear standard tal-fibreglass.
- **Art ċatta u miftuħa: 8 sa 10 dBi.** Ir-raġġ l-iktar ċatt jasal l-iktar 'il bogħod tul l-orizzont. Immuntat għoli, jgħaddi minn fuq in-nodes fil-qrib.

Il-gain fl-isem huwa l-aħjar ċifra fuq il-banda kollha tal-antenna. Ir-RAKARG12, li jinbiegħ bħala 3 dBi, għandu 2.8 dBi bejn 865 u 870 MHz. Fid-datasheet, aqra t-tabella tal-gain għall-frekwenza tal-preset tiegħek.

'Il fuq minn 7 dBi, bord ta' 22 dBm jaqbeż il-limitu legali, sakemm it-telf tal-kejbil u tal-filtru ma jpattix għad-differenza. Baxxi l-qawwa tat-trasmissjoni biex taqbel.

Gain għoli jgħin biss meta taf fejn jinsabu n-nodes: tul l-orizzont madwar repeater, jew f'repeater wieħed 'il bogħod għal Yagi. Companion f'idejk jippunta f'kull direzzjoni, għalhekk il-gain baxx li ġie miegħu huwa l-aħjar għalih.

## Għaliex vertikali {#vertical}

L-antenni jisimgħu lil xulxin l-aħjar meta jippuntaw fl-istess direzzjoni. It-telf jikber mal-angolu ta' bejniethom: 45 grad jiswewk 3 dB, nofs is-sinjal tiegħek. F'90 grad, antenna mimduda u oħra wieqfa, fit-teorija ma jasal xejn. Il-mesh tkun wieqfa, għalhekk l-antenna tiegħek ukoll trid tkun wieqfa. Dan jgħodd ukoll għal companion fuq skrivanija: jekk timduh, kull node madwarek jisma' inqas.

## Konnetturi {#connectors}

Ordna l-antenna bil-konnettur li għandu l-bord tiegħek. Kull adapter ifisser ġonta oħra x'tissiġilla u iktar sinjal mitluf.

- **SMA.** Konnettur bil-kamin wiesa' madwar 6 mm. Is-sokit fuq il-biċċa l-kbira tal-bordijiet għandu toqba fiċ-ċentru; l-antenna għandha l-pin. Konnettur ta' dan it-tip jitlef madwar 0.03 dB f'868 MHz.
- **RP-SMA.** L-istess korp u kamin bħal SMA, bil-pin u t-toqba mbiddlin. Jidher bħal SMA u ma jeqbilx miegħu. Iċċekkja liema wieħed għandu l-bord tiegħek qabel ma tordna.
- **U.FL (IPEX).** Sokit ċkejken li jidħol bl-imbuttar, fuq il-bord innifsu. Kejbil pigtail qasir jgħaddi minnu sa sokit SMA fil-kaxxa. Huwa klassifikat għal 30 ċiklu ta' konnessjoni, għalhekk qabbdu darba u ħallih.
- **N.** Il-konnettur il-kbir bil-kamin fuq antenni tal-fibreglass u kejbil oħxon. Jitlef l-iktar 0.05 dB. Repeater jeħtieġ adapter jew pigtail wieħed minn N għall-SMA tal-bord.

## Telf tal-kejbil {#cable}

Il-kejbil jiswik sinjal qabel ma s-sinjal jitlaq mill-antenna, fiż-żewġ direzzjonijiet. 3 dB huma nofs il-qawwa tiegħek. Iċ-ċifri tal-manifatturi kull metru, bejn 868 u 900 MHz:

| Kejbil | Telf kull metru | Telf fuq 5 m |
|---|---|---|
| RG174 | 1.02 dB | 5.1 dB |
| RG316 | 0.78 dB | 3.9 dB |
| RG58 | 0.45 dB | 2.2 dB |
| H-155 | 0.27 dB | 1.4 dB |
| LMR-240 | 0.25 dB | 1.2 dB |
| Ecoflex 10 | 0.13 dB | 0.7 dB |
| LMR-400 | 0.13 dB | 0.6 dB |

3 metri ta' RG174, il-pigtail irqiq li jiġi ma' ħafna bordijiet, jitilfu nofs il-qawwa tiegħek. Immunta l-bord ħdejn l-antenna b'pigtail qasir, jew għaddi kejbil oħxon sa għandha. Żid mas-somma kull adapter u filtru fit-triq.

## Filtri {#filters}

Filtru jkun bejn ir-radju u l-antenna. Jgħaddi l-banda tiegħek u jimblokka l-bqija, biex trasmettitur qawwi fil-qrib ma jgħarraqx ir-riċevitur. Teħtieġ wieħed meta node jisma' inqas milli suppost ħdejn trasmettituri oħra. Repeater fuq arblu ma' stazzjonijiet bażi tat-telefonija ċellulari huwa node bħal dan. Filtru jiswik sinjal fiż-żewġ direzzjonijiet: għodd it-telf tiegħu bħal dak tal-kejbil.

| | Filtru SAW | Filtru cavity |
|---|---|---|
| Daqs | Ftit millimetri, fuq bord żgħir | Blokka jew tubu tal-metall |
| Telf ta' wieħed tajjeb | inqas minn 2 dB | inqas minn 1 dB |
| Qawwa massima fid-dħul ta' wieħed tajjeb | 500 mW | diversi watts |

Is-sysmocom cf866.5-kt30, pereżempju, huwa filtru cavity għal 863 sa 870 MHz li jitlef l-iktar 1.0 dB u jiflaħ 30 W. Huwa magħmul għal ġewwa, għalhekk poġġih f'kaxxa ssiġillata fuq arblu.

Il-filtri jvarjaw ħafna, għalhekk iċċekkja d-datasheet qabel ma tixtri. Il-qawwa ta' dħul klassifikata trid taqbeż il-qawwa tat-trasmissjoni tiegħek, u l-passband irid jinkludi l-frekwenza tal-preset tiegħek.

## Immuntar {#mounting}

- **'Il fuq mit-tarf tal-bejt.** L-antenna teħtieġ veduta ċara f'kull direzzjoni li sservi. Anki ftit metri 'l fuq mill-btieħi ta' madwar jgħinu. [Agħżel post](/repeater-guide/#site) fil-gwida tar-repeater turik kif tiċċekkja l-veduta.
- **'Il bogħod mill-metall.** Kanali tal-ilma, arbli, antenni oħra u btieħi tal-metall ħdejn l-antenna jibdlu x-xejra u s-sintonizzazzjoni tagħha. Immuntaha fuq ras l-arblu, mhux ħdejh.
- **Wieqfa.** Uża livell; ara [Għaliex vertikali](#vertical).
- **Ċirku tat-taqtir.** Ħalli l-kejbil jiddendel taħt il-konnettur qabel ma jitla' jew jidħol. Hekk l-ilma jqattar minflok ma jidħol fil-ġonta.
- **Issiġilla kull konnettur ta' barra.** L-ilma f'konnettur iżid it-telf u jsaddad il-pin. Issiġillah kontra x-xita u ċċekkja s-siġill kull sena.
- **Sajjetti.** Antenna fuq bejt hija mira. Arrestor tal-iskariku tal-gass fil-kejbil jiskatta f'każ ta' żieda f'daqqa fil-vultaġġ u jibagħtha lejn l-art. Segwi [Hardware](/repeater-guide/#hardware) fil-gwida tar-repeater u r-regoli lokali tiegħek dwar l-ertjar.

## Fi ħdan il-limitu legali {#legal}

{{< callout type="legal" verified="2026-10-22" >}}
Fl-Ewropa MeshCore juża s-sottobanda 869.40-869.65 MHz, b'massimu ta' **500 mW** ta' qawwa radjata effettiva (e.r.p.). Il-limitu jqis dak li joħroġ mill-antenna: il-gain tal-antenna jiżdied, it-telf tal-kejbil u tal-filtru jitnaqqas. Gain f'dBi jgħodd 2.15 dB inqas, għax il-limitu jitkejjel meta mqabbel ma' dipole.
{{< /callout >}}

Collinear ta' 5.8 dBi fuq bord ta' 22 dBm jibqa' fi ħdan il-limitu. L-istess antenna fuq bord b'amplifikatur taqbeż il-limitu, sakemm ma tbaxxix il-qawwa tat-trasmissjoni. Fil-gwida tar-repeater, [Qawwa: e.r.p. u l-antenna tiegħek](/repeater-guide/#erp) fiha s-somma u 2 eżempji maħduma.

## Iċċekkja antenna b'NanoVNA {#nanovna}

NanoVNA huwa analizzatur vettorjali tan-netwerk daqs il-but. Juri għal liema frekwenza hija sintonizzata antenna, biex tkun taf qabel ma timmuntaha. In-NanoVNA-H ikejjel sa 1.5 GHz, li jkopri 868 MHz.

1. Ikkalibrah għal 800 sa 950 MHz bil-biċċiet open, short u load mis-sett tiegħu.
2. Qabbad l-antenna permezz tal-adapter li se tuża fuq in-node. Żommha wieqfa u 'l bogħod minn ġismek u mill-mejda.
3. Aqra l-kurva SWR (standing wave ratio): turi kemm sinjal l-antenna tibgħat lura. L-inżul irid ikun fuq il-frekwenza tal-preset tiegħek, 869.618 MHz għal EU/UK (Narrow). Inżul mijiet ta' MHz 'il bogħod ifisser li l-antenna hija magħmula għal banda oħra.

Kwart ta' mewġa f'868 MHz huwa 86 mm (it-tul tal-mewġa huwa 345 mm). It-tul waħdu ma jgħidlekx il-banda, għax il-manifatturi jitwu u jgħabbu l-whips; in-NanoVNA jgħidlek.

## Sorsi {#sources}

- Telf tal-kejbil: [Belden 8216 (RG174)](https://catalog.belden.com/techdata/en/8216_techdata.pdf), id-datasheet Huber+Suhner RG316, [Belden 8240 (RG58)](https://catalog.belden.com/techdata/en/8240_techdata.pdf), [SSB H-155](https://www.ssb.de/media/h155ssb-en.pdf), id-datasheets Times Microwave LMR-240 u LMR-400, [SSB Ecoflex 10](https://www.rigpix.com/otherusefulinfo/coax/ecoflex10.pdf).
- Antenni: [Sirio SPO 868-915-6](https://rigpix.com/antennas/sirio_spo8689156_manual.pdf), id-datasheet Sirio SO 868-915-2, [Amphenol Procom 7176870](https://amphenolprocom.com/products/base-station-antennas/2236-7176870), [RAKwireless RAKARG12](https://docs.rakwireless.com/product-categories/accessories/rakarg12/datasheet/).
- Il-gain bħala sinjal magħfus f'inqas spazju: [RF Cafe, introduzzjoni għall-antenni](https://www.rfcafe.com/references/electrical/ew-radar-handbook/antenna-introduction-basics.htm).
- Konnetturi: id-datasheets Rosenberger 32S102 (SMA) u 53S101 (N), il-katalgu Hirose U.FL.
- Filtri: il-paġna tal-prodott sysmocom cf866.5-kt30, [arrestors tal-iskariku tal-gass Citel](https://citel.us/en/gas-tube-surge-arrestors-for-coaxial-line-protection).
- Telf tal-polarizzazzjoni: [University of Toronto, effetti Friis](https://www.waves.utoronto.ca/prof/svhum/ece422/notes/12-friiseffects.pdf).
- Gain tad-dipole skont it-tul: [Wikipedia, Dipole antenna](https://en.wikipedia.org/wiki/Dipole_antenna).
- Tul tal-mewġa: il-veloċità tad-dawl minn [NIST](https://physics.nist.gov/cgi-bin/cuu/Value?c).
- NanoVNA: [NanoVNA-H](https://github.com/hugen79/NanoVNA-H).
- Limitu legali: [CEPT ERC Recommendation 70-03](https://docdb.cept.org/document/845), Anness 1, banda h1.7; il-[gwida tar-repeater](/repeater-guide/#legal) telenka l-bqija.
