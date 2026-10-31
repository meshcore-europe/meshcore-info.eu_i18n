---
title: Udělej mesh odolnou
lead: Je mesh ve tvém okolí pomalá nebo plná smetí? Zjisti, co to způsobuje, zapni na repeateru nastavení, které to zastaví, a dej vědět své místní skupině.
description: 'Flood a spam v MeshCore mesh: jak poznat jednotlivé druhy, které nastavení repeateru pomůže, jak flood uvidět a jak najít jeho zdroj.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '500188ff'
  seeded: '2026-10-31'
  fields: {title: '33ec7ac8', lead: '780da19b', description: '1826e5e8'}
  sections: ['68ca5d36', '133c764a', 'a3bb5172', 'f4cc9cad', 'ace7b1ee', '89651002', 'f4dfdf59', '764c832c', 'f342b64b', 'f348e208']
  blocks: ['68ca5d36', 'c9cfbe6c', 'bcb31992', 'de7f60e4', 'e862fb9b', '0046b51f', '25f34d1d', 'c3c3ea52', '853a0f1d', '2bcea703', '871a7661', '2690aacf', 'a4aec3a1', 'd6da27c6', 'e8405458', 'f9150ee6', '8508ce40', '4b03ccd5', 'fb79c493', '695adde7', 'eba5a5b5', '836e0bac', '3497c5e8', '71c78fa1', '537d0930', '6a315252', '7c84dc56', '682e08e6', '258d7a27', '53af1400', '0dbebf97', 'ac0dca3c', '70fb4e9a', '9f055f50', 'ae90facc']
---

Přicházejí zprávy pozdě nebo vůbec? Plní se Public smetím? To je flood:
víc provozu, než mesh unese. Někdo ho posílá omylem, nebo záměrně. Najdi
v tabulkách níže, co vidíš. Každý řádek uvádí nastavení, které to zastaví.
Zapni ho na svém repeateru, tedy uzlu, který předává zprávy dál. Pak dej
vědět své [místní skupině](/community/), aby totéž udělaly i repeatery
kolem tebe. Každý repeater, který flood zahodí, uvolní vysílací čas pro
ostatní.

## Flood omylem {#mistake}

Flood omylem pochází z uzlu, jehož majitel neví, že ho způsobuje. Jakmile
to zjistí, flood skončí. Advert v tabulkách níže je pozdrav, který uzel
vysílá, aby ho ostatní našli.

Nastavení v tabulkách vycházejí z toho, co firmware dělá. Ne každé z nich
už zastavilo flood ve skutečné mesh.

