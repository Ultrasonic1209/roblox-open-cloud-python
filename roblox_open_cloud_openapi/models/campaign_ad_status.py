from enum import StrEnum


class CampaignAdStatus(StrEnum):
    ACTIVE = "ACTIVE"
    PAUSED = "PAUSED"
    REMOVED = "REMOVED"

    def __str__(self) -> str:
        return str(self.value)
