"""Device automation exceptions."""
from homeassistant.exceptions import HomeAssistantError


class InvalidDeviceAutomationConfig(HomeAssistantError):
    """When device automation config is invalid."""
