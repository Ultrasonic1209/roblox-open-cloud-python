from enum import Enum


class AlertStorageAlertConfigState(str, Enum):
    DISABLED = "Disabled"
    ENABLED = "Enabled"
    ERROR = "Error"
    PAUSED_BY_ROBLOX = "PausedByRoblox"
    SYNCING = "Syncing"

    def __str__(self) -> str:
        return str(self.value)
