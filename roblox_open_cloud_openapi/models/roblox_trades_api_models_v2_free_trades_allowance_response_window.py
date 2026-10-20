from enum import StrEnum


class RobloxTradesApiModelsV2FreeTradesAllowanceResponseWindow(StrEnum):
    DAY = "day"
    LIFETIME = "lifetime"
    MONTH = "month"
    WEEK = "week"
    YEAR = "year"

    def __str__(self) -> str:
        return str(self.value)
