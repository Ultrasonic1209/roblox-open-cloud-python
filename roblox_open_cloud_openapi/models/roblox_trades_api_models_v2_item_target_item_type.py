from enum import StrEnum


class RobloxTradesApiModelsV2ItemTargetItemType(StrEnum):
    ASSET = "Asset"
    BUNDLE = "Bundle"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
