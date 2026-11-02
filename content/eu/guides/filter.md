---
title: Pakete-iragazkia
lead: 'Eragotzi zure errepikagailuak zaborra birbidaltzea: urrutiko uholdeak, inoiz gelditzen ez den bot bat, kanal zaratatsu bat. Probatu ezarpen bat lehenik, eta aktibatu gero.'
description: 'DMC errepikagailu-firmwarearen pakete-iragazkia: zer baztertzen duen, ezarpen prestatuak errepikagailu arrunt baterako eta lanpetu baterako, iragazki-komando guztiak lehenetsitako balioekin, eta baztertutakoa nola ikusi.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'b07d39a8'
  seeded: '2026-11-02'
  fields: {title: '20a3ef1f', lead: 'd948682d', description: 'a8c57a9f'}
  sections: ['d06c9ddd', 'b1d9a8d1', '2dd3448d', 'ee64176e', 'a3cb880e', '09b568f0', 'a1a4fb68', '95fe64ae', 'dbac19c3', '05123b18', '3fa1bb28', 'e98b2285']
  blocks: ['b6231504', 'c66e4d9a', 'c0502fb4', 'fa699506', 'f7008037', '3acbb97b', '5e55d14c', 'bd024580', '68c8a4b1', '119fc5b9', '61804e40', '2fa7ebe8', '0610128b', 'a3cb880e', '0e6268be', 'e6d77222', 'f50be141', '2a1ae00c', '095e165f', 'd96efc68', 'b8a89bea', 'a29d0e87', 'c69ba7d1', 'f553d783', '1a83fda3', 'b6f87585', '64e2bbfa', 'dc79ca3a', '6ed9acff', 'd3701ccc', 'd4a25061', '22092611', '9184f977', 'f70c9e55', 'b2f0d9cb', 'c7b214c1', 'e8da9f3e', '0742c6c4', '7f2f59ae', '2789fc6d', 'ae920329', '7dd6f173', 'e1ca9ac7', 'ac11c47b', 'ec7913ae']
---

Errepikagailu batek (mezuak birbidaltzen dituen nodo batek) entzuten duen guztia errepikatzen du.
Mesh lanpetu batean, horren artean zaborra ere badago. Bot batek minuturo argitaratzen du.
Nodo batek bere iragarkia (besteek aurki dezaten bidaltzen duen agurra) berriro bidaltzen du minutu gutxi batzuetik behin.
Herrialdearen erdia zeharkatu duten mezuak ere iristen dira. Errepikapen bakoitzak aireko denbora kentzen die inguruko guztiei.
Pakete-iragazkiarekin, zure errepikagailuak trafiko hori bazter dezake, birbidali beharrean.
Zure mesha zerk gainezkatzen duen lehenik jakiteko, eta iragazkiaz gain zerk laguntzen duen ikusteko, irakurri
[Egin mesha erresilientea](/guides/resilient/).

{{< callout type="warning" >}}
Pakete-iragazkia **DMC errepikagailu-firmwarearen** parte da, hau da,
[Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore) proiektuaren errepikagailu-bertsioarena.
MeshCore estandarrak ez du pakete-iragazkirik. `region denyf *` eta `set flood.max.unscoped` ditu,
[CLI komandoak](/guides/cli/) orrian. Gida honek 2026ko urriaren 19ko 1.18.0 dev builda (`ecfb2d4`) hartzen du oinarri.
1.17.1 bertsio egonkorrak hop, abiadura, kanal, hash eta akastun paketeen iragazkiak baino ez ditu.
Dry-runik ere ez du.
{{< /callout >}}

## Zer egiten duen iragazkiak {#what}

Iragazkiak zure errepikagailuak flooding bidez (irismeneko nodo guztietara bidalita) birbidaltzen dituen paketeak baino ez ditu aztertzen.
Ez du inoiz ukitzen zure errepikagailuak berak bidaltzen duena, ezta nodo baterako bide ezagun bat jarraitzen duten paketeak ere.
Zure kontaktuetara doazen eta haietatik datozen mezu zuzenak eta eskaerak ere pasatzen dira. Hauek bazter ditzake:

- dagoeneko baimentzen duzun adina errepikagailu (hop) igaro dituzten paketeak, pakete-mota bakoitzeko;
- minutuan baimentzen duzuna baino mota bateko pakete gehiago;
- azken orduetan iragarkia bidali duen nodo baten iragarkia;
- blokeatzen duzun kanal bateko mezuak;
- blokeatzen duzun errepikagailu batetik etorritako guztia;
- igorle bateko edo hitz bat duten talde-mezuak, edo horietako batzuk bakarrik;
- akastunak edo baimentzen duzuna baino zaharragoak diren talde-mezuak.

