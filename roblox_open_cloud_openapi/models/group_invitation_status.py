from enum import StrEnum


class GroupInvitationStatus(StrEnum):
    ACCEPTED = "Accepted"
    DECLINED = "Declined"
    DELETED = "Deleted"
    OPEN = "Open"

    def __str__(self) -> str:
        return str(self.value)
