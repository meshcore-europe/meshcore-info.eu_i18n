---
title: Scagaire paicéad
lead: 'Ná lig do d''athsheoltóir dramhthrácht a chur ar aghaidh: tuilte ó áiteanna i bhfad uait, bot nach stopann choíche, cainéal callánach. Bain triail as socrú ar dtús, ansin cuir ar siúl é.'
description: 'Scagaire paicéad na ndochtearraí athsheoltóra DMC: cad a chaitheann sé amach, socruithe réamhdhéanta d''athsheoltóir gnáth agus d''athsheoltóir gnóthach, gach ordú scagaire lena luach réamhshocraithe, agus conas a fheiceann tú cad a caitheadh amach.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'b07d39a8'
  seeded: '2026-11-02'
  fields: {title: '20a3ef1f', lead: 'd948682d', description: 'a8c57a9f'}
  sections: ['d06c9ddd', 'b1d9a8d1', '2dd3448d', 'ee64176e', 'a3cb880e', '09b568f0', 'a1a4fb68', '95fe64ae', 'dbac19c3', '05123b18', '3fa1bb28', 'e98b2285']
  blocks: ['b6231504', 'c66e4d9a', 'c0502fb4', 'fa699506', 'f7008037', '3acbb97b', '5e55d14c', 'bd024580', '68c8a4b1', '119fc5b9', '61804e40', '2fa7ebe8', '0610128b', 'a3cb880e', '0e6268be', 'e6d77222', 'f50be141', '2a1ae00c', '095e165f', 'd96efc68', 'b8a89bea', 'a29d0e87', 'c69ba7d1', 'f553d783', '1a83fda3', 'b6f87585', '64e2bbfa', 'dc79ca3a', '6ed9acff', 'd3701ccc', 'd4a25061', '22092611', '9184f977', 'f70c9e55', 'b2f0d9cb', 'c7b214c1', 'e8da9f3e', '0742c6c4', '7f2f59ae', '2789fc6d', 'ae920329', '7dd6f173', 'e1ca9ac7', 'ac11c47b', 'ec7913ae']
---

Athsheolann athsheoltóir (nód a chuireann teachtaireachtaí ar aghaidh) gach rud a chloiseann sé.
Ar mesh gnóthach, bíonn dramhthrácht i measc an méid sin. Postálann bot gach nóiméad. Seolann nód amháin
a fhógra (an beannú a ligeann do nóid eile é a aimsiú) arís gach cúpla nóiméad.
Tagann teachtaireachtaí isteach a thaistil trasna leath na tíre. Baineann gach athsheoladh
am craolta de gach duine timpeall ort. Leis an scagaire paicéad, caitheann d'athsheoltóir
an trácht sin amach in áit é a chur ar aghaidh. Chun fáil amach ar dtús cad atá ag tuile do mesh,
agus cad eile a chabhraíonn seachas an scagaire, féach
[Déan an mesh athléimneach](/guides/resilient/).

{{< callout type="warning" >}}
Tá an scagaire paicéad mar chuid de **dhochtearraí athsheoltóra DMC**, an leagan athsheoltóra de
[Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore). Níl scagaire paicéad
ag MeshCore caighdeánach. Tá `region denyf *` agus `set flood.max.unscoped` aige, ar an leathanach
[Orduithe CLI](/guides/cli/). Leanann an treoir seo leagan forbartha 1.18.0 `ecfb2d4`,
dar dáta 19 Deireadh Fómhair 2026. Níl sa leagan cobhsaí 1.17.1 ach na scagairí hop, ráta, cainéil, hais agus míchumtha.
Níl dry-run aige ach oiread.
{{< /callout >}}

## Cad a dhéanann an scagaire {#what}

Ní scrúdaíonn an scagaire ach paicéid a chuireann d'athsheoltóir ar aghaidh trí thuile (iad a sheoladh
chuig gach nód i raon). Ní bhaineann sé riamh leis an méid a sheolann d'athsheoltóir féin, ná le paicéid
a leanann conair aitheanta chuig nód amháin. Téann teachtaireachtaí díreacha agus iarratais
chuig do theagmhálaithe féin agus uathu tríd freisin. Is féidir leis na nithe seo a chaitheamh amach:

- paicéid a chuaigh cheana féin tríd an líon athsheoltóirí (hops) a cheadaíonn tú, de réir chineál an phaicéid;
- níos mó paicéad de chineál amháin in aghaidh an nóiméid ná mar a cheadaíonn tú;
- fógra ó nód a d'fhógair cheana féin sna huaireanta deireanacha;
- teachtaireachtaí ar chainéal a bhlocálann tú;
- gach rud a tháinig trí athsheoltóir amháin a bhlocálann tú;
- teachtaireachtaí grúpa ó sheoltóir amháin nó ina bhfuil focal amháin, nó cuid acu sin;
- teachtaireachtaí grúpa atá briste, nó níos sine ná mar a cheadaíonn tú.

