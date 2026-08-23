from enum import Enum


class RobloxTradesApiModelsV2FreeTradesAllowanceResponseWindow(str, Enum):
    DAY = "day"
    LIFETIME = "lifetime"
    MONTH = "month"
    WEEK = "week"
    YEAR = "year"

    def __str__(self) -> str:
        return str(self.value)
