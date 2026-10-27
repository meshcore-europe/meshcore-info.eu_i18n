---
title: Filtr paketů
lead: 'Zabraň svému repeateru v šíření balastu: floodům z velké dálky, botovi, který nikdy nepřestane, hlučnému kanálu. Nastavení nejdřív vyzkoušej, pak ho zapni.'
description: 'Filtr paketů ve firmwaru DMC pro repeatery: co zahazuje, hotová nastavení pro běžný a vytížený repeater, každý příkaz filtru s výchozí hodnotou a jak se podívat, co zahodil.'
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '2bf23d24'
  seeded: '2026-10-26'
  fields: {title: '20a3ef1f', lead: 'd948682d', description: 'a8c57a9f'}
  sections: ['0625daa2', 'b1d9a8d1', '2dd3448d', 'ee64176e', 'a3cb880e', '09b568f0', 'a1a4fb68', '95fe64ae', 'dbac19c3', 'ffc3f3a0', '3fa1bb28', '09511608']
---

Repeater (uzel, který předává zprávy dál) opakuje všechno, co slyší.
Na vytíženém meshi k tomu patří i balast. Bot posílá příspěvek každou minutu.
Jeden uzel posílá svůj advert, pozdrav, díky kterému ho ostatní najdou,
znovu každých pár minut. Přicházejí zprávy, které urazily půl republiky.
Každé opakování bere vysílací čas všem kolem tebe. Filtr paketů umožní tvému
repeateru takový provoz zahodit místo toho, aby ho předával dál.

{{< callout type="warning" >}}
Filtr paketů je součástí **firmwaru DMC pro repeatery**, sestavení pro
repeatery od [Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore).
Standardní MeshCore filtr paketů nemá; má `region denyf *` a
`set flood.max.unscoped`, viz stránka [Příkazy CLI](/guides/cli/). Tento
návod vychází z vývojového sestavení 1.18.0 `ecfb2d4` z 19. října 2026.
Stabilní sestavení 1.17.1 má jen filtry hops, rate, channel, hash a malformed.
Nemá ani zkušební režim (dry-run).
{{< /callout >}}

## Co filtr dělá {#what}

Filtr se dívá jen na pakety, které tvůj repeater předává dál floodem
(posílá je každému uzlu v dosahu). Nikdy nesahá na to, co tvůj repeater
posílá sám, ani na pakety, které jdou po známé cestě k jednomu uzlu. Přímé
zprávy a požadavky od tvých kontaktů a k nim projdou také. Zahodit umí:

- pakety, které už prošly tolika repeatery (skoky), kolik dovolíš, podle
  typu paketu;
- více paketů jednoho typu, než dovolíš za minutu;
- advert od uzlu, který se v posledních hodinách už ohlásil;
- zprávy na kanálu, který blokuješ;
- všechno, co přišlo přes jeden repeater, který blokuješ;
- skupinové zprávy od jednoho odesílatele nebo s jedním slovem, nebo jen část z nich;
- skupinové zprávy, které jsou poškozené nebo starší, než dovolíš.

