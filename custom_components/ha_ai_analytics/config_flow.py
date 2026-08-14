import voluptuous as vol
from homeassistant import config_entries
from .const import DOMAIN, DEFAULT_MAX_ENTRIES

class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        errors = {}
        if user_input is not None:
            return self.async_create_entry(title="AI 交互分析", data=user_input)
        
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Optional("max_entries", default=DEFAULT_MAX_ENTRIES): 
                    vol.All(vol.Coerce(int), vol.Range(min=10, max=1000)),
                vol.Optional("exclude_words", default=""): str,
            })
        )