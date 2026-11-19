from enum import StrEnum


class PerformanceEstimateResponsePredicted(StrEnum):
    BUDGET = "BUDGET"
    OUTCOME = "OUTCOME"

    def __str__(self) -> str:
        return str(self.value)
