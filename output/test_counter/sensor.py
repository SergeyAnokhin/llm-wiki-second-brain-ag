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
