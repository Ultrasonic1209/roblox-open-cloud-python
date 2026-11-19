from enum import StrEnum


class UpdateCampaignAdRequestStatus(StrEnum):
    ACTIVE = "ACTIVE"
    PAUSED = "PAUSED"

    def __str__(self) -> str:
        return str(self.value)
