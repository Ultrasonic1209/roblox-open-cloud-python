from enum import StrEnum


class PaymentActivityType(StrEnum):
    AD_CREDIT_GRANT = "AD_CREDIT_GRANT"
    AD_CREDIT_SPEND = "AD_CREDIT_SPEND"
    CHARGE = "CHARGE"
    REFUND = "REFUND"
    ROBUX_CONVERSION = "ROBUX_CONVERSION"

    def __str__(self) -> str:
        return str(self.value)
