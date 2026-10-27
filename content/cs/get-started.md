---
title: Začínáme
lead: Od nové desky k první zprávě v meshi. Potřebuješ desku LoRa, počítač s Chromem nebo Edgem a telefon nebo notebook pro aplikaci.
description: Nahraj MeshCore z prohlížeče, spáruj aplikaci, zvol rádiový preset používaný ve tvé oblasti, pošli první zprávu a připoj se k místnímu kanálu.
eyebrow: 6 kroků · MeshCore v1.18.0
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '68c89544'
  seeded: '2026-10-26'
  fields: {title: '61e8d44a', lead: '45b0e5c3', description: 'cf031b18', eyebrow: '4fa6fe1e'}
  sections: ['16c3728c', '203acaa5', '36a3eba3', '6da9fd7a', 'cb5fb72e', '89626504', 'a419ce79', 'aa273b20']
---

Tyto kroky odpovídají firmwaru MeshCore v1.18.0 a oficiálním nástrojům z
října 2026. Názvy položek v menu aplikace se mohou mezi verzemi mírně lišit.

## 1. Vyber si zařízení {#device}

Funguje každá deska na [stránce zařízení](/devices/), u které je uvedeno companion. Pro
svůj první uzel si vyber *companion*: rádio, ze kterého píšeš zprávy. Spáruj ho
s telefonem nebo notebookem přes Bluetooth nebo USB, nebo si vyber model s vlastním displejem
a klávesnicí, který funguje samostatně.

Pořiď si verzi pro 868 MHz. Dodaná anténa svůj úkol zvládne;
[průvodce anténami](/guides/antenna/) ukazuje, jak ji zkontrolovat.

{{< callout type="warning" >}}
Před zapnutím rádia připoj anténu. Rádio LoRa, které
vysílá bez antény, si může poškodit vlastní čip.
{{< /callout >}}

## 2. Nahraj firmware {#flash}

1. Připoj zařízení k počítači datovým kabelem USB.
2. Otevři webový flasher na [flasher.meshcore.io](https://flasher.meshcore.io)
   v Chromu nebo Edgi. Používá Web Serial, který jiné prohlížeče nemají.
3. Vyber své zařízení a pak firmware **Companion** pro **Bluetooth** (nebo
   USB, pokud ho budeš používat jen s počítačem přes kabel).
4. Nahraj firmware. Některé desky nejdřív přejdou do režimu aktualizace; flasher ti
   řekne jak.

Volbu *erase* použij jen pro čistý začátek: vymazání smaže identitu zařízení
a tvé kontakty. Při pozdějších aktualizacích nahrávej firmware bez mazání.

## 3. Nainstaluj aplikaci {#app}

Oficiální aplikace MeshCore existuje pro Android, iOS, Windows a macOS;
odkazy na všechny verze najdeš na [meshcore.io](https://meshcore.io). Existuje také
webová aplikace na [app.meshcore.nz](https://app.meshcore.nz), která běží v Chromu nebo
Edgi na počítači.

## 4. Spáruj svůj uzel {#pair}

Zapni uzel, otevři aplikaci a připoj se k němu přes Bluetooth. Když
tě požádá o PIN:

- uzel **s** displejem ti PIN ukáže; zadej ten;
- uzel **bez** displeje používá `123456`.

Pokud párování selže, odeber zařízení z nastavení Bluetooth v telefonu a
zkus to znovu. Potom dej uzlu jméno. Toto jméno vidí ostatní, takže nepoužívej
celé jméno nebo adresu, pokud sám nechceš.

## 5. Zvol rádiový preset své oblasti {#preset}

Všechna rádia v jedné oblasti používají stejnou frekvenci a nastavení, jinak se
navzájem neslyší. V rádiovém nastavení aplikace zvol preset, který se používá ve tvé oblasti.
Mimo níže uvedené oblasti se v Evropě používá **EU/UK (Narrow)**. Nizozemsko,
Česko, Maďarsko, Slovensko, Portugalsko a Švýcarsko mají vlastní presety a
nizozemský Limburg má svou variantu:

{{< presets >}}

Nevíš jistě? Tvá [místní skupina](/community/) ví, který preset se ve tvé oblasti používá.
Aplikace si tento seznam stahuje z projektu MeshCore, takže nový preset
nevyžaduje aktualizaci aplikace.

## 6. Pozdrav ostatní {#hello}

1. **Ohlas se.** Pošli z aplikace *advert*. Advert typu „flood“
   putuje přes repeatery (uzly, které zprávy předávají dál), takže si tě může
   přidat každý v meshi.
   Companion se nikdy neohlašuje automaticky.
2. **Najdi ostatní.** Lidé se ti objeví v kontaktech, jakmile k tobě dorazí jejich
   adverty. Repeatery posílají flood advert ve výchozím nastavení každých 47 hodin, takže se tvůj seznam
   může plnit 2 dny.
3. **Pošli zprávu.** Otevři kontakt a piš. První zpráva se šíří sítí
   jako flood; příjemce ti nahlásí cestu, kterou zpráva prošla, a další
   zprávy už jdou touto cestou.
4. **Připoj se ke kanálům.** Kanál **Public** je už nastavený; cokoli tam
   napíšeš, dorazí všem v meshi. *Hashtagový kanál* svého regionu (název
   začínající na `#`) přidáš zadáním jeho názvu. Tvá
   [místní skupina](/community/) ti řekne, které kanály jsou aktivní.

## Když něco nefunguje {#troubleshooting}

**Aplikace nenajde mé zařízení přes Bluetooth.**
Nejspíš jsi nahrál companion pro USB. Nahraj firmware znovu a zvol
verzi pro Bluetooth. Na Heltec V3 má malá vestavěná anténa Bluetooth
krátký dosah; měj telefon blízko.

**Párování stále selhává.**
Odeber zařízení z nastavení Bluetooth v telefonu, restartuj Bluetooth
a spáruj ho znovu s PINem z displeje nebo `123456`.

**V kontaktech se mi nikdo neobjevuje.**
Zkontroluj, že tvůj preset odpovídá tvé oblasti. Pošli flood advert. Pokud není v dosahu žádný
repeater, uslyšíš jen rádia v blízkém okolí;
[stránka s mapou](/map/) ukazuje, kde repeatery jsou.

**U kontaktu je „naposledy viděn“ před několika dny, přestože je aktivní.**
Jeden ze dvou uzlů má špatně nastavený čas. Companion si bere čas
z tvého telefonu; repeaterům a room serverům (uzlům, které ukládají zprávy pro
skupinu) musí čas nastavit jejich majitel.

**Flasher nedokáže na Linuxu otevřít sériový port.**
Tvůj uživatel potřebuje přístup k portu, například
`sudo setfacl -m u:$USER:rw /dev/ttyUSB0`, nebo členství ve skupině
`dialout`.

**Něco jiného.**
[FAQ k MeshCore](https://github.com/meshcore-dev/MeshCore/blob/main/docs/faq.md)
pokrývá mnoho dalších problémů.
