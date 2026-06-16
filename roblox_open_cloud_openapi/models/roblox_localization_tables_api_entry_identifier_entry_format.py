from enum import Enum


class RobloxLocalizationTablesApiEntryIdentifierEntryFormat(str, Enum):
    ICU = "Icu"
    INVALID = "Invalid"
    LEGACY = "Legacy"

    def __str__(self) -> str:
        return str(self.value)
