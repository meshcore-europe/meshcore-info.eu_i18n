---
title: Wygeneruj klucz
layout: keygen
lead: Nadaj swojemu przekaźnikowi prefiks, którego nie używa żaden przekaźnik w twojej okolicy. Znajdź wolny prefiks, utwórz klucz, który się od niego zaczyna, i ustaw go.
description: Utwórz w przeglądarce klucz MeshCore z wybranym przez siebie prefiksem, aby żaden przekaźnik w pobliżu nie miał w ścieżce tego samego prefiksu co twój.
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '009b5708'
  seeded: '2026-10-26'
  fields: {title: 'e798fa1b', lead: 'a855fdb1', description: 'e2c1d5de'}
  sections: ['009b5708']
---

Przekaźnik przekazuje wiadomości dalej dla wszystkich wokół. W ścieżce MeshCore
oznacza każdy przekaźnik pierwszymi bajtami jego klucza publicznego:
prefiksem. Gdy przekaźnik w twojej okolicy ma ten sam prefiks, ścieżka nie
pokazuje, który z nich przekazał wiadomość. MeshCore losuje klucz. Tutaj
utworzysz klucz z takim prefiksem, jaki chcesz.

Wybierz 2 bajty. 13 października 2026 [MeshCore Analyzer](https://meshcore-analyzer.eu/)
widział w Europie każdy prefiks 1-bajtowy jako współdzielony. Rozmiar hasha ścieżki,
ustawienie nadawcy, decyduje, ile bajtów każdego prefiksu trafia do ścieżki; zobacz [Polecenia CLI](/guides/cli/).
