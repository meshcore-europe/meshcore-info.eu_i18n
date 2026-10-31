---
title: Začínáme
lead: Od nové desky k první zprávě v mesh síti. Potřebuješ LoRa desku, počítač s Chrome nebo Edge a telefon nebo notebook pro aplikaci.
description: Nahraj MeshCore z prohlížeče, spáruj aplikaci, vyber rádiové nastavení své oblasti, pošli první zprávu a připoj se k místnímu kanálu.
eyebrow: 6 kroků · MeshCore v1.18.0
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'f97ca1b9'
  seeded: '2026-10-31'
  fields: {title: '61e8d44a', lead: '45b0e5c3', description: 'cf031b18', eyebrow: '4fa6fe1e'}
  sections: ['16c3728c', '203acaa5', 'df7a1665', '6da9fd7a', 'cb5fb72e', 'a1cf8b26', 'a419ce79', '66d00206']
  blocks: ['16c3728c', '2a70a7ed', '6f8e6f5f', '16c11d47', '081db416', 'd5e7fd0b', '6d28c323', 'eb2ea361', 'de50125c', 'ae20cb8e', 'abd42710', 'c08a865a', '7d1eb0b9', '263e0c96', '0903299f', 'eba20370', '5cdc20cf', '7f542f82', '802ca5a8', '1a854187', 'bc333adf', 'f25b16fa', '7c893ae2', '7f5927b4', '26e13713', '39a142cf', 'a786620c', '216897fa', '2d222782', 'a9755900', 'f081b357']
---

Tento postup vychází z firmwaru MeshCore v1.18.0 a oficiálních nástrojů
z října 2026. Názvy nabídek v aplikaci se mohou mezi verzemi trochu lišit.

## 1. Vyber zařízení {#device}

Hodí se každá deska ze [stránky se zařízeními](/devices/), u které je uvedený
companion. Jako první uzel si vyber *companion*: rádio, ze kterého píšeš
zprávy. Spáruješ ho s telefonem nebo notebookem přes Bluetooth nebo USB.
Můžeš také zvolit zařízení s vlastním displejem a klávesnicí, které funguje
samostatně.

Kup verzi pro 868 MHz. Přiložená anténa stačí. Jak ji zkontrolovat, najdeš
v [průvodci anténami](/guides/antenna/).

{{< callout type="warning" >}}
Než rádio zapneš, připoj anténu. LoRa rádio, které vysílá bez antény, si
může poškodit vlastní čip.
{{< /callout >}}

## 2. Nahraj firmware {#flash}

