from enum import StrEnum


class PaymentMethodStatus(StrEnum):
    ACTION_REQUIRED = "ACTION_REQUIRED"
    ACTIVE = "ACTIVE"
    DISABLED = "DISABLED"
    EXPIRED = "EXPIRED"

    def __str__(self) -> str:
        return str(self.value)
