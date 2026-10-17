from enum import StrEnum


class RobloxLocalizationTablesApiEntryIdentifierEntryFormat(StrEnum):
    ICU = "Icu"
    INVALID = "Invalid"
    LEGACY = "Legacy"

    def __str__(self) -> str:
        return str(self.value)
