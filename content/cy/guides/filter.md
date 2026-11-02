---
title: Hidlydd pecynnau
lead: 'Cadw dy ailadroddydd rhag trosglwyddo sothach: llifogydd o bell, bot sydd byth yn stopio, sianel swnllyd. Rho gynnig ar osodiad yn gyntaf, yna rho''r hidlydd ar waith.'
description: 'Hidlydd pecynnau cadarnwedd ailadroddydd DMC: beth mae''n ei ollwng, gosodiadau parod ar gyfer ailadroddydd arferol ac un prysur, pob gorchymyn hidlo gyda''i werth diofyn, a sut i weld beth mae wedi''i ollwng.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'b07d39a8'
  seeded: '2026-11-02'
  fields: {title: '20a3ef1f', lead: 'd948682d', description: 'a8c57a9f'}
  sections: ['d06c9ddd', 'b1d9a8d1', '2dd3448d', 'ee64176e', 'a3cb880e', '09b568f0', 'a1a4fb68', '95fe64ae', 'dbac19c3', '05123b18', '3fa1bb28', 'e98b2285']
  blocks: ['b6231504', 'c66e4d9a', 'c0502fb4', 'fa699506', 'f7008037', '3acbb97b', '5e55d14c', 'bd024580', '68c8a4b1', '119fc5b9', '61804e40', '2fa7ebe8', '0610128b', 'a3cb880e', '0e6268be', 'e6d77222', 'f50be141', '2a1ae00c', '095e165f', 'd96efc68', 'b8a89bea', 'a29d0e87', 'c69ba7d1', 'f553d783', '1a83fda3', 'b6f87585', '64e2bbfa', 'dc79ca3a', '6ed9acff', 'd3701ccc', 'd4a25061', '22092611', '9184f977', 'f70c9e55', 'b2f0d9cb', 'c7b214c1', 'e8da9f3e', '0742c6c4', '7f2f59ae', '2789fc6d', 'ae920329', '7dd6f173', 'e1ca9ac7', 'ac11c47b', 'ec7913ae']
---

