from enum import Enum


class ThumbnailsApiRobloxWebResponsesThumbnailsThumbnailResponseState(str, Enum):
    BLOCKED = "Blocked"
    COMPLETED = "Completed"
    ERROR = "Error"
    INREVIEW = "InReview"
    PENDING = "Pending"
    TEMPORARILYUNAVAILABLE = "TemporarilyUnavailable"

    def __str__(self) -> str:
        return str(self.value)
