---
title: Guida alle antenne
lead: L'antenna è metà del tuo nodo. Quella giusta, montata bene, arriva più lontano di una potenza maggiore. Controlla l'antenna del tuo companion, poi scegli, collega e monta quella per un ripetitore.
description: 'Scegli e monta un''antenna MeshCore per 868 MHz: controlla lo stilo del companion, tipi di antenna e guadagno, connettori, perdita del cavo al metro, filtri, montaggio e come il guadagno conta nel limite di legge.'
eyebrow: Companion e ripetitore · 868 MHz
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '45010ad0'
  seeded: '2026-10-26'
  fields: {title: '3a76cb0e', lead: '98430ade', description: 'ce3f3e73', eyebrow: 'd2203a35'}
  sections: ['908e2678', 'f9b96f42', '94c5bae4', 'bcfb40ec', '851afd23', '8b7a2209', 'd8832cfa', '5b70b9e8', '14a38e92', 'a5dc1e34', 'de04ca41', 'a23f19c6', '93846db4']
---

Altezza, un'antenna accordata e un cavo corto danno più portata di qualsiasi milliwatt in più. Questa guida parte dal companion, la radio con cui scrivi i messaggi. Poi passa all'antenna di un ripetitore, un nodo che inoltra i messaggi da un tetto o da un palo.

## Il tuo companion {#companion}

{{< callout type="warning" >}}
Collega l'antenna prima di accendere la radio. Una radio LoRa che
trasmette senza antenna può danneggiare il proprio chip.
{{< /callout >}}

L'antenna fornita con la tua scheda fa il suo lavoro. Collegala, tieni il
nodo in verticale e inizia a scrivere messaggi. Un'antenna migliore
su un companion porta poco; un ripetitore a portata porta molto.

