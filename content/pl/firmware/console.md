---
title: Konsola szeregowa
layout: console
lead: Wpisuj komendy do swojego przekaźnika z przeglądarki, przez USB.
description: Skonfiguruj przekaźnik, serwer pokoju lub czujnik MeshCore przez USB z Chrome, Edge lub Opery, dzięki konsoli szeregowej w przeglądarce. Bez instalowania programu.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: 'c33167ce'
  seeded: '2026-10-26'
  fields: {title: '4e3c41fa', lead: 'f0d52063', description: 'a2fe0704'}
  sections: ['c33167ce']
---

Przekaźnik (przekazuje wiadomości dalej), serwer pokoju (przechowuje wpisy dla grupy) i czujnik (wysyła odczyty) nie mają aplikacji, więc konfigurujesz je, wpisując komendy przez USB. Podłącz swój węzeł do komputera, otwórz tę stronę w Chrome, Edge lub Operze na komputerze i wybierz port swojego węzła. Konsola najpierw wysyła `get role` i `ver`, żeby wiedzieć, czym jest twój węzeł. Obie komendy tylko odczytują. Potem pokazuje, co odpowiada twój węzeł; wpisz komendę, na przykład `get name`, i naciśnij Enter. Podczas pisania konsola podpowiada komendy, które rozumie twój węzeł, a Tab uzupełnia pierwszą z nich.

Companion, czyli węzeł, z którego wysyłasz wiadomości, rozmawia z aplikacją przez USB. Jego wiersz poleceń znajdziesz w aplikacji MeshCore w wersji 1.50 lub nowszej.
