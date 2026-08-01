from enum import Enum


class EventVisibility(str, Enum):
    MODERATED = "moderated"
    PRIVATE = "private"
    PUBLIC = "public"

    def __str__(self) -> str:
        return str(self.value)
