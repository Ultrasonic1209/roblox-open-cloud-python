from enum import Enum


class RobloxTradesApiModelsV2ItemTargetItemType(str, Enum):
    ASSET = "Asset"
    BUNDLE = "Bundle"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
