from enum import StrEnum


class PingSignalLevel(StrEnum):
    HIGH = "High"
    LOW = "Low"
    MEDIUM = "Medium"

    def __str__(self) -> str:
        return str(self.value)
