from enum import Enum


class ThumbnailPersonalizationApiModerationStatus(str, Enum):
    APPROVED = "Approved"
    REJECTED = "Rejected"
    REVIEWING = "Reviewing"
    UNSPECIFIED = "Unspecified"

    def __str__(self) -> str:
        return str(self.value)
