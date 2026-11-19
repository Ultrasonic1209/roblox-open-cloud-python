from enum import StrEnum


class BillingAccountPaymentStatus(StrEnum):
    ACTION_REQUIRED = "ACTION_REQUIRED"
    DISABLED = "DISABLED"
    PAST_DUE = "PAST_DUE"
    READY = "READY"

    def __str__(self) -> str:
        return str(self.value)
