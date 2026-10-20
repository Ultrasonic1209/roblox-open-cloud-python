from enum import StrEnum


class InternalPublicV1CreativeModerationStatus(StrEnum):
    APPROVED = "APPROVED"
    PENDING_REVIEW = "PENDING_REVIEW"
    REJECTED = "REJECTED"

    def __str__(self) -> str:
        return str(self.value)
