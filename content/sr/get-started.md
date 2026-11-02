---
title: Prvi koraci
lead: Od nove pločice do prve poruke na mreži. Treba ti LoRa pločica, računar sa Chrome-om ili Edge-om i telefon ili laptop za aplikaciju.
description: Instaliraj MeshCore iz pregledača, poveži aplikaciju, izaberi radio preset svog područja, pošalji prvu poruku i pridruži se lokalnom kanalu.
eyebrow: 6 koraka · MeshCore v1.18.0
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'f97ca1b9'
  seeded: '2026-11-02'
  fields: {title: '61e8d44a', lead: '45b0e5c3', description: 'cf031b18', eyebrow: '4fa6fe1e'}
  sections: ['16c3728c', '203acaa5', 'df7a1665', '6da9fd7a', 'cb5fb72e', 'a1cf8b26', 'a419ce79', '66d00206']
  blocks: ['16c3728c', '2a70a7ed', '6f8e6f5f', '16c11d47', '081db416', 'd5e7fd0b', '6d28c323', 'eb2ea361', 'de50125c', 'ae20cb8e', 'abd42710', 'c08a865a', '7d1eb0b9', '263e0c96', '0903299f', 'eba20370', '5cdc20cf', '7f542f82', '802ca5a8', '1a854187', 'bc333adf', 'f25b16fa', '7c893ae2', '7f5927b4', '26e13713', '39a142cf', 'a786620c', '216897fa', '2d222782', 'a9755900', 'f081b357']
---

Ovi koraci važe za MeshCore firmver v1.18.0 i zvanične alate iz oktobra 2026.
Nazivi menija u aplikaciji mogu se malo razlikovati od verzije do verzije.

## 1. Izaberi uređaj {#device}

Odgovara svaka pločica sa [stranice o uređajima](/devices/) uz koju piše companion. Za
svoj prvi čvor izaberi *companion*: radio preko kog šalješ poruke. Poveži ga sa
telefonom ili laptopom preko Bluetooth-a ili USB-a. Možeš izabrati i model sa sopstvenim ekranom
i tastaturom, koji radi samostalno.

Uzmi verziju za 868 MHz. Antena iz kompleta je dovoljna. U
[vodiču za antene](/guides/antenna/) piše kako da je proveriš.

{{< callout type="warning" >}}
Priključi antenu pre nego što uključiš radio. LoRa radio koji
emituje bez antene može da ošteti sopstveni čip.
{{< /callout >}}

## 2. Instaliraj firmver {#flash}

