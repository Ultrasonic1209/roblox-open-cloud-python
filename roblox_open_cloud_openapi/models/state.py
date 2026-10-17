from enum import StrEnum


class State(StrEnum):
    ACTIVE = "Active"
    ARCHIVED = "Archived"
    UNSPECIFIED = "Unspecified"

    def __str__(self) -> str:
        return str(self.value)
