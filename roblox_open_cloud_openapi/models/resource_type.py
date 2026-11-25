from enum import StrEnum


class ResourceType(StrEnum):
    GROUP = "Group"
    INVALID = "Invalid"
    UNIVERSE = "Universe"

    def __str__(self) -> str:
        return str(self.value)
