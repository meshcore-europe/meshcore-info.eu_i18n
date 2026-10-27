---
title: Przewodnik po antenach
lead: Antena to połowa twojego węzła. Dobra antena, dobrze zamontowana, sięga dalej niż większa moc. Sprawdź antenę w swoim companionie, potem wybierz, podłącz i zamontuj antenę dla przekaźnika.
description: 'Wybierz i zamontuj antenę MeshCore na 868 MHz: sprawdź antenę prętową companiona, typy anten i zysk, złącza, tłumienie kabla na metr, filtry, montaż i to, jak zysk liczy się do limitu prawnego.'
eyebrow: Companion i przekaźnik · 868 MHz
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '45010ad0'
  seeded: '2026-10-26'
  fields: {title: '3a76cb0e', lead: '98430ade', description: 'ce3f3e73', eyebrow: 'd2203a35'}
  sections: ['908e2678', 'f9b96f42', '94c5bae4', 'bcfb40ec', '851afd23', '8b7a2209', 'd8832cfa', '5b70b9e8', '14a38e92', 'a5dc1e34', 'de04ca41', 'a23f19c6', '93846db4']
---

Wysokość, dostrojona antena i krótki kabel dają więcej zasięgu niż każdy
dodatkowy miliwat. Ten przewodnik zaczyna od companiona, czyli radia, z
którego piszesz wiadomości. Potem przechodzi do anteny przekaźnika, czyli
węzła, który przekazuje wiadomości dalej z dachu lub masztu.

## Twój companion {#companion}

{{< callout type="warning" >}}
Podłącz antenę, zanim włączysz radio. Radio LoRa, które nadaje bez
anteny, może uszkodzić własny układ.
{{< /callout >}}

Antena dołączona do twojej płytki wystarcza. Podłącz ją, trzymaj węzeł
pionowo i zacznij pisać wiadomości. Lepsza antena w companionie daje
niewiele; przekaźnik w zasięgu daje bardzo dużo.

