from enum import StrEnum


class UniverseVisibility(StrEnum):
    PRIVATE = "PRIVATE"
    PUBLIC = "PUBLIC"
    VISIBILITY_UNSPECIFIED = "VISIBILITY_UNSPECIFIED"

    def __str__(self) -> str:
        return str(self.value)
