from enum import StrEnum


class CampaignAdReviewStatus(StrEnum):
    APPROVED = "APPROVED"
    IN_REVIEW = "IN_REVIEW"
    REJECTED = "REJECTED"

    def __str__(self) -> str:
        return str(self.value)
