from enum import StrEnum


class HoldState(StrEnum):
    ACCEPTED = "Accepted"
    CANCELED = "Canceled"
    COMPLETED = "Completed"
    FAILED = "Failed"
    INVALID = "Invalid"
    PENDING = "Pending"
    REJECTED = "Rejected"
    TIMEDOUT = "Timedout"

    def __str__(self) -> str:
        return str(self.value)
