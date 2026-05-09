# Создание компонента Test Counter

Для реализации вашей задачи мы создадим простую интеграцию ([[Home Assistant Custom Component]]), которая содержит переключатель и сенсор. Переключатель будет обновлять счетчик, а сенсор будет отображать количество переключений.

В соответствии с [[Custom Component Structure]], вам необходимо создать следующую структуру папок и файлов в директории `config/custom_components/test_counter`:

```
test_counter/
├── __init__.py
├── manifest.json
├── sensor.py
└── switch.py
```

### 1. `manifest.json`
Этот файл содержит базовую информацию о компоненте.

```json
{
  "domain": "test_counter",
  "name": "Test Counter Component",
  "version": "1.0.0",
  "documentation": "https://github.com/example/test_counter",
  "dependencies": [],
  "codeowners": [],
  "requirements": [],
  "iot_class": "local_polling"
}
```

### 2. `__init__.py`
Файл инициализации компонента. Здесь мы будем использовать [[Asynchronous Integration Setup]] для подготовки переменной, которая будет хранить количество переключений.

```python
DOMAIN = "test_counter"

async def async_setup(hass, config):
    """Настройка компонента test_counter."""
    # Инициализация хранилища данных для домена
    hass.data.setdefault(DOMAIN, {"count": 0})
    return True
```

### 3. `switch.py`
Реализация переключателя, наследуемого от [[SwitchEntity]]. При каждом вызове методов `turn_on` и `turn_off` мы будем увеличивать счетчик и посылать сигнал об обновлении сенсору.

```python
from homeassistant.components.switch import SwitchEntity
from homeassistant.helpers.dispatcher import async_dispatcher_send

DOMAIN = "test_counter"
UPDATE_TOPIC = f"{DOMAIN}_update"

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Настройка платформы выключателя."""
    async_add_entities([TestCounterSwitch(hass)])

class TestCounterSwitch(SwitchEntity):
    """Класс тестового выключателя."""
    
    def __init__(self, hass):
        self.hass = hass
        self._is_on = False
        self._attr_name = "Test Switch"
        self._attr_unique_id = "test_counter_switch_1"

    @property
    def is_on(self):
        """Возвращает true, если выключатель включен."""
        return self._is_on

    async def async_turn_on(self, **kwargs):
        """Включает устройство."""
        self._is_on = True
        self._increment_and_notify()

    async def async_turn_off(self, **kwargs):
        """Выключает устройство."""
        self._is_on = False
        self._increment_and_notify()
        
    def _increment_and_notify(self):
        """Увеличивает счетчик и уведомляет сенсор об изменении."""
        self.hass.data[DOMAIN]["count"] += 1
        # Рассылка сигнала обновления для сенсора
        async_dispatcher_send(self.hass, UPDATE_TOPIC)
        self.async_write_ha_state()
```

### 4. `sensor.py`
Сенсор, который является наследником [[Entity Class]] (или `SensorEntity`). Он подписывается на сигнал об обновлении от переключателя.

```python
from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.dispatcher import async_dispatcher_connect

DOMAIN = "test_counter"
UPDATE_TOPIC = f"{DOMAIN}_update"

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Настройка платформы сенсора."""
    async_add_entities([TestCounterSensor(hass)])

class TestCounterSensor(SensorEntity):
    """Класс сенсора, считающего переключения."""
    
    def __init__(self, hass):
        self.hass = hass
        self._attr_name = "Test Switch Toggles"
        self._attr_unique_id = "test_counter_sensor_1"

    async def async_added_to_hass(self):
        """Вызывается при добавлении сущности в Home Assistant."""
        # Подписываемся на сигнал от выключателя
        self.async_on_remove(
            async_dispatcher_connect(
                self.hass, UPDATE_TOPIC, self.async_write_ha_state
            )
        )

    @property
    def native_value(self):
        """Возвращает текущее состояние сенсора (значение счетчика)."""
        return self.hass.data[DOMAIN].get("count", 0)
```

### 5. Конфигурация в `configuration.yaml`
Для того чтобы добавить эти устройства в систему, добавьте следующий код в `configuration.yaml` и перезагрузите Home Assistant:

```yaml
test_counter:

switch:
  - platform: test_counter

sensor:
  - platform: test_counter
```
