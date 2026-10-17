from enum import StrEnum


class CursorPagingDirection(StrEnum):
    BACKWARD = "Backward"
    FORWARD = "Forward"

    def __str__(self) -> str:
        return str(self.value)
