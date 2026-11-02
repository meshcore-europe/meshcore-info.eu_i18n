---
title: Vodič za antene
lead: Dobra antena, pravilno postavljena, dosegne dalje od veće snage. Provjeri antenu na svom companionu, a zatim odaberi, spoji i postavi antenu za repetitor.
description: 'Odaberi i postavi MeshCore antenu za 868 MHz: provjera štapne antene na companionu, vrste antena i dobitak, konektori, gubitak u kabelu po metru, filtri, postavljanje i kako se dobitak računa u zakonsko ograničenje.'
eyebrow: Companion i repetitor · 868 MHz
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'f828c4aa'
  seeded: '2026-11-02'
  fields: {title: '3a76cb0e', lead: 'd82ec429', description: 'ce3f3e73', eyebrow: 'd2203a35'}
  sections: ['908e2678', 'f9b96f42', 'ca18da90', 'bcfb40ec', '851afd23', '8b7a2209', 'd8832cfa', '5b70b9e8', '14a38e92', 'a5dc1e34', 'de04ca41', 'a23f19c6', '93846db4']
  blocks: ['908e2678', '0868bca9', '081db416', 'ad1da217', '73844333', 'aa14f1b1', '07e4fbad', '32d64d0d', 'ef66133c', '558c115b', '5d28e314', '57d6e138', 'e9b3d055', 'dd757d4a', '2cbd0b58', '21c67ec0', '306a3ded', 'fa46c89f', '1e6ccb3a', 'a3e53320', '6ae131c0', '98f350c6', '138d049d', '3bd28746', '2fc98ff1', '5ea29ee5', 'cfbd64e1', '48833347', '56a82a5c', '4ef7e883', '711e4fee', '1f7844ed', '6b188411', '8da9aa78', '4c2d8bbc', 'a721a9d0', '69c1dc1a', 'a631dbfa', '3f9f3471', '5af4ae3b', 'fa5095fd', '65eeb436', '15aa0eca', 'a8f5b505', '57f35115', '8e5e4975', '89764d3d']
---

Visina, dobro podešena antena i kratak kabel donose veći domet od bilo kojeg
dodatnog milivata. Ovaj vodič počinje companionom, radiom s kojeg šalješ
poruke. Zatim objašnjava antenu na repetitoru, čvoru koji prosljeđuje poruke
s krova ili jarbola.

## Tvoj companion {#companion}

{{< callout type="warning" >}}
Spoji antenu prije nego što uključiš radio. LoRa radio koji odašilje bez
antene može oštetiti vlastiti čip.
{{< /callout >}}

Antena koja je došla uz pločicu sasvim je dovoljna. Spoji je, drži čvor
uspravno i počni slati poruke. Boljom antenom na companionu dobivaš malo, a
repetitorom u dometu puno.

