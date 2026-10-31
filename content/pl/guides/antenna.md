---
title: Poradnik antenowy
lead: Dobra antena, dobrze zamontowana, sięga dalej niż większa moc. Sprawdź antenę w swoim companionie, a potem wybierz, podłącz i zamontuj antenę dla przekaźnika.
description: 'Wybierz i zamontuj antenę MeshCore na 868 MHz: sprawdzenie anteny companiona, typy anten i zysk, złącza, straty kabla na metr, filtry, montaż oraz to, jak zysk wlicza się do limitu prawnego.'
eyebrow: Companion i przekaźnik · 868 MHz
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'f828c4aa'
  seeded: '2026-10-31'
  fields: {title: '3a76cb0e', lead: 'd82ec429', description: 'ce3f3e73', eyebrow: 'd2203a35'}
  sections: ['908e2678', 'f9b96f42', 'ca18da90', 'bcfb40ec', '851afd23', '8b7a2209', 'd8832cfa', '5b70b9e8', '14a38e92', 'a5dc1e34', 'de04ca41', 'a23f19c6', '93846db4']
  blocks: ['908e2678', '0868bca9', '081db416', 'ad1da217', '73844333', 'aa14f1b1', '07e4fbad', '32d64d0d', 'ef66133c', '558c115b', '5d28e314', '57d6e138', 'e9b3d055', 'dd757d4a', '2cbd0b58', '21c67ec0', '306a3ded', 'fa46c89f', '1e6ccb3a', 'a3e53320', '6ae131c0', '98f350c6', '138d049d', '3bd28746', '2fc98ff1', '5ea29ee5', 'cfbd64e1', '48833347', '56a82a5c', '4ef7e883', '711e4fee', '1f7844ed', '6b188411', '8da9aa78', '4c2d8bbc', 'a721a9d0', '69c1dc1a', 'a631dbfa', '3f9f3471', '5af4ae3b', 'fa5095fd', '65eeb436', '15aa0eca', 'a8f5b505', '57f35115', '8e5e4975', '89764d3d']
---

Wysokość, dostrojona antena i krótki kabel dają większy zasięg niż jakikolwiek dodatkowy
miliwat. Ten poradnik zaczyna się od companiona, czyli radia, z którego wysyłasz
wiadomości. Potem omawia antenę przekaźnika. Przekaźnik to węzeł, który przekazuje
wiadomości dalej z dachu lub masztu.

## Twój companion {#companion}

{{< callout type="warning" >}}
Podłącz antenę, zanim włączysz radio. Radio LoRa, które nadaje bez anteny,
może uszkodzić własny układ.
{{< /callout >}}

Antena dołączona do płytki wystarczy. Podłącz ją, trzymaj węzeł pionowo
i zacznij pisać. Lepsza antena w companionie daje niewiele.
Przekaźnik w zasięgu daje bardzo dużo.

