from enum import StrEnum


class AssetQuotaPeriod(StrEnum):
    DAY = "DAY"
    MONTH = "MONTH"
    PERIOD_UNSPECIFIED = "PERIOD_UNSPECIFIED"

    def __str__(self) -> str:
        return str(self.value)
