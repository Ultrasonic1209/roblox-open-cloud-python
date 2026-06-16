from enum import Enum


class RobloxEngineScriptRunContext(str, Enum):
    CLIENT = "Client"
    LEGACY = "Legacy"
    PLUGIN = "Plugin"
    SERVER = "Server"

    def __str__(self) -> str:
        return str(self.value)
