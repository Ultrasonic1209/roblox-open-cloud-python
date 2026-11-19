from enum import StrEnum


class BillingAccountOptionPaymentStatusReason(StrEnum):
    ACCOUNT_DISABLED = "ACCOUNT_DISABLED"
    NO_PAYMENT_METHOD = "NO_PAYMENT_METHOD"
    PROFILE_NOT_VERIFIED = "PROFILE_NOT_VERIFIED"
    TRANSACTION_FAILURE = "TRANSACTION_FAILURE"

    def __str__(self) -> str:
        return str(self.value)
