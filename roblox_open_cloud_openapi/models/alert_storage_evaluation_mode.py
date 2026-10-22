from enum import StrEnum


class AlertStorageEvaluationMode(StrEnum):
    ABSOLUTE = "Absolute"
    PERIOD_OVER_PERIOD = "PeriodOverPeriod"

    def __str__(self) -> str:
        return str(self.value)
