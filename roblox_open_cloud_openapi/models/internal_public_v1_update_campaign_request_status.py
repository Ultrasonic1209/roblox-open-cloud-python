from enum import Enum


class InternalPublicV1UpdateCampaignRequestStatus(str, Enum):
    ACTIVE = "ACTIVE"
    CANCELLED = "CANCELLED"
    PAUSED = "PAUSED"

    def __str__(self) -> str:
        return str(self.value)
