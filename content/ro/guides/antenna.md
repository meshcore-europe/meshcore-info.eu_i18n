---
title: Ghid de antene
lead: O antenă potrivită, montată bine, ajunge mai departe decât mai multă putere. Verifică antena de pe companionul tău, apoi alege, conectează și montează una pentru un repetor.
description: 'Alege și montează o antenă MeshCore pentru 868 MHz: verificarea antenei whip a unui companion, tipuri de antene și câștig, conectori, pierderi în cablu pe metru, filtre, montare și cum intră câștigul în limita legală.'
eyebrow: Companion și repetor · 868 MHz
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'f828c4aa'
  seeded: '2026-10-31'
  fields: {title: '3a76cb0e', lead: 'd82ec429', description: 'ce3f3e73', eyebrow: 'd2203a35'}
  sections: ['908e2678', 'f9b96f42', 'ca18da90', 'bcfb40ec', '851afd23', '8b7a2209', 'd8832cfa', '5b70b9e8', '14a38e92', 'a5dc1e34', 'de04ca41', 'a23f19c6', '93846db4']
  blocks: ['908e2678', '0868bca9', '081db416', 'ad1da217', '73844333', 'aa14f1b1', '07e4fbad', '32d64d0d', 'ef66133c', '558c115b', '5d28e314', '57d6e138', 'e9b3d055', 'dd757d4a', '2cbd0b58', '21c67ec0', '306a3ded', 'fa46c89f', '1e6ccb3a', 'a3e53320', '6ae131c0', '98f350c6', '138d049d', '3bd28746', '2fc98ff1', '5ea29ee5', 'cfbd64e1', '48833347', '56a82a5c', '4ef7e883', '711e4fee', '1f7844ed', '6b188411', '8da9aa78', '4c2d8bbc', 'a721a9d0', '69c1dc1a', 'a631dbfa', '3f9f3471', '5af4ae3b', 'fa5095fd', '65eeb436', '15aa0eca', 'a8f5b505', '57f35115', '8e5e4975', '89764d3d']
---

Înălțimea, o antenă acordată și un cablu scurt îți aduc o rază mai mare
decât orice miliwatt în plus. Ghidul începe cu companionul, radioul de pe
care trimiți mesaje. Apoi trece la antena unui repetor, un nod care
transmite mai departe mesajele de pe un acoperiș sau un catarg.

## Companionul tău {#companion}

{{< callout type="warning" >}}
Montează antena înainte să pornești radioul. Un radio LoRa care
transmite fără antenă își poate distruge propriul cip.
{{< /callout >}}

Antena primită cu placa e suficientă. Montează-o, ține nodul vertical și
începe să trimiți mesaje. O antenă mai bună pe un companion aduce puțin;
un repetor în rază aduce mult.

