---
title: Průvodce repeaterem
lead: Repeater umístěný vysoko předává zprávy všem v okolí, třeba v celém městě nebo údolí. Vyber místo, napájej ho ze slunce, nastav ho a dodržuj zákon.
description: 'Naplánuj, napájej, nastav a legálně provozuj repeater MeshCore v Evropě: výběr místa, dimenzování solárního napájení, nastavení v CLI, limity výkonu a střídy vysílání na 868 MHz.'
eyebrow: 868 MHz · až 500 mW · bez licence
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '7c7e3be3'
  seeded: '2026-10-31'
  fields: {title: '4608abcd', lead: 'bc670c65', description: '9e483ce5', eyebrow: '9fd33416'}
  sections: ['05ee477a', '938c518c', '766086be', '70faf508', '8bc641aa', '399cd683', 'e9dedb7b', '92beca03', '17634750', 'cadf6024', 'e9cc6834', '2e6e59ca', 'fb44b8db']
  blocks: ['20ac0371', 'ed2b1adf', '432543ee', '7af42c89', 'd0f7543a', '9ef3580f', '3476aef7', '1bab7bec', '6a7c4493', 'dbd9fa1f', 'aa06d32b', '9958aad3', 'd162b028', 'cca1bbdf', '64ef011d', 'e7f16724', 'd2e34ff0', 'bb195cfc', '8d080bb3', '2b1d995b', '210f1b66', 'dc7419d2', 'bdc66db0', 'b59f248c', '7184bd63', 'de5a24f9', 'f5cfb426', '48c7422f', '9d3c0836', 'da8a6af3', '240126df', '8aac2b33', '81a475b8', 'a53e42b5', '36ff1db4', 'e4ca8602', 'e4594afd', '3b24b8e9', '58330858', '68f2966e', 'd7418228', '23536e60', 'cbc5c2d1', '2ea02ba9', '92540256', '6e21f681', 'a8c12311', '3382ae7f', 'cdeafb0f', '1b1319d2']
---

Repeatery nesou celou mesh. Companiony, tedy rádia, ze kterých píšeš zprávy,
zprávy dál nepředávají. Bez repeaterů tak zastihneš jen lidi v přímém dosahu.
Repeater na správném místě rozšíří mesh pro všechny kolem. Tento průvodce
vychází z firmwaru MeshCore v1.18.0.

Než začneš, ozvi se své [místní skupině](/community/). Ví, kde chybí pokrytí,
[jaký preset se ve vaší oblasti používá](/guides/settings/) a jak se repeatery
pojmenovávají. Na [mapách pokrytí](/map/) najdeš repeatery ve svém okolí. Pozdrav
ostatní ve veřejných nebo místních [kanálech](/guides/channels/).

## Potřebuješ ho? {#need}

Repeater vyšle dál každou flood zprávu, kterou zachytí. Všechny repeatery v
dosahu sdílejí stejný vysílací čas. Kde k tobě mesh už dosáhne, přidá další
repeater provoz, a pokrytí nezlepší. Často ti stačí companion umístěný vysoko,
v podkrovním okně nebo na balkoně.

Repeater postav tam, kde chybí pokrytí:

- [mapy pokrytí](/map/) neukazují žádný repeater ve tvém okolí, nebo jen takové,
  které tvůj companion neslyší;
- tvoje místní skupina říká, že oblast repeater potřebuje.

## Vyber místo {#site}

Výška je důležitější než výkon. LoRa na 868 MHz se nejlépe šíří při volné
přímé viditelnosti. Kopce, budovy a hustý les ubírají mnohem víc dosahu, než
kolik vrátí pár miliwattů navíc.

- **Jdi vysoko.** Střecha, stožár, vysoká budova nebo kopec pokryjí mnohem víc
  než parapet. Pomůže i pár metrů nad okolními střechami.
- **Nech anténu volnou.** Namontuj ji nad okraj střechy, dál od kovu, okapů a
  jiných antén.
