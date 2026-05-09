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
