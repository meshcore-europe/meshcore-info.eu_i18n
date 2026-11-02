---
title: Ibda
lead: Minn bord ġdid sal-ewwel messaġġ tiegħek fuq il-mesh. Għandek bżonn bord LoRa, kompjuter b'Chrome jew Edge, u mowbajl jew laptop għall-app.
description: Agħmel flash ta' MeshCore mill-browser, qabbad l-app, agħżel il-preset tar-radju taż-żona tiegħek, ibgħat l-ewwel messaġġ u ingħaqad mal-kanal lokali.
eyebrow: 6 passi · MeshCore v1.18.0
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'f97ca1b9'
  seeded: '2026-11-02'
  fields: {title: '61e8d44a', lead: '45b0e5c3', description: 'cf031b18', eyebrow: '4fa6fe1e'}
  sections: ['16c3728c', '203acaa5', 'df7a1665', '6da9fd7a', 'cb5fb72e', 'a1cf8b26', 'a419ce79', '66d00206']
  blocks: ['16c3728c', '2a70a7ed', '6f8e6f5f', '16c11d47', '081db416', 'd5e7fd0b', '6d28c323', 'eb2ea361', 'de50125c', 'ae20cb8e', 'abd42710', 'c08a865a', '7d1eb0b9', '263e0c96', '0903299f', 'eba20370', '5cdc20cf', '7f542f82', '802ca5a8', '1a854187', 'bc333adf', 'f25b16fa', '7c893ae2', '7f5927b4', '26e13713', '39a142cf', 'a786620c', '216897fa', '2d222782', 'a9755900', 'f081b357']
---

Dawn il-passi huma bbażati fuq il-firmware MeshCore v1.18.0 u l-għodod uffiċjali ta' Ottubru 2026. L-ismijiet tal-menus fl-app jistgħu jvarjaw ftit minn verżjoni għal oħra.

## 1. Agħżel apparat {#device}

Tista' tuża kull bord fil-[paġna tal-apparati](/devices/) li jkollu companion imniżżel. Għall-ewwel node tiegħek, agħżel *companion*: ir-radju li minnu tibgħat il-messaġġi. Qabbdu mal-mowbajl jew mal-laptop tiegħek permezz ta' Bluetooth jew USB. Inkella, agħżel wieħed li jaħdem waħdu, bl-iskrin u t-tastiera tiegħu.

Ħu l-verżjoni ta' 868 MHz. L-antenna li tiġi mal-apparat tajba biżżejjed. Fil-[gwida tal-antenni](/guides/antenna/) issib kif tiċċekkja waħda.

{{< callout type="warning" >}}
Waħħal l-antenna qabel ma tixgħel ir-radju. Radju LoRa li jittrasmetti mingħajr antenna jista' jagħmel ħsara liċ-ċippa tiegħu stess.
{{< /callout >}}

## 2. Agħmel flash tal-firmware {#flash}

