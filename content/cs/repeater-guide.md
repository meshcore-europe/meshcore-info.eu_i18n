---
title: Průvodce repeaterem
lead: Repeater umístěný vysoko předává zprávy všem kolem sebe, napříč celým městem nebo údolím. Vyber místo, napájej ho ze slunce, nastav ho a dodržuj zákon.
description: 'Naplánuj, napájej, nastav a legálně provozuj repeater MeshCore v Evropě: výběr místa, dimenzování solárního napájení, nastavení v CLI, limity výkonu a střídy provozu v pásmu 868 MHz.'
eyebrow: 868 MHz · až 500 mW · bez licence
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '3e38a8c6'
  seeded: '2026-11-04'
  fields: {title: '4608abcd', lead: 'bc670c65', description: '9e483ce5', eyebrow: '9fd33416'}
  sections: ['05ee477a', '938c518c', '824ab38e', '662ea23c', '70faf508', '8bc641aa', '399cd683', 'e9dedb7b', '92beca03', '17634750', 'cadf6024', 'e9cc6834', '2e6e59ca', 'fb44b8db']
  blocks: ['20ac0371', 'ed2b1adf', '432543ee', '7af42c89', 'd0f7543a', '9ef3580f', '3476aef7', '1bab7bec', 'bbea9a0c', '2b9fab3b', 'b13d1947', 'c2bad16f', '636edc86', 'c2d6bcd1', '957ae975', '98874949', '96d1ebad', 'dbd9fa1f', 'aa06d32b', '9958aad3', 'd162b028', 'cca1bbdf', '64ef011d', 'e7f16724', 'd2e34ff0', 'bb195cfc', '8d080bb3', '2b1d995b', '210f1b66', 'dc7419d2', 'bdc66db0', 'b59f248c', '7184bd63', 'de5a24f9', 'f5cfb426', '48c7422f', '9d3c0836', 'da8a6af3', '240126df', '8aac2b33', '81a475b8', 'a53e42b5', '36ff1db4', 'e4ca8602', 'e4594afd', '3b24b8e9', '58330858', '68f2966e', 'd7418228', '23536e60', 'cbc5c2d1', '2ea02ba9', '92540256', '6e21f681', 'a8c12311', '3382ae7f', 'cdeafb0f', '1b1319d2']
---

Na repeaterech stojí celý mesh. Companiony, tedy vysílačky, ze kterých posíláš zprávy, je dál nepředávají. Bez repeaterů proto zastihneš jen lidi v přímém dosahu. Repeater na správném místě rozšíří mesh všem kolem sebe. Tento návod vychází z firmwaru MeshCore v1.18.0.

Než začneš, promluv si se svou [místní skupinou](/community/). Její členové vědí, kde chybí pokrytí, [jaký preset se ve tvé oblasti používá](/guides/settings/) a jak se repeatery pojmenovávají. Na [mapách pokrytí](/map/) si vyhledej repeatery ve svém okolí a pozdrav ostatní ve veřejných nebo místních [kanálech](/guides/channels/).

## Potřebuješ ho? {#need}

Repeater přeposílá každou flood zprávu, kterou zachytí, a všechny repeatery v dosahu sdílejí stejný vysílací čas. Kde už na tebe mesh dosáhne, přidá další repeater provoz, ne pokrytí. Možná ti bude stačit companion umístěný vysoko, v půdním okně nebo na balkoně.

Repeater postav tam, kde chybí pokrytí:

- na [mapách pokrytí](/map/) není poblíž žádný repeater, nebo jsou tam jen takové, které tvůj companion neslyší;
- tvoje místní skupina říká, že oblast repeater potřebuje.

## Vyber místo {#site}

Výška je důležitější než výkon. LoRa na 868 MHz se nejlépe šíří při přímé viditelnosti bez překážek. Kopce, budovy a husté stromy ti vezmou mnohem víc dosahu, než kolik vrátí několik miliwattů navíc.

