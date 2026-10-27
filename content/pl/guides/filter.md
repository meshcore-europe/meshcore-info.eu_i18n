---
title: Filtr pakietów
lead: 'Nie pozwól, by twój przekaźnik przekazywał śmieci: floody z daleka, bota, który nigdy nie milknie, hałaśliwy kanał. Najpierw wypróbuj ustawienie, potem je włącz.'
description: 'Filtr pakietów w firmware przekaźnika DMC: co odrzuca, gotowe ustawienia dla zwykłego i obciążonego przekaźnika, każde polecenie filtra z wartością domyślną i jak sprawdzić, co odrzucił.'
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '2bf23d24'
  seeded: '2026-10-26'
  fields: {title: '20a3ef1f', lead: 'd948682d', description: 'a8c57a9f'}
  sections: ['0625daa2', 'b1d9a8d1', '2dd3448d', 'ee64176e', 'a3cb880e', '09b568f0', 'a1a4fb68', '95fe64ae', 'dbac19c3', 'ffc3f3a0', '3fa1bb28', '09511608']
---

Przekaźnik (węzeł, który przekazuje wiadomości dalej) powtarza wszystko, co usłyszy.
W ruchliwej siatce są w tym także śmieci. Bot pisze co minutę. Jeden węzeł co kilka
minut znów wysyła swoje ogłoszenie, czyli powitanie, dzięki któremu inni go znajdują.
Docierają wiadomości, które przebyły pół kraju. Każde powtórzenie zabiera czas antenowy
wszystkim wokół ciebie. Dzięki filtrowi pakietów twój przekaźnik odrzuca taki ruch
zamiast przekazywać go dalej.

{{< callout type="warning" >}}
Filtr pakietów jest częścią **firmware przekaźnika DMC**, czyli kompilacji dla
przekaźników od [Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore). Standardowy
MeshCore nie ma filtra pakietów; ma `region denyf *` oraz
`set flood.max.unscoped`, opisane na stronie [Polecenia CLI](/guides/cli/). Ten
przewodnik opiera się na kompilacji deweloperskiej 1.18.0 `ecfb2d4` z 19 października 2026.
Stabilna kompilacja 1.17.1 ma tylko filtry skoków, częstotliwości, kanału, skrótu
i uszkodzonych pakietów. Nie ma też trybu próbnego.
{{< /callout >}}

## Co robi filtr {#what}

Filtr sprawdza tylko pakiety, które twój przekaźnik przekazuje dalej floodem (wysyła
je do każdego węzła w zasięgu). Nigdy nie dotyka tego, co twój przekaźnik wysyła sam,
ani pakietów, które idą znaną trasą do jednego węzła. Wiadomości prywatne i zapytania
od twoich kontaktów i do nich także przechodzą. Filtr może odrzucić:

- pakiety, które przeszły już przez tyle przekaźników (skoków), ile dopuszczasz, osobno
  dla każdego typu pakietu;
- więcej pakietów jednego typu, niż dopuszczasz na minutę;
- ogłoszenie węzła, który ogłosił się już w ostatnich godzinach;
- wiadomości na kanale, który blokujesz;
- wszystko, co przyszło przez jeden blokowany przez ciebie przekaźnik;
- wiadomości grupowe od jednego nadawcy lub z jednym słowem, albo tylko część z nich;
- wiadomości grupowe, które są uszkodzone lub starsze, niż dopuszczasz.

