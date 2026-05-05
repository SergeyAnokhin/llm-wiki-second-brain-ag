---
tags: [tools, formatting, linting]
sources: [Building a Home Assistant Custom Component Part 2 Unit Testing and Continuous Integration.md]
created: 2026-05-05
updated: 2026-05-05
---

# Pre-commit

Фреймворк для управления и поддержки хуков (hooks), запускающихся перед выполнением `git commit`. Для разработки [[Home Assistant Custom Component]] шаблон [[Cookiecutter]] поставляет преднастроенный файл `.pre-commit-config.yaml`, который автоматически проверяет код линтерами (black, flake8, isort), чтобы он соответствовал высоким стандартам ядра Home Assistant.
