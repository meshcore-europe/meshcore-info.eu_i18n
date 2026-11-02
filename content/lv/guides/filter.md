---
title: Pakešu filtrs
lead: 'Neļauj savam retranslatoram pārsūtīt nevajadzīgu trafiku: ziņu plūdus no tālienes, botu, kas nekad neapstājas, trokšņainu kanālu. Vispirms izmēģini iestatījumu, pēc tam ieslēdz to.'
description: 'DMC retranslatora programmaparatūras pakešu filtrs: ko tas atmet, gatavi iestatījumi parastam un noslogotam retranslatoram, visas filtra komandas ar noklusējuma vērtībām un veids, kā redzēt atmestās paketes.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'b07d39a8'
  seeded: '2026-11-02'
  fields: {title: '20a3ef1f', lead: 'd948682d', description: 'a8c57a9f'}
  sections: ['d06c9ddd', 'b1d9a8d1', '2dd3448d', 'ee64176e', 'a3cb880e', '09b568f0', 'a1a4fb68', '95fe64ae', 'dbac19c3', '05123b18', '3fa1bb28', 'e98b2285']
  blocks: ['b6231504', 'c66e4d9a', 'c0502fb4', 'fa699506', 'f7008037', '3acbb97b', '5e55d14c', 'bd024580', '68c8a4b1', '119fc5b9', '61804e40', '2fa7ebe8', '0610128b', 'a3cb880e', '0e6268be', 'e6d77222', 'f50be141', '2a1ae00c', '095e165f', 'd96efc68', 'b8a89bea', 'a29d0e87', 'c69ba7d1', 'f553d783', '1a83fda3', 'b6f87585', '64e2bbfa', 'dc79ca3a', '6ed9acff', 'd3701ccc', 'd4a25061', '22092611', '9184f977', 'f70c9e55', 'b2f0d9cb', 'c7b214c1', 'e8da9f3e', '0742c6c4', '7f2f59ae', '2789fc6d', 'ae920329', '7dd6f173', 'e1ca9ac7', 'ac11c47b', 'ec7913ae']
---

Retranslators (mezgls, kas pārsūta ziņas tālāk) atkārto visu, ko dzird.
Noslogotā tīklā tas ietver arī nevajadzīgu trafiku. Kāds bots publicē ziņu katru minūti. Kāds mezgls
ik pēc dažām minūtēm atkal sūta savu paziņojumu (advert), sveicienu, pēc kura citi to atrod.
Pienāk ziņas, kas ceļojušas pāri pusei valsts. Katrs atkārtojums atņem ētera laiku
visiem tev apkārt. Ar pakešu filtru tavs retranslators šo trafiku atmet
un nepārsūta tālāk. Lapā
[Padari tīklu noturīgu](/guides/resilient/) vari vispirms noskaidrot, kas pārpludina tavu tīklu
un kas vēl palīdz bez filtra.

{{< callout type="warning" >}}
Pakešu filtrs ir daļa no **DMC retranslatora programmaparatūras**, kas ir
[Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore) retranslatora būvējums. Standarta
MeshCore nav pakešu filtra. Tajā ir `region denyf *` un
`set flood.max.unscoped`, kas aprakstīti lapā [CLI komandas](/guides/cli/). Šī
rokasgrāmata atbilst 2026. gada 19. oktobra izstrādes būvējumam 1.18.0 `ecfb2d4`. Stabilajā
būvējumā 1.17.1 ir tikai lēcienu, ātruma, kanālu, jaucējvērtības un bojāto pakešu filtri.
Tajā nav arī dry-run režīma.
{{< /callout >}}

## Ko filtrs dara {#what}

Filtrs pārbauda tikai tās paketes, ko tavs retranslators pārsūta ar pārpludināšanu (sūta
visiem mezgliem darbības zonā). Tas nekad neaiztiek to, ko tavs retranslators sūta
pats, vai paketes, kas pa zināmu maršrutu iet uz vienu mezglu. Tiešās ziņas un
pieprasījumi no taviem kontaktiem un uz tiem arī iet cauri. Filtrs var atmest:

- paketes, kas jau izgājušas caur tik daudziem retranslatoriem (lēcieniem, hops), cik tu atļauj,
  katram pakešu tipam atsevišķi;
- vairāk viena tipa pakešu minūtē, nekā tu atļauj;
- paziņojumu no mezgla, kas jau sūtījis paziņojumu pēdējās stundās;
- ziņas kanālā, ko tu bloķē;
- visu, kas nācis caur vienu tevis bloķētu retranslatoru;
- grupas ziņas no viena sūtītāja vai ar vienu vārdu, vai tikai daļu no tām;
- grupas ziņas, kas ir bojātas vai vecākas, nekā tu atļauj.

