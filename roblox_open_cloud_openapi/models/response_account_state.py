from enum import Enum


class ResponseAccountState(str, Enum):
    INVALID = "Invalid"
    NORMAL = "Normal"
    OVERDUE = "Overdue"
    SUSPENDED = "Suspended"

    def __str__(self) -> str:
        return str(self.value)
