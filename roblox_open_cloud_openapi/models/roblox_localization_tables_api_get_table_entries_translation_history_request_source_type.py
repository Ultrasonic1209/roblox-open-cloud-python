from enum import Enum


class RobloxLocalizationTablesApiGetTableEntriesTranslationHistoryRequestSourceType(str, Enum):
    ASSETIMAGE = "AssetImage"
    INVALID = "Invalid"
    TEXT = "Text"

    def __str__(self) -> str:
        return str(self.value)
