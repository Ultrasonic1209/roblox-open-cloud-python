from enum import StrEnum


class FeaturingStatus(StrEnum):
    DISABLED = "disabled"
    ENABLED = "enabled"

    def __str__(self) -> str:
        return str(self.value)
