from enum import StrEnum


class ResponseAccountState(StrEnum):
    INVALID = "Invalid"
    NORMAL = "Normal"
    OVERDUE = "Overdue"
    SUSPENDED = "Suspended"

    def __str__(self) -> str:
        return str(self.value)
