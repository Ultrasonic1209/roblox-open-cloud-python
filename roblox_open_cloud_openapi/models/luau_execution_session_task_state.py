from enum import StrEnum


class LuauExecutionSessionTaskState(StrEnum):
    CANCELLED = "CANCELLED"
    COMPLETE = "COMPLETE"
    FAILED = "FAILED"
    PROCESSING = "PROCESSING"
    QUEUED = "QUEUED"
    STATE_UNSPECIFIED = "STATE_UNSPECIFIED"

    def __str__(self) -> str:
        return str(self.value)