Filtr je **vypnutý**, dokud ho nezapneš. Nastavuješ ho příkazy. Zadávej je
přes USB v [sériové konzoli](/firmware/console/) na tomto webu. Nebo je
pošli z aplikace MeshCore, jak popisuje
[návod k repeateru](/repeater-guide/#config).

## Získej firmware {#firmware}

Nahraj **DutchMeshCore Repeater** pomocí flasheru v
[DutchMeshCore Toolbox](https://toolbox.dutchmeshcore.nl/). Firmware pro
observer ze stránky [MQTT na tvém observeru](/guides/mqtt/) má stejný filtr.

## Nejdřív to vyzkoušej {#dryrun}

Ve zkušebním režimu (dry-run) filtr počítá každý paket, který by zahodil,
ale přesto ho předá dál. Takto si nastavení vyladíš dřív, než něco zahodí:

```text
filter on
filter dryrun on
```

Dokud je zkušební režim zapnutý, stavový řádek příkazu `filter` končí na
`(dry-run)`. Počty ukazují, co by filtr zahodil. Nech ho běžet jeden den,
pak se na ně podívej (viz [Co zahodil](#stats)). Když čísla vypadají dobře,
filtr zapni naostro:

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

Skupinové zprávy projdou nejvýše 20 za minutu, přímé zprávy nejvýše 5 za
minutu a poškozené skupinové zprávy filtr zahodí. Vlastní běžné nastavení
firmwaru dovoluje 20 přímých zpráv za minutu. Tato stránka přebírá hodnotu 5,
kterou firmware radí od floodu přímých zpráv v červenci 2026.

### Vytížený repeater {#busy}

Pro repeater na vysokém stanovišti, který slyší celý region, nebo pro
repeater zahlcený floodem:

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

Toto sníží skupinové zprávy a adverty na polovinu a advert každého uzlu
předá jednou za den. Zprávy, které už prošly 16 repeatery, zahodí. Po
restartu projde od každého uzlu jeden advert. Vlastní dokumentace firmwaru
tu nastavuje i `filter hash 2`; tato stránka ho vynechává (proč, viz
[Každé nastavení](#settings)).

### Zablokuj hlučný kanál {#channel}

```text
filter channel add #bot
```

Tvůj repeater kanál dál slyší. Už ho ale nepředává dalším repeaterům a
companionům (uzlům, ze kterých lidé píší zprávy). Nejvýše 16 kanálů.

### Přibrzdi jednoho odesílatele {#sender}

Bot, který píše příliš často na kanál, který si chceš nechat:

```text
filter watch add #test
filter sender add Bob 60
```

Bobovy zprávy na kanálu Public a `#test` teď projdou jednou za minutu;
zbytek filtr zahodí. Filtr porovnává jméno ve zprávě, takže odesílatel,
který se přejmenuje, se přes něj dostane.

### Zablokuj jeden repeater výše po cestě {#path}

Když balast přichází přes jeden repeater, zablokuj jeho prefix: první část
jeho ID v šestnáctkové soustavě (hex).

```text
filter path add a1b2
```

Krátký prefix jako `a1` zablokuje i každý jiný repeater, jehož ID začíná na
`a1`. Používej co nejdelší prefix. Nejvýše 8 prefixů.

## Každé nastavení {#settings}

Typy paketů se zadávají číslem. Na repeateru ukáže `filter types` stejná
čísla s názvy z firmwaru, například `TXT_MSG` a `GRP_TXT`:

| Číslo | Typ | Číslo | Typ |
| --- | --- | --- | --- |
| `00` | požadavek | `06` | skupinová data |
| `01` | odpověď | `07` | anonymní požadavek |
| `02` | přímá zpráva | `08` | cesta |
| `03` | potvrzení | `09` | trace |
| `04` | advert | `10` | vícedílný paket |
| `05` | skupinová zpráva | `11` | řídicí paket |

| Příkaz | Co dělá | Výchozí hodnota |
| --- | --- | --- |
| `filter on` / `filter off` | Zapne nebo vypne filtr. | vypnuto |
| `filter dryrun on` / `off` | Počítá zahozené pakety, ale všechno dál předává. | vypnuto |
| `filter hops <type> <max>` | Zahodí paket daného typu, který už prošel tolika repeatery, 0 až 64. | 32 pro skupinové zprávy, 8 pro ostatní |
| `filter rate <type> <limit> <secs> [soft]` | Předá nejvýše `limit` paketů daného typu za `secs` sekund. Se `soft` propouštění od `soft` po `limit` postupně slábne. `0` limit vypne. | 20 za 60 s pro přímé a skupinové zprávy, 10 pro adverty, 5 pro ostatní |
| `filter advert <hours>` | Předá advert každého uzlu jednou za tento počet hodin, nejvýše 720. | 0 (vypnuto) |
| `filter channel add <#name>` | Přestane předávat kanál dál. | žádný |
| `filter path add <hex>` | Zahodí všechno, co přišlo přes repeater s tímto prefixem, 2 až 8 hex číslic. | žádný |
| `filter sender add <name> [secs] [prob]` | Zahodí skupinové zprávy od odesílatele na kanálu Public a sledovaných kanálech. `Bot*` odpovídá každému jménu, které začíná na Bot. | žádný |
| `filter text add <word> [secs] [prob]` | Zahodí skupinové zprávy obsahující slovo, na kanálu Public a sledovaných kanálech. `^word` odpovídá jen na začátku. | žádný |
| `filter watch add <#name>` | Nechá pravidla sender a text číst i tento kanál, nejvýše 4. Public se čte vždy. | Public |
| `filter malformed on` / `off` | Zahodí zprávy na kanálu Public, které jsou prázdné, poškozené nebo mají datum posunuté o více než týden (kontrola data čeká, dokud nejsou nastavené hodiny). | vypnuto |
| `filter age <minutes>` / `off` | Zahodí skupinové zprávy starší než tolik minut, na kanálu Public a sledovaných kanálech, 1 až 10080. | vypnuto |
| `filter hash <bytes>` | Zahodí pakety s kratším ID cesty, než je tato hodnota, 1 až 3. | 1 |
| `filter reset` | Vrátí každé nastavení na výchozí hodnotu. | |

Každé `add` má své `remove` a `list`, například `filter channel remove #bot`.
V pravidlech sender a text propustí `secs` jednu zprávu za daný počet sekund.
`prob` použije pravidlo jen na tento podíl shod, 1 až 100. Nejvýše 8 pravidel
sender a 8 pravidel text. U jmen a slov se rozlišují velká a malá písmena;
jméno má nejvýše 15 znaků, slovo nejvýše 23.

Dvě nastavení zahazují víc, než možná čekáš:

- `filter hash 2` zahodí téměř veškerý provoz. Uzly ve výchozím nastavení
  posílají 1bajtová ID cesty.
- `filter age` spoléhá na hodiny tvého repeateru. Nastav je příkazem
  `clock sync` z aplikace, zkontroluj je příkazem `clock` a začni velkoryse:
  `filter age 60`.

Každé nastavení zůstane zachované i po restartu.

## Co zahodil {#stats}

`filter` ukáže součty podle důvodu:

```text
> Filter on: Blocked [ Hops: 3 | Rate: 12 | Channel: 1 | Hash: 0 | Malformed: 2 ]
```

`filter stats <topic>` ukáže podrobnosti k jednomu nastavení. Témata jsou
`hops`, `rate`, `channel`, `hash`, `malformed`, `advert`, `path`, `sender`,
`text` a `age`. `filter stats top` ukáže první bajt ID uzlů, které stojí za
nejvíce zahozenými pakety, spíš stopu než důkaz.
`filter stats air` ukáže vysílací čas, který tvůj repeater ušetřil tím, že
tyto pakety nepředal dál.

Počítadla začínají znovu od 0 po restartu a po příkazu `clear stats`.