Filtrs ir **izslēgts**, līdz tu to ieslēdz. Tu to iestati ar komandām. Ievadi
tās pa USB šīs vietnes [seriālajā konsolē](/firmware/console/). Vari arī
sūtīt tās no MeshCore lietotnes, kā aprakstīts
[retranslatora rokasgrāmatā](/repeater-guide/#config).

## Iegūsti programmaparatūru {#firmware}

Ieraksti ierīcē **DutchMeshCore Repeater** ar programmaparatūras ierakstīšanas rīku no
[DutchMeshCore Toolbox](https://toolbox.dutchmeshcore.nl/). Novērotāja programmaparatūrā no lapas
[MQTT tavā novērotājā](/guides/mqtt/) ir tāds pats filtrs.

## Vispirms izmēģini {#dryrun}

Dry-run režīmā filtrs saskaita katru paketi, ko tas atmestu, bet tomēr pārsūta
to tālāk. Tā vari piemeklēt iestatījumu, pirms filtrs kaut ko atmet:

```text
filter on
filter dryrun on
```

Kamēr dry-run ir ieslēgts, `filter` statusa rindas beigās ir `(dry-run)`. Skaitītāji
rāda, ko filtrs būtu atmetis. Ļauj tam darboties vienu dienu, tad apskati
skaitļus (skaties [Ko filtrs atmeta](#stats)). Kad skaitļi izskatās pareizi, ieslēdz
īstu atmešanu:

```text
filter dryrun off
```

## Ieteicamās konfigurācijas {#configs}

### Parasts retranslators {#typical}

```text
filter on
filter malformed on
filter rate 05 20 60
filter rate 02 5 60
filter hops 05 32
```

Filtrs izlaiž līdz 20 grupas ziņām minūtē un līdz 5 tiešajām ziņām minūtē.
Bojātās grupas ziņas tas atmet. Pašas programmaparatūras parastā konfigurācija
atļauj 20 tiešās ziņas minūtē. Šī lapa izmanto skaitli 5, ko programmaparatūra iesaka
kopš tiešo ziņu plūdiem 2026. gada jūlijā.

### Noslogots retranslators {#busy}

Retranslatoram augstā vietā, kas dzird visu reģionu, vai retranslatoram, ko
pārpludina:

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

Šie iestatījumi uz pusi samazina grupas ziņas un paziņojumus un izlaiž katra mezgla
paziņojumu reizi dienā. Filtrs atmet ziņas, kas jau izgājušas caur 16 retranslatoriem. Pēc
pārstartēšanas katram mezglam cauri tiek viens paziņojums. Pašas programmaparatūras dokumentācijā šeit
ir arī `filter hash 2`. Šajā lapā tā nav (iemeslu skaties sadaļā
[Visi iestatījumi](#settings)).

### Bloķē trokšņainu kanālu {#channel}

```text
filter channel add #bot
```

Tavs retranslators joprojām dzird šo kanālu. Tas vairs nepārsūta to citiem
retranslatoriem un companion ierīcēm (mezgliem, no kuriem cilvēki sūta ziņas). Vari bloķēt līdz 16 kanāliem.

### Palēnini vienu sūtītāju {#sender}

Bots pārāk bieži publicē ziņas kanālā, ko gribi paturēt:

```text
filter watch add #test
filter sender add Bob 60
```

Bob ziņas kanālos Public un `#test` tagad iet cauri reizi minūtē, pārējās
filtrs atmet. Filtrs pārbauda ziņā norādīto vārdu, tāpēc sūtītājs, kurš nomaina vārdu, tiek tam garām.

### Bloķē vienu retranslatoru ceļā uz tevi {#path}

Ja nevajadzīgais trafiks nāk caur vienu retranslatoru, bloķē tā prefiksu: tā ID
pirmo daļu heksadecimālā pierakstā (hex). Tam vajag izstrādes būvējumu 1.18, jo būvējumā 1.17.1
nav ceļa filtra.

```text
filter path add a1b2
filter path list
filter stats path
```

`filter path list` rāda tevis bloķētos prefiksus, bet `filter stats path` rāda, cik
daudz atmests katra prefiksa dēļ. Ar `filter path remove a1b2` tu to atkal izlaid cauri.
Īss prefikss, piemēram, `a1`, bloķē arī visus citus retranslatorus, kuru ID sākas
ar `a1`. Izmanto garāko prefiksu, kādu vari. Vari bloķēt līdz 8 prefiksiem.

## Visi iestatījumi {#settings}

Pakešu tipiem ir numuri. Retranslatorā `filter types` rāda tos pašus
numurus ar programmaparatūras nosaukumiem, piemēram, `TXT_MSG` un `GRP_TXT`:

| Numurs | Tips | Numurs | Tips |
| --- | --- | --- | --- |
| `00` | pieprasījums | `06` | grupas dati |
| `01` | atbilde | `07` | anonīms pieprasījums |
| `02` | tiešā ziņa | `08` | ceļš |
| `03` | apstiprinājums | `09` | izsekošana |
| `04` | paziņojums | `10` | vairākdaļu pakete |
| `05` | grupas ziņa | `11` | vadība |

| Komanda | Ko tā dara | Sākumvērtība |
| --- | --- | --- |
| `filter on` / `filter off` | Ieslēdz vai izslēdz filtru. | izslēgts |
| `filter dryrun on` / `off` | Skaita atmestās paketes, bet tomēr visu pārsūta tālāk. | izslēgts |
| `filter hops <type> <max>` | Atmet šī tipa paketes, kas jau izgājušas caur tik daudziem retranslatoriem, no 0 līdz 64. | 32 grupas ziņām, 8 pārējām |
| `filter rate <type> <limit> <secs> [soft]` | Izlaiž ne vairāk kā `limit` viena tipa pakešu `secs` sekundēs. Ar `soft` izlaišana pakāpeniski samazinās no `soft` līdz `limit`. `0` izslēdz ierobežojumu. | 20 katrās 60 s tiešajām un grupas ziņām, 10 paziņojumiem, 5 pārējām |
| `filter advert <hours>` | Izlaiž katra mezgla paziņojumu reizi norādītajā stundu skaitā, līdz 720. | 0 (izslēgts) |
| `filter channel add <#name>` | Pārtrauc kanāla pārsūtīšanu. | nav |
| `filter path add <hex>` | Atmet visu, kas nācis caur retranslatoru ar šo prefiksu, no 2 līdz 8 hex cipariem. | nav |
| `filter sender add <name> [secs] [prob]` | Atmet sūtītāja grupas ziņas kanālā Public un novērotajos kanālos. `Bot*` atbilst katram vārdam, kas sākas ar Bot. | nav |
| `filter text add <word> [secs] [prob]` | Atmet grupas ziņas, kurās ir noteikts vārds, kanālā Public un novērotajos kanālos. `^word` atbilst tikai sākumā. | nav |
| `filter watch add <#name>` | Ļauj sūtītāju un teksta noteikumiem lasīt arī šo kanālu, līdz 4 kanāliem. Public tie lasa vienmēr. | Public |
| `filter malformed on` / `off` | Atmet Public ziņas, kas ir tukšas, bojātas vai kuru datums atšķiras vairāk nekā par nedēļu (datuma pārbaude gaida, līdz pulkstenis ir iestatīts). | izslēgts |
| `filter age <minutes>` / `off` | Atmet grupas ziņas, kas vecākas par šo vērtību, kanālā Public un novērotajos kanālos, no 1 līdz 10080. | izslēgts |
| `filter hash <bytes>` | Atmet paketes, kuru ceļa ID ir īsāks par šo vērtību, no 1 līdz 3. | 1 |
| `filter reset` | Atjauno visu iestatījumu noklusējuma vērtības. | |

Katrai `add` komandai ir `remove` un `list`, piemēram, `filter channel remove #bot`.
Sūtītāju un teksta noteikumos `secs` izlaiž vienu ziņu norādītajā sekunžu skaitā.
`prob` piemēro noteikumu tikai šai atbilstību daļai, no 1 līdz 100. Vari izveidot līdz 8
sūtītāju un 8 teksta noteikumiem. Sūtītāju vārdos un teksta vārdos atšķiras lielie un mazie burti. Sūtītāja vārdā var būt līdz
15 rakstzīmēm, teksta vārdā līdz 23.

Divi iestatījumi atmet vairāk, nekā tu varētu gaidīt:

- `filter hash 2` atmet gandrīz visu trafiku. Mezgli pēc noklusējuma sūta 1 baita ceļa
  ID.
- `filter age` paļaujas uz tava retranslatora pulksteni. Iestati to ar `clock sync` no
  lietotnes, pārbaudi ar `clock` un sāc ar lielu rezervi: `filter age 60`.

Visi iestatījumi saglabājas pēc pārstartēšanas.

## Ko filtrs atmeta {#stats}

`filter` rāda kopsummas pa iemesliem:

```text
> Filter on: Blocked [ Hops: 3 | Rate: 12 | Channel: 1 | Hash: 0 | Malformed: 2 ]
```

`filter stats <topic>` rāda sīkāku informāciju par vienu iestatījumu. Tēmas ir
`hops`, `rate`, `channel`, `hash`, `malformed`, `advert`, `path`, `sender`,
`text` un `age`. `filter stats top` rāda to mezglu ID pirmo baitu, kuru dēļ atmests
visvairāk. Šis baits ir vienāds daudziem mezgliem.
`filter stats air` rāda ētera laiku, ko tavs retranslators ietaupījis, nepārsūtot šīs
paketes.

Skaitītāji atkal sākas no 0 pēc pārstartēšanas un pēc `clear stats`.
