---
title: Guida alle antenne
lead: Un'antenna giusta, montata bene, arriva più lontano di una potenza maggiore. Controlla l'antenna del tuo companion, poi scegli, collega e monta quella per un ripetitore.
description: 'Scegli e monta un''antenna MeshCore per 868 MHz: controllo dello stilo di un companion, tipi di antenna e guadagno, connettori, perdita del cavo per metro, filtri, montaggio e come il guadagno conta per il limite di legge.'
eyebrow: Companion e ripetitore · 868 MHz
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'f828c4aa'
  seeded: '2026-10-31'
  fields: {title: '3a76cb0e', lead: 'd82ec429', description: 'ce3f3e73', eyebrow: 'd2203a35'}
  sections: ['908e2678', 'f9b96f42', 'ca18da90', 'bcfb40ec', '851afd23', '8b7a2209', 'd8832cfa', '5b70b9e8', '14a38e92', 'a5dc1e34', 'de04ca41', 'a23f19c6', '93846db4']
  blocks: ['908e2678', '0868bca9', '081db416', 'ad1da217', '73844333', 'aa14f1b1', '07e4fbad', '32d64d0d', 'ef66133c', '558c115b', '5d28e314', '57d6e138', 'e9b3d055', 'dd757d4a', '2cbd0b58', '21c67ec0', '306a3ded', 'fa46c89f', '1e6ccb3a', 'a3e53320', '6ae131c0', '98f350c6', '138d049d', '3bd28746', '2fc98ff1', '5ea29ee5', 'cfbd64e1', '48833347', '56a82a5c', '4ef7e883', '711e4fee', '1f7844ed', '6b188411', '8da9aa78', '4c2d8bbc', 'a721a9d0', '69c1dc1a', 'a631dbfa', '3f9f3471', '5af4ae3b', 'fa5095fd', '65eeb436', '15aa0eca', 'a8f5b505', '57f35115', '8e5e4975', '89764d3d']
---

L'altezza, un'antenna accordata e un cavo corto danno più portata di qualsiasi
milliwatt in più. Questa guida parte dal companion, la radio da cui invii
i messaggi. Poi passa all'antenna di un ripetitore, un nodo che inoltra
i messaggi da un tetto o da un palo.

## Il tuo companion {#companion}

{{< callout type="warning" >}}
Collega l'antenna prima di accendere la radio. Una radio LoRa che
trasmette senza antenna può danneggiare il proprio chip.
{{< /callout >}}

L'antenna fornita con la scheda fa il suo lavoro. Collegala, tieni il
nodo in verticale e inizia a scrivere. Un'antenna migliore
su un companion rende poco; un ripetitore a portata rende molto.