1. Qabbad l-apparat mal-kompjuter b'kejbil USB tad-dejta.
2. Iftaħ il-web flasher fuq [flasher.meshcore.io](https://flasher.meshcore.io) f'Chrome jew Edge. Il-flasher juża Web Serial, li browsers oħra m'għandhomx.
3. Agħżel l-apparat tiegħek, imbagħad il-firmware **Companion** għal **Bluetooth** (jew USB, jekk se tużah biss b'kejbil mal-kompjuter).
4. Agħmel il-flash. Xi bordijiet l-ewwel jidħlu f'modalità ta' aġġornament, u l-flasher jgħidlek kif.

Uża *erase* biss jekk trid tibda mill-ġdid: it-tħassir ineħħi l-identità tal-apparat u l-kuntatti tiegħek. Għall-aġġornamenti ta' wara, agħmel flash mingħajr ma tħassar. Biex iżżomm l-identità tiegħek wara erase, l-ewwel esporta ċ-ċavetta privata tal-companion mill-app, u wara importaha.

## 3. Installa l-app {#app}

L-app uffiċjali ta' MeshCore teżisti għal Android, iOS, Windows u macOS. Fuq [meshcore.io](https://meshcore.io) issib links għal kull verżjoni. Hemm ukoll web app fuq [app.meshcore.nz](https://app.meshcore.nz), li taħdem f'Chrome jew Edge fuq kompjuter.

## 4. Qabbad in-node tiegħek {#pair}

Ixgħel in-node, iftaħ l-app u qabbad miegħu permezz ta' Bluetooth. Meta l-app titolbok PIN:

- node **bi** skrin juri PIN: daħħal dak;
- node **mingħajr** skrin juża `123456`.

Jekk it-tqabbid ifalli, neħħi l-apparat mis-settings tal-Bluetooth tal-mowbajl u erġa' pprova. Imbagħad agħti isem lin-node tiegħek. Ħaddieħor jara dan l-isem, għalhekk tużax ismek sħiħ jew l-indirizz tiegħek jekk ma tridx.

## 5. Agħżel il-preset tar-radju taż-żona tiegħek {#preset}

Ir-radji kollha f'żona jużaw l-istess frekwenza u settings, inkella ma jisimgħux lil xulxin. Fis-settings tar-radju fl-app, agħżel il-preset li tuża ż-żona tiegħek. Barra ż-żoni t'hawn taħt, l-Ewropa tuża **EU/UK (Narrow)**. In-Netherlands, iċ-Ċekja, l-Ungerija, is-Slovakkja, il-Portugall u l-Iżvizzera għandhom il-preset tagħhom, u Limburg fin-Netherlands għandha varjant:

{{< presets >}}

L-apparat tiegħek ma joffrix il-preset taż-żona tiegħek? Daħħal l-4 valuri mit-tabella manwalment fis-settings tar-radju fl-app: frekwenza, bandwidth, spreading factor u coding rate. Node b'valuri differenti ma jismax il-mesh.

M'intix ċert? Il-[grupp lokali tiegħek](/community/) jaf liema preset tuża ż-żona tiegħek. L-app tniżżel din il-lista mill-proġett MeshCore, għalhekk preset ġdid ma jeħtieġ l-ebda aġġornament tal-app.

## 6. Sellem {#hello}

1. **Ħabbar lilek innifsek.** Ibgħat *advert* mill-app. Advert "flood" jgħaddi mir-repeaters (nodes li jgħaddu l-messaġġi), biex kulħadd fuq il-mesh ikun jista' jżidek.
   Il-companions qatt ma jħabbru lilhom infushom awtomatikament.
2. **Sib lil ħaddieħor.** In-nies jidhru fil-kuntatti tiegħek meta l-adverts tagħhom jaslu għandek. Skont is-settings standard, ir-repeaters jibagħtu flood advert kull 47 siegħa, għalhekk il-lista tiegħek tista' tieħu 2 jiem biex timtela.
3. **Ibgħat messaġġ.** Iftaħ kuntatt u ikteb. L-ewwel messaġġ jinxtered fin-netwerk kollu b'flood. Min jirċevih jirrapporta lura r-rotta li ħa, u l-messaġġi ta' wara jsegwu dik ir-rotta.
4. **Ingħaqad mal-kanali.** Il-kanal **Public** huwa diġà konfigurat, u dak kollu li tikteb hemm jasal għand kulħadd fuq il-mesh. Żid il-*hashtag channel* tar-reġjun tiegħek (isem li jibda b'`#`) billi tikteb ismu. Il-[grupp lokali tiegħek](/community/) jgħidlek liema kanali huma attivi.

## Meta xi ħaġa ma taħdimx {#troubleshooting}

**L-app ma ssibx l-apparat tiegħi permezz ta' Bluetooth.**
Probabbilment għamilt flash tal-companion għal USB. Erġa' agħmel flash u agħżel il-verżjoni għal Bluetooth. Fuq il-Heltec V3, l-antenna Bluetooth żgħira integrata għandha firxa qasira, għalhekk żomm il-mowbajl qrib.

**It-tqabbid jibqa' jfalli.**
Neħħi l-apparat mis-settings tal-Bluetooth tal-mowbajl, itfi u erġa' ixgħel il-Bluetooth, u erġa' qabbad bil-PIN li jidher fuq l-iskrin jew b'`123456`.

**Ħadd ma jidher fil-kuntatti tiegħi.**
Iċċekkja li l-preset jaqbel maż-żona tiegħek. Ibgħat flood advert. Jekk m'hemmx repeater fil-firxa tiegħek, tisma' biss ir-radji fil-qrib. Il-[paġna tal-mappa](/map/) turi fejn jinsabu r-repeaters.

**Kuntatt juri "last seen" ta' ġranet ilu, għalkemm huwa attiv.**
Wieħed miż-żewġ nodes għandu l-ħin ħażin. Companion jieħu l-ħin mill-mowbajl tiegħek. Fir-repeaters u r-room servers (nodes li jaħżnu l-messaġġi għal grupp), is-sid irid jissettja l-ħin.

**Messaġġ dirett qatt ma jasal.**
Int trid ikollok lill-persuna l-oħra bħala kuntatt, u hi lilek. Node jwarrab messaġġ minn xi ħadd li ma jafx, mingħajr ma javża lil min bagħtu. Ibgħat flood advert u itlob lill-persuna l-oħra tibgħat wieħed ukoll. Iċċekkja fl-app li żżid il-kuntatti ġodda awtomatikament. L-app iżżid biss nodes fil-limitu ta' hops tagħha.

**Il-kuntatti l-qodma jaħdmu, imma dawk il-ġodda qatt ma jikkonnettjaw.**
L-ewwel messaġġ jinxtered b'flood, u repeater jgħaddih biss jekk ikollu r-reġjun tal-messaġġ. Il-messaġġi ta' wara jsegwu rotta li n-node tgħallem, u l-ebda kontroll tar-reġjun ma jwaqqafhom. Staqsi lill-[grupp lokali tiegħek](/community/) liema reġjuni għandhom ir-repeaters ta' madwarek, u iċċekkja [s-settings għaż-żona tiegħek](/guides/settings/#traffic).

**L-app ma tibqax tikkonnettja mal-companion tiegħek.**
Xi bordijiet għandhom buttuna għall-utent, bħal xi bordijiet RAK u l-Heltec T114. Żommha magħfusa fl-ewwel 8 sekondi wara li jibda l-bord. Il-companion jiftaħ rescue console permezz ta' USB. Fil-console fuq [flasher.meshcore.io](https://flasher.meshcore.io), `set pin <pin>` jissettja PIN ġdid tal-Bluetooth u `erase` iħassar kollox mill-apparat.

**Il-flasher ma jistax jiftaħ il-port serjali fuq Linux.**
L-utent tiegħek għandu bżonn aċċess għall-port, pereżempju `sudo setfacl -m u:$USER:rw /dev/ttyUSB0`, jew sħubija fil-grupp `dialout`.

**Xi ħaġa oħra.** Il-[MeshCore FAQ](https://github.com/meshcore-dev/MeshCore/blob/main/docs/faq.md) ikopri ħafna aktar problemi.
