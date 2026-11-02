---
title: Prvi koraci
lead: Od nove pločice do prve poruke na mesh mreži. Trebaju ti LoRa pločica, računalo s preglednikom Chrome ili Edge te mobitel ili prijenosnik za aplikaciju.
description: Upiši MeshCore na uređaj iz preglednika, upari aplikaciju, odaberi radijski predložak svojeg područja, pošalji prvu poruku i pridruži se lokalnom kanalu.
eyebrow: 6 koraka · MeshCore v1.18.0
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '0c1b08d9'
  seeded: '2026-11-02'
  fields: {title: '61e8d44a', lead: '45b0e5c3', description: 'cf031b18', eyebrow: '4fa6fe1e'}
  sections: ['16c3728c', '90f3d626', 'df7a1665', '6da9fd7a', 'cb5fb72e', 'a1cf8b26', 'a419ce79', '66d00206']
  blocks: ['16c3728c', '2a70a7ed', '6f8e6f5f', '16c11d47', '757c634a', '081db416', 'd5e7fd0b', '6d28c323', 'eb2ea361', 'de50125c', 'ae20cb8e', 'abd42710', 'c08a865a', '7d1eb0b9', '263e0c96', '0903299f', 'eba20370', '5cdc20cf', '7f542f82', '802ca5a8', '1a854187', 'bc333adf', 'f25b16fa', '7c893ae2', '7f5927b4', '26e13713', '39a142cf', 'a786620c', '216897fa', '2d222782', 'a9755900', 'f081b357']
---

Ovi koraci odnose se na MeshCore firmware v1.18.0 i službene alate iz
listopada 2026. Nazivi izbornika u aplikaciji mogu se malo razlikovati među verzijama.

## 1. Odaberi uređaj {#device}

Odgovara svaka pločica na [stranici o uređajima](/devices/) uz koju piše companion. Za
svoj prvi čvor odaberi *companion*: radio s kojeg šalješ poruke. Upari ga s
mobitelom ili prijenosnikom preko Bluetooth veze ili USB-a. Možeš odabrati i model s vlastitim zaslonom
i tipkovnicom koji radi samostalno.

Nabavi verziju za 868 MHz. Antena iz paketa je dovoljna, a u
[vodiču za antene](/guides/antenna/) piše kako je možeš provjeriti.

