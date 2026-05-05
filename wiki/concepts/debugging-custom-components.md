---
tags: [debugging, development]
sources: [Building a Home Assistant Custom Component Part 5 Debugging.md]
created: 2026-05-05
updated: 2026-05-05
---

# Debugging Custom Components

Процесс поиска и устранения ошибок в пользовательских интеграциях ([[Home Assistant Custom Component]]).

Согласно лучшим практикам, вместо ручного копирования файлов на рабочий сервер и перезапуска Home Assistant, разработчикам следует использовать [[VS Code Devcontainer]]. Клонировав ядро системы и поместив свой компонент в папку `config/custom_components`, можно запускать локальную изолированную копию HA. Это дает доступ к полноценному графическому дебаггеру, где можно устанавливать точки останова (breakpoints) в коде Python и инспектировать переменные в реальном времени.
