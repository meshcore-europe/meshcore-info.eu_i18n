---
title: Polecenia CLI
layout: cli
lead: Wszystkie polecenia przekaźnika, room servera, czujnika i companiona, pogrupowane według tego, co chcesz zrobić. Przeczytaj, co robi każde polecenie i od jakiej wartości startuje. Potem wpisz własną wartość i skopiuj polecenie.
description: 'Wszystkie polecenia firmware MeshCore 1.18.0 dla przekaźników, room serverów, czujników i companionów, pogrupowane według zadań: co robią, od jakiej wartości startuje firmware i które węzły je mają.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '15bdb6eb'
  seeded: '2026-10-31'
  fields: {title: 'a13cc6cb', lead: 'd051d3b4', description: '9a2dae75'}
  sections: ['15bdb6eb']
  blocks: ['8253bb3c', '66c83d82', '4f1b7c73', 'f28cf8b4']
---

Polecenia na tej stronie dotyczą firmware MeshCore 1.18.0. Spisaliśmy je z kodu źródłowego
firmware. Przy poleceniu dodanym w nowszej wersji podajemy, której wersji wymaga.
Przekaźnik przekazuje wiadomości dalej. Room server przechowuje wpisy dla grupy. Czujnik
wysyła odczyty. Room servery, czujniki i companiony mają wiele wspólnych poleceń.
Przy każdym poleceniu widzisz, które węzły je mają. Filtr „Który węzeł?” pokazuje
tylko polecenia twojego węzła.

Na przekaźniku, room serverze lub czujniku wpisujesz polecenia przez USB z komputera, na przykład w [konsoli szeregowej](/firmware/console/) na tej stronie. Aplikacja MeshCore wysyła je przez siatkę.
[Poradnik o przekaźniku](/repeater-guide/#config) opisuje oba sposoby.

Od wersji 1.18 companion (węzeł, z którego wysyłasz wiadomości, sparowany z telefonem lub laptopem albo
z własnym ekranem) też ma wiersz poleceń.
Otwórz Command Line w ustawieniach aplikacji MeshCore w wersji 1.50 lub
nowszej. Kontakt z uprawnieniem Remote CLI może wysyłać twojemu companionowi
te same polecenia przez siatkę. Dotyczy to także poleceń WiFi i PIN.

Wartość początkowa przy poleceniu to wartość przekaźnika. Room server, czujnik lub
companion może mieć inną wartość początkową. Polecenie, które ma tylko companion, podaje jego własną wartość.
