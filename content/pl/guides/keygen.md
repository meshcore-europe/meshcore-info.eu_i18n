---
title: Wygeneruj klucz
layout: keygen
lead: Daj swojemu przekaźnikowi prefiks, którego nie używa żaden przekaźnik w pobliżu. Znajdź wolny prefiks, utwórz klucz, który się od niego zaczyna, i ustaw go.
description: Utwórz w przeglądarce klucz MeshCore z wybranym prefiksem, aby żaden przekaźnik w pobliżu nie miał tego samego prefiksu w ścieżce.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '009b5708'
  seeded: '2026-10-31'
  fields: {title: 'e798fa1b', lead: 'a855fdb1', description: 'e2c1d5de'}
  sections: ['009b5708']
  blocks: ['843e44ff', '2586eaae']
---

Przekaźnik przekazuje wiadomości dalej dla wszystkich wokół siebie. MeshCore oznacza
w ścieżce każdy przekaźnik pierwszymi bajtami jego klucza publicznego.
To jego prefiks. Jeśli przekaźnik w pobliżu ma ten sam prefiks co twój, ze ścieżki nie
wynika, który z nich przekazał wiadomość. MeshCore wybiera klucz losowo. Tutaj
tworzysz klucz z prefiksem, który chcesz.

Wybierz 2 bajty. 13 października 2026 [MeshCore Analyzer](https://meshcore-analyzer.eu/)
wykazał, że w Europie każdy 1-bajtowy prefiks ma więcej niż jeden przekaźnik.
Rozmiar hasha ścieżki to ustawienie nadawcy. Od niego zależy, ile bajtów każdego
prefiksu trafia do ścieżki. Zobacz [polecenia CLI](/guides/cli/).
