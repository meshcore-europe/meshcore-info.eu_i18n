---
title: Co je MeshCore?
lead: MeshCore posílá textové zprávy rádiem, od uzlu k uzlu. Funguje bez internetu a bez předplatného.
description: 'Co MeshCore je a co není: druhy uzlů, směrování, rozdíly oproti Meshtastic, šifrování a pásmo 868 MHz.'
eyebrow: MeshCore v1.18.0
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '279b56a4'
  seeded: '2026-11-02'
  fields: {title: '06eda66b', lead: 'c0174569', description: '15e6d2a7', eyebrow: '8610c822'}
  sections: ['aa768ac3', '16fde264', '0a55792c', 'c3de803d', '493b444f', 'a8b2b9b4', '429f699c', 'f8008f48', '88af2bd3', '0894fe81']
  blocks: ['c3c9c568', '55e4248c', 'c0324d05', 'b20e61c3', 'fab378a5', '68ed3005', 'cabeb32d', 'b2ca68ba', '681d55b9', 'd1df283f', '0d0e2a8b', '0596f602', 'eec63bed', '183a79e4', '47910535', 'd5a92bbf', 'b44d4637', 'fc8f3129', '8dec428a', '07cbac35', '431021a0', '83c03732', 'e908ca85', '8f79fbf9', '3323d83e', '857c37dc', '0c4d0dd2', 'bd238f09', '794792be', '95e18f18', '02f1fe2f', 'e6b5b258']
---

MeshCore je svobodný software pro malá rádia LoRa. LoRa je rádiová technika,
která přenáší málo dat na velkou vzdálenost a s velmi malou spotřebou. Rádiu
s MeshCore se říká *uzel*. Spáruješ ho s aplikací v telefonu nebo notebooku,
nebo použiješ jeho vlastní displej a klávesnici. Pak posíláš text lidem
vzdáleným celé kilometry. Mezi vámi nestojí žádný vysílač, router ani operátor.

Software je open source. Vyvíjí se v repozitáři
[meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore) pod licencí
MIT.

## Co MeshCore není {#not}

S rádiem začínáš? Tohle od MeshCore lidé nejčastěji očekávají, a přitom to
neumí.

- **Není to internet ani telefon.** MeshCore posílá krátké textové zprávy,
  zhruba tak dlouhé jako SMS v telefonu. Žádný hlas, fotky, video ani weby
  a na běžné telefonní číslo se nedovoláš ani nenapíšeš.
- **Není to tísňová služba.** V meshi nenaslouchá žádná tísňová služba a nikdo
  neslibuje, že si někdo tvou zprávu přečte. V nouzi volej 112.
- **Není to okamžité a nefunguje to všude.** Zpráva přeskakuje z rádia na rádio
  a může jí to trvat několik sekund, nebo nedorazí vůbec. Jestli projde, záleží
  na repeaterech kolem tebe, na výšce, budovách a tvé anténě. Malé rádio uvnitř
  budovy často nikoho nezastihne. Repeater na střeše dosáhne kilometry daleko.
- **Není to služba, kterou pro tebe někdo provozuje.** Není tu žádný
  poskytovatel, žádná podpora ani slíbené pokrytí. Mesh existuje tam, kde lidé
  z komunity postavili repeatery, a nikde jinde.
