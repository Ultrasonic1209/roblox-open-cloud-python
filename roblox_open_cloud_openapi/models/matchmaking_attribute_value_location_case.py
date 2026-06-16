from enum import Enum


class MatchmakingAttributeValueLocationCase(str, Enum):
    DATASTORELOCATION = "DataStoreLocation"
    INVALID = "Invalid"

    def __str__(self) -> str:
        return str(self.value)
