from enum import StrEnum


class RobloxGameInternationalizationApiMediaAssetResponseState(StrEnum):
    APPROVED = "Approved"
    ERROR = "Error"
    PENDINGREVIEW = "PendingReview"
    REJECTED = "Rejected"
    UNAVAILABLE = "UnAvailable"

    def __str__(self) -> str:
        return str(self.value)
