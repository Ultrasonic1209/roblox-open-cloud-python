from enum import StrEnum


class CreatorType(StrEnum):
    GROUP = "Group"
    INVALID = "Invalid"
    USER = "User"

    def __str__(self) -> str:
        return str(self.value)
