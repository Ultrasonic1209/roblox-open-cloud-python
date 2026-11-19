from enum import StrEnum


class PerformanceEstimateOutcomeOutcomeType(StrEnum):
    PLAYS = "PLAYS"

    def __str__(self) -> str:
        return str(self.value)