- **Ověř si výhled.** Nástroje jako [HeyWhatsThat](https://www.heywhatsthat.com/)
  ukážou, co je z daného místa vidět. Pokud nějaké místo vidíš, repeater tam
  je v dosahu.
- **Nech volný prostor.** Rádiová cesta potřebuje kolem přímé spojnice i trochu
  volného místa, ne jen samotnou čáru. Na dlouhé vzdálenosti má být střed
  cesty o několik metrů nad překážkami.
- **Požádej o svolení.** Získej souhlas majitele střechy nebo stožáru. Domluv
  se, jak se k repeateru dostaneš kvůli údržbě.

## Hardware {#hardware}

- **Deska.** Vyber úspornou desku nRF52, třeba
  [Heltec T114](/devices/), RAK WisBlock nebo SenseCAP Solar Node. Desky ESP32
  mají větší spotřebu (stránka se zařízeními je označuje jako High). Na
  solární napájení se proto hodí špatně.
- **Anténa.** Použij anténu určenou pro 868 MHz, namontovanou svisle. Typy,
  konektory, kabely a montáž popisuje [průvodce anténami](/guides/antenna/).
  Zisk antény se započítává do zákonného limitu výkonu, viz
  [Zákonné limity](#legal).
- **Kabel.** Koaxiální kabel měj krátký, nebo použij kabel s nízkým útlumem.
  Na 868 MHz může pár metrů tenkého kabelu spolknout polovinu výkonu.
- **Krabička.** Vodotěsná krabička (IP65 nebo lepší) s kabelovou průchodkou,
  větracím nebo odtokovým otvorem proti kondenzaci a světlou barvou nebo
  stříškou proti slunci. Baterie trpí horkem a pod bodem mrazu je nenabiješ.
- **Blesk.** Anténa na střeše přitahuje blesky. Uzemni ji podle místních
  předpisů, nebo ji namontuj tam, kde by úder nezasáhl elektroinstalaci budovy.

## Napájení a dimenzování solárního panelu {#power}

Solární repeater musí přežít nejtemnější týdny zimy. Dimenzuj ho právě na ně:

1. **Změř spotřebu.** Nech nastavený repeater běžet den přes USB měřič.
   Odečti spotřebovanou energii ve watthodinách (Wh). Provoz ve tvé oblasti
   číslo ovlivňuje, takže měř pokud možno na místě.
2. **Přidej rezervu.** Kapacitu baterie plánuj alespoň na 5 až 7 dní
   bez využitelného slunce.
3. **Zjisti zimní osvit.** Bezplatný
   [nástroj PVGIS](https://re.jrc.ec.europa.eu/pvg_tools/en/) od EU ukáže pro
   libovolné místo, kolik energie panel vyrobí za měsíc. Vezmi měsíc s
   nejméně sluncem.
4. **Dimenzuj panel.** Panel musí v tom nejhorším měsíci každý den nahradit
   spotřebu, i s rezervou na ztráty při nabíjení.

Příklad výpočtu s předpokládanými čísly: repeater se spotřebou 1 Wh denně
potřebuje na týden rezervy baterii alespoň 7 Wh, tedy asi 2 Ah využitelné
kapacity při 3,7 V. Pokud podle PVGIS dá panel 1 W na tvém místě v prosinci
0,5 Wh denně, potřebuješ panel alespoň 2 W. Panel 3 až 5 W ti nechá rezervu na
mraky, sníh a stárnutí.

## Nastavení {#config}

**Nahraj firmware.** Otevři [webový flasher](https://flasher.meshcore.io) a
vyber pro svou desku firmware **Repeater**. Postup nahrání najdeš v sekci
[Začínáme](/get-started/#flash).

**Nastav ho přes USB.** Repeater nech připojený k počítači a otevři
[config.meshcore.io](https://config.meshcore.io) nebo konzoli flasheru. Můžeš
použít i libovolný sériový terminál na 115200 baud. Nejdůležitější příkazy:

| Co | Příkaz |
|---|---|
| Změna hesla správce | `password <new password>` |
| Pojmenování | `set name <name>` |
| Preset rádia: frekvence, šířka pásma, SF, CR (projeví se po restartu) | `set radio 869.618,62.5,8,8` |
| Limit střídy vysílání v procentech | `set dutycycle 10` |
| Vysílací výkon rádiového čipu v dBm | `set tx <dBm>` |
| Poloha, aby se zobrazil na mapách | `set lat <degrees>` a `set lon <degrees>` |
| Kontakt pro ostatní provozovatele | `set owner.info <text>` |
| Počet hodin mezi flood adverty, které slyší celá mesh | `set flood.advert.interval <hours>` |
| Okamžité ohlášení | `advert` |
| Restart | `reboot` |

Výchozí heslo správce je `password`. Kdo se s ním přihlásí, stane se správcem.
Změň ho dřív, než repeater začne vysílat.

Příklad `set radio` výše platí pro EU/UK (Narrow). Použij místo něj hodnoty
presetu pro svou oblast. [Doporučená nastavení](/guides/settings/) je uvádějí
po jednotlivých zemích.

**Nastav hodiny.** Bez modulu hodin (RTC) repeater při každém výpadku proudu
ztratí čas a naběhne s datem v květnu 2024. Za běhu se jeho hodiny navíc
rozcházejí: předbíhají se nebo zpožďují. Hodiny proto čas od času nastav:
přihlas se vzdáleně z aplikace a použij `clock sync`, nebo nastav čas přes
USB. S modulem RTC to potřebuješ jen zřídka. Modul udrží čas i při výpadku
proudu a rozchází se mnohem méně.

**Spravuj ho na dálku.** Jakmile je repeater v mesh, přihlas se k němu z
aplikace MeshCore heslem správce. Tam si přečteš jeho stav a stejné příkazy
zadáš přes rádio. Některé příkazy fungují jen přes USB, například `set freq` a
obnovení továrního nastavení `erase`.

**Zachovej jeho identitu.** Před příkazem erase zadej přes USB `get prv.key`.
Zobrazený soukromý klíč si bezpečně ulož. Po smazání zadej `set prv.key <key>`
a `reboot`, a repeater dostane zpět svou původní identitu. Uzly, které ho
znají, ho pak najdou pod stejným prefixem.

Úplný seznam příkazů najdeš v
[referenční příručce MeshCore CLI](https://github.com/meshcore-dev/MeshCore/blob/main/docs/cli_commands.md).

## Aktualizace vzduchem {#update}

Když už repeater visí vysoko, aktualizuješ ho ze země. Přihlas se z aplikace
MeshCore heslem správce, otevři jeho příkazový řádek a zadej `start ota`. Další
postup závisí na desce. Jiné desky odpoví `Error` a ty aktualizuješ přes USB.

**Desky nRF52**, například RAK, Heltec T114, Seeed XIAO a SenseCAP Solar:

1. Z [webového flasheru](https://flasher.meshcore.io) si stáhni **ZIP** s
   novým firmwarem pro svou desku.
2. Zadej `start ota`. Repeater odpoví `OK` a objeví se přes Bluetooth
   jako `<board>_OTA`, například `RAK4631_OTA`.
3. V telefonu otevři aplikaci nRF Device Firmware Update, vyber ZIP a
   repeater a spusť nahrávání. Trvá to několik minut.

Na desku nRF52 nainstaluj ještě před montáží
[bootloader OTAFIX](https://github.com/oltaco/Adafruit_nRF52_Bootloader_OTAFIX).
S původním bootloaderem opravíš nepovedenou aktualizaci jen přes USB. S OTAFIX
se deska vrátí do režimu aktualizace a ty to zkusíš znovu přes Bluetooth.

**Desky ESP32**, například Heltec V3 a V4:

1. Z webového flasheru si stáhni **nesloučený** soubor `.bin` pro svou desku:
   ten, který nemá v názvu „merged“.
2. Zadej `start ota`. Repeater otevře WiFi síť s názvem `MeshCore-OTA` a
   odpoví adresou své stránky pro nahrání.
3. V dosahu WiFi připoj telefon nebo notebook k této síti, otevři adresu a
   nahraj soubor.

## Zákonné limity {#legal}

{{< callout type="legal" verified="2026-10-02" >}}
Evropské presety MeshCore leží v podpásmu **869.40-869.65 MHz**. V EU, ve
Spojeném království, ve Švýcarsku a v Norsku ho smí zařízení krátkého dosahu
používat bez licence, v těchto mezích:

- vyzářený výkon nejvýše **500 mW e.r.p.**;
- střída vysílání nejvýše **10%**: každé zařízení smí vysílat nejvýše 360
  sekund za hodinu. Zařízení může místo toho použít listen-before-talk
  s adaptivní frekvenční agilitou podle ETSI EN 300 220-2;
- celý signál, široký nejvýše 250 kHz, musí zůstat uvnitř podpásma.

Pásmo je sdílené: nesmíš rušit licencované služby a ostatní mohou rušit tebe.
Rádio musí mít označení CE (ve Velké Británii CE nebo UKCA).
{{< /callout >}}

Zdroje: [doporučení CEPT ERC 70-03](https://docdb.cept.org/document/845),
příloha 1, pásmo h1.7;
[rozhodnutí Komise 2006/771/ES](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02006D0771(01)-20250123)
a jeho změny;
[ETSI EN 300 220-2](https://www.etsi.org/deliver/etsi_en/300200_300299/30022002/03.03.01_60/en_30022002v030301p.pdf),
pásmo O.

### Power: e.r.p. and your antenna {#erp}

The limit applies to the *radiated* power, measured against a simple dipole
antenna (e.r.p.). Antenna gain counts; cable loss subtracts. Makers state
antenna gain in dBi, which is 2.15 dB more than the same gain in dBd
(relative to a dipole). Keep this sum at or below 27 dBm (500 mW):

> transmit power (dBm) + antenna gain (dBi) − cable loss (dB) − 2.15 ≤ 27

- A board transmitting 22 dBm into a 5 dBi antenna through 1 dB of cable:
  22 + 5 − 1 − 2.15 = 23.85 dBm, about 240 mW e.r.p. Within the limit.
- A board with a 30 dBm (1 W) amplifier into a 3 dBi antenna:
  30 + 3 − 2.15 = 30.85 dBm, about 1.2 W e.r.p. Over the limit; lower the
  transmit power.

`set tx` sets the output of the LoRa chip, in dBm. The SX1262 chip itself
tops out at 22 dBm; the firmware does not check the number you enter. Boards with an extra
amplifier, such as the Heltec V4 or the Station G2, transmit much more than
the number you set. Check the manufacturer's table before you set it, and
start low.

### Střída vysílání {#duty-cycle}

Repeater vysílá pro všechny kolem, a svůj vysílací čas proto spotřebuje
rychleji než companion. Omezovač střídy vysílání v MeshCore má výchozí hodnotu
50%, což je víc, než toto pásmo dovoluje. Na každém repeateru ho nastav na 10%:

```text
set dutycycle 10
```

### Přesnost frekvence {#frequency}

Kanál EU/UK (Narrow), 869.618 MHz se šířkou pásma 62.5 kHz, sahá až
k 869.649 MHz: méně než 1 kHz pod horní hranicí podpásma. Signál musí
zůstat uvnitř pásma při jakékoli teplotě. K tomu je potřeba teplotně
kompenzovaný krystal (TCXO). Má ho téměř každá současná deska. Starší desky
bez něj, například Heltec V2, se rozladí příliš daleko a na 62.5 kHz
nefungují spolehlivě.

### Poznámky k jednotlivým zemím {#countries}

- **Členské státy EU** musí toto dílčí pásmo za těchto podmínek zpřístupnit
  (rozhodnutí 2006/771/ES, článek 3).
- **Spojené království:** stejné limity, v předpisu Ofcom
  [IR 2030](https://www.ofcom.org.uk/spectrum/radio-equipment/short-range-devices).
- **Švýcarsko a Lichtenštejnsko:** stejné limity, v předpisu OFCOM
  [RIR1008-09](https://www.ofcomnet.ch/api/rir/1008/09).
- **Norsko:** stejné limity, v
  [nařízení o všeobecných oprávněních](https://lovdata.no/dokument/SF/forskrift/2012-01-19-77)
  (fribruksforskriften).

Tyto poznámky nejsou právní rada. Pravidla se mění. Když si nejsi jistý,
ověř si je u svého národního regulačního úřadu.

## Kontrolní seznam před nasazením {#checklist}

- [ ] Majitel místa souhlasí a k repeateru se dostaneš kvůli údržbě.
- [ ] Na desce běží firmware **Repeater** a anténa byla připojená ještě před
      prvním zapnutím.
- [ ] Heslo správce je změněné.
- [ ] Rádio odpovídá [presetu tvé oblasti](/guides/settings/) (`get radio`).
- [ ] Je nastaveno `set dutycycle 10`.
- [ ] Vysílací výkon se ziskem antény nepřekračuje 500 mW e.r.p.
- [ ] Název, poloha a `owner.info` jsou nastavené, aby ostatní věděli, kdo
      repeater provozuje.
- [ ] Hodiny jsou nastavené (`clock`).
- [ ] Krabička je utěsněná, s odtokovým nebo větracím otvorem, a kabel má
      okapovou smyčku.
- [ ] Baterie a panel jsou dimenzované na nejhorší zimní měsíc.
- [ ] Před odchodem z místa jsi repeater otestoval z dálky v aplikaci.
- [ ] Tvoje místní skupina ví, že repeater běží.
