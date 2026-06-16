from enum import Enum


class CloudListLuauExecutionSessionTaskLogsView(str, Enum):
    FLAT = "FLAT"
    STRUCTURED = "STRUCTURED"
    VIEW_UNSPECIFIED = "VIEW_UNSPECIFIED"

    def __str__(self) -> str:
        return str(self.value)
