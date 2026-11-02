---
title: Vodič za antene
lead: Dobra antena, dobro postavljena, dobacuje dalje od veće snage. Proveri antenu na svom companionu, a zatim izaberi, poveži i postavi antenu za repetitor.
description: 'Izaberi i postavi MeshCore antenu za 868 MHz: provera štapaste antene na companionu, tipovi antena i dobitak, konektori, gubici u kablu po metru, filteri, montaža i uticaj dobitka na zakonsku granicu.'
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

Visina, podešena antena i kratak kabl donose veći domet od bilo kog dodatnog
milivata. Ovaj vodič počinje od companiona, radija s kojeg šalješ poruke.
Zatim prelazi na antenu repetitora, čvora koji prenosi poruke s krova ili jarbola.

## Tvoj companion {#companion}

{{< callout type="warning" >}}
Prvo priključi antenu, pa tek onda uključi radio. LoRa radio koji emituje bez
antene može da ošteti sopstveni čip.
{{< /callout >}}

Antena koja stiže uz ploču sasvim je dovoljna. Priključi je, drži čvor
uspravno i počni da šalješ poruke. Bolja antena na companionu donosi malo, a
repetitor u dometu donosi mnogo.

Posebnu štapastu antenu kupi samo ako je isporučena polomljena ili ako je nemaš.
Nije svaka štapasta antena koja se prodaje za 868 MHz zaista podešena za tu
frekvenciju. Pre nego što se osloniš na nju, [proveri je NanoVNA uređajem](#nanovna),
džepnim analizatorom antena, ili pozajmi antenu s ploče koja radi.

Čvor pored jakog predajnika čuje manje nego što bi trebalo. Mali
[SAW filter (filter s površinskim akustičnim talasima)](#filters) između radija i
antene ne pušta signal tog predajnika u prijemnik. Prvo proveri njegov datasheet:

- **Maksimalna ulazna snaga.** Kroz filter prolazi i tvoje emitovanje. Ploča koja
  emituje 22 dBm (160 mW) uništiće filter predviđen za 15 dBm.
- **Propusni opseg.** Mora da obuhvata frekvenciju tvog preseta. Filter za
  868.65 do 869.25 MHz ne propušta EU/UK (Narrow) kanal na 869.618 MHz.

## Tipovi antena za repetitor {#types}

Sve antene u mreži stoje uspravno. Tip biraš prema tome gde su čvorovi do kojih
želiš da dopreš:

- **Kolinearna antena od fiberglasa.** Bela cev na jarbolu, s dobitkom svuda duž
  horizonta. To je standardni izbor za repetitor koji pokriva grad.
- **Dipol.** Kraći je, ima manji dobitak i visok snop. Bolje od kolinearne antene
  doseže čvorove ispod i iznad tebe, na primer s brda iznad doline.
- **Yagi.** Nosač s poprečnim elementima, usmeren ka jednom mestu. Doseže jedan
  daleki repetitor i malo šta drugo. Postavi je s uspravnim elementima, jer njena
  polarizacija prati elemente.

## Dobitak i snop {#gain}

Dobitak ne dodaje snagu. Antena uzima signal koji bi otišao gore i dole i šalje
ga duž horizonta. Slično je s baterijskom lampom koju fokusiraš: ista baterija,
duži i uži snop. Dipol i kolinearna antena istog proizvođača to pokazuju:

| Antena | Dobitak | Vertikalna širina snopa |
|---|---|---|
| Dipol (Sirio SO 868-915-2) | 2.2 dBi | 88 stepeni |
| Kolinearna antena od fiberglasa (Sirio SPO 868-915-6) | 5.8 dBi | 23 stepena |

{{< gain >}}

Dijagram prikazuje presek kroz jarbol, gledano sa strane. Okreni ga oko jarbola
i dobićeš ceo snop: krofnu kod dipola, ravan disk kod kolinearne antene. Uspravna
antena emituje jednako u svim pravcima oko sebe. Signal ne prestaje izvan nacrtanog
snopa. Tamo je slabiji, ali i dalje dovoljan za obližnji čvor.

Na krovu ti treba ravan snop. Na brdu visoko iznad čvorova snop od 23 stepena
prolazi iznad njihovih glava, a dipol ih pokriva. Yagi ide još dalje: 16.6 dBi
u snopu visokom 23 stepena i širokom 25 stepeni (Amphenol Procom 7176870), a
ka stranama ništa.

Dobitak se računa u odnosu na referencu. dBi poredi antenu s idealnom antenom koja
emituje jednako u svim pravcima. dBd je poredi s polutalasnim dipolom, koji i sam
ima 2.15 dBi: čak ni najjednostavnija antena ne emituje ništa pravo gore ili dole.
Duži dipol, od 1.25 talasne dužine, dostiže 5.2 dBi. Kolinearna antena umesto toga
slaže polutalasne elemente jedan iznad drugog: što ih više složi, to je dobitak veći.
Sabij isti signal u upola manji prostor i tamo će biti dvaput jači: 3 dB. U četvrtinu
prostora, 4 puta jači: 6 dB. Proizvođači navode dobitak u dBi, a zakonska granica se
računa u dBd, pogledaj [U okviru zakonske granice](#legal).

### Koji dobitak za tvoju lokaciju {#choose-gain}

- **Brda, doline ili gust grad: oko 3 dBi.** Visok snop doseže čvorove iznad i ispod
  tebe, kao i one iza padina i zgrada na putu. Važi i obrnuto: iz doline ravan snop
  prolazi ispod repetitora na brdu iznad tebe. Jedna takva antena je RAKwireless
  RAKARG12, cev od fiberglasa duga 36 cm.
- **Predgrađa ili grad s niskim krovovima: 5 do 6 dBi.** Standardna kolinearna antena
  od fiberglasa.
- **Ravan, otvoren teren: 8 do 10 dBi.** Najravniji snop dobacuje najdalje duž
  horizonta. Ako je antena postavljena visoko, snop prolazi iznad obližnjih čvorova.

Dobitak u nazivu je najbolja vrednost u celom opsegu antene. RAKARG12 se prodaje kao
antena od 3 dBi, a na 865 do 870 MHz ima 2.8 dBi. U datasheetu pročitaj tabelu
dobitka na frekvenciji svog preseta.

Iznad 7 dBi ploča od 22 dBm prelazi zakonsku granicu, osim ako gubici u kablu i
filteru ne nadoknade razliku. Smanji snagu emitovanja koliko treba.

Veliki dobitak pomaže samo kad znaš gde su čvorovi: duž horizonta oko repetitora ili
kod jednog dalekog repetitora, ako imaš Yagi. Companion u ruci okrenut je na sve
strane, pa mu najbolje odgovara mali dobitak antene s kojom je stigao.

## Zašto vertikalno {#vertical}

Antene se najbolje čuju kad su okrenute na istu stranu. Gubitak raste s uglom između
njih: na 45 stepeni gubiš 3 dB, odnosno pola signala. Na 90 stepeni, kad je jedna antena
položena, a druga uspravna, u teoriji ne stiže ništa. Antene u mreži stoje uspravno, pa
neka i tvoja stoji tako. To važi i za companion na stolu: ako ga položiš, svaki
čvor oko tebe čuje manje.

## Konektori {#connectors}

Naruči antenu s konektorom koji tvoja ploča ima. Svaki adapter je još jedan spoj koji
moraš da zaptiješ i još malo izgubljenog signala.

- **SMA.** Konektor s navojem, širok oko 6 mm. Utičnica na većini ploča ima rupu u
  sredini, a antena ima pin. Gubitak ovakvog konektora je oko 0.03 dB na 868 MHz.
- **RP-SMA.** Isto kućište i navoj kao SMA, ali su pin i rupa zamenili mesta. Izgleda
  kao SMA, a ne može da se spoji s njim. Pre naručivanja proveri koji konektor ima
  tvoja ploča.
- **U.FL (IPEX).** Sićušna utična priključnica na samoj ploči. Kratak pigtail kabl
  vodi od nje do SMA utičnice na kućištu. Predviđena je za 30 spajanja, zato je spoji
  jednom i ne diraj je više.
- **N.** Veliki konektor s navojem na antenama od fiberglasa i debelom kablu. Gubitak
  mu je najviše 0.05 dB. Za repetitor ti treba jedan adapter ili pigtail kabl od N do SMA
  konektora na ploči.

## Gubici u kablu {#cable}

Kabl troši signal pre nego što signal napusti antenu, i to u oba smera. 3 dB je pola
tvoje snage. Podaci proizvođača po metru, na 868 do 900 MHz:

| Kabl | Gubitak po metru | Gubitak na 5 m |
|---|---|---|
| RG174 | 1.02 dB | 5.1 dB |
| RG316 | 0.78 dB | 3.9 dB |
| RG58 | 0.45 dB | 2.2 dB |
| H-155 | 0.27 dB | 1.4 dB |
| LMR-240 | 0.25 dB | 1.2 dB |
| Ecoflex 10 | 0.13 dB | 0.7 dB |
| LMR-400 | 0.13 dB | 0.6 dB |

Na 3 metra kabla RG174, tankog pigtail kabla koji se isporučuje uz mnoge ploče, gubiš
pola snage. Postavi ploču uz antenu s kratkim pigtail kablom ili do antene povuci debeo
kabl. U zbir dodaj svaki adapter i filter na putu signala.

## Filteri {#filters}

Filter se nalazi između radija i antene. Propušta tvoj opseg i blokira ostalo, pa jak
predajnik u blizini ne zaguši prijemnik. Treba ti kad čvor u blizini drugih predajnika
čuje manje nego što bi trebalo. Takav čvor je repetitor na jarbolu s baznim stanicama
mobilne telefonije. Filter troši signal u oba smera: njegov gubitak računaj kao gubitak
u kablu.

| | SAW filter | Kavitetni filter |
|---|---|---|
| Veličina | Nekoliko milimetara, na maloj ploči | Metalni blok ili cev |
| Gubitak dobrog filtera | ispod 2 dB | ispod 1 dB |
| Maksimalna ulazna snaga dobrog filtera | 500 mW | nekoliko vati |

Na primer, sysmocom cf866.5-kt30 je kavitetni filter za 863 do 870 MHz koji gubi najviše
1.0 dB i podnosi 30 W. Napravljen je za zatvoren prostor, zato ga na jarbolu stavi u
zaptivenu kutiju.

Filteri se dosta razlikuju, zato pre kupovine proveri datasheet. Nazivna ulazna snaga
mora biti veća od tvoje snage emitovanja, a propusni opseg mora da obuhvata frekvenciju
tvog preseta.

## Montaža {#mounting}

- **Iznad ivice krova.** Antena mora imati slobodan vidik u svim pravcima koje pokriva. Čak
  i nekoliko metara iznad okolnih krovova pomaže. U vodiču za repetitore, odeljak
  [Izaberi lokaciju](/repeater-guide/#site) objašnjava kako da proveriš vidik.
- **Dalje od metala.** Oluci, jarboli, druge antene i metalni krovovi pored antene menjaju
  njen dijagram zračenja i podešenost. Postavi je na vrh jarbola, a ne pored njega.
- **Uspravno.** Koristi libelu, pogledaj [Zašto vertikalno](#vertical).
- **Petlja za kapanje.** Pusti da kabl visi ispod konektora pre nego što krene nagore ili
  unutra. Voda tada kaplje s kabla i ne sliva se u spoj.
- **Zaptij svaki spoljni konektor.** Voda u konektoru povećava gubitak i nagriza pin.
  Zaštiti ga od kiše i svake godine proveri zaptivku.
- **Grom.** Antena na krovu je meta. Gasni odvodnik u kablu reaguje na prenapon
  i odvodi ga u uzemljenje. Za uzemljenje prati odeljak [Hardver](/repeater-guide/#hardware)
  u vodiču za repetitore i lokalne propise.

## U okviru zakonske granice {#legal}

{{< callout type="legal" verified="2026-10-22" >}}
U Evropi MeshCore koristi podopseg 869.40-869.65 MHz, s najviše **500 mW** efektivne
izračene snage (e.r.p.). Granica se odnosi na ono što napušta antenu: dobitak antene se
dodaje, a gubici u kablu i filteru se oduzimaju. Dobitak u dBi računa se kao 2.15 dB manji,
jer se granica meri u odnosu na dipol.
{{< /callout >}}

Kolinearna antena od 5.8 dBi na ploči od 22 dBm ostaje u okviru granice. Ista antena na
ploči s pojačavačem prelazi granicu dok ne smanjiš snagu emitovanja. Računicu i 2 urađena
primera naći ćeš u vodiču za repetitore, u odeljku
[Snaga: e.r.p. i tvoja antena](/repeater-guide/#erp).

## Proveri antenu NanoVNA uređajem {#nanovna}

NanoVNA je vektorski analizator mreže džepne veličine. Pokazuje na koju je frekvenciju
antena podešena, pa to znaš pre montaže. NanoVNA-H meri do 1.5 GHz, što obuhvata 868 MHz.

1. Kalibriši ga za 800 do 950 MHz pomoću delova open, short i load iz kompleta.
2. Poveži antenu preko adaptera koji će koristiti na čvoru. Drži je uspravno, dalje od
   tela i stola.
3. Očitaj SWR krivu (standing wave ratio, odnos stojećih talasa): ona pokazuje koliko
   signala antena vraća nazad. Udubljenje mora biti na frekvenciji tvog preseta, 869.618
   MHz za EU/UK (Narrow). Udubljenje stotinama MHz dalje znači da je antena napravljena
   za drugi opseg.

Četvrtina talasa na 868 MHz iznosi 86 mm (talasna dužina je 345 mm). Sama dužina ne otkriva
opseg, jer proizvođači savijaju i opterećuju štapaste antene. NanoVNA ga otkriva.

## Izvori {#sources}

- Gubici u kablu: [Belden 8216 (RG174)](https://catalog.belden.com/techdata/en/8216_techdata.pdf),
  Huber+Suhner RG316 datasheet,
  [Belden 8240 (RG58)](https://catalog.belden.com/techdata/en/8240_techdata.pdf),
  [SSB H-155](https://www.ssb.de/media/h155ssb-en.pdf),
  Times Microwave LMR-240 i LMR-400 datasheetovi,
  [SSB Ecoflex 10](https://www.rigpix.com/otherusefulinfo/coax/ecoflex10.pdf).
- Antene: [Sirio SPO 868-915-6](https://rigpix.com/antennas/sirio_spo8689156_manual.pdf),
  Sirio SO 868-915-2 datasheet,
  [Amphenol Procom 7176870](https://amphenolprocom.com/products/base-station-antennas/2236-7176870),
  [RAKwireless RAKARG12](https://docs.rakwireless.com/product-categories/accessories/rakarg12/datasheet/).
- Dobitak kao signal sabijen u manji prostor: [RF Cafe, uvod u antene](https://www.rfcafe.com/references/electrical/ew-radar-handbook/antenna-introduction-basics.htm).
- Konektori: Rosenberger 32S102 (SMA) i 53S101 (N) datasheetovi, Hirose U.FL katalog.
- Filteri: stranica proizvoda sysmocom cf866.5-kt30,
  [Citel gasni odvodnici prenapona](https://citel.us/en/gas-tube-surge-arrestors-for-coaxial-line-protection).
- Gubitak zbog polarizacije: [Univerzitet u Torontu, Friis efekti](https://www.waves.utoronto.ca/prof/svhum/ece422/notes/12-friiseffects.pdf).
- Dobitak dipola prema dužini: [Wikipedia, dipol antena](https://en.wikipedia.org/wiki/Dipole_antenna).
- Talasna dužina: brzina svetlosti prema [NIST](https://physics.nist.gov/cgi-bin/cuu/Value?c).
- NanoVNA: [NanoVNA-H](https://github.com/hugen79/NanoVNA-H).
- Zakonska granica: [CEPT ERC preporuka 70-03](https://docdb.cept.org/document/845),
  Aneks 1, opseg h1.7. Ostale izvore navodi [vodič za repetitore](/repeater-guide/#legal).
