from enum import Enum


class InternalPublicV1CampaignOptionsResponseObjectivesItem(str, Enum):
    ENGAGEMENT = "ENGAGEMENT"

    def __str__(self) -> str:
        return str(self.value)
