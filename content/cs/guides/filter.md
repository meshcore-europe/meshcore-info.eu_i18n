---
title: Filtr paketů
lead: 'Zabraň svému repeateru, aby šířil balast: floody z velké dálky, bota, který nikdy nepřestane, hlučný kanál. Nastavení si nejdřív vyzkoušej a pak ho zapni.'
description: 'Filtr paketů ve firmwaru DMC pro repeatery: co zahazuje, hotová nastavení pro běžný a vytížený repeater, všechny příkazy filtru s výchozími hodnotami a jak zjistíš, co zahodil.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'b07d39a8'
  seeded: '2026-10-31'
  fields: {title: '20a3ef1f', lead: 'd948682d', description: 'a8c57a9f'}
  sections: ['d06c9ddd', 'b1d9a8d1', '2dd3448d', 'ee64176e', 'a3cb880e', '09b568f0', 'a1a4fb68', '95fe64ae', 'dbac19c3', '05123b18', '3fa1bb28', 'e98b2285']
  blocks: ['b6231504', 'c66e4d9a', 'c0502fb4', 'fa699506', 'f7008037', '3acbb97b', '5e55d14c', 'bd024580', '68c8a4b1', '119fc5b9', '61804e40', '2fa7ebe8', '0610128b', 'a3cb880e', '0e6268be', 'e6d77222', 'f50be141', '2a1ae00c', '095e165f', 'd96efc68', 'b8a89bea', 'a29d0e87', 'c69ba7d1', 'f553d783', '1a83fda3', 'b6f87585', '64e2bbfa', 'dc79ca3a', '6ed9acff', 'd3701ccc', 'd4a25061', '22092611', '9184f977', 'f70c9e55', 'b2f0d9cb', 'c7b214c1', 'e8da9f3e', '0742c6c4', '7f2f59ae', '2789fc6d', 'ae920329', '7dd6f173', 'e1ca9ac7', 'ac11c47b', 'ec7913ae']
---

Repeater (uzel, který předává zprávy dál) opakuje všechno, co zachytí.
Na vytížené mesh síti to zahrnuje i balast. Bot posílá zprávu každou minutu.
Jeden uzel vysílá svůj advert, ohlášení, podle kterého ho ostatní najdou,
znovu každých pár minut. Přicházejí zprávy, které prošly přes půl země. Každé
opakování bere vysílací čas všem kolem tebe. S filtrem paketů tvůj repeater
takový provoz zahodí, místo aby ho předal dál. Co tvou mesh síť zahlcuje
a co kromě filtru pomáhá, zjistíš nejdřív v návodu
[Odolná mesh síť](/guides/resilient/).

{{< callout type="warning" >}}
Filtr paketů je součástí **firmwaru DMC pro repeatery**, tedy repeaterové
verze [Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore). Běžný
MeshCore filtr paketů nemá. Má `region denyf *` a
`set flood.max.unscoped`, viz stránka [Příkazy CLI](/guides/cli/). Tento
návod vychází z vývojové verze 1.18.0 `ecfb2d4` z 19. října 2026. Stabilní
verze 1.17.1 má jen filtry skoků, četnosti, kanálů, hashe a poškozených zpráv.
Nemá ani zkušební režim (dry-run).
{{< /callout >}}

## Co filtr dělá {#what}

Filtr kontroluje jen pakety, které tvůj repeater předává floodem (rozesílá
je všem uzlům v dosahu). Nikdy se nedotkne toho, co tvůj repeater vysílá
sám, ani paketů, které jdou známou cestou k jednomu uzlu. Projdou i přímé
zprávy a požadavky od tvých kontaktů a k nim. Filtr umí zahodit:

- pakety, které už prošly tolika repeatery (skoky), kolik povolíš, zvlášť pro
  každý typ paketu;
- víc paketů jednoho typu za minutu, než povolíš;
- advert od uzlu, který se už ohlásil v posledních hodinách;
- zprávy na kanálu, který zablokuješ;
- všechno, co prošlo jedním repeaterem, který zablokuješ;
- skupinové zprávy od jednoho odesílatele nebo s jedním slovem, případně jen
  část z nich;
- skupinové zprávy, které jsou poškozené nebo starší, než povolíš.