Iragazkia **itzalita** dago zuk piztu arte. Komandoekin konfiguratzen duzu.
Idatzi USB bidez, webgune honetako [serieko kontsolan](/firmware/console/).
Bestela, bidali MeshCore aplikaziotik, [errepikagailuaren gidan](/repeater-guide/#config) azaltzen den moduan.

## Eskuratu firmwarea {#firmware}

Instalatu **DutchMeshCore Repeater**
[DutchMeshCore Toolbox](https://toolbox.dutchmeshcore.nl/) tresnako flasherraren bidez.
[MQTT zure observerrean](/guides/mqtt/) orriko observer firmwareak iragazki bera du.

## Probatu lehenik {#dryrun}

Dry-run moduan, iragazkiak baztertuko lukeen pakete bakoitza zenbatzen du, baina birbidali egiten du hala ere.
Horrela doi dezakezu ezarpen bat, ezer baztertu aurretik:

```text
filter on
filter dryrun on
```

Dry-run piztuta dagoen bitartean, `filter` komandoaren egoera-lerroa `(dry-run)` testuarekin amaitzen da.
Zenbaketek erakusten dute iragazkiak zer baztertuko zukeen. Utzi martxan egun batez, eta gero begiratu zenbaketei
(ikusi [Zer baztertu duen](#stats)). Zenbakiek itxura ona dutenean, jarri iragazkia benetan martxan:

```text
filter dryrun off
```

## Gomendatutako konfigurazioak {#configs}

### Errepikagailu arrunta {#typical}

```text
filter on
filter malformed on
filter rate 05 20 60
filter rate 02 5 60
filter hops 05 32
```

Minutuan 20 talde-mezu eta 5 mezu zuzen pasatzen dira gehienez, eta iragazkiak talde-mezu akastunak baztertzen ditu.
Firmwarearen beraren konfigurazio arruntak minutuan 20 mezu zuzen baimentzen ditu.
Orri honek 5 erabiltzen ditu, firmwareak 2026ko uztaileko mezu zuzenen uholdetik hona gomendatzen duen kopurua.

### Errepikagailu lanpetua {#busy}

Eskualde oso bat entzuten duen leku garai bateko errepikagailurako, edo uholdea jasaten ari den baterako:

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

Ezarpen honek talde-mezuak eta iragarkiak erdira murrizten ditu, eta nodo bakoitzaren iragarkia egunean behin birbidaltzen du.
Dagoeneko 16 errepikagailu igaro dituzten mezuak baztertzen ditu.
Berrabiarazi ondoren, nodo bakoitzak iragarki bat pasarazten du.
Firmwarearen beraren dokumentazioak `filter hash 2` ere ezartzen du hemen. Orri honek kanpoan uzten du (arrazoia ikusteko, irakurri [Ezarpen guztiak](#settings)).

### Blokeatu kanal zaratatsu bat {#channel}

```text
filter channel add #bot
```

Zure errepikagailuak kanala entzuten jarraitzen du. Ez die gehiago birbidaltzen beste errepikagailuei eta companion nodoei (jendeak mezuak bidaltzeko erabiltzen dituen nodoei).
Gehienez 16 kanal.

### Moteldu igorle bat {#sender}

Mantendu nahi duzun kanal batean gehiegi argitaratzen duen bot baterako:

```text
filter watch add #test
filter sender add Bob 60
```

Orain Boben mezuak minutuan behin pasatzen dira Public kanalean eta `#test` kanalean. Gainerakoak baztertu egiten dira.
Iragazkiak mezuko izenari begiratzen dio, beraz izena aldatzen duen igorleak saihestu egiten du.

### Blokeatu aurreko errepikagailu bat {#path}

Zaborra errepikagailu batetik datorrenean, blokeatu haren aurrizkia: IDaren lehen zatia, hamaseitarrean (hex).
Horretarako 1.18 dev builda behar duzu. 1.17.1 bertsioak ez du bide-iragazkirik.

```text
filter path add a1b2
filter path list
filter stats path
```

`filter path list` komandoak blokeatzen dituzun aurrizkiak erakusten ditu, eta `filter stats path` komandoak bakoitzak zenbat baztertu duen.
`filter path remove a1b2` komandoarekin berriro pasatzen uzten duzu.
`a1` bezalako aurrizki labur batek `a1`-ekin hasten den IDa duten beste errepikagailu guztiak ere blokeatzen ditu.
Erabili ahalik eta aurrizki luzeena. Gehienez 8 aurrizki.

## Ezarpen guztiak {#settings}

Pakete-motek zenbaki bana dute. Errepikagailuan, `filter types` komandoak zenbaki berak erakusten ditu firmwarearen izenekin, hala nola `TXT_MSG` eta `GRP_TXT`:

| Zenbakia | Mota | Zenbakia | Mota |
| --- | --- | --- | --- |
| `00` | eskaera | `06` | talde-datuak |
| `01` | erantzuna | `07` | eskaera anonimoa |
| `02` | mezu zuzena | `08` | bidea |
| `03` | berrespena | `09` | trazadura |
| `04` | iragarkia | `10` | zati anitzekoa |
| `05` | talde-mezua | `11` | kontrola |

| Komandoa | Zer egiten duen | Hasierako balioa |
| --- | --- | --- |
| `filter on` / `filter off` | Iragazkia piztu edo itzaltzen du. | itzalita |
| `filter dryrun on` / `off` | Baztertzeak zenbatzen ditu, baina dena birbidaltzen du. | itzalita |
| `filter hops <type> <max>` | Dagoeneko hainbeste errepikagailu igaro dituen mota bateko paketeak baztertzen ditu, 0tik 64ra. | 32 talde-mezuetarako, 8 gainerakoetarako |
| `filter rate <type> <limit> <secs> [soft]` | Mota bateko `limit` pakete pasatzen ditu gehienez `secs` bakoitzean. `soft` erabilita, birbidaltzea pixkanaka murrizten da `soft` baliotik `limit` baliora. `0` balioak muga kentzen du. | Mezu zuzenetarako eta talde-mezuetarako 20 60 s-tan, iragarkietarako 10, gainerakoetarako 5 |
| `filter advert <hours>` | Nodo bakoitzaren iragarkia hainbeste ordutan behin birbidaltzen du, gehienez 720. | 0 (itzalita) |
| `filter channel add <#name>` | Kanal bat birbidaltzeari uzten dio. | bat ere ez |
| `filter path add <hex>` | Aurrizki hau duen errepikagailu batetik etorritako guztia baztertzen du, 2tik 8ra hex digitu. | bat ere ez |
| `filter sender add <name> [secs] [prob]` | Igorle baten talde-mezuak baztertzen ditu, Public kanalean eta behatutako kanaletan. `Bot*` balioak Bot-ekin hasten diren izen guztiak hartzen ditu. | bat ere ez |
| `filter text add <word> [secs] [prob]` | Hitz bat duten talde-mezuak baztertzen ditu, Public kanalean eta behatutako kanaletan. `^word` balioak hasieran bakarrik bilatzen du. | bat ere ez |
| `filter watch add <#name>` | Igorle- eta testu-arauek kanal hau ere irakur dezaten uzten du, gehienez 4. Public beti irakurtzen da. | Public |
| `filter malformed on` / `off` | Public kanaleko mezu hutsak, akastunak edo astebete baino gehiagoko data-aldea dutenak baztertzen ditu (data-egiaztapenak erlojua ezarri arte itxaroten du). | itzalita |
| `filter age <minutes>` / `off` | Hau baino zaharragoak diren talde-mezuak baztertzen ditu, Public kanalean eta behatutako kanaletan, 1etik 10080ra. | itzalita |
| `filter hash <bytes>` | Hau baino bide-ID laburragoa duten paketeak baztertzen ditu, 1etik 3ra. | 1 |
| `filter reset` | Ezarpen guztiak lehenetsitako baliora itzultzen ditu. | |

`add` bakoitzak `remove` eta `list` ditu, adibidez `filter channel remove #bot`.
Igorle- eta testu-arauetan, `secs` balioak mezu bat pasatzen uzten du hainbeste segundotan behin.
`prob` balioarekin, araua bat datozenen ehuneko horri bakarrik aplikatzen zaio, 1etik 100era.
Gehienez 8 igorle-arau eta 8 testu-arau. Izenek eta hitzek maiuskulak eta minuskulak bereizten dituzte.
Izen batek gehienez 15 karaktere ditu, eta hitz batek gehienez 23.

Bi ezarpenek espero baino gehiago baztertzen dute:

- `filter hash 2` ezarpenak ia trafiko guztia baztertzen du. Nodoek 1 byteko bide-IDak bidaltzen dituzte lehenespenez.
- `filter age` ezarpena zure errepikagailuaren erlojuaz fidatzen da. Ezarri erlojua aplikazioko `clock sync` komandoarekin, egiaztatu `clock` komandoarekin, eta hasi balio zabal batekin: `filter age 60`.

Ezarpen guztiak gordeta geratzen dira berrabiarazi ondoren.

## Zer baztertu duen {#stats}

`filter` komandoak arrazoi bakoitzeko guztizkoak erakusten ditu:

```text
> Filter on: Blocked [ Hops: 3 | Rate: 12 | Channel: 1 | Hash: 0 | Malformed: 2 ]
```

`filter stats <topic>` komandoak ezarpen baten xehetasunak erakusten ditu. Gaiak hauek dira:
`hops`, `rate`, `channel`, `hash`, `malformed`, `advert`, `path`, `sender`, `text` eta `age`.
`filter stats top` komandoak baztertze gehien eragin dituzten nodoen IDen lehen bytea erakusten du.
Nodo askok byte bera dute.
`filter stats air` komandoak erakusten du zenbat aireko denbora aurreztu duen zure errepikagailuak pakete hauek ez birbidaltzean.

Kontagailuak 0tik hasten dira berriro berrabiarazi ondoren eta `clear stats` komandoaren ondoren.
