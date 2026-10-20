from enum import StrEnum


class InternalPublicV1CampaignOptionsResponseObjectivesItem(StrEnum):
    ENGAGEMENT = "ENGAGEMENT"
    PLAYS = "PLAYS"

    def __str__(self) -> str:
        return str(self.value)
