---
tags: [architecture, advanced]
sources: [The Great Migration  Home Assistant Developer Docs.md]
created: 2026-05-05
updated: 2026-05-05
---

# Custom Component Overlays

Практика изменения или тестирования встроенных (built-in) интеграций [[Home Assistant]] путём их копирования в папку `custom_components`. 

После исторического рефакторинга ("The Great Migration"), система требует, чтобы при переопределении встроенного компонента копировались **абсолютно все** файлы из исходной папки интеграции (например, весь `homeassistant/components/hue/` в `custom_components/hue/`), даже если вы хотите изменить только один файл. Частичное переопределение файлов не поддерживается и приведет к ошибкам загрузки платформы.
