---
title: Створи конфігурацію моста
lead: 'Надсилай те, що чує твій ретранслятор, на будь-який MQTT-брокер: власний або Analyzer. Дані надсилає комп''ютер, що стоїть поруч із ретранслятором.'
description: Запусти meshcoretomqtt на Raspberry Pi або іншому комп'ютері. Він надсилатиме те, що ретранслятор MeshCore чує, через USB на твій MQTT-брокер, на MeshCore Analyzer або на обидва.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'e0f7daa0'
  seeded: '2026-11-02'
  fields: {title: 'fd2dd667', lead: 'fa0c29ce', description: 'ed719ece'}
  sections: ['af5761f3', 'dca6b13e', '06316a22', '61b943e5', '55d5754a']
  blocks: ['af5761f3', '231a92ad', 'b80540ea', '46961e94', '51a4e1da', 'b066c819', 'b3d5ca4d', 'fb38b5f9', '7c1f4a97', '789a975f', 'a303d7b9', '04e0dbe0', '04087e05', 'cdaee24b', '2eaf18e9', '726148ad']
---

Ретранслятор (repeater) є вузлом, який передає повідомлення далі. Ти хочеш передавати його трафік на MQTT-брокер: на власний для панелі моніторингу чи бази даних або на брокер
[MeshCore Analyzer](https://meshcore-analyzer.eu/). Або в ретранслятора немає власного Wi-Fi, зате поруч із ним стоїть Raspberry Pi чи сервер.
Мостом є [meshcoretomqtt](https://github.com/Cisien/meshcoretomqtt), інструмент від спільноти:
він надсилає трафік із цього комп'ютера. Ретранслятор далі передає повідомлення, бо міст лише читає те, що той виводить у журнал через USB.

## Що тобі потрібно {#need}

- Ретранслятор, зібраний із журналюванням пакетів (див. нижче).
- Raspberry Pi Zero, 2, 3 або 4 чи будь-який комп'ютер із Linux або macOS, де є Python
  3.11 або новіший.
- USB-кабель для передавання даних між цими пристроями.

Стандартна прошивка ретранслятора з флешера не записує пакети в журнал. Збери
прошивку ретранслятора самостійно з
[вихідного коду MeshCore](https://github.com/meshcore-dev/MeshCore) і додай до збірки для своєї плати такий прапорець:

```text
-D MESH_PACKET_LOGGING=1
```

## Встановлення {#install}

Підключи ретранслятор до комп'ютера, а потім запусти на цьому комп'ютері інсталяційний скрипт meshcoretomqtt:

```text
curl -fsSL https://raw.githubusercontent.com/Cisien/meshcoretomqtt/main/install.sh | sudo bash
```

Скрипт встановлює міст як службу, що запускається разом із комп'ютером, і запитує,
на які брокери надсилати дані. Analyzer у цьому списку немає: ти додаси його у файлі конфігурації нижче. Твої власні налаштування зберігаються у
`/etc/mctomqtt/config.d/99-user.toml`, і оновлення ніколи не перезаписує цей файл.

## Брокери {#brokers}

Кожен брокер має власний блок `[[broker]]`, тому один ретранслятор може одночасно надсилати дані на кілька брокерів. Для власного брокера вкажи ім'я користувача та пароль або обійдися без входу
(`method = "none"`).
Натомість для MeshCore Analyzer потрібен токен, підписаний ключем твого ретранслятора:

- адреса `mqtt.meshcore-analyzer.eu`, порт `443`, через захищений вебсокет;
- аудиторія токена (audience) збігається з цією адресою.

## Твій файл конфігурації {#config}

Заміни вміст `/etc/mctomqtt/config.d/99-user.toml` на наведений нижче. Вкажи код найближчого до ретранслятора аеропорту (наприклад, `AMS`) і USB-порт, до якого підключено ретранслятор. Потім додай власний брокер. Блок, який тобі не потрібен, пропусти.

```toml
[general]
iata = "AMS"

[serial]
ports = ["/dev/ttyACM0"]

# Your own broker
[[broker]]
name = "my-broker"
enabled = true
server = "mqtt.example.org"
port = 1883

[broker.auth]
method = "password"
username = "my_username"
password = "my_password"

# The MeshCore Analyzer
[[broker]]
name = "meshcore-analyzer"
enabled = true
server = "mqtt.meshcore-analyzer.eu"
port = 443
transport = "websockets"

[broker.tls]
enabled = true
verify = true

[broker.auth]
method = "token"
audience = "mqtt.meshcore-analyzer.eu"
```

Після кожної зміни перезапускай службу (`sudo systemctl restart mctomqtt` у
Linux). Тоді твій ретранслятор з'явиться в Analyzer під власним іменем як спостерігач (observer), тобто вузол, який вивантажує те, що чує. Усі інші налаштування описано в
[README meshcoretomqtt](https://github.com/Cisien/meshcoretomqtt).
