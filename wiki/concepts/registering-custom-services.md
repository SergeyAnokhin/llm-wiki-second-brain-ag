---
tags: [development, home-assistant, services]
sources: [Example Custom Config Repository]
created: 2026-05-05
updated: 2026-05-05
---

# Registering Custom Services

В [[Home Assistant]] компоненты могут предоставлять пользовательские службы (services), которые затем можно вызывать из автоматизаций, скриптов или пользовательского интерфейса (Developer Tools).

## Регистрация сервиса
Регистрация обычно происходит в функции `async_setup` или `async_setup_entry` с использованием `hass.services.async_register()`.

```python
async def async_setup(hass, config):
    async def my_service_handler(call):
        # Логика обработки вызова
        name = call.data.get("name", "World")
        hass.states.async_set("hello_world.greeting", f"Hello {name}")

    hass.services.async_register(
        "my_domain", "my_service", my_service_handler
    )
    return True
```

## Валидация входных данных
Для проверки передаваемых в сервис параметров используется библиотека `voluptuous` ([[Voluptuous Schema Validation]]). В функцию регистрации можно передать аргумент `schema=MY_SERVICE_SCHEMA`, чтобы HA автоматически отклонял некорректные вызовы.
