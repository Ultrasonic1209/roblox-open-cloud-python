from enum import Enum


class GetAdsManagementV1CampaignOptionsObjective(str, Enum):
    ENGAGEMENT = "ENGAGEMENT"
    PLAYS = "PLAYS"

    def __str__(self) -> str:
        return str(self.value)
