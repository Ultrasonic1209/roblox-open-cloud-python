from enum import StrEnum


class CloudListLuauExecutionSessionTaskLogsView(StrEnum):
    FLAT = "FLAT"
    STRUCTURED = "STRUCTURED"
    VIEW_UNSPECIFIED = "VIEW_UNSPECIFIED"

    def __str__(self) -> str:
        return str(self.value)
