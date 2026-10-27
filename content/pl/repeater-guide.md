---
title: Poradnik o przekaźnikach
lead: Przekaźnik umieszczony wysoko przekazuje wiadomości dla wszystkich wokół, w całym mieście lub dolinie. Wybierz miejsce, zasil go ze słońca, skonfiguruj i trzymaj się przepisów.
description: 'Zaplanuj, zasil, skonfiguruj i legalnie uruchom przekaźnik MeshCore w Europie: wybór miejsca, dobór paneli słonecznych, ustawienia CLI, limity mocy i duty cycle na 868 MHz.'
eyebrow: 868 MHz · do 500 mW · bez licencji
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '4a0fe39f'
  seeded: '2026-10-26'
  fields: {title: '4608abcd', lead: 'bc670c65', description: '9e483ce5', eyebrow: '9fd33416'}
  sections: ['1de4a4f7', '766086be', '70faf508', '8bc641aa', '2018aa04', '92beca03', '17634750', 'cadf6024', 'e9cc6834', '2e6e59ca', 'fb44b8db']
---

Przekaźniki tworzą siatkę. Companiony, czyli radia, z których piszesz wiadomości, nie przekazują ich dalej. Bez przekaźników docierasz więc tylko do osób w bezpośrednim zasięgu. Każdy przekaźnik, który postawisz, rozszerza siatkę dla wszystkich wokół. Ten poradnik opiera się na firmware MeshCore w wersji v1.18.0.

Zanim zaczniesz, porozmawiaj ze swoją [lokalną grupą](/community/). Oni wiedzą, gdzie brakuje zasięgu, [który preset obowiązuje w twojej okolicy](/guides/settings/) i jak nazywać przekaźniki. Sprawdź na [mapach zasięgu](/map/), jakie przekaźniki są w pobliżu, i przywitaj się na publicznych lub lokalnych [kanałach](/guides/channels/).

## Wybierz miejsce {#site}

Wysokość wygrywa z mocą. LoRa na 868 MHz najlepiej rozchodzi się w czystej linii widoczności. Wzgórza, budynki i gęste drzewa zabierają znacznie więcej zasięgu, niż odzyska kilka dodatkowych miliwatów.

