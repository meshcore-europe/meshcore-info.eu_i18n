---
title: Sprievodca opakovačom
lead: Opakovač umiestnený vysoko odovzdáva správy všetkým okolo seba, v celom meste alebo údolí. Vyber miesto, napájaj ho zo slnka, nastav ho a dodržuj zákon.
description: 'Naplánuj, napájaj, nastav a legálne prevádzkuj opakovač MeshCore v Európe: výber miesta, dimenzovanie solárneho napájania, nastavenia cez CLI, limity výkonu a pracovného cyklu v pásme 868 MHz.'
eyebrow: 868 MHz · do 500 mW · bez licencie
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '7c7e3be3'
  seeded: '2026-11-02'
  fields: {title: '4608abcd', lead: 'bc670c65', description: '9e483ce5', eyebrow: '9fd33416'}
  sections: ['05ee477a', '938c518c', '766086be', '70faf508', '8bc641aa', '399cd683', 'e9dedb7b', '92beca03', '17634750', 'cadf6024', 'e9cc6834', '2e6e59ca', 'fb44b8db']
  blocks: ['20ac0371', 'ed2b1adf', '432543ee', '7af42c89', 'd0f7543a', '9ef3580f', '3476aef7', '1bab7bec', '6a7c4493', 'dbd9fa1f', 'aa06d32b', '9958aad3', 'd162b028', 'cca1bbdf', '64ef011d', 'e7f16724', 'd2e34ff0', 'bb195cfc', '8d080bb3', '2b1d995b', '210f1b66', 'dc7419d2', 'bdc66db0', 'b59f248c', '7184bd63', 'de5a24f9', 'f5cfb426', '48c7422f', '9d3c0836', 'da8a6af3', '240126df', '8aac2b33', '81a475b8', 'a53e42b5', '36ff1db4', 'e4ca8602', 'e4594afd', '3b24b8e9', '58330858', '68f2966e', 'd7418228', '23536e60', 'cbc5c2d1', '2ea02ba9', '92540256', '6e21f681', 'a8c12311', '3382ae7f', 'cdeafb0f', '1b1319d2']
---

Na opakovačoch (repeateroch) stojí sieť mesh. Companiony, teda rádiá, z ktorých píšeš správy, ich
ďalej neposielajú. Bez opakovačov sa preto spojíš len s ľuďmi v priamom dosahu. Opakovač na správnom
mieste rozšíri sieť všetkým okolo seba. Tento návod vychádza z firmvéru MeshCore
v1.18.0.

Skôr než začneš, porozprávaj sa so svojou [miestnou skupinou](/community/). Ľudia v nej vedia, kde
chýba pokrytie, [aká predvoľba sa v tvojej oblasti používa](/guides/settings/) a ako opakovače pomenúvať. Na
[mapách pokrytia](/map/) si pozri opakovače vo svojom okolí a pozdrav ostatných na verejných
alebo miestnych [kanáloch](/guides/channels/).

## Potrebuješ ho? {#need}

Opakovač vysiela ďalej každú flood správu, ktorú zachytí, a všetky opakovače v dosahu
sa delia o ten istý vysielací čas. Kde ťa sieť už pokrýva, ďalší
opakovač pridá prevádzku, nie pokrytie. Možno ti postačí companion umiestnený vysoko, v podkrovnom
okne alebo na balkóne.

Opakovač postav tam, kde chýba pokrytie:

- na [mapách pokrytia](/map/) nevidíš pri sebe žiadny opakovač alebo len také, ktoré tvoj
  companion nepočuje;
- podľa tvojej miestnej skupiny oblasť opakovač potrebuje.

## Vyber miesto {#site}

Výška je dôležitejšia než výkon. LoRa na 868 MHz sa najlepšie šíri pri priamej
viditeľnosti bez prekážok. Kopce, budovy a husté stromy uberú oveľa viac dosahu, než koľko vrátí
pár miliwattov navyše.

- **Choď do výšky.** Strecha, stožiar, vysoká budova alebo kopec pokryjú oveľa viac
  než parapet. Pomôže aj pár metrov nad okolitými strechami.
- **Nechaj anténu vo voľnom priestore.** Namontuj ju nad okraje striech, ďalej od
  kovu, odkvapov a iných antén.
