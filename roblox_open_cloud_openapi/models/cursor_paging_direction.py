from enum import Enum


class CursorPagingDirection(str, Enum):
    BACKWARD = "Backward"
    FORWARD = "Forward"

    def __str__(self) -> str:
        return str(self.value)
