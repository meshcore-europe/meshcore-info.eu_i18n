---
title: Долучитися
lead: Цей посібник пишуть, перевіряють і перекладають волонтери. Ось як можна допомогти, з обліковим записом GitHub або без нього.
description: Додай свою спільноту, пристрій або проєкт, перевір переклад чи вдоскональ посібник на meshcore-info.eu.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'f3ed6e9b'
  seeded: '2026-11-02'
  fields: {title: '97b0c61b', lead: 'e9b40d4d', description: '3bd97cd2'}
  sections: ['6e9d4b61', 'aca796d7', 'd4848d5b', '247b2601', '8a60e0d4', '645c82d3', 'c755b654']
  blocks: ['2f9dd6e8', '44167907', 'b020e1a4', 'f2c726cd', '2e9d1fdd', 'b2a902ba', 'b15ce10b', '2be86888', '3db6cb63', '2e3c2fc0', '693a5d9d', '73e33897', '96d8689d', 'c67fd14a', 'f92f7e49', '12ddca6c', 'e947e2a9', '526df4bb', 'e0d3559e']
---

Усе, що є на цьому сайті, зберігається в публічному
[репозиторії GitHub](https://github.com/meshcore-europe/meshcore-info.eu). Для дрібних змін
заповни форму на GitHub (issue). Для більших змін створи pull request: це пропозиція
змін у файлах, яку переглядає супровідник. Супровідник перевіряє кожну зміну перед
публікацією.

Немає облікового запису GitHub? Напиши нам у [Discord](https://discord.meshcore-info.eu/) про
групу, якої бракує, помилковий факт або переклад, що звучить дивно. Далі цим займеться
волонтер.

## Додай свою спільноту {#community}

Ведеш місцеву групу MeshCore, до якої може приєднатися будь-хто? Заповни
[форму спільноти](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-community.yml):
вкажи назву, район і публічні посилання. Після додавання твоя група з'явиться
на сторінці [Місцеві групи](/community/) усіма мовами.

## Запропонуй пристрій або проєкт {#device-project}

На [сторінці пристроїв](/devices/) ми наводимо характеристики з документації виробників
і ніколи не даємо посилань на магазини. Запропонуй обладнання через
[форму пристрою](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-device.yml).
Створив застосунок, інструмент, міст або апаратну розробку для MeshCore із публічним
вихідним кодом? Додай свій проєкт через
[форму проєкту](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=add-project.yml).

## Перевір переклад {#translate}

Сторінки іншими мовами спочатку перекладає машина, і вгорі сторінки про це сказано.
Переклади зберігаються в окремому репозиторії,
[meshcore-info.eu_i18n](https://github.com/meshcore-europe/meshcore-info.eu_i18n), тому
тобі ніколи не доведеться торкатися коду сайту. Якщо добре знаєш одну з цих мов,
можеш покращити переклад:

1. Відкрий сторінку й перейди за посиланням «Допоможи покращити цей переклад». Так ти
   відкриєш файл на GitHub і зможеш редагувати його в браузері.
2. Виправ формулювання. Посилання, код, числа й назви на кшталт MeshCore залиш без жодних змін.
3. У блоці `translation` угорі заміни `status: ai` на
   `status: human` і запропонуй зміну.

Помітив неправильне слово, але не маєш часу його виправити? Повідом про нього через
[форму перекладу](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=translation-bug.yml).

## Покращ посібник {#guides}

Посібники ми спочатку пишемо англійською, а потім перекладаємо з неї. Виправлення
й нові теми надсилай через
[форму вмісту](https://github.com/meshcore-europe/meshcore-info.eu/issues/new?template=new-content.yml)
або pull request. Для фактів потрібне джерело: прошивка MeshCore та її
документація, регулятор радіозв'язку або виробник. Пиши власними словами. Можна навести
коротку цитату із зазначенням джерела.

У [посібнику для учасників](https://github.com/meshcore-europe/meshcore-info.eu/blob/main/CONTRIBUTING.md)
описано, як працювати над сайтом на власному комп'ютері.

## Стан перекладу {#coverage}

«Перевірено» означає, що текст перевірила людина; «Машинний» означає, що текст
переклала машина і його ще не перевірено; «Застарілий» означає, що англійський текст
змінився після створення перекладу; «Відсутній» означає, що сторінка ще не має перекладу.

{{< coverage >}}

## Подяки {#credits}

Сайт створено за допомогою [Astro](https://astro.build/). Він використовує шрифти
IBM Plex Sans та IBM Plex Mono за ліцензією SIL Open Font License. Переклади
відповідають
правилам [kiekr-i18n](https://github.com/marcelverdult/kiekr-i18n) і
використовують його глосарії MeshCore. Сам MeshCore розробляють у
[meshcore-dev/MeshCore](https://github.com/meshcore-dev/MeshCore).

Текст і переклади поширюються за ліцензією CC BY 4.0, а код за ліцензією MIT.
