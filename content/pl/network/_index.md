---
title: Sieć
layout: network
lead: Zobacz siatkę w całej Europie i pomóż jej widzieć więcej. Obserwatory słyszą siatkę i zgłaszają to, co odbierają. Każdy nowy pokazuje trochę więcej.
description: 'Jak siatka MeshCore w Europie staje się widoczna: obserwatory zgłaszają to, co słyszą, do MeshCore Analyzer. Liczby na żywo i sposób na dodanie własnego obserwatora.'
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '90bef266'
  seeded: '2026-10-31'
  fields: {title: '1b32d67c', lead: '382c041f', description: '0dcdc2ac'}
  sections: ['90bef266']
  blocks: ['535ce3c7', 'dee00f8d', '23271f25']
---

Sama siatka niczego nie zapisuje: wiadomość przechodzi od węzła do węzła i
znika. To, co widzisz na [mapach zasięgu](/map/) i w statystykach, pochodzi
od obserwatorów. Obserwator to węzeł, który dodatkowo zgłasza przez MQTT to, co słyszy,
za pośrednictwem Wi-Fi lub internetu. Zgłoszenie płynie tylko w jedną stronę:
nic nie wraca do siatki. Przekaźnik (węzeł, który przekazuje wiadomości dalej)
z firmware obserwatora nadal przekazuje wiadomości tak jak wcześniej.

Obserwatory w całej Europie wysyłają zgłoszenia do [MeshCore Analyzer](https://meshcore-analyzer.eu/)
pod adresem mqtt.meshcore-analyzer.eu. Analyzer odczytuje też inne brokery,
więc obserwator podłączony do nich również się liczy. Na podstawie tych
zgłoszeń Analyzer tworzy mapy, statystyki i [listę kanałów](/guides/channels/) na tej stronie.

{{< callout type="tip" >}}
Siatce nic z tego nie jest potrzebne. Narzędzia pomagają ci tylko ją zobaczyć i zaplanować. Zgłoszenia obserwatorów, Analyzer, te mapy
i narzędzia działają przez internet. Gdy zabraknie prądu lub internetu, przestają działać.
Siatka dalej przekazuje wiadomości drogą radiową, przez każdy przekaźnik, który
wciąż ma zasilanie, na przykład przez te na energię słoneczną.
{{< /callout >}}
