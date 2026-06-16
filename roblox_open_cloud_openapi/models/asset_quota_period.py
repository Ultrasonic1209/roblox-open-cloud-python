from enum import Enum


class AssetQuotaPeriod(str, Enum):
    DAY = "DAY"
    MONTH = "MONTH"
    PERIOD_UNSPECIFIED = "PERIOD_UNSPECIFIED"

    def __str__(self) -> str:
        return str(self.value)
