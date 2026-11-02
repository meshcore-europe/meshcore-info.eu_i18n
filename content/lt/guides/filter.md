---
title: Paketų filtras
lead: 'Neleisk savo retransliatoriui perduoti šiukšlių: užtvindymų iš toli, nesustojančio boto, triukšmingo kanalo. Pirma išbandyk nustatymą, tada jį įjunk.'
description: 'DMC retransliatoriaus programinės įrangos paketų filtras: ką jis atmeta, paruošti nustatymai įprastam ir apkrautam retransliatoriui, visos filtro komandos su numatytosiomis reikšmėmis ir kaip pamatyti, ką jis atmetė.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'b07d39a8'
  seeded: '2026-11-02'
  fields: {title: '20a3ef1f', lead: 'd948682d', description: 'a8c57a9f'}
  sections: ['d06c9ddd', 'b1d9a8d1', '2dd3448d', 'ee64176e', 'a3cb880e', '09b568f0', 'a1a4fb68', '95fe64ae', 'dbac19c3', '05123b18', '3fa1bb28', 'e98b2285']
  blocks: ['b6231504', 'c66e4d9a', 'c0502fb4', 'fa699506', 'f7008037', '3acbb97b', '5e55d14c', 'bd024580', '68c8a4b1', '119fc5b9', '61804e40', '2fa7ebe8', '0610128b', 'a3cb880e', '0e6268be', 'e6d77222', 'f50be141', '2a1ae00c', '095e165f', 'd96efc68', 'b8a89bea', 'a29d0e87', 'c69ba7d1', 'f553d783', '1a83fda3', 'b6f87585', '64e2bbfa', 'dc79ca3a', '6ed9acff', 'd3701ccc', 'd4a25061', '22092611', '9184f977', 'f70c9e55', 'b2f0d9cb', 'c7b214c1', 'e8da9f3e', '0742c6c4', '7f2f59ae', '2789fc6d', 'ae920329', '7dd6f173', 'e1ca9ac7', 'ac11c47b', 'ec7913ae']
---

Retransliatorius (mazgas, kuris perduoda žinutes toliau) pakartoja viską, ką girdi.
Apkrautame tinkle tarp to pasitaiko ir šiukšlių. Botas rašo kas minutę. Vienas mazgas
kas kelias minutes vėl siunčia savo skelbimą (advert), pasisveikinimą, pagal kurį jį randa kiti.
Atkeliauja žinutės, įveikusios pusę šalies. Kiekvienas pakartojimas atima eterio laiką
iš visų aplink tave. Su paketų filtru tavo retransliatorius tokį srautą atmeta ir
toliau nebeperduoda. Kas pirmiausia užtvindo tavo tinklą ir kas dar padeda be filtro,
sužinosi puslapyje [Padaryk tinklą atsparų](/guides/resilient/).

{{< callout type="warning" >}}
Paketų filtras yra **DMC retransliatoriaus programinės įrangos** dalis. Tai
[Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore) versija retransliatoriams.
Standartinis MeshCore paketų filtro neturi. Jame yra `region denyf *` ir
`set flood.max.unscoped`, aprašyti puslapyje [CLI komandos](/guides/cli/). Šis
vadovas remiasi 2026 m. spalio 19 d. kūrimo versija 1.18.0 `ecfb2d4`. Stabilioje
1.17.1 versijoje yra tik šuolių, srauto, kanalų, maišos ir sugadintų žinučių filtrai.
Bandomojo režimo (dry-run) joje taip pat nėra.
{{< /callout >}}

## Ką daro filtras {#what}

Filtras tikrina tik tuos paketus, kuriuos tavo retransliatorius perduoda užtvindymu
(siunčia visiems mazgams ryšio zonoje). Jis neliečia to, ką tavo retransliatorius siunčia
pats, ir paketų, keliaujančių žinomu maršrutu iki vieno mazgo. Tiesioginės žinutės ir
užklausos tavo kontaktams ir iš jų taip pat praeina. Filtras gali atmesti:

- paketus, kurie jau perėjo tiek retransliatorių (šuolių), kiek leidi konkrečiam
  paketų tipui;
- daugiau vieno tipo paketų per minutę, nei leidi;
- skelbimą iš mazgo, kuris jau skelbėsi per pastarąsias valandas;
- žinutes kanale, kurį blokuoji;
- viską, kas atėjo per vieną tavo blokuojamą retransliatorių;
- grupines žinutes nuo vieno siuntėjo arba su vienu žodžiu, visas arba tik dalį;
- sugadintas grupines žinutes arba senesnes, nei leidi.

