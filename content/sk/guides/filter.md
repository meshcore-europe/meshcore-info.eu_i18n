---
title: Filter paketov
lead: 'Zabráň repeatru, aby šíril nezmysly: floody z veľkej diaľky, bota, ktorý nikdy neprestane, alebo hlučný kanál. Nastavenie najprv vyskúšaj a potom ho zapni.'
description: 'Filter paketov vo firmvéri DMC pre repeatre: čo zahadzuje, hotové nastavenia pre bežný a vyťažený repeater, všetky príkazy filtra s predvolenými hodnotami a spôsob, ako zistíš, čo filter zahodil.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'b07d39a8'
  seeded: '2026-11-02'
  fields: {title: '20a3ef1f', lead: 'd948682d', description: 'a8c57a9f'}
  sections: ['d06c9ddd', 'b1d9a8d1', '2dd3448d', 'ee64176e', 'a3cb880e', '09b568f0', 'a1a4fb68', '95fe64ae', 'dbac19c3', '05123b18', '3fa1bb28', 'e98b2285']
  blocks: ['b6231504', 'c66e4d9a', 'c0502fb4', 'fa699506', 'f7008037', '3acbb97b', '5e55d14c', 'bd024580', '68c8a4b1', '119fc5b9', '61804e40', '2fa7ebe8', '0610128b', 'a3cb880e', '0e6268be', 'e6d77222', 'f50be141', '2a1ae00c', '095e165f', 'd96efc68', 'b8a89bea', 'a29d0e87', 'c69ba7d1', 'f553d783', '1a83fda3', 'b6f87585', '64e2bbfa', 'dc79ca3a', '6ed9acff', 'd3701ccc', 'd4a25061', '22092611', '9184f977', 'f70c9e55', 'b2f0d9cb', 'c7b214c1', 'e8da9f3e', '0742c6c4', '7f2f59ae', '2789fc6d', 'ae920329', '7dd6f173', 'e1ca9ac7', 'ac11c47b', 'ec7913ae']
---

Repeater (uzol, ktorý posúva správy ďalej) opakuje všetko, čo zachytí.
V rušnej sieti je v tom aj balast. Bot prispieva každú minútu. Ďalší uzol
každých pár minút znova vysiela svoj advert, teda pozdrav, podľa ktorého ho ostatní nájdu.
Prichádzajú správy, ktoré precestovali pol krajiny. Každé opakovanie berie
vysielací čas všetkým okolo teba. Vďaka filtru paketov tvoj repeater takú prevádzku
zahodí a neposunie ju ďalej. Najprv zisti, čo tvoju sieť zaplavuje a čo okrem filtra pomáha:
pozri návod [Odolná sieť](/guides/resilient/).

{{< callout type="warning" >}}
Filter paketov je súčasťou **firmvéru DMC pre repeatre**, teda repeatrovej
verzie [Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore). Štandardný
MeshCore filter paketov nemá. Má príkazy `region denyf *` a
`set flood.max.unscoped`, ktoré nájdeš na stránke [príkazov CLI](/guides/cli/).
Tento návod vychádza z vývojovej verzie 1.18.0 `ecfb2d4` z 19. októbra 2026. Stabilná
verzia 1.17.1 má iba filtre hopov, rýchlosti, kanálov, hashu a poškodených správ.
Nemá ani dry-run.
{{< /callout >}}

## Čo filter robí {#what}

Filter kontroluje iba pakety, ktoré tvoj repeater posúva floodingom (vysiela ich
všetkým uzlom v dosahu). Nikdy sa nedotkne toho, čo tvoj repeater vysiela sám,
ani paketov, ktoré idú známou trasou k jednému uzlu. Prejdú aj priame správy a
požiadavky od tvojich kontaktov a pre ne. Filter môže zahodiť:

- pakety, ktoré už prešli toľkými repeatrami (hopmi), koľko povolíš, zvlášť
  pre každý typ paketu;
- viac paketov jedného typu za minútu, než povolíš;
- advert od uzla, ktorý už advert vyslal počas posledných hodín;
- správy na kanáli, ktorý zablokuješ;
- všetko, čo prišlo cez jeden repeater, ktorý zablokuješ;
- skupinové správy od jedného odosielateľa alebo s jedným slovom, prípadne iba niektoré z nich;
- skupinové správy, ktoré sú poškodené alebo staršie, než povolíš.

