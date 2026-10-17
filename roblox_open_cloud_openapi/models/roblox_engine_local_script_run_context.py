from enum import StrEnum


class RobloxEngineLocalScriptRunContext(StrEnum):
    CLIENT = "Client"
    LEGACY = "Legacy"
    PLUGIN = "Plugin"
    SERVER = "Server"

    def __str__(self) -> str:
        return str(self.value)
