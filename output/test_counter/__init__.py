DOMAIN = "test_counter"

async def async_setup(hass, config):
    """Настройка компонента test_counter."""
    # Инициализация хранилища данных для домена
    hass.data.setdefault(DOMAIN, {"count": 0})
    return True
