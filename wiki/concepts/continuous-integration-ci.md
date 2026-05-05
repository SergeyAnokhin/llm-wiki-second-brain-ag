---
tags: [ci, automation]
sources: [Building a Home Assistant Custom Component Part 2 Unit Testing and Continuous Integration.md]
created: 2026-05-05
updated: 2026-05-05
---

# Continuous Integration (CI)

Практика автоматической сборки и тестирования кода. Для [[Home Assistant Custom Component]] типичный CI pipeline строится на базе [[GitHub Actions]] и включает в себя:
1. Проверку валидности компонента с помощью [[Hassfest]].
2. Запуск тестов ([[Unit Testing in Home Assistant]]) во всех поддерживаемых версиях Python.
Перед коммитом разработчики также используют локальный CI в виде [[Pre-commit]] хуков для форматирования кода.