Filtras yra **išjungtas**, kol pats jo neįjungi. Jį nustatai komandomis. Rašyk jas per USB
šios svetainės [nuosekliojoje konsolėje](/firmware/console/). Arba siųsk jas iš
MeshCore programėlės, kaip aprašyta [retransliatoriaus vadove](/repeater-guide/#config).

## Kur gauti programinę įrangą {#firmware}

Įrašyk **DutchMeshCore Repeater** įrašymo įrankiu, kurį rasi
[DutchMeshCore Toolbox](https://toolbox.dutchmeshcore.nl/). Tokį patį filtrą turi ir
stebėtojo programinė įranga iš puslapio [MQTT tavo stebėtojui](/guides/mqtt/).

## Pirma išbandyk {#dryrun}

Bandomuoju režimu (dry-run) filtras skaičiuoja kiekvieną paketą, kurį atmestų, bet vis tiek jį
perduoda. Taip gali parinkti nustatymą, kol filtras dar nieko neatmeta:

```text
filter on
filter dryrun on
```

Kol bandomasis režimas įjungtas, komandos `filter` būsenos eilutė baigiasi `(dry-run)`. Skaitikliai
rodo, ką filtras būtų atmetęs. Palik jį veikti parą, tada peržiūrėk skaičius
(žr. [Ką jis atmetė](#stats)). Kai skaičiai atrodo tinkami, įjunk tikrą atmetimą:

```text
filter dryrun off
```

## Rekomenduojami nustatymai {#configs}

### Įprastas retransliatorius {#typical}

```text
filter on
filter malformed on
filter rate 05 20 60
filter rate 02 5 60
filter hops 05 32
```

Praeina iki 20 grupinių žinučių per minutę ir iki 5 tiesioginių žinučių per minutę.
Sugadintos grupinės žinutės atmetamos. Pačios programinės įrangos įprasti nustatymai
leidžia 20 tiesioginių žinučių per minutę. Šiame puslapyje naudojame 5: tiek
programinė įranga pataria nuo tiesioginių žinučių užtvindymo 2026 m. liepą.

### Apkrautas retransliatorius {#busy}

Šie nustatymai skirti retransliatoriui aukštoje vietoje, kuris girdi visą regioną, arba
užtvindytam retransliatoriui:

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

Taip perpus sumažini grupinių žinučių ir skelbimų skaičių, o kiekvieno mazgo skelbimą
perduodi kartą per parą. Filtras atmeta žinutes, jau perėjusias 16 retransliatorių. Po
paleidimo iš naujo praeina po vieną kiekvieno mazgo skelbimą. Pačios programinės įrangos
dokumentacijoje čia dar nustatoma `filter hash 2`. Šiame puslapyje to nenaudojame
(priežastį rasi skyriuje [Visi nustatymai](#settings)).

### Užblokuok triukšmingą kanalą {#channel}

```text
filter channel add #bot
```

Tavo retransliatorius kanalą vis dar girdi. Tačiau kitiems retransliatoriams ir kompanionams
(mazgams, iš kurių žmonės rašo žinutes) jo nebeperduoda. Gali užblokuoti iki 16 kanalų.

### Pristabdyk vieną siuntėją {#sender}

Tai tinka botui, kuris per dažnai rašo kanale, kurį nori palikti:

```text
filter watch add #test
filter sender add Bob 60
```

Dabar Bob žinutės Public kanale ir `#test` praeina kartą per minutę, o kitos atmetamos.
Filtras tikrina žinutėje esantį vardą, todėl vardą pakeitęs siuntėjas filtrą apeina.

### Užblokuok vieną retransliatorių maršrute {#path}

Kai šiukšlės ateina per vieną retransliatorių, užblokuok jo prefiksą: pirmąją jo ID dalį
šešioliktainiu formatu (hex). Tam reikia 1.18 kūrimo versijos, nes 1.17.1 versijoje
maršruto filtro nėra.

```text
filter path add a1b2
filter path list
filter stats path
```

`filter path list` rodo tavo blokuojamus prefiksus, o `filter stats path` rodo, kiek atmetė
kiekvienas iš jų. Su `filter path remove a1b2` srautą vėl praleidi.
Trumpas prefiksas, pavyzdžiui, `a1`, blokuoja ir visus kitus retransliatorius, kurių ID
prasideda `a1`. Naudok kuo ilgesnį prefiksą. Gali užblokuoti iki 8 prefiksų.

## Visi nustatymai {#settings}

Paketų tipus nurodai numeriais. Retransliatoriuje komanda `filter types` rodo tuos pačius
numerius su programinės įrangos pavadinimais, pavyzdžiui, `TXT_MSG` ir `GRP_TXT`:

| Numeris | Tipas | Numeris | Tipas |
| --- | --- | --- | --- |
| `00` | užklausa | `06` | grupiniai duomenys |
| `01` | atsakymas | `07` | anoniminė užklausa |
| `02` | tiesioginė žinutė | `08` | maršrutas |
| `03` | patvirtinimas | `09` | sekimas |
| `04` | skelbimas | `10` | kelių dalių paketas |
| `05` | grupinė žinutė | `11` | valdymas |

| Komanda | Ką ji daro | Pradinė reikšmė |
| --- | --- | --- |
| `filter on` / `filter off` | Įjungia arba išjungia filtrą. | išjungta |
| `filter dryrun on` / `off` | Skaičiuoja atmetimus, bet vis tiek viską perduoda. | išjungta |
| `filter hops <type> <max>` | Atmeta tipą, kuris jau perėjo tiek retransliatorių, nuo 0 iki 64. | 32 grupinėms žinutėms, 8 kitiems tipams |
| `filter rate <type> <limit> <secs> [soft]` | Perduoda ne daugiau kaip `limit` vieno tipo paketų per `secs`. Su `soft` perdavimas palaipsniui mažėja nuo `soft` iki `limit`. `0` išjungia ribą. | 20 per 60 s tiesioginėms ir grupinėms žinutėms, 10 skelbimams, 5 kitiems tipams |
| `filter advert <hours>` | Perduoda kiekvieno mazgo skelbimą kartą per tiek valandų, iki 720. | 0 (išjungta) |
| `filter channel add <#name>` | Nutraukia kanalo perdavimą. | nėra |
| `filter path add <hex>` | Atmeta viską, kas atėjo per retransliatorių su šiuo prefiksu, nuo 2 iki 8 šešioliktainių skaitmenų. | nėra |
| `filter sender add <name> [secs] [prob]` | Atmeta siuntėjo grupines žinutes Public ir stebimuose kanaluose. `Bot*` atitinka kiekvieną vardą, prasidedantį Bot. | nėra |
| `filter text add <word> [secs] [prob]` | Atmeta grupines žinutes su nurodytu žodžiu Public ir stebimuose kanaluose. `^word` atitinka tik pradžioje. | nėra |
| `filter watch add <#name>` | Leidžia siuntėjų ir teksto taisyklėms skaityti ir šį kanalą, iki 4 kanalų. Public skaitomas visada. | Public |
| `filter malformed on` / `off` | Atmeta Public žinutes, kurios yra tuščios, sugadintos arba kurių data skiriasi daugiau kaip savaite (datą filtras tikrina tik nustačius laikrodį). | išjungta |
| `filter age <minutes>` / `off` | Atmeta už šią ribą senesnes grupines žinutes Public ir stebimuose kanaluose, nuo 1 iki 10080. | išjungta |
| `filter hash <bytes>` | Atmeta paketus, kurių maršruto ID trumpesnis už šią reikšmę, nuo 1 iki 3. | 1 |
| `filter reset` | Grąžina visiems nustatymams numatytąsias reikšmes. | |

Kiekviena `add` komanda turi `remove` ir `list`, pavyzdžiui, `filter channel remove #bot`.
Siuntėjų ir teksto taisyklėse `secs` praleidžia vieną žinutę per tiek sekundžių.
`prob` taiko taisyklę tik tokiai atitikčių daliai, nuo 1 iki 100. Gali turėti iki 8
siuntėjų ir 8 teksto taisyklių. Varduose ir žodžiuose didžiosios ir mažosios raidės skiriasi.
Vardas gali turėti iki 15 ženklų, žodis iki 23.

Du nustatymai atmeta daugiau, nei gali tikėtis:

- `filter hash 2` atmeta beveik visą srautą. Pagal numatytuosius nustatymus mazgai siunčia 1 baito
  maršruto ID.
- `filter age` remiasi tavo retransliatoriaus laikrodžiu. Nustatyk jį iš programėlės komanda
  `clock sync`, patikrink komanda `clock` ir pradėk nuo didelės atsargos: `filter age 60`.

Po paleidimo iš naujo visi nustatymai išlieka.

## Ką jis atmetė {#stats}

`filter` rodo sumas pagal priežastį:

```text
> Filter on: Blocked [ Hops: 3 | Rate: 12 | Channel: 1 | Hash: 0 | Malformed: 2 ]
```

`filter stats <topic>` rodo vieno nustatymo išsamius duomenis. Temos yra
`hops`, `rate`, `channel`, `hash`, `malformed`, `advert`, `path`, `sender`,
`text` ir `age`. `filter stats top` rodo pirmąjį ID baitą tų mazgų, dėl kurių atmesta daugiausia paketų.
Tą patį baitą turi daug mazgų.
`filter stats air` rodo, kiek eterio laiko sutaupė tavo retransliatorius, neperduodamas šių paketų.

Po paleidimo iš naujo ir po `clear stats` skaitikliai vėl pradeda nuo 0.