- **Idź wysoko.** Dach, maszt, wysoki budynek lub wzgórze pokrywają znacznie więcej niż parapet. Pomaga nawet kilka metrów ponad okolicznymi dachami.
- **Antena w wolnej przestrzeni.** Zamontuj ją powyżej krawędzi dachu, z dala od metalu, rynien i innych anten.
- **Sprawdź widok.** Narzędzia takie jak [HeyWhatsThat](https://www.heywhatsthat.com/) pokazują, co widać z danego miejsca. Jeśli widzisz jakiś punkt, przekaźnik tam stojący jest w zasięgu.
- **Zostaw zapas przestrzeni.** Droga radiowa potrzebuje wolnego miejsca wokół prostej linii, nie tylko samej linii. Na dużych odległościach środek trasy powinien mijać przeszkody z zapasem kilku metrów.
- **Zapytaj o zgodę.** Uzyskaj zgodę właściciela dachu lub masztu i ustal, jak będziesz dostawać się do przekaźnika w celu konserwacji.

## Sprzęt {#hardware}

- **Płytka.** Wybierz energooszczędną płytkę nRF52, na przykład [Heltec T114](/devices/), RAK WisBlock lub SenseCAP Solar Node. Płytki ESP32 pobierają więcej prądu (strona urządzeń oznacza je jako High), co utrudnia zasilanie słoneczne.
- **Antena.** Użyj anteny przeznaczonej na 868 MHz, zamontowanej pionowo. [Poradnik o antenach](/guides/antenna/) opisuje typy, złącza, kable i montaż. Zysk anteny wlicza się do prawnego limitu mocy, zobacz [Limity prawne](#legal).
- **Kabel.** Kabel koncentryczny trzymaj krótki albo użyj kabla o niskich stratach. Na 868 MHz kilka metrów cienkiego kabla może pochłonąć połowę mocy.
- **Obudowa.** Odporna na pogodę skrzynka (IP65 lub lepsza) z dławnicą kablową, otworem wentylacyjnym lub odpływowym przeciw skraplaniu, w jasnym kolorze lub z osłoną od słońca. Akumulatory źle znoszą upał, a poniżej zera nie da się ich ładować.
- **Piorun.** Antena na dachu to cel. Przestrzegaj lokalnych zasad uziemienia albo zamontuj ją tam, gdzie wyładowanie nie dosięgnie instalacji elektrycznej budynku.

## Zasilanie i dobór paneli słonecznych {#power}

Przekaźnik na energię słoneczną musi przetrwać najciemniejsze tygodnie zimy. Dobierz go pod nie:

1. **Zmierz pobór.** Podłącz skonfigurowany przekaźnik na dobę przez miernik mocy USB. Odczytaj zużytą energię w watogodzinach (Wh). Ruch w twojej okolicy wpływa na wynik, więc jeśli możesz, mierz na miejscu.
2. **Dodaj rezerwę.** Zaplanuj pojemność akumulatora na co najmniej 5 do 7 dni bez użytecznego słońca.
3. **Sprawdź zimowe słońce.** Bezpłatne unijne [narzędzie PVGIS](https://re.jrc.ec.europa.eu/pvg_tools/en/) pokazuje dla dowolnej lokalizacji, ile energii panel produkuje w każdym miesiącu. Weź miesiąc z najmniejszą ilością słońca.
4. **Dobierz panel.** Panel musi w tym najgorszym miesiącu uzupełniać dzienne zużycie, z zapasem na straty ładowania.

Przykład na założonych liczbach: przekaźnik zużywający 1 Wh dziennie potrzebuje akumulatora o pojemności co najmniej 7 Wh na tydzień rezerwy, czyli około 2 Ah użytecznej pojemności przy 3,7 V. Jeśli PVGIS podaje, że panel 1 W w twojej lokalizacji daje w grudniu 0,5 Wh dziennie, potrzebujesz panelu co najmniej 2 W, a 3 do 5 W zostawia margines na chmury, śnieg i starzenie.

## Konfiguracja {#config}

**Wgraj firmware.** Użyj [flashera webowego](https://flasher.meshcore.io) i wybierz firmware **Repeater** dla swojej płytki. Kroki wgrywania opisuje strona [Pierwsze kroki](/get-started/#flash).

**Skonfiguruj przez USB.** Gdy przekaźnik jest jeszcze podłączony do komputera, otwórz [config.meshcore.io](https://config.meshcore.io) lub konsolę flashera. Możesz też użyć dowolnego terminala szeregowego z prędkością 115200 baud. Najważniejsze polecenia:

| Co | Polecenie |
|---|---|
| Zmiana hasła administratora | `password <new password>` |
| Nadanie nazwy | `set name <name>` |
| Preset radia: częstotliwość, szerokość pasma, SF, CR (zastosuj przez restart) | `set radio 869.618,62.5,8,8` |
| Limit duty cycle, w procentach | `set dutycycle 10` |
| Moc nadawania układu radiowego, w dBm | `set tx <dBm>` |
| Pozycja, żeby przekaźnik pokazywał się na mapach | `set lat <degrees>` i `set lon <degrees>` |
| Dane kontaktowe dla innych operatorów | `set owner.info <text>` |
| Liczba godzin między ogłoszeniami flood, tymi, które słyszy cała siatka | `set flood.advert.interval <hours>` |
| Ogłoś przekaźnik teraz | `advert` |
| Restart | `reboot` |

Domyślne hasło administratora to `password`, a każdy, kto się nim zaloguje, zostaje administratorem. Zmień je, zanim przekaźnik zacznie nadawać.

Powyższy przykład `set radio` dotyczy presetu EU/UK (Narrow). Użyj zamiast niego wartości presetu dla swojej okolicy: [Zalecane ustawienia](/guides/settings/) podają je dla każdego kraju.

**Ustaw zegar.** Bez modułu zegara (RTC) przekaźnik traci czas przy każdej przerwie w zasilaniu i startuje w maju 2024. W trakcie pracy jego zegar też się rozjeżdża. Zaloguj się zdalnie z aplikacji i użyj `clock sync` albo ustaw czas przez USB. Moduł RTC to opłacalny dodatek do przekaźnika: utrzymuje czas podczas przerw w zasilaniu i rozjeżdża się znacznie mniej.

**Zarządzaj zdalnie.** Gdy przekaźnik jest już w siatce, zaloguj się z aplikacji MeshCore hasłem administratora. Odczytasz tam jego stan i użyjesz tych samych poleceń przez radio. Niektóre polecenia działają tylko przez USB, na przykład `set freq` i reset do ustawień fabrycznych `erase`.

Pełna lista poleceń znajduje się w [dokumentacji CLI MeshCore](https://github.com/meshcore-dev/MeshCore/blob/main/docs/cli_commands.md).

## Limity prawne {#legal}

{{< callout type="legal" verified="2026-10-02" >}}
Europejskie presety MeshCore leżą w podpaśmie **869.40-869.65 MHz**. W UE, Wielkiej Brytanii, Szwajcarii i Norwegii jest ono otwarte dla urządzeń krótkiego zasięgu bez licencji, w tych granicach:

- najwyżej **500 mW e.r.p.** mocy wypromieniowanej;
- najwyżej **10% duty cycle**: nie więcej niż 360 sekund nadawania w dowolnej godzinie, na urządzenie. Zamiast tego urządzenie może stosować nasłuch przed nadawaniem z adaptacyjną zmianą częstotliwości, zgodnie z ETSI EN 300 220-2;
- cały sygnał, o szerokości najwyżej 250 kHz, musi mieścić się w podpaśmie.

Pasmo jest współdzielone: nie wolno ci zakłócać służb licencjonowanych, a inni mogą zakłócać ciebie.
Radio musi mieć oznaczenie CE (w Wielkiej Brytanii CE lub UKCA).
{{< /callout >}}

Źródła: [Zalecenie CEPT ERC 70-03](https://docdb.cept.org/document/845),
załącznik 1, pasmo h1.7;
[Decyzja Komisji 2006/771/WE](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02006D0771(01)-20250123)
wraz ze zmianami;
[ETSI EN 300 220-2](https://www.etsi.org/deliver/etsi_en/300200_300299/30022002/03.03.01_60/en_30022002v030301p.pdf),
pasmo O.

### Moc: e.r.p. i twoja antena {#erp}

Limit dotyczy mocy *wypromieniowanej*, mierzonej względem prostej anteny dipolowej (e.r.p.). Zysk anteny się wlicza, straty w kablu się odejmują. Producenci podają zysk anteny w dBi, czyli o 2.15 dB więcej niż ten sam zysk w dBd (względem dipola). Utrzymuj tę sumę na poziomie 27 dBm (500 mW) lub niższym:

> moc nadawania (dBm) + zysk anteny (dBi) − straty w kablu (dB) − 2.15 ≤ 27

- Płytka nadająca 22 dBm do anteny 5 dBi przez kabel o stratach 1 dB:
  22 + 5 − 1 − 2.15 = 23.85 dBm, około 240 mW e.r.p. W granicach limitu.
- Płytka ze wzmacniaczem 30 dBm (1 W) do anteny 3 dBi:
  30 + 3 − 2.15 = 30.85 dBm, około 1.2 W e.r.p. Ponad limit; obniż moc nadawania.

`set tx` ustawia moc wyjściową układu LoRa, w dBm. Sam układ SX1262 kończy się na 22 dBm; firmware nie sprawdza wpisanej liczby. Płytki z dodatkowym wzmacniaczem, takie jak Heltec V4 lub Station G2, nadają ze znacznie większą mocą, niż ustawisz. Sprawdź tabelę producenta, zanim ją ustawisz, i zacznij od niskiej wartości.

### Duty cycle {#duty-cycle}

Przekaźnik nadaje dla wszystkich wokół, więc zużywa czas antenowy szybciej niż companion. Ogranicznik duty cycle w MeshCore ma domyślnie 50%, czyli więcej, niż pozwala to pasmo. Na każdym przekaźniku ustaw 10%:

```text
set dutycycle 10
```

### Dokładność częstotliwości {#frequency}

Kanał EU/UK (Narrow), 869.618 MHz z szerokością pasma 62.5 kHz, sięga aż do 869.649 MHz: niecały 1 kHz poniżej górnej granicy podpasma. Sygnał musi pozostać wewnątrz pasma w każdej temperaturze. Wymaga to kwarcu z kompensacją temperaturową (TCXO). Prawie każda obecna płytka go ma; starsze płytki bez niego, na przykład Heltec V2, dryfują za bardzo, żeby niezawodnie pracować przy 62.5 kHz.

### Uwagi dla krajów {#countries}

- **Państwa członkowskie UE** muszą udostępnić to podpasmo na tych warunkach (decyzja 2006/771/WE, art. 3).
- **Wielka Brytania:** te same limity, w dokumencie Ofcom [IR 2030](https://www.ofcom.org.uk/spectrum/radio-equipment/short-range-devices).
- **Szwajcaria i Liechtenstein:** te same limity, w dokumencie OFCOM [RIR1008-09](https://www.ofcomnet.ch/api/rir/1008/09).
- **Norwegia:** te same limity, w [rozporządzeniu o zezwoleniach ogólnych](https://lovdata.no/dokument/SF/forskrift/2012-01-19-77) (fribruksforskriften).

Te uwagi nie są poradą prawną. Przepisy się zmieniają. W razie wątpliwości sprawdź u swojego krajowego regulatora.

## Lista kontrolna uruchomienia {#checklist}

- [ ] Właściciel miejsca się zgodził i masz dostęp do przekaźnika w celu konserwacji.
- [ ] Płytka ma firmware **Repeater**, a antena była podłączona przed pierwszym włączeniem.
- [ ] Hasło administratora jest zmienione.
- [ ] Radio odpowiada [presetowi twojej okolicy](/guides/settings/) (`get radio`).
- [ ] Ustawiono `set dutycycle 10`.
- [ ] Moc nadawania plus zysk anteny mieści się w 500 mW e.r.p.
- [ ] Nazwa, pozycja i `owner.info` są ustawione, żeby inni wiedzieli, kto go prowadzi.
- [ ] Zegar jest ustawiony (`clock`).
- [ ] Obudowa jest szczelna, ma otwór odpływowy lub wentylacyjny, a kabel ma pętlę ociekową.
- [ ] Akumulator i panel są dobrane pod najgorszy zimowy miesiąc.
- [ ] Przed opuszczeniem miejsca przetestowano go z aplikacji z pewnej odległości.
- [ ] Twoja lokalna grupa wie, że działa.
