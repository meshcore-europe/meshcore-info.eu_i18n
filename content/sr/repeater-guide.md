---
title: Vodič za ripitere
lead: Ripiter postavljen visoko prenosi poruke za sve oko sebe, širom celog grada ili doline. Izaberi lokaciju, napajaj ga solarnom energijom, podesi ga i poštuj zakon.
description: 'Isplaniraj, napajaj, podesi i zakonito koristi MeshCore ripiter u Evropi: izbor lokacije, dimenzionisanje solarnog napajanja, CLI podešavanja, ograničenja snage i duty cycle-a na 868 MHz.'
eyebrow: 868 MHz · do 500 mW · bez licence
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '7c7e3be3'
  seeded: '2026-11-02'
  fields: {title: '4608abcd', lead: 'bc670c65', description: '9e483ce5', eyebrow: '9fd33416'}
  sections: ['05ee477a', '938c518c', '766086be', '70faf508', '8bc641aa', '399cd683', 'e9dedb7b', '92beca03', '17634750', 'cadf6024', 'e9cc6834', '2e6e59ca', 'fb44b8db']
  blocks: ['20ac0371', 'ed2b1adf', '432543ee', '7af42c89', 'd0f7543a', '9ef3580f', '3476aef7', '1bab7bec', '6a7c4493', 'dbd9fa1f', 'aa06d32b', '9958aad3', 'd162b028', 'cca1bbdf', '64ef011d', 'e7f16724', 'd2e34ff0', 'bb195cfc', '8d080bb3', '2b1d995b', '210f1b66', 'dc7419d2', 'bdc66db0', 'b59f248c', '7184bd63', 'de5a24f9', 'f5cfb426', '48c7422f', '9d3c0836', 'da8a6af3', '240126df', '8aac2b33', '81a475b8', 'a53e42b5', '36ff1db4', 'e4ca8602', 'e4594afd', '3b24b8e9', '58330858', '68f2966e', 'd7418228', '23536e60', 'cbc5c2d1', '2ea02ba9', '92540256', '6e21f681', 'a8c12311', '3382ae7f', 'cdeafb0f', '1b1319d2']
---

Mesh mrežu drže ripiteri. Kompanjoni, radio-uređaji s kojih šalješ poruke, ne prosleđuju poruke dalje. Bez ripitera zato dopireš samo do ljudi u direktnom dometu. Ripiter na pravom mestu proširuje mrežu za sve oko sebe. Ovaj vodič prati MeshCore firmware v1.18.0.

Pre nego što počneš, porazgovaraj sa svojom [lokalnom grupom](/community/). Članovi grupe znaju gde nedostaje pokrivenost, [koji preset se koristi u tvom području](/guides/settings/) i kako se ripiteri imenuju. Na [mapama pokrivenosti](/map/) proveri ima li ripitera u tvojoj blizini, pa se javi na javnim ili lokalnim [kanalima](/guides/channels/).

## Da li ti je potreban? {#need}

Ripiter prosleđuje svaku flood poruku koju čuje, a svi ripiteri u dometu dele isto vreme emitovanja. Gde mreža već dopire do tebe, još jedan ripiter dodaje saobraćaj, a ne pokrivenost. Možda ti je dovoljan kompanjon postavljen visoko, na tavanskom prozoru ili balkonu.

Postavi ripiter tamo gde nedostaje pokrivenost:

- na [mapama pokrivenosti](/map/) nema ripitera u tvojoj blizini ili su tu samo oni koje tvoj kompanjon ne čuje;
- tvoja lokalna grupa kaže da je području potreban ripiter.

## Izaberi lokaciju {#site}

Visina vredi više od snage. LoRa na 868 MHz najbolje se prostire duž čiste linije vidljivosti. Brda, zgrade i gusto drveće oduzimaju daleko više dometa nego što ti nekoliko dodatnih milivata može vratiti.

