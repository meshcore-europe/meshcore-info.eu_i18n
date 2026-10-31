---
title: Filtr pakietów
lead: 'Nie pozwól, by twój przekaźnik przekazywał śmieci: floody z daleka, bota, który nigdy nie milknie, hałaśliwy kanał. Najpierw wypróbuj ustawienie, potem je włącz.'
description: 'Filtr pakietów w firmware przekaźnika DMC: co odrzuca, gotowe ustawienia dla zwykłego i obciążonego przekaźnika, każde polecenie filtra z wartością domyślną oraz jak sprawdzić, co odrzucił.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'b07d39a8'
  seeded: '2026-10-31'
  fields: {title: '20a3ef1f', lead: 'd948682d', description: 'a8c57a9f'}
  sections: ['d06c9ddd', 'b1d9a8d1', '2dd3448d', 'ee64176e', 'a3cb880e', '09b568f0', 'a1a4fb68', '95fe64ae', 'dbac19c3', '05123b18', '3fa1bb28', 'e98b2285']
  blocks: ['b6231504', 'c66e4d9a', 'c0502fb4', 'fa699506', 'f7008037', '3acbb97b', '5e55d14c', 'bd024580', '68c8a4b1', '119fc5b9', '61804e40', '2fa7ebe8', '0610128b', 'a3cb880e', '0e6268be', 'e6d77222', 'f50be141', '2a1ae00c', '095e165f', 'd96efc68', 'b8a89bea', 'a29d0e87', 'c69ba7d1', 'f553d783', '1a83fda3', 'b6f87585', '64e2bbfa', 'dc79ca3a', '6ed9acff', 'd3701ccc', 'd4a25061', '22092611', '9184f977', 'f70c9e55', 'b2f0d9cb', 'c7b214c1', 'e8da9f3e', '0742c6c4', '7f2f59ae', '2789fc6d', 'ae920329', '7dd6f173', 'e1ca9ac7', 'ac11c47b', 'ec7913ae']
---

Przekaźnik (węzeł, który przekazuje wiadomości dalej) powtarza wszystko, co usłyszy.
W ruchliwej siatce obejmuje to też śmieci. Bot publikuje co minutę. Jeden węzeł
co kilka minut wysyła ponownie swoje ogłoszenie, czyli powitanie, dzięki któremu inni go znajdują.
Docierają wiadomości, które przebyły pół kraju. Każde powtórzenie zabiera
czas antenowy wszystkim wokół ciebie. Dzięki filtrowi pakietów twój przekaźnik
odrzuca taki ruch, zamiast go przekazywać. Jeśli chcesz najpierw sprawdzić, co zalewa twoją siatkę,
i co pomaga poza filtrem, zajrzyj na stronę
[Odporna siatka](/guides/resilient/).

