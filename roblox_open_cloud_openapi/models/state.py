from enum import Enum


class State(str, Enum):
    ACTIVE = "Active"
    ARCHIVED = "Archived"
    UNSPECIFIED = "Unspecified"

    def __str__(self) -> str:
        return str(self.value)
