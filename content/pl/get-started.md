---
title: Pierwsze kroki
lead: Od nowej płytki do pierwszej wiadomości w siatce. Potrzebujesz płytki LoRa, komputera z Chrome lub Edge oraz telefonu albo laptopa do aplikacji.
description: Wgraj MeshCore z przeglądarki, sparuj aplikację, wybierz preset radiowy swojej okolicy, wyślij pierwszą wiadomość i dołącz do lokalnego kanału.
eyebrow: 6 kroków · MeshCore v1.18.0
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'f97ca1b9'
  seeded: '2026-10-31'
  fields: {title: '61e8d44a', lead: '45b0e5c3', description: 'cf031b18', eyebrow: '4fa6fe1e'}
  sections: ['16c3728c', '203acaa5', 'df7a1665', '6da9fd7a', 'cb5fb72e', 'a1cf8b26', 'a419ce79', '66d00206']
  blocks: ['16c3728c', '2a70a7ed', '6f8e6f5f', '16c11d47', '081db416', 'd5e7fd0b', '6d28c323', 'eb2ea361', 'de50125c', 'ae20cb8e', 'abd42710', 'c08a865a', '7d1eb0b9', '263e0c96', '0903299f', 'eba20370', '5cdc20cf', '7f542f82', '802ca5a8', '1a854187', 'bc333adf', 'f25b16fa', '7c893ae2', '7f5927b4', '26e13713', '39a142cf', 'a786620c', '216897fa', '2d222782', 'a9755900', 'f081b357']
---

Te kroki opisują firmware MeshCore v1.18.0 i oficjalne narzędzia z
października 2026. Nazwy menu w aplikacji mogą się nieco różnić między wersjami.

## 1. Wybierz urządzenie {#device}

Nada się każda płytka ze [strony urządzeń](/devices/), przy której widnieje companion.
Na pierwszy węzeł wybierz *companion*: radio, z którego wysyłasz wiadomości.
Parujesz je z telefonem lub laptopem przez Bluetooth albo USB. Możesz też
wybrać model z własnym ekranem i klawiaturą, który działa samodzielnie.

Kup wersję na 868 MHz. Antena z zestawu wystarczy. Z
[poradnika o antenach](/guides/antenna/) dowiesz się, jak ją sprawdzić.

{{< callout type="warning" >}}
Podłącz antenę, zanim włączysz radio. Radio LoRa, które nadaje bez anteny,
może uszkodzić własny układ.
{{< /callout >}}

## 2. Wgraj firmware {#flash}

