from enum import Enum


class RobloxGameInternationalizationApiGetDeveloperProductIconResponseState(str, Enum):
    APPROVED = "Approved"
    ERROR = "Error"
    PENDINGREVIEW = "PendingReview"
    REJECTED = "Rejected"
    UNAVAILABLE = "UnAvailable"

    def __str__(self) -> str:
        return str(self.value)
