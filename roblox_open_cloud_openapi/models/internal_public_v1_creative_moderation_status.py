from enum import Enum


class InternalPublicV1CreativeModerationStatus(str, Enum):
    APPROVED = "APPROVED"
    PENDING_REVIEW = "PENDING_REVIEW"
    REJECTED = "REJECTED"

    def __str__(self) -> str:
        return str(self.value)
