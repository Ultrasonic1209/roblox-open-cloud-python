from enum import StrEnum


class EventVisibility(StrEnum):
    MODERATED = "moderated"
    PRIVATE = "private"
    PUBLIC = "public"

    def __str__(self) -> str:
        return str(self.value)
