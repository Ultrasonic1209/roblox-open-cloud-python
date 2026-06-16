from enum import Enum


class RevenueSummaryTimeFrame(str, Enum):
    DAY = "Day"
    MONTH = "Month"
    WEEK = "Week"
    YEAR = "Year"

    def __str__(self) -> str:
        return str(self.value)
