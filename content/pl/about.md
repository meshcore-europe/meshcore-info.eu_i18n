---
title: Czym jest MeshCore?
lead: MeshCore przesyła wiadomości tekstowe drogą radiową, od węzła do węzła. Działa bez internetu i bez abonamentu.
description: 'Czym MeshCore jest, a czym nie jest: siatka, companiony, przekaźniki i room serwery, trasowanie, szyfrowanie oraz pasmo 868 MHz w Europie.'
eyebrow: MeshCore v1.18.0
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '78bc31e8'
  seeded: '2026-10-31'
  fields: {title: '06eda66b', lead: 'c0174569', description: '658f8a01', eyebrow: '8610c822'}
  sections: ['aa768ac3', 'c9b24089', '0a55792c', 'c3de803d', '493b444f', '429f699c', 'f8008f48', '655373a9', '0894fe81']
  blocks: ['c3c9c568', '55e4248c', 'c0324d05', 'b20e61c3', 'b9fc8810', '68ed3005', 'cabeb32d', 'b2ca68ba', '681d55b9', 'd1df283f', '0d0e2a8b', '0596f602', 'eec63bed', '183a79e4', '47910535', 'd5a92bbf', 'b44d4637', '431021a0', '83c03732', 'e908ca85', '8f79fbf9', '3323d83e', '857c37dc', '0c4d0dd2', 'bd238f09', '794792be', '0eb54b47', '02f1fe2f', 'e6b5b258']
---

MeshCore to darmowe oprogramowanie dla małych radiostacji LoRa. LoRa to technika radiowa, która przesyła niewiele danych na duże odległości przy bardzo małym poborze mocy. Radio z MeshCore nazywamy *węzłem*. Łączysz go z aplikacją na telefonie lub laptopie albo korzystasz z jego własnego ekranu i klawiatury. Wtedy wysyłasz tekst do ludzi oddalonych o wiele kilometrów. Po drodze nie ma masztu, routera ani operatora.

Oprogramowanie jest otwarte. Powstaje w repozytorium
[meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore) na licencji MIT.

## Czym MeshCore nie jest {#not}

Dopiero zaczynasz z radiem? Oto rzeczy, których ludzie najczęściej oczekują od MeshCore, a których on nie robi.

- **To nie jest internet ani telefon.** MeshCore przesyła krótkie wiadomości tekstowe, mniej więcej długości SMS-a. Nie przesyłasz głosu, zdjęć, filmów ani stron internetowych. Nie dodzwonisz się też na zwykły numer telefonu.
- **To nie jest służba ratunkowa.** Żadna służba ratunkowa nie nasłuchuje w siatce. Nikt nie gwarantuje, że ktoś przeczyta twoją wiadomość. W nagłym wypadku dzwoń pod 112.
- **To nie działa natychmiast ani wszędzie.** Wiadomość przeskakuje od radia do radia. Może to potrwać kilka sekund, a wiadomość może w ogóle nie dotrzeć. To, czy dotrze, zależy od przekaźników w okolicy, wysokości, budynków i twojej anteny. Małe radio w pomieszczeniu często do nikogo nie dociera. Przekaźnik na dachu sięga na wiele kilometrów.
- **To nie jest usługa, którą ktoś dla ciebie prowadzi.** Nie ma operatora, pomocy technicznej ani gwarancji zasięgu. Siatka istnieje tam, gdzie ludzie ze społeczności postawili przekaźniki, i nigdzie indziej.
- **Nie wszystko w niej jest prywatne.** Wiadomości prywatne są szyfrowane. Kanał Public i kanały z hashtagiem może jednak czytać każdy. Nazwę twojego węzła i udostępnioną pozycję widzą wszyscy w zasięgu. [Obserwatory](/network/) przekazują to, co słyszą, na publiczne mapy. Co pozostaje prywatne, wyjaśnia [sekcja o szyfrowaniu](#encryption).
- **To nie działa bez ograniczeń.** Wszyscy w danym obszarze dzielą jeden kanał radiowy. Przepisy dla [pasma 868 MHz](#band) ograniczają, jak długo każde radio może nadawać. Każda wiadomość zabiera czas antenowy wszystkim innym. Boty, częste ogłoszenia i wiadomości testowe spowalniają więc siatkę dla wszystkich.
- **To nie jest Meshtastic.** Meshtastic to inny system, który działa na bardzo podobnych płytkach. Te dwa systemy nie mogą się ze sobą komunikować.

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

- Do utrzymywania kontaktu na wędrówkach, na morzu i na festiwalach, gdzie sieć komórkowa jest przeciążona lub jej nie ma.
- Jako zapasowy kanał dla rodziny lub sąsiadów, gdy zawiedzie prąd lub sieć komórkowa.
- Do lokalnych rozmów na radiach, które ludzie mają na własność.
- Do eksperymentów z radiem, antenami, energią słoneczną i otwartym oprogramowaniem.

## Skąd pochodzą dane {#data}

Wyszukiwarka na stronie [lokalnych grup](/community/) znajduje miejscowość dzięki kopii darmowych list miejscowości i kodów pocztowych z [GeoNames](https://www.geonames.org/), udostępnionych na licencji [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Ta kopia znajduje się w tym serwisie. Wyszukiwanie nie opuszcza twojego urządzenia i żadne zapytanie nie trafia do GeoNames.
