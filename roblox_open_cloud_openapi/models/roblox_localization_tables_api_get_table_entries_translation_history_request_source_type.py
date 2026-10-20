from enum import StrEnum


class RobloxLocalizationTablesApiGetTableEntriesTranslationHistoryRequestSourceType(StrEnum):
    ASSETIMAGE = "AssetImage"
    INVALID = "Invalid"
    TEXT = "Text"

    def __str__(self) -> str:
        return str(self.value)
