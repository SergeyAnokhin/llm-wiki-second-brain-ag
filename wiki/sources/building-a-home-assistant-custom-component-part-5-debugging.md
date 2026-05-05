---
tags: [home-assistant, debugging, devcontainer, vscode]
sources: [Building a Home Assistant Custom Component Part 5 Debugging.md]
created: 2026-05-05
updated: 2026-05-05
---

# Building a Home Assistant Custom Component Part 5 Debugging

**Источник:** Building a Home Assistant Custom Component Part 5 Debugging.md
**Дата добавления:** 2026-05-05
**Тип:** статья

## Краткое содержание

Заключительная часть руководства посвящена эффективной отладке ([[Debugging Custom Components]]) в локальной среде разработки без риска сломать "боевой" сервер умного дома. 

Автор описывает процесс использования [[VS Code Devcontainer]]: клонирование основного репозитория `home-assistant/core`, копирование своего компонента во внутреннюю папку `config/custom_components` и запуск встроенного дебаггера. Это позволяет разработчикам ставить точки останова (breakpoints) в Python-коде и инспектировать переменные во время работы компонента.

## Ключевые утверждения

- Разработка на рабочем (продакшн) сервере медленна и опасна; использование [[VS Code Devcontainer]] решает эту проблему.
- Встроенный отладчик VS Code позволяет ставить breakpoints и изучать состояние переменных (локальных и глобальных) в реальном времени.

## Упомянутые сущности

- [[VS Code Devcontainer]] — среда разработки в Docker-контейнере, преднастроенная командой Home Assistant.

## Изученные концепции

- [[Debugging Custom Components]] — процесс поиска ошибок и тестирования кода в изолированной, контролируемой среде.
