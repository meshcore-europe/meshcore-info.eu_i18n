---
title: Przewodnik po przekaźnikach
lead: Przekaźnik ustawiony wysoko przekazuje wiadomości wszystkim wokół, w całym mieście lub dolinie. Wybierz miejsce, zasil go energią słoneczną, skonfiguruj i działaj zgodnie z prawem.
description: 'Zaplanuj, zasil, skonfiguruj i legalnie uruchom przekaźnik MeshCore w Europie: wybór miejsca, dobór paneli słonecznych, ustawienia CLI, limity mocy i cyklu pracy na 868 MHz.'
eyebrow: 868 MHz · do 500 mW · bez licencji
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '7c7e3be3'
  seeded: '2026-10-31'
  fields: {title: '4608abcd', lead: 'bc670c65', description: '9e483ce5', eyebrow: '9fd33416'}
  sections: ['05ee477a', '938c518c', '766086be', '70faf508', '8bc641aa', '399cd683', 'e9dedb7b', '92beca03', '17634750', 'cadf6024', 'e9cc6834', '2e6e59ca', 'fb44b8db']
  blocks: ['20ac0371', 'ed2b1adf', '432543ee', '7af42c89', 'd0f7543a', '9ef3580f', '3476aef7', '1bab7bec', '6a7c4493', 'dbd9fa1f', 'aa06d32b', '9958aad3', 'd162b028', 'cca1bbdf', '64ef011d', 'e7f16724', 'd2e34ff0', 'bb195cfc', '8d080bb3', '2b1d995b', '210f1b66', 'dc7419d2', 'bdc66db0', 'b59f248c', '7184bd63', 'de5a24f9', 'f5cfb426', '48c7422f', '9d3c0836', 'da8a6af3', '240126df', '8aac2b33', '81a475b8', 'a53e42b5', '36ff1db4', 'e4ca8602', 'e4594afd', '3b24b8e9', '58330858', '68f2966e', 'd7418228', '23536e60', 'cbc5c2d1', '2ea02ba9', '92540256', '6e21f681', 'a8c12311', '3382ae7f', 'cdeafb0f', '1b1319d2']
---

Przekaźniki są podstawą siatki. Companiony, czyli radia, z których wysyłasz
wiadomości, nie przekazują ich dalej. Bez przekaźników docierasz więc tylko
do osób w bezpośrednim zasięgu. Przekaźnik w dobrym miejscu rozszerza siatkę
dla wszystkich w okolicy. Ten przewodnik opisuje firmware MeshCore v1.18.0.

Zanim zaczniesz, porozmawiaj ze swoją [lokalną grupą](/community/). Jej
członkowie wiedzą, gdzie brakuje zasięgu, [jakiego presetu używa się w twojej okolicy](/guides/settings/)
i jak nazywać przekaźniki. Sprawdź na [mapach zasięgu](/map/), jakie przekaźniki
działają w pobliżu, i przywitaj się na publicznych lub lokalnych
[kanałach](/guides/channels/).

## Czy potrzebujesz przekaźnika? {#need}

Przekaźnik nadaje dalej każdą wiadomość flood, którą usłyszy. Wszystkie
przekaźniki w zasięgu dzielą ten sam czas antenowy. Tam, gdzie siatka już do
ciebie dociera, kolejny przekaźnik dokłada ruchu, a zasięgu nie poprawia.
Companion ustawiony wysoko, w oknie na strychu lub na balkonie, może w zupełności wystarczyć.

Postaw przekaźnik tam, gdzie brakuje zasięgu:

- [mapy zasięgu](/map/) nie pokazują żadnego przekaźnika w pobliżu albo tylko
  takie, których twój companion nie słyszy;
- twoja lokalna grupa mówi, że okolica go potrzebuje.

## Wybierz miejsce {#site}

Wysokość wygrywa z mocą. LoRa na 868 MHz najlepiej rozchodzi się w linii
wzroku bez przeszkód. Wzgórza, budynki i gęste drzewa zabierają dużo więcej
zasięgu, niż odzyskasz kilkoma dodatkowymi miliwatami.

