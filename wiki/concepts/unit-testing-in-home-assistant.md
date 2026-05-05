---
tags: [testing, python]
sources: [Building a Home Assistant Custom Component Part 2 Unit Testing and Continuous Integration.md]
created: 2026-05-05
updated: 2026-05-05
---

# Unit Testing in Home Assistant

Модульное тестирование пользовательских компонентов обычно выполняется с помощью фреймворка `pytest`.

Особенности:
- Для доступа к контексту системы используется плагин [[pytest-home-assistant]], который автоматически предоставляет фикстуру `hass` с настроенным инстансом Home Assistant.
- Поскольку Home Assistant активно использует [[Asynchronous Integration Setup]], тесты тоже пишутся как асинхронные (`async def test_...`).
- Для изоляции внешних вызовов (например, HTTP-запросов к API) широко применяется `AsyncMock`.