Mae ailadroddydd (nod sy'n trosglwyddo negeseuon ymlaen) yn ailadrodd popeth mae'n ei glywed.
Ar rwyll brysur, mae hynny'n cynnwys sothach. Mae bot yn postio bob munud. Mae un nod yn anfon
ei hysbyseb, y cyfarchiad sy'n gadael i eraill ddod o hyd iddo, eto bob ychydig funudau.
Mae negeseuon yn cyrraedd ar ôl teithio ar draws hanner y wlad. Mae pob ailadrodd yn cymryd
amser darlledu oddi wrth bawb o dy gwmpas. Gyda'r hidlydd pecynnau, mae dy ailadroddydd yn gollwng
y traffig hwnnw yn lle ei drosglwyddo. I weld yn gyntaf beth sy'n gorlifo dy rwyll, a beth sy'n
helpu heblaw'r hidlydd, darllena
[Gwneud y rwyll yn wydn](/guides/resilient/).

{{< callout type="warning" >}}
Mae'r hidlydd pecynnau yn rhan o **gadarnwedd ailadroddydd DMC**, fersiwn ailadroddydd
[Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore). Does gan MeshCore safonol ddim
hidlydd pecynnau; mae ganddo `region denyf *` a
`set flood.max.unscoped`, ar y dudalen [gorchmynion CLI](/guides/cli/). Mae'r canllaw hwn
yn dilyn fersiwn ddatblygu 1.18.0 `ecfb2d4` o 19 Hydref 2026. Dim ond yr hidlwyr naid, cyfradd,
sianel, hash a phecynnau diffygiol sydd gan fersiwn sefydlog 1.17.1. Does ganddi ddim dry-run chwaith.
{{< /callout >}}

## Beth mae'r hidlydd yn ei wneud {#what}

Dim ond ar y pecynnau mae dy ailadroddydd yn eu trosglwyddo drwy orlifo (eu hanfon at bob nod
o fewn cyrraedd) mae'r hidlydd yn edrych. Dydy o byth yn cyffwrdd â'r hyn mae dy ailadroddydd
yn ei anfon ei hun, nac â phecynnau sy'n dilyn llwybr hysbys at un nod. Mae negeseuon uniongyrchol
a cheisiadau at dy gysylltiadau di ac oddi wrthyn nhw hefyd yn mynd drwodd. Gall yr hidlydd ollwng:

- pecynnau sydd eisoes wedi pasio cynifer o ailadroddwyr (neidiau) ag rwyt ti'n ei ganiatáu, fesul
  math o becyn;
- mwy o becynnau o un math nag rwyt ti'n eu caniatáu y funud;
- hysbyseb gan nod sydd eisoes wedi hysbysebu yn ystod yr oriau diwethaf;
- negeseuon ar sianel rwyt ti'n ei rhwystro;
- popeth a ddaeth drwy un ailadroddydd rwyt ti'n ei rwystro;
- negeseuon grŵp gan un anfonwr neu gydag un gair, neu rai ohonyn nhw yn unig;
- negeseuon grŵp sydd wedi torri, neu sy'n hŷn nag rwyt ti'n ei ganiatáu.

Mae'r hidlydd **i ffwrdd** nes i ti ei droi ymlaen. Rwyt ti'n ei osod gyda gorchmynion. Teipia nhw
dros USB yn y [consol cyfresol](/firmware/console/) ar y wefan hon. Neu anfona nhw o ap MeshCore,
fel yn y [canllaw ailadroddydd](/repeater-guide/#config).

## Cael y gadarnwedd {#firmware}

Fflachia **DutchMeshCore Repeater** o'r fflachiwr yn
[DutchMeshCore Toolbox](https://toolbox.dutchmeshcore.nl/). Mae gan gadarnwedd yr arsyllwr
o [MQTT ar dy arsyllwr](/guides/mqtt/) yr un hidlydd.

## Rho gynnig arni yn gyntaf {#dryrun}

Mewn dry-run, mae'r hidlydd yn cyfrif pob pecyn y byddai'n ei ollwng, ond yn dal i'w drosglwyddo.
Fel hyn, gelli di bennu gwerthoedd gosodiad cyn iddo ollwng dim:

```text
filter on
filter dryrun on
```

Tra bod dry-run ymlaen, mae llinell statws `filter` yn gorffen gyda `(dry-run)`. Mae'r niferoedd yn
dangos beth fyddai'r hidlydd wedi'i ollwng. Gad iddo redeg am ddiwrnod, yna edrycha arnyn nhw (gweler
[Beth mae wedi'i ollwng](#stats)). Pan fydd y niferoedd yn edrych yn iawn, rho'r hidlydd ar waith:

```text
filter dryrun off
```

## Gosodiadau a argymhellir {#configs}

### Ailadroddydd arferol {#typical}

```text
filter on
filter malformed on
filter rate 05 20 60
filter rate 02 5 60
filter hops 05 32
```

Mae hyd at 20 neges grŵp y funud yn mynd drwodd, a hyd at 5 neges uniongyrchol y funud. Mae negeseuon
grŵp sydd wedi torri yn cael eu gollwng. Mae gosodiad arferol y gadarnwedd ei hun yn caniatáu 20 neges
uniongyrchol y funud. Mae'r dudalen hon yn defnyddio'r 5 mae'r gadarnwedd yn ei argymell ers llif o
negeseuon uniongyrchol ym mis Gorffennaf 2026.

### Ailadroddydd prysur {#busy}

Ar gyfer ailadroddydd ar safle uchel sy'n clywed rhanbarth cyfan, neu un sy'n cael ei orlifo:

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

Mae hyn yn haneru'r negeseuon grŵp a'r hysbysebion, ac yn trosglwyddo hysbyseb pob nod unwaith y dydd.
Mae'n gollwng negeseuon sydd eisoes wedi pasio 16 ailadroddydd. Ar ôl ailgychwyn, mae un hysbyseb gan
bob nod yn mynd drwodd. Mae dogfennau'r gadarnwedd ei hun hefyd yn gosod `filter hash 2` yma; mae'r
dudalen hon yn ei hepgor (gweler [Pob gosodiad](#settings) am y rheswm).

### Rhwystro sianel swnllyd {#channel}

```text
filter channel add #bot
```

Mae dy ailadroddydd yn dal i glywed y sianel. Dydy o ddim yn ei throsglwyddo mwyach i ailadroddwyr
eraill a chymdeithion (y nodau mae pobl yn anfon negeseuon ohonyn nhw). Hyd at 16 sianel.

### Arafu un anfonwr {#sender}

Bot sy'n postio'n rhy aml ar sianel rwyt ti am ei chadw:

```text
filter watch add #test
filter sender add Bob 60
```

Mae negeseuon Bob ar y sianel Public a `#test` bellach yn mynd drwodd unwaith y funud; mae'r gweddill
yn cael ei ollwng. Mae'r hidlydd yn edrych ar yr enw yn y neges, felly mae anfonwr sy'n newid ei enw yn
mynd heibio iddo.

### Rhwystro un ailadroddydd yn gynharach ar y llwybr {#path}

Pan ddaw'r sothach i mewn drwy un ailadroddydd, rhwystra ei ragddodiad: rhan gyntaf ei ID, mewn
hecsadegol (hex). Mae angen fersiwn ddatblygu 1.18 ar gyfer hyn; does gan 1.17.1 ddim hidlydd llwybr.

```text
filter path add a1b2
filter path list
filter stats path
```

Mae `filter path list` yn dangos y rhagddodiaid rwyt ti'n eu rhwystro, a `filter stats path` faint mae
pob un wedi'i ollwng. Mae `filter path remove a1b2` yn gadael iddo fynd drwodd eto.
Mae rhagddodiad byr fel `a1` hefyd yn rhwystro pob ailadroddydd arall y mae ei ID yn dechrau gyda `a1`.
Defnyddia'r rhagddodiad hiraf y galli di. Hyd at 8 rhagddodiad.

## Pob gosodiad {#settings}

Mae gan bob math o becyn rif. Ar yr ailadroddydd, mae `filter types` yn dangos yr un rhifau gydag enwau'r
gadarnwedd, fel `TXT_MSG` a `GRP_TXT`:

| Rhif | Math | Rhif | Math |
| --- | --- | --- | --- |
| `00` | cais | `06` | data grŵp |
| `01` | ymateb | `07` | cais dienw |
| `02` | neges uniongyrchol | `08` | llwybr |
| `03` | cydnabyddiaeth | `09` | olrhain |
| `04` | hysbyseb | `10` | aml-ran |
| `05` | neges grŵp | `11` | rheoli |

| Gorchymyn | Beth mae'n ei wneud | Gwerth cychwynnol |
| --- | --- | --- |
| `filter on` / `filter off` | Troi'r hidlydd ymlaen neu i ffwrdd. | i ffwrdd |
| `filter dryrun on` / `off` | Cyfrif y pecynnau i'w gollwng ond dal i drosglwyddo popeth. | i ffwrdd |
| `filter hops <type> <max>` | Gollwng math sydd eisoes wedi pasio'r nifer hwn o ailadroddwyr, 0 i 64. | 32 ar gyfer negeseuon grŵp, 8 ar gyfer y gweddill |
| `filter rate <type> <limit> <secs> [soft]` | Trosglwyddo uchafswm o `limit` o un math fesul `secs`. Gyda `soft`, mae'r trosglwyddo'n lleihau'n raddol o `soft` i `limit`. Mae `0` yn diffodd y terfyn. | 20 fesul 60 s ar gyfer negeseuon uniongyrchol a grŵp, 10 ar gyfer hysbysebion, 5 ar gyfer y gweddill |
| `filter advert <hours>` | Trosglwyddo hysbyseb pob nod unwaith fesul y nifer hwn o oriau, hyd at 720. | 0 (i ffwrdd) |
| `filter channel add <#name>` | Stopio trosglwyddo sianel. | dim |
| `filter path add <hex>` | Gollwng popeth a ddaeth drwy ailadroddydd gyda'r rhagddodiad hwn, 2 i 8 digid hex. | dim |
| `filter sender add <name> [secs] [prob]` | Gollwng negeseuon grŵp gan anfonwr, ar Public a'r sianeli sy'n cael eu gwylio. Mae `Bot*` yn cyfateb i bob enw sy'n dechrau gyda Bot. | dim |
| `filter text add <word> [secs] [prob]` | Gollwng negeseuon grŵp sy'n cynnwys gair, ar Public a'r sianeli sy'n cael eu gwylio. Mae `^word` yn cyfateb ar y dechrau yn unig. | dim |
| `filter watch add <#name>` | Gadael i'r rheolau anfonwr a thestun ddarllen y sianel hon hefyd, hyd at 4. Mae Public bob amser yn cael ei darllen. | Public |
| `filter malformed on` / `off` | Gollwng negeseuon Public sy'n wag, wedi torri neu â dyddiad sy'n anghywir o fwy nag wythnos (mae'r gwiriad dyddiad yn aros nes bod y cloc wedi'i osod). | i ffwrdd |
| `filter age <minutes>` / `off` | Gollwng negeseuon grŵp sy'n hŷn na hyn, ar Public a'r sianeli sy'n cael eu gwylio, 1 i 10080. | i ffwrdd |
| `filter hash <bytes>` | Gollwng pecynnau gydag ID llwybr byrrach na hyn, 1 i 3. | 1 |
| `filter reset` | Rhoi pob gosodiad yn ôl i'w werth diofyn. | |

Mae gan bob `add` orchymyn `remove` a `list`, fel `filter channel remove #bot`.
Mewn rheolau anfonwr a thestun, mae `secs` yn gadael i un neges fesul y nifer hwnnw o eiliadau fynd drwodd.
Mae `prob` yn cymhwyso'r rheol i'r gyfran honno o'r cyfatebiadau yn unig, 1 i 100. Hyd at 8 rheol anfonwr
ac 8 rheol testun. Mae enwau a geiriau yn sensitif i lythrennau mawr a bach; gall enw fod hyd at 15 cymeriad,
a gair hyd at 23.

Mae dau osodiad yn gollwng mwy nag y gallet ti ei ddisgwyl:

- Mae `filter hash 2` yn gollwng bron yr holl draffig. Mae nodau'n anfon IDs llwybr 1 beit yn ddiofyn.
- Mae `filter age` yn ymddiried yng nghloc dy ailadroddydd. Gosoda'r cloc gyda `clock sync` o'r ap,
  gwiria fo gyda `clock`, a dechreua'n hael: `filter age 60`.

Mae pob gosodiad yn cael ei gadw ar ôl ailgychwyn.

## Beth mae wedi'i ollwng {#stats}

Mae `filter` yn dangos y cyfansymiau fesul rheswm:

```text
> Filter on: Blocked [ Hops: 3 | Rate: 12 | Channel: 1 | Hash: 0 | Malformed: 2 ]
```

Mae `filter stats <topic>` yn dangos y manylion ar gyfer un gosodiad. Y pynciau yw
`hops`, `rate`, `channel`, `hash`, `malformed`, `advert`, `path`, `sender`,
`text` ac `age`. Mae `filter stats top` yn dangos beit cyntaf IDs y nodau sydd y tu ôl i'r nifer fwyaf o
becynnau a ollyngwyd. Mae llawer o nodau'n rhannu'r beit hwnnw.
Mae `filter stats air` yn dangos yr amser darlledu mae dy ailadroddydd wedi'i arbed drwy beidio â
throsglwyddo'r pecynnau hyn.

Mae'r cownteri'n dechrau eto ar 0 ar ôl ailgychwyn ac ar ôl `clear stats`.
