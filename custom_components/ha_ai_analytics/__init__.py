from homeassistant.core import HomeAssistant, Event
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from datetime import datetime
import asyncio

from .const import DOMAIN, EVENT_CONVERSATION
from .storage import async_load_storage, async_save_storage
from .sensor import async_setup_entry as sensor_setup
from .services import async_setup_services

PLATFORMS = [Platform.SENSOR]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    # 加载存储数据
    data, store = await async_load_storage(hass)
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN]["storage"] = data
    hass.data[DOMAIN]["store"] = store
    hass.data[DOMAIN]["config"] = entry.data
    hass.data[DOMAIN]["exclude_words"] = entry.data.get("exclude_words", "").split(",")
    hass.data[DOMAIN]["max_entries"] = entry.data.get("max_entries", 200)

    # 监听对话事件
    async def handle_conversation(event: Event):
        text = event.data.get("text", "")
        # 过滤排除词
        exclude = hass.data[DOMAIN]["exclude_words"]
        if any(word in text for word in exclude):
            return
        
        # 解析意图（假设格式为 "turn_on_light" 之类的）
        intent = event.data.get("intent", {}).get("name", "unknown")
        
        new_entry = {
            "time": datetime.now().isoformat(),
            "text": text,
            "intent": intent,
            "success": event.data.get("success", False)
        }
        
        # 更新存储
        storage_data = hass.data[DOMAIN]["storage"]
        storage_data["history"].append(new_entry)
        storage_data["total_count"] = storage_data.get("total_count", 0) + 1
        
        # 每日计数（保留最近24小时）
        today = datetime.now().date().isoformat()
        daily_list = [h for h in storage_data["history"] if h["time"].startswith(today)]
        storage_data["daily_count"] = len(daily_list)
        
        # 限制历史记录数量
        max_entries = hass.data[DOMAIN]["max_entries"]
        if len(storage_data["history"]) > max_entries:
            storage_data["history"] = storage_data["history"][-max_entries:]
        
        await async_save_storage(hass.data[DOMAIN]["store"], storage_data)
        # 触发传感器更新
        for update_callback in hass.data[DOMAIN].get("update_callbacks", []):
            update_callback()

    hass.bus.async_listen(EVENT_CONVERSATION, handle_conversation)

    # 设置服务和传感器
    await async_setup_services(hass)
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    return await hass.config_entries.async_unload_platforms(entry, PLATFORMS)