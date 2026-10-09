from enum import Enum


class AlertStorageEvaluationMode(str, Enum):
    ABSOLUTE = "Absolute"
    PERIOD_OVER_PERIOD = "PeriodOverPeriod"

    def __str__(self) -> str:
        return str(self.value)
