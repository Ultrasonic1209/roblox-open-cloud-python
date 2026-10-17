from enum import StrEnum


class LuauExecutionSessionTaskLogLogMessageMessageType(StrEnum):
    ERROR = "ERROR"
    INFO = "INFO"
    MESSAGE_TYPE_UNSPECIFIED = "MESSAGE_TYPE_UNSPECIFIED"
    OUTPUT = "OUTPUT"
    WARNING = "WARNING"

    def __str__(self) -> str:
        return str(self.value)
