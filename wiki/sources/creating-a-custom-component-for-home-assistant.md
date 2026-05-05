---
tags: [home-assistant, custom-component, synchronous, switch]
sources: [Creating a custom component for home assistant.md]
created: 2026-05-05
updated: 2026-05-05
---

# Creating a Custom Component for Home Assistant

**Источник:** Creating a custom component for home assistant.md
**Дата добавления:** 2026-05-05
**Тип:** статья

## Краткое содержание

В статье описывается процесс создания простого синхронного компонента (на примере интеграции платы open433) для системы Home Assistant. 

Автор подробно разбирает структуру папок, создание файла `manifest.json`, объявление констант и схемы валидации (`voluptuous`) в `__init__.py`. В качестве платформы реализован файл `switch.py`, где класс устройства наследует `SwitchEntity`. Для управления жизненным циклом и взаимодействия с оборудованием используются события запуска/остановки системы (`EVENT_HOMEASSISTANT_START` и `EVENT_HOMEASSISTANT_STOP`).

## Ключевые утверждения

- Экземпляры пользовательских библиотек (для работы с "железом") хорошей практикой является сохранять в словаре `hass.data[DOMAIN]`, чтобы другие платформы компонента (например, сенсоры или выключатели) могли к ним обращаться.
- При разработке выключателя (Switch) класс должен наследоваться от `SwitchEntity` и обязательно реализовать свойства `is_on` и методы `turn_on` / `turn_off`.
- Изменения состояния в Home Assistant применяются вызовом `self.schedule_update_ha_state()`.

## Упомянутые сущности

- [[SwitchEntity]] — базовый класс для выключателей в Home Assistant.

## Изученные концепции

- [[Custom Component Structure]] — структура папок, рассматриваемая на примере `open433`.
