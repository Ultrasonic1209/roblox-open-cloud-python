from enum import StrEnum


class PerformanceEstimateCampaignContextObjective(StrEnum):
    PLAYS = "PLAYS"

    def __str__(self) -> str:
        return str(self.value)
