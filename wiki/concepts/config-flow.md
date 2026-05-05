---
tags: [configuration, ui, modern-practices]
sources: [Building a Home Assistant Custom Component Part 3 Config Flow.md]
created: 2026-05-05
updated: 2026-05-05
---

# Config Flow

Механизм в [[Home Assistant]] для добавления и настройки интеграций прямо из пользовательского интерфейса (UI). Является современной альтернативой YAML-конфигурации ([[Platform Configuration Schema]]).

Для реализации Config Flow необходимо:
1. Включить поддержку: установить `"config_flow": true` в `manifest.json`.
2. Создать файл `config_flow.py` с классом, наследующим `ConfigFlow`.
3. Определить шаги конфигурации (например, `async_step_user`), которые возвращают формы для заполнения и валидируют пользовательский ввод.
4. В файле инициализации (`__init__.py`) обрабатывать переданную конфигурацию через функцию `async_setup_entry`.
