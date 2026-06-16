from enum import Enum


class UniverseVisibility(str, Enum):
    PRIVATE = "PRIVATE"
    PUBLIC = "PUBLIC"
    VISIBILITY_UNSPECIFIED = "VISIBILITY_UNSPECIFIED"

    def __str__(self) -> str:
        return str(self.value)
