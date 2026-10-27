---
title: Průvodce repeaterem
lead: Repeater umístěný vysoko předává zprávy všem v okolí, přes celé město nebo údolí. Vyber místo, napájej ho ze slunce, nastav ho a drž se zákona.
description: 'Naplánuj, napájej, nastav a legálně provozuj repeater MeshCore v Evropě: výběr místa, dimenzování solárního panelu, nastavení přes CLI, výkon na 868 MHz a limity klíčovacího poměru.'
eyebrow: 868 MHz · až 500 mW · bez licence
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '4a0fe39f'
  seeded: '2026-10-26'
  fields: {title: '4608abcd', lead: 'bc670c65', description: '9e483ce5', eyebrow: '9fd33416'}
  sections: ['1de4a4f7', '766086be', '70faf508', '8bc641aa', '2018aa04', '92beca03', '17634750', 'cadf6024', 'e9cc6834', '2e6e59ca', 'fb44b8db']
---

Repeatery drží mesh pohromadě. Companiony, tedy rádia, ze kterých píšeš zprávy, zprávy dál nepředávají. Bez repeaterů se tedy dovoláš jen lidem v přímém dosahu. Každý repeater, který postavíš, rozšíří mesh všem kolem. Tento průvodce vychází z firmwaru MeshCore v1.18.0.

Než začneš, domluv se se svou [místní skupinou](/community/). Lidé v ní vědí, kde chybí pokrytí, jaký [preset se ve tvé oblasti používá](/guides/settings/) a jak repeatery pojmenovávat. Podívej se na [mapy pokrytí](/map/), kde jsou repeatery blízko tebe, a pozdrav na veřejných nebo místních [kanálech](/guides/channels/).

## Vyber místo {#site}

Výška je víc než výkon. LoRa na 868 MHz se šíří nejlépe po přímé viditelnosti. Kopce, budovy a husté stromy ubírají mnohem víc dosahu, než kolik pár miliwattů navíc získá zpět.

