from enum import Enum


class InternalPublicV1CreateCampaignRequestObjective(str, Enum):
    ENGAGEMENT = "ENGAGEMENT"

    def __str__(self) -> str:
        return str(self.value)
