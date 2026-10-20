from enum import StrEnum


class GetAdsManagementV1CampaignOptionsObjective(StrEnum):
    ENGAGEMENT = "ENGAGEMENT"
    PLAYS = "PLAYS"

    def __str__(self) -> str:
        return str(self.value)
