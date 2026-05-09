---
tags: [synology, configuration, os]
sources: [Управление hibernation debug.md]
created: 2026-05-09
updated: 2026-05-09
---

# synoinfo.conf

Главный конфигурационный файл в операционной системе [[dsm|DSM]] на устройствах [[synology|Synology]]. Расположен по пути `/etc/synoinfo.conf`. 

В этом файле хранятся ключевые параметры работы системы, в том числе настройки отладки, такие как `enable_hibernation_debug` (для режима [[hibernation|Hibernation]]). Для безопасного внесения изменений в этот файл рекомендуется использовать утилиту [[synosetkeyvalue]].
