from enum import StrEnum


class ModerationStatus(StrEnum):
    APPROVED = "Approved"
    REJECTED = "Rejected"
    REVIEWING = "Reviewing"
    UNSPECIFIED = "Unspecified"

    def __str__(self) -> str:
        return str(self.value)
