from homeassistant.helpers.storage import Store
from .const import STORAGE_KEY, STORAGE_VERSION

async def async_load_storage(hass):
    store = Store(hass, STORAGE_VERSION, STORAGE_KEY)
    data = await store.async_load()
    if data is None:
        data = {"history": [], "total_count": 0, "daily_count": 0}
    return data, store

async def async_save_storage(store, data):
    await store.async_save(data)