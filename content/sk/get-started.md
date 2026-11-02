---
title: Začíname
lead: Od novej dosky po prvú správu v sieti. Potrebuješ dosku LoRa, počítač s prehliadačom Chrome alebo Edge a telefón alebo notebook pre aplikáciu.
description: Nahraj MeshCore z prehliadača, spáruj aplikáciu, vyber predvoľbu rádia pre svoju oblasť, pošli prvú správu a pridaj sa do miestneho kanála.
eyebrow: 6 krokov · MeshCore v1.18.0
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'f97ca1b9'
  seeded: '2026-11-02'
  fields: {title: '61e8d44a', lead: '45b0e5c3', description: 'cf031b18', eyebrow: '4fa6fe1e'}
  sections: ['16c3728c', '203acaa5', 'df7a1665', '6da9fd7a', 'cb5fb72e', 'a1cf8b26', 'a419ce79', '66d00206']
  blocks: ['16c3728c', '2a70a7ed', '6f8e6f5f', '16c11d47', '081db416', 'd5e7fd0b', '6d28c323', 'eb2ea361', 'de50125c', 'ae20cb8e', 'abd42710', 'c08a865a', '7d1eb0b9', '263e0c96', '0903299f', 'eba20370', '5cdc20cf', '7f542f82', '802ca5a8', '1a854187', 'bc333adf', 'f25b16fa', '7c893ae2', '7f5927b4', '26e13713', '39a142cf', 'a786620c', '216897fa', '2d222782', 'a9755900', 'f081b357']
---

Tento postup vychádza z firmvéru MeshCore v1.18.0 a oficiálnych nástrojov z októbra 2026. Názvy položiek v menu aplikácie sa môžu medzi verziami trochu líšiť.

## 1. Vyber si zariadenie {#device}

Hodí sa každá doska zo [stránky zariadení](/devices/), pri ktorej je uvedený companion. Ako prvý uzol si vyber *companion*: rádio, z ktorého píšeš správy. Spáruj ho s telefónom alebo notebookom cez Bluetooth alebo USB. Môžeš si vybrať aj model s vlastnou obrazovkou a klávesnicou, ktorý funguje samostatne.

Kúp si verziu na 868 MHz. Dodaná anténa postačí. V [návode k anténam](/guides/antenna/) zistíš, ako ju skontrolovať.

{{< callout type="warning" >}}
Anténu pripoj skôr, ako rádio zapneš. Rádio LoRa, ktoré vysiela bez antény, si môže poškodiť vlastný čip.
{{< /callout >}}

## 2. Nahraj firmvér {#flash}

