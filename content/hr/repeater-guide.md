---
title: Vodič za repetitore
lead: Repetitor postavljen visoko prosljeđuje poruke svima oko sebe, diljem cijelog grada ili doline. Odaberi lokaciju, napajaj ga sunčevom energijom, postavi ga i poštuj propise.
description: 'Isplaniraj, napajaj, podesi i zakonito koristi MeshCore repetitor u Europi: izbor lokacije, dimenzioniranje solarnog sustava, CLI postavke, ograničenja snage i radnog ciklusa na 868 MHz.'
eyebrow: 868 MHz · do 500 mW · bez licence
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '3e38a8c6'
  seeded: '2026-11-04'
  fields: {title: '4608abcd', lead: 'bc670c65', description: '9e483ce5', eyebrow: '9fd33416'}
  sections: ['05ee477a', '938c518c', '824ab38e', '662ea23c', '70faf508', '8bc641aa', '399cd683', 'e9dedb7b', '92beca03', '17634750', 'cadf6024', 'e9cc6834', '2e6e59ca', 'fb44b8db']
  blocks: ['20ac0371', 'ed2b1adf', '432543ee', '7af42c89', 'd0f7543a', '9ef3580f', '3476aef7', '1bab7bec', 'bbea9a0c', '2b9fab3b', 'b13d1947', 'c2bad16f', '636edc86', 'c2d6bcd1', '957ae975', '98874949', '96d1ebad', 'dbd9fa1f', 'aa06d32b', '9958aad3', 'd162b028', 'cca1bbdf', '64ef011d', 'e7f16724', 'd2e34ff0', 'bb195cfc', '8d080bb3', '2b1d995b', '210f1b66', 'dc7419d2', 'bdc66db0', 'b59f248c', '7184bd63', 'de5a24f9', 'f5cfb426', '48c7422f', '9d3c0836', 'da8a6af3', '240126df', '8aac2b33', '81a475b8', 'a53e42b5', '36ff1db4', 'e4ca8602', 'e4594afd', '3b24b8e9', '58330858', '68f2966e', 'd7418228', '23536e60', 'cbc5c2d1', '2ea02ba9', '92540256', '6e21f681', 'a8c12311', '3382ae7f', 'cdeafb0f', '1b1319d2']
---

Mreža počiva na repetitorima. Companioni, radiji s kojih šalješ poruke, ne prosljeđuju poruke. Bez repetitora zato dopireš samo do ljudi u izravnom dometu. Repetitor na pravom mjestu proširuje mrežu za sve oko sebe. Ovaj vodič temelji se na firmwareu MeshCore v1.18.0.

Prije početka razgovaraj sa svojom [lokalnom grupom](/community/). Članovi znaju gdje nedostaje pokrivenost, [koji se preset koristi u tvom području](/guides/settings/) i kako imenovati repetitore. Na [kartama pokrivenosti](/map/) provjeri ima li repetitora blizu tebe i pozdravi ostale na javnim ili lokalnim [kanalima](/guides/channels/).

## Treba li ti repetitor? {#need}

Repetitor prosljeđuje svaku flood poruku koju čuje, a svi repetitori u dometu dijele isto vrijeme emitiranja. Gdje te mreža već doseže, još jedan repetitor povećava promet, ne pokrivenost. Možda će ti biti dovoljan companion postavljen visoko, na tavanskom prozoru ili balkonu.

Postavi repetitor tamo gdje nedostaje pokrivenost:

- na [kartama pokrivenosti](/map/) nema repetitora blizu tebe ili su tu samo oni koje tvoj companion ne čuje;
- tvoja lokalna grupa kaže da tom području treba repetitor.

## Odaberi lokaciju {#site}

Visina vrijedi više od snage. LoRa na 868 MHz najbolje se širi uz čistu liniju vidljivosti. Brda, zgrade i gusto drveće oduzmu daleko više dometa nego što nekoliko dodatnih milivata može vratiti.

