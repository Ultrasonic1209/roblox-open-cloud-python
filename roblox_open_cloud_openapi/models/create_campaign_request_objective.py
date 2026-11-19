from enum import StrEnum


class CreateCampaignRequestObjective(StrEnum):
    ENGAGEMENT = "ENGAGEMENT"
    PLAYS = "PLAYS"
    ROBUX_SPEND = "ROBUX_SPEND"

    def __str__(self) -> str:
        return str(self.value)
