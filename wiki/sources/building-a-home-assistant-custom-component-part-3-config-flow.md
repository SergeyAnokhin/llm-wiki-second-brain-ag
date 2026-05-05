---
tags: [home-assistant, custom-component, config-flow, ui-configuration]
sources: [Building a Home Assistant Custom Component Part 3 Config Flow.md]
created: 2026-05-05
updated: 2026-05-05
---

# Building a Home Assistant Custom Component Part 3 Config Flow

**Источник:** Building a Home Assistant Custom Component Part 3 Config Flow.md
**Дата добавления:** 2026-05-05
**Тип:** статья

## Краткое содержание

В третьей части руководства описывается процесс перехода от конфигурации через YAML к настройке компонента через пользовательский интерфейс (UI) с использованием [[Config Flow]].

Для этого необходимо установить `"config_flow": true` в `manifest.json` и создать файл `config_flow.py` с классом, наследующим `ConfigFlow`. Рассматривается создание многошаговых форм ввода (шаг пользователя и шаг репозитория) с базовой валидацией, использованием файлов перевода ([[Home Assistant Translations]]) для вывода ошибок и тестированием потока с помощью [[pytest-home-assistant]].

## Ключевые утверждения

- Использование [[Config Flow]] является современным стандартом (Best Practice) для настройки интеграций через UI вместо YAML.
- В файле `__init__.py` необходимо реализовать `async_setup_entry`, который перенаправляет данные конфигурации в платформу сенсоров.
- Файлы переводов (например, `translations/en.json`) используются для отображения человекочитаемых строк и ошибок в UI.
- Фикстуры библиотеки [[pytest-home-assistant]] значительно упрощают написание unit-тестов для конфигурационного потока.

## Упомянутые сущности

- [[pytest-home-assistant]] — пакет для удобного unit-тестирования компонентов.

## Изученные концепции

- [[Config Flow]] — процесс настройки интеграций через UI Home Assistant.
- [[Home Assistant Translations]] — система локализации текстов и ошибок в UI.
