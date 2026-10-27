---
title: Ghid pentru antene
lead: Antena este jumătate din nodul tău. Una potrivită, montată bine, ajunge mai departe decât mai multă putere. Verifică antena de pe companionul tău, apoi alege, conectează și montează una pentru un repetor.
description: 'Alege și montează o antenă MeshCore pentru 868 MHz: verifică antena-baston a unui companion, tipuri de antene și câștig, conectori, pierderea pe cablu per metru, filtre, montaj și cum intră câștigul în limita legală.'
eyebrow: Companion și repetor · 868 MHz
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '45010ad0'
  seeded: '2026-10-26'
  fields: {title: '3a76cb0e', lead: '98430ade', description: 'ce3f3e73', eyebrow: 'd2203a35'}
  sections: ['908e2678', 'f9b96f42', '94c5bae4', 'bcfb40ec', '851afd23', '8b7a2209', 'd8832cfa', '5b70b9e8', '14a38e92', 'a5dc1e34', 'de04ca41', 'a23f19c6', '93846db4']
---

Înălțimea, o antenă acordată și un cablu scurt aduc mai multă rază de acțiune decât orice miliwatt în plus. Ghidul începe cu companionul, radioul de pe care scrii mesaje. Apoi trece la antena unui repetor, un nod care transmite mesajele mai departe de pe un acoperiș sau un catarg.

## Companionul tău {#companion}

{{< callout type="warning" >}}
Montează antena înainte să pornești radioul. Un radio LoRa care
transmite fără antenă își poate distruge propriul cip.
{{< /callout >}}

Antena livrată cu placa ta își face treaba. Montează-o, ține nodul
drept și începe să scrii mesaje. O antenă mai bună pe un companion
câștigă puțin; un repetor în raza de acțiune câștigă mult.

