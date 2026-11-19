from enum import StrEnum


class PaymentMethodVerificationState(StrEnum):
    CHALLENGE_PENDING = "CHALLENGE_PENDING"
    UNVERIFIED = "UNVERIFIED"
    VERIFIED = "VERIFIED"

    def __str__(self) -> str:
        return str(self.value)
