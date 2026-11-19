from enum import StrEnum


class CampaignStatusStatus(StrEnum):
    ACTIVE = "ACTIVE"
    CANCELLED = "CANCELLED"
    PAUSED = "PAUSED"

    def __str__(self) -> str:
        return str(self.value)
