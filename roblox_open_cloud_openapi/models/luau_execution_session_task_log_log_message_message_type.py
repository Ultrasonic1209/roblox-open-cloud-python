from enum import Enum


class LuauExecutionSessionTaskLogLogMessageMessageType(str, Enum):
    ERROR = "ERROR"
    INFO = "INFO"
    MESSAGE_TYPE_UNSPECIFIED = "MESSAGE_TYPE_UNSPECIFIED"
    OUTPUT = "OUTPUT"
    WARNING = "WARNING"

    def __str__(self) -> str:
        return str(self.value)
