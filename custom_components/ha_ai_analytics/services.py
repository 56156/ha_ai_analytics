from homeassistant.core import HomeAssistant, ServiceCall
from homeassistant.components import persistent_notification
import json
from .const import DOMAIN
from .storage import async_save_storage

async def async_setup_services(hass: HomeAssistant):
    async def clear_history(call: ServiceCall):
        hass.data[DOMAIN]["storage"]["history"] = []
        hass.data[DOMAIN]["storage"]["total_count"] = 0
        hass.data[DOMAIN]["storage"]["daily_count"] = 0
        await async_save_storage(hass.data[DOMAIN]["store"], hass.data[DOMAIN]["storage"])
        # 触发传感器更新
        for cb in hass.data[DOMAIN].get("update_callbacks", []):
            cb()
        persistent_notification.async_create(
            hass, "AI 交互历史已清空", "清空成功"
        )

    async def export_history(call: ServiceCall):
        data = hass.data[DOMAIN]["storage"]
        json_str = json.dumps(data["history"][-50:], ensure_ascii=False, indent=2)
        persistent_notification.async_create(
            hass, f"最近50条历史记录:\n{json_str}", "导出历史"
        )

    hass.services.async_register(DOMAIN, "clear_history", clear_history)
    hass.services.async_register(DOMAIN, "export_history", export_history)