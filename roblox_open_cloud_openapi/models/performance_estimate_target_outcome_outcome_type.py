from enum import StrEnum


class PerformanceEstimateTargetOutcomeOutcomeType(StrEnum):
    PLAYS = "PLAYS"

    def __str__(self) -> str:
        return str(self.value)