Kup osobną antenę prętową tylko wtedy, gdy dołączona jest uszkodzona lub jej brak.
Nie każda antena prętowa sprzedawana na 868 MHz jest dostrojona do tej częstotliwości.
[Sprawdź ją NanoVNA](#nanovna), kieszonkowym analizatorem antenowym, zanim jej zaufasz.
Możesz też pożyczyć antenę z płytki, która działa.

Węzeł obok silnego nadajnika słyszy gorzej, niż powinien. Mały
[filtr SAW (z akustyczną falą powierzchniową)](#filters) między radiem a
anteną odcina ten nadajnik od odbiornika. Najpierw sprawdź jego kartę katalogową:

- **Maksymalna moc wejściowa.** Przez filtr przechodzi też twoja własna
  transmisja. Płytka nadająca 22 dBm (160 mW) do filtra o wytrzymałości 15 dBm
  niszczy ten filtr.
- **Pasmo przenoszenia.** Musi obejmować częstotliwość twojego presetu. Filtr na pasmo
  868.65 do 869.25 MHz nie przepuszcza kanału EU/UK (Narrow) na
  869.618 MHz.

## Typy anten dla przekaźnika {#types}

Każda antena w siatce stoi pionowo. Typ wybierz według tego, gdzie są węzły,
do których chcesz dotrzeć:

- **Kolinearna z włókna szklanego.** Biała rura na maszcie, z zyskiem dookoła
  całego horyzontu. To standardowy wybór dla przekaźnika, który obsługuje miasto.
- **Dipol.** Krótszy, z mniejszym zyskiem i wysoką wiązką. Lepiej niż kolinearna
  sięga do węzłów poniżej i powyżej ciebie, na przykład ze wzgórza
  nad doliną.
- **Yagi.** Wysięgnik z poprzecznymi elementami, skierowany w jedno miejsce. Sięga do
  jednego odległego przekaźnika i niewiele poza nim. Zamontuj ją z elementami pionowo,
  bo jej polaryzacja zależy od ułożenia elementów.

## Zysk i wiązka {#gain}

Zysk nie dodaje mocy. Antena zabiera sygnał, który poszedłby w górę i w dół,
i wysyła go wzdłuż horyzontu. Działa to jak latarka, którą ogniskujesz: ta sama bateria,
dłuższa i węższa wiązka. Widać to na dipolu i kolinearnej tego samego producenta:

| Antena | Zysk | Pionowa szerokość wiązki |
|---|---|---|
| Dipol (Sirio SO 868-915-2) | 2.2 dBi | 88 stopni |
| Kolinearna z włókna szklanego (Sirio SPO 868-915-6) | 5.8 dBi | 23 stopnie |

{{< gain >}}

Wykres to przekrój przez maszt, widziany z boku. Obróć go wokół
masztu, a zobaczysz całą wiązkę: obwarzanek dla dipola, płaski dysk
dla kolinearnej. Pionowa antena nadaje tak samo we wszystkich kierunkach
dookoła siebie. Poza narysowaną wiązką sygnał nie znika. Jest słabszy, ale
wystarcza dla węzła w pobliżu.

Na dachu potrzebujesz płaskiej wiązki. Na wzgórzu wysoko nad węzłami
wiązka 23 stopni przechodzi nad ich głowami, a dipol je obejmuje. Yagi
idzie jeszcze dalej: 16.6 dBi w wiązce o wysokości 23 stopni
i szerokości 25 stopni (Amphenol Procom
7176870), a na boki nic.

Zysk podaje się względem punktu odniesienia. dBi to porównanie z idealną anteną, która
nadaje równo we wszystkich kierunkach. dBd to porównanie z dipolem półfalowym,
który sam ma 2.15 dBi: nawet najprostsza antena nie nadaje nic prosto
w górę ani w dół. Dłuższy dipol, 1.25 długości fali, osiąga 5.2 dBi. Kolinearna
zamiast tego układa elementy półfalowe jeden nad drugim. Im więcej ich ma, tym
wyższy zysk. Ściśnij ten sam sygnał w połowę przestrzeni, a będzie tam
dwa razy silniejszy: 3 dB. W ćwierć przestrzeni, a będzie 4 razy silniejszy: 6 dB.
Producenci podają zysk w dBi. Limit prawny liczy się w dBd, zobacz
[W granicach limitu prawnego](#legal).

### Jaki zysk dla twojego miejsca {#choose-gain}

- **Wzgórza, doliny lub gęsta zabudowa: około 3 dBi.** Wysoka wiązka sięga
  do węzłów powyżej i poniżej ciebie oraz za zbocza i budynki na drodze.
  Działa to też w drugą stronę: z doliny płaska wiązka przechodzi pod
  przekaźnikiem na wzgórzu powyżej. Przykładem jest RAKwireless RAKARG12:
  rura z włókna szklanego o długości 36 cm.
- **Przedmieścia lub miasto z niskimi dachami: 5 do 6 dBi.** Standardowa
  kolinearna z włókna szklanego.
- **Płaski, otwarty teren: 8 do 10 dBi.** Najbardziej płaska wiązka sięga najdalej
  wzdłuż horyzontu. Zamontowana wysoko, przechodzi nad pobliskimi węzłami.

Zysk w nazwie to najlepsza wartość w całym paśmie anteny.
RAKARG12, sprzedawana jako 3 dBi, ma 2.8 dBi w zakresie 865 do 870 MHz. Odczytaj tabelę
zysku w karcie katalogowej dla częstotliwości twojego presetu.

Powyżej 7 dBi płytka 22 dBm przekracza limit prawny, chyba że straty kabla i filtra
wyrównają różnicę. Obniż wtedy odpowiednio moc nadawania.

Wysoki zysk pomaga tylko wtedy, gdy wiesz, gdzie są węzły: wzdłuż horyzontu
wokół przekaźnika albo, w przypadku Yagi, w jednym odległym przekaźniku. Companion
w twojej dłoni jest skierowany na wszystkie strony, więc najlepiej pasuje mu niski
zysk, z którym przyszedł.

## Dlaczego pionowo {#vertical}

Anteny słyszą się najlepiej, gdy są skierowane tak samo. Strata rośnie
wraz z kątem między nimi: 45 stopni kosztuje 3 dB, czyli połowę sygnału. Przy
90 stopniach, czyli antenie leżącej wobec stojącej, teoretycznie nic
nie dociera. Siatka stoi pionowo, więc twoja antena też. Dotyczy to również
companiona na biurku: jeśli go położysz, każdy węzeł wokół ciebie słyszy
gorzej.

## Złącza {#connectors}

Zamów antenę z takim złączem, jakie ma twoja płytka. Każdy adapter to
kolejne połączenie do uszczelnienia i większa strata sygnału.

- **SMA.** Złącze gwintowane o szerokości około 6 mm. Gniazdo na większości płytek
  ma otwór w środku, a antena ma bolec. Takie złącze traci
  około 0.03 dB przy 868 MHz.
- **RP-SMA.** Ten sam korpus i gwint co SMA, ale bolec i otwór są zamienione.
  Wygląda jak SMA, a mimo to do niego nie pasuje. Sprawdź, które ma twoja
  płytka, zanim zamówisz.
- **U.FL (IPEX).** Malutkie wciskane gniazdo na samej płytce. Krótki kabel
  pigtail prowadzi z niego do gniazda SMA w obudowie. Jest przewidziane na
  30 cykli łączenia, więc podłącz je raz i zostaw.
- **N.** Duże złącze gwintowane w antenach z włókna szklanego i na grubym kablu.
  Traci najwyżej 0.05 dB. Przekaźnik potrzebuje jednego
  adaptera lub pigtaila z N na SMA płytki.

## Straty kabla {#cable}

Kabel zabiera sygnał, zanim ten opuści antenę, w obu kierunkach. 3 dB
to połowa twojej mocy. Dane producentów na metr, przy 868 do 900 MHz:

| Kabel | Strata na metr | Strata na 5 m |
|---|---|---|
| RG174 | 1.02 dB | 5.1 dB |
| RG316 | 0.78 dB | 3.9 dB |
| RG58 | 0.45 dB | 2.2 dB |
| H-155 | 0.27 dB | 1.4 dB |
| LMR-240 | 0.25 dB | 1.2 dB |
| Ecoflex 10 | 0.13 dB | 0.7 dB |
| LMR-400 | 0.13 dB | 0.6 dB |

3 metry RG174, cienkiego pigtaila dołączanego do wielu płytek, to strata połowy
twojej mocy. Zamontuj płytkę przy antenie z krótkim pigtailem albo
poprowadź do niej gruby kabel. Do sumy dodaj każdy adapter i filtr na drodze sygnału.

## Filtry {#filters}

Filtr znajduje się między radiem a anteną. Przepuszcza twoje pasmo i
blokuje resztę, więc silny pobliski nadajnik nie zagłusza
odbiornika. Potrzebujesz go, gdy węzeł w pobliżu innych nadajników słyszy gorzej,
niż powinien. Takim węzłem jest przekaźnik na maszcie ze stacjami bazowymi
telefonii komórkowej. Filtr zabiera sygnał w obu kierunkach: licz jego stratę jak
stratę kabla.

| | Filtr SAW | Filtr wnękowy |
|---|---|---|
| Rozmiar | Kilka milimetrów, na małej płytce | Metalowy blok lub rura |
| Strata dobrego filtra | poniżej 2 dB | poniżej 1 dB |
| Maksymalna moc wejściowa dobrego filtra | 500 mW | kilka watów |

Przykładem jest sysmocom cf866.5-kt30: filtr wnękowy na 863 do
870 MHz, który traci najwyżej 1.0 dB i wytrzymuje 30 W. Jest przeznaczony do wnętrz,
więc na maszcie umieść go w szczelnej skrzynce.

Filtry bardzo się od siebie różnią, więc przed zakupem sprawdź kartę katalogową.
Znamionowa moc wejściowa filtra musi przekraczać twoją moc nadawania, a pasmo
przenoszenia musi obejmować częstotliwość twojego presetu.

## Montaż {#mounting}

- **Ponad krawędzią dachu.** Antena potrzebuje wolnego widoku w każdym
  kierunku, który obsługuje. Pomaga nawet kilka metrów ponad okolicznymi dachami.
  W poradniku przekaźnika rozdział [Wybierz miejsce](/repeater-guide/#site)
  pokazuje, jak sprawdzić widok.
- **Z dala od metalu.** Rynny, maszty, inne anteny i metalowe dachy obok
  anteny zmieniają jej charakterystykę i dostrojenie. Zamontuj ją na szczycie
  masztu, nie obok niego.
- **Pionowo.** Użyj poziomicy; zobacz [Dlaczego pionowo](#vertical).
- **Pętla okapowa.** Niech kabel zwisa poniżej złącza, zanim pójdzie w górę
  lub do środka. Woda wtedy skapuje, zamiast spływać do połączenia.
- **Uszczelnij każde złącze na zewnątrz.** Woda w złączu zwiększa stratę
  i powoduje korozję bolca. Uszczelnij je przed deszczem i co roku sprawdzaj uszczelnienie.
- **Pioruny.** Antena na dachu przyciąga wyładowania. Odgromnik gazowy
  w kablu zadziała przy przepięciu i odprowadza je do ziemi. Kieruj się
  rozdziałem [Hardware](/repeater-guide/#hardware) w poradniku przekaźnika i
  lokalnymi przepisami dotyczącymi uziemienia.

## W granicach limitu prawnego {#legal}

{{< callout type="legal" verified="2026-10-22" >}}
W Europie MeshCore korzysta z podpasma 869.40-869.65 MHz, z mocą najwyżej
**500 mW** e.r.p. (efektywnej mocy promieniowanej). Limit liczy to, co opuszcza antenę:
zysk anteny się dodaje, a straty kabla i filtra się odejmują. Zysk w dBi liczy się
o 2.15 dB mniej, bo limit mierzy się względem dipola.
{{< /callout >}}

Kolinearna 5.8 dBi na płytce 22 dBm mieści się w limicie. Ta sama
antena na płytce ze wzmacniaczem już nie, dopóki nie obniżysz mocy
nadawania. W poradniku przekaźnika rozdział [Moc: e.r.p. i twoja antena](/repeater-guide/#erp)
zawiera to obliczenie i 2 przykłady z wyliczeniami.

## Sprawdź antenę NanoVNA {#nanovna}

NanoVNA to kieszonkowy wektorowy analizator sieci. Pokazuje, na jaką
częstotliwość antena jest dostrojona, więc wiesz to przed montażem.
NanoVNA-H mierzy do 1.5 GHz, co obejmuje 868 MHz.

1. Skalibruj go dla 800 do 950 MHz za pomocą elementów open, short i load
   z zestawu.
2. Podłącz antenę przez adapter, z którym będzie pracować na węźle. Trzymaj ją
   pionowo, z dala od ciała i stołu.
3. Odczytaj krzywą SWR (współczynnika fali stojącej): pokazuje, ile sygnału
   antena odbija z powrotem. Minimum musi wypadać na częstotliwości twojego presetu, 869.618
   MHz dla EU/UK (Narrow). Minimum oddalone o setki MHz oznacza, że antena
   jest zrobiona na inne pasmo.

Ćwierć fali przy 868 MHz to 86 mm (długość fali wynosi 345 mm). Sama długość
nie mówi ci, jakie to pasmo, bo producenci zwijają i obciążają anteny prętowe.
NanoVNA to pokaże.

## Źródła {#sources}

- Straty kabla: [Belden 8216 (RG174)](https://catalog.belden.com/techdata/en/8216_techdata.pdf),
  karta katalogowa Huber+Suhner RG316,
  [Belden 8240 (RG58)](https://catalog.belden.com/techdata/en/8240_techdata.pdf),
  [SSB H-155](https://www.ssb.de/media/h155ssb-en.pdf),
  karty katalogowe Times Microwave LMR-240 i LMR-400,
  [SSB Ecoflex 10](https://www.rigpix.com/otherusefulinfo/coax/ecoflex10.pdf).
- Anteny: [Sirio SPO 868-915-6](https://rigpix.com/antennas/sirio_spo8689156_manual.pdf),
  karta katalogowa Sirio SO 868-915-2,
  [Amphenol Procom 7176870](https://amphenolprocom.com/products/base-station-antennas/2236-7176870),
  [RAKwireless RAKARG12](https://docs.rakwireless.com/product-categories/accessories/rakarg12/datasheet/).
- Zysk jako sygnał ściśnięty w mniejszą przestrzeń: [RF Cafe, wprowadzenie do anten](https://www.rfcafe.com/references/electrical/ew-radar-handbook/antenna-introduction-basics.htm).
- Złącza: karty katalogowe Rosenberger 32S102 (SMA) i 53S101 (N),
  katalog Hirose U.FL.
- Filtry: strona produktu sysmocom cf866.5-kt30,
  [odgromniki gazowe Citel](https://citel.us/en/gas-tube-surge-arrestors-for-coaxial-line-protection).
- Strata polaryzacyjna: [University of Toronto, efekty we wzorze Friisa](https://www.waves.utoronto.ca/prof/svhum/ece422/notes/12-friiseffects.pdf).
- Zysk dipola a jego długość: [Wikipedia, Dipole antenna](https://en.wikipedia.org/wiki/Dipole_antenna).
- Długość fali: prędkość światła według [NIST](https://physics.nist.gov/cgi-bin/cuu/Value?c).
- NanoVNA: [NanoVNA-H](https://github.com/hugen79/NanoVNA-H).
- Limit prawny: [CEPT ERC Recommendation 70-03](https://docdb.cept.org/document/845),
  Annex 1, pasmo h1.7; resztę wymienia [poradnik przekaźnika](/repeater-guide/#legal).