Bíonn an scagaire **as** go dtí go gcuirfidh tú ar siúl é. Socraíonn tú é le horduithe. Clóscríobh iad thar USB
sa [chonsól sraitheach](/firmware/console/) ar an suíomh seo. Nó seol iad ón aip MeshCore, mar atá sa
[treoir athsheoltóra](/repeater-guide/#config).

## Faigh na dochtearraí {#firmware}

Flaiseáil **DutchMeshCore Repeater** ón bhflaiseálaí sa
[DutchMeshCore Toolbox](https://toolbox.dutchmeshcore.nl/). Tá an scagaire céanna sna dochtearraí breathnóra
ó [MQTT ar do bhreathnóir](/guides/mqtt/).

## Bain triail as ar dtús {#dryrun}

I mód dry-run, comhaireann an scagaire gach paicéad a chaithfeadh sé amach, ach cuireann sé ar aghaidh é
mar sin féin. Meas socrú ar an mbealach seo sula gcaitheann sé aon rud amach:

```text
filter on
filter dryrun on
```

Fad atá dry-run ar siúl, críochnaíonn líne stádais `filter` le `(dry-run)`. Is é atá sna háirimh ná
an méid a chaithfeadh sé amach. Fág ag rith é ar feadh lae, ansin breathnaigh orthu (féach
[Cad a caitheadh amach](#stats)). Nuair is cosúil go bhfuil na huimhreacha ceart, cuir i bhfeidhm é:

```text
filter dryrun off
```

## Cumraíochtaí molta {#configs}

### Gnáth-athsheoltóir {#typical}

```text
filter on
filter malformed on
filter rate 05 20 60
filter rate 02 5 60
filter hops 05 32
```

Téann suas le 20 teachtaireacht ghrúpa tríd in aghaidh an nóiméid, agus suas le 5 theachtaireacht dhíreach
in aghaidh an nóiméid. Caitear teachtaireachtaí grúpa briste amach. Ceadaíonn gnáthchumraíocht na ndochtearraí féin
20 teachtaireacht dhíreach in aghaidh an nóiméid. Glacann an leathanach seo leis an 5 a mholann na dochtearraí
ó tharla tuile teachtaireachtaí díreacha i mí Iúil 2026.

### Athsheoltóir gnóthach {#busy}

D'athsheoltóir ar shuíomh ard a chloiseann réigiún iomlán, nó d'athsheoltóir atá faoi thuile:

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

Laghdaíonn sé seo na teachtaireachtaí grúpa agus na fógraí faoi leath, agus cuireann sé fógra gach nóid
ar aghaidh uair sa lá. Caitheann sé amach teachtaireachtaí a chuaigh cheana féin trí 16 athsheoltóir. Tar éis
atosaithe, faigheann gach nód fógra amháin tríd. Socraíonn doiciméid na ndochtearraí féin `filter hash 2` anseo freisin.
Fágann an leathanach seo ar lár é (féach [Gach socrú](#settings) le fáil amach cén fáth).

### Blocáil cainéal callánach {#channel}

```text
filter channel add #bot
```

Cloiseann d'athsheoltóir an cainéal fós. Ní chuireann sé ar aghaidh é a thuilleadh chuig athsheoltóirí eile
ná chuig companions (na nóid óna seolann daoine teachtaireachtaí). Suas le 16 chainéal.

### Cuir moill ar sheoltóir amháin {#sender}

Bot a phostálann rómhinic ar chainéal ar mhaith leat a choinneáil:

```text
filter watch add #test
filter sender add Bob 60
```

Anois téann teachtaireachtaí Bob ar an gcainéal Public agus ar `#test` tríd uair sa nóiméad. Caitear an chuid eile amach.
Meaitseálann an scagaire an t-ainm sa teachtaireacht, mar sin éalaíonn seoltóir a athraíonn a ainm thairis.

### Blocáil athsheoltóir amháin in aghaidh srutha {#path}

Nuair a thagann an dramhthrácht isteach trí athsheoltóir amháin, blocáil a réimír: an chéad chuid dá aitheantas,
i bhfoirm heicsidheachúlach (hex). Tá an leagan forbartha 1.18 de dhíth chuige seo. Níl scagaire conaire ag 1.17.1.

```text
filter path add a1b2
filter path list
filter stats path
```

Taispeánann `filter path list` na réimíreanna a bhlocálann tú, agus `filter stats path` an méid a chaith gach ceann acu amach.
Ligeann `filter path remove a1b2` tríd arís é.
Blocálann réimír ghearr mar `a1` freisin gach athsheoltóir eile a dtosaíonn a aitheantas le `a1`.
Úsáid an réimír is faide is féidir leat. Suas le 8 réimír.

## Gach socrú {#settings}

Tá uimhir ag gach cineál paicéid. Ar an athsheoltóir, taispeánann `filter types` na huimhreacha céanna le hainmneacha na ndochtearraí, mar `TXT_MSG` agus `GRP_TXT`:

| Uimhir | Cineál | Uimhir | Cineál |
| --- | --- | --- | --- |
| `00` | iarratas | `06` | sonraí grúpa |
| `01` | freagra | `07` | iarratas gan ainm |
| `02` | teachtaireacht dhíreach | `08` | conair |
| `03` | admháil | `09` | rianú |
| `04` | fógra | `10` | ilchodach |
| `05` | teachtaireacht ghrúpa | `11` | rialú |

| Ordú | Cad a dhéanann sé | Luach tosaigh |
| --- | --- | --- |
| `filter on` / `filter off` | Cuireann sé an scagaire ar siúl nó as. | as |
| `filter dryrun on` / `off` | Comhaireann sé na paicéid a chaithfí amach ach cuireann sé gach rud ar aghaidh fós. | as |
| `filter hops <type> <max>` | Caitheann sé amach cineál a chuaigh cheana féin tríd an líon seo athsheoltóirí, 0 go 64. | 32 do theachtaireachtaí grúpa, 8 don chuid eile |
| `filter rate <type> <limit> <secs> [soft]` | Cuireann sé ar aghaidh `limit` de chineál ar a mhéad in aghaidh `secs`. Le `soft`, laghdaíonn an cur ar aghaidh de réir a chéile ó `soft` go `limit`. Múchann `0` an teorainn. | 20 in aghaidh 60 s do theachtaireachtaí díreacha agus grúpa, 10 d'fhógraí, 5 don chuid eile |
| `filter advert <hours>` | Cuireann sé fógra gach nóid ar aghaidh uair amháin sa líon seo uaireanta, suas le 720. | 0 (as) |
| `filter channel add <#name>` | Stopann sé ag cur cainéil ar aghaidh. | dada |
| `filter path add <hex>` | Caitheann sé amach gach rud a tháinig trí athsheoltóir leis an réimír seo, 2 go 8 ndigit hex. | dada |
| `filter sender add <name> [secs] [prob]` | Caitheann sé amach teachtaireachtaí grúpa ó sheoltóir, ar Public agus ar chainéil faoi fhaire. Meaitseálann `Bot*` gach ainm a thosaíonn le Bot. | dada |
| `filter text add <word> [secs] [prob]` | Caitheann sé amach teachtaireachtaí grúpa ina bhfuil focal, ar Public agus ar chainéil faoi fhaire. Ní mheaitseálann `^word` ach ag an tús. | dada |
| `filter watch add <#name>` | Ligeann sé do rialacha seoltóra agus téacs an cainéal seo a léamh freisin, suas le 4. Léann siad Public i gcónaí. | Public |
| `filter malformed on` / `off` | Caitheann sé amach teachtaireachtaí Public atá folamh, briste nó a bhfuil an dáta orthu níos mó ná seachtain as (fanann seiceáil an dáta go socrófar an clog). | as |
| `filter age <minutes>` / `off` | Caitheann sé amach teachtaireachtaí grúpa níos sine ná seo, ar Public agus ar chainéil faoi fhaire, 1 go 10080. | as |
| `filter hash <bytes>` | Caitheann sé amach paicéid a bhfuil aitheantas conaire níos giorra ná seo acu, 1 go 3. | 1 |
| `filter reset` | Cuireann sé gach socrú ar ais go dtí a luach réamhshocraithe. | |

Tá `remove` agus `list` ag gach `add`, mar `filter channel remove #bot`.
I rialacha seoltóra agus téacs, ligeann `secs` teachtaireacht amháin tríd sa líon sin soicindí.
Cuireann `prob` an riail i bhfeidhm ar an sciar sin de na meaitseálacha amháin, 1 go 100. Suas le 8 riail seoltóra
agus 8 riail téacs. Bíonn ainmneacha agus focail cásíogair. Is féidir le hainm a bheith suas le 15 charachtar, agus focal suas le 23.

Caitheann dhá shocrú níos mó amach ná mar a cheapfá:

- Caitheann `filter hash 2` beagnach an trácht ar fad amach. Seolann nóid aitheantais conaire 1 bheart de réir réamhshocraithe.
- Braitheann `filter age` ar chlog d'athsheoltóra. Socraigh é le `clock sync` ón aip, seiceáil é le `clock`,
  agus tosaigh go flaithiúil: `filter age 60`.

Coinnítear gach socrú tar éis atosaithe.

## Cad a caitheadh amach {#stats}

Taispeánann `filter` na hiomláin de réir cúise:

```text
> Filter on: Blocked [ Hops: 3 | Rate: 12 | Channel: 1 | Hash: 0 | Malformed: 2 ]
```

Taispeánann `filter stats <topic>` na sonraí do shocrú amháin. Is iad na hábhair
`hops`, `rate`, `channel`, `hash`, `malformed`, `advert`, `path`, `sender`,
`text` agus `age`. Taispeánann `filter stats top` an chéad bheart d'aitheantais na nód is cúis leis an líon is mó paicéad a caitheadh amach.
Tá an beart sin ag go leor nód.
Taispeánann `filter stats air` an t-am craolta a shábháil d'athsheoltóir toisc nár chuir sé na paicéid seo ar aghaidh.

Tosaíonn na háiritheoirí arís ag 0 tar éis atosaithe agus tar éis `clear stats`.
