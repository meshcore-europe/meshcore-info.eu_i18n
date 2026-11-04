---
title: Czym jest MeshCore?
lead: MeshCore przesyła wiadomości tekstowe drogą radiową, od węzła do węzła. Działa bez internetu i bez abonamentu.
description: 'Czym MeshCore jest, a czym nie jest: rodzaje węzłów, routing, szyfrowanie i pasmo 868 MHz.'
eyebrow: MeshCore v1.18.0
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '2a40da22'
  seeded: '2026-11-04'
  fields: {title: '06eda66b', lead: 'c0174569', description: 'c2255f49', eyebrow: '8610c822'}
  sections: ['aa768ac3', '92fc3ea7', '0a55792c', 'c3de803d', '493b444f', '429f699c', 'f8008f48', '203a07ef', '0894fe81']
  blocks: ['c3c9c568', '55e4248c', 'c0324d05', 'b20e61c3', 'ac039316', '68ed3005', 'cabeb32d', 'b2ca68ba', '681d55b9', 'd1df283f', '0d0e2a8b', '0596f602', 'eec63bed', '183a79e4', '47910535', 'd5a92bbf', 'b44d4637', '431021a0', '83c03732', 'e908ca85', '8f79fbf9', '3323d83e', '857c37dc', '0c4d0dd2', 'bd238f09', '794792be', '5d796ffb', '1a490368', 'f0dd237f', '3182d5c8', '02f1fe2f', 'e6b5b258']
---

MeshCore to darmowe oprogramowanie dla małych radiostacji LoRa. LoRa to technika radiowa, która przesyła niewiele danych na duże odległości przy bardzo małym poborze mocy. Radio z MeshCore nazywamy *węzłem*. Łączysz go z aplikacją na telefonie lub laptopie albo korzystasz z jego własnego ekranu i klawiatury. Wtedy wysyłasz tekst do ludzi oddalonych o wiele kilometrów. Po drodze nie ma masztu, routera ani operatora.

Oprogramowanie jest otwarte. Powstaje w repozytorium
[meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore) na licencji MIT.

## Czym MeshCore nie jest {#not}

Dopiero zaczynasz z radiem? Oto rzeczy, których ludzie najczęściej oczekują od MeshCore, a których on nie robi.

- **To nie jest internet ani telefon.** MeshCore wysyła krótkie wiadomości tekstowe,
  mniej więcej tak długie jak SMS w twoim telefonie. Nie ma głosu, zdjęć, wideo
  ani stron internetowych. Nie dodzwonisz się też na zwykły numer telefonu.
- **To nie jest służba ratunkowa.** Żadna służba ratunkowa nie obiecuje, że
  nasłuchuje w siatce. Nikt też nie obiecuje, że ktoś przeczyta twoją wiadomość.
- **To nie działa natychmiast ani wszędzie.** Wiadomość przeskakuje od radia do
  radia. Może to potrwać kilka sekund, a wiadomość może też w ogóle nie dotrzeć. To, czy
  przejdzie, zależy od przekaźników wokół ciebie, od wysokości, budynków i twojej
  anteny. Małe radio w pomieszczeniu często do nikogo nie dociera. Przekaźnik na dachu
  sięga na kilometry.
- **To nie jest usługa, którą ktoś dla ciebie prowadzi.** Nie ma operatora,
  pomocy technicznej ani obietnicy zasięgu. Siatka istnieje tam, gdzie ludzie
  ze społeczności postawili przekaźniki.
