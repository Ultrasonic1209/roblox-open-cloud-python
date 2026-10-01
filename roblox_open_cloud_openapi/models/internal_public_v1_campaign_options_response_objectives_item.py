from enum import Enum


class InternalPublicV1CampaignOptionsResponseObjectivesItem(str, Enum):
    ENGAGEMENT = "ENGAGEMENT"
    PLAYS = "PLAYS"

    def __str__(self) -> str:
        return str(self.value)
