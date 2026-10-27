---
title: Polecenia CLI
layout: cli
lead: Każde polecenie twojego przekaźnika, serwera pokoju, czujnika lub companiona, pogrupowane według tego, co chcesz zrobić. Przeczytaj, co robi i jaką wartość ma na start, wpisz własną i skopiuj.
description: 'Każde polecenie firmware MeshCore 1.18.0 dla przekaźników, serwerów pokoju, czujników i companionów, pogrupowane według zadań: co robi, jaką wartość ma w firmware na start i które węzły je mają.'
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '15bdb6eb'
  seeded: '2026-10-26'
  fields: {title: 'a13cc6cb', lead: 'd051d3b4', description: '9a2dae75'}
  sections: ['15bdb6eb']
---

Te polecenia odpowiadają firmware MeshCore 1.18.0 i pochodzą ze źródeł firmware. Przy poleceniu dodanym w nowszej wersji podajemy, której wersji wymaga. Przekaźnik przekazuje wiadomości dalej, serwer pokoju przechowuje wpisy dla grupy, a czujnik zgłasza odczyty. Serwery pokoju, czujniki i companiony mają wiele wspólnych poleceń. Przy każdym poleceniu podajemy, które węzły je mają. „Który węzeł?” pokazuje tylko polecenia twojego węzła.

Do przekaźnika, serwera pokoju lub czujnika wpisujesz je przez USB z komputera, na przykład w [konsoli szeregowej](/firmware/console/) na tej stronie. Aplikacja MeshCore wysyła je przez siatkę. Oba sposoby opisujemy w [poradniku o przekaźniku](/repeater-guide/#config).

Od wersji 1.18 companion (węzeł, z którego piszesz wiadomości, sparowany z telefonem lub laptopem albo z własnym ekranem) też ma wiersz poleceń. Otwórz Command Line w ustawieniach aplikacji MeshCore w wersji 1.50 lub nowszej. Kontakt z uprawnieniem Remote CLI może wysłać twojemu companionowi te same polecenia przez siatkę. Dotyczy to też poleceń WiFi i PIN.

Wartość startowa polecenia to wartość przekaźnika. Serwer pokoju, czujnik lub companion może startować z inną wartością. Polecenie, które ma tylko companion, pokazuje swoją własną.