- **Nie wszystko jest w niej prywatne.** Wiadomości prywatne są szyfrowane, ale
  kanał Public i kanały z hashtagiem może czytać każdy. Nazwę twojego węzła
  i udostępnioną pozycję widzi każdy w zasięgu.
  [Obserwatorzy](/network/) przekazują to, co słyszą, do publicznych map.
  [Sekcja o szyfrowaniu](#encryption) wyjaśnia, co pozostaje prywatne.
- **To nie działa bez ograniczeń.** Wszyscy w okolicy dzielą jeden kanał radiowy, a
  zasady dla [pasma 868 MHz](#band) ograniczają, jak długo każde radio może nadawać.
  Każda wiadomość zabiera czas antenowy wszystkim innym. Dlatego boty, częste ogłoszenia
  i wiadomości testowe spowalniają siatkę dla wszystkich.
- **To nie jest Meshtastic.** Meshtastic to inny system, który działa
  w dużej mierze na tych samych płytkach. Te dwa systemy nie potrafią się ze sobą porozumieć.

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

- Łączność na wędrówkach, na morzu i na festiwalach, gdzie sieć komórkowa
  jest przeciążona albo jej nie ma.
- Zapasowy kanał dla rodziny lub sąsiadów, gdy zabraknie prądu albo padnie
  sieć komórkowa.
- Łączność zapasowa dla lokalnych władz, gdy zawiodą ich zwykłe sieci.
- Lokalny czat na radiach, które ludzie sami posiadają.
- Łączność w zespole poszukiwawczo-ratowniczym tam, gdzie nie ma sieci komórkowej.
  MeshCore SAR, aplikacja społeczności opisana w [Projektach](/projects/), dodaje
  mapy i udostępnianie lokalizacji.
- Sprawdzanie odległego miejsca z domu. Przekaźniki i węzły z czujnikami
  podają napięcie baterii i inne odczyty, gdy o nie poprosisz.
- Monitorowanie czujnika. Węzeł z czujnikiem ma firmware MeshCore przeznaczony
  do pomiarów. Przechowuje historię napięcia swojej baterii. Zaloguj się
  jako admin, a ostrzeże cię, gdy bateria będzie słaba. Ostrzeżenia dla innych
  odczytów dodajesz własnym kodem.
- Przełączanie czegoś na odległość, na przykład pompy. Tę funkcję dodajesz
  do firmware czujnika własnym kodem.
- Eksperymentowanie z radiem, antenami, energią słoneczną i otwartym oprogramowaniem.

Niektóre instytucje publiczne budują lub testują zapasową łączność opartą na MeshCore. Te przykłady sprawdziliśmy w listopadzie 2026 r.

- Cyklon Gabrielle odciął całą łączność w regionie Tairāwhiti w Nowej Zelandii. We
  wrześniu 2025 r. regionalne służby zarządzania kryzysowego uznały MeshCore za
  [jeden z co najmniej 6 zapasowych sposobów komunikacji](https://www.scoop.co.nz/stories/AK2509/S00669.htm).
  Budowały też przekaźniki zasilane energią słoneczną jako szkielet sieci.
- Niemiecki powiat Bad Kissingen
  [buduje sieć tekstową na MeshCore](https://www.landkreis-badkissingen.de/wirtschaft/digitalisierung/kommunikationsnetze/index.html)
  dla urzędów, służb ratunkowych i obiektów infrastruktury krytycznej. Jako pierwsze
  podłączają się remizy strażackie.
- Rada miasta Hilversum w Holandii
  [zagłosowała 34 do 1 za testem](https://hilversum.nl/nieuwsoverzicht/gemeenteraad-buigt-zich-over-financien)
  z przekaźnikiem na wieży ratusza. Gmina
  [oceni go jesienią 2027 r.](https://www.spreekbuis.nl/hilversum-start-proef-met-onafhankelijk-noodcommunicatienetwerk-meshcore/).
- Dwa holenderskie regiony bezpieczeństwa, które organizują reagowanie na kryzys,
  testują MeshCore:
  [Limburgia Południowa](https://nos.nl/nieuwsuur/artikel/2607176-communicatie-hulpdiensten-valt-uit-bij-lange-stroomstoring-oplossing-niet-in-zicht)
  i [Drenthe](https://www.rtvdrenthe.nl/nieuws/18438486/hackerspace-drenthe-werkt-aan-een-noodnetwerk-voor-de-provincie).
  Według Drenthe jest za wcześnie, by określić, jak i kiedy mogłoby z niego korzystać.
- W Dalfsen, również w Holandii, wolontariusze
  [prowadzą pilotaż wspólnie z gminami](https://noodnetoverijssel.nl/).
  W pierwszej kolejności używają radia głosowego, a MeshCore jako drugiej warstwy do tekstu.

Nikt nie obiecuje, że ktoś w siatce w twojej okolicy przeczyta twoją wiadomość.

## Skąd pochodzą dane {#data}

Wyszukiwarka na stronie [lokalnych grup](/community/) znajduje miejscowość dzięki kopii darmowych list miejscowości i kodów pocztowych z [GeoNames](https://www.geonames.org/), udostępnionych na licencji [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Ta kopia znajduje się w tym serwisie. Wyszukiwanie nie opuszcza twojego urządzenia i żadne zapytanie nie trafia do GeoNames.
