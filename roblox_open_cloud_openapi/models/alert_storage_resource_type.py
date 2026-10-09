from enum import Enum


class AlertStorageResourceType(str, Enum):
    UNIVERSE = "Universe"

    def __str__(self) -> str:
        return str(self.value)
