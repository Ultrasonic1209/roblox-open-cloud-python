from enum import StrEnum


class RevenueSummaryTimeFrame(StrEnum):
    DAY = "Day"
    MONTH = "Month"
    WEEK = "Week"
    YEAR = "Year"

    def __str__(self) -> str:
        return str(self.value)
