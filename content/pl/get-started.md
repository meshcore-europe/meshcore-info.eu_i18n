---
title: Pierwsze kroki
lead: Od nowej płytki do pierwszej wiadomości w siatce. Potrzebujesz płytki LoRa, komputera z Chrome lub Edge oraz telefonu lub laptopa do aplikacji.
description: Wgraj MeshCore z przeglądarki, sparuj aplikację, wybierz preset radiowy używany w twojej okolicy, wyślij pierwszą wiadomość i dołącz do lokalnego kanału.
eyebrow: 6 kroków · MeshCore v1.18.0
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '68c89544'
  seeded: '2026-10-26'
  fields: {title: '61e8d44a', lead: '45b0e5c3', description: 'cf031b18', eyebrow: '4fa6fe1e'}
  sections: ['16c3728c', '203acaa5', '36a3eba3', '6da9fd7a', 'cb5fb72e', '89626504', 'a419ce79', 'aa273b20']
---

Te kroki odpowiadają firmware MeshCore v1.18.0 i oficjalnym narzędziom z
października 2026. Nazwy w menu aplikacji mogą się nieco różnić między wersjami.

## 1. Wybierz urządzenie {#device}

Zadziała każda płytka ze [strony urządzeń](/devices/), przy której podano companion. Na
swój pierwszy węzeł wybierz *companion*: radio, z którego wysyłasz wiadomości. Sparuj je z
telefonem lub laptopem przez Bluetooth albo USB, albo wybierz model z własnym ekranem
i klawiaturą, który działa samodzielnie.

Kup wersję na 868 MHz. Dołączona antena wystarczy; w
[poradniku o antenach](/guides/antenna/) znajdziesz, jak ją sprawdzić.

{{< callout type="warning" >}}
Podłącz antenę, zanim włączysz radio. Radio LoRa, które
nadaje bez anteny, może uszkodzić własny układ.
{{< /callout >}}

## 2. Wgraj firmware {#flash}

1. Podłącz urządzenie do komputera kablem USB do transmisji danych.
2. Otwórz flasher webowy na [flasher.meshcore.io](https://flasher.meshcore.io)
   w Chrome lub Edge. Korzysta on z Web Serial, którego inne przeglądarki nie mają.
3. Wybierz swoje urządzenie, a potem firmware **Companion** dla **Bluetooth** (lub
   USB, jeśli będziesz go używać tylko po kablu z komputerem).
4. Wgraj. Niektóre płytki najpierw przechodzą w tryb aktualizacji; flasher podpowie ci,
   jak to zrobić.

Opcji *erase* używaj tylko, gdy chcesz zacząć od zera: wymazanie usuwa tożsamość urządzenia
i twoje kontakty. Przy późniejszych aktualizacjach wgrywaj bez wymazywania.

## 3. Zainstaluj aplikację {#app}

Oficjalna aplikacja MeshCore jest dostępna na Androida, iOS, Windows i macOS;
na [meshcore.io](https://meshcore.io) znajdziesz linki do każdej wersji. Istnieje też
aplikacja webowa [app.meshcore.nz](https://app.meshcore.nz), która działa w Chrome lub
Edge na komputerze.

## 4. Sparuj węzeł {#pair}

Włącz węzeł, otwórz aplikację i połącz się z nim przez Bluetooth. Gdy aplikacja
poprosi o PIN:

- węzeł **z** ekranem wyświetla PIN; wpisz ten kod;
- węzeł **bez** ekranu używa `123456`.

Jeśli parowanie się nie uda, usuń urządzenie z ustawień Bluetooth w telefonie i
spróbuj ponownie. Potem nadaj węzłowi nazwę. Inni ją widzą, więc nie używaj
pełnego imienia i nazwiska ani adresu, chyba że tego chcesz.

## 5. Wybierz preset radiowy swojej okolicy {#preset}

Wszystkie radia w okolicy używają tej samej częstotliwości i ustawień, inaczej nie
słyszą się nawzajem. W ustawieniach radia w aplikacji wybierz preset używany w twojej okolicy.
Poza obszarami wymienionymi poniżej Europa używa **EU/UK (Narrow)**. Holandia,
Czechy, Węgry, Słowacja, Portugalia i Szwajcaria mają własne, a
Limburgia w Holandii ma wariant:

{{< presets >}}

Nie masz pewności? Twoja [lokalna grupa](/community/) wie, którego presetu używa twoja okolica.
Aplikacja pobiera tę listę z projektu MeshCore, więc nowy preset nie wymaga
aktualizacji aplikacji.

## 6. Przywitaj się {#hello}

1. **Ogłoś swoją obecność.** Wyślij z aplikacji *ogłoszenie*. Ogłoszenie typu "flood"
   przechodzi przez przekaźniki (węzły, które przekazują wiadomości dalej), więc każdy
   w siatce może cię dodać.
   Companiony nigdy nie ogłaszają się automatycznie.
2. **Znajdź innych.** Ludzie pojawiają się w twoich kontaktach, gdy ich ogłoszenia do ciebie
   dotrą. Przekaźniki domyślnie wysyłają ogłoszenie flood co 47 godzin, więc zapełnienie
   listy może zająć 2 dni.
3. **Wyślij wiadomość.** Otwórz kontakt i napisz. Pierwsza wiadomość idzie floodem
   przez sieć; odbiorca odsyła informację o trasie, którą przeszła, a kolejne
   wiadomości podążają tą trasą.
4. **Dołącz do kanałów.** Kanał **Public** jest już skonfigurowany; wszystko, co
   tam napiszesz, dociera do każdego w siatce. Dodaj *kanał hashtagowy* swojego regionu
   (nazwa zaczynająca się od `#`), wpisując jego nazwę. Twoja
   [lokalna grupa](/community/) powie ci, które kanały są aktywne.

## Gdy coś nie działa {#troubleshooting}

**Aplikacja nie znajduje mojego urządzenia przez Bluetooth.**
Prawdopodobnie wgrałeś companion w wersji USB. Wgraj ponownie i wybierz wersję
Bluetooth. W Heltec V3 mała wbudowana antena Bluetooth
ma krótki zasięg; trzymaj telefon blisko.

**Parowanie ciągle się nie udaje.**
Usuń urządzenie z ustawień Bluetooth w telefonie, uruchom Bluetooth ponownie
i sparuj jeszcze raz z PIN-em z ekranu lub `123456`.

**Nikt nie pojawia się w moich kontaktach.**
Sprawdź, czy twój preset zgadza się z okolicą. Wyślij ogłoszenie flood. Jeśli w zasięgu
nie ma przekaźnika, usłyszysz tylko radia w pobliżu;
[strona z mapą](/map/) pokazuje, gdzie są przekaźniki.

**Kontakt pokazuje "ostatnio widziany" sprzed kilku dni, choć jest aktywny.**
Jeden z dwóch węzłów ma złą godzinę. Companion pobiera czas z
twojego telefonu; przekaźniki i room servery (węzły, które przechowują wiadomości dla
grupy) potrzebują ustawienia czasu przez właściciela.

**Flasher nie może otworzyć portu szeregowego w Linuksie.**
Twój użytkownik potrzebuje dostępu do portu, na przykład
`sudo setfacl -m u:$USER:rw /dev/ttyUSB0`, albo członkostwa w grupie `dialout`.

**Coś innego.**
[FAQ MeshCore](https://github.com/meshcore-dev/MeshCore/blob/main/docs/faq.md)
opisuje wiele innych problemów.
