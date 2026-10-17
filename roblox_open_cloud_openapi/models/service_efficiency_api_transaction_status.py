from enum import Enum


class ServiceEfficiencyApiTransactionStatus(str, Enum):
    FAILED = "Failed"
    INVALID = "Invalid"
    PENDING = "Pending"
    SUCCESSFUL = "Successful"

    def __str__(self) -> str:
        return str(self.value)
