from enum import Enum


class LuauExecutionSessionTaskState(str, Enum):
    CANCELLED = "CANCELLED"
    COMPLETE = "COMPLETE"
    FAILED = "FAILED"
    PROCESSING = "PROCESSING"
    QUEUED = "QUEUED"
    STATE_UNSPECIFIED = "STATE_UNSPECIFIED"

    def __str__(self) -> str:
        return str(self.value)