Compra un'antenna a stilo separata solo quando quella fornita è rotta o manca. Non
tutti gli stili venduti per 868 MHz sono accordati su quella frequenza. [Verificalo con un
NanoVNA](#nanovna), un analizzatore di antenne tascabile, prima di fidarti, oppure prendine uno in prestito da una scheda che
funziona.

Un nodo vicino a un trasmettitore forte sente meno di quanto dovrebbe. Un piccolo
[filtro SAW (surface acoustic wave)](#filters) tra la radio e
l'antenna tiene quel trasmettitore fuori dal ricevitore. Controlla prima la sua scheda tecnica:

- **Potenza massima in ingresso.** Il filtro si trova anche sul percorso della tua
  trasmissione. Una scheda che trasmette 22 dBm (160 mW) in un filtro previsto per 15 dBm
  rompe il filtro.
- **Banda passante.** Deve includere la frequenza del tuo preset. Un filtro da
  868.65 a 869.25 MHz non lascia passare il canale EU/UK (Narrow) su
  869.618 MHz.

## Tipi di antenna per un ripetitore {#types}

Ogni antenna della mesh sta in verticale. Scegli il tipo in base a dove si trovano i nodi che vuoi raggiungere:

- **Collineare in vetroresina.** Un tubo bianco su un palo, con guadagno tutt'intorno all'orizzonte. La scelta standard per un ripetitore che serve una città.
- **Dipolo.** Più corto, con meno guadagno e un lobo alto. Raggiunge i nodi sotto e sopra di te meglio di una collineare. È importante su una collina sopra una valle.
- **Yagi.** Un'asta con elementi trasversali, puntata verso un solo punto. Raggiunge un singolo ripetitore lontano e poco altro. Montala con gli elementi in verticale, perché la sua polarizzazione segue gli elementi.

## Guadagno e lobo {#gain}

Il guadagno non aggiunge potenza. Prende il segnale che andrebbe verso l'alto e il basso e lo manda lungo l'orizzonte. Come una torcia che metti a fuoco: la stessa batteria, un fascio più lungo e più stretto. Un dipolo e una collineare dello stesso produttore lo mostrano:

| Antenna | Guadagno | Apertura verticale |
|---|---|---|
| Dipolo (Sirio SO 868-915-2) | 2.2 dBi | 88 gradi |
| Collineare in vetroresina (Sirio SPO 868-915-6) | 5.8 dBi | 23 gradi |

{{< gain >}}

Il diagramma è una sezione attraverso il palo, vista di lato. Fallo ruotare intorno al palo e hai il lobo completo: una ciambella per il dipolo, un disco piatto per la collineare. Un'antenna verticale trasmette allo stesso modo in ogni direzione intorno a sé. Fuori dal lobo disegnato il segnale non si ferma; è più debole, ma basta ancora per un nodo vicino.

Su un tetto, un lobo piatto è quello che vuoi. Su una collina alta sopra i nodi, un lobo di 23 gradi passa sopra le loro teste; un dipolo li copre. Una Yagi spinge oltre: 16.6 dBi in un lobo alto 23 gradi e largo 25 gradi (Amphenol Procom 7176870), e niente ai lati.

Il guadagno si misura rispetto a un riferimento. I dBi confrontano con un'antenna ideale che trasmette allo stesso modo in ogni direzione. I dBd confrontano con un dipolo a mezz'onda, che ha già 2.15 dBi di suo: anche l'antenna più semplice non trasmette nulla dritto in alto o in basso. Un dipolo più lungo, di 1.25 lunghezze d'onda, arriva a 5.2 dBi. Una collineare invece impila elementi a mezz'onda uno sopra l'altro: più ne impila, più alto è il guadagno. Concentra lo stesso segnale in metà dello spazio e lì è due volte più forte: 3 dB. In un quarto, 4 volte più forte: 6 dB. I produttori dichiarano il guadagno in dBi; il limite di legge conta in dBd, vedi [Entro il limite di legge](#legal).

### Quale guadagno per il tuo sito {#choose-gain}

- **Colline, valli o una città densa: circa 3 dBi.** Il lobo alto raggiunge i nodi sopra e sotto di te, e aggira i pendii e gli edifici di mezzo. Vale anche al contrario: da una valle, un lobo piatto passa sotto un ripetitore sulla collina in alto. La RAKwireless RAKARG12 è una di queste: un tubo in vetroresina di 36 cm.
- **Periferie o una cittadina con tetti bassi: da 5 a 6 dBi.** La collineare in vetroresina standard.
- **Terreno piatto e aperto: da 8 a 10 dBi.** Il lobo più piatto arriva più lontano lungo l'orizzonte. Montata in alto, passa sopra i nodi vicini.

Il guadagno nel nome è il valore migliore su tutta la banda dell'antenna. La RAKARG12, venduta come 3 dBi, ha 2.8 dBi tra 865 e 870 MHz. Leggi la tabella del guadagno nella scheda tecnica alla frequenza del tuo preset.

Sopra i 7 dBi una scheda da 22 dBm supera il limite di legge, a meno che le perdite di cavo e filtro non compensino la differenza. Abbassa la potenza di trasmissione di conseguenza.

Un guadagno alto serve solo se sai dove sono i nodi: lungo l'orizzonte intorno a un ripetitore, o su un singolo ripetitore lontano per una Yagi. Un companion in mano punta in tutte le direzioni, quindi il guadagno basso con cui è arrivato è quello che gli si addice di più.

## Perché in verticale {#vertical}

Le antenne si sentono meglio quando puntano nella stessa direzione. La perdita cresce con l'angolo tra loro: 45 gradi costano 3 dB, metà del tuo segnale. A 90 gradi, un'antenna sdraiata contro una verticale, in teoria non arriva nulla. La mesh sta in verticale, quindi anche la tua antenna. Vale anche per un companion sulla scrivania: se lo sdrai, ogni nodo intorno a te sente meno.

## Connettori {#connectors}

Ordina l'antenna con il connettore che ha la tua scheda. Ogni adattatore è un giunto in più da sigillare e altro segnale perso.

- **SMA.** Un connettore filettato largo circa 6 mm. La presa sulla maggior parte delle schede ha un foro al centro; l'antenna ha il pin. Un connettore di questo tipo perde circa 0.03 dB a 868 MHz.
- **RP-SMA.** Stesso corpo e stessa filettatura dell'SMA, con pin e foro invertiti. Sembra un SMA e non si accoppia con esso. Controlla quale ha la tua scheda prima di ordinare.
- **U.FL (IPEX).** Una minuscola presa a pressione sulla scheda stessa. Da lì un corto cavetto pigtail arriva a una presa SMA sul contenitore. È garantita per 30 cicli di innesto, quindi collegala una volta e lasciala stare.
- **N.** Il grande connettore filettato delle antenne in vetroresina e dei cavi spessi. Perde al massimo 0.05 dB. Un ripetitore ha bisogno di un adattatore o pigtail da N all'SMA della scheda.

## Perdita del cavo {#cable}

Il cavo fa perdere segnale prima che esca dall'antenna, in entrambe le direzioni. 3 dB sono metà della tua potenza. I valori al metro dei produttori, tra 868 e 900 MHz:

| Cavo | Perdita al metro | Perdita su 5 m |
|---|---|---|
| RG174 | 1.02 dB | 5.1 dB |
| RG316 | 0.78 dB | 3.9 dB |
| RG58 | 0.45 dB | 2.2 dB |
| H-155 | 0.27 dB | 1.4 dB |
| LMR-240 | 0.25 dB | 1.2 dB |
| Ecoflex 10 | 0.13 dB | 0.7 dB |
| LMR-400 | 0.13 dB | 0.6 dB |

3 metri di RG174, il pigtail sottile fornito con molte schede, perdono metà della tua potenza. Monta la scheda vicino all'antenna con un pigtail corto, oppure portaci un cavo spesso. Aggiungi alla somma ogni adattatore e filtro sul percorso.

## Filtri {#filters}

Un filtro si trova tra la radio e l'antenna. Lascia passare la tua banda e
blocca il resto, così un trasmettitore forte nelle vicinanze non satura il
ricevitore. Ti serve quando un nodo sente meno di quanto dovrebbe vicino ad altri
trasmettitori. Un ripetitore su un palo con stazioni base di telefonia mobile è un
nodo di questo tipo. Un filtro fa perdere segnale in entrambe le direzioni: conta la sua perdita come
quella del cavo.

| | Filtro SAW | Filtro a cavità |
|---|---|---|
| Dimensioni | Pochi millimetri, su una piccola scheda | Un blocco o un tubo di metallo |
| Perdita di uno buono | sotto 2 dB | sotto 1 dB |
| Potenza massima in ingresso di uno buono | 500 mW | diversi watt |

Il sysmocom cf866.5-kt30, per esempio, è un filtro a cavità per la banda da 863 a
870 MHz che perde al massimo 1.0 dB e regge 30 W. È fatto per interni,
quindi mettilo in una scatola sigillata su un palo.

I filtri sono molto diversi tra loro, quindi controlla la scheda tecnica prima di comprare. La sua
potenza massima in ingresso deve superare la tua potenza di trasmissione, e la sua banda passante deve includere
la frequenza del tuo preset.

## Montaggio {#mounting}

- **Sopra il bordo del tetto.** L'antenna ha bisogno di una visuale libera in ogni direzione che serve. Anche pochi metri sopra i tetti circostanti aiutano. [Scegli un sito](/repeater-guide/#site) nella guida al ripetitore mostra come verificare la visuale.
- **Lontano dal metallo.** Grondaie, pali, altre antenne e tetti in metallo accanto all'antenna ne cambiano il diagramma e l'accordatura. Montala in cima al palo, non di fianco.
- **In verticale.** Usa una livella a bolla; vedi [Perché in verticale](#vertical).
- **Ansa di sgocciolamento.** Lascia pendere il cavo sotto il connettore prima che salga o entri. Così l'acqua gocciola via invece di colare nel giunto.
- **Sigilla ogni connettore esterno.** L'acqua in un connettore aumenta la perdita e corrode il pin. Sigillalo contro la pioggia e controlla la sigillatura ogni anno.
- **Fulmini.** Un'antenna su un tetto è un bersaglio. Uno scaricatore a gas sul cavo scatta su una sovratensione e la manda a terra. Segui [Hardware](/repeater-guide/#hardware) nella guida al ripetitore e le norme locali per la messa a terra.

## Entro il limite di legge {#legal}

{{< callout type="legal" verified="2026-10-22" >}}
In Europa MeshCore usa la sottobanda 869.40-869.65 MHz, con al massimo **500 mW** di potenza efficace irradiata (e.r.p.). Il limite conta ciò che esce dall'antenna: il guadagno dell'antenna si somma, le perdite di cavo e filtro si sottraggono. Il guadagno in dBi conta 2.15 dB in meno, perché il limite si misura rispetto a un dipolo.
{{< /callout >}}

Una collineare da 5.8 dBi su una scheda da 22 dBm resta entro il limite. La stessa antenna su una scheda con amplificatore no, finché non abbassi la potenza di trasmissione. [Potenza: e.r.p. e la tua antenna](/repeater-guide/#erp) nella guida al ripetitore contiene il calcolo e 2 esempi svolti.

## Verifica un'antenna con un NanoVNA {#nanovna}

Un NanoVNA è un analizzatore di reti vettoriale tascabile. Mostra su quale
frequenza un'antenna è accordata, così lo sai prima di montarla. Il
NanoVNA-H misura fino a 1.5 GHz, quindi copre gli 868 MHz.

1. Calibralo da 800 a 950 MHz con i pezzi open, short e load
   del suo kit.
2. Collega l'antenna tramite l'adattatore che userà sul nodo. Tienila
   in verticale e lontana dal tuo corpo e dal tavolo.
3. Leggi la curva del SWR (rapporto d'onda stazionaria): mostra quanto segnale
   l'antenna rimanda indietro. Il minimo deve stare sulla frequenza del tuo preset, 869.618
   MHz per EU/UK (Narrow). Un minimo a centinaia di MHz di distanza significa che l'antenna è
   fatta per un'altra banda.

Un quarto d'onda a 868 MHz è 86 mm (la lunghezza d'onda è 345 mm). La lunghezza
da sola non ti dice la banda, perché i produttori ripiegano e caricano gli stili; il
NanoVNA sì.

## Fonti {#sources}

- Perdita del cavo: [Belden 8216 (RG174)](https://catalog.belden.com/techdata/en/8216_techdata.pdf), la scheda tecnica Huber+Suhner RG316, [Belden 8240 (RG58)](https://catalog.belden.com/techdata/en/8240_techdata.pdf), [SSB H-155](https://www.ssb.de/media/h155ssb-en.pdf), le schede tecniche Times Microwave LMR-240 e LMR-400, [SSB Ecoflex 10](https://www.rigpix.com/otherusefulinfo/coax/ecoflex10.pdf).
- Antenne: [Sirio SPO 868-915-6](https://rigpix.com/antennas/sirio_spo8689156_manual.pdf), la scheda tecnica Sirio SO 868-915-2, [Amphenol Procom 7176870](https://amphenolprocom.com/products/base-station-antennas/2236-7176870), [RAKwireless RAKARG12](https://docs.rakwireless.com/product-categories/accessories/rakarg12/datasheet/).
- Guadagno come segnale concentrato in meno spazio: [RF Cafe, introduzione alle antenne](https://www.rfcafe.com/references/electrical/ew-radar-handbook/antenna-introduction-basics.htm).
- Connettori: le schede tecniche Rosenberger 32S102 (SMA) e 53S101 (N), il catalogo Hirose U.FL.
- Filtri: la pagina prodotto del sysmocom cf866.5-kt30, [scaricatori a gas Citel](https://citel.us/en/gas-tube-surge-arrestors-for-coaxial-line-protection).
- Perdita di polarizzazione: [Università di Toronto, effetti di Friis](https://www.waves.utoronto.ca/prof/svhum/ece422/notes/12-friiseffects.pdf).
- Guadagno del dipolo in base alla lunghezza: [Wikipedia, Dipole antenna](https://en.wikipedia.org/wiki/Dipole_antenna).
- Lunghezza d'onda: velocità della luce da [NIST](https://physics.nist.gov/cgi-bin/cuu/Value?c).
- NanoVNA: [NanoVNA-H](https://github.com/hugen79/NanoVNA-H).
- Limite di legge: [Raccomandazione CEPT ERC 70-03](https://docdb.cept.org/document/845), Allegato 1, banda h1.7; la [guida al ripetitore](/repeater-guide/#legal) elenca il resto.
