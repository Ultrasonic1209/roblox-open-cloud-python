from enum import StrEnum


class MusicChartType(StrEnum):
    CURRENT = "Current"
    MONTH = "Month"
    NONE = "None"
    WEEK = "Week"
    YEAR = "Year"

    def __str__(self) -> str:
        return str(self.value)
