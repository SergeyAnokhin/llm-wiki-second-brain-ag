---
tags: [async, performance]
sources: [Building a Home Assistant Custom Component Part 1 Project Structure and Basics.md]
created: 2026-05-05
updated: 2026-05-05
---

# Asynchronous Integration Setup

В экосистеме [[Home Assistant]] использование асинхронного кода (через модуль Python `asyncio`) критически важно во избежание блокировки основного цикла событий (event loop).

При инициализации платформы разработчикам следует использовать функцию `async_setup_platform` вместо `setup_platform`. Для получения данных класс сущности ([[Entity Class]]) должен реализовывать метод `async_update`. Внешние HTTP-запросы должны выполняться с использованием асинхронных библиотек, таких как `aiohttp`, а не синхронных вроде `requests`.
