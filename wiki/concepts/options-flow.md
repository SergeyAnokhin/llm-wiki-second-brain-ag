---
tags: [configuration, ui]
sources: [Building a Home Assistant Custom Component Part 4 Options Flow.md]
created: 2026-05-05
updated: 2026-05-05
---

# Options Flow

Часть системы настройки Home Assistant, расширяющая [[Config Flow]]. Если Config Flow используется для первоначального добавления компонента, то Options Flow позволяет пользователю менять необязательные настройки позже (по кнопке "Настроить" в карточке интеграции).

Реализация:
1. В `config_flow.py` создается метод `async_get_options_flow` и класс `OptionsFlowHandler`.
2. Значения сохраняются в словарь `config_entry.options`.
3. Для применения новых настроек без перезагрузки системы в `__init__.py` добавляется слушатель (`options_update_listener`), который вызывает `hass.config_entries.async_reload` при обновлении формы.
