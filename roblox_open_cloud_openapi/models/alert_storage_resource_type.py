from enum import StrEnum


class AlertStorageResourceType(StrEnum):
    UNIVERSE = "Universe"

    def __str__(self) -> str:
        return str(self.value)
