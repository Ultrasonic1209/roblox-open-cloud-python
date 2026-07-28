from enum import Enum


class GetAdsManagementV1CampaignOptionsObjective(str, Enum):
    ENGAGEMENT = "ENGAGEMENT"

    def __str__(self) -> str:
        return str(self.value)
