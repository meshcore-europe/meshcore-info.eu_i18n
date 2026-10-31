---
title: Konsola szeregowa
layout: console
lead: Wpisuj polecenia dla swojego przekaźnika w przeglądarce, przez USB.
description: Skonfiguruj przekaźnik, room server albo czujnik MeshCore przez USB w Chrome, Edge lub Operze. Konsola szeregowa działa w przeglądarce i niczego nie musisz instalować.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'c33167ce'
  seeded: '2026-10-31'
  fields: {title: '4e3c41fa', lead: 'f0d52063', description: '5d53ba06'}
  sections: ['c33167ce']
  blocks: ['13e02e98', '81b697e3']
---

Przekaźnik (przekazuje wiadomości dalej), room server (przechowuje posty grupy)
ani czujnik (wysyła odczyty) nie mają aplikacji. Konfigurujesz je więc, wpisując
polecenia przez USB. Podłącz węzeł do komputera i otwórz tę stronę na komputerze
w Chrome, Edge lub Operze. Potem wybierz port swojego węzła. Konsola najpierw
wysyła `get role` i `ver`, żeby rozpoznać twój węzeł. Oba polecenia tylko
odczytują dane. Potem konsola pokazuje, co odpowiada twój węzeł. Wpisz polecenie,
na przykład `get name`, i naciśnij Enter. Podczas pisania konsola podpowiada
polecenia, które rozumie twój węzeł. Klawisz Tab wstawia pierwszą podpowiedź.

Companion, czyli węzeł, z którego wysyłasz wiadomości, łączy się natomiast przez USB z aplikacją. Jego wiersz poleceń znajdziesz w
aplikacji MeshCore w wersji 1.50 lub nowszej.