1. Poveži uređaj sa računarom USB kablom za prenos podataka.
2. Otvori veb-alat za instalaciju na [flasher.meshcore.io](https://flasher.meshcore.io)
   u Chrome-u ili Edge-u. Alat koristi Web Serial, a drugi pregledači ga nemaju.
3. Izaberi svoj uređaj, a zatim firmver **Companion** za **Bluetooth** (ili
   USB, ako ćeš ga koristiti samo sa računarom preko kabla).
4. Pokreni instalaciju. Neke pločice prvo moraš da prebaciš u režim za ažuriranje, a alat ti pokazuje
   kako.

Opciju *erase* koristi samo kada želiš da kreneš ispočetka: brisanje uklanja identitet uređaja
i tvoje kontakte. Za kasnija ažuriranja instaliraj firmver bez brisanja. Ako želiš da sačuvaš
identitet posle brisanja, prvo izvezi privatni ključ svog companion uređaja iz aplikacije,
a posle ga ponovo uvezi.

## 3. Instaliraj aplikaciju {#app}

Zvanična MeshCore aplikacija postoji za Android, iOS, Windows i macOS.
Na [meshcore.io](https://meshcore.io) naći ćeš linkove za sve verzije. Postoji i
veb-aplikacija na [app.meshcore.nz](https://app.meshcore.nz), koju na računaru otvaraš u Chrome-u ili
Edge-u.

## 4. Upari svoj čvor {#pair}

Uključi čvor, otvori aplikaciju i poveži se s njim preko Bluetooth-a. Kada
aplikacija zatraži PIN:

- čvor **sa** ekranom prikazuje PIN, pa ukucaj taj broj;
- čvor **bez** ekrana koristi `123456`.

Ako uparivanje ne uspe, ukloni uređaj iz Bluetooth podešavanja na telefonu i
pokušaj ponovo. Zatim daj čvoru ime. Drugi vide to ime, zato nemoj da koristiš
puno ime i prezime ili adresu, osim ako to želiš.

## 5. Izaberi radio preset svog područja {#preset}

Svi radio-uređaji na jednom području koriste istu frekvenciju i ista podešavanja, inače se međusobno ne čuju.
U radio-podešavanjima aplikacije izaberi preset koji se koristi na tvom području.
Van dole navedenih područja, Evropa koristi **EU/UK (Narrow)**. Holandija,
Češka, Mađarska, Slovačka, Portugal i Švajcarska imaju sopstvene presete, a
Limburg u Holandiji ima posebnu varijantu:

{{< presets >}}

Uređaj ne nudi preset za tvoje područje? Unesi ručno 4 vrednosti iz
tabele u radio-podešavanjima aplikacije: frekvenciju, širinu opsega, faktor širenja
i stopu kodiranja. Čvor sa drugačijim vrednostima ne čuje mrežu.

Nisi siguran? Tvoja [lokalna grupa](/community/) zna koji preset se koristi na tvom području.
Aplikacija preuzima ovu listu od projekta MeshCore, pa za novi preset ne moraš
da ažuriraš aplikaciju.

## 6. Javi se {#hello}

1. **Najavi se.** Pošalji *advert* (najavu) iz aplikacije. „Flood” advert
   putuje preko repeatera (čvorova koji prosleđuju poruke), pa svi
   na mreži mogu da te dodaju.
   Companion uređaji se nikada ne najavljuju automatski.
2. **Pronađi druge.** Ljudi se pojavljuju u tvojim kontaktima kada njihovi adverti stignu
   do tebe. Repeateri podrazumevano šalju flood advert na svakih 47 sati, pa punjenje
   liste može da potraje 2 dana.
3. **Pošalji poruku.** Otvori kontakt i piši. Prva poruka se širi celom
   mrežom. Primalac javlja kojom je putanjom stigla, a kasnije
   poruke idu tom putanjom.
4. **Pridruži se kanalima.** Kanal **Public** je već podešen. Sve što tamo napišeš stiže do svih na mreži. Dodaj *hashtag
   kanal* svog regiona (naziv koji počinje sa `#`) tako što ukucaš njegov naziv. Tvoja
   [lokalna grupa](/community/) će ti reći koji su kanali aktivni.

## Kada nešto ne radi {#troubleshooting}

**Aplikacija ne pronalazi moj uređaj preko Bluetooth-a.**
Verovatno si instalirao USB companion firmver. Ponovi instalaciju i izaberi
Bluetooth verziju. Na pločici Heltec V3 mala ugrađena Bluetooth antena
ima kratak domet, pa drži telefon blizu.

**Uparivanje stalno ne uspeva.**
Ukloni uređaj iz Bluetooth podešavanja na telefonu, ponovo pokreni Bluetooth
i ponovo se upari pomoću PIN-a sa ekrana ili koda `123456`.

**U kontaktima se niko ne pojavljuje.**
Proveri da li preset odgovara tvom području. Pošalji flood advert. Ako nijedan
repeater nije u dometu, čućeš samo radio-uređaje u blizini. Na
[stranici sa mapom](/map/) vidiš gde su repeateri.

**Kontakt pokazuje „last seen” od pre više dana, iako je aktivan.**
Jedan od dva čvora ima pogrešno vreme. Companion preuzima vreme sa
tvog telefona. Kod repeatera i room servera (čvorova koji čuvaju poruke za
grupu) vreme mora da podesi njihov vlasnik.

**Direktna poruka nikad ne stiže.**
Oboje morate da imate jedno drugo u kontaktima. Čvor odbacuje poruku od nekoga
koga ne poznaje i o tome ne obaveštava pošiljaoca. Pošalji flood advert i zamoli
drugu osobu da i ona pošalje svoj. U aplikaciji proveri da li ona automatski dodaje nove
kontakte. Aplikacija dodaje samo čvorove unutar svog ograničenja broja skokova.

**Stari kontakti rade, a novi se nikad ne povežu.**
Prva poruka se širi mrežom, a repeater je prosleđuje samo ako ima region te poruke.
Kasnije poruke idu naučenom putanjom, a nju provera regiona ne zaustavlja. Pitaj svoju [lokalnu grupu](/community/) koje regione imaju repeateri
oko tebe i proveri [podešavanja za svoje područje](/guides/settings/#traffic).

**Aplikacija više ne može da se poveže sa tvojim companion uređajem.**
Neke pločice imaju korisničko dugme, na primer neke RAK pločice i Heltec T114.
Drži ga pritisnutim u prvih 8 sekundi posle pokretanja pločice. Companion tada otvara
konzolu za oporavak preko USB-a. U konzoli na
[flasher.meshcore.io](https://flasher.meshcore.io) komanda `set pin <pin>` postavlja
novi Bluetooth PIN, a `erase` briše sve sa uređaja.

**Alat za instalaciju ne može da otvori serijski port na Linuxu.**
Tvoj korisnički nalog mora da ima pristup portu, na primer preko
`sudo setfacl -m u:$USER:rw /dev/ttyUSB0`, ili članstvo u grupi `dialout`.

**Nešto drugo.** Dokument
[MeshCore FAQ](https://github.com/meshcore-dev/MeshCore/blob/main/docs/faq.md)
obrađuje još mnogo problema.
