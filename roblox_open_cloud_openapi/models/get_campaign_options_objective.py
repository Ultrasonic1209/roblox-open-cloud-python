from enum import StrEnum


class GetCampaignOptionsObjective(StrEnum):
    ENGAGEMENT = "ENGAGEMENT"
    PLAYS = "PLAYS"
    ROBUX_SPEND = "ROBUX_SPEND"

    def __str__(self) -> str:
        return str(self.value)