Kup osobną antenę prętową tylko wtedy, gdy dołączona jest uszkodzona lub
jej brakuje. Nie każda antena sprzedawana na 868 MHz jest na nią
dostrojona. [Sprawdź ją analizatorem NanoVNA](#nanovna), kieszonkowym
analizatorem anten, zanim jej zaufasz, albo pożycz antenę z płytki, która
działa.

Węzeł obok silnego nadajnika słyszy mniej, niż powinien. Mały
[filtr SAW (z akustyczną falą powierzchniową)](#filters) między radiem a
anteną odcina ten nadajnik od odbiornika. Najpierw sprawdź jego kartę
katalogową:

- **Maksymalna moc wejściowa.** Filtr leży też na ścieżce twojej własnej
  transmisji. Płytka nadająca 22 dBm (160 mW) do filtra na 15 dBm
  niszczy filtr.
- **Pasmo przepustowe.** Musi obejmować częstotliwość twojego presetu.
  Filtr na 868.65 do 869.25 MHz nie przepuszcza kanału EU/UK (Narrow) na
  869.618 MHz.

## Typy anten dla przekaźnika {#types}

Każda antena w siatce stoi pionowo. Typ dobierz do tego, gdzie są węzły,
do których chcesz dotrzeć:

- **Kolinearna z włókna szklanego.** Biała rura na maszcie, z zyskiem
  dookoła horyzontu. Standardowy wybór dla przekaźnika obsługującego
  miasto.
- **Dipol.** Krótszy, z mniejszym zyskiem i wysoką wiązką. Lepiej niż
  kolinearna sięga węzłów poniżej i powyżej ciebie. To ma znaczenie na
  wzgórzu nad doliną.
- **Yagi.** Nośnik z poprzecznymi elementami, wycelowany w jedno miejsce.
  Dociera do jednego dalekiego przekaźnika i prawie nigdzie indziej.
  Zamontuj ją z elementami pionowo, bo jej polaryzacja podąża za
  elementami.

## Zysk i wiązka {#gain}

Zysk nie dodaje mocy. Bierze sygnał, który poszedłby w górę i w dół, i
kieruje go wzdłuż horyzontu. Jak latarka, którą ogniskujesz: ta sama
bateria, dłuższa i węższa wiązka. Pokazują to dipol i antena kolinearna
tego samego producenta:

| Antena | Zysk | Szerokość wiązki w pionie |
|---|---|---|
| Dipol (Sirio SO 868-915-2) | 2.2 dBi | 88 stopni |
| Kolinearna z włókna szklanego (Sirio SPO 868-915-6) | 5.8 dBi | 23 stopnie |

{{< gain >}}

Diagram to przekrój przez maszt, widziany z boku. Obróć go wokół masztu, a
dostaniesz całą wiązkę: obwarzanek dla dipola, płaski dysk dla kolinearnej.
Pionowa antena nadaje tak samo w każdym kierunku wokół siebie. Poza
narysowaną wiązką sygnał nie znika. Jest słabszy, ale wciąż wystarczy dla
węzła w pobliżu.

Na dachu płaska wiązka to właśnie to, czego chcesz. Na wzgórzu wysoko nad
węzłami wiązka 23 stopni przechodzi im nad głowami, a dipol je pokrywa.
Yagi idzie dalej: 16.6 dBi w wiązce o wysokości 23 stopni i szerokości
25 stopni (Amphenol Procom 7176870), i nic na boki.

Zysk liczy się względem odniesienia. dBi porównuje z idealną anteną, która
nadaje jednakowo w każdym kierunku. dBd porównuje z dipolem półfalowym,
który sam ma 2.15 dBi: nawet najprostsza antena nie nadaje nic prosto w
górę ani w dół. Dłuższy dipol, 1,25 długości fali, osiąga 5.2 dBi. Antena
kolinearna zamiast tego układa elementy półfalowe jeden nad drugim: im
więcej ich układa, tym wyższy zysk. Zmieść ten sam sygnał w połowie
przestrzeni, a będzie tam dwa razy silniejszy: 3 dB. W ćwiartce, 4 razy
silniejszy: 6 dB. Producenci podają zysk w dBi, a limit prawny liczy w
dBd, zobacz [W granicach limitu prawnego](#legal).

### Jaki zysk dla twojej lokalizacji {#choose-gain}

- **Wzgórza, doliny lub gęste miasto: około 3 dBi.** Wysoka wiązka sięga
  węzłów powyżej i poniżej ciebie oraz omija zbocza i budynki na drodze.
  Działa to też w drugą stronę: z doliny płaska wiązka przechodzi pod
  przekaźnikiem na wzgórzu powyżej. Przykładem jest RAKwireless RAKARG12:
  rura z włókna szklanego o długości 36 cm.
- **Przedmieścia lub miasto z niskimi dachami: 5 do 6 dBi.** Standardowa
  kolinearna z włókna szklanego.
- **Płaski, otwarty teren: 8 do 10 dBi.** Najbardziej płaska wiązka sięga
  najdalej wzdłuż horyzontu. Zamontowana wysoko, przechodzi nad bliskimi
  węzłami.

Zysk w nazwie to najlepsza wartość w całym paśmie anteny. RAKARG12,
sprzedawana jako 3 dBi, ma 2.8 dBi w zakresie 865 do 870 MHz. Odczytaj
tabelę zysku w karcie katalogowej przy częstotliwości twojego presetu.

Powyżej 7 dBi płytka 22 dBm przekracza limit prawny, chyba że tłumienie
kabla i filtra wyrównuje różnicę. Obniż odpowiednio moc nadawania.

Wysoki zysk pomaga tylko wtedy, gdy wiesz, gdzie są węzły: wzdłuż horyzontu
wokół przekaźnika albo w jednym dalekim przekaźniku dla Yagi. Companion w
twojej dłoni celuje we wszystkie strony, więc niski zysk dołączonej anteny
pasuje do niego najlepiej.

## Dlaczego pionowo {#vertical}

Anteny słyszą się najlepiej, gdy są skierowane tak samo. Strata rośnie z
kątem między nimi: 45 stopni kosztuje 3 dB, czyli połowę sygnału. Przy
90 stopniach, antena pozioma wobec pionowej, teoretycznie nic nie dociera.
Siatka stoi pionowo, więc twoja antena też. Dotyczy to też companiona na
biurku: połóż go płasko, a każdy węzeł wokół ciebie usłyszy mniej.

## Złącza {#connectors}

Zamów antenę ze złączem, które ma twoja płytka. Każdy adapter to jeszcze
jedno połączenie do uszczelnienia i więcej straconego sygnału.

- **SMA.** Gwintowane złącze o szerokości około 6 mm. Gniazdo na większości
  płytek ma otwór pośrodku, a antena ma pin. Złącze tego typu traci około
  0.03 dB przy 868 MHz.
- **RP-SMA.** Ten sam korpus i gwint co SMA, z zamienionymi pinem i otworem.
  Wygląda jak SMA i nie pasuje do niego. Sprawdź, które ma twoja płytka,
  zanim zamówisz.
- **U.FL (IPEX).** Malutkie wciskane gniazdo na samej płytce. Krótki kabel
  pigtail biegnie od niego do gniazda SMA w obudowie. Jest przewidziane na
  30 cykli łączenia, więc podłącz je raz i zostaw.
- **N.** Duże gwintowane złącze na antenach z włókna szklanego i grubym
  kablu. Traci najwyżej 0.05 dB. Przekaźnik potrzebuje jednego adaptera
  lub pigtaila z N na SMA płytki.

## Tłumienie kabla {#cable}

Kabel kosztuje sygnał, zanim ten opuści antenę, w obu kierunkach. 3 dB to
połowa twojej mocy. Dane producentów na metr, przy 868 do 900 MHz:

| Kabel | Tłumienie na metr | Tłumienie na 5 m |
|---|---|---|
| RG174 | 1.02 dB | 5.1 dB |
| RG316 | 0.78 dB | 3.9 dB |
| RG58 | 0.45 dB | 2.2 dB |
| H-155 | 0.27 dB | 1.4 dB |
| LMR-240 | 0.25 dB | 1.2 dB |
| Ecoflex 10 | 0.13 dB | 0.7 dB |
| LMR-400 | 0.13 dB | 0.6 dB |

3 metry RG174, cienkiego pigtaila dołączanego do wielu płytek, tracą połowę
twojej mocy. Zamontuj płytkę przy antenie z krótkim pigtailem albo
poprowadź do niej gruby kabel. Do sumy dolicz każdy adapter i filtr na
drodze sygnału.

## Filtry {#filters}

Filtr siedzi między radiem a anteną. Przepuszcza twoje pasmo i blokuje
resztę, więc silny nadajnik w pobliżu nie zagłusza odbiornika. Potrzebujesz
go, gdy węzeł w pobliżu innych nadajników słyszy mniej, niż powinien. Takim
węzłem jest przekaźnik na maszcie ze stacjami bazowymi telefonii
komórkowej. Filtr kosztuje sygnał w obu kierunkach: licz jego tłumienie
jak kabel.

| | Filtr SAW | Filtr wnękowy |
|---|---|---|
| Rozmiar | Kilka milimetrów, na małej płytce | Metalowy blok lub rura |
| Tłumienie dobrego egzemplarza | poniżej 2 dB | poniżej 1 dB |
| Maksymalna moc wejściowa dobrego egzemplarza | 500 mW | kilka watów |

Na przykład sysmocom cf866.5-kt30 to filtr wnękowy na 863 do 870 MHz,
który traci najwyżej 1.0 dB i wytrzymuje 30 W. Jest zrobiony do wnętrz,
więc na maszcie włóż go do szczelnej skrzynki.

Filtry bardzo się różnią, więc przed zakupem sprawdź kartę katalogową. Jego
znamionowa moc wejściowa musi przekraczać twoją moc nadawania, a pasmo
przepustowe musi obejmować częstotliwość twojego presetu.

## Montaż {#mounting}

- **Nad krawędzią dachu.** Antena potrzebuje wolnego widoku w każdym
  kierunku, który obsługuje. Pomaga nawet kilka metrów nad okolicznymi
  dachami. [Wybór lokalizacji](/repeater-guide/#site) w przewodniku po
  przekaźnikach pokazuje, jak sprawdzić widok.
- **Z dala od metalu.** Rynny, maszty, inne anteny i metalowe dachy obok
  anteny zmieniają jej charakterystykę i strojenie. Zamontuj ją na szczycie
  masztu, nie obok niego.
- **Pionowo.** Użyj poziomicy, zobacz [Dlaczego pionowo](#vertical).
- **Pętla ociekowa.** Pozwól kablowi zwisnąć poniżej złącza, zanim pójdzie
  w górę lub do środka. Woda wtedy skapuje, zamiast wpływać do połączenia.
- **Uszczelnij każde złącze na zewnątrz.** Woda w złączu zwiększa tłumienie
  i powoduje korozję pinu. Uszczelnij je przed deszczem i co roku sprawdzaj
  uszczelnienie.
- **Piorun.** Antena na dachu to cel. Odgromnik gazowy w kablu zadziała przy
  przepięciu i odprowadzi je do ziemi. Trzymaj się sekcji
  [Sprzęt](/repeater-guide/#hardware) w przewodniku po przekaźnikach i
  lokalnych przepisów dotyczących uziemienia.

## W granicach limitu prawnego {#legal}

{{< callout type="legal" verified="2026-10-22" >}}
W Europie MeshCore używa podpasma 869.40-869.65 MHz, z mocą najwyżej
**500 mW** skutecznej mocy promieniowanej (e.r.p.). Limit liczy to, co
opuszcza antenę: zysk anteny dodaje, tłumienie kabla i filtra odejmuje.
Zysk w dBi liczy się o 2.15 dB mniej, bo limit mierzy się względem dipola.
{{< /callout >}}

Kolinearna 5.8 dBi na płytce 22 dBm mieści się w limicie. Ta sama antena na
płytce ze wzmacniaczem już nie, dopóki nie obniżysz mocy nadawania.
[Moc: e.r.p. i twoja antena](/repeater-guide/#erp) w przewodniku po
przekaźnikach zawiera obliczenie i 2 rozwiązane przykłady.

## Sprawdź antenę analizatorem NanoVNA {#nanovna}

NanoVNA to kieszonkowy wektorowy analizator sieci. Pokazuje, na jaką
częstotliwość antena jest dostrojona, więc wiesz to przed montażem.
NanoVNA-H mierzy do 1.5 GHz, co obejmuje 868 MHz.

1. Skalibruj go na 800 do 950 MHz elementami otwartym, zwartym i
   obciążeniem z jego zestawu.
2. Podłącz antenę przez adapter, którego będzie używać na węźle. Trzymaj
   ją pionowo, z dala od swojego ciała i stołu.
3. Odczytaj krzywą SWR (współczynnika fali stojącej): pokazuje, ile sygnału
   antena odbija z powrotem. Dołek musi leżeć na częstotliwości twojego
   presetu, 869.618 MHz dla EU/UK (Narrow). Dołek setki MHz dalej oznacza,
   że antena jest zrobiona na inne pasmo.

Ćwierć fali przy 868 MHz to 86 mm (długość fali to 345 mm). Sama długość
nie mówi ci o paśmie, bo producenci zwijają i obciążają anteny prętowe;
NanoVNA mówi.

## Źródła {#sources}

- Tłumienie kabla: [Belden 8216 (RG174)](https://catalog.belden.com/techdata/en/8216_techdata.pdf),
  karta katalogowa Huber+Suhner RG316,
  [Belden 8240 (RG58)](https://catalog.belden.com/techdata/en/8240_techdata.pdf),
  [SSB H-155](https://www.ssb.de/media/h155ssb-en.pdf),
  karty katalogowe Times Microwave LMR-240 i LMR-400,
  [SSB Ecoflex 10](https://www.rigpix.com/otherusefulinfo/coax/ecoflex10.pdf).
- Anteny: [Sirio SPO 868-915-6](https://rigpix.com/antennas/sirio_spo8689156_manual.pdf),
  karta katalogowa Sirio SO 868-915-2,
  [Amphenol Procom 7176870](https://amphenolprocom.com/products/base-station-antennas/2236-7176870),
  [RAKwireless RAKARG12](https://docs.rakwireless.com/product-categories/accessories/rakarg12/datasheet/).
- Zysk jako sygnał ściśnięty w mniejszej przestrzeni: [RF Cafe, wprowadzenie do anten](https://www.rfcafe.com/references/electrical/ew-radar-handbook/antenna-introduction-basics.htm).
- Złącza: karty katalogowe Rosenberger 32S102 (SMA) i 53S101 (N), katalog
  Hirose U.FL.
- Filtry: strona produktu sysmocom cf866.5-kt30,
  [odgromniki gazowe Citel](https://citel.us/en/gas-tube-surge-arrestors-for-coaxial-line-protection).
- Strata polaryzacyjna: [University of Toronto, efekty Friisa](https://www.waves.utoronto.ca/prof/svhum/ece422/notes/12-friiseffects.pdf).
- Zysk dipola według długości: [Wikipedia, Dipole antenna](https://en.wikipedia.org/wiki/Dipole_antenna).
- Długość fali: prędkość światła z [NIST](https://physics.nist.gov/cgi-bin/cuu/Value?c).
- NanoVNA: [NanoVNA-H](https://github.com/hugen79/NanoVNA-H).
- Limit prawny: [CEPT ERC Recommendation 70-03](https://docdb.cept.org/document/845),
  Annex 1, pasmo h1.7; [przewodnik po przekaźnikach](/repeater-guide/#legal)
  wymienia resztę.