- **Jdi vysoko.** Střecha, stožár, vysoká budova nebo kopec pokryjí mnohem víc než parapet. Pomůže i pár metrů nad okolními střechami.
- **Nech anténu ve volném prostoru.** Umísti ji nad hrany střechy, dál od kovu, okapů a jiných antén.
- **Ověř si výhled.** Nástroje jako [HeyWhatsThat](https://www.heywhatsthat.com/) ukážou, co je z daného místa vidět. Když na nějaké místo dohlédneš, repeater tam bude v dosahu.
- **Nech volný prostor.** Rádiová cesta potřebuje kolem přímé spojnice trochu volného místa, ne jen spojnici samotnou. Na dlouhých vzdálenostech by měl střed cesty míjet překážky o několik metrů.
- **Požádej o svolení.** Získej souhlas majitele střechy nebo stožáru a domluv se, jak se k repeateru dostaneš kvůli údržbě.

## Hardware {#hardware}

- **Deska.** Vyber úspornou desku s nRF52, například [Heltec T114](/devices/), RAK WisBlock nebo SenseCAP Solar Node. Desky s ESP32 mají větší spotřebu (na stránce zařízení jsou označené jako High), takže se na solár provozují těžko.
- **Anténa.** Použij anténu určenou pro 868 MHz, namontovanou svisle. [Průvodce anténami](/guides/antenna/) popisuje typy, konektory, kabel a montáž. Zisk antény se počítá do zákonného limitu výkonu, viz [Zákonné limity](#legal).
- **Kabel.** Koaxiální kabel nech krátký, nebo použij kabel s nízkým útlumem. Na 868 MHz může pár metrů tenkého kabelu sebrat polovinu výkonu.
- **Krabice.** Krabice odolná proti počasí (IP65 nebo lepší) s kabelovou průchodkou, odvětrávacím nebo odtokovým otvorem proti kondenzaci a ve světlé barvě nebo se stínítkem. Bateriím vadí horko a pod bodem mrazu se nedají nabíjet.
- **Blesk.** Anténa na střeše je terč. Řiď se místními pravidly pro uzemnění, nebo ji umísti tak, aby zásah nedosáhl na elektroinstalaci budovy.

## Napájení a dimenzování soláru {#power}

Solární repeater musí přežít nejtemnější týdny zimy. Dimenzuj ho na ně:

1. **Změř spotřebu.** Nech nastavený repeater běžet jeden den přes USB měřič výkonu. Odečti spotřebovanou energii ve watthodinách (Wh). Provoz ve tvé oblasti to číslo mění, takže pokud můžeš, měř přímo na místě.
2. **Přidej rezervu.** Kapacitu baterie naplánuj aspoň na 5 až 7 dní bez užitečného slunce.
3. **Zjisti zimní slunce.** Bezplatný [nástroj PVGIS](https://re.jrc.ec.europa.eu/pvg_tools/en/) od EU ukáže pro každé místo, kolik energie panel vyrobí za měsíc. Vezmi měsíc s nejmenším osvitem.
4. **Dimenzuj panel.** Panel musí v tom nejhorším měsíci nahradit každodenní spotřebu, s rezervou na ztráty při nabíjení.

Příklad s odhadnutými čísly: repeater se spotřebou 1 Wh za den potřebuje na týden rezervy baterii aspoň 7 Wh, tedy zhruba 2 Ah využitelné kapacity při 3,7 V. Když PVGIS říká, že 1 W panel na tvém místě dá v prosinci 0,5 Wh za den, potřebuješ aspoň 2 W panel. Panel o 3 až 5 W nechá rezervu na mraky, sníh a stárnutí.

## Nastav ho {#config}

**Nahraj firmware.** Použij [webový flasher](https://flasher.meshcore.io) a vyber pro svou desku firmware **Repeater**. Postup nahrávání najdeš v části [Začínáme](/get-started/#flash).

**Nastav ho přes USB.** Nech repeater připojený k počítači a otevři [config.meshcore.io](https://config.meshcore.io) nebo konzoli ve flasheru. Můžeš použít i jakýkoli sériový terminál s rychlostí 115200 baud. Nejdůležitější příkazy:

| Co | Příkaz |
|---|---|
| Změna hesla správce | `password <new password>` |
| Pojmenování | `set name <name>` |
| Preset rádia: kmitočet, šířka pásma, SF, CR (restartuj, aby se projevil) | `set radio 869.618,62.5,8,8` |
| Limit duty cycle v procentech | `set dutycycle 10` |
| Vysílací výkon rádiového čipu v dBm | `set tx <dBm>` |
| Poloha, aby se zobrazil na mapách | `set lat <degrees>` a `set lon <degrees>` |
| Kontaktní údaje pro ostatní provozovatele | `set owner.info <text>` |
| Hodiny mezi flood adverty, které slyší celý mesh | `set flood.advert.interval <hours>` |
| Oznámit ho teď | `advert` |
| Restart | `reboot` |

Výchozí heslo správce je `password` a každý, kdo se s ním přihlásí, se stane správcem. Změň ho dřív, než repeater začne vysílat.

Příklad `set radio` výše je pro EU/UK (Narrow). Použij místo něj hodnoty presetu ve své oblasti: [Doporučená nastavení](/guides/settings/) je uvádí pro jednotlivé země.

**Nastav hodiny.** Bez modulu hodin (RTC) repeater ztratí čas při každém výpadku napájení a po restartu začne v květnu 2024, a za provozu se mu hodiny rozcházejí. Přihlas se vzdáleně z aplikace a použij `clock sync`, nebo nastav čas přes USB. Modul RTC je pro repeater užitečný doplněk: udrží čas i při výpadku napájení a rozchází se mnohem méně.

**Spravuj ho vzdáleně.** Jakmile je v meshi, přihlas se z aplikace MeshCore heslem správce. Tam si přečteš jeho stav a používáš stejné příkazy přes rádio. Některé příkazy fungují jen přes USB, například `set freq` a tovární reset `erase`.

Úplný seznam příkazů je v [referenci MeshCore CLI](https://github.com/meshcore-dev/MeshCore/blob/main/docs/cli_commands.md).

## Zákonné limity {#legal}

{{< callout type="legal" verified="2026-10-02" >}}
Evropské presety MeshCore leží v podpásmu **869.40-869.65 MHz**. V EU, Spojeném království, Švýcarsku a Norsku je otevřené zařízením krátkého dosahu bez licence, při těchto limitech:

- nejvýše **500 mW e.r.p.** vyzářeného výkonu;
- nejvýše **10% duty cycle**: ne víc než 360 sekund vysílání v kterékoli hodině, na jedno zařízení. Zařízení může místo toho použít listen-before-talk s adaptivní kmitočtovou agilitou podle ETSI EN 300 220-2;
- celý signál, široký nejvýše 250 kHz, musí zůstat uvnitř podpásma.

Pásmo je sdílené: nesmíš rušit licencované služby a ostatní mohou rušit tebe.
Rádio musí mít označení CE (ve Velké Británii CE nebo UKCA).
{{< /callout >}}

Zdroje: [doporučení CEPT ERC 70-03](https://docdb.cept.org/document/845), příloha 1, pásmo h1.7;
[rozhodnutí Komise 2006/771/ES](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02006D0771(01)-20250123)
a jeho změny;
[ETSI EN 300 220-2](https://www.etsi.org/deliver/etsi_en/300200_300299/30022002/03.03.01_60/en_30022002v030301p.pdf),
pásmo O.

### Výkon: e.r.p. a tvoje anténa {#erp}

Limit platí pro *vyzářený* výkon, měřený vůči jednoduché dipólové anténě (e.r.p.). Zisk antény se přičítá, útlum kabelu se odečítá. Výrobci uvádějí zisk antény v dBi, což je o 2.15 dB víc než stejný zisk v dBd (vztažený k dipólu). Tento součet drž na 27 dBm (500 mW) nebo níž:

> vysílací výkon (dBm) + zisk antény (dBi) − útlum kabelu (dB) − 2.15 ≤ 27

- Deska vysílající 22 dBm do antény 5 dBi přes kabel s útlumem 1 dB:
  22 + 5 − 1 − 2.15 = 23.85 dBm, zhruba 240 mW e.r.p. V limitu.
- Deska se zesilovačem 30 dBm (1 W) do antény 3 dBi:
  30 + 3 − 2.15 = 30.85 dBm, zhruba 1.2 W e.r.p. Nad limitem; sniž vysílací výkon.

`set tx` nastavuje výstup čipu LoRa v dBm. Samotný čip SX1262 končí na 22 dBm; firmware zadané číslo nekontroluje. Desky se zesilovačem navíc, například Heltec V4 nebo Station G2, vysílají mnohem víc, než kolik nastavíš. Než hodnotu nastavíš, podívej se do tabulky výrobce a začni nízko.

### Klíčovací poměr {#duty-cycle}

Repeater vysílá za všechny kolem sebe, takže svůj vysílací čas spotřebuje rychleji než companion. Omezovač klíčovacího poměru v MeshCore má výchozí hodnotu 50 %, což je víc, než toto pásmo dovoluje. Na každém repeateru ho nastav na 10 %:

```text
set dutycycle 10
```

### Přesnost kmitočtu {#frequency}

Kanál EU/UK (Narrow), 869.618 MHz se šířkou pásma 62.5 kHz, sahá až do 869.649 MHz: méně než 1 kHz pod horní okraj podpásma. Signál musí zůstat uvnitř pásma při každé teplotě. K tomu je potřeba teplotně kompenzovaný krystal (TCXO). Skoro každá současná deska ho má; starší desky bez něj, například Heltec V2, ujíždějí příliš, aby při 62.5 kHz fungovaly spolehlivě.

### Poznámky k zemím {#countries}

- **Členské státy EU** musí toto dílčí pásmo za těchto podmínek zpřístupnit (rozhodnutí 2006/771/ES, článek 3).
- **Spojené království:** stejné limity, v dokumentu Ofcom [IR 2030](https://www.ofcom.org.uk/spectrum/radio-equipment/short-range-devices).
- **Švýcarsko a Lichtenštejnsko:** stejné limity, v dokumentu OFCOM [RIR1008-09](https://www.ofcomnet.ch/api/rir/1008/09).
- **Norsko:** stejné limity, v [nařízení o všeobecných oprávněních](https://lovdata.no/dokument/SF/forskrift/2012-01-19-77) (fribruksforskriften).

Tyto poznámky nejsou právní rada. Pravidla se mění; když si nejsi jistý, ověř si to u svého národního regulátora.

## Kontrolní seznam pro nasazení {#checklist}

- [ ] Majitel místa souhlasil a k repeateru se dostaneš kvůli údržbě.
- [ ] Deska běží na firmwaru **Repeater** a anténa byla připojená před prvním zapnutím.
- [ ] Heslo správce je změněné.
- [ ] Rádio odpovídá [presetu pro tvou oblast](/guides/settings/) (`get radio`).
- [ ] Je nastaveno `set dutycycle 10`.
- [ ] Vysílací výkon plus zisk antény zůstávají v limitu 500 mW e.r.p.
- [ ] Jméno, poloha a `owner.info` jsou nastavené, aby ostatní věděli, kdo ho provozuje.
- [ ] Hodiny jsou nastavené (`clock`).
- [ ] Krabice je utěsněná, má odtokový nebo odvětrávací otvor a kabel má odkapávací smyčku.
- [ ] Baterie a panel jsou dimenzované na nejhorší zimní měsíc.
- [ ] Před odchodem z místa jsi ho otestoval z dálky pomocí aplikace.
- [ ] Tvoje místní skupina ví, že běží.
