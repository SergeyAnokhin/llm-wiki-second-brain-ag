---
tags: [architecture, python]
sources: [Building a Home Assistant Custom Component Part 1 Project Structure and Basics.md]
created: 2026-05-05
updated: 2026-05-05
---

# Entity Class

Класс Python, расширяющий базовый класс `homeassistant.helpers.entity.Entity`. Он представляет состояние и данные об устройстве или сервисе внутри пользовательского компонента ([[Home Assistant Custom Component]]).

Ключевые зоны ответственности обычно включают:
- Свойство `state`: Возвращает основное состояние сенсора.
- Свойство `device_state_attributes` (или `extra_state_attributes` в более новых версиях): Возвращает дополнительные метаданные.
- Метод `async_update`: Периодически вызывается системой [[Home Assistant]] (с интервалом, заданным константой `SCAN_INTERVAL`) для загрузки новых данных с использованием асинхронных вызовов ([[Asynchronous Integration Setup]]).
