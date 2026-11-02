---
title: Paketfilter
lead: 'Verhënner, datt däi Repeater Knascht weiderschéckt: Floods vu wäit ewech, e Bot, deen ni ophält, e Kanal mat vill Kaméidi. Test eng Astellung als éischt, schalt se dann un.'
description: 'De Paketfilter vun der DMC-Repeater-Firmware: wat e verwerft, fäerdeg Astellunge fir en normalen an e vollen Repeater, all Filterbefehl mat sengem Standardwäert, a wéi s du gesäis, wat e verworf huet.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'b07d39a8'
  seeded: '2026-11-02'
  fields: {title: '20a3ef1f', lead: 'd948682d', description: 'a8c57a9f'}
  sections: ['d06c9ddd', 'b1d9a8d1', '2dd3448d', 'ee64176e', 'a3cb880e', '09b568f0', 'a1a4fb68', '95fe64ae', 'dbac19c3', '05123b18', '3fa1bb28', 'e98b2285']
  blocks: ['b6231504', 'c66e4d9a', 'c0502fb4', 'fa699506', 'f7008037', '3acbb97b', '5e55d14c', 'bd024580', '68c8a4b1', '119fc5b9', '61804e40', '2fa7ebe8', '0610128b', 'a3cb880e', '0e6268be', 'e6d77222', 'f50be141', '2a1ae00c', '095e165f', 'd96efc68', 'b8a89bea', 'a29d0e87', 'c69ba7d1', 'f553d783', '1a83fda3', 'b6f87585', '64e2bbfa', 'dc79ca3a', '6ed9acff', 'd3701ccc', 'd4a25061', '22092611', '9184f977', 'f70c9e55', 'b2f0d9cb', 'c7b214c1', 'e8da9f3e', '0742c6c4', '7f2f59ae', '2789fc6d', 'ae920329', '7dd6f173', 'e1ca9ac7', 'ac11c47b', 'ec7913ae']
---

E Repeater (en Node, deen Noriichte weiderschéckt) widderhëlt alles, wat en héiert.
Op engem volle Mesh ass och Knascht dobäi. E Bot postt all Minutt. En Node
schéckt all puer Minutten erëm säin Advert, de Gruss, duerch deen anerer e
fannen. Et kommen Noriichten un, déi duerch d'halleft Land gereest sinn. All
Widderhuelung hëlt jidderengem ronderëm dech Airtime ewech. Mam Paketfilter
verwerft däi Repeater dësen Traffic, amplaz e weiderzeschécken. Fir als éischt
erauszefannen, wat däi Mesh iwwerschwemmt, a wat nieft dem Filter hëlleft, kuck
[De Mesh robust maachen](/guides/resilient/).

{{< callout type="warning" >}}
De Paketfilter gehéiert zur **DMC-Repeater-Firmware**, dem Repeater-Build vun
[Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore). Standard-MeshCore
huet kee Paketfilter. Et huet `region denyf *` an `set flood.max.unscoped`, op
der Säit [CLI-Befeeler](/guides/cli/). Dëse Guide baséiert um 1.18.0-Dev-Build
`ecfb2d4` vum 19. Oktober 2026. De stabille 1.17.1-Build huet nëmmen d'Filtere
fir Hops, Rate, Kanal, Hash a futtis Paketen. En huet och keen Dry-run.
{{< /callout >}}

## Wat de Filter mécht {#what}

De Filter kuckt sech nëmme Paketen un, déi däi Repeater per Flooding weiderschéckt
(un all Node a Reechwäit). E léisst ëmmer a Rou, wat däi Repeater selwer schéckt,
an och Paketen, déi op enger bekannter Route bei een Node ginn. Direkt Noriichten
an Ufroe vun an un deng eege Kontakter ginn och duerch. De Filter kann dës Saache
verwerfen:

- Paketen, déi schonn esou vill Repeater (Hops) passéiert hunn, wéi s du pro
  Pakettyp erlaabs;
- méi Pakete vun engem Typ pro Minutt, wéi s du erlaabs;
- en Advert vun engem Node, deen an de leschte Stonne schonn en Advert
  geschéckt huet;
- Noriichten op engem Kanal, deen s du spärs;
- alles, wat duerch ee Repeater komm ass, deen s du spärs;
- Gruppennoriichte vun engem Sender oder mat engem Wuert, oder nëmmen een Deel
  dovun;
- Gruppennoriichten, déi futtis oder méi al sinn, wéi s du erlaabs.

