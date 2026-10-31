---
title: Uodpornij siatkę
lead: Siatka w twojej okolicy działa wolno albo zalewają ją śmieci? Sprawdź, co jest przyczyną, włącz ustawienie przekaźnika, które to zatrzymuje, i daj znać swojej lokalnej grupie.
description: 'Flood i spam w siatce MeshCore: jak rozpoznać każdy rodzaj, które ustawienie przekaźnika pomaga, jak zobaczyć flood i jak znaleźć jego źródło.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '500188ff'
  seeded: '2026-10-31'
  fields: {title: '33ec7ac8', lead: '780da19b', description: '1826e5e8'}
  sections: ['68ca5d36', '133c764a', 'a3bb5172', 'f4cc9cad', 'ace7b1ee', '89651002', 'f4dfdf59', '764c832c', 'f342b64b', 'f348e208']
  blocks: ['68ca5d36', 'c9cfbe6c', 'bcb31992', 'de7f60e4', 'e862fb9b', '0046b51f', '25f34d1d', 'c3c3ea52', '853a0f1d', '2bcea703', '871a7661', '2690aacf', 'a4aec3a1', 'd6da27c6', 'e8405458', 'f9150ee6', '8508ce40', '4b03ccd5', 'fb79c493', '695adde7', 'eba5a5b5', '836e0bac', '3497c5e8', '71c78fa1', '537d0930', '6a315252', '7c84dc56', '682e08e6', '258d7a27', '53af1400', '0dbebf97', 'ac0dca3c', '70fb4e9a', '9f055f50', 'ae90facc']
---

Wiadomości docierają z opóźnieniem albo wcale? Kanał Public zapełnia się
śmieciami? To flood: więcej ruchu, niż siatka jest w stanie przenieść.
Ktoś wysyła go przez pomyłkę albo celowo. Znajdź w tabelach poniżej to, co
widzisz. W każdym wierszu podajemy ustawienie, które to zatrzymuje. Włącz je
na swoim przekaźniku, czyli węźle, który przekazuje wiadomości dalej. Potem
daj znać swojej [lokalnej grupie](/community/), żeby przekaźniki wokół
ciebie zrobiły to samo. Każdy przekaźnik, który odrzuca flood, zostawia
czas antenowy dla wszystkich innych.

## Flood przez pomyłkę {#mistake}

Flood przez pomyłkę pochodzi z węzła, którego właściciel nie wie, że go
wywołuje. Ustaje, gdy właściciel się o tym dowie. Ogłoszenie w tabelach
poniżej to sygnał „cześć”, który węzeł wysyła, żeby inni mogli go znaleźć.

Ustawienia w tabelach wynikają z tego, co robi firmware. Nie każde z nich
zatrzymało już flood w prawdziwej siatce.

