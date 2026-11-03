---
title: Czym jest MeshCore?
lead: MeshCore przesyła wiadomości tekstowe drogą radiową, od węzła do węzła. Działa bez internetu i bez abonamentu.
description: 'Czym MeshCore jest, a czym nie jest: rodzaje węzłów, routing, różnice względem Meshtastic, szyfrowanie i pasmo 868 MHz.'
eyebrow: MeshCore v1.18.0
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '279b56a4'
  seeded: '2026-11-02'
  fields: {title: '06eda66b', lead: 'c0174569', description: '15e6d2a7', eyebrow: '8610c822'}
  sections: ['aa768ac3', '16fde264', '0a55792c', 'c3de803d', '493b444f', 'a8b2b9b4', '429f699c', 'f8008f48', '88af2bd3', '0894fe81']
  blocks: ['c3c9c568', '55e4248c', 'c0324d05', 'b20e61c3', 'fab378a5', '68ed3005', 'cabeb32d', 'b2ca68ba', '681d55b9', 'd1df283f', '0d0e2a8b', '0596f602', 'eec63bed', '183a79e4', '47910535', 'd5a92bbf', 'b44d4637', 'fc8f3129', '8dec428a', '07cbac35', '431021a0', '83c03732', 'e908ca85', '8f79fbf9', '3323d83e', '857c37dc', '0c4d0dd2', 'bd238f09', '794792be', '95e18f18', '02f1fe2f', 'e6b5b258']
---

MeshCore to darmowe oprogramowanie dla małych radiostacji LoRa. LoRa to technika radiowa, która przesyła niewiele danych na duże odległości przy bardzo małym poborze mocy. Radio z MeshCore nazywamy *węzłem*. Łączysz go z aplikacją na telefonie lub laptopie albo korzystasz z jego własnego ekranu i klawiatury. Wtedy wysyłasz tekst do ludzi oddalonych o wiele kilometrów. Po drodze nie ma masztu, routera ani operatora.

Oprogramowanie jest otwarte. Powstaje w repozytorium
[meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore) na licencji MIT.

## Czym MeshCore nie jest {#not}

Dopiero zaczynasz z radiem? Oto rzeczy, których ludzie najczęściej oczekują od MeshCore, a których on nie robi.

- **To nie internet ani telefon.** MeshCore wysyła krótkie wiadomości tekstowe,
  mniej więcej tej długości co SMS w twoim telefonie. Nie prześlesz głosu, zdjęć, wideo
  ani stron internetowych. Nie dotrzesz też do zwykłego numeru telefonu.
- **To nie służba ratunkowa.** Żadna służba ratunkowa nie nasłuchuje w
  siatce i nikt nie obiecuje, że ktoś przeczyta twoją wiadomość. W
  nagłym wypadku zadzwoń pod 112.
- **To nie działa natychmiast ani wszędzie.** Wiadomość przeskakuje od radia do
  radia. Może jej to zająć kilka sekund, a może też w ogóle nie dotrzeć. To, czy
  dotrze, zależy od przekaźników wokół ciebie, od wysokości, budynków i twojej
  anteny. Małe radio w pomieszczeniu często do nikogo nie dociera; przekaźnik na dachu
  ma zasięg liczony w kilometrach.
- **To nie usługa, którą ktoś dla ciebie prowadzi.** Nie ma operatora, pomocy
  technicznej ani obietnicy zasięgu. Siatka istnieje tam, gdzie ludzie ze
  społeczności postawili przekaźniki, i nigdzie indziej.