- **Over si výhľad.** Nástroje ako [HeyWhatsThat](https://www.heywhatsthat.com/)
  ukážu, čo je z daného miesta vidieť. Ak nejaké miesto vidíš, opakovač na ňom
  je v dosahu.
- **Nechaj voľný priestor.** Rádiová trasa potrebuje voľný priestor aj okolo priamej
  spojnice, nielen samotnú spojnicu. Na dlhých vzdialenostiach by mal stred trasy
  prechádzať niekoľko metrov nad prekážkami.
- **Vypýtaj si povolenie.** Získaj súhlas vlastníka strechy alebo stožiara a dohodni sa,
  ako sa k opakovaču dostaneš pri údržbe.

## Hardvér {#hardware}

- **Doska.** Vyber si úspornú dosku nRF52, napríklad
  [Heltec T114](/devices/), RAK WisBlock alebo SenseCAP Solar Node. Dosky ESP32
  odoberajú viac energie (na stránke so zariadeniami majú označenie High), preto
  je ich napájanie zo slnka náročné.
- **Anténa.** Použi anténu určenú pre 868 MHz, namontovanú zvisle. Typy, konektory, kábel a
  montáž opisuje [návod k anténam](/guides/antenna/). Zisk antény sa započítava do zákonného
  limitu výkonu, pozri
  [Zákonné limity](#legal).
- **Kábel.** Koaxiálny kábel maj krátky alebo použi kábel s nízkym útlmom. Na 868 MHz môže
  pár metrov tenkého kábla pohltiť polovicu tvojho výkonu.
- **Krabica.** Vodotesná krabica (IP65 alebo lepšia) s káblovou priechodkou, vetracím
  alebo odtokovým otvorom proti kondenzácii a so svetlou farbou alebo tienením pred slnkom.
  Batériám škodí teplo a pod bodom mrazu sa nedajú nabíjať.
- **Blesk.** Anténa na streche je terč pre blesky. Dodržuj miestne pravidlá pre
  uzemnenie alebo ju namontuj tam, kde by úder nezasiahol elektrické rozvody
  budovy.

## Napájanie a dimenzovanie solárneho systému {#power}

Solárny opakovač musí prežiť najtmavšie týždne zimy. Podľa nich ho
navrhni:

1. **Zmeraj spotrebu.** Nechaj nastavený opakovač bežať deň cez USB merač
   výkonu. Odčítaj spotrebovanú energiu vo watthodinách (Wh). Prevádzka v
   tvojej oblasti toto číslo mení, preto meraj podľa možnosti na mieste.
2. **Pridaj rezervu.** Kapacitu batérie plánuj aspoň na 5 až 7 dní
   bez využiteľného slnka.
3. **Zisti, koľko slnka máš v zime.** Bezplatný
   [nástroj PVGIS](https://re.jrc.ec.europa.eu/pvg_tools/en/) od EÚ ukáže pre každé
   miesto, koľko energie panel vyrobí za mesiac. Počítaj s mesiacom, keď je
   slnka najmenej.
4. **Zvoľ veľkosť panelu.** Panel musí v tomto najhoršom mesiaci nahradiť dennú spotrebu
   a mať rezervu na straty pri nabíjaní.

Vzorový výpočet s predpokladanými číslami: opakovač so spotrebou 1 Wh za deň
potrebuje na týždeň rezervy batériu s kapacitou aspoň 7 Wh, približne 2 Ah
využiteľnej kapacity pri 3.7 V. Ak podľa PVGIS panel s výkonom 1 W na tvojom mieste vyrobí
v decembri 0.5 Wh za deň, potrebuješ panel aspoň 2 W. Panel s 3 až 5 W
ti nechá rezervu na oblaky, sneh a starnutie.

## Nastavenie {#config}

**Nahraj firmvér.** Použi [webový flasher](https://flasher.meshcore.io) a vyber
firmvér **Repeater** pre svoju dosku. Postup nahrávania nájdeš v časti
[Začíname](/get-started/#flash).

**Nastav ho cez USB.** Nechaj opakovač pripojený k počítaču a otvor
[config.meshcore.io](https://config.meshcore.io) alebo konzolu flashera. Môžeš použiť aj
ľubovoľný sériový terminál s rýchlosťou 115200 baud. Najdôležitejšie
príkazy:

| Čo | Príkaz |
|---|---|
| Zmena hesla správcu | `password <new password>` |
| Pomenovanie | `set name <name>` |
| Rádiová predvoľba: frekvencia, šírka pásma, SF, CR (platí po reštarte) | `set radio 869.618,62.5,8,8` |
| Limit pracovného cyklu v percentách | `set dutycycle 10` |
| Vysielací výkon rádiového čipu v dBm | `set tx <dBm>` |
| Poloha, aby sa opakovač zobrazil na mapách | `set lat <degrees>` a `set lon <degrees>` |
| Kontaktné údaje pre ostatných prevádzkovateľov | `set owner.info <text>` |
| Počet hodín medzi flood advertmi, ktoré počuje celá sieť | `set flood.advert.interval <hours>` |
| Okamžité ohlásenie opakovača | `advert` |
| Reštart | `reboot` |

Predvolené heslo správcu je `password` a každý, kto sa ním prihlási,
sa stane správcom. Zmeň ho skôr, než opakovač začne vysielať.

Príklad `set radio` vyššie platí pre EU/UK (Narrow). Namiesto neho použi hodnoty predvoľby
svojej oblasti: nájdeš ich podľa krajín v časti [Odporúčané nastavenia](/guides/settings/).

**Nastav hodiny.** Bez modulu hodín (RTC) opakovač pri každom výpadku napájania stratí
čas a po reštarte začne v máji 2024. Počas behu sa jeho hodiny navyše rozchádzajú:
idú čoraz viac napred alebo pozadu. Preto hodiny občas nastav: prihlás sa na diaľku
z aplikácie a použi `clock sync` alebo nastav čas cez USB. S
modulom RTC to potrebuješ len zriedka: udrží čas aj počas výpadkov napájania a
rozchádza sa oveľa menej.

**Spravuj ho na diaľku.** Keď je opakovač v sieti, prihlás sa k nemu z aplikácie MeshCore
heslom správcu. V aplikácii si prečítaš jeho stav a tie isté príkazy zadáš
cez rádio. Niektoré príkazy fungujú len cez USB, napríklad `set freq` a obnovenie
továrenských nastavení `erase`.

**Zachovaj jeho identitu.** Pred vymazaním zadaj cez USB `get prv.key` a súkromný kľúč,
ktorý sa zobrazí, si bezpečne ulož. Po vymazaní vrátiš opakovaču pôvodnú identitu príkazmi
`set prv.key <key>` a `reboot`. Uzly, ktoré ho poznajú,
ho tak nájdu pod tým istým prefixom.

Úplný zoznam príkazov nájdeš v
[referenčnej príručke MeshCore CLI](https://github.com/meshcore-dev/MeshCore/blob/main/docs/cli_commands.md).

## Aktualizácia cez rádio {#update}

Keď je opakovač vysoko, aktualizuješ ho zo zeme. Prihlás sa z aplikácie
MeshCore heslom správcu, otvor jeho príkazový riadok a zadaj
`start ota`. Ďalší postup závisí od dosky. Ostatné dosky odpovedia `Error`
a tie aktualizuješ cez USB.

**Dosky nRF52**, napríklad RAK, Heltec T114, Seeed XIAO a SenseCAP Solar:

1. Z [webového flashera](https://flasher.meshcore.io) si stiahni **ZIP** s novým firmvérom
   pre svoju dosku.
2. Zadaj `start ota`. Opakovač odpovie `OK` a cez Bluetooth sa zobrazí
   ako `<board>_OTA`, napríklad `RAK4631_OTA`.
3. V telefóne otvor aplikáciu nRF Device Firmware Update, vyber ZIP a
   opakovač a spusti nahrávanie. Trvá to pár minút.

Skôr než dosku nRF52 vynesieš hore, nainštaluj do nej
[bootloader OTAFIX](https://github.com/oltaco/Adafruit_nRF52_Bootloader_OTAFIX).
So štandardným bootloaderom opravíš neúspešnú aktualizáciu len cez USB. S OTAFIX sa
doska vráti do aktualizačného režimu a skúsiš to znova cez Bluetooth.

**Dosky ESP32**, napríklad Heltec V3 a V4:

1. Z webového flashera si stiahni **non-merged** `.bin` pre svoju dosku:
   súbor, ktorý nemá v názve „merged“.
2. Zadaj `start ota`. Opakovač otvorí WiFi sieť s názvom `MeshCore-OTA`
   a odpovie adresou svojej stránky na nahrávanie.
3. V dosahu WiFi pripoj telefón alebo notebook k tejto sieti, otvor
   adresu a nahraj súbor.

## Zákonné limity {#legal}

{{< callout type="legal" verified="2026-10-02" >}}
Európske predvoľby MeshCore sú v podpásme **869.40-869.65 MHz**. V
EÚ, Spojenom kráľovstve, Švajčiarsku a Nórsku ho môžu zariadenia krátkeho dosahu používať bez
licencie v rámci týchto limitov:

- najviac **500 mW e.r.p.** vyžiareného výkonu;
- najviac **10% pracovný cyklus**: nanajvýš 360 sekúnd vysielania
  za hodinu na jedno zariadenie. Zariadenie môže namiesto toho použiť listen-before-talk
  s adaptive frequency agility podľa ETSI EN 300 220-2;
- celý signál so šírkou najviac 250 kHz musí zostať vnútri podpásma.

Pásmo je zdieľané: nesmieš rušiť licencované služby a iní môžu rušiť teba.
Rádio musí mať označenie CE (vo Veľkej Británii CE alebo UKCA).
{{< /callout >}}

Zdroje: [CEPT ERC Recommendation 70-03](https://docdb.cept.org/document/845),
príloha 1, pásmo h1.7;
[rozhodnutie Komisie 2006/771/ES](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02006D0771(01)-20250123)
a jeho zmeny;
[ETSI EN 300 220-2](https://www.etsi.org/deliver/etsi_en/300200_300299/30022002/03.03.01_60/en_30022002v030301p.pdf),
pásmo O.

### Výkon: e.r.p. a tvoja anténa {#erp}

Limit platí pre *vyžiarený* výkon, meraný voči jednoduchej dipólovej
anténe (e.r.p.). Zisk antény sa pripočítava, útlm kábla sa odpočítava. Výrobcovia
uvádzajú zisk antény v dBi, čo je o 2.15 dB viac než ten istý zisk v dBd
(vzhľadom na dipól). Tento súčet udrž na 27 dBm (500 mW) alebo nižšie:

> vysielací výkon (dBm) + zisk antény (dBi) − útlm kábla (dB) − 2.15 ≤ 27

- Doska vysiela 22 dBm do antény s 5 dBi cez kábel s útlmom 1 dB:
  22 + 5 − 1 − 2.15 = 23.85 dBm, približne 240 mW e.r.p. V rámci limitu.
- Doska so zosilňovačom 30 dBm (1 W) vysiela do antény s 3 dBi:
  30 + 3 − 2.15 = 30.85 dBm, približne 1.2 W e.r.p. Nad limitom: zníž
  vysielací výkon.

Príkazom `set tx` nastavíš výstup čipu LoRa v dBm. Samotný čip SX1262
dosahuje najviac 22 dBm. Firmvér zadané číslo nekontroluje. Dosky s prídavným
zosilňovačom, napríklad Heltec V4 alebo Station G2, vysielajú oveľa viac,
než koľko nastavíš. Pred nastavením si pozri tabuľku výrobcu a
začni s nízkou hodnotou.

### Pracovný cyklus {#duty-cycle}

Opakovač vysiela pre všetkých okolo seba, preto minie svoj vysielací čas rýchlejšie
než companion. Obmedzovač pracovného cyklu v MeshCore má predvolených 50%, čo je
viac, než toto pásmo dovoľuje. Na každom opakovači nastav 10%:

```text
set dutycycle 10
```

### Presnosť frekvencie {#frequency}

Kanál EU/UK (Narrow), 869.618 MHz so šírkou pásma 62.5 kHz, siaha až
po 869.649 MHz: necelý 1 kHz pod hornou hranicou podpásma. Signál
musí zostať v pásme pri každej teplote. Na to je potrebný
teplotne kompenzovaný kryštál (TCXO). Má ho takmer každá súčasná doska.
Staršie dosky bez neho, napríklad Heltec V2, sa rozladia príliš na to, aby spoľahlivo fungovali
pri 62.5 kHz.

### Poznámky ku krajinám {#countries}

- **Členské štáty EÚ** musia toto podpásmo sprístupniť za týchto podmienok
  (rozhodnutie 2006/771/ES, článok 3).
- **Spojené kráľovstvo:** rovnaké limity v dokumente Ofcom
  [IR 2030](https://www.ofcom.org.uk/spectrum/radio-equipment/short-range-devices).
- **Švajčiarsko a Lichtenštajnsko:** rovnaké limity v dokumente OFCOM
  [RIR1008-09](https://www.ofcomnet.ch/api/rir/1008/09).
- **Nórsko:** rovnaké limity v
  [nariadení o všeobecných povoleniach](https://lovdata.no/dokument/SF/forskrift/2012-01-19-77)
  (fribruksforskriften).

Tieto poznámky nie sú právne poradenstvo. Pravidlá sa menia. V prípade pochybností sa obráť na
svojho národného regulátora.

## Kontrolný zoznam pred nasadením {#checklist}

- [ ] Vlastník miesta súhlasil a k opakovaču sa pri údržbe dostaneš.
- [ ] Na doske beží firmvér **Repeater** a anténa bola pripojená pred prvým
      zapnutím.
- [ ] Heslo správcu je zmenené.
- [ ] Rádio zodpovedá [predvoľbe tvojej oblasti](/guides/settings/) (`get radio`).
- [ ] Je nastavené `set dutycycle 10`.
- [ ] Vysielací výkon spolu so ziskom antény neprekračuje 500 mW e.r.p.
- [ ] Názov, poloha a `owner.info` sú nastavené, aby ostatní vedeli, kto opakovač prevádzkuje.
- [ ] Hodiny sú nastavené (`clock`).
- [ ] Krabica je utesnená, má odtokový alebo vetrací otvor a kábel má
      odkvapovú slučku.
- [ ] Batéria a panel sú dimenzované na najhorší zimný mesiac.
- [ ] Pred odchodom z miesta máš opakovač otestovaný z diaľky v aplikácii.
- [ ] Tvoja miestna skupina vie, že opakovač je v prevádzke.