Filtr jest **wyłączony**, dopóki go nie włączysz. Ustawiasz go poleceniami. Wpisujesz
je przez USB w [konsoli szeregowej](/firmware/console/) na tej stronie. Albo wysyłasz
je z aplikacji MeshCore, tak jak w
[przewodniku po przekaźniku](/repeater-guide/#config).

## Pobierz firmware {#firmware}

Wgraj **DutchMeshCore Repeater** z flashera w
[DutchMeshCore Toolbox](https://toolbox.dutchmeshcore.nl/). Firmware obserwatora
ze strony [MQTT na twoim obserwatorze](/guides/mqtt/) ma ten sam filtr.

## Najpierw wypróbuj {#dryrun}

W trybie próbnym filtr liczy każdy pakiet, który by odrzucił, ale nadal przekazuje go
dalej. Tak dobierzesz ustawienie, zanim filtr cokolwiek odrzuci:

```text
filter on
filter dryrun on
```

Gdy tryb próbny jest włączony, wiersz stanu polecenia `filter` kończy się na `(dry-run)`.
Liczniki pokazują, co filtr by odrzucił. Zostaw go na dzień, potem sprawdź liczniki
(zobacz [Co odrzucił](#stats)). Gdy liczby wyglądają dobrze, włącz filtr na ostro:

```text
filter dryrun off
```

## Zalecane konfiguracje {#configs}

### Zwykły przekaźnik {#typical}

```text
filter on
filter malformed on
filter rate 05 20 60
filter rate 02 5 60
filter hops 05 32
```

Wiadomości grupowe przechodzą do 20 na minutę, wiadomości prywatne do 5 na minutę,
a uszkodzone wiadomości grupowe są odrzucane. Własna zwykła konfiguracja firmware
dopuszcza 20 wiadomości prywatnych na minutę. Ta strona przyjmuje 5, które firmware
zaleca od floodu wiadomości prywatnych w lipcu 2026.

### Obciążony przekaźnik {#busy}

Dla przekaźnika na wysokim miejscu, który słyszy cały region, albo takiego, który jest
zalewany:

```text
filter on
filter malformed on
filter rate 05 10 60
filter rate 02 5 60
filter rate 04 5 60
filter advert 24
filter hops 05 16
filter hops 02 16
filter hops 04 8
```

To zmniejsza o połowę liczbę wiadomości grupowych i ogłoszeń, a ogłoszenie każdego
węzła przepuszcza raz dziennie. Odrzuca wiadomości, które przeszły już przez 16
przekaźników. Po ponownym uruchomieniu każdy węzeł przepuści jedno ogłoszenie. Własna
dokumentacja firmware ustawia tu także `filter hash 2`; ta strona to pomija (dlaczego,
zobacz w [Każde ustawienie](#settings)).

### Zablokuj hałaśliwy kanał {#channel}

```text
filter channel add #bot
```

Twój przekaźnik nadal słyszy ten kanał. Nie przekazuje go już dalej do innych
przekaźników i companionów (węzłów, z których ludzie piszą wiadomości). Do 16 kanałów.

### Przyhamuj jednego nadawcę {#sender}

Bot, który pisze za często na kanale, który chcesz zachować:

```text
filter watch add #test
filter sender add Bob 60
```

Wiadomości Boba na kanale Public i `#test` przechodzą teraz raz na minutę; resztę filtr
odrzuca. Filtr dopasowuje nazwę w wiadomości, więc nadawca, który zmieni nazwę, go ominie.

### Zablokuj jeden przekaźnik po drodze {#path}

Gdy śmieci przychodzą przez jeden przekaźnik, zablokuj jego prefiks: pierwszą część
jego ID, zapisaną szesnastkowo (hex).

```text
filter path add a1b2
```

Krótki prefiks, taki jak `a1`, blokuje także każdy inny przekaźnik, którego ID zaczyna
się od `a1`. Używaj najdłuższego prefiksu, jaki możesz. Do 8 prefiksów.

## Każde ustawienie {#settings}

Typy pakietów mają numery. Na przekaźniku `filter types` pokazuje te same numery
z nazwami używanymi przez firmware, takimi jak `TXT_MSG` i `GRP_TXT`:

| Numer | Typ | Numer | Typ |
| --- | --- | --- | --- |
| `00` | zapytanie | `06` | dane grupowe |
| `01` | odpowiedź | `07` | zapytanie anonimowe |
| `02` | wiadomość prywatna | `08` | ścieżka |
| `03` | potwierdzenie | `09` | trace |
| `04` | ogłoszenie | `10` | wieloczęściowy |
| `05` | wiadomość grupowa | `11` | sterujący |

| Polecenie | Co robi | Wartość domyślna |
| --- | --- | --- |
| `filter on` / `filter off` | Włącza lub wyłącza filtr. | wyłączony |
| `filter dryrun on` / `off` | Liczy odrzucenia, ale nadal przekazuje wszystko dalej. | wyłączony |
| `filter hops <type> <max>` | Odrzuca typ, który przeszedł już przez tyle przekaźników, od 0 do 64. | 32 dla wiadomości grupowych, 8 dla reszty |
| `filter rate <type> <limit> <secs> [soft]` | Przepuszcza najwyżej `limit` pakietów danego typu na `secs` sekund. Z `soft` przepuszczanie stopniowo maleje od `soft` do `limit`. `0` wyłącza limit. | 20 na 60 s dla wiadomości prywatnych i grupowych, 10 dla ogłoszeń, 5 dla reszty |
| `filter advert <hours>` | Przepuszcza ogłoszenie każdego węzła raz na tyle godzin, do 720. | 0 (wyłączony) |
| `filter channel add <#name>` | Przestaje przekazywać kanał dalej. | brak |
| `filter path add <hex>` | Odrzuca wszystko, co przyszło przez przekaźnik z tym prefiksem, od 2 do 8 cyfr szesnastkowych. | brak |
| `filter sender add <name> [secs] [prob]` | Odrzuca wiadomości grupowe od nadawcy, na kanale Public i kanałach obserwowanych. `Bot*` pasuje do każdej nazwy zaczynającej się od Bot. | brak |
| `filter text add <word> [secs] [prob]` | Odrzuca wiadomości grupowe zawierające słowo, na kanale Public i kanałach obserwowanych. `^word` pasuje tylko na początku. | brak |
| `filter watch add <#name>` | Pozwala regułom nadawcy i tekstu czytać także ten kanał, do 4. Public jest czytany zawsze. | Public |
| `filter malformed on` / `off` | Odrzuca wiadomości na Public, które są puste, uszkodzone lub mają datę przesuniętą o ponad tydzień (sprawdzanie daty czeka, aż zegar zostanie ustawiony). | wyłączony |
| `filter age <minutes>` / `off` | Odrzuca wiadomości grupowe starsze niż tyle minut, na kanale Public i kanałach obserwowanych, od 1 do 10080. | wyłączony |
| `filter hash <bytes>` | Odrzuca pakiety z krótszym ID ścieżki niż tyle bajtów, od 1 do 3. | 1 |
| `filter reset` | Przywraca każdemu ustawieniu wartość domyślną. | |

Każde `add` ma swoje `remove` i `list`, na przykład `filter channel remove #bot`.
W regułach nadawcy i tekstu `secs` przepuszcza jedną wiadomość na tyle sekund.
`prob` stosuje regułę tylko do takiego odsetka dopasowań, od 1 do 100. Do 8 reguł
nadawcy i 8 reguł tekstu. Nazwy i słowa rozróżniają wielkość liter; nazwa ma do 15
znaków, słowo do 23.

Dwa ustawienia odrzucają więcej, niż możesz się spodziewać:

- `filter hash 2` odrzuca niemal cały ruch. Węzły domyślnie wysyłają 1-bajtowe ID
  ścieżki.
- `filter age` ufa zegarowi twojego przekaźnika. Ustaw go poleceniem `clock sync`
  z aplikacji, sprawdź poleceniem `clock` i zacznij łagodnie: `filter age 60`.

Każde ustawienie zostaje zachowane po ponownym uruchomieniu.

## Co odrzucił {#stats}

`filter` pokazuje sumy według powodu:

```text
> Filter on: Blocked [ Hops: 3 | Rate: 12 | Channel: 1 | Hash: 0 | Malformed: 2 ]
```

`filter stats <topic>` pokazuje szczegóły jednego ustawienia. Tematy to
`hops`, `rate`, `channel`, `hash`, `malformed`, `advert`, `path`, `sender`,
`text` i `age`. `filter stats top` pokazuje pierwszy bajt ID węzłów, które stoją
za największą liczbą odrzuceń, to wskazówka, nie dowód.
`filter stats air` pokazuje czas antenowy, który twój przekaźnik oszczędził, nie
przekazując tych pakietów dalej.

Liczniki zaczynają znów od 0 po ponownym uruchomieniu i po `clear stats`.
