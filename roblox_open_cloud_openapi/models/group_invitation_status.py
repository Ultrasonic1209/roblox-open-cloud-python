from enum import Enum


class GroupInvitationStatus(str, Enum):
    ACCEPTED = "Accepted"
    DECLINED = "Declined"
    DELETED = "Deleted"
    OPEN = "Open"

    def __str__(self) -> str:
        return str(self.value)
