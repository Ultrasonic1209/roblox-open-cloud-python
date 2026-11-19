from enum import StrEnum


class PaymentActivityState(StrEnum):
    FAILED = "FAILED"
    PENDING = "PENDING"
    REVERSED = "REVERSED"
    SUCCEEDED = "SUCCEEDED"

    def __str__(self) -> str:
        return str(self.value)