- **Biraj visoko mjesto.** Krov, stup, visoka zgrada ili brdo pokrivaju puno više od prozorske daske. Pomaže već i nekoliko metara iznad okolnih krovova.
- **Drži antenu na otvorenom.** Montiraj je iznad rubova krova, podalje od metala, oluka i drugih antena.
- **Provjeri vidljivost.** Alati poput [HeyWhatsThat](https://www.heywhatsthat.com/) pokazuju što se vidi s nekog mjesta. Aplikacija MeshCore [izračuna dokle seže repetitor na tom mjestu](#check-site).
- **Ostavi slobodan prostor.** Radijskom putu treba slobodan prostor oko izravne linije, ne samo sama linija. Na 868 MHz taj je prostor oko 20 m u sredini puta od 5 km. Na putu od 20 km iznosi oko 40 m.
- **Zatraži dopuštenje.** Dobij pristanak vlasnika krova ili stupa i dogovori kako ćeš doći do repetitora radi održavanja.

### Provjeri lokaciju u aplikaciji {#check-site}

Od verzije 1.33 aplikacija MeshCore ima ove alate u izborniku, pod **Tools**. Rade i bez spojenog radija.

- **Line of Sight** crta teren između 2 točke i prostor koji signalu treba iznad njega. Dugo pritisni 2 točke na karti ili dodirni repetitore.
- **Antenna Coverage** na karti pokazuje dokle doseže antena na 1 točki. Dugo pritisni točku ili dodirni repetitor. Dodaj još točaka da usporediš lokacije.

Na računalu u izborniku alata odaberi **Add Point** i upiši koordinate.

Oba alata polaze od antene na tvojoj lokaciji na 5 m, pa u postavkama alata
upiši visinu koju planiraš. Antenna Coverage polazi od prijamne antene
na 1 m. Bez spojenog radija Line of Sight polazi od 915 MHz: u njegovim postavkama
upiši frekvenciju svog [preseta](/guides/settings/).

Alati računaju na temelju podataka o visini i ne testiraju tvoj radio. Drveće
i nove zgrade provjeri sam. Zatim odnesi companion na to mjesto i pogledaj koje
repetitore čuje.

![Line of Sight u aplikaciji MeshCore: teren između 2 točke i prostor koji signalu treba iznad njega](/media/guides/line-of-sight.webp)

![Antenna Coverage u aplikaciji MeshCore: područje koje antena na brdu može doseći, prikazano na karti](/media/guides/antenna-coverage.webp)

## Hardver {#hardware}

- **Pločica.** Odaberi nRF52 pločicu niske potrošnje, poput modela [Heltec T114](/devices/), RAK WisBlock ili SenseCAP Solar Node. ESP32 pločice troše više energije (na stranici s uređajima označene su kao High), pa ih je teško napajati solarno.
- **Antena.** Koristi antenu namijenjenu za 868 MHz i montiraj je okomito. [Vodič za antene](/guides/antenna/) obrađuje tipove, konektore, kabele i montažu. Dobitak antene ulazi u zakonsko ograničenje snage: pogledaj [Zakonska ograničenja](#legal).
- **Kabel.** Neka koaksijalni kabel bude kratak ili koristi kabel s malim gubicima. Na 868 MHz u nekoliko metara tankog kabela možeš izgubiti pola snage.
- **Kućište.** Vodootporna kutija (IP65 ili bolja) s kabelskom uvodnicom, otvorom za odzračivanje ili odvod protiv kondenzacije, svijetle boje ili sa zaštitom od sunca. Baterije loše podnose vrućinu i ne mogu se puniti na temperaturama ispod nule.
- **Munja.** Antena na krovu je meta. Drži se lokalnih pravila za uzemljenje ili je montiraj tako da udar ne dopre do električnih instalacija zgrade.

## Napajanje i dimenzioniranje solarnog sustava {#power}

Solarni repetitor mora preživjeti najmračnije zimske tjedne. Dimenzioniraj ga prema njima:

1. **Izmjeri potrošnju.** Pusti podešeni repetitor da jedan dan radi preko USB mjerača snage. Očitaj utrošenu energiju u vat-satima (Wh). Promet u tvom području utječe na taj broj, pa mjeri na lokaciji ako možeš.
2. **Dodaj rezervu.** Planiraj kapacitet baterije za najmanje 5 do 7 dana bez korisnog sunca.
3. **Provjeri koliko sunca imaš zimi.** Besplatni EU-ov [alat PVGIS](https://re.jrc.ec.europa.eu/pvg_tools/en/) za svaku lokaciju pokazuje koliko energije panel proizvede mjesečno. Uzmi mjesec s najmanje sunca.
4. **Dimenzioniraj panel.** Panel mora nadoknaditi dnevnu potrošnju u tom najgorem mjesecu, uz rezervu za gubitke pri punjenju.

Primjer izračuna s pretpostavljenim brojkama: repetitoru koji troši 1 Wh dnevno treba baterija od najmanje 7 Wh za tjedan dana rezerve, što je oko 2 Ah iskoristivog kapaciteta na 3.7 V. Ako PVGIS kaže da panel od 1 W na tvojoj lokaciji u prosincu daje 0.5 Wh dnevno, treba ti panel od najmanje 2 W. S 3 do 5 W imaš rezervu za oblake, snijeg i starenje.

## Postavljanje {#config}

**Flashanje.** Otvori [web flasher](https://flasher.meshcore.io) i odaberi firmware **Repeater** za svoju pločicu. Korake flashanja naći ćeš na stranici [Prvi koraci](/get-started/#flash).

**Podešavanje preko USB-a.** Dok je repetitor još spojen na računalo, otvori [config.meshcore.io](https://config.meshcore.io) ili konzolu flashera. Možeš koristiti i bilo koji serijski terminal na 115200 bauda. Najvažnije naredbe:

| Što | Naredba |
|---|---|
| Promjena administratorske lozinke | `password <new password>` |
| Dodjela imena | `set name <name>` |
| Radijski preset: frekvencija, širina pojasa, SF, CR (primjenjuje se nakon ponovnog pokretanja) | `set radio 869.618,62.5,8,8` |
| Ograničenje radnog ciklusa, u postocima | `set dutycycle 10` |
| Snaga odašiljanja radijskog čipa, u dBm | `set tx <dBm>` |
| Položaj, za prikaz na kartama | `set lat <degrees>` i `set lon <degrees>` |
| Kontakt podaci za druge operatere | `set owner.info <text>` |
| Sati između flood objava, onih koje čuje cijela mreža | `set flood.advert.interval <hours>` |
| Trenutna objava repetitora | `advert` |
| Ponovno pokretanje | `reboot` |

Zadana administratorska lozinka je `password`, a svatko tko se njome prijavi postaje administrator. Promijeni je prije nego što repetitor počne emitirati.

Gornji primjer za `set radio` vrijedi za EU/UK (Narrow). Umjesto njega upiši vrijednosti preseta za svoje područje: stranica [Preporučene postavke](/guides/settings/) navodi ih po državama.

**Podesi sat.** Bez modula sata (RTC) repetitor pri svakom nestanku struje gubi vrijeme i kreće ponovno od svibnja 2024. Dok radi, sat mu i odstupa: sve više žuri ili kasni. Zato povremeno podesi sat: prijavi se na daljinu iz aplikacije i upotrijebi `clock sync` ili postavi vrijeme preko USB-a. S RTC modulom to ti rijetko treba: on čuva vrijeme tijekom nestanka struje i puno manje odstupa.

**Upravljanje na daljinu.** Kad je repetitor na mreži, prijavi se iz aplikacije MeshCore administratorskom lozinkom. Tamo očitavaš njegov status i preko radija koristiš iste naredbe. Neke naredbe rade samo preko USB-a, primjerice `set freq` i `erase` za vraćanje na tvorničke postavke.

**Sačuvaj identitet.** Prije brisanja upiši `get prv.key` preko USB-a i spremi prikazani privatni ključ na sigurno mjesto. Nakon brisanja naredbe `set prv.key <key>` i `reboot` vraćaju repetitoru stari identitet. Čvorovi koji ga poznaju tako ga nalaze pod istim prefiksom.

Cijeli popis naredbi nalazi se u [referenci za MeshCore CLI](https://github.com/meshcore-dev/MeshCore/blob/main/docs/cli_commands.md).

## Bežično ažuriranje {#update}

Kad je repetitor postavljen visoko, ažuriraš ga sa zemlje. Prijavi se iz aplikacije MeshCore administratorskom lozinkom, otvori njegov naredbeni redak i upiši `start ota`. Dalje ovisi o pločici: ostale pločice odgovaraju s `Error`, a njih ažuriraš preko USB-a.

**nRF52 pločice**, poput RAK, Heltec T114, Seeed XIAO i SenseCAP Solar:

1. S [web flashera](https://flasher.meshcore.io) preuzmi **ZIP** novog firmwarea za svoju pločicu.
2. Upiši `start ota`. Repetitor odgovara s `OK` i preko Bluetootha se pojavljuje kao `<board>_OTA`, primjerice `RAK4631_OTA`.
3. Na mobitelu otvori aplikaciju nRF Device Firmware Update, odaberi ZIP i repetitor te pokreni prijenos. To traje nekoliko minuta.

Instaliraj [OTAFIX bootloader](https://github.com/oltaco/Adafruit_nRF52_Bootloader_OTAFIX) na nRF52 pločicu prije nego što je postaviš na visinu. S tvorničkim bootloaderom neuspjelo ažuriranje možeš popraviti samo preko USB-a. S OTAFIX-om se pločica vraća u način ažuriranja, a ti pokušavaš ponovno preko Bluetootha.

**ESP32 pločice**, poput Heltec V3 i V4:

1. S web flashera preuzmi **non-merged** `.bin` za svoju pločicu: datoteku bez riječi "merged" u nazivu.
2. Upiši `start ota`. Repetitor otvara WiFi mrežu pod nazivom `MeshCore-OTA` i odgovara adresom svoje stranice za prijenos.
3. U dometu WiFi mreže spoji mobitel ili laptop na tu mrežu, otvori adresu i prenesi datoteku.

## Zakonska ograničenja {#legal}

{{< callout type="legal" verified="2026-10-02" >}}
Europski preseti za MeshCore nalaze se u podpojasu **869.40-869.65 MHz**. U EU-u, Ujedinjenoj Kraljevini, Švicarskoj i Norveškoj taj je podpojas otvoren uređajima kratkog dometa bez licence, uz ova ograničenja:

- najviše **500 mW e.r.p.** izračene snage;
- najviše **10% radnog ciklusa**: ne više od 360 sekundi odašiljanja u bilo kojem satu, po uređaju. Uređaj umjesto toga smije koristiti listen-before-talk s adaptivnom frekvencijskom agilnošću, kako je definirano u ETSI EN 300 220-2;
- cijeli signal, širok najviše 250 kHz, mora ostati unutar podpojasa.

Pojas je zajednički: ne smiješ ometati licencirane službe, a drugi smiju ometati tebe.
Radio mora imati oznaku CE (u Velikoj Britaniji CE ili UKCA).
{{< /callout >}}

Izvori: [CEPT ERC preporuka 70-03](https://docdb.cept.org/document/845), Prilog 1, pojas h1.7; [Odluka Komisije 2006/771/EZ](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02006D0771(01)-20250123) i njezine izmjene; [ETSI EN 300 220-2](https://www.etsi.org/deliver/etsi_en/300200_300299/30022002/03.03.01_60/en_30022002v030301p.pdf), pojas O.

### Snaga: e.r.p. i tvoja antena {#erp}

Ograničenje se odnosi na *izračenu* snagu, mjerenu u odnosu na običnu dipolnu antenu (e.r.p.). Dobitak antene se pribraja, a gubitak u kabelu oduzima. Proizvođači navode dobitak antene u dBi, što je 2.15 dB više od istog dobitka u dBd (u odnosu na dipol). Neka ovaj zbroj bude najviše 27 dBm (500 mW):

> snaga odašiljanja (dBm) + dobitak antene (dBi) − gubitak u kabelu (dB) − 2.15 ≤ 27

- Pločica odašilje 22 dBm u antenu od 5 dBi kroz kabel s gubitkom od 1 dB: 22 + 5 − 1 − 2.15 = 23.85 dBm, oko 240 mW e.r.p. To je unutar ograničenja.
- Pločica s pojačalom od 30 dBm (1 W) odašilje u antenu od 3 dBi: 30 + 3 − 2.15 = 30.85 dBm, oko 1.2 W e.r.p. To je iznad ograničenja, pa smanji snagu odašiljanja.

`set tx` postavlja izlaznu snagu LoRa čipa, u dBm. Sam čip SX1262 doseže najviše 22 dBm, a firmware ne provjerava broj koji upišeš. Pločice s dodatnim pojačalom, poput Heltec V4 ili Station G2, odašilju puno više od postavljenog broja. Prije postavljanja provjeri proizvođačevu tablicu i kreni od niske vrijednosti.

### Radni ciklus {#duty-cycle}

Repetitor odašilje za sve oko sebe, pa svoje vrijeme emitiranja troši brže od companiona. Limiter radnog ciklusa u MeshCoreu zadano je postavljen na 50%, što je iznad dopuštenog u ovom pojasu. Postavi ga na 10% na svakom repetitoru:

```text
set dutycycle 10
```

### Točnost frekvencije {#frequency}

Kanal EU/UK (Narrow), 869.618 MHz sa širinom pojasa od 62.5 kHz, seže do 869.649 MHz: manje od 1 kHz ispod gornje granice podpojasa. Signal mora ostati unutar pojasa na svakoj temperaturi. Za to treba temperaturno kompenzirani kristal (TCXO). Ima ga gotovo svaka današnja pločica. Starije pločice bez njega, poput Heltec V2, previše odstupaju za pouzdan rad na 62.5 kHz.

### Napomene po državama {#countries}

- **Države članice EU-a** moraju staviti ovaj podpojas na raspolaganje pod ovim uvjetima (Odluka 2006/771/EZ, članak 3).
- **Ujedinjena Kraljevina:** ista ograničenja, u Ofcomovu dokumentu [IR 2030](https://www.ofcom.org.uk/spectrum/radio-equipment/short-range-devices).
- **Švicarska i Lihtenštajn:** ista ograničenja, u OFCOM-ovu dokumentu [RIR1008-09](https://www.ofcomnet.ch/api/rir/1008/09).
- **Norveška:** ista ograničenja, u [propisu o općim odobrenjima](https://lovdata.no/dokument/SF/forskrift/2012-01-19-77) (fribruksforskriften).

Ove napomene nisu pravni savjet. Pravila se mijenjaju, pa u slučaju dvojbe provjeri kod nacionalnog regulatora.

## Kontrolni popis za postavljanje {#checklist}

- [ ] Vlasnik lokacije se složio i možeš doći do repetitora radi održavanja.
- [ ] Na pločici je firmware **Repeater**, a antena je spojena prije prvog uključivanja.
- [ ] Administratorska lozinka je promijenjena.
- [ ] Radio odgovara [presetu tvog područja](/guides/settings/) (`get radio`).
- [ ] Postavljeno je `set dutycycle 10`.
- [ ] Snaga odašiljanja i dobitak antene zajedno ostaju unutar 500 mW e.r.p.
- [ ] Ime, položaj i `owner.info` su postavljeni, pa drugi znaju tko upravlja repetitorom.
- [ ] Sat je podešen (`clock`).
- [ ] Kućište je zabrtvljeno i ima otvor za odvod ili odzračivanje, a kabel ima petlju za otjecanje vode.
- [ ] Baterija i panel dimenzionirani su za najgori zimski mjesec.
- [ ] Prije odlaska s lokacije testirao si repetitor iz daljine pomoću aplikacije.
- [ ] Tvoja lokalna grupa zna da repetitor radi.