De Filter ass **aus**, bis s du en unschalts. Du stells e mat Befeeler an. Tipp
se iwwer USB an der [serieller Konsol](/firmware/console/) op dësem Site. Oder
schéck se aus der MeshCore-App, wéi am
[Repeater-Guide](/repeater-guide/#config).

## D'Firmware kréien {#firmware}

Flash **DutchMeshCore Repeater** mam Flasher an der
[DutchMeshCore Toolbox](https://toolbox.dutchmeshcore.nl/). D'Observer-Firmware
vun [MQTT op dengem Observer](/guides/mqtt/) huet dee selwechte Filter.

## Als éischt testen {#dryrun}

Am Dry-run zielt de Filter all Paket, deen e géif verwerfen, mä e schéckt en
trotzdeem weider. Sou kanns du eng Astellung ofstëmmen, ier se eppes verwerft:

```text
filter on
filter dryrun on
```

Soulaang den Dry-run un ass, hält d'Statuszeil vu `filter` mat `(dry-run)` op.
D'Zuele weisen, wat de Filter verworf hätt. Looss en een Dag lafen, a kontrolléier
dann d'Zuelen (kuck [Wat e verworf huet](#stats)). Wann d'Zuele richteg ausgesinn,
looss de Filter wierklech verwerfen:

```text
filter dryrun off
```

## Recommandéiert Konfiguratiounen {#configs}

### En normale Repeater {#typical}

```text
filter on
filter malformed on
filter rate 05 20 60
filter rate 02 5 60
filter hops 05 32
```

Bis zu 20 Gruppennoriichten d'Minutt ginn duerch, bis zu 5 direkt Noriichten
d'Minutt, a futtis Gruppennoriichte verwerft de Filter. Déi normal Konfiguratioun
vun der Firmware selwer erlaabt 20 direkt Noriichten d'Minutt. Dës Säit hëlt déi
5, déi d'Firmware recommandéiert, zënter engem Flood vun direkten Noriichten am
Juli 2026.

### E Repeater mat vill Traffic {#busy}

Fir e Repeater op enger héijer Plaz, deen eng ganz Regioun héiert, oder een, deen
iwwerschwemmt gëtt:

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

Dat halbéiert d'Gruppennoriichten an d'Adverten, a schéckt den Advert vun all Node
eemol den Dag weider. E verwerft Noriichten, déi schonn 16 Repeater passéiert hunn.
No engem Reboot kënnt vun all Node een Advert duerch. D'Dokumentatioun vun der
Firmware setzt hei och `filter hash 2`. Dës Säit léisst dat ewech (firwat, steet
ënner [All Astellungen](#settings)).

### E Kanal mat vill Kaméidi spären {#channel}

```text
filter channel add #bot
```

Däi Repeater héiert de Kanal weider. E schéckt en awer net méi un aner Repeater
a Companions (d'Noden, vun deenen aus d'Leit Noriichte schécken) weider. Bis zu
16 Kanäl.

### Ee Sender bremsen {#sender}

E Bot, deen ze dacks op engem Kanal postt, deen s du behale wëlls:

```text
filter watch add #test
filter sender add Bob 60
```

Dem Bob seng Noriichten um Public-Kanal an op `#test` ginn elo eemol d'Minutt
duerch. De Rescht verwerft de Filter. De Filter vergläicht den Numm an der
Noriicht, dofir kënnt e Sender laanscht, deen en aneren Numm hëlt.

### Ee Repeater virdrun op der Route spären {#path}

Wann de Knascht iwwer ee Repeater erakënnt, spär säi Prefix: den éischten Deel
vu senger ID, hexadezimal (Hex) geschriwwen. Dofir brauchs du den 1.18-Dev-Build.
1.17.1 huet kee Path-Filter.

```text
filter path add a1b2
filter path list
filter stats path
```

`filter path list` weist d'Prefixen, déi s du spärs, `filter stats path` wéi
vill all Prefix verworf huet. Mat `filter path remove a1b2` léisst du en erëm
duerch. E kuerze Prefix wéi `a1` spärt och all anere Repeater, deem seng ID mat
`a1` ufänkt. Benotz esou e laange Prefix wéi méiglech. Bis zu 8 Prefixen.

## All Astellungen {#settings}

Pakettypen hunn eng Nummer. Um Repeater weist `filter types` déi selwecht Nummere
mat den Nimm vun der Firmware, wéi `TXT_MSG` a `GRP_TXT`:

| Nummer | Typ | Nummer | Typ |
| --- | --- | --- | --- |
| `00` | Ufro | `06` | Gruppendaten |
| `01` | Äntwert | `07` | anonym Ufro |
| `02` | direkt Noriicht | `08` | Path |
| `03` | Bestätegung | `09` | Trace |
| `04` | Advert | `10` | Multipart |
| `05` | Gruppennoriicht | `11` | Kontroll |

| Befehl | Wat e mécht | Ufankswäert |
| --- | --- | --- |
| `filter on` / `filter off` | Schalt de Filter un oder aus. | aus |
| `filter dryrun on` / `off` | Zielt, wat verworf gëtt, mä schéckt alles weider. | aus |
| `filter hops <type> <max>` | Verwerft en Typ, deen schonn esou vill Repeater passéiert huet, 0 bis 64. | 32 fir Gruppennoriichten, 8 fir de Rescht |
| `filter rate <type> <limit> <secs> [soft]` | Schéckt héchstens `limit` vun engem Typ pro `secs` weider. Mat `soft` geet d'Weiderschécken tëscht `soft` a `limit` lues zeréck. `0` schalt d'Limit aus. | 20 pro 60 s fir direkt a Gruppennoriichten, 10 fir Adverten, 5 fir de Rescht |
| `filter advert <hours>` | Schéckt den Advert vun all Node eemol pro esou vill Stonne weider, bis zu 720. | 0 (aus) |
| `filter channel add <#name>` | Schéckt e Kanal net méi weider. | keng |
| `filter path add <hex>` | Verwerft alles, wat duerch e Repeater mat dësem Prefix komm ass, 2 bis 8 Hex-Zifferen. | keng |
| `filter sender add <name> [secs] [prob]` | Verwerft Gruppennoriichte vun engem Sender, op Public an iwwerwaachte Kanäl. `Bot*` passt op all Numm, deen mat Bot ufänkt. | keng |
| `filter text add <word> [secs] [prob]` | Verwerft Gruppennoriichten, an deenen e Wuert steet, op Public an iwwerwaachte Kanäl. `^word` passt nëmmen um Ufank. | keng |
| `filter watch add <#name>` | Léisst d'Sender- an Textreegelen och dëse Kanal liesen, bis zu 4. Public liesen se ëmmer. | Public |
| `filter malformed on` / `off` | Verwerft Public-Noriichten, déi eidel oder futtis sinn oder deenen hiren Datum méi wéi eng Woch dernieft läit (den Datumscheck waart, bis d'Auer gestallt ass). | aus |
| `filter age <minutes>` / `off` | Verwerft Gruppennoriichten, déi méi al sinn wéi dëse Wäert, op Public an iwwerwaachte Kanäl, 1 bis 10080. | aus |
| `filter hash <bytes>` | Verwerft Pakete mat enger Path-ID, déi méi kuerz ass wéi dëse Wäert, 1 bis 3. | 1 |
| `filter reset` | Setzt all Astellung op hire Standardwäert zeréck. | |

All `add` huet e `remove` an e `list`, wéi `filter channel remove #bot`. A Sender- an Textreegele léisst `secs` eng Noriicht pro esou vill Sekonnen duerch. `prob`
wennt d'Reegel nëmmen op dësen Undeel vun den Treffer un, 1 bis 100. Bis zu 8
Sender- an 8 Textreegelen. Bei Nimm a Wierder zielt d'Grouss- a Klengschreiwung.
En Numm huet bis zu 15 Zeechen, e Wuert bis zu 23.

Zwou Astellunge verwerfe méi, wéi s du vläicht erwaars:

- `filter hash 2` verwerft bal den ganzen Traffic. Node schécken standardméisseg
  Path-IDe vun 1 Byte.
- `filter age` verléisst sech op d'Auer vun dengem Repeater. Stell se mat
  `clock sync` aus der App, kontrolléier se mat `clock`, a fänk mat vill Spillraum
  un: `filter age 60`.

All Astellung bleift no engem Reboot erhalen.

## Wat e verworf huet {#stats}

`filter` weist d'Zomme pro Grond:

```text
> Filter on: Blocked [ Hops: 3 | Rate: 12 | Channel: 1 | Hash: 0 | Malformed: 2 ]
```

`filter stats <topic>` weist d'Detailer fir eng Astellung. D'Theme sinn `hops`,
`rate`, `channel`, `hash`, `malformed`, `advert`, `path`, `sender`, `text` an
`age`. `filter stats top` weist den éischte Byte vun den Node-IDen hannert de
meeschte verworfene Paketen. Vill Noden deelen dëse Byte. `filter stats air`
weist d'Airtime, déi däi Repeater gespuert huet, well en dës Paketen net
weidergeschéckt huet.

D'Zieler fänken no engem Reboot an no `clear stats` erëm bei 0 un.
