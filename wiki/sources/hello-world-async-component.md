---
tags: [code, home-assistant, basic, async]
sources: [__init__.py]
created: 2026-05-05
updated: 2026-05-05
---

# Hello World Async Component

**Источник:** __init__.py (из папки code)
**Дата добавления:** 2026-05-05
**Тип:** исходный код

## Краткое содержание

Простейший пример инициализации асинхронного пользовательского компонента `hello_world_async`. Содержит единственную функцию `async_setup`, которая жестко задает состояние сущности `hello_world_async.Hello_World` как `'Works!'` через `hass.states.async_set()`.

## Ключевые утверждения

- Для создания компонента, не имеющего платформ, достаточно файла `__init__.py` с функцией `async_setup`.
- Изменение состояния произвольной сущности может быть выполнено напрямую через `hass.states.async_set(entity_id, state)`.

## Изученные концепции

- [[Asynchronous Integration Setup]] — базовый пример `async_setup`.
