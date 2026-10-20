from enum import StrEnum


class ServiceEfficiencyApiTransactionStatus(StrEnum):
    FAILED = "Failed"
    INVALID = "Invalid"
    PENDING = "Pending"
    SUCCESSFUL = "Successful"

    def __str__(self) -> str:
        return str(self.value)