1. Připoj zařízení k počítači datovým USB kabelem.
2. V Chrome nebo Edge otevři webový flasher na [flasher.meshcore.io](https://flasher.meshcore.io).
   Flasher používá Web Serial a ten ostatní prohlížeče nemají.
3. Vyber své zařízení a potom firmware **Companion** pro **Bluetooth** (nebo
   USB, pokud ho budeš používat jen s kabelem k počítači).
4. Spusť nahrávání. Některé desky musíš nejdřív přepnout do režimu
   aktualizace. Flasher ti ukáže jak.

Volbu *erase* použij jen pro úplně nový začátek. Smazání odstraní identitu
zařízení i tvoje kontakty. Pozdější aktualizace nahrávej bez mazání. Pokud
chceš identitu zachovat i po smazání, nejdřív v aplikaci exportuj soukromý
klíč svého companionu. Potom ho znovu naimportuj.

## 3. Nainstaluj aplikaci {#app}

Oficiální aplikace MeshCore existuje pro Android, iOS, Windows a macOS.
Odkazy na všechny verze najdeš na [meshcore.io](https://meshcore.io). Na
počítači můžeš použít i webovou aplikaci na [app.meshcore.nz](https://app.meshcore.nz),
která běží v Chrome nebo Edge.

## 4. Spáruj svůj uzel {#pair}

Zapni uzel, otevři aplikaci a připoj se k němu přes Bluetooth. Když se
aplikace zeptá na PIN:

- uzel **s** displejem ukáže PIN, zadej ho;
- uzel **bez** displeje používá `123456`.

Pokud párování selže, odeber zařízení v nastavení Bluetooth na telefonu
a zkus to znovu. Potom svůj uzel pojmenuj. Toto jméno uvidí ostatní.
Nepoužívej proto celé jméno ani adresu, pokud o to sám nestojíš.

## 5. Vyber rádiové nastavení své oblasti {#preset}

Všechna rádia v jedné oblasti používají stejnou frekvenci a nastavení.
Jinak se navzájem neslyší. V rádiovém nastavení aplikace vyber preset, který
používá tvoje oblast. Mimo níže uvedené oblasti se v Evropě používá
**EU/UK (Narrow)**. Nizozemsko, Česko, Maďarsko, Slovensko, Portugalsko
a Švýcarsko mají vlastní preset. Nizozemské Limbursko má vlastní variantu:

{{< presets >}}

Tvoje zařízení preset tvé oblasti nenabízí? Zadej v rádiovém nastavení
aplikace ručně 4 hodnoty z tabulky: frekvenci, šířku pásma, spreading factor
a coding rate. Uzel s jinými hodnotami mesh síť neslyší.

Nejsi si jistý? Tvoje [místní skupina](/community/) ví, jaký preset se
ve tvé oblasti používá. Aplikace stahuje tento seznam z projektu MeshCore. Nový
preset proto nevyžaduje aktualizaci aplikace.

## 6. Pozdrav ostatní {#hello}

1. **Ohlas se.** Pošli z aplikace *advert*. „Flood“ advert putuje přes
   repeatery (uzly, které zprávy předávají dál). Díky tomu si tě může přidat
   každý v mesh síti.
   Companiony se nikdy neohlašují automaticky.
2. **Najdi ostatní.** Lidé se ti objeví v kontaktech, jakmile k tobě dorazí
   jejich adverty. Repeatery standardně posílají flood advert každých
   47 hodin. Naplnění seznamu proto může trvat 2 dny.
3. **Pošli zprávu.** Otevři kontakt a napiš zprávu. První zpráva se šíří
   sítí jako flood. Příjemce ti pošle zpět cestu, kterou zpráva prošla,
   a další zprávy už jdou po ní.
4. **Připoj se ke kanálům.** Kanál **Public** máš nastavený od začátku. Co
   do něj napíšeš, dostane každý v mesh síti. *Hashtagový kanál* svého
   regionu (název začínající `#`) přidáš tak, že napíšeš jeho název. Které
   kanály jsou aktivní, ti řekne tvoje [místní skupina](/community/).

## Když něco nefunguje {#troubleshooting}

**Aplikace nenajde moje zařízení přes Bluetooth.**
Nejspíš jsi nahrál USB companion. Nahraj firmware znovu a vyber verzi pro
Bluetooth. Heltec V3 má malou vestavěnou Bluetooth anténu s krátkým dosahem.
Drž telefon blízko.

**Párování pořád selhává.**
Odeber zařízení v nastavení Bluetooth na telefonu a restartuj Bluetooth.
Potom spáruj znovu s PINem z displeje nebo s `123456`.

**V kontaktech se nikdo neobjevuje.**
Zkontroluj, že tvůj preset odpovídá tvé oblasti. Pošli flood advert. Pokud
v dosahu není žádný repeater, uslyšíš jen blízká rádia. Kde repeatery jsou,
ukazuje [stránka s mapou](/map/).

**Kontakt ukazuje „naposledy viděn“ před několika dny, i když je aktivní.**
Jeden z obou uzlů má špatný čas. Companion bere čas z tvého telefonu.
Repeaterům a room serverům (uzlům, které ukládají zprávy pro skupinu) musí
čas nastavit jejich majitel.

**Přímá zpráva nikdy nedorazí.**
Musíte mít jeden druhého v kontaktech. Uzel zahodí zprávu od někoho, koho
nezná, a odesílateli to neoznámí. Pošli flood advert a požádej druhého, ať
taky jeden pošle. V aplikaci zkontroluj, že přidává nové kontakty
automaticky. Přidává jen uzly v rámci svého limitu skoků.

**Staré kontakty fungují, nové se nikdy nespojí.**
První zpráva se šíří jako flood. Repeater ji předá dál, jen když má
nastavený region zprávy. Další zprávy jdou po naučené cestě a tu kontrola
regionu nezastaví. Zeptej se své [místní skupiny](/community/), jaké
regiony mají repeatery ve tvém okolí. Zkontroluj taky [nastavení pro tvou oblast](/guides/settings/#traffic).

**Aplikace se už nepřipojí k tvému companionu.**
Některé desky mají uživatelské tlačítko, třeba některé desky RAK a Heltec T114.
Podrž ho během prvních 8 sekund po startu desky. Companion pak otevře
záchrannou konzoli přes USB. V konzoli na
[flasher.meshcore.io](https://flasher.meshcore.io) nastavíš příkazem
`set pin <pin>` nový Bluetooth PIN. Příkaz `erase` zařízení vymaže.

**Flasher na Linuxu nedokáže otevřít sériový port.**
Tvůj uživatelský účet potřebuje přístup k portu, například přes
`sudo setfacl -m u:$USER:rw /dev/ttyUSB0`, nebo členství ve skupině `dialout`.

**Něco jiného.** Spoustu dalších problémů řeší
[MeshCore FAQ](https://github.com/meshcore-dev/MeshCore/blob/main/docs/faq.md).