- **Wybierz wysokie miejsce.** Dach, maszt, wysoki budynek lub wzgórze obejmuje
  znacznie większy obszar niż parapet. Pomaga nawet kilka metrów ponad okolicznymi dachami.
- **Zostaw antenie wolną przestrzeń.** Zamontuj ją ponad krawędzią dachu, z dala
  od metalu, rynien i innych anten.
- **Sprawdź widok.** Narzędzia takie jak [HeyWhatsThat](https://www.heywhatsthat.com/)
  pokazują, co widać z danego miejsca. Jeśli widzisz jakiś punkt, przekaźnik
  w tym miejscu jest w zasięgu.
- **Zachowaj prześwit.** Ścieżka radiowa potrzebuje wolnej przestrzeni wokół
  linii bezpośredniej, nie tylko samej linii. Na dużych odległościach środek
  ścieżki powinien przechodzić kilka metrów nad przeszkodami.
- **Zapytaj o zgodę.** Uzyskaj zgodę właściciela dachu lub masztu. Ustal z nim,
  jak dostaniesz się do przekaźnika, żeby go serwisować.

## Sprzęt {#hardware}

- **Płytka.** Wybierz energooszczędną płytkę nRF52, taką jak
  [Heltec T114](/devices/), RAK WisBlock lub SenseCAP Solar Node. Płytki ESP32
  pobierają więcej prądu (na stronie urządzeń mają oznaczenie High). Przez to
  trudno je zasilać energią słoneczną.
- **Antena.** Użyj anteny przeznaczonej na 868 MHz, zamontowanej pionowo.
  [Przewodnik po antenach](/guides/antenna/) omawia typy, złącza, kable
  i montaż. Zysk anteny wlicza się do prawnego limitu mocy, więcej w sekcji
  [Limity prawne](#legal).
- **Kabel.** Używaj krótkiego kabla koncentrycznego albo kabla o niskich
  stratach. Na 868 MHz kilka metrów cienkiego kabla może zabrać połowę mocy.
- **Obudowa.** Wodoszczelna skrzynka (IP65 lub lepsza) z dławnicą kablową,
  otworem wentylacyjnym lub odpływowym przeciw kondensacji oraz w jasnym kolorze
  lub z osłoną przed słońcem. Akumulatory źle znoszą upał i nie można ich
  ładować poniżej zera.
- **Pioruny.** Antena na dachu jest celem dla piorunów. Uziem ją
  zgodnie z lokalnymi przepisami albo zamontuj tak, by uderzenie nie dotarło do
  instalacji elektrycznej budynku.

## Zasilanie i dobór paneli słonecznych {#power}

Przekaźnik solarny musi przetrwać najciemniejsze tygodnie zimy. Dobierz
zasilanie właśnie pod nie:

1. **Zmierz pobór.** Podłącz skonfigurowany przekaźnik na dobę przez miernik
   mocy USB. Odczytaj zużytą energię w watogodzinach (Wh). Ruch w twojej
   okolicy wpływa na wynik, więc w miarę możliwości mierz na miejscu.
2. **Dodaj rezerwę.** Zaplanuj pojemność akumulatora na co najmniej 5 do 7 dni
   bez przydatnego słońca.
3. **Sprawdź zimowe nasłonecznienie.** Darmowe unijne
   [narzędzie PVGIS](https://re.jrc.ec.europa.eu/pvg_tools/en/) pokazuje dla
   dowolnego miejsca, ile energii panel wytwarza w każdym miesiącu. Weź miesiąc
   z najmniejszym nasłonecznieniem.
4. **Dobierz panel.** Panel musi pokryć dzienne zużycie w tym najgorszym
   miesiącu, z zapasem na straty przy ładowaniu.

Przykład z założonymi liczbami: przekaźnik zużywający 1 Wh na dobę potrzebuje
akumulatora o pojemności co najmniej 7 Wh na tydzień rezerwy. To około 2 Ah
pojemności użytkowej przy 3.7 V. Jeśli według PVGIS panel 1 W daje w twoim
miejscu 0.5 Wh na dobę w grudniu, potrzebujesz panelu co najmniej 2 W. Panel
3 do 5 W zostawia zapas na chmury, śnieg i starzenie się.

## Konfiguracja {#config}

**Wgraj firmware.** Użyj [web flashera](https://flasher.meshcore.io) i wybierz
firmware **Repeater** dla swojej płytki. Kroki wgrywania opisuje sekcja
[Pierwsze kroki](/get-started/#flash).

**Skonfiguruj przez USB.** Gdy przekaźnik jest wciąż podłączony do komputera,
otwórz [config.meshcore.io](https://config.meshcore.io) albo konsolę flashera.
Możesz też użyć dowolnego terminala szeregowego z prędkością 115200 baud.
Najważniejsze polecenia:

| Co | Polecenie |
|---|---|
| Zmiana hasła administratora | `password <new password>` |
| Nazwa | `set name <name>` |
| Preset radia: częstotliwość, szerokość pasma, SF, CR (działa po restarcie) | `set radio 869.618,62.5,8,8` |
| Limit cyklu pracy, w procentach | `set dutycycle 10` |
| Moc nadawania układu radiowego, w dBm | `set tx <dBm>` |
| Pozycja, żeby przekaźnik był widoczny na mapach | `set lat <degrees>` i `set lon <degrees>` |
| Dane kontaktowe dla innych operatorów | `set owner.info <text>` |
| Godziny między ogłoszeniami flood, czyli tymi, które słyszy cała siatka | `set flood.advert.interval <hours>` |
| Natychmiastowe ogłoszenie | `advert` |
| Restart | `reboot` |

Domyślne hasło administratora to `password`, a każdy, kto się nim zaloguje,
zostaje administratorem. Zmień je, zanim przekaźnik zacznie nadawać.

Przykład `set radio` powyżej dotyczy presetu EU/UK (Narrow). Zamiast nich użyj
wartości presetu twojej okolicy: [Zalecane ustawienia](/guides/settings/)
podają je dla każdego kraju.

**Ustaw zegar.** Bez modułu zegara (RTC) przekaźnik traci czas przy każdym
zaniku zasilania i startuje z datą z maja 2024. W trakcie pracy jego zegar też
dryfuje: spieszy się albo spóźnia. Dlatego co jakiś czas ustawiaj zegar:
zaloguj się zdalnie z aplikacji i użyj `clock sync` albo ustaw czas przez USB.
Z modułem RTC rzadko musisz to robić: moduł utrzymuje czas mimo zaników
zasilania i dryfuje dużo mniej.

**Zarządzaj zdalnie.** Gdy przekaźnik jest już w siatce, zaloguj się do niego
z aplikacji MeshCore hasłem administratora. Tam odczytasz jego stan i użyjesz
tych samych poleceń przez radio. Niektóre polecenia działają tylko przez USB,
na przykład `set freq` i reset fabryczny `erase`.

**Zachowaj tożsamość.** Przed wymazaniem wpisz przez USB `get prv.key`
i zapisz wyświetlony klucz prywatny w bezpiecznym miejscu. Po wymazaniu
polecenia `set prv.key <key>` i `reboot` przywracają przekaźnikowi dawną
tożsamość, więc węzły, które go znają, znajdą go pod tym samym prefiksem.

Pełna lista poleceń jest w
[dokumentacji CLI MeshCore](https://github.com/meshcore-dev/MeshCore/blob/main/docs/cli_commands.md).

## Aktualizacja bezprzewodowa {#update}

Gdy przekaźnik wisi już wysoko, aktualizujesz go z ziemi. Zaloguj się do niego
z aplikacji MeshCore hasłem administratora, otwórz wiersz poleceń i wpisz
`start ota`. Dalsze kroki zależą od płytki. Płytki inne niż opisane niżej
odpowiadają `Error`, a te aktualizujesz przez USB.

**Płytki nRF52**, takie jak RAK, Heltec T114, Seeed XIAO i SenseCAP Solar:

1. Pobierz z [web flashera](https://flasher.meshcore.io) plik **ZIP** nowego
   firmware dla swojej płytki.
2. Wpisz `start ota`. Przekaźnik odpowiada `OK` i jest widoczny przez Bluetooth
   jako `<board>_OTA`, na przykład `RAK4631_OTA`.
3. Otwórz na telefonie aplikację nRF Device Firmware Update, wybierz plik ZIP
   i przekaźnik, a potem wyślij aktualizację. Trwa to kilka minut.

Zainstaluj [bootloader OTAFIX](https://github.com/oltaco/Adafruit_nRF52_Bootloader_OTAFIX)
na płytce nRF52, zanim zamontujesz ją wysoko. Ze standardowym bootloaderem
nieudaną aktualizację naprawisz tylko przez USB. Z OTAFIX płytka wraca do trybu
aktualizacji i możesz spróbować ponownie przez Bluetooth.

**Płytki ESP32**, takie jak Heltec V3 i V4:

1. Pobierz z web flashera plik `.bin` dla swojej płytki w wersji **non-merged**:
   plik bez słowa „merged” w nazwie.
2. Wpisz `start ota`. Przekaźnik tworzy sieć WiFi o nazwie `MeshCore-OTA`
   i odpowiada adresem swojej strony do wgrywania.
3. W zasięgu WiFi połącz telefon lub laptop z tą siecią, otwórz adres i wyślij
   plik.

## Limity prawne {#legal}

{{< callout type="legal" verified="2026-10-02" >}}
Europejskie presety MeshCore mieszczą się w podpaśmie **869.40-869.65 MHz**.
W UE, Wielkiej Brytanii, Szwajcarii i Norwegii urządzenia krótkiego zasięgu
mogą z niego korzystać bez licencji, w następujących granicach:

- maksymalnie **500 mW e.r.p.** mocy promieniowanej;
- maksymalnie **10% cyklu pracy**: nie więcej niż 360 sekund nadawania w każdej
  godzinie, na urządzenie. Alternatywnie urządzenie może stosować
  listen-before-talk z adaptacyjną zmianą częstotliwości, zgodnie z definicją
  w ETSI EN 300 220-2;
- cały sygnał, o szerokości maksymalnie 250 kHz, musi mieścić się w podpaśmie.

Pasmo jest współdzielone: nie wolno ci zakłócać służb licencjonowanych, a inni
mogą zakłócać ciebie.
Radio musi mieć oznakowanie CE (w Wielkiej Brytanii CE lub UKCA).
{{< /callout >}}

Źródła: [CEPT ERC Recommendation 70-03](https://docdb.cept.org/document/845),
Załącznik 1, pasmo h1.7;
[Decyzja Komisji 2006/771/WE](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02006D0771(01)-20250123)
wraz ze zmianami;
[ETSI EN 300 220-2](https://www.etsi.org/deliver/etsi_en/300200_300299/30022002/03.03.01_60/en_30022002v030301p.pdf),
pasmo O.

### Moc: e.r.p. i twoja antena {#erp}

Limit dotyczy mocy *promieniowanej*, mierzonej względem prostej anteny dipolowej
(e.r.p.). Zysk anteny się wlicza, straty w kablu się odejmuje. Producenci
podają zysk anteny w dBi, a ta wartość jest o 2.15 dB wyższa niż ten sam zysk
w dBd (względem dipola). Utrzymaj tę sumę na poziomie 27 dBm (500 mW) lub niżej:

> moc nadawania (dBm) + zysk anteny (dBi) − straty kabla (dB) − 2.15 ≤ 27

- Płytka nadaje 22 dBm do anteny 5 dBi przez kabel o stratach 1 dB:
  22 + 5 − 1 − 2.15 = 23.85 dBm, około 240 mW e.r.p. Mieści się w limicie.
- Płytka ze wzmacniaczem 30 dBm (1 W) nadaje do anteny 3 dBi:
  30 + 3 − 2.15 = 30.85 dBm, około 1.2 W e.r.p. Limit przekroczony, zmniejsz
  moc nadawania.

`set tx` ustawia moc wyjściową układu LoRa w dBm. Sam układ SX1262 osiąga
najwyżej 22 dBm. Firmware nie sprawdza wpisanej liczby. Płytki z dodatkowym
wzmacniaczem, takie jak Heltec V4 czy Station G2, nadają z dużo większą mocą,
niż ustawisz. Zanim ją ustawisz, sprawdź tabelę producenta i zacznij od niskiej
wartości.

### Cykl pracy {#duty-cycle}

Przekaźnik nadaje dla wszystkich wokół, więc zużywa swój czas antenowy szybciej
niż companion. Ogranicznik cyklu pracy w MeshCore ma domyślnie 50%, czyli
więcej, niż pozwala to pasmo. Ustaw 10% na każdym przekaźniku:

```text
set dutycycle 10
```

### Dokładność częstotliwości {#frequency}

Kanał EU/UK (Narrow), 869.618 MHz przy szerokości pasma 62.5 kHz, sięga do
869.649 MHz: mniej niż 1 kHz poniżej górnej granicy podpasma. Sygnał musi
mieścić się w paśmie w każdej temperaturze. Do tego potrzebny jest kwarc
z kompensacją temperatury (TCXO). Ma go prawie każda obecna płytka. Starsze
płytki bez niego, takie jak Heltec V2, dryfują zbyt mocno, by niezawodnie
działać przy 62.5 kHz.

### Uwagi dla poszczególnych krajów {#countries}

- **Państwa członkowskie UE** muszą udostępnić to podpasmo na tych warunkach
  (Decyzja 2006/771/WE, artykuł 3).
- **Wielka Brytania:** te same limity, w dokumencie Ofcom
  [IR 2030](https://www.ofcom.org.uk/spectrum/radio-equipment/short-range-devices).
- **Szwajcaria i Liechtenstein:** te same limity, w dokumencie OFCOM
  [RIR1008-09](https://www.ofcomnet.ch/api/rir/1008/09).
- **Norwegia:** te same limity, w
  [rozporządzeniu o zezwoleniach ogólnych](https://lovdata.no/dokument/SF/forskrift/2012-01-19-77)
  (fribruksforskriften).

Te uwagi nie są poradą prawną. Przepisy się zmieniają. W razie wątpliwości
sprawdź je u krajowego regulatora.

## Lista kontrolna przed montażem {#checklist}

- [ ] Właściciel miejsca się zgodził, a ty masz dostęp do przekaźnika, żeby go serwisować.
- [ ] Płytka ma firmware **Repeater**, a antenę podłączono przed pierwszym
      włączeniem.
- [ ] Hasło administratora jest zmienione.
- [ ] Radio odpowiada [presetowi twojej okolicy](/guides/settings/) (`get radio`).
- [ ] Ustawiono `set dutycycle 10`.
- [ ] Moc nadawania razem z zyskiem anteny nie przekracza 500 mW e.r.p.
- [ ] Nazwa, pozycja i `owner.info` są ustawione, więc inni wiedzą, kto prowadzi przekaźnik.
- [ ] Zegar jest ustawiony (`clock`).
- [ ] Obudowa jest szczelna, ma otwór odpływowy lub wentylacyjny, a kabel ma
      pętlę ociekową.
- [ ] Akumulator i panel są dobrane pod najgorszy zimowy miesiąc.
- [ ] Przed opuszczeniem miejsca sprawdziłeś przekaźnik z daleka w aplikacji.
- [ ] Twoja lokalna grupa wie, że przekaźnik działa.
