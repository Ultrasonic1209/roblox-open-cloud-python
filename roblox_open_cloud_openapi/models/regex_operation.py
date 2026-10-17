from enum import Enum


class RegexOperation(str, Enum):
    GROUP = "Group"
    IGNORE = "Ignore"
    INVALID = "Invalid"

    def __str__(self) -> str:
        return str(self.value)