- **Nie wszystko w siatce jest prywatne.** Wiadomości prywatne są szyfrowane, ale
  kanał Public i kanały z hashtagiem może czytać każdy. Nazwę twojego węzła
  i udostępnianą pozycję widzą wszyscy w zasięgu.
  [Obserwatorzy](/network/) przekazują to, co słyszą, na publiczne mapy.
  [Sekcja o szyfrowaniu](#encryption) wyjaśnia, co pozostaje prywatne.
- **To nie jest system bez ograniczeń.** Wszyscy na danym obszarze korzystają z jednego kanału radiowego, a
  przepisy dotyczące [pasma 868 MHz](#band) ograniczają, jak długo każde radio może nadawać.
  Każda wiadomość zabiera czas antenowy wszystkim innym, więc boty, częste ogłoszenia
  i wiadomości testowe spowalniają siatkę dla wszystkich.
- **To nie Meshtastic.** Meshtastic to inny system, który działa na
  niemal tych samych płytkach. Oba systemy nie mogą się ze sobą komunikować.
  [Przejście z Meshtastic](#meshtastic) opisuje, co działa inaczej.

## Siatka w minutę {#mesh}

Jedno radio LoRa sięga w mieście na kilka kilometrów, a ze wzgórza lub dachu znacznie dalej. Żeby dotrzeć dalej, radia przekazują sobie nawzajem wiadomości: to jest *siatka*. W MeshCore przekazywaniem zajmują się radia zwane *przekaźnikami*. Przekaźnik, który usłyszy wiadomość, nadaje ją ponownie. Dzięki temu może ona przejść przez cały region.

Siatka nie ma właściciela. Każdy węzeł i każdy przekaźnik należy do kogoś ze społeczności. Siatka sięga tak daleko, jak ich przekaźniki.

## 3 rodzaje węzłów {#roles}

Rodzaj węzła wybierasz podczas wgrywania firmware. Twój pierwszy węzeł to companion.

**Companion.** Twoje własne radio. Łączysz je z aplikacją MeshCore na telefonie lub laptopie przez Bluetooth lub USB. Niektóre mają własny ekran i klawiaturę. W aplikacji czytasz i piszesz. Companion przechowuje twoje kontakty i kanały oraz wiadomości, które przyszły, gdy aplikacja nie była połączona. Companion nie przekazuje wiadomości innych osób.

**Przekaźnik.** Radio umieszczone wysoko, które przekazuje wiadomości dla wszystkich. Większość działa na energii słonecznej. Własnego potrzebujesz tylko tam, gdzie siatka jeszcze nie sięga. Przekaźnik nie ma własnej aplikacji. Konfigurujesz go przez USB albo logujesz się hasłem i zarządzasz nim drogą radiową. Jak to zrobić, pokazuje [poradnik o przekaźnikach](/repeater-guide/).

**Room server.** Mała tablica ogłoszeń w siatce. Gdy się zalogujesz, dostaniesz posty, które przegapiłeś poza zasięgiem, do 32 ostatnich. Room server trzyma je tylko w pamięci, więc restart lub awaria zasilania je kasuje. Lokalna grupa używa go do ogłoszeń.

## Jak wiadomość znajduje drogę {#routing}

Każdy węzeł ma klucz tajny i klucz publiczny. Klucz publiczny to jego tożsamość. Węzeł przedstawia się *ogłoszeniem*: to podpisany pakiet z jego nazwą i, jeśli chcesz, z jego pozycją. Ktoś pojawia się w twoich kontaktach, gdy dotrze do ciebie jedno z jego ogłoszeń albo gdy zeskanujesz jego kod QR. Własne ogłoszenie wysyłasz przyciskiem w aplikacji.

Twoja pierwsza wiadomość do kontaktu idzie jako *flood*. Każdy przekaźnik, który ją usłyszy, przekazuje ją raz i dopisuje po drodze swój krótki identyfikator. Odpowiedź przynosi tę listę identyfikatorów z powrotem. Od tej chwili twoje wiadomości do tego kontaktu idą zapisaną ścieżką i nadają tylko przekaźniki na tej ścieżce. Gdy ścieżka się zerwie, aplikacja znów wysyła flood.

Wiadomości do kanału nie mają jednego adresu, więc zawsze idą jako flood. Przekaźniki pamiętają, co ostatnio przekazały, i odrzucają kopie, które docierają ponownie inną drogą. Wiadomość może przejść przez maksymalnie 64 przekaźniki. Gdy preset używa 2-bajtowych identyfikatorów, limit wynosi 32.

## Przejście z Meshtastic {#meshtastic}

Na wielu płytkach działa MeshCore albo Meshtastic, a ty wgrywasz ten, który chcesz. Oto różnice, które zauważysz na początku. Opierają się na MeshCore
v1.18.0 i dokumentacji Meshtastic z listopada 2026.

- **Kto przekazuje wiadomości.** W MeshCore robią to tylko przekaźniki, twój companion nigdy tego nie robi. W Meshtastic domyślna rola client też przekazuje wiadomości, chyba że zrobił to już inny węzeł.
- **Jak daleko dociera wiadomość.** Wiadomość w MeshCore może przejść przez maksymalnie 64 przekaźniki. Meshtastic domyślnie zatrzymuje ją po 3 skokach, a maksymalnie po 7.
- **Odczyty z innych węzłów.** Przekaźniki i węzły z czujnikami w MeshCore wysyłają odczyty, na przykład napięcie baterii, gdy o nie poprosisz. Nie wysyłają ich do całej siatki.
- **Internet.** Firmware MeshCore nie łączy siatek przez internet. [Obserwatorzy](/network/) przekazują mapom to, co słyszą, tylko w jedną stronę. Meshtastic ma wbudowany moduł MQTT, który może przenosić wiadomości między siatkami przez internet.

## Szyfrowanie i prywatność {#encryption}

Twoje wiadomości prywatne są szyfrowane od końca do końca: przeczytać je możesz tylko ty i twój rozmówca. Przekaźnik widzi adresata pakietu tylko jako 1-bajtową wskazówkę.

Kanały są szyfrowane wspólnym kluczem. To, kto może je czytać, zależy więc od tego, kto ma ten klucz:

- **Public** jest ustawiony na każdym companionie. Jego klucz jest opublikowany, więc każdy może go czytać.
- **Kanały z hashtagiem**, takie jak `#utrecht`, biorą klucz ze swojej nazwy. Każdy, kto zna nazwę, może dołączyć, więc traktuj je również jako publiczne.
- **Kanały prywatne** używają losowego klucza, który sam udostępniasz, na przykład jako kod QR.

Ogłoszenia są podpisane, ale nie szyfrowane. Nazwę twojego węzła i jego pozycję, jeśli ją udostępniasz, widzą wszyscy w zasięgu. Wybierz nazwę, która nie zdradza więcej, niż chcesz.

## Pasmo 868 MHz w Europie {#band}

W Europie MeshCore korzysta z niewielkiej części pasma 868 MHz, której każdy może używać bez licencji. Jego europejski preset radiowy, EU/UK (Narrow), działa na 869.618 MHz w kanale 62.5 kHz. Ta częstotliwość leży w podpaśmie 869.40-869.65 MHz, które dopuszcza do 500 mW e.r.p. Urządzenie może tam nadawać najwyżej przez 10% czasu. Szczegóły i limity dla poszczególnych krajów znajdziesz w [sekcji prawnej poradnika o przekaźnikach](/repeater-guide/#legal).

Wszyscy w danym obszarze używają tego samego presetu, bo inaczej ich radia się nie słyszą. Niektóre kraje i regiony używają wariantu: który, wie twoja [lokalna grupa](/community/).

## Do czego ludzie go używają {#uses}

- Utrzymywanie kontaktu na szlaku, na morzu i na festiwalach, gdzie sieć komórkowa
  jest przeciążona lub jej nie ma.
- Zapasowy kanał łączności dla rodziny lub sąsiadów, gdy zabraknie prądu lub padnie
  sieć komórkowa.
- Lokalny czat na radiach, które ludzie mają na własność.
- Sprawdzanie odległego miejsca z domu. Przekaźniki i węzły z czujnikami podają
  napięcie baterii i inne odczyty, gdy o nie poprosisz.
- Obserwowanie czujnika. Na węźle z czujnikiem działa firmware MeshCore do pomiarów.
  Węzeł przechowuje historię swoich odczytów. Jeśli go zasubskrybujesz, wyśle ci alert,
  na przykład gdy kończy mu się bateria.
- Przełączanie czegoś na odległość, na przykład pompy. Dodajesz to do firmware czujnika
  własnym kodem.
- Eksperymenty z radiem, antenami, energią słoneczną i otwartym oprogramowaniem.

## Skąd pochodzą dane {#data}

Wyszukiwarka na stronie [lokalnych grup](/community/) znajduje miejscowość dzięki kopii darmowych list miejscowości i kodów pocztowych z [GeoNames](https://www.geonames.org/), udostępnionych na licencji [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Ta kopia znajduje się w tym serwisie. Wyszukiwanie nie opuszcza twojego urządzenia i żadne zapytanie nie trafia do GeoNames.
