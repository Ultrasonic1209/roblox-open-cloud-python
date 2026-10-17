from enum import StrEnum


class GetV1LocalizationTableTablesTableIdEntriesEntryFormat(StrEnum):
    ICU = "Icu"
    INVALID = "Invalid"
    LEGACY = "Legacy"

    def __str__(self) -> str:
        return str(self.value)