{{< callout type="warning" >}}
Některá nastavení na této stránce potřebují firmware DMC. Standardní
**MeshCore** 1.18.0 má regiony, limity skoků `flood.max.*`, detekci smyček
a duty cycle. Paketový filtr, tedy pravidla, podle kterých tvůj repeater
zahazuje smetí, přináší **firmware DMC** od
[Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore). Totéž platí
pro duty-cycle gating a filtr companionu. Tato stránka vychází z vývojové
verze DMC 1.18.0 `ecfb2d4` z 19. října 2026. Kde ji získat, najdeš na
stránce [Paketový filtr](/guides/filter/#firmware).
{{< /callout >}}

| Co vidíš | Co to je | Co pomůže |
| --- | --- | --- |
| Dotazy na repeatery od jednoho uzlu ve dne i v noci a mesh, která zůstává pomalá celé dny | Domácí automatizace nebo bot, který se repeaterů ptá na stav příliš často | `filter on`. Paketový filtr pak propustí 5 dotazů za minutu. Dej vědět majiteli. |
| Stejný druh zprávy na kanálu každou minutu | Bot, který píše příliš často | [Zablokuj kanál](/guides/filter/#channel) nebo [zpomal odesílatele](/guides/filter/#sender). Dej vědět majiteli. |
| Nečitelné zprávy na Public a dalších kanálech | Uzel s poškozeným firmwarem nebo špatným nastavením rádia | `filter malformed on` je na Public zahodí. Dej vědět majiteli. |
| Advert jednoho uzlu každých pár minut | Uzel nastavený na příliš časté adverty | `filter advert 24` propustí advert každého uzlu jednou denně. `set flood.max.advert 3` udrží adverty do 3 skoků. |
| Zprávy z velké dálky s regiony, které sem nepatří | Most, který propojuje mesh sítě přes internet | `set flood.max.unscoped 1` a zařaď svůj repeater jen do [regionů, které obsluhuje](/guides/settings/#traffic). |
| Stejná zpráva prochází znovu a znovu a ID tvého repeateru je v její cestě víckrát | Repeater, který mění pakety a předává je dál, takže kolují ve smyčce | Detekce smyček běží ve výchozím stavu na `minimal`. `set loop.detect moderate` zahodí smyčku dřív. |

## Záměrný flood {#purpose}

Některé floody jsou spam: smetí, které někdo posílá záměrně, aby ucpal mesh.
Odesílatel mění jména, klíče i cesty, takže flood nezastaví žádné jediné
pravidlo.

| Co vidíš | Co to je | Co pomůže |
| --- | --- | --- |
| Spousta nových uzlů s náhodnými jmény, každý s novým klíčem | Falešné adverty | `filter rate 04 5 60` propustí 5 advertů za minutu. `filter advert` nepomůže: každý advert přichází z [nového klíče](#forged). |
| Zprávy s nečitelným textem od vymyšlených odesílatelů, často s datem starším než rok | Spam na kanálech | `filter malformed on` je na Public zahodí. `filter age 60` zahodí zprávy se starým datem na Public a na [sledovaných kanálech](/guides/filter/#settings). |
| Až 200 přímých zpráv za minutu uzlům, které neexistují, a žádná potvrzení zpět | Flood přímých zpráv | `filter rate 02 5 60`. Tvoje aplikace tyto zprávy nezobrazí, observer ano. |
| Série dotazů od jednoho uzlu na desítky dalších | Spam dotazů | S `filter on` propustí paketový filtr 5 dotazů za minutu. |
| Zpráva se vrátí o 10 až 20 minut později s téměř stejnou cestou | Replay: kopie odeslaná znovu | Repeater si pamatuje posledních 160 paketů, které viděl. V rušné mesh proto pozdější kopie znovu projde. `filter age` zahodí skupinovou zprávu starší, než povolíš. |
| Zprávy z Public odeslané znovu pod vymyšleným odesílatelem, někdy se starým datem | Echo spam | `filter age 60`. `filter malformed on` zahodí i datum posunuté o víc než týden. |
| Každých pár sekund zpráva na několika kanálech, pokaždé od nového jména, s běžnými otázkami | Vlna botů | `filter rate 05 10 60` a [zablokuj kanály](/guides/filter/#channel), které tvoje oblast nepoužívá. Každé jméno je nové, takže [pravidla pro odesílatele](#forged) ji minou. |

## Co se osvědčilo {#worked}

Místní skupiny zastavily floody těmito kroky:

1. **Dej vědět majiteli.** Flood omylem skončí, jakmile se o něm majitel
   dozví. Pošli mu přátelskou zprávu.
2. **Nereaguj v mesh.** Odpověď spammerovi ukáže, že spam funguje.
3. **Požádej o observery.** Observer je uzel, který přes MQTT hlásí každý
   paket, který slyší. Čím víc observerů kolem tebe, tím dřív uvidíš, kde
   flood vstupuje. Ze svého repeateru ho uděláš pomocí
   [MQTT na observeru](/guides/mqtt/).
4. **Najdi zdroj.** Observery určí oblast, kde odesílatel je. Poslední
   kilometr musí lidé projít pěšky s rádiem. Viz
   [Najdi zdroj](#source).
5. **Rozhýbej svou místní skupinu.** Jeden repeater se správným nastavením
   pomůže. Flood zastaví až všechny repeatery v oblasti společně. Tvoje
   [místní skupina](/community/) přiměje každého majitele nastavení zapnout.

## Vymyšlení odesílatelé a cesty {#forged}

Tyto části paketu píše odesílatel a nikdo je nekontroluje:

- **Jméno odesílatele.** Ve zprávě na kanálu je jméno součástí textu.
  Kdokoli s klíčem kanálu může napsat jakékoli jméno.
- **Začátek cesty.** Každý repeater přidá na konec cesty své ID. ID, která
  tam byla předtím, nikdo nekontroluje. Odesílatel proto může cestu začít
  vymyšlenými ID. Konec cesty je skutečný.

{{< forged-path >}}

`filter sender` a `filter path` tedy odesílatele zastaví jen do chvíle, než
změní jméno nebo cestu. [Blokování cesty](/guides/filter/#path) navíc
zahodí i skutečný provoz repeateru, jehož ID v ní je. Limity rychlosti,
limity skoků, kontroly stáří a poškozených zpráv, blokování kanálů, regiony
a duty cycle fungují dál.

## Nastavení pro každý flood {#always}

Tato nastavení platí, ať mesh zaplavuje cokoli:

- **Duty cycle na 10 %.** Tvůj repeater pak nikdy nevysílá víc, než dovoluje
  zákon, ať přichází cokoli. Popisuje to
  [průvodce repeaterem](/repeater-guide/#duty-cycle).
- **Regiony a limity skoků.** Region je oblast, ve které zpráva zůstává.
  Repeater předává dál jen zprávy v regionech, které má nastavené, a
  `flood.max.*` drží provoz nablízku. Obojí najdeš v části
  [Omez provoz](/guides/settings/#traffic).
- **Paketový filtr pro rušný repeater.**
  [Hotová nastavení](/guides/filter/#busy) sníží skupinové zprávy a adverty
  na polovinu. Nejdřív je vyzkoušej v režimu [dry-run](/guides/filter/#dryrun):
  ten jen počítá, co by zahodil.
- **Filtr companionu ve firmwaru DMC.** Tvůj companion, tedy uzel, ze
  kterého píšeš zprávy, drží smetí mimo tvoji aplikaci. Skryje poškozené a
  staré zprávy a také zprávy od repeateru či odesílatele nebo se slovem, které
  zablokuješ. Pravidlo pro odesílatele nebo slovo
  skryje zprávu jen tobě, ostatní ji dostanou dál.

### Duty-cycle gating {#gate}

Ve firmwaru DMC může tvůj repeater dát přednost vlastnímu regionu, když má
hodně práce. Jakmile vysílal víc než 35 % poslední minuty, přestane předávat
zprávy bez regionu. Pokud zůstane vytížený, zahodí potom nejširší region,
vždy o jednu úroveň. Jeho vlastní region projde vždy. Funguje to jen
s regiony nastavenými na tvém repeateru. Zapni to a zkontroluj:

```text
set dc.gate on
get dc.gate.status
```

{{< dc-gate >}}

Co takto zahodí, se v `filter stats` neukáže. Když se repeater zase
uklidní, regiony se vrátí, od nejvnitřnějšího.

## Jak flood uvidět {#see}

Tvoje aplikace ukazuje jen to, co dorazí k tobě. Flood přímých zpráv
uzlům, které neexistují, slyší jen observer. Každý observer posílá hlášení do
[MeshCore Analyzeru](https://meshcore-analyzer.eu/), kde je vidí každý. Ze
svého repeateru observer uděláš pomocí [MQTT na observeru](/guides/mqtt/).

V Analyzeru si prohlédni všechny kopie jednoho paketu. Jeho cesta obvykle
ukazuje, odkud přišel. Flooder může cestu začít
[vymyšlenými ID](#forged), takže první ID ti nic neřeknou. Každá kopie ale
nese stejný vymyšlený začátek. Kopie s nejkratší cestou prošla nejméně
skutečnými repeatery. Zachytil ji tedy někdo nejblíže k odesílateli.

{{< copies >}}

Na vlastním repeateru ti `filter stats` ukáže, co paketový filtr zahodil.
`filter stats top` ukáže první bajt ID uzlů, které stojí za nejvíc
zahozenými pakety. Tento bajt sdílí mnoho uzlů. Hledání tím zúžíš, ale
odesílatele nezjistíš.

## Najdi zdroj {#source}

Když se flood stále vrací:

1. **Sleduj cesty.** Cestu čti od konce: poslední ID jsou repeatery, kterými
   flood prošel. První skutečné ID je blízko zdroje. ID před ním můžou
   být [vymyšlená](#forged).
2. **Zúž oblast.** Když stejný paket slyší víc observerů, určí oblast, kde
   odesílatel je.
   [DMC Triangulator](https://triangulator.dutchmeshcore.nl/) ji vypočítá
   z repeaterů, které paket slyšely.
3. **Projdi poslední kilometr.** Repeatery slyší zdroj jen na okraji svého
   dosahu, takže poslední úsek musí lidé projít pěšky.
   [Mesh-Hunter](https://mesh-hunter.eu/) se spáruje s tvým companionem a
   zaznamená každý zachycený paket s tvojí GPS polohou. Když jde víc lidí
   najednou, najdou zdroj dřív.
4. **Dej vědět své [místní skupině](/community/).** Vidí z mesh víc,
   rozhodnou, co dál, a kontaktují toho, kdo flooduje záměrně.

## Doplň, co jsi viděl {#add}

Zasáhl tě flood, který v těchto
tabulkách není? Zastavilo nějaké nastavení flood? Napiš nám na
[Discord](https://discord.meshcore-info.eu/), co jsi viděl a co jsi
zapnul. Doplníme to na stránku.
