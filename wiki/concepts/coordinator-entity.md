---
tags: [development, python, architecture]
sources: [Entities examples from old project.md]
created: 2026-05-05
updated: 2026-05-05
---

# CoordinatorEntity

Базовый класс в [[Home Assistant]], предоставляемый модулем `homeassistant.helpers.update_coordinator`.

Используется совместно с `DataUpdateCoordinator` для оптимизации запросов к внешним API. Если несколько сенсоров зависят от одного и того же API, координатор выполняет один запрос, а все сущности, унаследованные от `CoordinatorEntity`, автоматически получают обновленные данные через вызов метода `_handle_coordinator_update()`. 

В проекте `camera_archiver` класс `ToCamera` использует множественное наследование: от `CoordinatorEntity` (для отслеживания обновлений файлов в памяти) и от базового класса `Camera`.
