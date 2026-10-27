---
title: Sieć
layout: network
lead: Zobacz siatkę w całej Europie i pomóż jej widzieć więcej. Obserwatorzy słuchają siatki i zgłaszają, co słyszą, a każdy nowy pokazuje trochę więcej.
description: 'Jak siatka MeshCore w Europie staje się widoczna: obserwatorzy zgłaszają do MeshCore Analyzer to, co słyszą. Liczby na żywo i jak dodać własnego obserwatora.'
# Fixed the wording? Set status to human, or a change to the English there can replace your fix.
translation:
  status: ai
  source_hash: '05fa5ea3'
  seeded: '2026-10-26'
  fields: {title: '1b32d67c', lead: '382c041f', description: '0dcdc2ac'}
  sections: ['05fa5ea3']
---

Sama siatka nic nie zapisuje: wiadomość przechodzi z węzła do węzła i znika.
To, co widzisz na [mapach zasięgu](/map/) i w statystykach, pochodzi od
obserwatorów. Obserwator to węzeł, który dodatkowo zgłasza przez MQTT, co słyszy,
przez WiFi lub internet. Zgłoszenie idzie w jedną stronę: nic nie wraca do
siatki. Przekaźnik (węzeł, który przekazuje wiadomości dalej) z firmware obserwatora
nadal przekazuje je tak jak wcześniej.

Obserwatorzy w całej Europie zgłaszają dane do [MeshCore Analyzer](https://meshcore-analyzer.eu/)
pod adresem mqtt.meshcore-analyzer.eu. Analyzer czyta też inne brokery, więc
obserwator zgłaszający tam również się liczy. Z tych zgłoszeń Analyzer buduje mapy,
statystyki i [listę kanałów](/guides/channels/) na tej stronie.

{{< callout type="tip" >}}
Siatka nic z tego nie potrzebuje. Zgłoszenia obserwatorów, Analyzer, te mapy
i narzędzia działają przez internet. Gdy zabraknie prądu lub padnie internet, przestają działać. Siatka
dalej przekazuje wiadomości drogą radiową, przez każdy przekaźnik, który nadal ma
zasilanie, na przykład te na panelach słonecznych. Narzędzia służą do oglądania i planowania
siatki, nie do jej działania.
{{< /callout >}}
