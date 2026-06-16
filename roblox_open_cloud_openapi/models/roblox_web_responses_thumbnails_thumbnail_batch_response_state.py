from enum import Enum


class RobloxWebResponsesThumbnailsThumbnailBatchResponseState(str, Enum):
    BLOCKED = "Blocked"
    COMPLETED = "Completed"
    ERROR = "Error"
    INREVIEW = "InReview"
    PENDING = "Pending"
    TEMPORARILYUNAVAILABLE = "TemporarilyUnavailable"

    def __str__(self) -> str:
        return str(self.value)
