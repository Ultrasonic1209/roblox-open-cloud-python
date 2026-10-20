from enum import StrEnum


class InternalPublicV1CampaignStatusDeliveryStatusReasonsItem(StrEnum):
    AUTO_PAUSED = "AUTO_PAUSED"
    CANCELLED = "CANCELLED"
    CLICK_BAIT = "CLICK_BAIT"
    COMPLETED = "COMPLETED"
    EXPIRED = "EXPIRED"
    GAME_FILTERED = "GAME_FILTERED"
    INACTIVE = "INACTIVE"
    LEARNING = "LEARNING"
    MODERATED = "MODERATED"
    PAUSED = "PAUSED"
    PLACE_JOIN_RESTRICTED = "PLACE_JOIN_RESTRICTED"
    PRIVATE = "PRIVATE"
    SCHEDULED = "SCHEDULED"

    def __str__(self) -> str:
        return str(self.value)
