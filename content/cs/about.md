---
title: Co je MeshCore?
lead: MeshCore posílá textové zprávy rádiem, z uzlu na uzel. Funguje bez internetu a bez předplatného.
description: 'Co MeshCore je a co není: mesh, companiony, repeatery a room servery, směrování, šifrování a pásmo 868 MHz v Evropě.'
eyebrow: MeshCore v1.18.0
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '33e571f0'
  seeded: '2026-10-26'
  fields: {title: '06eda66b', lead: 'c0174569', description: '658f8a01', eyebrow: '8610c822'}
  sections: ['a3a6c1ff', '007314d2', 'f1f23981', '493b444f', '429f699c', 'f8008f48', '655373a9']
---

MeshCore je svobodný software pro malá rádia LoRa. LoRa je rádiová technika, která přenáší málo dat na velkou vzdálenost s velmi malou spotřebou. Rádiu s MeshCore se říká *uzel*. Spáruješ ho s aplikací v telefonu nebo notebooku, nebo má vlastní displej a klávesnici. Pak s ním píšeš lidem vzdáleným kilometry. Mezi vámi není žádný vysílač, router ani operátor.

MeshCore posílá jen krátké textové zprávy: žádný hlas, fotky ani internetový provoz. Doručení zprávy může trvat několik sekund a závisí na repeaterech v tvém okolí. Záchranné služby nenahrazuje: v nouzi volej 112.

Software je open source. Vyvíjí se na [meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore) pod licencí MIT.

## Mesh za minutu {#mesh}

Jedno rádio LoRa dosáhne ve městě na několik kilometrů, z kopce nebo ze střechy mnohem dál. Aby zprávy došly dál, rádia si je navzájem předávají: to je *mesh*. V MeshCore se o předávání starají rádia zvaná *repeatery*. Repeater, který zprávu zaslechne, ji vyšle znovu. Tak může zpráva přejít celý region.

Mesh nikomu nepatří. Každý uzel a každý repeater patří někomu z komunity. Mesh je tak dobrý, jak dobré repeatery lidé postaví.

## 3 druhy uzlů {#roles}

Druh uzlu si volíš při flashování. Tvůj první uzel je companion.

**Companion.** Tvoje vlastní rádio. S aplikací MeshCore v telefonu nebo notebooku se páruje přes Bluetooth nebo USB; některé mají vlastní displej a klávesnici. V aplikaci čteš a píšeš. Companion uchovává tvoje kontakty a kanály a také zprávy, které dorazily, když aplikace nebyla připojená. Zprávy pro ostatní companion nepředává.

**Repeater.** Rádio umístěné vysoko, které předává zprávy pro všechny. Většina běží na solární energii. Vlastní potřebuješ jen tam, kam mesh ještě nedosahuje. Nemá vlastní aplikaci. Nastavíš ho přes USB, nebo se přihlásíš heslem a spravuješ ho přes rádio. Jak na to, ukazuje [průvodce repeaterem](/repeater-guide/).

**Room server.** Malá nástěnka na meshi. Po přihlášení dostaneš příspěvky, které ti unikly mimo dosah, nejvýše posledních 32. Místní skupina ji používá na oznámení.

## Jak si zpráva najde cestu {#routing}

Každý uzel má tajný klíč a veřejný klíč. Veřejný klíč je jeho identita. Uzel se ohlašuje *advertem*: podepsaným paketem se svým jménem a, pokud chceš, se svou polohou. Někdo se ti objeví v kontaktech, až k tobě dorazí jeden z jeho advertů, nebo když naskenuješ jeho QR kód. Vlastní advert pošleš tlačítkem v aplikaci.

Tvoje první zpráva kontaktu odchází jako *flood*. Každý repeater, který ji zaslechne, ji jednou předá dál a cestou přidá své krátké ID. Odpověď nese tento seznam ID zpět. Od té chvíle jdou tvoje zprávy tomu kontaktu po zaznamenané cestě a vysílají jen repeatery na ní. Když se cesta přeruší, aplikace znovu použije flood.

Zprávy do kanálu nemají jedinou adresu, proto jdou vždy floodem. Repeatery si pamatují, co nedávno předaly, a kopie, které dorazí znovu jinou cestou, zahodí. Zpráva může projít až 64 repeatery, nebo 32 tam, kde preset používá 2bajtová ID.

## Šifrování a soukromí {#encryption}

Tvoje přímé zprávy jsou šifrované end-to-end: přečteš je jen ty a druhá osoba. Repeater vidí, komu je paket určen, jen jako 1bajtovou nápovědu.

Kanály jsou šifrované sdíleným klíčem. Kdo je může číst, tedy závisí na tom, kdo ten klíč má:

- **Public** je nastavený na každém companionu. Jeho klíč je zveřejněný, takže ho může číst kdokoli.
- **Hashtagové kanály**, například `#utrecht`, odvozují klíč od svého názvu. Připojit se může každý, kdo název zná, proto je ber také jako veřejné.
- **Soukromé kanály** používají náhodný klíč, který sdílíš sám, například jako QR kód.

Adverty jsou podepsané, ale ne šifrované. Jméno tvého uzlu a jeho polohu, pokud ji sdílíš, vidí všichni v dosahu. Vyber si jméno, které neprozradí víc, než chceš.

## Pásmo 868 MHz v Evropě {#band}

V Evropě MeshCore používá malou část pásma 868 MHz, kterou smí kdokoli používat bez licence. Jeho evropský rádiový preset, EU/UK (Narrow), leží na 869.618 MHz v kanálu širokém 62.5 kHz. To je uvnitř dílčího pásma 869.40-869.65 MHz, kde je povoleno až 500 mW e.r.p. Zařízení tam smí vysílat nejvýše 10% času. Podrobnosti a limity pro jednotlivé země najdeš v [právní části průvodce repeaterem](/repeater-guide/#legal).

Všichni v jedné oblasti používají stejný preset, jinak se jejich rádia neuslyší. Některé země a regiony používají variantu: která to je, ví tvoje [místní skupina](/community/).

## K čemu ho lidé používají {#uses}

- Zůstat ve spojení na túrách, na moři a na festivalech, kde je mobilní síť přetížená nebo chybí.
- Záložní kanál pro rodinu nebo sousedy, když vypadne elektřina nebo mobilní sítě.
- Místní chat na rádiích, která lidé sami vlastní.
- Experimentování s rádiem, anténami, solární energií a open-source softwarem.
