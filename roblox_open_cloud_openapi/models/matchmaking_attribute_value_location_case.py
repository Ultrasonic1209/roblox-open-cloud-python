from enum import StrEnum


class MatchmakingAttributeValueLocationCase(StrEnum):
    DATASTORELOCATION = "DataStoreLocation"
    INVALID = "Invalid"

    def __str__(self) -> str:
        return str(self.value)