Cumpără o antenă whip separată doar dacă cea primită e stricată sau
lipsește. Nu orice whip vândut pentru 868 MHz e acordat pe această
frecvență. [Verifică-l cu un NanoVNA](#nanovna), un analizor de antene de
buzunar, înainte să te bazezi pe el. Sau împrumută antena unei plăci care
funcționează.

Un nod aflat lângă un emițător puternic aude mai puțin decât ar trebui. Un
mic [filtru SAW (cu undă acustică de suprafață)](#filters) între radio și
antenă ține acel emițător departe de receptor. Citește întâi fișa lui
tehnică:

- **Puterea maximă de intrare.** Filtrul stă și în calea propriei tale
  transmisii. O placă ce transmite 22 dBm (160 mW) într-un filtru
  specificat pentru 15 dBm distruge filtrul.
- **Banda de trecere.** Trebuie să includă frecvența presetării tale. Un
  filtru pentru 868.65-869.25 MHz nu lasă să treacă canalul EU/UK
  (Narrow) de pe 869.618 MHz.

## Tipuri de antene pentru un repetor {#types}

Toate antenele din mesh stau vertical. Alege tipul după locul în care se
află nodurile pe care vrei să le atingi:

- **Colineară din fibră de sticlă.** Un tub alb pe catarg, cu câștig pe
  tot orizontul. Alegerea standard pentru un repetor care deservește un
  oraș.
- **Dipol.** Mai scurt, cu câștig mai mic și un fascicul înalt. Atinge mai
  bine decât o colineară nodurile de sub și de deasupra ta, de exemplu de
  pe un deal deasupra unei văi.
- **Yagi.** O bară cu elemente transversale, îndreptată spre un singur
  loc. Atinge un singur repetor îndepărtat și aproape nimic altceva.
  Montează-o cu elementele în poziție verticală, pentru că polarizarea ei
  urmează elementele.

## Câștigul și fasciculul {#gain}

Câștigul nu adaugă putere. Ia semnalul care ar pleca în sus și în jos
și îl trimite de-a lungul orizontului. E ca o lanternă pe care o
focalizezi: aceeași baterie, un fascicul mai lung și mai îngust. Un dipol
și o colineară de la același producător arată asta:

| Antenă | Câștig | Lățimea verticală a fasciculului |
|---|---|---|
| Dipol (Sirio SO 868-915-2) | 2.2 dBi | 88 de grade |
| Colineară din fibră de sticlă (Sirio SPO 868-915-6) | 5.8 dBi | 23 de grade |

{{< gain >}}

Diagrama e o secțiune prin catarg, văzută din lateral. Rotește-o în jurul
catargului și obții tot fasciculul: o gogoașă pentru dipol, un disc plat
pentru colineară. O antenă verticală emite la fel în toate direcțiile din
jurul ei. În afara fasciculului desenat, semnalul nu dispare; e mai slab,
dar ajunge pentru un nod din apropiere.

Pe un acoperiș, ai nevoie de un fascicul plat. Pe un deal mult deasupra
nodurilor, un fascicul de 23 de grade trece pe deasupra lor; un dipol le
acoperă. O Yagi duce asta mai departe: 16.6 dBi într-un fascicul înalt de
23 de grade și lat de 25 de grade (Amphenol Procom 7176870), și nimic în
lateral.

Câștigul se măsoară față de o referință. dBi compară cu o antenă ideală
care emite egal în toate direcțiile. dBd compară cu un dipol în semiundă,
care are el însuși 2.15 dBi: nici cea mai simplă antenă nu emite nimic
direct în sus sau în jos. Un dipol mai lung, de 1.25 lungimi de undă,
ajunge la 5.2 dBi. O colineară, în schimb, așază elemente în semiundă unul
peste altul: cu cât are mai multe, cu atât câștigul e mai mare. Strânge
același semnal în jumătate din spațiu și acolo e de două ori mai puternic: 3
dB. Într-un sfert, de 4 ori mai puternic: 6 dB. Producătorii dau câștigul
în dBi; limita legală se calculează în dBd, vezi
[În limita legală](#legal).

### Ce câștig se potrivește locului tău {#choose-gain}

- **Dealuri, văi sau un oraș dens: circa 3 dBi.** Fasciculul înalt atinge
  nodurile de deasupra și de sub tine, și ocolește pantele și clădirile din
  cale. Funcționează și invers: dintr-o vale, un fascicul plat trece pe sub
  un repetor de pe dealul de deasupra. RAKwireless RAKARG12 e un exemplu:
  un tub din fibră de sticlă de 36 cm.
- **Suburbii sau un oraș cu acoperișuri joase: 5-6 dBi.** Colineara
  standard din fibră de sticlă.
- **Teren plat și deschis: 8-10 dBi.** Cel mai plat fascicul ajunge cel
  mai departe de-a lungul orizontului. Montat sus, trece pe deasupra
  nodurilor din apropiere.

Câștigul din denumire e cea mai bună valoare din toată banda antenei.
RAKARG12, vândută ca 3 dBi, are 2.8 dBi la 865-870 MHz. Citește tabelul
de câștig din fișa tehnică la frecvența presetării tale.

Peste 7 dBi, o placă de 22 dBm depășește limita legală, dacă pierderile
din cablu și filtru nu compensează diferența. Scade puterea de transmisie
pe măsură.

Câștigul mare ajută doar când știi unde sunt nodurile: de-a lungul
orizontului în jurul unui repetor sau, la o Yagi, la un repetor
îndepărtat. Un companion ținut în mână e orientat în toate direcțiile, așa
că i se potrivește cel mai bine câștigul mic cu care a venit.

## De ce vertical {#vertical}

Antenele se aud cel mai bine când sunt orientate la fel. Pierderea crește
cu unghiul dintre ele: 45 de grade costă 3 dB, adică jumătate din semnal.
La 90 de grade, o antenă culcată față de una verticală, teoretic nu ajunge
nimic. Mesh-ul stă vertical, deci și antena ta. Asta e valabil și pentru
un companion pe birou: dacă îl culci, toate nodurile din jur te aud mai
slab.

## Conectori {#connectors}

Comandă antena cu conectorul pe care îl are placa ta. Fiecare adaptor e
încă o îmbinare de etanșat și mai mult semnal pierdut.

- **SMA.** Un conector cu filet, lat de circa 6 mm. Mufa de pe majoritatea
  plăcilor are o gaură în centru; antena are pinul. Un conector de acest
  tip pierde circa 0.03 dB la 868 MHz.
- **RP-SMA.** Același corp și filet ca SMA, dar cu pinul și gaura
  inversate. Arată ca SMA, dar nu se cuplează cu el. Verifică ce tip are
  placa ta înainte să comanzi.
- **U.FL (IPEX).** O mufă minusculă, cu cuplare prin apăsare, direct pe
  placă. Un cablu pigtail scurt duce de la ea la o mufă SMA în carcasă. E
  specificată pentru 30 de cuplări, așa că o conectezi o dată și o lași
  așa.
- **N.** Conectorul mare cu filet de pe antenele din fibră de sticlă și de
  pe cablul gros. Pierde cel mult 0.05 dB. Un repetor are nevoie de un
  adaptor sau pigtail de la N la mufa SMA a plăcii.

## Pierderi în cablu {#cable}

Cablul consumă semnal înainte ca acesta să plece din antenă, în ambele
direcții. 3 dB înseamnă jumătate din putere. Valorile producătorilor pe
metru, la 868-900 MHz:

| Cablu | Pierdere pe metru | Pierdere pe 5 m |
|---|---|---|
| RG174 | 1.02 dB | 5.1 dB |
| RG316 | 0.78 dB | 3.9 dB |
| RG58 | 0.45 dB | 2.2 dB |
| H-155 | 0.27 dB | 1.4 dB |
| LMR-240 | 0.25 dB | 1.2 dB |
| Ecoflex 10 | 0.13 dB | 0.7 dB |
| LMR-400 | 0.13 dB | 0.6 dB |

3 metri de RG174, pigtail-ul subțire livrat cu multe plăci, îți înjumătățesc
puterea. Montează placa lângă antenă cu un pigtail scurt sau trage cablu
gros până la ea. Adaugă la total fiecare adaptor și filtru din cale.

## Filtre {#filters}

Un filtru stă între radio și antenă. Lasă să treacă banda ta și blochează
restul, ca un emițător puternic din apropiere să nu copleșească
receptorul. Ai nevoie de unul când un nod aude mai puțin decât ar trebui
lângă alți emițători. Un repetor pe un catarg cu stații de bază de
telefonie mobilă e un astfel de nod. Un filtru consumă semnal în ambele
direcții: socotește-i pierderea ca pe a unui cablu.

| | Filtru SAW | Filtru cu cavitate |
|---|---|---|
| Dimensiune | Câțiva milimetri, pe o plăcuță | Un bloc sau un tub de metal |
| Pierderea unuia bun | sub 2 dB | sub 1 dB |
| Puterea maximă de intrare a unuia bun | 500 mW | câțiva wați |

De exemplu, sysmocom cf866.5-kt30 e un filtru cu cavitate pentru
863-870 MHz, care pierde cel mult 1.0 dB și suportă 30 W. E făcut pentru
interior, așa că pe un catarg pune-l într-o cutie etanșă.

Filtrele diferă mult, așa că citește fișa tehnică înainte să cumperi.
Puterea de intrare specificată trebuie să depășească puterea ta de
transmisie, iar banda de trecere trebuie să includă frecvența presetării
tale.

## Montare {#mounting}

- **Deasupra marginii acoperișului.** Antena are nevoie de vedere liberă
  în fiecare direcție pe care o deservește. Chiar și câțiva metri peste
  acoperișurile din jur ajută. [Alege un amplasament](/repeater-guide/#site)
  din ghidul de repetoare arată cum verifici vederea.
- **Departe de metal.** Jgheaburile, catargele, alte antene și
  acoperișurile metalice de lângă antenă îi schimbă diagrama și acordul.
  Montează antena în vârful catargului, nu lângă el.
- **Vertical.** Folosește o nivelă cu bulă; vezi [De ce vertical](#vertical).
- **Bucla de scurgere.** Lasă cablul să atârne sub conector înainte să
  urce sau să intre în clădire. Astfel apa picură în loc să curgă în
  îmbinare.
- **Etanșează fiecare conector din exterior.** Apa dintr-un conector
  mărește pierderea și corodează pinul. Etanșează-l împotriva ploii și
  verifică etanșarea în fiecare an.
- **Fulgere.** O antenă pe acoperiș e o țintă. Un descărcător cu gaz pe
  cablu se declanșează la o supratensiune și o descarcă la pământ. Pentru
  împământare, urmează [Hardware](/repeater-guide/#hardware)
  din ghidul de repetoare și regulile locale.

## În limita legală {#legal}

{{< callout type="legal" verified="2026-10-22" >}}
În Europa, MeshCore folosește subbanda 869.40-869.65 MHz, cu cel mult
**500 mW** putere radiată efectivă (e.r.p.). Limita se aplică la ce iese
din antenă: câștigul antenei se adună, pierderile din cablu și filtru se
scad. Câștigul în dBi contează cu 2.15 dB mai puțin, pentru că limita se
măsoară față de un dipol.
{{< /callout >}}

O colineară de 5.8 dBi pe o placă de 22 dBm rămâne în limită. Aceeași
antenă pe o placă cu amplificator o depășește, până nu scazi puterea de
transmisie. [Putere: e.r.p. și antena ta](/repeater-guide/#erp) din ghidul
de repetoare are calculul și 2 exemple rezolvate.

## Verifică o antenă cu un NanoVNA {#nanovna}

Un NanoVNA este un analizor vectorial de rețea de buzunar. Îți arată pe ce
frecvență e acordată o antenă, așa că știi asta înainte s-o montezi.
NanoVNA-H măsoară până la 1.5 GHz, deci acoperă 868 MHz.

1. Calibrează-l pentru 800-950 MHz cu piesele open, short și load din
   kitul lui.
2. Conectează antena prin adaptorul pe care îl va folosi pe nod. Ține-o
   vertical, departe de corp și de masă.
3. Citește curba SWR (raportul de undă staționară): arată cât semnal
   trimite antena înapoi. Minimul trebuie să cadă pe frecvența presetării
   tale, 869.618 MHz pentru EU/UK (Narrow). Un minim aflat la sute de MHz
   distanță înseamnă că antena e făcută pentru altă bandă.

Un sfert de undă la 868 MHz are 86 mm (lungimea de undă e 345 mm).
Lungimea singură nu îți spune banda, pentru că producătorii pliază și
încarcă antenele whip; NanoVNA-ul îți spune.

## Surse {#sources}

- Pierderi în cablu: [Belden 8216 (RG174)](https://catalog.belden.com/techdata/en/8216_techdata.pdf),
  fișa tehnică Huber+Suhner RG316,
  [Belden 8240 (RG58)](https://catalog.belden.com/techdata/en/8240_techdata.pdf),
  [SSB H-155](https://www.ssb.de/media/h155ssb-en.pdf),
  fișele tehnice Times Microwave LMR-240 și LMR-400,
  [SSB Ecoflex 10](https://www.rigpix.com/otherusefulinfo/coax/ecoflex10.pdf).
- Antene: [Sirio SPO 868-915-6](https://rigpix.com/antennas/sirio_spo8689156_manual.pdf),
  fișa tehnică Sirio SO 868-915-2,
  [Amphenol Procom 7176870](https://amphenolprocom.com/products/base-station-antennas/2236-7176870),
  [RAKwireless RAKARG12](https://docs.rakwireless.com/product-categories/accessories/rakarg12/datasheet/).
- Câștigul ca semnal strâns în mai puțin spațiu: [RF Cafe, introducere în antene](https://www.rfcafe.com/references/electrical/ew-radar-handbook/antenna-introduction-basics.htm).
- Conectori: fișele tehnice Rosenberger 32S102 (SMA) și 53S101 (N),
  catalogul Hirose U.FL.
- Filtre: pagina de produs sysmocom cf866.5-kt30,
  [descărcătoarele cu gaz Citel](https://citel.us/en/gas-tube-surge-arrestors-for-coaxial-line-protection).
- Pierderi de polarizare: [University of Toronto, efecte Friis](https://www.waves.utoronto.ca/prof/svhum/ece422/notes/12-friiseffects.pdf).
- Câștigul dipolului în funcție de lungime: [Wikipedia, Dipole antenna](https://en.wikipedia.org/wiki/Dipole_antenna).
- Lungimea de undă: viteza luminii de la [NIST](https://physics.nist.gov/cgi-bin/cuu/Value?c).
- NanoVNA: [NanoVNA-H](https://github.com/hugen79/NanoVNA-H).
- Limita legală: [CEPT ERC Recommendation 70-03](https://docdb.cept.org/document/845),
  Anexa 1, banda h1.7; [ghidul de repetoare](/repeater-guide/#legal) le
  enumeră pe celelalte.