{{< callout type="warning" >}}
Niektóre ustawienia na tej stronie wymagają firmware DMC. Standardowy
**MeshCore** 1.18.0 ma regiony, limity skoków `flood.max.*`, wykrywanie
pętli i cykl pracy. Filtr pakietów, czyli reguły, dzięki którym twój
przekaźnik odrzuca śmieci, jest częścią **firmware DMC** od
[Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore). To samo
dotyczy blokowania według cyklu pracy i filtra companiona. Ta strona opisuje
wersję deweloperską DMC 1.18.0 `ecfb2d4` z 19 października 2026. Na stronie
[filtra pakietów](/guides/filter/#firmware) znajdziesz informację, skąd ją
pobrać.
{{< /callout >}}

| Co widzisz | Co to jest | Co pomaga |
| --- | --- | --- |
| Zapytania do przekaźników z jednego węzła, w dzień i w nocy, a siatka całymi dniami działa wolno | Automatyka domowa albo bot, który zbyt często pyta przekaźniki o ich status | `filter on`. Filtr pakietów przepuszcza wtedy 5 zapytań na minutę. Daj znać właścicielowi. |
| Ten sam rodzaj wiadomości na kanale, co minutę | Bot, który publikuje zbyt często | [Zablokuj kanał](/guides/filter/#channel) albo [spowolnij nadawcę](/guides/filter/#sender). Daj znać właścicielowi. |
| Nieczytelne wiadomości na kanale Public i innych kanałach | Węzeł z uszkodzonym firmware albo błędnymi ustawieniami radia | `filter malformed on` odrzuca je na kanale Public. Daj znać właścicielowi. |
| Ogłoszenie jednego węzła co kilka minut | Węzeł ustawiony tak, że wysyła ogłoszenia zbyt często | `filter advert 24` przepuszcza ogłoszenie każdego węzła raz na dobę. `set flood.max.advert 3` ogranicza ogłoszenia do 3 skoków. |
| Wiadomości z daleka, z regionami, które tu nie pasują | Most, który łączy siatki przez internet | `set flood.max.unscoped 1`. Przypisz też swój przekaźnik tylko do [regionów, które obsługuje](/guides/settings/#traffic). |
| Ta sama wiadomość przechodzi raz po raz, a ID twojego przekaźnika jest w jej ścieżce więcej niż raz | Przekaźnik, który zmienia pakiety i przekazuje je dalej, więc krążą w pętli | Wykrywanie pętli działa domyślnie na poziomie `minimal`. Po `set loop.detect moderate` przekaźnik odrzuca pętlę wcześniej. |

## Flood celowy {#purpose}

Część floodów to spam: śmieci wysyłane celowo, żeby zapchać siatkę. Nadawca
zmienia nazwy, klucze i ścieżki, więc żadna pojedyncza reguła nie zatrzyma
floodu.

| Co widzisz | Co to jest | Co pomaga |
| --- | --- | --- |
| Wiele nowych węzłów z losowymi nazwami, każdy z nowym kluczem | Fałszywe ogłoszenia | `filter rate 04 5 60` przepuszcza 5 ogłoszeń na minutę. `filter advert` nie pomaga: każde ogłoszenie pochodzi z [nowego klucza](#forged). |
| Wiadomości z nieczytelnym tekstem od zmyślonych nadawców, często z datą sprzed ponad roku | Spam na kanałach | `filter malformed on` odrzuca je na kanale Public. `filter age 60` odrzuca te ze starą datą na kanale Public i na [obserwowanych kanałach](/guides/filter/#settings). |
| Do 200 wiadomości prywatnych na minutę do nieistniejących węzłów, bez żadnych potwierdzeń w odpowiedzi | Flood wiadomości prywatnych | `filter rate 02 5 60`. Twoja aplikacja nie pokazuje tych wiadomości. Widzi je observer. |
| Serie zapytań z jednego węzła do dziesiątek innych | Spam zapytaniami | Przy `filter on` filtr pakietów przepuszcza 5 zapytań na minutę. |
| Wiadomość wraca po 10 do 20 minutach, z prawie tą samą ścieżką | Replay: ponownie wysłana kopia | Przekaźnik pamięta ostatnie 160 pakietów, które widział. W ruchliwej siatce późniejsza kopia przechodzi więc ponownie. `filter age` odrzuca wiadomość grupową starszą, niż pozwalasz. |
| Wiadomości z kanału Public wysłane ponownie pod zmyślonym nadawcą, czasem ze starą datą | Spam echem | `filter age 60`. `filter malformed on` odrzuca też datę przesuniętą o ponad tydzień. |
| Co kilka sekund wiadomość na kilku kanałach, za każdym razem od nowej nazwy, ze zwykłymi pytaniami | Fala botów | `filter rate 05 10 60`. [Zablokuj też kanały](/guides/filter/#channel), których twoja okolica nie używa. Każda nazwa jest nowa, więc [reguły nadawcy](#forged) jej nie łapią. |

## Co zadziałało {#worked}

Lokalne grupy zatrzymały floody tymi krokami:

1. **Daj znać właścicielowi.** Flood przez pomyłkę ustaje, gdy właściciel
   się o nim dowie. Napisz do niego życzliwą wiadomość.
2. **Nie reaguj w siatce.** Odpowiedź pokazuje spamerowi, że spam działa.
3. **Poproś o observery.** Observer to węzeł, który zgłasza przez MQTT
   każdy usłyszany pakiet. Im więcej observerów wokół ciebie, tym szybciej
   widzisz, którędy flood wchodzi do siatki. Swój przekaźnik zmienisz w
   observera dzięki [MQTT na observerze](/guides/mqtt/).
4. **Znajdź źródło.** Observery wskazują obszar, w którym jest nadawca.
   Ostatni kilometr wymaga ludzi, którzy pójdą pieszo z radiem. Zobacz
   [Znajdź źródło](#source).
5. **Zmobilizuj swoją lokalną grupę.** Jeden przekaźnik z właściwymi
   ustawieniami pomaga. Wszystkie przekaźniki w okolicy razem zatrzymują
   flood. Twoja [lokalna grupa](/community/) przekona każdego właściciela,
   żeby włączył to ustawienie.

## Zmyśleni nadawcy i ścieżki {#forged}

Te części pakietu wpisuje nadawca i nic ich nie sprawdza:

- **Nazwa nadawcy.** W wiadomości na kanale nazwa jest częścią tekstu.
  Każdy, kto ma klucz kanału, może wpisać dowolną nazwę.
- **Początek ścieżki.** Każdy przekaźnik dopisuje swoje ID na końcu
  ścieżki. Nic nie sprawdza ID, które były tam wcześniej, więc nadawca może
  zacząć ścieżkę od zmyślonych. Koniec ścieżki jest prawdziwy.

{{< forged-path >}}

Dlatego `filter sender` i `filter path` zatrzymują nadawcę tylko do chwili,
gdy zmieni nazwę albo ścieżkę. [Blokada ścieżki](/guides/filter/#path)
odrzuca też prawdziwy ruch przekaźnika, którego ID w niej jest. Limity
częstotliwości, limity skoków, sprawdzanie wieku i poprawności, blokady
kanałów, regiony i cykl pracy działają dalej.

## Ustawienia na każdy flood {#always}

Te ustawienia działają bez względu na to, co zalewa siatkę:

- **Cykl pracy 10%.** Twój przekaźnik nigdy wtedy nie nadaje dłużej, niż
  pozwala prawo, cokolwiek do niego dociera. Opisuje to
  [poradnik przekaźnika](/repeater-guide/#duty-cycle).
- **Regiony i limity skoków.** Region to obszar, w którym wiadomość
  zostaje. Przekaźnik przekazuje dalej tylko wiadomości z regionów, do
  których należy, a `flood.max.*` trzyma ruch blisko. Oba opisuje strona
  [Ogranicz ruch](/guides/settings/#traffic).
- **Filtr pakietów dla ruchliwego przekaźnika.**
  [Gotowe ustawienia](/guides/filter/#busy) zmniejszają o połowę liczbę
  wiadomości grupowych i ogłoszeń. Najpierw wypróbuj je w trybie
  [dry-run](/guides/filter/#dryrun): ten tryb tylko liczy, co by odrzucił.
- **Filtr companiona, w firmware DMC.** Twój companion, czyli węzeł, z
  którego piszesz, nie wpuszcza śmieci do aplikacji. Ukrywa uszkodzone i
  stare wiadomości oraz wiadomości od zablokowanego przez ciebie przekaźnika
  lub nadawcy albo z zablokowanym słowem. Reguła nadawcy albo słowa
  ukrywa wiadomość tylko przed tobą. Inni nadal ją dostają.

### Blokowanie według cyklu pracy {#gate}

W firmware DMC twój przekaźnik może dawać pierwszeństwo własnemu regionowi,
gdy ma dużo pracy. Gdy nadawał przez ponad 35% ostatniej minuty, przestaje
przekazywać wiadomości bez regionu. Jeśli nadal jest zajęty, odrzuca potem
najszerszy region, po jednym poziomie naraz. Własny region przechodzi
zawsze. Działa to tylko wtedy, gdy masz ustawione regiony na przekaźniku.
Włącz to i sprawdź:

```text
set dc.gate on
get dc.gate.status
```

{{< dc-gate >}}

To, co ta funkcja odrzuca, nie pojawia się w `filter stats`. Gdy na
przekaźniku znów jest spokojnie, regiony wracają, od najbardziej
wewnętrznego.

## Zobacz flood {#see}

Twoja aplikacja pokazuje tylko to, co do ciebie dociera. Flood wiadomości
prywatnych do nieistniejących węzłów słyszy tylko observer. Każdy observer
przesyła dane do [MeshCore Analyzer](https://meshcore-analyzer.eu/), gdzie
każdy może je zobaczyć. Swój przekaźnik zmienisz w observera dzięki
[MQTT na observerze](/guides/mqtt/).

W Analyzerze przejrzyj wszystkie kopie jednego pakietu. Jego ścieżka
zwykle pokazuje, skąd przyszedł. Flooder może zacząć ścieżkę od
[zmyślonych ID](#forged), więc pierwsze ID nic ci nie mówią. Każda kopia
ma jednak ten sam zmyślony początek. Kopia z najkrótszą ścieżką przeszła
przez najmniej prawdziwych przekaźników, więc usłyszano ją najbliżej
nadawcy.

{{< copies >}}

Na swoim przekaźniku `filter stats` pokazuje, co odrzucił filtr pakietów.
`filter stats top` pokazuje pierwszy bajt ID węzłów, które stoją za
większością odrzuceń. Wiele węzłów ma ten sam bajt, więc zawęża to
poszukiwania, ale nie wskazuje nadawcy.

## Znajdź źródło {#source}

Gdy flood wciąż powraca:

1. **Prześledź ścieżki.** Czytaj ścieżkę od końca: ostatnie ID to
   przekaźniki, przez które przeszedł flood. Najwcześniejsze prawdziwe ID
   jest blisko źródła. ID przed nim mogą być [zmyślone](#forged).
2. **Zawęź obszar.** Kilka observerów, które słyszą ten sam pakiet,
   wskazuje obszar, w którym jest nadawca.
   [DMC Triangulator](https://triangulator.dutchmeshcore.nl/) wylicza go
   na podstawie przekaźników, które usłyszały pakiet.
3. **Przejdź ostatni kilometr.** Przekaźniki słyszą źródło tylko na
   granicy swojego zasięgu, więc ostatni odcinek wymaga ludzi, którzy
   pójdą pieszo. [Mesh-Hunter](https://mesh-hunter.eu/) łączy się z twoim
   companionem i zapisuje każdy usłyszany pakiet razem z twoją pozycją
   GPS. Kilka osób, które szukają jednocześnie, znajdzie źródło szybciej.
4. **Daj znać swojej [lokalnej grupie](/community/).** Grupa widzi więcej
   z siatki, decyduje o dalszych krokach i kontaktuje się z tym, kto
   celowo wywołuje flood.

## Dodaj, co widziałeś {#add}

Trafił cię flood, którego nie ma
w tych tabelach? Jakieś ustawienie go zatrzymało? Napisz do nas na
[Discord](https://discord.meshcore-info.eu/): co widziałeś i co
włączyłeś. Dodamy to do strony.