Compra uno stilo separato solo se quello fornito è rotto o manca. Non
tutti gli stili venduti per 868 MHz sono accordati su questa frequenza. [Controllalo con un
NanoVNA](#nanovna), un analizzatore d'antenna tascabile, prima di fidarti, oppure prendine in prestito uno da una scheda che
funziona.

Un nodo vicino a un trasmettitore potente sente meno del dovuto. Un piccolo
[filtro SAW (surface acoustic wave, a onde acustiche di superficie)](#filters) tra la radio e
l'antenna impedisce a quel trasmettitore di entrare nel ricevitore. Prima controlla il suo datasheet:

- **Potenza massima in ingresso.** Il filtro sta anche sul percorso della tua
  trasmissione. Una scheda che trasmette 22 dBm (160 mW) in un filtro da 15 dBm
  rompe il filtro.
- **Banda passante.** Deve includere la frequenza del tuo preset. Un filtro per
  868.65-869.25 MHz non lascia passare il canale EU/UK (Narrow) a
  869.618 MHz.

## Tipi di antenna per un ripetitore {#types}

Tutte le antenne della mesh stanno in verticale. Scegli il tipo in base a dove si trovano
i nodi che vuoi raggiungere:

- **Collineare in vetroresina.** Un tubo bianco su un palo, con guadagno su tutto
  l'orizzonte. È la scelta standard per un ripetitore che copre una città.
- **Dipolo.** Più corto, con meno guadagno e un fascio alto. Raggiunge meglio di una collineare
  i nodi sotto e sopra di te, per esempio da una collina
  sopra una valle.
- **Yagi.** Un'asta con elementi trasversali, puntata verso un solo punto. Raggiunge un
  singolo ripetitore lontano e poco altro. Montala con gli elementi in verticale,
  perché la sua polarizzazione segue gli elementi.

## Guadagno e fascio {#gain}

Il guadagno non aggiunge potenza. Prende il segnale che andrebbe verso l'alto e verso il basso
e lo manda lungo l'orizzonte. Come una torcia che metti a fuoco: stessa batteria,
fascio più lungo e più stretto. Un dipolo e una collineare dello stesso produttore
lo dimostrano:

| Antenna | Guadagno | Apertura verticale del fascio |
|---|---|---|
| Dipolo (Sirio SO 868-915-2) | 2.2 dBi | 88 gradi |
| Collineare in vetroresina (Sirio SPO 868-915-6) | 5.8 dBi | 23 gradi |

{{< gain >}}

Il diagramma è una sezione attraverso il palo, vista di lato. Ruotalo attorno al
palo e ottieni il fascio intero: una ciambella per il dipolo, un disco piatto
per la collineare. Un'antenna verticale trasmette allo stesso modo in ogni direzione attorno
a sé. Fuori dal fascio disegnato il segnale non si ferma; è più debole, ma
basta ancora per un nodo vicino.

Su un tetto ti serve proprio un fascio piatto. Su una collina molto sopra i nodi,
un fascio di 23 gradi passa sopra le loro teste; un dipolo invece li copre. Una Yagi
va oltre: 16.6 dBi in un fascio alto 23 gradi
e largo 25 gradi (Amphenol Procom
7176870), e niente ai lati.

Il guadagno si misura rispetto a un riferimento. Il dBi prende come riferimento un'antenna ideale che
trasmette in modo uguale in ogni direzione. Il dBd prende come riferimento un dipolo a mezz'onda,
che ha già 2.15 dBi: anche l'antenna più semplice non manda nulla dritto
in alto o in basso. Un dipolo più lungo, di 1.25 lunghezze d'onda, arriva a 5.2 dBi. Una collineare
invece impila elementi a mezz'onda uno sopra l'altro: più ne impila, più
sale il guadagno. Se comprimi lo stesso segnale in metà spazio, lì è
due volte più forte: 3 dB. In un quarto, 4 volte più forte: 6 dB.
I produttori indicano il guadagno in dBi; il limite di legge è espresso in dBd, vedi
[Entro il limite di legge](#legal).

### Quale guadagno per il tuo sito {#choose-gain}

- **Colline, valli o città densa: circa 3 dBi.** Il fascio alto raggiunge
  i nodi sopra e sotto di te, e aggira i pendii e gli edifici che stanno in mezzo.
  Vale anche al contrario: da una valle, un fascio piatto passa sotto un
  ripetitore sulla collina sopra. Un esempio è RAKwireless RAKARG12: un
  tubo in vetroresina di 36 cm.
- **Periferia o paese con tetti bassi: da 5 a 6 dBi.** La classica
  collineare in vetroresina.
- **Terreno piatto e aperto: da 8 a 10 dBi.** Il fascio più piatto arriva più lontano
  lungo l'orizzonte. Se lo monti in alto, passa sopra i nodi vicini.

Il guadagno nel nome è il valore migliore su tutta la banda dell'antenna.
La RAKARG12, venduta come 3 dBi, ha 2.8 dBi tra 865 e 870 MHz. Leggi la tabella
del guadagno nel datasheet alla frequenza del tuo preset.

Sopra 7 dBi una scheda da 22 dBm supera il limite di legge, a meno che le perdite di cavo e filtro
non compensino la differenza. Abbassa la potenza di trasmissione di conseguenza.

Un guadagno alto aiuta solo se sai dove sono i nodi: lungo l'orizzonte
attorno a un ripetitore, o verso un ripetitore lontano per una Yagi. Un companion in
mano punta in ogni direzione, quindi gli si adatta meglio il basso guadagno con cui viene fornito.

## Perché in verticale {#vertical}

Le antenne si sentono meglio quando puntano nella stessa direzione. La perdita cresce
con l'angolo tra loro: 45 gradi costano 3 dB, metà del segnale. A
90 gradi, un'antenna orizzontale contro una verticale, in teoria non
arriva nulla. La mesh sta in verticale, quindi deve starci anche la tua antenna. Vale anche
per un companion sulla scrivania: se lo appoggi piatto, tutti i nodi attorno a te sentono
meno.

## Connettori {#connectors}

Ordina l'antenna con il connettore
della tua scheda. Ogni adattatore è un giunto in più da sigillare e altro segnale
perso.

- **SMA.** Un connettore filettato largo circa 6 mm. La presa sulla maggior parte delle schede
  ha un foro al centro; il pin sta sull'antenna. Un connettore di
  questo tipo perde circa 0.03 dB a 868 MHz.
- **RP-SMA.** Stesso corpo e stessa filettatura dell'SMA, con pin e foro
  invertiti. Sembra un SMA ma non si innesta su un SMA. Controlla quale ha
  la tua scheda prima di ordinare.
- **U.FL (IPEX).** Una minuscola presa a pressione direttamente sulla scheda. Un corto
  cavo pigtail va da lì a una presa SMA sul case. È garantita per
  30 cicli di innesto, quindi collegala una volta e lasciala lì.
- **N.** Il grosso connettore filettato delle antenne in vetroresina e del cavo spesso.
  Perde al massimo 0.05 dB. Per un ripetitore ti serve un
  adattatore o un pigtail da N all'SMA della scheda.

## Perdita del cavo {#cable}

Il cavo ti costa segnale prima che esca dall'antenna, in entrambe le direzioni. 3 dB
sono metà della tua potenza. I valori dei produttori per metro, tra 868 e 900 MHz:

| Cavo | Perdita per metro | Perdita su 5 m |
|---|---|---|
| RG174 | 1.02 dB | 5.1 dB |
| RG316 | 0.78 dB | 3.9 dB |
| RG58 | 0.45 dB | 2.2 dB |
| H-155 | 0.27 dB | 1.4 dB |
| LMR-240 | 0.25 dB | 1.2 dB |
| Ecoflex 10 | 0.13 dB | 0.7 dB |
| LMR-400 | 0.13 dB | 0.6 dB |

3 metri di RG174, il pigtail sottile fornito con molte schede, ti fanno perdere metà
della potenza. Monta la scheda vicino all'antenna con un pigtail corto, oppure
porta un cavo spesso fino all'antenna. Aggiungi al conto ogni adattatore e filtro sul percorso.

## Filtri {#filters}

Un filtro sta tra la radio e l'antenna. Lascia passare la tua banda e
blocca il resto, così un trasmettitore potente vicino non sovrasta il
ricevitore. Ti serve quando un nodo vicino ad altri trasmettitori sente meno del dovuto.
Un ripetitore su un palo con stazioni base della telefonia mobile è un nodo di questo tipo.
Un filtro costa segnale in entrambe le direzioni: conta la sua perdita come quella del cavo.

| | Filtro SAW | Filtro a cavità |
|---|---|---|
| Dimensioni | Pochi millimetri, su una piccola scheda | Un blocco o un tubo di metallo |
| Perdita di uno buono | sotto 2 dB | sotto 1 dB |
| Potenza massima in ingresso di uno buono | 500 mW | diversi watt |

Il sysmocom cf866.5-kt30, per esempio, è un filtro a cavità per 863-870 MHz
che perde al massimo 1.0 dB e regge 30 W. È fatto per l'interno,
quindi su un palo mettilo in una scatola sigillata.

I filtri variano molto, quindi controlla il datasheet prima di comprare. La potenza
in ingresso nominale deve superare la tua potenza di trasmissione, e la banda passante deve includere
la frequenza del tuo preset.

## Montaggio {#mounting}

- **Sopra il bordo del tetto.** L'antenna ha bisogno di vista libera in ogni
  direzione che copre. Anche pochi metri sopra i tetti intorno
  aiutano. In [Scegli un sito](/repeater-guide/#site) della guida al ripetitore trovi
  come controllare la vista.
- **Lontano dal metallo.** Grondaie, pali, altre antenne e tetti in metallo vicino
  all'antenna ne cambiano il diagramma e l'accordo. Montala in cima al
  palo, non di fianco.
- **In verticale.** Usa una livella a bolla; vedi [Perché in verticale](#vertical).
- **Ansa di gocciolamento.** Fai pendere il cavo sotto il connettore prima che salga
  o entri. Così l'acqua gocciola via invece di scorrere nel giunto.
- **Sigilla ogni connettore all'aperto.** L'acqua in un connettore aumenta la perdita
  e corrode il pin. Sigillalo contro la pioggia e controlla la sigillatura ogni anno.
- **Fulmini.** Un'antenna sul tetto è un bersaglio. Uno scaricatore a gas
  sul cavo interviene durante una sovratensione e la scarica a terra. Per la messa a terra segui
  [Hardware](/repeater-guide/#hardware) nella guida al ripetitore e le norme
  locali.

## Entro il limite di legge {#legal}

{{< callout type="legal" verified="2026-10-22" >}}
In Europa MeshCore usa la sottobanda 869.40-869.65 MHz, con al massimo
**500 mW** di potenza irradiata efficace (e.r.p.). Il limite riguarda ciò che esce dall'antenna:
il guadagno dell'antenna si somma, le perdite di cavo e filtro si sottraggono. Il guadagno in dBi conta
2.15 dB in meno, perché il limite si misura rispetto a un dipolo.
{{< /callout >}}

Una collineare da 5.8 dBi su una scheda da 22 dBm resta entro il limite. La stessa
antenna su una scheda con amplificatore lo supera, finché non abbassi la potenza
di trasmissione. In [Potenza: e.r.p. e la tua antenna](/repeater-guide/#erp) della
guida al ripetitore trovi il calcolo e 2 esempi svolti.

## Controlla un'antenna con un NanoVNA {#nanovna}

Un NanoVNA è un analizzatore di reti vettoriale tascabile. Ti mostra su quale
frequenza è accordata un'antenna, così lo sai prima di montarla. Il
NanoVNA-H misura fino a 1.5 GHz, quindi copre 868 MHz.

1. Calibralo per 800-950 MHz con i pezzi open, short e load
   del suo kit.
2. Collega l'antenna tramite l'adattatore che userà sul nodo. Tienila
   in verticale, lontana dal corpo e dal tavolo.
3. Leggi la curva SWR (standing wave ratio, rapporto di onde stazionarie): mostra quanto segnale
   l'antenna rimanda indietro. Il minimo deve cadere sulla frequenza del tuo preset, 869.618
   MHz per EU/UK (Narrow). Un minimo a centinaia di MHz di distanza significa che l'antenna è
   fatta per un'altra banda.

Un quarto d'onda a 868 MHz misura 86 mm (la lunghezza d'onda è 345 mm). La lunghezza
da sola non ti dice la banda, perché i produttori ripiegano e caricano gli stili; il
NanoVNA sì.

## Fonti {#sources}

- Perdita del cavo: [Belden 8216 (RG174)](https://catalog.belden.com/techdata/en/8216_techdata.pdf),
  il datasheet Huber+Suhner RG316,
  [Belden 8240 (RG58)](https://catalog.belden.com/techdata/en/8240_techdata.pdf),
  [SSB H-155](https://www.ssb.de/media/h155ssb-en.pdf),
  i datasheet Times Microwave LMR-240 e LMR-400,
  [SSB Ecoflex 10](https://www.rigpix.com/otherusefulinfo/coax/ecoflex10.pdf).
- Antenne: [Sirio SPO 868-915-6](https://rigpix.com/antennas/sirio_spo8689156_manual.pdf),
  il datasheet Sirio SO 868-915-2,
  [Amphenol Procom 7176870](https://amphenolprocom.com/products/base-station-antennas/2236-7176870),
  [RAKwireless RAKARG12](https://docs.rakwireless.com/product-categories/accessories/rakarg12/datasheet/).
- Guadagno come segnale compresso in meno spazio: [RF Cafe, introduzione alle antenne](https://www.rfcafe.com/references/electrical/ew-radar-handbook/antenna-introduction-basics.htm).
- Connettori: i datasheet Rosenberger 32S102 (SMA) e 53S101 (N), il
  catalogo Hirose U.FL.
- Filtri: la pagina prodotto sysmocom cf866.5-kt30,
  [scaricatori a gas Citel](https://citel.us/en/gas-tube-surge-arrestors-for-coaxial-line-protection).
- Perdita di polarizzazione: [University of Toronto, effetti di Friis](https://www.waves.utoronto.ca/prof/svhum/ece422/notes/12-friiseffects.pdf).
- Guadagno del dipolo in base alla lunghezza: [Wikipedia, Dipole antenna](https://en.wikipedia.org/wiki/Dipole_antenna).
- Lunghezza d'onda: velocità della luce da [NIST](https://physics.nist.gov/cgi-bin/cuu/Value?c).
- NanoVNA: [NanoVNA-H](https://github.com/hugen79/NanoVNA-H).
- Limite di legge: [CEPT ERC Recommendation 70-03](https://docdb.cept.org/document/845),
  Annex 1, banda h1.7; la [guida al ripetitore](/repeater-guide/#legal) elenca le
  altre fonti.