Filter je **vypnutý**, kým ho nezapneš. Nastavuješ ho príkazmi. Zadaj ich cez USB
v [sériovej konzole](/firmware/console/) na tomto webe. Alebo ich pošli
z aplikácie MeshCore podľa [návodu na repeater](/repeater-guide/#config).

## Získaj firmvér {#firmware}

Nahraj **DutchMeshCore Repeater** pomocou flashera v
[DutchMeshCore Toolbox](https://toolbox.dutchmeshcore.nl/). Rovnaký filter má aj firmvér
pre observer z návodu [MQTT na tvojom observeri](/guides/mqtt/).

## Najprv to vyskúšaj {#dryrun}

V režime dry-run filter započíta každý paket, ktorý by zahodil, ale aj tak ho
posunie ďalej. Takto si nastavenie vyladíš skôr, než filter niečo zahodí:

```text
filter on
filter dryrun on
```

Keď je dry-run zapnutý, stavový riadok príkazu `filter` končí textom `(dry-run)`. Počítadlá
ukazujú, čo by filter zahodil. Nechaj ho bežať jeden deň a potom si ich prezri
(pozri [Čo filter zahodil](#stats)). Keď budú čísla vyzerať správne, filter naostro zapni:

```text
filter dryrun off
```

## Odporúčané konfigurácie {#configs}

### Bežný repeater {#typical}

```text
filter on
filter malformed on
filter rate 05 20 60
filter rate 02 5 60
filter hops 05 32
```

Prejde najviac 20 skupinových správ za minútu a najviac 5 priamych správ za minútu.
Poškodené skupinové správy filter zahodí. Bežná konfigurácia samotného firmvéru povoľuje
20 priamych správ za minútu. Táto stránka používa hodnotu 5, ktorú firmvér odporúča
od záplavy priamych správ v júli 2026.

### Vyťažený repeater {#busy}

Pre repeater na vysokom mieste, ktorý počuje celý región, alebo pre zaplavený
repeater:

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

Toto nastavenie znižuje počet skupinových správ a advertov na polovicu a advert každého uzla
posunie raz denne. Zahadzuje správy, ktoré už prešli 16 repeatrami. Po reštarte
prejde od každého uzla jeden advert. Dokumentácia samotného firmvéru tu nastavuje aj
`filter hash 2`. Táto stránka ho vynecháva (dôvod nájdeš v časti
[Všetky nastavenia](#settings)).

### Zablokuj hlučný kanál {#channel}

```text
filter channel add #bot
```

Tvoj repeater kanál stále počuje. Už ho však neposúva ďalším repeatrom ani
companionom (uzlom, z ktorých ľudia píšu správy). Zablokovať môžeš najviac 16 kanálov.

### Spomaľ jedného odosielateľa {#sender}

Bot píše príliš často na kanáli, ktorý si chceš nechať:

```text
filter watch add #test
filter sender add Bob 60
```

Bobove správy na kanáli Public a na `#test` teraz prejdú raz za minútu. Ostatné
filter zahodí. Filter porovnáva meno v správe, takže odosielateľ ho po premenovaní obíde.

### Zablokuj jeden repeater na trase {#path}

Keď balast prichádza cez jeden repeater, zablokuj jeho prefix: prvú časť
jeho ID v šestnástkovej sústave (hex). Potrebuješ na to vývojovú verziu 1.18. Verzia 1.17.1
filter trasy nemá.

```text
filter path add a1b2
filter path list
filter stats path
```

`filter path list` zobrazí prefixy, ktoré blokuješ, a `filter stats path` ukáže,
koľko každý z nich zahodil. `filter path remove a1b2` tento prefix znova prepustí.
Krátky prefix ako `a1` zablokuje aj každý ďalší repeater, ktorého ID začína na `a1`.
Použi čo najdlhší prefix. Zablokovať môžeš najviac 8 prefixov.

## Všetky nastavenia {#settings}

Typy paketov sa zadávajú číslom. Na repeatri `filter types` zobrazí rovnaké
čísla s názvami z firmvéru, napríklad `TXT_MSG` a `GRP_TXT`:

| Číslo | Typ | Číslo | Typ |
| --- | --- | --- | --- |
| `00` | požiadavka | `06` | skupinové dáta |
| `01` | odpoveď | `07` | anonymná požiadavka |
| `02` | priama správa | `08` | trasa |
| `03` | potvrdenie | `09` | trasovanie |
| `04` | advert | `10` | viacdielny paket |
| `05` | skupinová správa | `11` | riadiaci paket |

| Príkaz | Čo robí | Predvolene |
| --- | --- | --- |
| `filter on` / `filter off` | Zapne alebo vypne filter. | vypnuté |
| `filter dryrun on` / `off` | Počíta zahodenia, ale všetko posúva ďalej. | vypnuté |
| `filter hops <type> <max>` | Zahodí pakety daného typu, ktoré už prešli týmto počtom repeatrov, 0 až 64. | 32 pre skupinové správy, 8 pre ostatné |
| `filter rate <type> <limit> <secs> [soft]` | Za `secs` prepustí najviac `limit` paketov daného typu. So `soft` sa prepúšťanie postupne znižuje od `soft` po `limit`. `0` limit vypne. | 20 za 60 s pre priame a skupinové správy, 10 pre adverty, 5 pre ostatné |
| `filter advert <hours>` | Advert každého uzla prepustí raz za tento počet hodín, najviac 720. | 0 (vypnuté) |
| `filter channel add <#name>` | Prestane posúvať kanál ďalej. | žiadne |
| `filter path add <hex>` | Zahodí všetko, čo prišlo cez repeater s týmto prefixom, 2 až 8 hex číslic. | žiadne |
| `filter sender add <name> [secs] [prob]` | Zahodí skupinové správy od odosielateľa na kanáli Public a na sledovaných kanáloch. `Bot*` zodpovedá každému menu, ktoré začína na Bot. | žiadne |
| `filter text add <word> [secs] [prob]` | Zahodí skupinové správy s daným slovom na kanáli Public a na sledovaných kanáloch. `^word` hľadá zhodu iba na začiatku. | žiadne |
| `filter watch add <#name>` | Pravidlá pre odosielateľov a text budú čítať aj tento kanál, najviac 4. Public čítajú vždy. | Public |
| `filter malformed on` / `off` | Zahodí správy na kanáli Public, ktoré sú prázdne, poškodené alebo majú dátum posunutý o viac než týždeň (kontrola dátumu čaká na nastavenie hodín). | vypnuté |
| `filter age <minutes>` / `off` | Zahodí skupinové správy staršie než táto hodnota na kanáli Public a na sledovaných kanáloch, 1 až 10080. | vypnuté |
| `filter hash <bytes>` | Zahodí pakety s kratším ID trasy, než je táto hodnota, 1 až 3. | 1 |
| `filter reset` | Vráti všetky nastavenia na predvolené hodnoty. | |

Každé `add` má aj `remove` a `list`, napríklad `filter channel remove #bot`.
V pravidlách pre odosielateľov a text `secs` prepustí jednu správu za daný počet sekúnd.
`prob` použije pravidlo iba na tento podiel zhôd, 1 až 100. Môžeš mať najviac 8
pravidiel pre odosielateľov a 8 pravidiel pre text. V menách a slovách sa rozlišujú malé a veľké
písmená. Meno má najviac 15 znakov, slovo najviac 23.

Dve nastavenia zahadzujú viac, než možno čakáš:

- `filter hash 2` zahodí takmer všetku prevádzku. Uzly predvolene posielajú
  1-bajtové ID trasy.
- `filter age` sa spolieha na hodiny tvojho repeatra. Nastav ich z aplikácie príkazom
  `clock sync`, skontroluj ich príkazom `clock` a začni so štedrou hodnotou: `filter age 60`.

Všetky nastavenia zostanú zachované aj po reštarte.

## Čo filter zahodil {#stats}

`filter` zobrazí súčty podľa dôvodu:

```text
> Filter on: Blocked [ Hops: 3 | Rate: 12 | Channel: 1 | Hash: 0 | Malformed: 2 ]
```

`filter stats <topic>` zobrazí podrobnosti k jednému nastaveniu. Témy sú
`hops`, `rate`, `channel`, `hash`, `malformed`, `advert`, `path`, `sender`,
`text` a `age`. `filter stats top` zobrazí prvý bajt ID uzlov, za ktorými je
najviac zahodení. Tento bajt má spoločný veľa uzlov.
`filter stats air` ukáže vysielací čas, ktorý tvoj repeater ušetril tým, že tieto
pakety neposunul ďalej.

Počítadlá začnú znova od 0 po reštarte a po príkaze `clear stats`.
