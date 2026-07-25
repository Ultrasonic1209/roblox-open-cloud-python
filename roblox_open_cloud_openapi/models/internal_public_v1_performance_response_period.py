from enum import Enum


class InternalPublicV1PerformanceResponsePeriod(str, Enum):
    LAST_30_DAYS = "LAST_30_DAYS"
    LAST_7_DAYS = "LAST_7_DAYS"
    LAST_MONTH = "LAST_MONTH"
    PREVIOUS_YEAR = "PREVIOUS_YEAR"
    THIS_MONTH = "THIS_MONTH"
    TODAY = "TODAY"
    YEAR_TO_DATE = "YEAR_TO_DATE"
    YESTERDAY = "YESTERDAY"

    def __str__(self) -> str:
        return str(self.value)