- **Jdi do výšky.** Střecha, stožár, vysoká budova nebo kopec pokryje mnohem víc
  než parapet. Pomůže i pár metrů nad okolními střechami.
- **Dej anténě volný výhled.** Namontuj ji nad okraj střechy, dál od kovu, okapů
  a jiných antén.
- **Ověř si výhled.** Nástroje jako [HeyWhatsThat](https://www.heywhatsthat.com/)
  ukážou, co je z daného místa vidět. Aplikace MeshCore
  [spočítá, kam odtud repeater dosáhne](#check-site).
- **Nech volný prostor.** Rádiová cesta potřebuje volný prostor kolem přímé
  spojnice, nejen samotnou spojnici. Na 868 MHz je to asi 20 m kolem středu
  cesty dlouhé 5 km. Na cestě dlouhé 20 km je to asi 40 m.
- **Požádej o svolení.** Získej souhlas majitele střechy nebo stožáru a domluv
  se, jak se k repeateru dostaneš kvůli údržbě.

### Ověř místo v aplikaci {#check-site}

Aplikace MeshCore má od verze 1.33 tyto nástroje v nabídce pod **Tools**.
Fungují i bez připojené vysílačky.

- **Line of Sight** vykreslí terén mezi 2 body a prostor, který signál nad ním
  potřebuje. Dlouze podrž 2 body na mapě nebo klepni na repeatery.
- **Antenna Coverage** ukáže na mapě, kam dosáhne anténa v 1 bodě.
  Dlouze podrž bod nebo klepni na repeater. Přidej další body a porovnej místa.

Na počítači zvol v nabídce nástroje **Add Point** a zadej souřadnice.

Oba nástroje na začátku počítají s anténou na tvém stanovišti ve výšce 5 m, takže
plánovanou výšku zadej v nastavení nástroje. Antenna Coverage na začátku počítá
s přijímací anténou ve výšce 1 m. Bez připojené vysílačky začíná Line of Sight
na 915 MHz: v jeho nastavení zadej frekvenci své [předvolby](/guides/settings/).

Nástroje vycházejí z výškových dat a tvoje rádio netestují. Stromy a nové
budovy si ověř sám, pak vezmi companion na místo a podívej se, které
repeatery slyší.

![Line of Sight v aplikaci MeshCore: terén mezi 2 body a prostor, který nad ním signál potřebuje](/media/guides/line-of-sight.webp)

![Antenna Coverage v aplikaci MeshCore: oblast na mapě, kam dosáhne anténa na kopci](/media/guides/antenna-coverage.webp)

## Hardware {#hardware}

- **Deska.** Vyber úspornou desku nRF52, například [Heltec T114](/devices/), RAK WisBlock nebo SenseCAP Solar Node. Desky ESP32 mají vyšší spotřebu (na stránce zařízení mají označení High), takže se na solární napájení provozují těžko.
- **Anténa.** Použij anténu určenou pro 868 MHz a namontuj ji svisle. Typy, konektory, kabely a montáž popisuje [návod k anténám](/guides/antenna/). Zisk antény se započítává do zákonného limitu výkonu, viz [Zákonné limity](#legal).
- **Kabel.** Koaxiální kabel měj krátký, nebo použij kabel s nízkým útlumem. Na 868 MHz může pár metrů tenkého kabelu sebrat polovinu výkonu.
- **Krabička.** Použij krabičku odolnou proti počasí (IP65 nebo lepší) s kabelovou průchodkou a s větracím nebo odtokovým otvorem proti kondenzaci. Měla by mít světlou barvu nebo stínítko proti slunci. Baterie špatně snášejí horko a pod bodem mrazu je nemůžeš nabíjet.
- **Blesk.** Anténa na střeše je pro blesk terč. Dodržuj místní pravidla pro uzemnění, nebo ji namontuj tam, kde by úder nezasáhl elektroinstalaci budovy.

## Napájení a dimenzování solární sestavy {#power}

Solární repeater musí přežít nejtemnější týdny zimy. Podle nich ho dimenzuj:

1. **Změř spotřebu.** Nech nastavený repeater běžet jeden den přes USB měřič spotřeby. Odečti spotřebovanou energii ve watthodinách (Wh). Hodnotu ovlivňuje provoz ve tvé oblasti, takže měř pokud možno přímo na místě.
2. **Přidej rezervu.** Kapacitu baterie plánuj alespoň na 5 až 7 dní bez využitelného slunce.
3. **Zjisti zimní osvit.** Bezplatný [nástroj PVGIS](https://re.jrc.ec.europa.eu/pvg_tools/en/) od EU ukáže pro libovolné místo, kolik energie panel vyrobí za měsíc. Počítej s měsícem, kdy je nejméně slunce.
4. **Urči velikost panelu.** Panel musí i v tomto nejhorším měsíci každý den nahradit denní spotřebu a pokrýt ztráty při nabíjení.

Příklad výpočtu s předpokládanými hodnotami: repeater se spotřebou 1 Wh za den potřebuje na týdenní rezervu baterii s kapacitou alespoň 7 Wh, tedy přibližně 2 Ah využitelné kapacity při 3.7 V. Pokud PVGIS uvádí, že panel 1 W u tebe v prosinci vyrobí 0.5 Wh za den, potřebuješ panel alespoň 2 W. Panel 3 až 5 W ti nechá rezervu na mraky, sníh a stárnutí.

## Nastavení {#config}

**Nahraj firmware.** Otevři [webový flasher](https://flasher.meshcore.io) a vyber firmware **Repeater** pro svou desku. Postup nahrání najdeš v části [Začínáme](/get-started/#flash).

**Nastav ho přes USB.** Nech repeater připojený k počítači a otevři [config.meshcore.io](https://config.meshcore.io) nebo konzoli ve flasheru. Můžeš použít i libovolný sériový terminál s rychlostí 115200 baud. Nejdůležitější příkazy:

| Co | Příkaz |
|---|---|
| Změna hesla správce | `password <new password>` |
| Pojmenování | `set name <name>` |
| Rádiový preset: frekvence, šířka pásma, SF, CR (projeví se po restartu) | `set radio 869.618,62.5,8,8` |
| Limit střídy provozu v procentech | `set dutycycle 10` |
| Vysílací výkon rádiového čipu v dBm | `set tx <dBm>` |
| Poloha, aby se repeater zobrazil na mapách | `set lat <degrees>` a `set lon <degrees>` |
| Kontaktní údaje pro ostatní provozovatele | `set owner.info <text>` |
| Počet hodin mezi flood adverty, tedy těmi, které slyší celý mesh | `set flood.advert.interval <hours>` |
| Okamžité ohlášení | `advert` |
| Restart | `reboot` |

Výchozí heslo správce je `password` a kdokoli se s ním přihlásí, stane se správcem. Změň ho dřív, než repeater začne vysílat.

Příklad `set radio` výše platí pro EU/UK (Narrow). Místo něj použij hodnoty presetu pro svou oblast: najdeš je podle zemí v části [Doporučená nastavení](/guides/settings/).

**Nastav hodiny.** Bez modulu hodin (RTC) repeater při každém výpadku napájení ztratí čas a po startu začíná v květnu 2024. Za běhu se mu hodiny navíc rozcházejí: stále víc se předbíhají nebo zpožďují. Proto hodiny občas nastav: přihlas se vzdáleně z aplikace a použij `clock sync`, nebo nastav čas přes USB. S modulem RTC to potřebuješ jen zřídka: udrží čas i při výpadku napájení a rozchází se mnohem méně.

**Spravuj ho na dálku.** Jakmile je repeater v meshi, přihlas se k němu z aplikace MeshCore heslem správce. V aplikaci vidíš jeho stav a stejné příkazy zadáváš přes rádio. Některé příkazy fungují jen přes USB, například `set freq` a tovární reset `erase`.

**Zachovej jeho identitu.** Před smazáním zadej přes USB `get prv.key` a soukromý klíč, který se zobrazí, si bezpečně ulož. Po smazání vrátíš repeateru původní identitu příkazem `set prv.key <key>` a následným `reboot`. Uzly, které ho znají, ho pak najdou pod stejným prefixem.

Úplný seznam příkazů najdeš v [referenční příručce MeshCore CLI](https://github.com/meshcore-dev/MeshCore/blob/main/docs/cli_commands.md).

## Bezdrátová aktualizace {#update}

Když už je repeater nahoře, aktualizuješ ho ze země. Přihlas se z aplikace MeshCore heslem správce, otevři jeho příkazový řádek a zadej `start ota`. Další postup závisí na desce. Jiné desky odpoví `Error` a aktualizuješ je přes USB.

**Desky nRF52**, například RAK, Heltec T114, Seeed XIAO a SenseCAP Solar:

1. Ve [webovém flasheru](https://flasher.meshcore.io) si stáhni **ZIP** s novým firmwarem pro svou desku.
2. Zadej `start ota`. Repeater odpoví `OK` a přes Bluetooth se zobrazí jako `<board>_OTA`, například `RAK4631_OTA`.
3. V telefonu otevři aplikaci nRF Device Firmware Update, vyber ZIP a repeater a spusť nahrávání. Trvá to několik minut.

Než desku nRF52 vyneseš nahoru, nainstaluj na ni [bootloader OTAFIX](https://github.com/oltaco/Adafruit_nRF52_Bootloader_OTAFIX). Se standardním bootloaderem opravíš nepovedenou aktualizaci jen přes USB. S OTAFIX se deska vrátí do aktualizačního režimu a zkusíš to znovu přes Bluetooth.

**Desky ESP32**, například Heltec V3 a V4:

1. Ve webovém flasheru si stáhni **non-merged** `.bin` pro svou desku: soubor, který nemá v názvu „merged“.
2. Zadej `start ota`. Repeater otevře WiFi síť s názvem `MeshCore-OTA` a odpoví adresou své stránky pro nahrání.
3. V dosahu WiFi připoj telefon nebo notebook k této síti, otevři danou adresu a nahraj soubor.

## Zákonné limity {#legal}

{{< callout type="legal" verified="2026-10-02" >}}
Evropské presety MeshCore leží v dílčím pásmu **869.40-869.65 MHz**. V EU, ve Spojeném království, ve Švýcarsku a v Norsku je toto pásmo otevřené zařízením krátkého dosahu bez licence, a to v těchto mezích:

- vyzářený výkon nejvýše **500 mW e.r.p.**;
- střída provozu nejvýše **10 %**: každé zařízení smí vysílat nejvýše 360 sekund za hodinu. Zařízení může místo toho používat listen-before-talk s adaptivní frekvenční agilitou podle ETSI EN 300 220-2;
- celý signál o šířce nejvýše 250 kHz musí zůstat uvnitř dílčího pásma.

Pásmo je sdílené: nesmíš rušit licencované služby a ostatní mohou rušit tebe.
Rádio musí mít označení CE (ve Velké Británii CE nebo UKCA).
{{< /callout >}}

Zdroje: [Doporučení CEPT ERC 70-03](https://docdb.cept.org/document/845), příloha 1, pásmo h1.7; [rozhodnutí Komise 2006/771/ES](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02006D0771(01)-20250123) a jeho změny; [ETSI EN 300 220-2](https://www.etsi.org/deliver/etsi_en/300200_300299/30022002/03.03.01_60/en_30022002v030301p.pdf), pásmo O.

### Výkon: e.r.p. a tvoje anténa {#erp}

Limit se vztahuje na *vyzářený* výkon, měřený vůči jednoduché dipólové anténě (e.r.p.). Zisk antény se přičítá, útlum kabelu se odečítá. Výrobci uvádějí zisk antény v dBi, což je o 2.15 dB více než stejný zisk v dBd (vůči dipólu). Udrž tento součet na 27 dBm (500 mW) nebo níž:

> vysílací výkon (dBm) + zisk antény (dBi) − útlum kabelu (dB) − 2.15 ≤ 27

- Deska vysílá 22 dBm do antény 5 dBi přes kabel s útlumem 1 dB: 22 + 5 − 1 − 2.15 = 23.85 dBm, přibližně 240 mW e.r.p. To je v limitu.
- Deska se zesilovačem 30 dBm (1 W) vysílá do antény 3 dBi: 30 + 3 − 2.15 = 30.85 dBm, přibližně 1.2 W e.r.p. To je nad limitem, sniž vysílací výkon.

`set tx` nastavuje výstupní výkon čipu LoRa v dBm. Samotný čip SX1262 dosáhne nejvýše 22 dBm a firmware zadanou hodnotu nekontroluje. Desky s přídavným zesilovačem, například Heltec V4 nebo Station G2, vysílají mnohem větším výkonem, než jaký nastavíš. Před nastavením si zkontroluj tabulku výrobce a začni na nízké hodnotě.

### Střída provozu {#duty-cycle}

Repeater vysílá pro všechny kolem sebe, takže svůj vysílací čas vyčerpá rychleji než companion. Omezovač střídy provozu má v MeshCore výchozí hodnotu 50 %, což je víc, než toto pásmo dovoluje. Na každém repeateru nastav 10 %:

```text
set dutycycle 10
```

### Přesnost frekvence {#frequency}

Kanál EU/UK (Narrow), 869.618 MHz se šířkou pásma 62.5 kHz, sahá až k 869.649 MHz: necelý 1 kHz pod horní hranicí dílčího pásma. Signál musí zůstat v pásmu při každé teplotě. K tomu je potřeba teplotně kompenzovaný krystal (TCXO). Má ho téměř každá současná deska. Starší desky bez něj, například Heltec V2, se rozlaďují příliš na to, aby na 62.5 kHz spolehlivě fungovaly.

### Poznámky k jednotlivým zemím {#countries}

- **Členské státy EU** musí toto dílčí pásmo za těchto podmínek zpřístupnit (rozhodnutí 2006/771/ES, článek 3).
- **Spojené království:** stejné limity, v dokumentu Ofcom [IR 2030](https://www.ofcom.org.uk/spectrum/radio-equipment/short-range-devices).
- **Švýcarsko a Lichtenštejnsko:** stejné limity, v dokumentu OFCOM [RIR1008-09](https://www.ofcomnet.ch/api/rir/1008/09).
- **Norsko:** stejné limity, v [předpisu o všeobecných oprávněních](https://lovdata.no/dokument/SF/forskrift/2012-01-19-77) (fribruksforskriften).

Tyto poznámky nejsou právní rada. Pravidla se mění. V případě pochybností se obrať na svůj národní regulační úřad.

## Kontrolní seznam před nasazením {#checklist}

- [ ] Majitel místa souhlasil a k repeateru se dostaneš kvůli údržbě.
- [ ] Na desce běží firmware **Repeater** a anténa byla připojená před prvním zapnutím.
- [ ] Heslo správce je změněné.
- [ ] Rádio odpovídá [presetu pro tvoji oblast](/guides/settings/) (`get radio`).
- [ ] Je nastaveno `set dutycycle 10`.
- [ ] Vysílací výkon plus zisk antény zůstává v limitu 500 mW e.r.p.
- [ ] Jméno, poloha a `owner.info` jsou nastavené, aby ostatní věděli, kdo repeater provozuje.
- [ ] Hodiny jsou nastavené (`clock`).
- [ ] Krabička je utěsněná, má odtokový nebo větrací otvor a kabel má odkapávací smyčku.
- [ ] Baterie a panel jsou dimenzované na nejhorší zimní měsíc.
- [ ] Před odchodem z místa máš repeater otestovaný z dálky v aplikaci.
- [ ] Tvoje místní skupina ví, že repeater běží.