- **Postavi ga visoko.** Krov, antenski stub, visoka zgrada ili brdo pokrivaju mnogo više od prozorske daske. Pomaže čak i nekoliko metara iznad okolnih krovova.
- **Drži antenu na otvorenom.** Montiraj je iznad ivica krova, dalje od metala, oluka i drugih antena.
- **Proveri vidljivost.** Alati kao što je [HeyWhatsThat](https://www.heywhatsthat.com/) pokazuju šta se vidi s neke lokacije. Ako neko mesto vidiš, ripiter na njemu je u dometu.
- **Ostavi slobodan prostor.** Radio-putanji treba slobodan prostor i oko direktne linije, a ne samo sama linija. Na velikim razdaljinama sredina putanje treba da prolazi nekoliko metara iznad prepreka.
- **Zatraži dozvolu.** Obezbedi saglasnost vlasnika krova ili stuba i dogovori kako ćeš pristupati ripiteru radi održavanja.

## Hardver {#hardware}

- **Ploča.** Izaberi nRF52 ploču male potrošnje, kao što su [Heltec T114](/devices/), RAK WisBlock ili SenseCAP Solar Node. ESP32 ploče troše više struje (na stranici o uređajima označene su sa High), pa ih je teško napajati solarnom energijom.
- **Antena.** Koristi antenu napravljenu za 868 MHz i montiraj je vertikalno. U [vodiču za antene](/guides/antenna/) naći ćeš tipove, konektore, kablove i montažu. Dobitak antene ulazi u zakonsko ograničenje snage. Pogledaj [Zakonska ograničenja](#legal).
- **Kabl.** Neka koaksijalni kabl bude kratak ili koristi kabl s malim gubicima. Na 868 MHz nekoliko metara tankog kabla može da odnese polovinu tvoje snage.
- **Kućište.** Koristi kutiju otpornu na vremenske uslove (IP65 ili bolju) s kablovskom uvodnicom i otvorom za ventilaciju ili odvod protiv kondenzacije. Neka bude svetle boje ili ima zaštitu od sunca. Baterijama šteti toplota, a ispod nule ne mogu da se pune.
- **Grom.** Antena na krovu je meta. Poštuj lokalna pravila za uzemljenje ili je montiraj tako da udar ne dosegne električne instalacije zgrade.

## Napajanje i dimenzionisanje solarnog sistema {#power}

Solarni ripiter mora da preživi najmračnije zimske nedelje. Dimenzioniši ga prema njima:

1. **Izmeri potrošnju.** Pusti podešeni ripiter da radi jedan dan preko USB merača snage. Očitaj utrošenu energiju u vat-satima (Wh). Saobraćaj u tvom području menja tu vrednost, pa meri na licu mesta ako možeš.
2. **Dodaj rezervu.** Planiraj kapacitet baterije za najmanje 5 do 7 dana bez korisnog sunca.
3. **Saznaj koliko sunca imaš zimi.** Besplatni alat EU [PVGIS](https://re.jrc.ec.europa.eu/pvg_tools/en/) pokazuje za svaku lokaciju koliko energije panel proizvede mesečno. Koristi mesec s najmanje sunca.
4. **Odredi veličinu panela.** Panel mora da nadoknadi dnevnu potrošnju u tom najgorem mesecu, uz rezervu za gubitke pri punjenju.

Primer računice, s pretpostavljenim brojevima: ripiteru koji troši 1 Wh dnevno treba baterija od najmanje 7 Wh za nedelju dana rezerve, što je oko 2 Ah korisnog kapaciteta na 3.7 V. Ako PVGIS kaže da panel od 1 W na tvojoj lokaciji u decembru daje 0.5 Wh dnevno, treba ti panel od najmanje 2 W. Sa 3 do 5 W imaš rezervu za oblake, sneg i starenje.

## Podesi ga {#config}

**Fleširanje.** Otvori [web flasher](https://flasher.meshcore.io) i izaberi **Repeater** firmware za svoju ploču. Korake za fleširanje naći ćeš u odeljku [Prvi koraci](/get-started/#flash).

**Podešavanje preko USB-a.** Dok je ripiter još povezan s računarom, otvori [config.meshcore.io](https://config.meshcore.io) ili konzolu flasher-a. Možeš da koristiš i bilo koji serijski terminal na 115200 baud. Najvažnije komande:

| Šta | Komanda |
|---|---|
| Promena administratorske lozinke | `password <new password>` |
| Davanje imena | `set name <name>` |
| Radio preset: frekvencija, širina opsega, SF, CR (primenjuje se posle ponovnog pokretanja) | `set radio 869.618,62.5,8,8` |
| Ograničenje duty cycle-a, u procentima | `set dutycycle 10` |
| Predajna snaga radio-čipa, u dBm | `set tx <dBm>` |
| Položaj, da se ripiter vidi na mapama | `set lat <degrees>` i `set lon <degrees>` |
| Kontakt podaci za druge operatere | `set owner.info <text>` |
| Broj sati između flood objava (advert), onih koje čuje cela mreža | `set flood.advert.interval <hours>` |
| Objava ripitera odmah | `advert` |
| Ponovno pokretanje | `reboot` |

Podrazumevana administratorska lozinka je `password`, a svako ko se njome prijavi postaje administrator. Promeni je pre nego što ripiter počne da emituje.

Gornji primer za `set radio` važi za EU/UK (Narrow). Umesto njega koristi vrednosti preseta za svoje područje. Spisak po zemljama naći ćeš u odeljku [Preporučena podešavanja](/guides/settings/).

**Podesi sat.** Bez modula sa satom (RTC) ripiter pri svakom nestanku struje izgubi tačno vreme i ponovo kreće od maja 2024. Dok radi, sat mu i odstupa: sve više žuri ili kasni. Zato povremeno podesi sat: prijavi se na daljinu iz aplikacije i pokreni `clock sync` ili podesi vreme preko USB-a. Sa RTC modulom to retko moraš da radiš: on čuva vreme tokom nestanka struje i mnogo manje odstupa.

**Upravljaj njime na daljinu.** Kada je ripiter u mreži, prijavi se iz MeshCore aplikacije administratorskom lozinkom. Tamo čitaš njegov status i preko radija koristiš iste komande. Neke komande rade samo preko USB-a, na primer `set freq` i vraćanje na fabrička podešavanja komandom `erase`.

**Sačuvaj njegov identitet.** Pre brisanja unesi `get prv.key` preko USB-a i privatni ključ koji se prikaže sačuvaj na bezbednom mestu. Posle brisanja, `set prv.key <key>` i `reboot` vraćaju ripiteru stari identitet. Čvorovi koji ga poznaju tako ga nalaze pod istim prefiksom.

Celu listu komandi naći ćeš u [referenci za MeshCore CLI](https://github.com/meshcore-dev/MeshCore/blob/main/docs/cli_commands.md).

## Ažuriraj ga bežično {#update}

Kada je ripiter već visoko, ažuriraš ga sa zemlje. Prijavi se iz MeshCore aplikacije administratorskom lozinkom, otvori njegovu komandnu liniju i unesi `start ota`. Dalji postupak zavisi od ploče. Ostale ploče odgovaraju sa `Error` i njih ažuriraš preko USB-a.

**nRF52 ploče**, kao što su RAK, Heltec T114, Seeed XIAO i SenseCAP Solar:

1. Preuzmi **ZIP** novog firmware-a za svoju ploču sa [web flasher-a](https://flasher.meshcore.io).
2. Unesi `start ota`. Ripiter odgovara sa `OK` i pojavljuje se preko Bluetooth-a kao `<board>_OTA`, na primer `RAK4631_OTA`.
3. Na telefonu otvori aplikaciju nRF Device Firmware Update, izaberi ZIP i ripiter, pa pokreni otpremanje. To traje nekoliko minuta.

Instaliraj [OTAFIX bootloader](https://github.com/oltaco/Adafruit_nRF52_Bootloader_OTAFIX) na nRF52 ploču pre nego što je postaviš na visinu. Sa fabričkim bootloader-om neuspelo ažuriranje možeš da popraviš samo preko USB-a. Sa OTAFIX-om se ploča vraća u režim ažuriranja, pa možeš ponovo da pokušaš preko Bluetooth-a.

**ESP32 ploče**, kao što su Heltec V3 i V4:

1. Sa web flasher-a preuzmi **non-merged** `.bin` za svoju ploču: datoteku koja u imenu nema "merged".
2. Unesi `start ota`. Ripiter otvara WiFi mrežu pod imenom `MeshCore-OTA` i odgovara adresom svoje stranice za otpremanje.
3. U dometu WiFi mreže poveži telefon ili laptop s tom mrežom, otvori adresu i otpremi datoteku.

## Zakonska ograničenja {#legal}

{{< callout type="legal" verified="2026-10-02" >}}
Evropski preseti za MeshCore nalaze se u podopsegu **869.40-869.65 MHz**. U EU, Ujedinjenom Kraljevstvu, Švajcarskoj i Norveškoj uređaji kratkog dometa mogu da ga koriste bez licence, u okviru ovih ograničenja:

- najviše **500 mW e.r.p.** izračene snage;
- najviše **10% duty cycle**: ne više od 360 sekundi emitovanja u svakom satu, po uređaju. Uređaj umesto toga može da koristi listen-before-talk s adaptive frequency agility, kako je definisano u ETSI EN 300 220-2;
- ceo signal, širok najviše 250 kHz, mora da ostane unutar podopsega.

Opseg je deljen: ne smeš da ometaš licencirane službe, a drugi mogu da ometaju tebe.
Radio mora da ima CE oznaku (u Velikoj Britaniji CE ili UKCA).
{{< /callout >}}

Izvori: [CEPT ERC Recommendation 70-03](https://docdb.cept.org/document/845), Aneks 1, opseg h1.7; [Odluka Komisije 2006/771/EC](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02006D0771(01)-20250123) i njene izmene; [ETSI EN 300 220-2](https://www.etsi.org/deliver/etsi_en/300200_300299/30022002/03.03.01_60/en_30022002v030301p.pdf), opseg O.

### Snaga: e.r.p. i tvoja antena {#erp}

Ograničenje važi za *izračenu* snagu, merenu u odnosu na običnu dipol antenu (e.r.p.). Dobitak antene se dodaje, a gubitak u kablu oduzima. Proizvođači navode dobitak antene u dBi, što je 2.15 dB više od istog dobitka u dBd (u odnosu na dipol). Neka ovaj zbir bude najviše 27 dBm (500 mW):

> predajna snaga (dBm) + dobitak antene (dBi) − gubitak u kablu (dB) − 2.15 ≤ 27

- Ploča emituje 22 dBm u antenu od 5 dBi kroz kabl s gubitkom od 1 dB: 22 + 5 − 1 − 2.15 = 23.85 dBm, oko 240 mW e.r.p. To je u okviru ograničenja.
- Ploča s pojačavačem od 30 dBm (1 W) emituje u antenu od 3 dBi: 30 + 3 − 2.15 = 30.85 dBm, oko 1.2 W e.r.p. To je iznad ograničenja, pa smanji predajnu snagu.

`set tx` podešava izlaz LoRa čipa, u dBm. Sam čip SX1262 ide najviše do 22 dBm, a firmware ne proverava broj koji uneseš. Ploče s dodatnim pojačavačem, kao što su Heltec V4 ili Station G2, emituju mnogo više od broja koji podesiš. Pre podešavanja proveri tabelu proizvođača i počni s niskom vrednošću.

### Duty cycle {#duty-cycle}

Ripiter emituje za sve oko sebe, pa svoje vreme emitovanja troši brže od kompanjona. Ograničavač duty cycle-a u MeshCore-u podrazumevano stoji na 50%, što je iznad dozvoljenog u ovom opsegu. Podesi ga na 10% na svakom ripiteru:

```text
set dutycycle 10
```

### Tačnost frekvencije {#frequency}

Kanal EU/UK (Narrow), 869.618 MHz sa širinom opsega od 62.5 kHz, doseže do 869.649 MHz: manje od 1 kHz ispod gornje granice podopsega. Signal mora da ostane unutar opsega na svakoj temperaturi. Za to je potreban temperaturno kompenzovan kristal (TCXO). Skoro svaka današnja ploča ga ima. Starije ploče bez njega, kao što je Heltec V2, previše odstupaju da bi pouzdano radile na 62.5 kHz.

### Napomene po zemljama {#countries}

- **Države članice EU** moraju da omoguće ovaj podopseg pod ovim uslovima (Odluka 2006/771/EC, član 3).
- **Ujedinjeno Kraljevstvo:** ista ograničenja, u Ofcom dokumentu [IR 2030](https://www.ofcom.org.uk/spectrum/radio-equipment/short-range-devices).
- **Švajcarska i Lihtenštajn:** ista ograničenja, u OFCOM dokumentu [RIR1008-09](https://www.ofcomnet.ch/api/rir/1008/09).
- **Norveška:** ista ograničenja, u [propisu o opštim odobrenjima](https://lovdata.no/dokument/SF/forskrift/2012-01-19-77) (fribruksforskriften).

Ove napomene nisu pravni savet. Pravila se menjaju. U nedoumici proveri kod svog nacionalnog regulatora.

## Kontrolna lista za postavljanje {#checklist}

- [ ] Vlasnik lokacije je dao saglasnost i možeš da pristupiš ripiteru radi održavanja.
- [ ] Na ploči radi **Repeater** firmware, a antenu si povezao pre prvog uključivanja.
- [ ] Administratorska lozinka je promenjena.
- [ ] Radio odgovara [presetu za tvoje područje](/guides/settings/) (`get radio`).
- [ ] Podešeno je `set dutycycle 10`.
- [ ] Predajna snaga i dobitak antene zajedno ostaju u okviru 500 mW e.r.p.
- [ ] Ime, položaj i `owner.info` su podešeni, pa drugi znaju ko upravlja ripiterom.
- [ ] Sat je podešen (`clock`).
- [ ] Kućište je zaptiveno i ima otvor za odvod ili ventilaciju, a kabl ima petlju za oticanje vode.
- [ ] Baterija i panel su dimenzionisani za najgori zimski mesec.
- [ ] Pre odlaska s lokacije testirao si ripiter iz daljine pomoću aplikacije.
- [ ] Tvoja lokalna grupa zna da ripiter radi.