Zasebnu štapnu antenu kupi samo ako je isporučena pokvarena ili je nema. Nije
svaka štapna antena koja se prodaje za 868 MHz podešena za tu frekvenciju.
[Provjeri je NanoVNA uređajem](#nanovna), džepnim analizatorom antena, prije
nego što joj povjeruješ, ili posudi antenu s pločice koja radi.

Čvor pokraj jakog odašiljača čuje manje nego što bi trebao. Mali
[SAW filtar (filtar s površinskim akustičnim valom)](#filters) između radija i
antene ne pušta taj odašiljač u prijemnik. Prvo provjeri njegov tehnički list:

- **Najveća ulazna snaga.** Filtar se nalazi i na putu tvog vlastitog
  odašiljanja. Pločica koja odašilje 22 dBm (160 mW) uništit će filtar
  predviđen za 15 dBm.
- **Propusni pojas.** Mora obuhvaćati frekvenciju tvog preseta. Filtar za
  868.65 do 869.25 MHz ne propušta kanal EU/UK (Narrow) na 869.618 MHz.

## Vrste antena za repetitor {#types}

Sve antene u mreži stoje uspravno. Vrstu odaberi prema tome gdje su čvorovi
koje želiš dosegnuti:

- **Kolinearna antena od stakloplastike.** Bijela cijev na jarbolu, s dobitkom
  duž cijelog obzora. To je standardni izbor za repetitor koji pokriva grad.
- **Dipol.** Kraći je, ima manji dobitak i visok snop. Čvorove ispod i iznad
  sebe dosežeš njime bolje nego kolinearnom antenom, primjerice s brda iznad
  doline.
- **Yagi.** Nosač s poprečnim elementima, usmjeren prema jednom mjestu. Njime
  dosežeš jedan udaljeni repetitor i malo što drugo. Postavi ga s uspravnim
  elementima, jer polarizacija prati smjer elemenata.

## Dobitak i snop {#gain}

Dobitak ne dodaje snagu. Antena uzima signal koji bi otišao gore i dolje te ga
šalje duž obzora. Slično je sa svjetiljkom koju fokusiraš: baterija je ista, a
snop dulji i uži. To se vidi na dipolu i kolinearnoj anteni istog proizvođača:

| Antena | Dobitak | Okomita širina snopa |
|---|---|---|
| Dipol (Sirio SO 868-915-2) | 2.2 dBi | 88 stupnjeva |
| Kolinearna antena od stakloplastike (Sirio SPO 868-915-6) | 5.8 dBi | 23 stupnja |

{{< gain >}}

Dijagram prikazuje presjek kroz jarbol, gledano sa strane. Zarotiraj ga oko
jarbola i dobit ćeš cijeli snop: krafnu kod dipola, ravan disk kod kolinearne
antene. Uspravna antena odašilje jednako u svim smjerovima oko sebe. Izvan
nacrtanog snopa signal ne prestaje: slabiji je, ali i dalje dovoljan za obližnji
čvor.

Na krovu ti treba ravan snop. Na brdu visoko iznad čvorova snop od 23 stupnja
prolazi iznad njih, a dipol ih pokriva. Yagi ide još dalje: 16.6 dBi u snopu
visokom 23 stupnja i širokom 25 stupnjeva (Amphenol Procom 7176870), a u stranu
ništa.

Dobitak se izražava u odnosu na referencu. dBi uspoređuje antenu s idealnom antenom
koja odašilje jednako u svim smjerovima. dBd je uspoređuje s poluvalnim dipolom, koji
sam ima 2.15 dBi: čak ni najjednostavnija antena ne odašilje ništa ravno gore ili
dolje. Dulji dipol, od 1.25 valne duljine, doseže 5.2 dBi. Kolinearna antena
umjesto toga slaže poluvalne elemente jedan iznad drugog: što ih je više, dobitak
je veći. Sažmeš li isti signal u pola prostora, tamo je dvostruko jači: 3 dB. U
četvrtini prostora jači je 4 puta: 6 dB. Proizvođači navode dobitak u dBi, a
zakonsko ograničenje računa se u dBd, pogledaj
[Unutar zakonskog ograničenja](#legal).

### Koji dobitak za tvoju lokaciju {#choose-gain}

- **Brda, doline ili gusto izgrađen grad: oko 3 dBi.** Visoki snop doseže čvorove
  iznad i ispod tebe te zaobilazi padine i zgrade na putu. Vrijedi i obrnuto: iz
  doline ravan snop prolazi ispod repetitora na brdu iznad. Takva je antena
  RAKwireless RAKARG12: cijev od stakloplastike duga 36 cm.
- **Predgrađe ili grad s niskim krovovima: 5 do 6 dBi.** Standardna kolinearna
  antena od stakloplastike.
- **Ravan, otvoren teren: 8 do 10 dBi.** Najravniji snop najdalje dosiže duž
  obzora. Postavljen visoko, prolazi iznad obližnjih čvorova.

Dobitak u nazivu najbolja je vrijednost u cijelom pojasu antene. RAKARG12,
koji se prodaje kao antena od 3 dBi, ima 2.8 dBi na 865 do 870 MHz. U tablici
dobitka u tehničkom listu očitaj vrijednost za frekvenciju svog preseta.

Iznad 7 dBi pločica od 22 dBm prelazi zakonsko ograničenje, osim ako gubici u
kabelu i filtru nadoknade razliku. Smanji snagu odašiljanja u skladu s time.

Visok dobitak pomaže samo ako znaš gdje su čvorovi: duž obzora oko repetitora ili
kod jednog udaljenog repetitora za Yagi. Companion u ruci okrenut je na sve
strane, pa mu najbolje odgovara nizak dobitak antene s kojom je došao.

## Zašto okomito {#vertical}

Antene se najbolje čuju kad su okrenute u istom smjeru. Gubitak raste s kutom između
njih: pri 45 stupnjeva gubiš 3 dB, pola svog signala. Pri 90 stupnjeva, kad je jedna
antena položena, a druga uspravna, u teoriji ne stiže ništa. Antene u mreži stoje
uspravno, pa mora i tvoja. To vrijedi i za companion na stolu: položiš li ga, svaki
čvor oko tebe čuje manje.

## Konektori {#connectors}

Naruči antenu s konektorom koji ima tvoja pločica. Svaki adapter znači još jedan
spoj za brtvljenje i dodatni gubitak signala.

- **SMA.** Navojni konektor širok oko 6 mm. Utičnica na većini pločica ima rupu u
  sredini, a antena ima pin. Ovakav konektor gubi oko 0.03 dB na 868 MHz.
- **RP-SMA.** Isto tijelo i navoj kao SMA, ali pin i rupa zamijenili su mjesta.
  Izgleda kao SMA, ali se s njim ne može spojiti. Prije narudžbe provjeri koji
  konektor ima tvoja pločica.
- **U.FL (IPEX).** Sićušna utisna utičnica na samoj pločici. Od nje kratki pigtail
  kabel vodi do SMA utičnice na kućištu. Predviđena je za 30 spajanja, pa je spoji
  jednom i ostavi tako.
- **N.** Veliki navojni konektor na antenama od stakloplastike i debelom kabelu.
  Gubi najviše 0.05 dB. Za repetitor ti treba jedan adapter ili pigtail s N
  konektora na SMA konektor pločice.

## Gubitak u kabelu {#cable}

Kabel troši signal prije nego što napusti antenu, u oba smjera. 3 dB je pola tvoje
snage. Podaci proizvođača po metru, na 868 do 900 MHz:

| Kabel | Gubitak po metru | Gubitak na 5 m |
|---|---|---|
| RG174 | 1.02 dB | 5.1 dB |
| RG316 | 0.78 dB | 3.9 dB |
| RG58 | 0.45 dB | 2.2 dB |
| H-155 | 0.27 dB | 1.4 dB |
| LMR-240 | 0.25 dB | 1.2 dB |
| Ecoflex 10 | 0.13 dB | 0.7 dB |
| LMR-400 | 0.13 dB | 0.6 dB |

3 metra kabela RG174, tankog pigtaila koji dolazi uz mnoge pločice, gube pola tvoje
snage. Postavi pločicu uz antenu s kratkim pigtailom ili do antene provuci debeli
kabel. U zbroj dodaj svaki adapter i filtar na putu signala.

## Filtri {#filters}

Filtar se nalazi između radija i antene. Propušta tvoj pojas i blokira ostalo, pa
jak obližnji odašiljač ne preplavi prijemnik. Treba ti kad čvor u blizini drugih
odašiljača čuje manje nego što bi trebao. Takav je čvor repetitor na jarbolu s
baznim stanicama mobilne mreže. Filtar troši signal u oba smjera: njegov gubitak
računaj kao gubitak u kabelu.

| | SAW filtar | Šupljinski filtar |
|---|---|---|
| Veličina | Nekoliko milimetara, na maloj pločici | Metalni blok ili cijev |
| Gubitak dobrog filtra | ispod 2 dB | ispod 1 dB |
| Najveća ulazna snaga dobrog filtra | 500 mW | nekoliko vata |

Primjerice, sysmocom cf866.5-kt30 šupljinski je filtar za 863 do 870 MHz koji gubi
najviše 1.0 dB i podnosi 30 W. Namijenjen je unutarnjoj upotrebi, pa ga na
jarbolu stavi u zabrtvljenu kutiju.

Filtri se jako razlikuju, pa prije kupnje provjeri tehnički list. Nazivna ulazna
snaga mora biti veća od tvoje snage odašiljanja, a propusni pojas mora obuhvaćati
frekvenciju tvog preseta.

## Postavljanje {#mounting}

- **Iznad ruba krova.** Antena mora imati čist pogled u svim smjerovima koje pokriva.
  Pomaže čak i nekoliko metara iznad okolnih krovova. Odjeljak
  [Odaberi lokaciju](/repeater-guide/#site) u vodiču za repetitore objašnjava kako
  provjeriti pogled.
- **Dalje od metala.** Oluci, jarboli, druge antene i metalni krovovi pokraj antene
  mijenjaju njezin dijagram zračenja i podešenost. Postavi je na vrh jarbola, ne
  pokraj njega.
- **Uspravno.** Koristi libelu (pogledaj [Zašto okomito](#vertical)).
- **Petlja za kapanje.** Pusti da kabel visi ispod konektora prije nego što krene
  prema gore ili unutra. Voda tada kaplje s kabela umjesto da uđe u spoj.
- **Zabrtvi svaki vanjski konektor.** Voda u konektoru povećava gubitak i nagriza
  pin. Zabrtvi ga protiv kiše i svake godine provjeri brtvu.
- **Munja.** Antena na krovu meta je za munju. Plinski odvodnik prenapona u kabelu
  reagira na prenapon i odvodi ga u uzemljenje. Za uzemljenje slijedi upute iz
  odjeljka [Hardver](/repeater-guide/#hardware) u vodiču za repetitore i lokalne
  propise.

## Unutar zakonskog ograničenja {#legal}

{{< callout type="legal" verified="2026-10-22" >}}
U Europi MeshCore koristi podpojas 869.40-869.65 MHz, s najviše **500 mW**
efektivne izračene snage (e.r.p.). Ograničenje se odnosi na ono što izlazi iz
antene: dobitak antene se dodaje, a gubici u kabelu i filtru oduzimaju. Dobitak u
dBi računa se 2.15 dB manje, jer se ograničenje mjeri u odnosu na dipol.
{{< /callout >}}

Kolinearna antena od 5.8 dBi na pločici od 22 dBm ostaje unutar ograničenja. Ista
antena na pločici s pojačalom prelazi ga dok ne smanjiš snagu odašiljanja.
Odjeljak [Snaga: e.r.p. i tvoja antena](/repeater-guide/#erp) u vodiču za repetitore
sadrži izračun i 2 razrađena primjera.

## Provjeri antenu NanoVNA uređajem {#nanovna}

NanoVNA je vektorski analizator mreže džepne veličine. Pokazuje na koju je
frekvenciju antena podešena, pa to znaš prije postavljanja. NanoVNA-H mjeri do
1.5 GHz, što pokriva 868 MHz.

1. Kalibriraj ga za 800 do 950 MHz pomoću open, short i load nastavaka iz njegova
   kompleta.
2. Spoji antenu preko adaptera koji će koristiti na čvoru. Drži je uspravno i podalje
   od tijela i stola.
3. Očitaj krivulju SWR (omjer stojnih valova): ona pokazuje koliko signala antena
   vraća natrag. Najniža točka krivulje mora biti na frekvenciji tvog preseta, 869.618
   MHz za EU/UK (Narrow). Ako je ta točka stotinama MHz dalje, antena je napravljena
   za drugi pojas.

Četvrtina vala na 868 MHz iznosi 86 mm (valna duljina je 345 mm). Sama duljina ne
otkriva pojas, jer proizvođači savijaju i dodatno opterećuju štapne antene, a
NanoVNA ga otkriva.

## Izvori {#sources}

- Gubitak u kabelu: [Belden 8216 (RG174)](https://catalog.belden.com/techdata/en/8216_techdata.pdf),
  tehnički list Huber+Suhner RG316,
  [Belden 8240 (RG58)](https://catalog.belden.com/techdata/en/8240_techdata.pdf),
  [SSB H-155](https://www.ssb.de/media/h155ssb-en.pdf),
  tehnički listovi Times Microwave LMR-240 i LMR-400,
  [SSB Ecoflex 10](https://www.rigpix.com/otherusefulinfo/coax/ecoflex10.pdf).
- Antene: [Sirio SPO 868-915-6](https://rigpix.com/antennas/sirio_spo8689156_manual.pdf),
  tehnički list Sirio SO 868-915-2,
  [Amphenol Procom 7176870](https://amphenolprocom.com/products/base-station-antennas/2236-7176870),
  [RAKwireless RAKARG12](https://docs.rakwireless.com/product-categories/accessories/rakarg12/datasheet/).
- Dobitak kao signal sažet u manji prostor: [RF Cafe, uvod u antene](https://www.rfcafe.com/references/electrical/ew-radar-handbook/antenna-introduction-basics.htm).
- Konektori: tehnički listovi Rosenberger 32S102 (SMA) i 53S101 (N), katalog
  Hirose U.FL.
- Filtri: stranica proizvoda sysmocom cf866.5-kt30,
  [plinski odvodnici prenapona Citel](https://citel.us/en/gas-tube-surge-arrestors-for-coaxial-line-protection).
- Gubitak zbog polarizacije: [Sveučilište u Torontu, Friisovi efekti](https://www.waves.utoronto.ca/prof/svhum/ece422/notes/12-friiseffects.pdf).
- Dobitak dipola prema duljini: [Wikipedia, dipolna antena](https://en.wikipedia.org/wiki/Dipole_antenna).
- Valna duljina: brzina svjetlosti prema [NIST-u](https://physics.nist.gov/cgi-bin/cuu/Value?c).
- NanoVNA: [NanoVNA-H](https://github.com/hugen79/NanoVNA-H).
- Zakonsko ograničenje: [CEPT ERC preporuka 70-03](https://docdb.cept.org/document/845),
  Dodatak 1, pojas h1.7, a [vodič za repetitore](/repeater-guide/#legal) navodi
  ostalo.
