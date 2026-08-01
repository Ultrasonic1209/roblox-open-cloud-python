from enum import Enum


class FeaturingStatus(str, Enum):
    DISABLED = "disabled"
    ENABLED = "enabled"
    INVALID = "invalid"

    def __str__(self) -> str:
        return str(self.value)