Cumpără o antenă tip bici separată doar dacă cea livrată e ruptă sau lipsește. Nu
orice antenă bici vândută pentru 868 MHz e acordată pentru această frecvență. [Verific-o cu un
NanoVNA](#nanovna), un analizor de antenă de buzunar, înainte să ai încredere în ea, sau împrumută una de la o placă care
funcționează.

Un nod aflat lângă un emițător puternic aude mai puțin decât ar trebui. Un mic
[filtru SAW (cu unde acustice de suprafață)](#filters) între radio și
antenă ține acel emițător departe de receptor. Verifică mai întâi fișa
tehnică:

- **Puterea maximă de intrare.** Filtrul stă și în calea propriei tale
  transmisii. O placă ce transmite 22 dBm (160 mW) într-un filtru prevăzut pentru 15 dBm
  strică filtrul.
- **Banda de trecere.** Trebuie să includă frecvența presetării tale. Un filtru pentru
  868.65 până la 869.25 MHz nu lasă să treacă canalul EU/UK (Narrow) de pe
  869.618 MHz.

## Tipuri de antene pentru un repetor {#types}

Fiecare antenă din mesh stă vertical. Alege tipul după locul unde se află nodurile pe care vrei să le atingi:

- **Colineară din fibră de sticlă.** Un tub alb pe un catarg, cu câștig în toate direcțiile de-a lungul orizontului. Alegerea standard pentru un repetor care deservește un oraș.
- **Dipol.** Mai scurt, cu câștig mai mic și un fascicul înalt. Ajunge mai bine decât o colineară la nodurile de sub tine și de deasupra ta. Asta contează pe un deal deasupra unei văi.
- **Yagi.** O bară cu elemente transversale, îndreptată spre un singur loc. Ajunge la un singur repetor îndepărtat și aproape la nimic altceva. Monteaz-o cu elementele pe verticală, pentru că polarizarea ei urmează elementele.

## Câștigul și fasciculul {#gain}

Câștigul nu adaugă putere. Ia semnalul care s-ar duce în sus și în jos și îl trimite de-a lungul orizontului. Ca o lanternă pe care o focalizezi: aceeași baterie, un fascicul mai lung și mai îngust. Un dipol și o colineară de la același producător arată asta:

| Antenă | Câștig | Deschidere verticală a fasciculului |
|---|---|---|
| Dipol (Sirio SO 868-915-2) | 2.2 dBi | 88 de grade |
| Colineară din fibră de sticlă (Sirio SPO 868-915-6) | 5.8 dBi | 23 de grade |

{{< gain >}}

Diagrama taie prin catarg, văzut din lateral. Rotește-o în jurul catargului și ai întregul fascicul: o gogoașă pentru dipol, un disc plat pentru colineară. O antenă verticală emite la fel în toate direcțiile din jurul ei. În afara fasciculului desenat semnalul nu se oprește; este mai slab, dar tot de ajuns pentru un nod din apropiere.

Pe un acoperiș, un fascicul plat este ce vrei. Pe un deal mult deasupra nodurilor, un fascicul de 23 de grade trece pe deasupra lor; un dipol le acoperă. O Yagi duce asta mai departe: 16.6 dBi într-un fascicul înalt de 23 de grade și lat de 25 de grade (Amphenol Procom 7176870), și nimic în lateral.

Câștigul se raportează la o referință. dBi compară cu o antenă ideală care emite la fel în toate direcțiile. dBd compară cu un dipol în semiundă, care are el însuși 2.15 dBi: nici cea mai simplă antenă nu emite nimic drept în sus sau în jos. Un dipol mai lung, de 1.25 lungimi de undă, ajunge la 5.2 dBi. O colineară pune în schimb elemente în semiundă unul deasupra altuia: cu cât pune mai multe, cu atât câștigul este mai mare. Înghesuie același semnal în jumătate din spațiu și acolo este de două ori mai puternic: 3 dB. Într-un sfert, de 4 ori mai puternic: 6 dB. Producătorii dau câștigul în dBi; limita legală se socotește în dBd, vezi [În limita legală](#legal).

### Ce câștig pentru locul tău {#choose-gain}

- **Dealuri, văi sau un oraș dens: în jur de 3 dBi.** Fasciculul înalt ajunge la
  nodurile de deasupra și de sub tine, și pe după pantele și clădirile din cale.
  Merge și invers: dintr-o vale, un fascicul plat trece pe sub un
  repetor de pe dealul de deasupra. RAKwireless RAKARG12 este una: un
  tub din fibră de sticlă de 36 cm.
- **Suburbii sau un oraș cu acoperișuri joase: 5 până la 6 dBi.** Colineara
  standard din fibră de sticlă.
- **Teren plat, deschis: 8 până la 10 dBi.** Cel mai plat fascicul ajunge cel mai departe
  de-a lungul orizontului. Montată sus, trece pe deasupra nodurilor din apropiere.

Câștigul din nume este cea mai bună valoare din întreaga bandă a antenei.
RAKARG12, vândută ca 3 dBi, are 2.8 dBi la 865 până la 870 MHz. Citește tabelul
de câștig din fișa tehnică la frecvența presetării tale.

Peste 7 dBi o placă de 22 dBm depășește limita legală, dacă pierderile din cablu și filtru
nu compensează diferența. Scade puterea de transmisie ca să te încadrezi.

Câștigul mare ajută doar când știi unde sunt nodurile: de-a lungul orizontului
în jurul unui repetor, sau la un singur repetor îndepărtat pentru o Yagi. Un companion din
mâna ta este îndreptat în toate direcțiile, așa că câștigul mic cu care a venit i se potrivește cel mai bine.

## De ce vertical {#vertical}

Antenele se aud cel mai bine când sunt orientate la fel. Pierderea crește cu unghiul dintre ele: 45 de grade costă 3 dB, jumătate din semnalul tău. La 90 de grade, o antenă culcată față de una verticală, în teorie nu ajunge nimic. Mesh-ul stă vertical, deci și antena ta stă la fel. Asta e valabil și pentru un companion pe birou: pune-l culcat și fiecare nod din jurul tău aude mai puțin.

## Conectori {#connectors}

Comandă antena cu conectorul pe care îl are placa ta. Fiecare adaptor este încă o îmbinare de etanșat și încă un pic de semnal pierdut.

- **SMA.** Un conector cu filet, lat de circa 6 mm. Mufa de pe majoritatea plăcilor are o gaură în centru; antena are pinul. Un conector de acest fel pierde circa 0.03 dB la 868 MHz.
- **RP-SMA.** Același corp și același filet ca SMA, cu pinul și gaura inversate. Arată ca SMA și nu se potrivește cu el. Verifică pe care îl are placa ta înainte să comanzi.
- **U.FL (IPEX).** O mufă minusculă cu apăsare, direct pe placă. De la ea pleacă un cablu scurt (pigtail) spre o mufă SMA din carcasă. Este proiectată pentru 30 de cuplări, așa că o conectezi o dată și o lași așa.
- **N.** Conectorul mare cu filet de pe antenele din fibră de sticlă și cablurile groase. Pierde cel mult 0.05 dB. Un repetor are nevoie de un adaptor sau un pigtail de la N la SMA-ul plăcii.

## Pierderea în cablu {#cable}

Cablul consumă semnal înainte ca acesta să părăsească antena, în ambele direcții. 3 dB
înseamnă jumătate din puterea ta. Valorile producătorilor pe metru, la 868 până la 900 MHz:

| Cablu | Pierdere pe metru | Pierdere pe 5 m |
|---|---|---|
| RG174 | 1.02 dB | 5.1 dB |
| RG316 | 0.78 dB | 3.9 dB |
| RG58 | 0.45 dB | 2.2 dB |
| H-155 | 0.27 dB | 1.4 dB |
| LMR-240 | 0.25 dB | 1.2 dB |
| Ecoflex 10 | 0.13 dB | 0.7 dB |
| LMR-400 | 0.13 dB | 0.6 dB |

3 metri de RG174, pigtail-ul subțire livrat cu multe plăci, pierd jumătate
din puterea ta. Montează placa lângă antenă cu un pigtail scurt, sau
trage un cablu gros până la ea. Adaugă la sumă fiecare adaptor și filtru de pe traseu.

## Filtre {#filters}

Un filtru stă între radio și antenă. Lasă să treacă banda ta și
blochează restul, ca un emițător puternic din apropiere să nu sufoce
receptorul. Ai nevoie de unul când un nod aude mai puțin decât ar trebui lângă alte
emițătoare. Un repetor pe un catarg cu stații de bază de telefonie mobilă este un astfel
de nod. Un filtru costă semnal în ambele direcții: socotește-i pierderea ca pe cea din
cablu.

| | Filtru SAW | Filtru cu cavități |
|---|---|---|
| Mărime | Câțiva milimetri, pe o plăcuță mică | Un bloc sau un tub de metal |
| Pierderea unuia bun | sub 2 dB | sub 1 dB |
| Puterea maximă de intrare a unuia bun | 500 mW | câțiva wați |

Sysmocom cf866.5-kt30, de exemplu, este un filtru cu cavități pentru 863 până la
870 MHz care pierde cel mult 1.0 dB și suportă 30 W. Este făcut pentru interior,
așa că pune-l într-o cutie etanșă pe catarg.

Filtrele diferă mult, așa că verifică fișa tehnică înainte să cumperi. Puterea
de intrare nominală trebuie să depășească puterea ta de transmisie, iar banda de trecere trebuie să includă
frecvența presetării tale.

## Montaj {#mounting}

- **Deasupra marginii acoperișului.** Antena are nevoie de vedere liberă în fiecare direcție pe care o deservește. Chiar și câțiva metri deasupra acoperișurilor din jur ajută. [Alege un amplasament](/repeater-guide/#site) din ghidul pentru repetoare arată cum verifici vederea.
- **Departe de metal.** Jgheaburile, catargele, alte antene și acoperișurile de metal de lângă antenă îi schimbă diagrama și acordul. Monteaz-o în vârful catargului, nu lângă el.
- **Vertical.** Folosește o nivelă cu bulă; vezi [De ce vertical](#vertical).
- **Buclă de scurgere.** Lasă cablul să atârne sub conector înainte să urce sau să intre. Apa picură astfel jos în loc să curgă în îmbinare.
- **Etanșează fiecare conector de exterior.** Apa dintr-un conector crește pierderea și corodează pinul. Etanșează-l împotriva ploii și verifică etanșarea în fiecare an.
- **Trăsnet.** O antenă pe acoperiș este o țintă. Un descărcător cu gaz montat pe cablu se declanșează la o supratensiune și o trimite la pământ. Urmează [Hardware](/repeater-guide/#hardware) din ghidul pentru repetoare și regulile locale pentru împământare.

## În limita legală {#legal}

{{< callout type="legal" verified="2026-10-22" >}}
În Europa MeshCore folosește subbanda 869.40-869.65 MHz, cu cel mult
**500 mW** putere efectivă radiată (e.r.p.). Limita socotește ce părăsește antena:
câștigul antenei se adună, pierderile din cablu și filtru se scad. Câștigul în dBi contează
cu 2.15 dB mai puțin, pentru că limita se măsoară față de un dipol.
{{< /callout >}}

O colineară de 5.8 dBi pe o placă de 22 dBm rămâne în limită. Aceeași
antenă pe o placă cu amplificator nu rămâne, până nu scazi puterea
de transmisie. [Puterea: e.r.p. și antena ta](/repeater-guide/#erp) din
ghidul pentru repetoare are calculul și 2 exemple rezolvate.

## Verifică o antenă cu un NanoVNA {#nanovna}

Un NanoVNA este un analizor vectorial de rețea de buzunar. Arată pe ce
frecvență este acordată o antenă, așa că știi înainte să o montezi.
NanoVNA-H măsoară până la 1.5 GHz, ceea ce acoperă 868 MHz.

1. Calibrează-l pentru 800 până la 950 MHz cu piesele open, short și load
   din kitul lui.
2. Conectează antena prin adaptorul pe care îl va folosi pe nod. Ține-o
   drept și departe de corpul tău și de masă.
3. Citește curba SWR (raportul de unde staționare): arată cât semnal
   trimite antena înapoi. Minimul trebuie să stea pe frecvența presetării tale, 869.618
   MHz pentru EU/UK (Narrow). Un minim la sute de MHz distanță înseamnă că antena este
   făcută pentru altă bandă.

Un sfert de undă la 868 MHz are 86 mm (lungimea de undă este 345 mm). Lungimea
singură nu îți spune banda, pentru că producătorii pliază și încarcă antenele bici;
NanoVNA o face.

## Surse {#sources}

- Pierderea pe cablu: [Belden 8216 (RG174)](https://catalog.belden.com/techdata/en/8216_techdata.pdf),
  fișa tehnică Huber+Suhner RG316,
  [Belden 8240 (RG58)](https://catalog.belden.com/techdata/en/8240_techdata.pdf),
  [SSB H-155](https://www.ssb.de/media/h155ssb-en.pdf),
  fișele tehnice Times Microwave LMR-240 și LMR-400,
  [SSB Ecoflex 10](https://www.rigpix.com/otherusefulinfo/coax/ecoflex10.pdf).
- Antene: [Sirio SPO 868-915-6](https://rigpix.com/antennas/sirio_spo8689156_manual.pdf),
  fișa tehnică Sirio SO 868-915-2,
  [Amphenol Procom 7176870](https://amphenolprocom.com/products/base-station-antennas/2236-7176870),
  [RAKwireless RAKARG12](https://docs.rakwireless.com/product-categories/accessories/rakarg12/datasheet/).
- Câștigul ca semnal înghesuit în mai puțin spațiu: [RF Cafe, introducere în antene](https://www.rfcafe.com/references/electrical/ew-radar-handbook/antenna-introduction-basics.htm).
- Conectori: fișele tehnice Rosenberger 32S102 (SMA) și 53S101 (N), catalogul Hirose U.FL.
- Filtre: pagina produsului sysmocom cf866.5-kt30,
  [descărcătoare cu gaz Citel](https://citel.us/en/gas-tube-surge-arrestors-for-coaxial-line-protection).
- Pierderea prin polarizare: [Universitatea din Toronto, efectele Friis](https://www.waves.utoronto.ca/prof/svhum/ece422/notes/12-friiseffects.pdf).
- Câștigul dipolului după lungime: [Wikipedia, Dipole antenna](https://en.wikipedia.org/wiki/Dipole_antenna).
- Lungimea de undă: viteza luminii de la [NIST](https://physics.nist.gov/cgi-bin/cuu/Value?c).
- NanoVNA: [NanoVNA-H](https://github.com/hugen79/NanoVNA-H).
- Limita legală: [Recomandarea CEPT ERC 70-03](https://docdb.cept.org/document/845),
  Anexa 1, banda h1.7; [ghidul pentru repetoare](/repeater-guide/#legal) le enumeră pe celelalte.
