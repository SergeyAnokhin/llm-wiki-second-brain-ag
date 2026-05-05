---
tags: [code, home-assistant, entities, camera_archiver]
sources: [Entities examples from old project.md]
created: 2026-05-05
updated: 2026-05-05
---

# Entities Examples from Old Project

**Источник:** Entities examples from old project.md
**Дата добавления:** 2026-05-05
**Тип:** исходный код

## Краткое содержание

Архив старого кода компонента `camera_archiver`. Содержит реализацию трех платформ:
1. `camera.py` — кастомная камера, наследующая `Camera` и `CoordinatorEntity` ([[CoordinatorEntity]]). Изображения считываются из памяти (`MemoryStorage`).
2. `binary_sensor.py` — датчики активности для различных фаз пайплайна (перемещение файлов, загрузка).
3. `sensor.py` — набор сенсоров (`ConnectorSensor`), использующих паттерн "наблюдатель" для обновления состояния по кастомным событиям (`FileEventObject`, `StartEventObject`).

## Ключевые утверждения

- При использовании `DataUpdateCoordinator` сущности должны наследоваться от `CoordinatorEntity`, что позволяет им автоматически обновлять состояние при срабатывании `_handle_coordinator_update`.
- Использование шины событий внутри компонента позволяет отвязать логику получения данных от логики их отображения в сенсорах.
- Свойства сущностей, такие как `is_on` или `has_file`, динамически вычисляются на основе содержимого внутреннего хранилища.

## Изученные концепции

- [[CoordinatorEntity]] — класс для синхронизированного получения данных несколькими сущностями.
- [[Entity Class]] — примеры базовых классов (`SensorEntity`, `BinarySensorEntity`, `Camera`).