- **Ne všechno v něm je soukromé.** Přímé zprávy jsou šifrované, ale kanál
  Public a hashtagové kanály si může přečíst kdokoli. Jméno tvého uzlu
  a sdílenou polohu vidí všichni v dosahu.
  [Observery](/network/) hlásí veřejným mapám, co slyší. Co zůstává soukromé,
  vysvětluje [část o šifrování](#encryption).
- **Není to neomezené.** Všichni v oblasti sdílejí jeden rádiový kanál. Pravidla
  pro [pásmo 868 MHz](#band) omezují, jak dlouho smí každé rádio vysílat. Každá
  zpráva bere vysílací čas všem ostatním, takže boti, časté adverty a testovací
  zprávy zpomalují mesh pro všechny.
- **Není to Meshtastic.** Meshtastic je jiný systém, který běží na velmi
  podobných deskách. Oba systémy se spolu nedomluví.
  [Přechod z Meshtasticu](#meshtastic) popisuje, co funguje jinak.

## Mesh za minutu {#mesh}

Jedno rádio LoRa dosáhne ve městě na pár kilometrů. Z kopce nebo ze střechy
mnohem dál. Aby se zpráva dostala dál, rádia si ji navzájem předávají: to je
*mesh*. V MeshCore zprávy předávají rádia, kterým se říká *repeatery*.
Repeater, který zprávu zachytí, ji vyšle znovu. Tak může projít celým regionem.

Mesh nikomu nepatří. Každý uzel a každý repeater patří někomu z komunity.
Mesh sahá tak daleko, kam dosáhnou jejich repeatery.

## 3 druhy uzlů {#roles}

Druh uzlu zvolíš, když do něj nahráváš firmware. Tvůj první uzel je companion.

**Companion.** Tvoje vlastní rádio. Spáruješ ho s aplikací MeshCore
v telefonu nebo notebooku přes Bluetooth nebo USB. Některé mají vlastní
displej a klávesnici. V aplikaci čteš a píšeš. Companion uchovává tvoje
kontakty a kanály. Uchovává i zprávy, které přišly, když aplikace nebyla
připojená. Companion zprávy pro ostatní nepředává.

**Repeater.** Rádio umístěné vysoko, které předává zprávy pro všechny.
Většina běží na solární energii. Vlastní potřebuješ jen tam, kam mesh zatím
nedosahuje. Nemá vlastní aplikaci. Nastavíš ho přes USB, nebo se přihlásíš
heslem a spravuješ ho přes rádio. Jak na to, ukazuje
[průvodce repeaterem](/repeater-guide/).

**Room server.** Malá nástěnka se zprávami na meshi. Když se přihlásíš,
dostaneš příspěvky, které jsi zmeškal mimo dosah, maximálně posledních 32.
Drží je jen v paměti, takže je restart nebo výpadek proudu smaže. Místní
skupina ho používá pro oznámení.

## Jak zpráva najde cestu {#routing}

Každý uzel má soukromý klíč a veřejný klíč. Veřejný klíč je jeho identita.
Uzel se ohlašuje *advertem*: podepsaným paketem se svým názvem a polohou,
pokud ji chceš sdílet. Někdo se ti objeví v kontaktech, když k tobě dorazí
jeho advert, nebo když naskenuješ jeho QR kód. V aplikaci je tlačítko,
kterým pošleš vlastní advert.

Tvoje první zpráva kontaktu odchází jako *flood*. Každý repeater, který ji
zachytí, ji jednou předá dál a přidá k ní svoje krátké ID. Odpověď nese
tenhle seznam ID zpět. Od té chvíle jdou tvoje zprávy tomu kontaktu
zaznamenanou cestou a vysílají jen repeatery na ní. Když se cesta přeruší,
aplikace pošle zprávu znovu jako flood.

Zprávy do kanálu nemají jednu adresu, takže jdou vždy jako flood. Repeatery
si pamatují, co nedávno předaly, a kopie, které dorazí znovu jinou cestou,
zahodí. Zpráva může projít až 64 repeatery, nebo 32, pokud preset používá
2bajtová ID.

## Přechod z Meshtasticu {#meshtastic}

Na mnoha deskách běží buď MeshCore, nebo Meshtastic, a ty si nahraješ ten, který chceš. Tohle jsou rozdíly, kterých si všimneš jako první. Vycházejí z MeshCore
v1.18.0 a z dokumentace Meshtasticu z listopadu 2026.

- **Kdo předává zprávy.** V MeshCore to dělají jen repeatery, tvůj companion
  nikdy. V Meshtasticu zprávy předává i výchozí role client, pokud to už
  neudělal jiný uzel.
- **Jak daleko zpráva dojde.** Zpráva v MeshCore může projít až 64 repeatery.
  Meshtastic ve výchozím nastavení končí po 3 skocích, maximálně po 7.
- **Údaje z jiných uzlů.** Repeatery a senzorové uzly v MeshCore posílají údaje,
  například napětí baterie, když si o ně řekneš. Neposílají je celému meshi.
- **Internet.** Firmware MeshCore nemá žádné propojení meshů přes internet.
  [Observery](/network/) hlásí mapám, co slyší, a to jen jedním směrem.
  Meshtastic má vestavěný modul MQTT, který umí přenášet zprávy mezi meshi
  přes internet.

## Šifrování a soukromí {#encryption}

Tvoje přímé zprávy jsou šifrované end-to-end: přečteš je jen ty a druhá
osoba. Repeater vidí, komu je paket určen, jen jako 1bajtovou nápovědu.

Kanály jsou šifrované sdíleným klíčem. Kdo je může číst, proto závisí na tom,
kdo ten klíč má:

- **Public** je nastavený na každém companionu. Jeho klíč je zveřejněný,
  takže ho může číst kdokoli.
- **Hashtagové kanály**, třeba `#utrecht`, odvozují klíč ze svého názvu.
  Připojit se může každý, kdo název zná. Ber je proto také jako veřejné.
- **Soukromé kanály** používají náhodný klíč, který sdílíš sám, třeba
  jako QR kód.

Adverty jsou podepsané, ale ne šifrované. Název tvého uzlu a jeho polohu,
pokud ji sdílíš, vidí každý v dosahu. Vyber si název, který neprozradí víc,
než chceš.

## Pásmo 868 MHz v Evropě {#band}

V Evropě MeshCore používá malou část pásma 868 MHz, kterou smí kdokoli
používat bez licence. Jeho evropský rádiový preset, EU/UK (Narrow), leží na
869.618 MHz s kanálem 62.5 kHz. Spadá tak do podpásma 869.40-869.65 MHz,
kde je povoleno až 500 mW e.r.p. Zařízení tam smí vysílat nejvýš 10% času.
Podrobnosti a limity pro jednotlivé země najdeš v
[právní části průvodce repeaterem](/repeater-guide/#legal).

Všichni v oblasti používají stejný preset, jinak se jejich rádia neslyší.
Některé země a regiony používají variantu. Kterou, ví tvoje
[místní skupina](/community/).

## K čemu to lidé používají {#uses}

- Spojení na túrách, na moři a na festivalech, kde je mobilní síť přetížená
  nebo chybí.
- Záložní kanál pro rodinu nebo sousedy, když vypadne proud nebo mobilní sítě.
- Místní chat na rádiích, která lidé sami vlastní.
- Kontrola vzdáleného místa z domova. Repeatery a senzorové uzly hlásí napětí
  baterie a další údaje, když si o ně řekneš.
- Sledování senzoru. Na senzorovém uzlu běží firmware MeshCore určený k měření.
  Uchovává historii naměřených hodnot. Když se přihlásíš k odběru, upozorní tě,
  například když mu dochází baterie.
- Spínání něčeho na dálku, třeba čerpadla. Do firmwaru senzoru to přidáš
  vlastním kódem.
- Experimenty s rádiem, anténami, solární energií a open source softwarem.

## Odkud pocházejí data {#data}

Vyhledávání na stránce [místních skupin](/community/) hledá místa v kopii
volně dostupných seznamů míst a PSČ z [GeoNames](https://www.geonames.org/), pod
licencí [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Kopie je
uložená na tomto webu. Tvoje hledání nikdy neopustí tvoje zařízení a na
GeoNames neodchází žádný požadavek.