{{< callout type="warning" >}}
Filtr pakietów jest częścią **firmware przekaźnika DMC**, czyli wersji
dla przekaźników z projektu [Dutch-MeshCore](https://github.com/Dutch-MeshCore/MeshCore). Standardowy
MeshCore nie ma filtra pakietów. Ma za to `region denyf *` i
`set flood.max.unscoped`, opisane na stronie [Polecenia CLI](/guides/cli/). Ten
poradnik opisuje wersję deweloperską 1.18.0 `ecfb2d4` z 19 października 2026. Stabilna
wersja 1.17.1 ma tylko filtry skoków, limitu, kanałów, hash i uszkodzonych pakietów.
Nie ma też trybu dry-run.
{{< /callout >}}

## Co robi filtr {#what}

Filtr sprawdza tylko pakiety, które twój przekaźnik przekazuje przez flood (wysyła
je do każdego węzła w zasięgu). Nigdy nie rusza tego, co twój przekaźnik wysyła
sam, ani pakietów, które idą znaną trasą do jednego węzła. Przechodzą też wiadomości prywatne
i zapytania od twoich kontaktów i do nich. Filtr może odrzucać:

- pakiety, które minęły już tyle przekaźników (skoków), ile dopuszczasz, osobno dla
  każdego typu pakietu;
- więcej pakietów jednego typu na minutę, niż dopuszczasz;
- ogłoszenie od węzła, który ogłaszał się już w ostatnich godzinach;
- wiadomości na kanale, który blokujesz;
- wszystko, co przyszło przez jeden przekaźnik, który blokujesz;
- wiadomości grupowe od jednego nadawcy lub z jednym słowem, albo tylko część z nich;
- wiadomości grupowe uszkodzone lub starsze, niż dopuszczasz.

Filtr jest **wyłączony**, dopóki go nie włączysz. Ustawiasz go poleceniami. Wpisz
je przez USB w [konsoli szeregowej](/firmware/console/) na tej stronie. Możesz też
wysłać je z aplikacji MeshCore, jak w
[poradniku przekaźnika](/repeater-guide/#config).

## Pobierz firmware {#firmware}

Wgraj **DutchMeshCore Repeater** za pomocą flashera w
[DutchMeshCore Toolbox](https://toolbox.dutchmeshcore.nl/). Firmware observera
ze strony [MQTT na twoim observerze](/guides/mqtt/) ma ten sam filtr.

## Najpierw wypróbuj {#dryrun}

W trybie dry-run filtr liczy każdy pakiet, który by odrzucił, ale nadal go
przekazuje. Tak dobierzesz ustawienie, zanim filtr cokolwiek odrzuci:

```text
filter on
filter dryrun on
```

Gdy dry-run jest włączony, wiersz stanu polecenia `filter` kończy się na `(dry-run)`. Liczniki
pokazują, co filtr by odrzucił. Zostaw go włączonego na dobę, potem je
sprawdź (zobacz [Co odrzucił](#stats)). Gdy liczby wyglądają dobrze, włącz
filtr naprawdę:

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
a uszkodzone wiadomości grupowe są odrzucane. Zwykła konfiguracja zapisana w samym
firmware dopuszcza 20 wiadomości prywatnych na minutę. Od floodu wiadomości prywatnych w lipcu 2026
ta strona przyjmuje 5, które zaleca firmware.

### Obciążony przekaźnik {#busy}

Dla przekaźnika w wysokim miejscu, który słyszy cały region, albo zalewanego floodem:

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

Ta konfiguracja zmniejsza o połowę liczbę wiadomości grupowych i ogłoszeń. Ogłoszenie każdego węzła
przechodzi raz na dobę. Odrzucane są wiadomości, które minęły już 16 przekaźników. Po
restarcie przechodzi jedno ogłoszenie od każdego węzła. Dokumentacja firmware ustawia tu też
`filter hash 2`. Ta strona to pomija (powód znajdziesz w
[Wszystkie ustawienia](#settings)).

### Zablokuj hałaśliwy kanał {#channel}

```text
filter channel add #bot
```

Twój przekaźnik nadal słyszy ten kanał. Nie przekazuje go już innym
przekaźnikom ani companionom (węzłom, z których ludzie piszą wiadomości). Maksymalnie 16 kanałów.

### Spowolnij jednego nadawcę {#sender}

Bot, który publikuje zbyt często na kanale, który chcesz zachować:

```text
filter watch add #test
filter sender add Bob 60
```

Wiadomości Boba na kanale Public i `#test` przechodzą teraz raz na minutę. Resztę
filtr odrzuca. Filtr dopasowuje nazwę w wiadomości, więc nadawca, który zmieni nazwę, go ominie.

### Zablokuj jeden przekaźnik po drodze {#path}

Gdy śmieci przychodzą przez jeden przekaźnik, zablokuj jego prefiks: początek
jego ID w zapisie szesnastkowym (hex). Potrzebujesz do tego wersji deweloperskiej 1.18. Wersja 1.17.1
nie ma filtra ścieżek.

```text
filter path add a1b2
filter path list
filter stats path
```

`filter path list` pokazuje blokowane prefiksy, a `filter stats path`, ile odrzucił
każdy z nich. `filter path remove a1b2` znowu go przepuszcza.
Krótki prefiks, taki jak `a1`, blokuje też każdy inny przekaźnik, którego ID zaczyna się
od `a1`. Używaj najdłuższego prefiksu, jaki możesz. Maksymalnie 8 prefiksów.

## Wszystkie ustawienia {#settings}

Typy pakietów mają numery. Na przekaźniku `filter types` pokazuje te same
numery z nazwami z firmware, takimi jak `TXT_MSG` i `GRP_TXT`:

| Numer | Typ | Numer | Typ |
| --- | --- | --- | --- |
| `00` | zapytanie | `06` | dane grupowe |
| `01` | odpowiedź | `07` | anonimowe zapytanie |
| `02` | wiadomość prywatna | `08` | ścieżka |
| `03` | potwierdzenie | `09` | trace |
| `04` | ogłoszenie | `10` | wieloczęściowy |
| `05` | wiadomość grupowa | `11` | sterowanie |

| Polecenie | Co robi | Domyślnie |
| --- | --- | --- |
| `filter on` / `filter off` | Włącza lub wyłącza filtr. | wył. |
| `filter dryrun on` / `off` | Liczy odrzucenia, ale nadal wszystko przekazuje. | wył. |
| `filter hops <type> <max>` | Odrzuca typ, który minął już tyle przekaźników, od 0 do 64. | 32 dla wiadomości grupowych, 8 dla reszty |
| `filter rate <type> <limit> <secs> [soft]` | Przepuszcza najwyżej `limit` pakietów danego typu na `secs`. Z `soft` przepuszczanie stopniowo maleje od `soft` do `limit`. `0` wyłącza limit. | 20 na 60 s dla wiadomości prywatnych i grupowych, 10 dla ogłoszeń, 5 dla reszty |
| `filter advert <hours>` | Przepuszcza ogłoszenie każdego węzła raz na tyle godzin, maksymalnie 720. | 0 (wył.) |
| `filter channel add <#name>` | Przestaje przekazywać kanał. | brak |
| `filter path add <hex>` | Odrzuca wszystko, co przyszło przez przekaźnik z tym prefiksem, od 2 do 8 cyfr hex. | brak |
| `filter sender add <name> [secs] [prob]` | Odrzuca wiadomości grupowe od nadawcy na kanale Public i obserwowanych kanałach. `Bot*` pasuje do każdej nazwy zaczynającej się od Bot. | brak |
| `filter text add <word> [secs] [prob]` | Odrzuca wiadomości grupowe zawierające słowo, na kanale Public i obserwowanych kanałach. `^word` pasuje tylko na początku. | brak |
| `filter watch add <#name>` | Reguły nadawcy i tekstu czytają też ten kanał, maksymalnie 4. Public jest czytany zawsze. | Public |
| `filter malformed on` / `off` | Odrzuca wiadomości z Public, które są puste, uszkodzone albo mają datę przesuniętą o ponad tydzień (sprawdzanie daty czeka na ustawienie zegara). | wył. |
| `filter age <minutes>` / `off` | Odrzuca wiadomości grupowe starsze niż ta wartość, na kanale Public i obserwowanych kanałach, od 1 do 10080. | wył. |
| `filter hash <bytes>` | Odrzuca pakiety z ID ścieżki krótszym niż ta wartość, od 1 do 3. | 1 |
| `filter reset` | Przywraca wszystkie ustawienia domyślne. | |

Każde `add` ma swoje `remove` i `list`, na przykład `filter channel remove #bot`.
W regułach nadawcy i tekstu `secs` przepuszcza jedną wiadomość na tyle sekund.
`prob` stosuje regułę tylko do takiego odsetka dopasowań, od 1 do 100. Maksymalnie 8
reguł nadawcy i 8 reguł tekstu. Nazwy i słowa rozróżniają wielkość liter. Nazwa ma maksymalnie
15 znaków, słowo maksymalnie 23.

Dwa ustawienia odrzucają więcej, niż możesz się spodziewać:

- `filter hash 2` odrzuca niemal cały ruch. Węzły domyślnie wysyłają
  1-bajtowe ID ścieżki.
- `filter age` polega na zegarze twojego przekaźnika. Ustaw go poleceniem `clock sync` z
  aplikacji, sprawdź poleceniem `clock` i zacznij z dużym zapasem: `filter age 60`.

Wszystkie ustawienia zostają zachowane po restarcie.

## Co odrzucił {#stats}

`filter` pokazuje sumy według powodu:

```text
> Filter on: Blocked [ Hops: 3 | Rate: 12 | Channel: 1 | Hash: 0 | Malformed: 2 ]
```

`filter stats <topic>` pokazuje szczegóły jednego ustawienia. Tematy to
`hops`, `rate`, `channel`, `hash`, `malformed`, `advert`, `path`, `sender`,
`text` i `age`. `filter stats top` pokazuje pierwszy bajt ID węzłów,
które odpowiadają za najwięcej odrzuceń. Wiele węzłów ma ten sam bajt.
`filter stats air` pokazuje czas antenowy, który twój przekaźnik zaoszczędził, nie przekazując tych
pakietów.

Liczniki zaczynają znowu od 0 po restarcie i po `clear stats`.
