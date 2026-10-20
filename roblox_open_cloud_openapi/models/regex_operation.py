from enum import StrEnum


class RegexOperation(StrEnum):
    GROUP = "Group"
    IGNORE = "Ignore"
    INVALID = "Invalid"

    def __str__(self) -> str:
        return str(self.value)
