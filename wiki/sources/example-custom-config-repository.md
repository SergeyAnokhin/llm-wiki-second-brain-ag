---
tags: [source, home-assistant, examples, custom-component]
sources: [home-assistant-example-custom-config.url]
created: 2026-05-05
updated: 2026-05-05
---

# Example Custom Config Repository

**Источник:** https://github.com/home-assistant/example-custom-config
**Тип:** Официальные примеры кода

## Краткое содержание
Официальная коллекция минималистичных примеров компонентов (`custom_components`) и скриптов (`python_scripts`) от команды Home Assistant. Эти примеры предназначены для того, чтобы разработчики могли скопировать их к себе и понять базовые принципы.

## Для чего нужен этот проект?
- Это шпаргалка по синтаксису и архитектуре простейших интеграций.
- Позволяет быстро стартовать, скопировав нужный пример (например, асинхронный сенсор) и модифицировав его под свои нужды.

## Разбор примеров (новое для нашей базы)

В репозитории представлены следующие ключевые шаблоны:
- `hello_world` и `hello_world_async` — базовые примеры инициализации компонента (синхронно и асинхронно). Задают состояние одной сущности.
- `example_light` и `example_sensor` — примеры реализации базовых сущностей (свет и сенсор). Показывают, как унаследовать классы `LightEntity` и `SensorEntity` и определить свойства (`is_on`, `state`).
- `expose_service_sync` и `expose_service_async` — [[Registering Custom Services]]. Отличные примеры того, как интеграция может добавлять свои собственные сервисы (например, вызов `my_domain.my_service`) в систему Home Assistant с валидацией входных параметров.
- `example_load_platform` — пример динамической загрузки платформы из основного компонента (`discovery.load_platform`).
- `mqtt_basic_sync` и `mqtt_basic_async` — примеры интеграции, которая подписывается на MQTT топик и реагирует на сообщения, обновляя состояние Home Assistant.
- `python_scripts` — примеры скриптов (`counter.py`, `count_people_home.py`), показывающие, как можно взаимодействовать с состояниями HA напрямую из Python-песочницы без создания полноценного компонента.

## Новые концепции для базы
- [[Registering Custom Services]] — регистрация собственных вызовов служб (services).
- [[Python Scripts in Home Assistant]] — использование песочницы python_scripts для простых автоматизаций.
