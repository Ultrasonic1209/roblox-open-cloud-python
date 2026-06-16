from enum import Enum


class LuauExecutionSessionTaskErrorCode(str, Enum):
    DEADLINE_EXCEEDED = "DEADLINE_EXCEEDED"
    ERROR_CODE_UNSPECIFIED = "ERROR_CODE_UNSPECIFIED"
    INTERNAL_ERROR = "INTERNAL_ERROR"
    OUTPUT_SIZE_LIMIT_EXCEEDED = "OUTPUT_SIZE_LIMIT_EXCEEDED"
    SCRIPT_ERROR = "SCRIPT_ERROR"

    def __str__(self) -> str:
        return str(self.value)
