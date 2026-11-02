---
title: Създай конфигурация за мост
lead: 'Изпращай това, което репийтърът ти чува, към който и да е MQTT брокер: собствен или този на Analyzer. Изпращането поема компютър до репийтъра.'
description: Стартирай meshcoretomqtt на Raspberry Pi или друг компютър. Така изпращаш през USB това, което репийтър на MeshCore чува, към собствен MQTT брокер, към MeshCore Analyzer или към двата.
# Fixed a translation? Set status: human below, or the next change to the English page can overwrite your fix.
translation:
  status: ai
  source_hash: 'e0f7daa0'
  seeded: '2026-11-02'
  fields: {title: 'fd2dd667', lead: 'fa0c29ce', description: 'ed719ece'}
  sections: ['af5761f3', 'dca6b13e', '06316a22', '61b943e5', '55d5754a']
  blocks: ['af5761f3', '231a92ad', 'b80540ea', '46961e94', '51a4e1da', 'b066c819', 'b3d5ca4d', 'fb38b5f9', '7c1f4a97', '789a975f', 'a303d7b9', '04e0dbe0', '04087e05', 'cdaee24b', '2eaf18e9', '726148ad']
---

Репийтърът е възел, който препредава съобщенията. Искаш трафикът му да стига до MQTT
брокер: собствен за табло или база данни, или този на
[MeshCore Analyzer](https://meshcore-analyzer.eu/). Или репийтърът ти няма
собствен Wi-Fi, но до него има Raspberry Pi или сървър.
Мостът е [meshcoretomqtt](https://github.com/Cisien/meshcoretomqtt), инструмент от общността:
той изпраща трафика от този компютър. Репийтърът ти продължава да препредава,
защото мостът само чете лога, който репийтърът извежда през USB.

## Какво ти трябва {#need}

- Репийтър с фърмуер, компилиран със запис на пакетите в лог (виж по-долу).
- Raspberry Pi Zero, 2, 3 или 4, или всеки друг компютър с Linux или macOS, с Python
  3.11 или по-нов.
- USB кабел за данни между двете устройства.

Стандартният фърмуер за репийтър от инструмента за флашване не записва пакетите в лог.
Компилирай сам фърмуера за репийтър от
[изходния код на MeshCore](https://github.com/meshcore-dev/MeshCore), като добавиш
този флаг към компилацията за твоята платка:

```text
-D MESH_PACKET_LOGGING=1
```

## Инсталиране {#install}

Свържи репийтъра с компютъра, после стартирай на този компютър инсталационния
скрипт на meshcoretomqtt:

```text
curl -fsSL https://raw.githubusercontent.com/Cisien/meshcoretomqtt/main/install.sh | sudo bash
```

Скриптът инсталира моста като услуга, която се стартира заедно с компютъра, и те пита
към кои брокери да изпраща. Analyzer не е в този списък: добавяш го в
конфигурационния файл по-долу. Собствените ти настройки са в
`/etc/mctomqtt/config.d/99-user.toml`: обновяванията никога не презаписват този файл.

## Брокери {#brokers}

Всеки брокер има свой блок `[[broker]]`, затова един репийтър може да изпраща трафика си към няколко
едновременно. Собственият ти брокер приема потребителско име и парола или работи изобщо без вход
(`method = "none"`).
MeshCore Analyzer вместо това приема токен, подписан с ключа на репийтъра ти:

- адрес `mqtt.meshcore-analyzer.eu`, порт `443`, през защитен websocket;
- аудиторията на токена е същият адрес.

## Твоят конфигурационен файл {#config}

Замени съдържанието на `/etc/mctomqtt/config.d/99-user.toml` със следното. Впиши
кода на най-близкото до репийтъра летище (например `AMS`) и USB
порта, към който е свързан репийтърът. После добави собствения си брокер. Пропусни всеки блок,
който не ти трябва.

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

След промяна рестартирай услугата (`sudo systemctl restart mctomqtt` на
Linux). Тогава репийтърът ти се появява в Analyzer под собственото си име като наблюдател (observer): възел, който
качва това, което чува. В
[README на meshcoretomqtt](https://github.com/Cisien/meshcoretomqtt) ще намериш всички
останали настройки.
