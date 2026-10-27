---
title: Czym jest MeshCore?
lead: MeshCore przesyła wiadomości tekstowe drogą radiową, od węzła do węzła. Działa bez internetu i bez abonamentu.
description: 'Czym MeshCore jest, a czym nie jest: siatka, companiony, przekaźniki i room servery, trasowanie, szyfrowanie oraz pasmo 868 MHz w Europie.'
eyebrow: MeshCore v1.18.0
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '33e571f0'
  seeded: '2026-10-26'
  fields: {title: '06eda66b', lead: 'c0174569', description: '658f8a01', eyebrow: '8610c822'}
  sections: ['a3a6c1ff', '007314d2', 'f1f23981', '493b444f', '429f699c', 'f8008f48', '655373a9']
---

MeshCore to darmowe oprogramowanie dla małych radiomodułów LoRa. LoRa to technika radiowa,
która przesyła niewielkie ilości danych na duże odległości przy bardzo małym poborze mocy. Radio z MeshCore
nazywamy *węzłem*. Sparowane z aplikacją na telefonie lub laptopie, albo wyposażone we własny
ekran i klawiaturę, wysyła tekst do ludzi oddalonych o kilometry. Po drodze nie ma żadnego masztu, routera ani operatora.

MeshCore przesyła tylko krótkie wiadomości tekstowe: bez głosu, zdjęć czy ruchu
internetowego.
Dostarczenie wiadomości może potrwać kilka sekund, a to, czy dotrze, zależy od
przekaźników w okolicy. MeshCore nie zastępuje służb ratunkowych: w nagłym
wypadku dzwoń pod 112.

Oprogramowanie jest otwarte, rozwijane w repozytorium
[meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore) na licencji
MIT.

## Siatka w minutę {#mesh}

Jedno radio LoRa ma zasięg kilku kilometrów w mieście, a ze wzgórza lub dachu
znacznie większy. Aby sięgnąć dalej, radia przekazują sobie nawzajem wiadomości: to
właśnie jest *siatka*. W MeshCore przekazywaniem zajmują się radia zwane *przekaźnikami*. Przekaźnik,
który odbierze wiadomość, nadaje ją ponownie, więc może ona przebyć cały region.

Siatka nie ma właściciela. Każdy węzeł i każdy przekaźnik należy do kogoś ze
społeczności. Siatka jest tak dobra, jak przekaźniki, które ludzie postawią.

## 3 rodzaje węzłów {#roles}

Rodzaj węzła wybierasz podczas wgrywania firmware'u. Twój pierwszy węzeł to companion.

**Companion.** Twoje własne radio. Łączysz je z aplikacją MeshCore na telefonie lub
laptopie przez Bluetooth albo USB; niektóre mają własny ekran i klawiaturę. W aplikacji
czytasz i piszesz wiadomości. Companion przechowuje twoje kontakty i kanały
oraz wiadomości, które przyszły, gdy aplikacja nie była połączona. Companion nie przekazuje wiadomości dla innych.

**Przekaźnik.** Radio umieszczone wysoko, które przekazuje wiadomości dla wszystkich. Większość
działa na energii słonecznej. Własnego potrzebujesz tylko tam, gdzie siatka jeszcze nie
sięga. Nie ma własnej aplikacji. Konfigurujesz go przez USB albo
logujesz się hasłem i zarządzasz nim drogą radiową. Jak to zrobić, pokazuje
[poradnik o przekaźnikach](/repeater-guide/).

**Room server.** Mała tablica ogłoszeń w siatce. Po zalogowaniu dostajesz
wpisy, które ominęły cię poza zasięgiem, maksymalnie ostatnie 32. Lokalna grupa
używa go do ogłoszeń.

## Jak wiadomość znajduje drogę {#routing}

Każdy węzeł ma klucz tajny i klucz publiczny. Klucz publiczny to jego tożsamość. Węzeł
przedstawia się *ogłoszeniem*: podpisanym pakietem z nazwą i, jeśli tak
zdecydujesz, pozycją. Ktoś pojawia się w twoich kontaktach, gdy dotrze do ciebie jego
ogłoszenie albo gdy zeskanujesz jego kod QR. Aplikacja ma przycisk do wysłania własnego ogłoszenia.

Twoja pierwsza wiadomość do kontaktu idzie jako *flood*. Każdy przekaźnik, który ją
odbierze, przekazuje ją raz i dopisuje po drodze swój krótki identyfikator. Odpowiedź
niesie tę listę identyfikatorów z powrotem. Od tej pory twoje wiadomości do tego kontaktu
idą zapisaną trasą i nadają tylko przekaźniki, które na niej leżą. Gdy trasa
się zerwie, aplikacja znów wysyła flood.

Wiadomości do kanału nie mają jednego adresata, więc zawsze idą jako flood.
Przekaźniki pamiętają, co niedawno przekazały, i odrzucają kopie, które
docierają ponownie inną drogą. Wiadomość może przejść przez maksymalnie 64 przekaźniki, albo 32 tam, gdzie preset używa identyfikatorów
2-bajtowych.

## Szyfrowanie i prywatność {#encryption}

Twoje wiadomości prywatne są szyfrowane od końca do końca: mogą je odczytać tylko ty i druga
osoba. Przekaźnik widzi adresata pakietu tylko jako 1-bajtową wskazówkę.

Kanały są szyfrowane wspólnym kluczem, więc to, kto je czyta, zależy od tego, kto
ma ten klucz:

- **Public** jest skonfigurowany na każdym companionie. Jego klucz jest opublikowany, więc może go
  czytać każdy.
- **Kanały z hashtagiem**, na przykład `#utrecht`, wyprowadzają klucz ze swojej nazwy.
  Dołączyć może każdy, kto zna nazwę, więc traktuj je także jako publiczne.
- **Kanały prywatne** używają losowego klucza, który sam przekazujesz innym, na przykład
  jako kod QR.

Ogłoszenia są podpisane, ale nie szyfrowane. Nazwę twojego węzła, a także jego pozycję, jeśli
ją udostępniasz, widzi każdy w zasięgu. Wybierz nazwę, która nie mówi więcej,
niż chcesz.

## Pasmo 868 MHz w Europie {#band}

W Europie MeshCore korzysta z małego wycinka pasma 868 MHz, którego każdy może używać
bez pozwolenia. Europejski preset radiowy, EU/UK (Narrow), leży na
869.618 MHz w kanale o szerokości 62.5 kHz. To mieści się w podpaśmie 869.40-869.65 MHz,
które dopuszcza do 500 mW e.r.p. Urządzenie może tam nadawać najwyżej przez 10%
czasu. Szczegóły i limity dla poszczególnych krajów znajdziesz w
[sekcji prawnej poradnika o przekaźnikach](/repeater-guide/#legal).

Wszyscy na danym obszarze używają tego samego presetu, inaczej ich radia się nie
usłyszą. Niektóre kraje i regiony stosują wariant: który, wie twoja
[lokalna grupa](/community/).

## Do czego ludzie tego używają {#uses}

- Do utrzymywania kontaktu na wędrówkach, na morzu i na festiwalach, gdzie sieć komórkowa
  jest przeciążona albo jej nie ma.
- Jako kanał zapasowy dla rodziny lub sąsiadów, gdy zawiedzie prąd albo sieć
  komórkowa.
- Do lokalnego czatu na radiach, które ludzie mają na własność.
- Do eksperymentów z radiem, antenami, energią słoneczną i otwartym oprogramowaniem.