1. Pripoj zariadenie k počítaču dátovým káblom USB.
2. V prehliadači Chrome alebo Edge otvor webový flasher na adrese [flasher.meshcore.io](https://flasher.meshcore.io). Flasher používa Web Serial a ostatné prehliadače túto funkciu nemajú.
3. Vyber svoje zariadenie a potom firmvér **Companion** pre **Bluetooth** (alebo USB, ak ho budeš používať len s počítačom cez kábel).
4. Nahraj firmvér. Niektoré dosky musíš najprv prepnúť do režimu aktualizácie. Flasher ti povie ako.

Funkciu *erase* použi len vtedy, keď chceš začať odznova: vymazanie odstráni identitu zariadenia aj tvoje kontakty. Pri neskorších aktualizáciách nahrávaj firmvér bez mazania. Ak si chceš pri vymazaní zachovať identitu, najprv v aplikácii exportuj súkromný kľúč svojho companionu a po vymazaní ho znova importuj.

## 3. Nainštaluj aplikáciu {#app}

Oficiálna aplikácia MeshCore je dostupná pre Android, iOS, Windows a macOS. Odkazy na všetky verzie nájdeš na [meshcore.io](https://meshcore.io). Na adrese [app.meshcore.nz](https://app.meshcore.nz) je aj webová aplikácia, ktorá beží v prehliadači Chrome alebo Edge na počítači.

## 4. Spáruj svoj uzol {#pair}

Zapni uzol, otvor aplikáciu a pripoj sa k nemu cez Bluetooth. Keď si aplikácia vypýta PIN:

- uzol **s** obrazovkou zobrazí PIN, zadaj ho;
- uzol **bez** obrazovky používa `123456`.

Ak párovanie zlyhá, odstráň zariadenie z nastavení Bluetooth v telefóne a skús to znova. Potom daj svojmu uzlu názov. Ostatní tento názov uvidia, takže nepoužívaj celé meno ani adresu, ak to sám nechceš.

## 5. Vyber predvoľbu rádia pre svoju oblasť {#preset}

Všetky rádiá v jednej oblasti používajú rovnakú frekvenciu a nastavenia, inak sa navzájom nepočujú. V nastaveniach rádia v aplikácii vyber predvoľbu, ktorú používa tvoja oblasť. Mimo oblastí uvedených nižšie používa Európa **EU/UK (Narrow)**. Holandsko, Česko, Maďarsko, Slovensko, Portugalsko a Švajčiarsko majú vlastnú predvoľbu a Limburg v Holandsku má variant:

{{< presets >}}

Tvoje zariadenie neponúka predvoľbu pre tvoju oblasť? V nastaveniach rádia v aplikácii zadaj ručne 4 hodnoty z tabuľky: frekvenciu, šírku pásma, spreading factor a coding rate. Uzol s inými hodnotami sieť nepočuje.

Nie si si istý? Tvoja [miestna skupina](/community/) vie, ktorú predvoľbu používa tvoja oblasť. Aplikácia si tento zoznam sťahuje z projektu MeshCore, takže nová predvoľba nevyžaduje aktualizáciu aplikácie.

## 6. Pozdrav ostatných {#hello}

1. **Ohlás sa.** Pošli z aplikácie *advert*. „Flood“ advert putuje cez repeatery (uzly, ktoré posúvajú správy ďalej), takže si ťa môže pridať každý v sieti.
   Companiony sa nikdy neohlasujú automaticky.
2. **Nájdi ostatných.** Ľudia sa objavia v tvojich kontaktoch, keď k tebe dorazia ich adverty. Repeatery predvolene posielajú flood advert každých 47 hodín, takže zoznam sa môže plniť 2 dni.
3. **Pošli správu.** Otvor kontakt a napíš mu. Prvá správa zaplaví sieť. Príjemca potom spätne oznámi trasu, ktorou prišla, a ďalšie správy idú touto trasou.
4. **Pridaj sa do kanálov.** Kanál **Public** je už nastavený a všetko, čo doň napíšeš, sa dostane ku každému v sieti. *Hashtagový kanál* svojho regiónu (názov začína znakom `#`) pridáš zadaním jeho názvu. Tvoja [miestna skupina](/community/) ti povie, ktoré kanály sú aktívne.

## Keď niečo nefunguje {#troubleshooting}

**Aplikácia nenájde moje zariadenie cez Bluetooth.**
Pravdepodobne si nahral USB verziu firmvéru Companion. Nahraj firmvér znova a vyber verziu pre Bluetooth. Heltec V3 má malú vstavanú anténu Bluetooth s krátkym dosahom, preto maj telefón blízko.

**Párovanie stále zlyháva.**
Odstráň zariadenie z nastavení Bluetooth v telefóne, reštartuj Bluetooth a znova spáruj zariadenie pomocou PIN-u na obrazovke alebo `123456`.

**V kontaktoch sa nikto neobjavuje.**
Skontroluj, či predvoľba zodpovedá tvojej oblasti. Pošli flood advert. Ak nemáš v dosahu žiadny repeater, budeš počuť len rádiá v blízkosti. Polohu repeaterov nájdeš na [stránke s mapou](/map/).

**Kontakt ukazuje „last seen“ spred niekoľkých dní, hoci je aktívny.**
Jeden z dvoch uzlov má nesprávny čas. Companion preberá čas z tvojho telefónu. Na repeateroch a room serveroch (uzloch, ktoré ukladajú správy pre skupinu) musí čas nastaviť ich vlastník.

**Priama správa nikdy nedorazí.**
Obaja musíte mať jeden druhého v kontaktoch. Uzol zahodí správu od neznámeho odosielateľa a nedá mu o tom vedieť. Pošli flood advert a požiadaj druhú osobu, aby ho poslala tiež. V aplikácii skontroluj, či pridáva nové kontakty automaticky. Pridáva len uzly v rámci svojho limitu skokov.

**Staré kontakty fungujú, nové sa nikdy nepripoja.**
Prvá správa zaplaví sieť a repeater ju posunie ďalej, len ak má nastavený jej región. Ďalšie správy idú naučenou trasou a tú kontrola regiónu nezastaví. Opýtaj sa [miestnej skupiny](/community/), ktoré regióny majú nastavené repeatery okolo teba, a skontroluj [nastavenia pre svoju oblasť](/guides/settings/#traffic).

**Aplikácia sa už nepripojí k tvojmu companionu.**
Niektoré dosky majú používateľské tlačidlo, napríklad niektoré dosky RAK a Heltec T114. Podrž ho počas prvých 8 sekúnd po štarte dosky. Companion potom cez USB otvorí záchrannú konzolu. V konzole na [flasher.meshcore.io](https://flasher.meshcore.io) nastavíš príkazom `set pin <pin>` nový PIN pre Bluetooth a príkazom `erase` vymažeš zariadenie.

**Flasher v Linuxe nedokáže otvoriť sériový port.**
Tvoj používateľský účet potrebuje prístup k portu, napríklad `sudo setfacl -m u:$USER:rw /dev/ttyUSB0`, alebo členstvo v skupine `dialout`.

**Niečo iné.** [MeshCore FAQ](https://github.com/meshcore-dev/MeshCore/blob/main/docs/faq.md) rieši mnoho ďalších problémov.
