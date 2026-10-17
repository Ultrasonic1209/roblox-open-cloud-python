from enum import StrEnum


class CloudGetLuauExecutionSessionTaskView(StrEnum):
    BASIC = "BASIC"
    FULL = "FULL"
    VIEW_UNSPECIFIED = "VIEW_UNSPECIFIED"

    def __str__(self) -> str:
        return str(self.value)