Filtr je **vypnutý**, dokud ho nezapneš. Nastavuješ ho příkazy. Zadáš je
přes USB v [sériové konzoli](/firmware/console/) na tomto webu. Nebo je
pošleš z aplikace MeshCore, jak popisuje
[návod k repeateru](/repeater-guide/#config).

## Jak získat firmware {#firmware}

Nahraj **DutchMeshCore Repeater** z flasheru v
[DutchMeshCore Toolbox](https://toolbox.dutchmeshcore.nl/). Firmware pro
observer z návodu [MQTT na tvém observeru](/guides/mqtt/) má stejný filtr.

## Nejdřív to vyzkoušej {#dryrun}

V režimu dry-run filtr spočítá každý paket, který by zahodil, ale přesto ho
předá dál. Takhle si nastavení vyladíš, než začne cokoli zahazovat:

```text
filter on
filter dryrun on
```

Když je dry-run zapnutý, stavový řádek příkazu `filter` končí `(dry-run)`.
Počty ukazují, co by filtr zahodil. Nech ho běžet jeden den a pak se na ně
podívej (viz [Co filtr zahodil](#stats)). Až budou čísla vypadat správně,
zapni ho naostro:

```text
filter dryrun off
```

## Doporučená nastavení {#configs}

### Běžný repeater {#typical}

```text
filter on
filter malformed on
filter rate 05 20 60
filter rate 02 5 60
filter hops 05 32
```

Skupinové zprávy projdou až 20 za minutu, přímé zprávy až 5 za minutu.
Poškozené skupinové zprávy filtr zahodí. Vlastní běžné nastavení firmwaru
povoluje 20 přímých zpráv za minutu. Tato stránka používá 5, které firmware
doporučuje od floodu přímých zpráv v červenci 2026.

### Vytížený repeater {#busy}

Pro repeater na vysokém místě, který slyší celý region, nebo pro zahlcený
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

Toto nastavení sníží skupinové zprávy a adverty na polovinu. Advert každého
uzlu projde jednou denně. Zprávy, které už prošly 16 repeatery, filtr zahodí.
Po restartu projde od každého uzlu jeden advert. Dokumentace firmwaru tu
nastavuje i `filter hash 2`. Tato stránka ho vynechává (proč, viz
[Všechna nastavení](#settings)).

### Zablokuj hlučný kanál {#channel}

```text
filter channel add #bot
```

Tvůj repeater kanál dál slyší. Už ho ale nepředává ostatním repeaterům
a companionům (uzlům, ze kterých lidé píšou zprávy). Nejvýš 16 kanálů.

### Přibrzdi jednoho odesílatele {#sender}

Bot, který píše příliš často na kanálu, o který nechceš přijít:

```text
filter watch add #test
filter sender add Bob 60
```

Bobovy zprávy na kanálu Public a `#test` teď projdou jednou za minutu.
Zbytek filtr zahodí. Filtr porovnává jméno ve zprávě, takže odesílatel,
který se přejmenuje, projde.

### Zablokuj jeden repeater před sebou {#path}

Když balast přichází přes jeden repeater, zablokuj jeho prefix: začátek
jeho ID v šestnáctkové soustavě (hex). Potřebuješ k tomu vývojovou verzi
1.18. Verze 1.17.1 filtr cesty nemá.

```text
filter path add a1b2
filter path list
filter stats path
```

`filter path list` ukáže prefixy, které blokuješ, a `filter stats path`, kolik
každý z nich zahodil. Příkazem `filter path remove a1b2` ho zase pustíš.
Krátký prefix jako `a1` zablokuje i každý další repeater, jehož ID začíná
na `a1`. Použij co nejdelší prefix. Nejvýš 8 prefixů.

## Všechna nastavení {#settings}

Typy paketů se zadávají číslem. Na repeateru ukáže `filter types` stejná
čísla s názvy z firmwaru, například `TXT_MSG` a `GRP_TXT`:

| Číslo | Typ | Číslo | Typ |
| --- | --- | --- | --- |
| `00` | požadavek | `06` | skupinová data |
| `01` | odpověď | `07` | anonymní požadavek |
| `02` | přímá zpráva | `08` | cesta |
| `03` | potvrzení | `09` | trasování |
| `04` | advert | `10` | vícedílná zpráva |
| `05` | skupinová zpráva | `11` | řízení |

| Příkaz | Co dělá | Výchozí hodnota |
| --- | --- | --- |
| `filter on` / `filter off` | Zapne nebo vypne filtr. | vypnuto |
| `filter dryrun on` / `off` | Počítá zahozené pakety, ale dál všechno předává. | vypnuto |
| `filter hops <type> <max>` | Zahodí typ, který už prošel tolika repeatery, 0 až 64. | 32 pro skupinové zprávy, 8 pro ostatní |
| `filter rate <type> <limit> <secs> [soft]` | Předá nejvýš `limit` paketů daného typu za `secs`. Se `soft` předávání postupně ubývá od `soft` do `limit`. `0` limit vypne. | 20 za 60 s pro přímé a skupinové zprávy, 10 pro adverty, 5 pro ostatní |
| `filter advert <hours>` | Předá advert každého uzlu jednou za tolik hodin, nejvýš 720. | 0 (vypnuto) |
| `filter channel add <#name>` | Přestane předávat kanál. | žádné |
| `filter path add <hex>` | Zahodí všechno, co prošlo repeaterem s tímto prefixem, 2 až 8 hex číslic. | žádné |
| `filter sender add <name> [secs] [prob]` | Zahodí skupinové zprávy od odesílatele na kanálu Public a sledovaných kanálech. `Bot*` odpovídá každému jménu, které začíná na Bot. | žádné |
| `filter text add <word> [secs] [prob]` | Zahodí skupinové zprávy se slovem na kanálu Public a sledovaných kanálech. `^word` odpovídá jen na začátku. | žádné |
| `filter watch add <#name>` | Pravidla pro odesílatele a text čtou i tento kanál, nejvýš 4. Public čtou vždy. | Public |
| `filter malformed on` / `off` | Zahodí zprávy na kanálu Public, které jsou prázdné, poškozené nebo mají datum posunuté o víc než týden (kontrola data čeká, až budou hodiny nastavené). | vypnuto |
| `filter age <minutes>` / `off` | Zahodí skupinové zprávy starší než tato hodnota na kanálu Public a sledovaných kanálech, 1 až 10080. | vypnuto |
| `filter hash <bytes>` | Zahodí pakety s kratším ID cesty, než je tato hodnota, 1 až 3. | 1 |
| `filter reset` | Vrátí všechna nastavení na výchozí hodnoty. | |

Každé `add` má i `remove` a `list`, například `filter channel remove #bot`.
V pravidlech pro odesílatele a text propustí `secs` jednu zprávu za tolik
sekund. `prob` použije pravidlo jen na takový podíl shod, 1 až 100. Nejvýš 8
pravidel pro odesílatele a 8 pro text. Jména a slova rozlišují velká a malá
písmena. Jméno má nejvýš 15 znaků, slovo nejvýš 23.

Dvě nastavení zahodí víc, než možná čekáš:

- `filter hash 2` zahodí skoro všechen provoz. Uzly standardně posílají
  1bajtová ID cesty.
- `filter age` spoléhá na hodiny tvého repeateru. Nastav je příkazem
  `clock sync` z aplikace, zkontroluj je příkazem `clock` a začni velkoryse:
  `filter age 60`.

Všechna nastavení zůstanou zachovaná i po restartu.

## Co filtr zahodil {#stats}

`filter` ukáže součty podle důvodu:

```text
> Filter on: Blocked [ Hops: 3 | Rate: 12 | Channel: 1 | Hash: 0 | Malformed: 2 ]
```

`filter stats <topic>` ukáže podrobnosti k jednomu nastavení. Témata jsou
`hops`, `rate`, `channel`, `hash`, `malformed`, `advert`, `path`, `sender`,
`text` a `age`. `filter stats top` ukáže první bajt ID uzlů, kvůli kterým
filtr zahodil nejvíc paketů. Ten bajt sdílí mnoho uzlů.
`filter stats air` ukáže vysílací čas, který tvůj repeater ušetřil, protože
tyto pakety nepředal dál.

Počítadla začínají znovu od 0 po restartu a po příkazu `clear stats`.