Na pločici ti sada radi Meshtastic? Kad flashaš MeshCore, on zamjenjuje Meshtastic, a ta dva sustava
međusobno ne komuniciraju. Na stranici [Dolaziš s Meshtastica](/about/#meshtastic)
piše što radi drugačije.

{{< callout type="warning" >}}
Spoji antenu prije nego što uključiš radio. LoRa radio koji odašilje bez antene
može oštetiti vlastiti čip.
{{< /callout >}}

## 2. Upiši firmware {#flash}

1. Spoji uređaj na računalo podatkovnim USB kabelom.
2. Otvori web flasher na [flasher.meshcore.io](https://flasher.meshcore.io)
   u pregledniku Chrome ili Edge. Flasher treba Web Serial, a drugi preglednici to nemaju.
3. Odaberi svoj uređaj, a zatim firmware **Companion** za **Bluetooth** (ili
   USB, ako ćeš uređaj koristiti samo s računalom preko kabela).
4. Pokreni upisivanje. Neke pločice prvo moraš prebaciti u način za ažuriranje, a flasher
   će ti reći kako.

Opciju *erase* koristi samo kad želiš krenuti ispočetka: brisanjem gubiš identitet
uređaja i svoje kontakte. Kod kasnijih ažuriranja upisuj firmware bez brisanja. Ako želiš zadržati
identitet nakon brisanja, prvo izvezi privatni ključ svojeg companiona iz aplikacije,
a poslije ga ponovno uvezi.

## 3. Instaliraj aplikaciju {#app}

Službena aplikacija za MeshCore postoji za Android, iOS, Windows i macOS, a
na [meshcore.io](https://meshcore.io) naći ćeš poveznice na sve verzije. Postoji i
web aplikacija na [app.meshcore.nz](https://app.meshcore.nz) koju na računalu pokrećeš u pregledniku Chrome ili
Edge.

## 4. Upari svoj čvor {#pair}

Uključi čvor, otvori aplikaciju i poveži se s njim preko Bluetooth veze. Kad
aplikacija zatraži PIN:

- čvor **sa** zaslonom prikazuje PIN, pa upiši taj broj;
- čvor **bez** zaslona koristi `123456`.

Ako uparivanje ne uspije, ukloni uređaj iz Bluetooth postavki na mobitelu i
pokušaj ponovno. Zatim daj čvoru ime. To ime vide i drugi, pa nemoj upisivati
puno ime i prezime ili adresu, osim ako to želiš.

## 5. Odaberi radijski predložak svojeg područja {#preset}

Svi radiji na jednom području koriste istu frekvenciju i iste postavke, inače se međusobno ne čuju. U radijskim postavkama aplikacije odaberi predložak koji se koristi na tvojem području.
Izvan dolje navedenih područja Europa koristi **EU/UK (Narrow)**. Nizozemska,
Češka, Mađarska, Slovačka, Portugal i Švicarska imaju vlastite predloške, a
nizozemski Limburg ima svoju varijantu:

{{< presets >}}

Tvoj uređaj ne nudi predložak za tvoje područje? Ručno upiši 4 vrijednosti iz
tablice u radijske postavke aplikacije: frekvenciju, širinu pojasa, faktor širenja
(spreading factor) i stopu kodiranja (coding rate). Čvor s drugim vrijednostima ne čuje mesh mrežu.

Nisi siguran? Tvoja [lokalna grupa](/community/) zna koji se predložak koristi na tvojem području.
Aplikacija preuzima ovaj popis od projekta MeshCore, pa za novi predložak
ne trebaš ažurirati aplikaciju.

## 6. Javi se {#hello}

1. **Predstavi se.** Pošalji *advert* iz aplikacije. "Flood" advert
   putuje preko repetitora (čvorova koji prosljeđuju poruke), pa te svi
   na mesh mreži mogu dodati.
   Companioni se nikad ne predstavljaju automatski.
2. **Pronađi druge.** Ljudi se pojavljuju u tvojim kontaktima kad do tebe stignu
   njihovi adverti. Repetitori prema zadanim postavkama šalju flood advert svakih 47 sati, pa
   se tvoj popis može puniti 2 dana.
3. **Pošalji poruku.** Otvori kontakt i piši. Prva poruka preplavljuje
   mrežu. Primatelj zatim javlja kojim je putem stigla, a sljedeće
   poruke idu tim putem.
4. **Pridruži se kanalima.** Kanal **Public** već je postavljen, a sve što
   tamo napišeš stiže do svih na mesh mreži. Dodaj *hashtag kanal* svoje regije
   (naziv koji počinje znakom `#`) tako da upišeš njegov naziv. Tvoja
   [lokalna grupa](/community/) reći će ti koji su kanali aktivni.

## Kad nešto ne radi {#troubleshooting}

**Aplikacija ne pronalazi moj uređaj preko Bluetooth veze.**
Vjerojatno si upisao USB companion. Ponovno upiši firmware i odaberi
Bluetooth verziju. Na uređaju Heltec V3 mala ugrađena Bluetooth antena
ima kratak domet, pa drži mobitel blizu.

**Uparivanje stalno ne uspijeva.**
Ukloni uređaj iz Bluetooth postavki na mobitelu, ponovno pokreni Bluetooth
i ponovno upari uređaj s PIN-om sa zaslona ili s `123456`.

**U mojim se kontaktima nitko ne pojavljuje.**
Provjeri odgovara li tvoj predložak tvojem području. Pošalji flood advert. Ako
u dometu nema repetitora, čut ćeš samo radije u blizini. Na
[stranici s kartom](/map/) vidiš gdje su repetitori.

**Kontakt je aktivan, ali uz njega piše "last seen" od prije nekoliko dana.**
Jedan od dva čvora ima pogrešno vrijeme. Companion preuzima vrijeme s
tvojeg mobitela. Repetitorima i room serverima (čvorovima koji spremaju poruke za
grupu) vrijeme mora postaviti njihov vlasnik.

**Izravna poruka nikad ne stigne.**
Oboje morate imati jedno drugo u kontaktima. Čvor odbacuje poruku pošiljatelja
kojeg ne poznaje i o tome ga ne obavještava. Pošalji flood advert i zamoli
drugu osobu da i ona pošalje svoj. U aplikaciji provjeri dodaje li automatski nove
kontakte. Aplikacija dodaje samo čvorove unutar svojeg ograničenja skokova.

**Stari kontakti rade, a novi se nikad ne povežu.**
Prva poruka preplavljuje mrežu, a repetitor je prosljeđuje samo ako ima
regiju te poruke. Kasnije poruke idu naučenim putem, a njih provjera regije ne zaustavlja. Pitaj svoju [lokalnu grupu](/community/) koje regije imaju repetitori
oko tebe i provjeri [postavke za svoje područje](/guides/settings/#traffic).

**Aplikacija se više ne povezuje s tvojim companionom.**
Neke pločice imaju korisničku tipku, primjerice neke RAK pločice i Heltec T114.
Drži je pritisnutom tijekom prvih 8 sekundi nakon pokretanja pločice. Companion tada otvara
konzolu za spašavanje preko USB-a. U konzoli na
[flasher.meshcore.io](https://flasher.meshcore.io) naredbom `set pin <pin>` postavljaš
novi Bluetooth PIN, a naredbom `erase` brišeš uređaj.

**Flasher na Linuxu ne može otvoriti serijski port.**
Tvoj korisnički račun treba pristup portu, primjerice
`sudo setfacl -m u:$USER:rw /dev/ttyUSB0`, ili članstvo u grupi
`dialout`.

**Nešto drugo.** Dokument
[MeshCore FAQ](https://github.com/meshcore-dev/MeshCore/blob/main/docs/faq.md)
opisuje još mnogo problema.
