---
title: Co je MeshCore?
lead: MeshCore posílá textové zprávy rádiem, od uzlu k uzlu. Funguje bez internetu a bez předplatného.
description: 'Co MeshCore je a co není: druhy uzlů, směrování, šifrování a pásmo 868 MHz.'
eyebrow: MeshCore v1.18.0
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '70b86ac3'
  seeded: '2026-11-11'
  fields: {title: '06eda66b', lead: 'c0174569', description: 'c2255f49', eyebrow: '8610c822'}
  sections: ['aa768ac3', '9e1e2d85', '0a55792c', 'c3de803d', '493b444f', '429f699c', 'f8008f48', 'd516c212', '0894fe81']
  blocks: ['c3c9c568', '55e4248c', 'c0324d05', 'b20e61c3', 'b7b981e6', '68ed3005', 'cabeb32d', 'b2ca68ba', '681d55b9', 'd1df283f', '0d0e2a8b', '0596f602', 'eec63bed', '183a79e4', '47910535', 'd5a92bbf', 'b44d4637', '431021a0', '83c03732', 'e908ca85', '8f79fbf9', '3323d83e', '857c37dc', '0c4d0dd2', 'bd238f09', '794792be', '5d796ffb', '1a490368', 'f0dd237f', '053d85bc', '02f1fe2f', 'e6b5b258']
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
  zhruba tak dlouhé jako SMS v tvém telefonu. Žádný hlas, fotky, video
  ani weby a na běžné telefonní číslo se nedovoláš.
- **Není to tísňová služba.** Žádná tísňová služba neslibuje, že bude mesh
  poslouchat. Víme, že mesh fungovat může. Jestli funguje v nouzi, to neví
  nikdo.
- **Není to okamžité a není to všude.** Zpráva skáče od rádia k rádiu.
  Může to trvat pár sekund, nebo zpráva nedorazí vůbec. Jestli projde,
  záleží na repeaterech kolem tebe, na výšce, budovách a tvé anténě. Malé
  rádio uvnitř domu často nedosáhne na nikoho. Repeater na střeše dosáhne
  na kilometry.
- **Není to služba, kterou za tebe někdo provozuje.** Není tu žádný
  poskytovatel, podpora ani slib pokrytí. Mesh existuje tam, kde lidé
  z komunity postavili repeatery.
- **Ne všechno v meshi je soukromé.** Přímé zprávy jsou šifrované. Public
  a hashtagové kanály ale může číst kdokoli. Jméno tvého uzlu a sdílenou
  polohu vidí každý v dosahu. [Observery](/network/) hlásí, co slyší,
  na veřejné mapy. Co zůstává soukromé, vysvětluje
  [část o šifrování](#encryption).
- **Není to neomezené.** Všichni v oblasti sdílejí jeden rádiový kanál.
  Pravidla pro [pásmo 868 MHz](#band) omezují, jak dlouho smí každé rádio
  vysílat. Každá zpráva bere vysílací čas všem ostatním. Boti, časté
  adverty a testovací zprávy proto zpomalují mesh pro všechny.
- **Není to Meshtastic.** Meshtastic je jiný systém, který běží na většinou
  stejných deskách. Tyto dva systémy spolu komunikovat nemůžou.

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

- Spojení na túrách, na moři a na festivalech, kde je mobilní síť
  přetížená nebo chybí.
- Záložní kanál pro rodinu nebo sousedy, když vypadne proud nebo mobilní
  síť.
- Záloha pro místní úřady, když jejich běžné sítě selžou.
- Místní chat na rádiích, která lidé sami vlastní.
- Spojení pro pátrací a záchranný tým tam, kde není mobilní síť.
  MeshCore SAR, komunitní aplikace v [Projektech](/projects/), přidává mapy
  a sdílené polohy.
- Kontrola vzdáleného místa z domova. Repeatery a senzorové uzly hlásí
  napětí baterie a další hodnoty, když se zeptáš.
- Hlídání senzoru. Na senzorovém uzlu běží firmware MeshCore určený k měření.
  Uchovává historii napětí své baterie. Přihlas se jako admin a uzel tě
  upozorní, když baterie dochází. Upozornění na jiné hodnoty přidáš
  vlastním kódem.
- Spínání něčeho na dálku, třeba čerpadla. To přidáš do senzorového
  firmwaru vlastním kódem.
- Experimenty s rádiem, anténami, solární energií a open source softwarem.

Některé úřady na MeshCore budují nebo testují záložní řešení. Tyto příklady jsme
ověřili v listopadu 2026.

- Cyklon Gabrielle přerušil veškerou komunikaci v regionu Tairāwhiti na Novém
  Zélandu. V září 2025 krizové řízení regionu uvedlo MeshCore jako
  [jeden z nejméně 6 záložních způsobů komunikace](https://www.scoop.co.nz/stories/AK2509/S00669.htm).
  Jako páteř sítě navíc budovalo solární repeatery.
- Německý okres Bad Kissingen
  [buduje na MeshCore textovou síť](https://www.landkreis-badkissingen.de/wirtschaft/digitalisierung/kommunikationsnetze/index.html)
  pro úřady, záchranné složky a kritická místa. Jako první se připojují
  hasičské stanice.
- Zastupitelstvo nizozemského Hilversumu
  [hlasovalo 34 ku 1 pro zkušební provoz](https://hilversum.nl/nieuwsoverzicht/gemeenteraad-buigt-zich-over-financien)
  s repeaterem na věži radnice. Obec ho
  [vyhodnotí na podzim 2027](https://www.spreekbuis.nl/hilversum-start-proef-met-onafhankelijk-noodcommunicatienetwerk-meshcore/).
- S MeshCore experimentují dva nizozemské bezpečnostní regiony, které
  řídí reakci na krize:
  [Jižní Limburg](https://nos.nl/nieuwsuur/artikel/2607176-communicatie-hulpdiensten-valt-uit-bij-lange-stroomstoring-oplossing-niet-in-zicht)
  a [Drenthe](https://www.rtvdrenthe.nl/nieuws/18438486/hackerspace-drenthe-werkt-aan-een-noodnetwerk-voor-de-provincie).
  Podle Drenthe je zatím příliš brzy říct, jak nebo kdy by ho mohla použít.
- V Dalfsenu, rovněž v Nizozemsku,
  [provozují dobrovolníci pilotní projekt spolu s obcemi](https://noodnetoverijssel.nl/).
  Primárně používají hlasové rádio a MeshCore jako druhou vrstvu pro text.

Jestli mesh ve tvém okolí v nouzi funguje, nikdo neví.

## Odkud pocházejí data {#data}

Vyhledávání na stránce [místních skupin](/community/) hledá místa v kopii
volně dostupných seznamů míst a PSČ z [GeoNames](https://www.geonames.org/), pod
licencí [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Kopie je
uložená na tomto webu. Tvoje hledání nikdy neopustí tvoje zařízení a na
GeoNames neodchází žádný požadavek.
