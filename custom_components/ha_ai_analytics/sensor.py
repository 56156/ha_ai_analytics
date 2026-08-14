from homeassistant.components.sensor import SensorEntity
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.config_entries import ConfigEntry
from datetime import datetime
from collections import Counter

from .const import DOMAIN, SENSOR_TOTAL, SENSOR_TODAY, SENSOR_TOP_INTENT

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback):
    sensors = [
        TotalCommandsSensor(hass),
        TodayCommandsSensor(hass),
        TopIntentSensor(hass)
    ]
    async_add_entities(sensors, True)
    
    # 注册更新回调
    @callback
    def update_sensors():
        for sensor in sensors:
            sensor.async_schedule_update_ha_state(True)
    
    if "update_callbacks" not in hass.data[DOMAIN]:
        hass.data[DOMAIN]["update_callbacks"] = []
    hass.data[DOMAIN]["update_callbacks"].append(update_sensors)

class TotalCommandsSensor(SensorEntity):
    _attr_icon = "mdi:counter"
    _attr_unique_id = "ha_ai_total_commands"
    _attr_name = "AI 总指令数"

    def __init__(self, hass):
        self.hass = hass

    @property
    def native_value(self):
        return self.hass.data[DOMAIN]["storage"].get("total_count", 0)

class TodayCommandsSensor(SensorEntity):
    _attr_icon = "mdi:calendar-today"
    _attr_unique_id = "ha_ai_today_commands"
    _attr_name = "AI 今日指令数"

    def __init__(self, hass):
        self.hass = hass

    @property
    def native_value(self):
        return self.hass.data[DOMAIN]["storage"].get("daily_count", 0)

class TopIntentSensor(SensorEntity):
    _attr_icon = "mdi:chart-bar"
    _attr_unique_id = "ha_ai_top_intent"
    _attr_name = "AI 最常用意图"

    def __init__(self, hass):
        self.hass = hass

    @property
    def native_value(self):
        history = self.hass.data[DOMAIN]["storage"].get("history", [])
        if not history:
            return "无数据"
        intents = [h.get("intent", "unknown") for h in history[-100:]]  # 最近100条
        if not intents:
            return "无数据"
        return Counter(intents).most_common(1)[0][0]
    
    @property
    def extra_state_attributes(self):
        history = self.hass.data[DOMAIN]["storage"].get("history", [])
        return {
            "recent_commands": [h["text"] for h in history[-5:]],
            "last_updated": datetime.now().isoformat()
        }