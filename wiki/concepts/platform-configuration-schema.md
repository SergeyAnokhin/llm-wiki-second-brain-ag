---
tags: [configuration, validation]
sources: [Building a Home Assistant Custom Component Part 1 Project Structure and Basics.md]
created: 2026-05-05
updated: 2026-05-05
---

# Platform Configuration Schema

Схема (обычно определяемая с помощью библиотеки `voluptuous` в Python), которая валидирует пользовательский ввод из `configuration.yaml` до того, как загрузится [[Home Assistant Custom Component]]. Она гарантирует, что обязательные поля (например, токены API) и дополнительные параметры имеют правильный формат.

*Примечание к современным практикам:* Хотя раньше настройка схемы через YAML была стандартом, для современных интеграций [[Home Assistant]] настоятельно рекомендуется использовать **Config Flow** (настройка через пользовательский интерфейс) вместо `configuration.yaml`.