1. Podłącz urządzenie do komputera kablem USB do transmisji danych.
2. Otwórz webowy flasher pod adresem [flasher.meshcore.io](https://flasher.meshcore.io)
   w Chrome lub Edge. Flasher korzysta z Web Serial, którego inne przeglądarki nie mają.
3. Wybierz swoje urządzenie, a potem firmware **Companion** dla **Bluetooth** (albo
   USB, jeśli będziesz go używać tylko z kablem do komputera).
4. Wgraj firmware. Niektóre płytki muszą najpierw przejść w tryb aktualizacji. Flasher
   podpowie ci, jak to zrobić.

Używaj opcji *erase* tylko wtedy, gdy chcesz zacząć od zera. Kasowanie usuwa tożsamość
urządzenia i twoje kontakty. Przy kolejnych aktualizacjach wgrywaj firmware bez kasowania.
Jeśli chcesz zachować tożsamość mimo kasowania, najpierw wyeksportuj w aplikacji klucz
prywatny companiona. Po kasowaniu zaimportuj go z powrotem.

## 3. Zainstaluj aplikację {#app}

Oficjalna aplikacja MeshCore działa na Androidzie, iOS, Windowsie i macOS.
Na [meshcore.io](https://meshcore.io) znajdziesz linki do wszystkich wersji. Jest też
aplikacja webowa pod adresem [app.meshcore.nz](https://app.meshcore.nz), która działa
w Chrome lub Edge na komputerze.

## 4. Sparuj swój węzeł {#pair}

Włącz węzeł, otwórz aplikację i połącz się z nim przez Bluetooth. Gdy aplikacja
zapyta o PIN:

- węzeł **z** ekranem wyświetla PIN, wpisz właśnie ten;
- węzeł **bez** ekranu używa `123456`.

Jeśli parowanie się nie uda, usuń urządzenie z ustawień Bluetooth w telefonie i
spróbuj ponownie. Potem nadaj węzłowi nazwę. Inni ją widzą, więc nie podawaj
pełnego imienia i nazwiska ani adresu, chyba że tego chcesz.

## 5. Wybierz preset radiowy swojej okolicy {#preset}

Wszystkie radia w okolicy muszą używać tej samej częstotliwości i ustawień. Inaczej
się nie słyszą. W ustawieniach radia w aplikacji wybierz preset swojej okolicy.
Poza obszarami wymienionymi niżej Europa używa **EU/UK (Narrow)**. Holandia,
Czechy, Węgry, Słowacja, Portugalia i Szwajcaria mają własne presety, a
holenderska Limburgia ma swój wariant:

{{< presets >}}

Twoje urządzenie nie ma presetu twojej okolicy? Wpisz ręcznie 4 wartości z
tabeli w ustawieniach radia w aplikacji: częstotliwość, szerokość pasma, spreading
factor i coding rate. Węzeł z innymi wartościami nie słyszy siatki.

Nie masz pewności? Twoja [lokalna grupa](/community/) wie, jakiego presetu używa twoja okolica.
Aplikacja pobiera tę listę z projektu MeshCore, więc nowy preset nie wymaga
aktualizacji aplikacji.

## 6. Przywitaj się {#hello}

1. **Ogłoś się.** Wyślij z aplikacji *ogłoszenie*. Ogłoszenie typu „flood”
   przechodzi przez przekaźniki (węzły, które przekazują wiadomości dalej), więc każdy
   w siatce może cię dodać.
   Companiony nigdy nie ogłaszają się same.
2. **Znajdź innych.** Ludzie pojawiają się w twoich kontaktach, gdy dotrą do ciebie
   ich ogłoszenia. Przekaźniki domyślnie wysyłają ogłoszenie flood co 47 godzin, więc
   zapełnienie listy może potrwać 2 dni.
3. **Wyślij wiadomość.** Otwórz kontakt i napisz. Pierwsza wiadomość rozchodzi się
   po całej sieci metodą flood. Odbiorca odsyła trasę, którą do niego dotarła, a kolejne
   wiadomości idą już tą trasą.
4. **Dołącz do kanałów.** Kanał **Public** jest już skonfigurowany. Wszystko, co tam
   napiszesz, trafia do wszystkich w siatce. Dodaj *kanał hashtagowy* swojego regionu
   (nazwa zaczynająca się od `#`), wpisując jego nazwę. Twoja
   [lokalna grupa](/community/) powie ci, które kanały są aktywne.

## Gdy coś nie działa {#troubleshooting}

**Aplikacja nie znajduje mojego urządzenia przez Bluetooth.**
Prawdopodobnie wgrałeś companiona na USB. Wgraj firmware jeszcze raz i wybierz
wersję na Bluetooth. W Heltec V3 mała wbudowana antena Bluetooth ma krótki
zasięg, więc trzymaj telefon blisko.

**Parowanie ciągle się nie udaje.**
Usuń urządzenie z ustawień Bluetooth w telefonie, uruchom Bluetooth ponownie
i sparuj jeszcze raz z PIN-em z ekranu albo `123456`.

**W moich kontaktach nikt się nie pojawia.**
Sprawdź, czy twój preset pasuje do okolicy. Wyślij ogłoszenie flood. Jeśli w zasięgu
nie ma żadnego przekaźnika, usłyszysz tylko radia w pobliżu. Na
[stronie z mapą](/map/) zobaczysz, gdzie są przekaźniki.

**Kontakt pokazuje „ostatnio widziany” kilka dni temu, choć jest aktywny.**
Jeden z dwóch węzłów ma źle ustawiony czas. Companion pobiera czas z twojego
telefonu. W przekaźnikach i room serverach (węzłach, które przechowują wiadomości
dla grupy) czas musi ustawić ich właściciel.

**Wiadomość prywatna nigdy nie dociera.**
Musicie mieć się nawzajem w kontaktach. Węzeł odrzuca wiadomość od kogoś,
kogo nie zna, i nie informuje o tym nadawcy. Wyślij ogłoszenie flood i poproś
drugą osobę, żeby też je wysłała. Sprawdź, czy aplikacja automatycznie dodaje nowe
kontakty. Dodaje tylko węzły w granicach swojego limitu skoków.

**Stare kontakty działają, nowe nigdy się nie łączą.**
Pierwsza wiadomość idzie metodą flood, a przekaźnik przekazuje ją dalej tylko wtedy,
gdy obsługuje region tej wiadomości. Kolejne wiadomości idą poznaną trasą, której
sprawdzanie regionu nie blokuje. Zapytaj swoją [lokalną grupę](/community/), jakie regiony
obsługują przekaźniki wokół ciebie, i sprawdź [ustawienia dla twojej okolicy](/guides/settings/#traffic).

**Aplikacja nie łączy się już z twoim companionem.**
Niektóre płytki mają przycisk użytkownika, na przykład część płytek RAK i Heltec T114.
Przytrzymaj go przez pierwsze 8 sekund po uruchomieniu płytki. Companion otworzy
wtedy konsolę ratunkową przez USB. W konsoli na
[flasher.meshcore.io](https://flasher.meshcore.io) polecenie `set pin <pin>` ustawia
nowy PIN Bluetooth, a `erase` czyści urządzenie.

**Flasher nie może otworzyć portu szeregowego w Linuksie.**
Twoje konto użytkownika potrzebuje dostępu do portu, na przykład przez
`sudo setfacl -m u:$USER:rw /dev/ttyUSB0`, albo członkostwa w grupie
`dialout`.

**Coś innego.** W
[MeshCore FAQ](https://github.com/meshcore-dev/MeshCore/blob/main/docs/faq.md)
znajdziesz opisy wielu innych problemów.
