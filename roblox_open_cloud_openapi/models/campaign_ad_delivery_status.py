from enum import StrEnum


class CampaignAdDeliveryStatus(StrEnum):
    IN_REVIEW = "IN_REVIEW"
    NOT_SERVING = "NOT_SERVING"
    REJECTED = "REJECTED"
    SERVING = "SERVING"

    def __str__(self) -> str:
        return str(self.value)
