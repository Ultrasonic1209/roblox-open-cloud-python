from enum import StrEnum


class AlertStorageAlertConfigState(StrEnum):
    DISABLED = "Disabled"
    ENABLED = "Enabled"
    ERROR = "Error"
    PAUSED_BY_ROBLOX = "PausedByRoblox"
    SYNCING = "Syncing"

    def __str__(self) -> str:
        return str(self.value)
