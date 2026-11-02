---
title: Створи ключ
layout: keygen
lead: Дай своєму repeater префікс, якого не використовує жоден repeater поблизу. Знайди вільний префікс, створи ключ, який із нього починається, і встанови цей ключ.
description: Створи ключ MeshCore із вибраним префіксом у браузері, щоб жоден repeater поблизу не мав такого самого префікса в шляху.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: '009b5708'
  seeded: '2026-11-02'
  fields: {title: 'e798fa1b', lead: 'a855fdb1', description: 'e2c1d5de'}
  sections: ['009b5708']
  blocks: ['843e44ff', '2586eaae']
---

Repeater передає повідомлення далі для всіх довкола. У шляху MeshCore
позначає кожен repeater першими байтами його публічного ключа:
це його префікс. Якщо в repeater поблизу такий самий префікс, зі шляху не видно,
який із двох передав повідомлення. MeshCore вибирає ключ випадково. Тут
ти створюєш ключ із потрібним тобі префіксом.

Бери 2 байти. 13 жовтня 2026 року [MeshCore Analyzer](https://meshcore-analyzer.eu/)
показав, що в Європі кожен 1-байтовий префікс мають кілька пристроїв. Розмір хешу шляху (налаштування відправника) визначає,
скільки байтів кожного префікса потрапляє у шлях; див. [команди CLI](/guides/cli/).
